Welcome to the QR Code Attendance System! This system automates attendance tracking using QR codes, capturing attendance data through webcam scanning and storing it in a MySQL database. It also provides functionality to export attendance data to a CSV file and send notifications via WhatsApp.

Prerequisites
Before running the application, ensure you have the following prerequisites installed:

Python 3.x: Download and install Python
OpenCV: Install using pip install opencv-python
pyzbar: Install using pip install pyzbar
mysql-connector-python: Install using pip install mysql-connector-python
pywhatkit: Install using pip install pywhatkit
pyttsx3: Install using pip install pyttsx3

Python Environment:

Ensure you have a Python environment set up on your system to execute Python scripts.
Required Python Libraries:

Make sure to have the necessary Python libraries installed. You can install them using the pip package manager.
MySQL Database Setup:

You will need access to a MySQL database. Prepare the required database credentials (hostname, username, password, and database name) to be used in the code.

make sure to update the names of the students that are to be a part of this system and make them as absent as default 

This system will detect the qrcode and scan the name in it and if the name matches it will update as present 

WhatsApp Configuration:

Obtain the WhatsApp number of the faculty member to whom attendance will be sent.
Ensure the faculty member has WhatsApp installed and configured on their device.

QR Code Generation:

QR codes for each person should be generated beforehand. Save the generated QR code images in a specific folder.
Folder Structure:

Organize the project files within a folder. Ensure the Python script, generated QR code images, and related files are properly organized.
Code Configuration:

Modify the Python script accordingly. Update the MySQL database credentials and the WhatsApp number of the faculty member within the code.
Running the Project:

Open a terminal or command prompt.
Navigate to the project folder using the appropriate commands.
Execute the Python script by running the command to start the attendance system.
Follow the on-screen instructions to take attendance using QR codes.
Additional Information:

Make sure your system has a functioning webcam for QR code scanning.
Ensure appropriate permissions are set for file and folder creation within the project directory.
Troubleshoot any errors encountered during execution by referring to error messages and seeking assistance if needed.