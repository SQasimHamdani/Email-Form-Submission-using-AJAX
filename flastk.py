# app.py
from flask import Flask, render_template, request
import psycopg2

app = Flask(__name__)

# Replace these values with your actual PostgreSQL database credentials
DATABASE_URI = "postgresql://username:password@localhost:5432/yourdatabase"

@app.route('/')
def index():
    return render_template('your_html_file.html')  # Replace with the actual HTML file path

@app.route('/receive_availability_update', methods=['POST'])
def receive_availability_update():
    try:
        conn = psycopg2.connect(DATABASE_URI)
        cursor = conn.cursor()

        # Access form data using request.form
        token = request.form['token']
        show_thank_you = request.form['show_thank_you']
        response = request.form['response']
        availability_status_id = request.form['availabilityStatusId']
        starts_in_weeks = request.form['startsInWeeks']

        # Insert data into your PostgreSQL table
        cursor.execute("INSERT INTO your_table (token, show_thank_you, response, availability_status_id, starts_in_weeks) VALUES (%s, %s, %s, %s, %s)",
                       (token, show_thank_you, response, availability_status_id, starts_in_weeks))

        conn.commit()
        return "Data successfully submitted to PostgreSQL database"
    except Exception as e:
        print(f"Error: {e}")
        return "Error submitting data to PostgreSQL database"

    finally:
        cursor.close()
        conn.close()

if __name__ == '__main__':
    app.run(debug=True)
