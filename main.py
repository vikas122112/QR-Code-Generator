import qrcode

UPI_id = input("Entrer your UPI ID = ")

#upi://pay?pa=UPI_ID&apn=NAMR&am=AMOUNT&cu=CURRENCY&tn=MESSAGE

# Defining the URL based on UPI ID and the payment app
# you can modify the URLs based on the payment app you want to use


phonepe_url = f'upi://pay?pa={UPI_id}&pn=RECIPIENT%20Name'
paytm_url = f'upi://pay?pa={UPI_id}&pn=RECIPIENT%20Name'
google_pay_url = f'upi://pay?pa={UPI_id}&pn=RECIPIENT%20Name'

# Create the QR code for each payment app
phonepe_qr = qrcode.make(phonepe_url)
paytm_qr = qrcode.make(paytm_url)
google_pay_qr = qrcode.make(google_pay_url)

# Display the QR code
phonepe_qr.show()
paytm_qr.show()
google_pay_qr.show()