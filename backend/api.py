from flask import Flask, request, jsonify
from flask_cors import CORS
from flask import Blueprint
from sqlalchemy.exc import SQLAlchemyError

from db_pool import get_db_session, create_tables
from models import CoffeeMachines, Profile

api = Blueprint('api', __name__)
CORS(api)

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///coffee_machine.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False


@api.route('/coffee_machines', methods=['GET'])
def get_coffee_machines():
    """
        Handles GET request to fetch all coffee machines from the database.

        Returns:
            A JSON response containing all coffee machines.
        """
    session = get_db_session()
    try:
        coffee_machines = session.query(CoffeeMachines).all()
        return jsonify({'coffee_machines': [machine.to_dict() for machine in coffee_machines]})
    finally:
        session.close()


@api.route('/addmachine', methods=['POST'])
def add_coffee_machine():
    """
        Handles POST request to add a new coffee machine to the database.

        Returns:
            A JSON response confirming successful addition of a coffee machine.
        """
    data = request.get_json()
    session = get_db_session()
    try:
        coffee_machine = CoffeeMachines(id=data['id'], model=data['model'], location_id=data['location_id'])
        session.add(coffee_machine)
        session.commit()
        return jsonify({'message': 'Coffee machine added successfully'})
    finally:
        session.close()


@api.route('/editmachines', methods=['POST'])
def edit_coffee_machine():
    """
        Handles POST request to update details of a specific coffee machine.

        Returns:
            A JSON response confirming successful update or an error message if any exception occurs.
        """
    data = request.get_json()
    session = get_db_session()
    try:
        coffee_machine = session.query(CoffeeMachines).get(data['id'])
        if coffee_machine is None:
            return jsonify({'message': 'Coffee machine not found'}), 404

        coffee_machine.model = data['model']
        coffee_machine.location_id = data['location_id']

        session.commit()

        return jsonify({'message': 'Coffee machine updated successfully'})
    except Exception:
        return jsonify({'message': 'An error occurred during the update'}), 500
    finally:
        session.close()


@api.route('/deletemachine/<int:id>', methods=['DELETE'])
def delete_coffee_machine(id):
    """
        Handles DELETE request to remove a specific coffee machine from the database.

        Returns:
            A JSON response confirming successful deletion of the coffee machine.
        """
    session = get_db_session()
    try:
        coffee_machine = session.query(CoffeeMachines).get(id)
        if coffee_machine is None:
            return jsonify({'message': 'Coffee machine not found'}), 404

        session.delete(coffee_machine)
        session.commit()
        return jsonify({'message': 'Coffee machine deleted successfully'})
    finally:
        session.close()


@api.route('/profileedit', methods=['POST'])
def profile_edit():
    """
    Handles POST request to update a specific user's profile details.

    Returns:
        A JSON response confirming successful profile update or an error message if any exception occurs.
    """
    data = request.get_json()
    session = get_db_session()
    try:
        profile = session.query(Profile).filter(Profile.id == data['id']).first()

        if profile is None:
            return {'message': 'Profile not found'}, 404

        profile.name = data.get('name', profile.name)
        profile.position = data.get('position', profile.position)
        profile.description = data.get('description', profile.description)
        profile.profilePicture = data.get('profilePicture', profile.profilePicture)

        session.commit()

        return {'message': 'Profile updated successfully'}, 200
    finally:
        session.close()


@api.route('/profiles/<int:id>', methods=['GET'])
def get_profile(id):
    """
        Handles GET request to fetch a specific user's profile details.

        Returns:
            A JSON response with profile details or an error message if any exception occurs.
        """
    session = get_db_session()
    try:
        profile = session.query(Profile).filter(Profile.id == id).first()

        if profile is None:
            return jsonify({'message': 'Profile not found'}), 404

        return jsonify({
            'id': profile.id,
            'name': profile.name,
            'position': profile.position,
            'description': profile.description,
            'profilePicture': profile.profilePicture if profile.profilePicture else None
        })
    except SQLAlchemyError as e:
        app.logger.error(f"Error getting profile: {e}")
        return jsonify({'message': 'There was an error processing your request'}), 500
    finally:
        session.close()


if __name__ == '__main__':
    app.register_blueprint(api)
    app.run()
