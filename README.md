This is a Flask web application that allows users to submit survey responses, stores the data in MongoDB, and automatically exports the stored responses to a CSV file.

## Features
User Input Form (A) - Collects user details including age, gender, income, and expenses.
MongoDB Storage - Saves submitted responses to a MongoDB database.
CSV Export -  Automatically generates a CSV file (`user_data.csv`) after each submission.
Manual CSV Export - Provides a route to manually trigger CSV generation.

## Requirements
- Python 3+
- MongoDB (Installed & Running)
- Flask
- PyMongo



## Installation Dependencies
pip install flask pymongo


## Start MongoDB
Ensure that MongoDB is running on localhost:27017


## Run the Flask Application
sh
Copy
Edit
python app.py