from flask import Flask, request, jsonify, send_from_directory
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

app = Flask(__name__)

# Update these with your SMTP details
SMTP_SERVER = 'smtp.gmail.com'
SMTP_PORT = 587
SMTP_USERNAME = 'satishbekkam9999@gmail.com'  # Replace with your Gmail
SMTP_PASSWORD = 'vyie kmgx wdye rgyq'      # Use App Password if 2FA enabled
ADMIN_EMAIL = 'satishbekkam9999@gmail.com'

@app.route('/')
def index():
    return send_from_directory('.', 'index.html')

@app.route('/index.html')
def index_html():
    return send_from_directory('.', 'index.html')

@app.route('/register', methods=['POST'])
def register():
    data = request.json
    name = data.get('name')
    mobile = data.get('mobile')
    age = data.get('age')
    institute = data.get('institute')
    course = data.get('course')
    address = data.get('address')
    room_type = data.get('roomType')
    additional_info = data.get('additionalInfo')

    subject = 'PG Hostel Registration'
    body = f"""
    Name: {name}
    Phone Number: {mobile}
    Age: {age}
    School/College/Workplace: {institute}
    Course/Occupation: {course}
    Address: {address}
    Room Preference: {room_type}
    Additional Information: {additional_info}
    """

    msg = MIMEMultipart()
    msg['From'] = SMTP_USERNAME
    msg['To'] = ADMIN_EMAIL
    msg['Subject'] = subject
    msg.attach(MIMEText(body, 'plain'))

    try:
        server = smtplib.SMTP(SMTP_SERVER, SMTP_PORT)
        server.starttls()
        server.login(SMTP_USERNAME, SMTP_PASSWORD)
        server.sendmail(SMTP_USERNAME, ADMIN_EMAIL, msg.as_string())
        server.quit()
        return jsonify({'success': True})
    except Exception as e:
        return jsonify({'success': False, 'error': str(e)}), 500

@app.route('/Webpage.html')
def webpage():
    return send_from_directory('.', 'Webpage.html')

@app.route('/register.html')
def register_html():
    return send_from_directory('.', 'register.html')

if __name__ == '__main__':
    app.run(debug=True)
