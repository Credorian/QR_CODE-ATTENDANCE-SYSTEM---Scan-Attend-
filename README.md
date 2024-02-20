# QR_CODE-ATTENDANCE-SYSTEM-Scan-Attend
Discover the innovative QR Code Attendance System, revolutionizing educational institutions with real-time tracking, seamless integration, and automated updates. Experience the future of attendance management today!


Import Libraries: The code begins by importing the necessary libraries. qrcode is imported to generate QR codes, and os is imported to perform file system operations.

Function Definition: The code defines a function generate_qr_code that takes two parameters: name (the data to be encoded in the QR code) and folder_path (the path to the folder where the QR code image will be saved).

QR Code Generation: Inside the generate_qr_code function, a QR code object qr is created using the QRCode class from the qrcode library. The version, error correction level, box size, and border size are specified for the QR code. The data (name) is added to the QR code using the add_data method, and the QR code is generated using the make method with the fit=True parameter to fit the QR code to the data size.

Folder Creation: The code checks if the specified folder (folder_path) exists. If the folder doesn't exist, it is created using os.makedirs(folder_path, exist_ok=True).

QR Code Image Creation: The QR code image is created using the make_image method of the qr object. The fill_color parameter specifies the color of the QR code, and the back_color parameter specifies the background color.

Save QR Code Image: The QR code image is saved in the specified folder using the save method. The os.path.join(folder_path, "qr_code.png") function constructs the full path for the QR code image, combining the folder path with the file name "qr_code.png".

Print Confirmation Message: Finally, a confirmation message is printed to indicate that the QR code has been generated successfully and saved in the specified folder.

Function Call: The function generate_qr_code is called with the name "John Doe" and the specified folder path where the QR code image will be saved.

MAKE SURE THAT YOU CREATE THE NAME IN THE QR_CODE AS SAME AS THE NAME THAT YOU ENTER IN THE ATTENDANCE_LIST DICTIONARY IN THE SCANATTEND FILE SO AS THE NAME MATCHES AND IT GETS UPDATED ALSO IN THE DB 
EVEN THE SPACES AND THE CASES






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
