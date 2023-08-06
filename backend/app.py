from flask import jsonify, Flask, request
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_cors import CORS
from flask_bcrypt import Bcrypt
from models import CoffeeMachines, Employee, Users, Log
from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField
from wtforms.validators import DataRequired
from db_pool import get_db_session
from werkzeug.security import generate_password_hash, check_password_hash
import logging
import jwt
from api import api
from sqlalchemy.orm import Session
import os
from werkzeug.utils import secure_filename

app = Flask(__name__)
app.register_blueprint(api)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///coffee_machines.db '
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['UPLOAD_FOLDER'] = 'static/files'


db = SQLAlchemy(app)
migrate = Migrate(app, db)
CORS(app)
bcrypt = Bcrypt(app)


class SQLAlchemyHandler(logging.Handler):
    def __init__(self, session: Session):
        super().__init__()
        self.session = session

    def emit(self, record):
        log_entry = Log(message=self.format(record))
        self.session.add(log_entry)
        self.session.commit()


logger = logging.getLogger(__name__)
db_session = get_db_session()
handler = SQLAlchemyHandler(db_session)
formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
handler.setFormatter(formatter)
logger.addHandler(handler)


class LoginForm(FlaskForm):
    username = StringField('Username', validators=[DataRequired()])
    password = PasswordField('Password', validators=[DataRequired()])
    submit = SubmitField('Login')


@app.route('/authenticate', methods=['POST'])
def authenticate():
    """
        Authenticates a user with their username and password.
        :return: A JWT token and the user's role if the authentication is successful, otherwise a failure message.
        """
    try:
        data = request.get_json()
        username = data['username']
        password = data['password']

        with get_db_session() as session:
            user = session.query(Users).filter_by(username=username).first()
            if user and check_password_hash(user.password, password):
                access_token = jwt.encode({'username': username, 'role': user.role, 'id': user.user_id}, 'secret_key', algorithm='HS256')
                return jsonify(
                    {'result': 'success', 'access_token': access_token, 'role': user.role, 'name': user.name, 'id': user.user_id}), 200
    except Exception as e:
        logger.error(f"An error occurred during authentication: {str(e)}")

    logger.error('Error validating user: invalid credentials')
    return jsonify({'result': 'failure', 'message': 'Invalid username or password.'}), 401


@app.route('/users', methods=['GET'])
def get_users():
    """
        Retrieves all users from the database.
        :return: A JSON object containing all users.
        """
    session = get_db_session()

    try:
        users = session.query(Users).all()
        results = [
            {
                'username': users.username,
                'password': users.password
            } for users in users
        ]

        return jsonify(results)
    finally:
        session.close()


@app.route('/employees', methods=['GET'])
def get_employees():
    """
        Retrieves all employees from the database.
        :return: A JSON object containing all employees.
    """
    session = get_db_session()

    try:
        employees = session.query(Employee).all()
        results = [
            {
                'id': employees.id,
                'name': employees.name,
                'role': employees.title_id,
            } for employees in employees
        ]

        return jsonify(results)
    finally:
        session.close()


@app.route('/user', methods=['POST'])
def add_user():
    """
        Adds a new user to the database.
        :return: A success message if the user is added successfully, otherwise a failure message.
        """
    id = request.json.get('id')
    name = request.json.get('name')
    title_id = request.json.get('title_id')
    session = get_db_session()

    if id and name and title_id:
        new_user = Employee(id=id, name=name, title_id=title_id)
        session.add(new_user)
        session.commit()
        return {"message": "User added successfully!"}, 200
    else:
        return {"message": "Missing data!"}, 400


@app.route('/user/<id>', methods=['DELETE'])
def delete_user(id):
    """
        Deletes a user from the database.
        :param id: The ID of the user to delete.
        :return: A success message if the user is deleted successfully, otherwise a failure message.
    """
    session = get_db_session()
    user = session.query(Employee).get(id)

    if user:
        session.delete(user)
        session.commit()
        return {"message": "User deleted successfully!"}, 200
    else:
        return {"message": "User not found!"}, 404


@app.route('/list_machines', methods=['GET'])
def get_all_coffee_machines():
    """
        Retrieves all coffee machines from the database.
        :return: A JSON object containing all coffee machines.
        """
    db = get_db_session()

    try:

        coffee_machines = db.query(CoffeeMachines).all()

        coffee_machines_dict = [
            {
                "id": machine.id,
                "model": machine.model,
                "location_id": machine.location_id,
                "caretaker_id": machine.caretaker_id,
            }
            for machine in coffee_machines
        ]

        return jsonify(coffee_machines_dict)

    except Exception as e:
        print(f"An error occurred: {e}")
        return jsonify({"error": str(e)}), 500

    finally:
        db.close()


@app.route('/upload', methods=['POST'])
def upload_file():
    """
            Handles the file uploaded in the frontend and saves it to the server.
            :return: A String success message.
            """
    if 'file' not in request.files:
        return 'No file part'
    file = request.files['file']
    if file.filename == '':
        return 'No selected file'
    if file:
        filename = secure_filename(file.filename)
        file.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
        return 'File uploaded successfully'


@app.route('/log')
def log_message():
    """
        Logs debug, info and warning messages.
        :return: A confirmation message.
        """
    logger.debug('Debug message')
    logger.info('Info message')
    logger.warning('Warning message')

    return "Logged the messages"


@app.route('/applogs', methods=['GET'])
def get_logs():
    """
    GET endpoint for fetching all logs from the database.

    Returns:
        A JSON object containing all logs. Each log is represented by a dictionary.
    """
    db = get_db_session()

    try:
        logs = db.query(Log).all()
        results = [
            {
                'id': log.id,
                'timestamp': log.timestamp,
                'level': log.level,
                'message': log.message,
            } for log in logs
        ]

        return jsonify(results)
    finally:
        db.close()


@app.route('/test')
def create_error():
    """
        Creates an error for testing purposes.
        :return: An error message.
        """
    try:
        x = 1 / 0  # This will throw a ZeroDivisionError
    except Exception as e:
        app.logger.error(f"An error occurred: {str(e)}")
        return str(e), 500

    return "This won't be reached due to the error above"


@app.route('/password')
def pass_test():
    """
       This is a help function for testing the usage of password hashing and verification in the application,
        not meant for production.
      Returns:
           str: A formatted string displaying a plaintext password, its hashed version, and the result of the password verification.
       """
    password = 'admin'
    hashed_password = 'sha256$cCxumqcfW7M2wrGk$b79ffa34d98896fe27d1d317f8009e1e86ff7114520dc0818b9b362004134568'
    is_valid = check_password_hash(hashed_password, 'admin')

    my_password = 'admin'
    hashed_password = generate_password_hash(my_password, method='sha256')
    return f"Password: {password}<br>Hashed Password: {hashed_password} < br > Is Valid: {is_valid} "


if __name__ == '__main__':
    app.run(debug=True)
