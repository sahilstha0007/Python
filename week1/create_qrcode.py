import qrcode

def qr_code():
    phone_number = input("Enter the phone number:").strip()

    if phone_number:
        # Correct the text inside the QR code
        qr = qrcode.make(f"Phone number: {phone_number}")
        qr.save(f"{phone_number}.png")
        print(f"QR Code for phone number {phone_number} generated successfully")
    else:
        print("No phone number entered. Please try again.")

# Example usage:
qr_code()
