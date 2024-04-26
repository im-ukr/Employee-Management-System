# Employee-Management-System

This project is a simple job application management system implemented using Flask, a web framework for Python. The goal of this system is to provide basic CRUD (Create, Read, Update, Delete) functionality for managing employee data. Here's a detailed breakdown:

Flask Setup: The Flask app is created with two main routes (/data and /data/<int:id>) for handling GET requests to retrieve all employees and a specific employee by ID, respectively. Additional routes are defined for adding, updating, and deleting employees.
CORS Support: The project uses the flask_cors extension to enable Cross-Origin Resource Sharing (CORS), allowing the API to be accessed from a frontend application running on a different domain.
Data Storage: Employee data is stored in a list of dictionaries (data), which serves as a simple in-memory database for this example. In a real application, this would be replaced with a database.
API Endpoints:
GET /data: Returns a JSON response containing all employee data.
GET /data/int:id: Returns a JSON response containing the employee with the specified ID. If the employee is not found, it returns an error message.
POST /data: Adds a new employee to the database. Expects JSON data with employee details and returns a JSON response confirming the addition.
PUT /data/int:id: Updates an existing employee's information. Expects JSON data with the updated employee details and returns a JSON response confirming the update.
DELETE /data/int:id: Deletes the employee with the specified ID from the database and returns a JSON response confirming the deletion.
Frontend (HTML and JavaScript): The HTML file contains a simple user interface with buttons and forms for interacting with the API. JavaScript functions are used to send requests to the API endpoints using fetch() and display the responses on the webpage.
