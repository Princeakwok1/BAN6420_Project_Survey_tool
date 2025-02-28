from flask import Flask, render_template, request, redirect
from pymongo import MongoClient
import csv
import os

app = Flask(__name__)

# Connect to MongoDB
client = MongoClient("mongodb://localhost:27017/")  # Update if using MongoDB Atlas
db = client["survey_db"]
collection = db["users"]

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        age = request.form['age']
        gender = request.form['gender']
        income = request.form['income']
        
        expenses = {
            "utilities": request.form.get("utilities", 0),
            "entertainment": request.form.get("entertainment", 0),
            "school_fees": request.form.get("school_fees", 0),
            "shopping": request.form.get("shopping", 0),
            "healthcare": request.form.get("healthcare", 0)
        }

        collection.insert_one({"age": age, "gender": gender, "income": income, "expenses": expenses})
        
        # Generate CSV after inserting new data
        export_to_csv()

        return redirect('/')
    
    return '''
    <form method="POST">
        Age: <input type="text" name="age" required><br>
        Gender: <input type="text" name="gender" required><br>
        Income: <input type="text" name="income" required><br>
        Utilities: <input type="text" name="utilities"><br>
        Entertainment: <input type="text" name="entertainment"><br>
        School Fees: <input type="text" name="school_fees"><br>
        Shopping: <input type="text" name="shopping"><br>
        Healthcare: <input type="text" name="healthcare"><br>
        <input type="submit" value="Submit">
    </form>
    '''

# Function to export data to CSV
def export_to_csv():
    users = list(collection.find())
    with open('user_data.csv', 'w', newline='') as file:
        writer = csv.writer(file)
        writer.writerow(["age", "gender", "income", "utilities", "entertainment", "school_fees", "shopping", "healthcare"])
        for user in users:
            writer.writerow([user["age"], user["gender"], user["income"],
                             user["expenses"].get("utilities", 0), user["expenses"].get("entertainment", 0),
                             user["expenses"].get("school_fees", 0), user["expenses"].get("shopping", 0),
                             user["expenses"].get("healthcare", 0)])

# Route to manually trigger CSV export
@app.route('/export')
def export():
    export_to_csv()
    return "CSV file has been generated!"

if __name__ == '__main__':
    export_to_csv()  # Ensure CSV is generated when the app starts
    app.run(debug=True)
