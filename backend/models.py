from sqlalchemy import Column, Integer, String, ForeignKey, DateTime, Text, LargeBinary
from sqlalchemy.orm import declarative_base, relationship
from sqlalchemy import func

Base = declarative_base()


class Location(Base):
    __tablename__ = 'locations'

    id = Column(Integer, primary_key=True)
    name = Column(String, nullable=False)

    def to_dict(self):
        return {
            'LocationID': self.LocationID,
            'Address': self.Address,
            'CareTakerID': self.CareTakerID
        }


class CoffeeMachines(Base):
    __tablename__ = 'coffee_machines'

    id = Column(Integer, primary_key=True)
    model = Column(String(50), nullable=False)
    location_id = Column(String(50), nullable=False)
    caretaker_id = Column(Integer, nullable=False)

    def to_dict(self):
        return {
            "id": self.id,
            "model": self.model,
            "location_id": self.location_id,
            "caretaker_id": self.caretaker_id
        }


class DailyStatistic(Base):
    __tablename__ = 'daily_statistics'

    id = Column(Integer, primary_key=True)
    coffee_machine_id = Column(Integer, ForeignKey('coffee_machines.id'), nullable=False)
    date = Column(DateTime, nullable=False)
    cups_per_day = Column(Integer, nullable=False)
    coffee_amount = Column(Integer, nullable=False)
    chocolate_amount = Column(Integer, nullable=False)
    coffee_machine = relationship('CoffeeMachines')


class Users(Base):
    __tablename__ = 'users'
    username = Column(String, nullable=False, unique=True, primary_key=True)
    password = Column(String(100), nullable=False)
    name = Column(String(100), nullable=False)
    user_id = Column(Integer, ForeignKey('employees.id'), nullable=False)
    role = Column(String(100), nullable=False)


class Repair(Base):
    __tablename__ = 'repairs'

    id = Column(Integer, primary_key=True)
    coffee_machine_id = Column(Integer, ForeignKey('coffee_machines.id'), nullable=False)
    technician_id = Column(Integer, ForeignKey('employees.id'), nullable=False)
    repair_date = Column(DateTime, nullable=False)
    type_of_failure = Column(String, nullable=False)

    coffee_machine = relationship('CoffeeMachines')
    technician = relationship('Employee', foreign_keys=[technician_id])


class EmployeeTitle(Base):
    __tablename__ = 'employee_titles'

    id = Column(Integer, primary_key=True)
    title = Column(String, nullable=False)

    def to_dict(self):
        return {
            'EmployeeID': self.EmployeeID,
            'FirstName': self.FirstName,
            'LastName': self.LastName
        }


class Employee(Base):
    __tablename__ = 'employees'

    id = Column(Integer, primary_key=True)
    name = Column(String, nullable=False)
    title_id = Column(Integer, ForeignKey('employee_titles.id'), nullable=False)


class ErrorLog(Base):
    __tablename__ = 'error_logs'

    id = Column(Integer, primary_key=True)
    timestamp = Column(DateTime, nullable=False)
    message = Column(Text, nullable=False)
    coffee_machine_id = Column(Integer, ForeignKey('coffee_machines.id'))

    coffee_machine = relationship('CoffeeMachines')


class Profile(Base):
    __tablename__ = 'profiles'

    id = Column(Integer, primary_key=True)
    name = Column(String(500), nullable=True)
    position = Column(String(500), nullable=True)
    description = Column(String(500), nullable=True)
    profilePicture = Column(String(500), nullable=True)

    def to_dict(self):
        return {
            'id': self.id,
            'name': self.name,
            'position': self.position,
            'description': self.description,
            'profilePicture': self.profilePicture
        }


class Log(Base):
    __tablename__ = 'logs'

    id = Column(Integer, primary_key=True)
    timestamp = Column(DateTime, default=func.current_timestamp())
    level = Column(String)
    message = Column(Text)
