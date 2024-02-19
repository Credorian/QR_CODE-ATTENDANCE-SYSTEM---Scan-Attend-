import cv2
from pyzbar.pyzbar import decode
import time
import mysql.connector
import datetime
import csv
import pywhatkit
import pyttsx3

# Initialize text-to-speech engine
engine = pyttsx3.init()
voices = engine.getProperty("voices")
engine.setProperty("voice", voices[1].id)

# Function to count occurrences of a value in a dictionary
def countVal(dict, value):
    count = 0
    for keys, values in dict.items():
        if values == value:
            count += 1
    return count

# Connect to MySQL database
mydb = mysql.connector.connect(
    host="hostname",
    user="username",
    password="pwd",
    database="DB name"
)
mycursor = mydb.cursor()

# Create a table to store attendance data if not exists
mycursor.execute("CREATE TABLE IF NOT EXISTS Attendance (name VARCHAR(255), attendance VARCHAR(255), date DATE)")

# Open webcam
cap = cv2.VideoCapture(0)
delay_time = 1

# Initialize attendance variables
attendance_list = {'Name': 'Absent', 'Name2': 'Absent', 'Name3': 'Absent'}
present_count = 0
absent_count = 0

# Loop to capture frames and process QR codes
while True:
    ret, frame = cap.read()
    qr_codes = decode(frame)

    if len(qr_codes) > 0:
        qr_code = qr_codes[0]
        name = qr_code.data.decode('utf-8')
        if name in attendance_list:
            attendance_list[name] = 'Present'
            present_count += 1
        else:
            attendance_list[name] = 'Absent'
            absent_count += 1

        # Insert attendance data into MySQL table
        sql = "INSERT INTO Attendance (name, attendance, date) VALUES (%s, %s, %s)"
        val = (name, attendance_list[name], datetime.date.today())
        mycursor.execute(sql, val)
        mydb.commit()

        time.sleep(delay_time)

    cv2.imshow('Attendance', frame)

    # Press 'q' to exit the loop
    if cv2.waitKey(1) & 0xFF == ord('q'):
        absent_count = countVal(attendance_list, "Absent")
        break

# Release webcam and close windows
cap.release()
cv2.destroyAllWindows()

# Print attendance counts
print('Total present:', present_count)
print('Total absent:', absent_count)

# Create a CSV file to store attendance data
with open('attendance.csv', mode='w', newline='') as file:
    writer = csv.writer(file)
    writer.writerow(['Name', 'Attendance', 'Date'])
    for name, attendance in attendance_list.items():
        writer.writerow([name, attendance, datetime.date.today()])

# Send attendance list to a WhatsApp number using pywhatkit
present_list = [name for name, attendance in attendance_list.items() if attendance == 'Present']
message = 'The following students are present: ' + ', '.join(present_list)

# Text-to-speech feedback
text2 = "The attendance has been taken for which subject"
engine.say(text2)
engine.runAndWait()
subject = input("The attendance has been taken for which subject: ")
text3 = "On which day"
engine.say(text3)
engine.runAndWait()
day = input("On which day: ")
text4 = "Attendance has been taken and it will be sent to the concerned faculties"
engine.say(text4)
engine.runAndWait()

# Send WhatsApp message based on subject and day
if subject == "cse" and day == "tuesday":
    pywhatkit.sendwhatmsg('FACULTY WHATSAPP NUM', message, 15, 10)
elif subject == "eee":
    pywhatkit.sendwhatmsg('FACULTY WHATSAPP NUM', message, 22, 60)
elif subject == "chem":
    pywhatkit.sendwhatmsg('FACULTY WHATSAPP NUM', message, 22, 47)
elif subject == "mat":
    pywhatkit.sendwhatmsg('FACULTY WHATSAPP NUM', message, 22, 47)
elif subject == "mec":
    pywhatkit.sendwhatmsg('FACULTY WHATSAPP NUM', message, 22, 47)

# Text-to-speech feedback
text5 = "Let's see you in the next class"
engine.say(text5)
engine.runAndWait()
