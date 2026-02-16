# Student Management API

## What is This Project?

This is a simple **Student Management System** built using Django and Django REST Framework. It's a web-based application that lets you create, view, update, and delete student records through a nice web interface or API calls.

Think of it like a digital notebook where you can store information about students - their names, ages, and what courses they're taking.

## What Can You Do With It?

### Regular Features:

- **View all students** - See a list of every student in the system
- **Add a new student** - Create a new student record by providing their information
- **View one student** - Look at the details of a specific student
- **Update a student** - Change information about an existing student
- **Delete a student** - Remove a student from the system

### Special Feature - Hardcoded Student Creation:

There's a special feature where you can create a student **without typing anything**! The information is already written in the code itself:

- **Name**: John Doe
- **Age**: 20
- **Course**: Computer Science

This is useful for testing or creating a sample student quickly.

## What Information Does Each Student Have?

Each student record contains:

- **ID** - A unique number automatically assigned
- **Name** - The student's full name
- **Age** - The student's age (must be greater than 5)
- **Course** - What subject or course they're studying

## How to Set Up and Run

### Prerequisites

Before you start, make sure you have:

- Python installed on your computer
- Django installed
- Django REST Framework installed

### Step-by-Step Setup

1. **Navigate to the project folder** in your terminal:

   ```
   cd C:\Users\chand\OneDrive\Desktop\PEPCLASS\Assignments1\Assignments1
   ```

2. **Apply database migrations** (this sets up the database):

   ```
   py manage.py migrate
   ```

3. **Start the server**:

   ```
   py manage.py runserver
   ```

4. **Open your web browser** and go to:
   ```
   http://127.0.0.1:8000/api/students/
   ```

## How to Use the API

### Using the Web Interface (Easiest Way)

1. **View All Students**:
   - Go to: `http://127.0.0.1:8000/api/students/`
   - You'll see a nice web page showing all students

2. **Add a New Student Manually**:
   - On the students page, scroll to the bottom
   - You'll see a form where you can type the student's information
   - Fill in the name, age, and course
   - Click the "POST" button

3. **Use the Hardcoded Student Feature**:
   - On the students page, look for the "Extra Actions" button
   - Click it and select "Create Hardcoded Student"
   - Click the "POST" button to automatically create a student with pre-set information
   - No need to type anything - the data is already in the code!

4. **View a Single Student**:
   - Click on any student ID in the list
   - You'll see their detailed information

5. **Update a Student**:
   - Click on a student to view their details
   - Change any information in the form
   - Click the "PUT" button to save changes

6. **Delete a Student**:
   - View a student's details
   - Click the "DELETE" button
   - Confirm the deletion

### API Endpoints (For Programmers)

If you want to use tools like Postman or write code to interact with this API:

- **GET** `/api/students/` - Get list of all students
- **POST** `/api/students/` - Create a new student (provide JSON data)
- **GET** `/api/students/{id}/` - Get details of one student
- **PUT** `/api/students/{id}/` - Update a student
- **DELETE** `/api/students/{id}/` - Delete a student
- **GET** `/api/students/create_hardcoded_student/` - See what hardcoded data will be created
- **POST** `/api/students/create_hardcoded_student/` - Create student with hardcoded data

### Example JSON Format

When creating or updating students via API, use this format:

```json
{
  "name": "Jane Smith",
  "age": 22,
  "course": "Mathematics"
}
```

## Important Rules

- **Age must be greater than 5** - The system won't accept ages of 5 or below
- **All fields are required** - You must provide name, age, and course

## Where is the Hardcoded Data?

The hardcoded student data is located in the file:

- **File**: `asso/views.py`
- **Lines**: 18-22

If you want to change what information gets created automatically, just open that file and edit the values:

```python
student_data = {
    'name': 'John Doe',      # Change this to any name
    'age': 20,               # Change this to any age (must be > 5)
    'course': 'Computer Science'  # Change this to any course
}
```

## Project Structure

```
Assignments1/
├── manage.py                 # Django management script
├── db.sqlite3               # Database file (stores all student records)
├── Assignments1/            # Main project settings
│   ├── settings.py          # Configuration
│   └── urls.py              # Main URL routing
└── asso/                    # Student app
    ├── models.py            # Student data structure definition
    ├── serializers.py       # Converts student data to/from JSON
    ├── views.py             # The logic (including hardcoded feature!)
    └── urls.py              # App-specific URL routing
```

## Technology Used

- **Django 5.2.10** - The main web framework
- **Django REST Framework** - Makes creating APIs easy
- **SQLite** - A simple database that stores all the data
- **Python** - The programming language everything is written in

## Tips for Beginners

1. **The web interface is your friend** - You don't need to know JSON or API calls to use this. Just open it in your browser!

2. **The hardcoded feature is for learning** - It shows how you can have data built into your code instead of always asking users to type it in.

3. **Experiment safely** - It's just a test database. If you mess something up, you can always delete `db.sqlite3` and run migrations again to start fresh.

4. **Watch for the age rule** - If you try to create a student with age 5 or less, you'll get an error. This is intentional!

## Common Questions

**Q: Why won't my student save?**
A: Check that the age is greater than 5 and all fields are filled in.

**Q: Where is my data stored?**
A: In the `db.sqlite3` file in the project folder.

**Q: How do I change the hardcoded student information?**
A: Open `asso/views.py` and find lines 18-22. Change the values there.

**Q: The server isn't starting. What do I do?**
A: Make sure you ran `py manage.py migrate` first, and check that no other program is using port 8000.

## Need Help?

If something isn't working:

1. Check that the server is running
2. Make sure you're using the correct URL
3. Look at the error message - it usually tells you what's wrong
4. Check that all required fields have values

---

**Happy Learning! 🎓**
