import qrcode
import os

def generate_qr_code(name, folder_path):
    # Generate QR code
    qr = qrcode.QRCode(
        version=1,
        error_correction=qrcode.constants.ERROR_CORRECT_L,
        box_size=10,
        border=4,
    )
    qr.add_data(name)
    qr.make(fit=True)

    # Create the folder if it doesn't exist
    os.makedirs(folder_path, exist_ok=True)

    # Save the QR code image in the specified folder
    qr.make_image(fill_color="black", back_color="white").save(os.path.join(folder_path, "qr_code.png"))

    print("QR code generated successfully and saved in the specified folder!")

# Define the data (name) you want to encode in the QR code
name = "STUDENT NAME"

# Specify the folder path to save the QR code image
folder_path = "/path/to/your/folder"

# Call the function to generate and save the QR code
generate_qr_code(name, folder_path)
