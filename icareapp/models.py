from datetime import datetime
from sqlalchemy import DECIMAL, Boolean, Column, Date, ForeignKey, Integer, String, DateTime, Time
from sqlalchemy.orm import relationship, sessionmaker, registry
from sqlalchemy.ext.declarative import declarative_base
from icareapp import Base, engine
from pydantic import BaseModel


Session = sessionmaker(bind=engine)
session = Session()

mapper_registry = registry()
mapper_registry.configure()

Base = declarative_base()

from sqlalchemy import ForeignKey
from sqlalchemy.orm import relationship

class Hospital(Base):
    __tablename__="hospitals"
    
    id = Column(Integer, primary_key=True)
    name = Column(String)
    address = Column(String)
    phonenumber = Column(String)  # Changed to String for flexibility
    emailaddress = Column(String)
    state = Column(String)  # Changed to String assuming state abbreviation or name
    websitename = Column(String)
    URL = Column(String)

    doctors = relationship("Doctor", back_populates="hospital")  # Relationship with Doctor

class Staff(Base):
    __tablename__="staff"
    
    id = Column(Integer, primary_key=True)
    first_name = Column(String)
    last_name = Column(String)
    age = Column(Integer)
    gender = Column(String)
    phone_number = Column(String)  # Changed to String for flexibility
    email_address = Column(String)
    password = Column(String)
    imagename = Column(String)  # Changed to String, assuming the image path or reference
    imagedate = Column(DateTime)
    job_role_id = Column(Integer, ForeignKey('job_roles.id'))  # Foreign key relationship to Job_role table
    department_id = Column(Integer, ForeignKey('departments.id'))  # Foreign key relationship to Department table
    
    job_role = relationship("JobRole")  # Relationship with JobRole
    department = relationship("Department")  # Relationship with Department

class JobRole(Base):
    __tablename__="job_roles"
    id = Column(Integer, primary_key=True)
    speciality = Column(String)

    staff = relationship("Staff", back_populates="job_role")  # Relationship with Staff

class Patient(Base):
    __tablename__ = "patients"

    id = Column(Integer, primary_key=True)
    first_name = Column(String)
    last_name = Column(String)
    age = Column(Integer)
    date_of_birth = Column(Date)
    gender = Column(String)
    contact_number = Column(String)
    email = Column(String)
    occupation = Column(String)
    state_of_origin = Column(String)  # Changed for consistency
    nationality = Column(String)
    imagename = Column(String)  # Changed to String, assuming the image path or reference
    imagedate = Column(DateTime)
    next_of_kin_name = Column(String)  # Changed for consistency
    next_of_kin_phonenumber = Column(String)  # Changed to String for flexibility
    weight_kg = Column(DECIMAL(7, 3))
    height_meters = Column(DECIMAL(5,2))

class PatientVitalSigns(Base):
    __tablename__ = "patient_vital_signs"
    
    id = Column(Integer, primary_key=True)
    date_of_measurement = Column(DateTime)  # Changed for consistency
    time_of_measurement = Column(Time)  # Changed for consistency
    blood_pressure_systolic = Column(Integer)
    blood_pressure_diastolic = Column(Integer)
    pulse = Column(Integer)
    temperature = Column(DECIMAL(5,2))
    spO2_percentage = Column(DECIMAL(5,2))  # Changed for consistency
    respiratory_rate_bpm = Column(Integer)  # Changed for consistency
    pain_level = Column(DECIMAL(4,2))
    patient_id = Column(Integer, ForeignKey('patients.id'))  # Foreign key relationship to Patient table

    patient = relationship("Patient")  # Relationship with Patient

class Doctor(Base):
    __tablename__ = "doctors"

    id = Column(Integer, primary_key=True)
    first_name = Column(String)
    last_name = Column(String)
    specialty = Column(String)
    contact_number = Column(String)
    email = Column(String)
    hospital_id = Column(Integer, ForeignKey('hospitals.id'))  # Foreign key relationship to Hospital table

    hospital = relationship("Hospital", back_populates="doctors")  # Relationship with Hospital

class Department(Base):
    __tablename__ = "departments"
        
    id = Column(Integer, primary_key=True)
    department_name = Column(String)
    hospital_id = Column(Integer, ForeignKey('hospitals.id'))  # Foreign key relationship to Hospital table
    
    staff = relationship("Staff", back_populates="department")  # Relationship with Staff

class PatientAppointment(Base):
    __tablename__ = "patient_appointments"
    
    id = Column(Integer, primary_key=True)
    date_of_appointment = Column(DateTime)
    time_of_appointment = Column(Time)
    patient_id = Column(Integer, ForeignKey('patients.id'))  # Foreign key relationship to Patient table
    doctor_id = Column(Integer, ForeignKey('doctors.id'))  # Foreign key relationship to Doctor table
    doctor_appointment_schedule = Column(Date)
    patient_complaints = Column(String)

    patient = relationship("Patient")  # Relationship with Patient
    doctor = relationship("Doctor")  # Relationship with Doctor


class Medical_Checkup_Records(Base):
    __tablename__='medical_checkup_records'
    id = Column(Integer, primary_key=True)
    doctor_reviews = Column(String)
    drugs = Column(String)
    patient_id = Column(Integer, ForeignKey('patient.id'))
    doctor_id = Column(Integer, ForeignKey('doctor.id'))
    

class Diagnose(Base):
    __tablename__ = "diagnose"
    
    id = Column(Integer, primary_key=True)
    diagnosis_date = Column(Date)
    diagnosis_code = Column(String)
    diagnosis_description = Column(String)
    patientappointment_id = Column(Integer, ForeignKey('patientappointment.id'))
    doctor_id = Column(Integer, ForeignKey('doctor.id'))
    medical_checkup_records_id = Column(Integer, ForeignKey('medical_checkup_records.id'))
    
    patient_appointment = relationship("Patient_appointment")  # Relationship with Patient
    doctor = relationship("Doctor")  # Relationship with Doctor
    medical_checkup_records = relationship("medical_checkup_records")
    
class Billing(Base):
    __tablename__ = "billing"
    
    id = Column(Integer, primary_key=True)
    bill_date = Column(Date)
    total_amount = Column(DECIMAL(10,2))
    payment_status = Column(Date)
    payment_method = Column(String)
    billing_description = Column(String)
    patient_id = Column(Integer, ForeignKey('patient.id'))
    
    
class Payment(Base):
    __tablename__="payment"
    
    id = Column(Integer, primary_key=True)
    payment_date =Column(Date)
    amount = Column(DECIMAL(10,2))
    payment_method = Column(String)
    patient_id = Column(Integer, ForeignKey('patient.id'))
    bill_id = Column(Integer, ForeignKey('bill.id'))
    
class Receipts(Base):
    __tablename__="receipt"
    
    id = Column(Integer, primary_key=True)
    receipt_date = Column(Date)
    total_amount = Column(DECIMAL(10,2))
    payment_method = Column(String)
    notes = Column(String)
    patient_id = Column(Integer, ForeignKey('patient.id'))
    
class Room(Base):
    __tablename__="room"
    id = Column(Integer, primary_key=True)
    addmission_date = Column(Date)
    patient_id = Column(Integer, ForeignKey('patient.id'))
    staff_id = Column(Integer, ForeignKey('staff.id'))


    
    
    
