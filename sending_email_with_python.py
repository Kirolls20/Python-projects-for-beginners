import smtplib
import ssl
from email.message import EmailMessage

subject= input('Enter The Subject For The Email: ')
body = input("Enter The Body For The Message: ")
sender = input("Enter The Sender Email: ")
password = input('PassWord: ')
reciever= input("Enter the Receiver Email: ")

message = EmailMessage()
message['From'] = sender
message['To'] = reciever
message['Subject'] = subject

html =f"""
<html>
  <body>
    <h1>{subject}</h1>
    <p>{body}</p>
  </body>
</html>
"""
message.add_alternative(html,subtype='html')
context = ssl.create_default_context()
print('Sending...')
with smtplib.SMTP_SSL('smtp.gmail.com',465,context=context) as server:
  server.login(sender,password)
  server.sendmail(sender, reciever,message.as_string())

print("Successfully Sent!")

