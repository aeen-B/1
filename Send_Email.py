import smtplib, ssl
from credentials import password
import random
def generate_password():
    input_1 = input("pls enter password : ")
    password_1 = ""
    for i in range(6):
        password_1 += str(random.randint(0, 9))
    return password_1
    if input_1 == password_1:
        send()
    else:
        print("password inst True ")
        input_1 = input("pls enter password : ")


port = 465  # For SSL
smtp_server = "smtp.gmail.com"
sender_email = "aeenbaggeryan@gmail.com"  # Enter your address
receiver_email = "aeenbagherian@gmail.com@gmail.com"  # Enter receiver address

def send():
    context = ssl.create_default_context()
    with smtplib.SMTP_SSL(smtp_server, port, context=context) as server:
        server.login(sender_email, password)
        server.sendmail(sender_email, receiver_email, message)

message = generate_password()