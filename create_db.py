from app import app, db
from models import Major, User, Student
from werkzeug.security import generate_password_hash
import datetime as dt

# run inside the app context so SQLAlchemy connects to the right app/db
with app.app_context():
    # reset the database each time this runs
    db.drop_all()
    db.create_all()

    # add majors
    majors = [
        'Aerospace Engineering', 'Biology', 'Civil Engineering', 'Computer Science',
        'Electrical Engineering', 'Finance', 'Information Systems', 'Marketing',
        'Mechanical Engineering'
    ]
    for each_major in majors:
        print(f'{each_major} inserted into Major')
        db.session.add(Major(major=each_major))
        db.session.commit()

    # add users (username and password both = ELMS username; password is hashed)
    users = [
        {
            'username': 'ldasti',                       # ELMS username
            'email': 'ldasti@umd.edu',                  # UMD email
            'first_name': 'Laith',
            'last_name': 'Dasti',
            'password': generate_password_hash('ldasti', method='pbkdf2:sha256'),
            'role': 'STUDENT'                           # Step 3: only add as USER
        },
        {
            'username': 'manager',
            'email': 'manager@umd.edu',
            'first_name': 'Joe',
            'last_name': 'King',
            'password': generate_password_hash('managerpw', method='pbkdf2:sha256'),
            'role': 'MANAGER'
        },
        {
            'username': 'admin',
            'email': 'admin@umd.edu',
            'first_name': 'Crystal',
            'last_name': 'Ball',
            'password': generate_password_hash('adminpw', method='pbkdf2:sha256'),
            'role': 'ADMIN'
        }
    ]
    for each_user in users:
        print(f'{each_user["username"]} inserted into User')
        db.session.add(User(
            username=each_user["username"],
            email=each_user["email"],
            first_name=each_user["first_name"],
            last_name=each_user["last_name"],
            password=each_user["password"],
            role=each_user["role"]
        ))
        db.session.commit()

    print("\n Database successfully created and users inserted.")
