import qrcode

# Taking url as input 
upi_id = input("Enter your UPI ID: ")

# Define the payment url base on the payment app
phone_pay_url = f'upi://pay?pa={upi_id}&pn=Recipient%20Name'
paytm_url = f'upi://pay?pa={upi_id}&pn=Recipient%20Name'
google_pay_url = f'upi://pay?pa={upi_id}&pn=Recipient%20Name'

# making QR codes for each payment app
phone_pay_qr = qrcode.make(phone_pay_url)
paytm_qr = qrcode.make(paytm_url)
google_pay_qr = qrcode.make(google_pay_url)

# Saving the QR codes as images
# phone_pay_qr.save('phone_pay_qr.png')
# paytm_qr.save('paytm_qr.png')
# google_pay_qr.save('google_pay_qr.png')

# Display the QR codes
phone_pay_qr.show()
paytm_qr.show()
google_pay_qr.show()
