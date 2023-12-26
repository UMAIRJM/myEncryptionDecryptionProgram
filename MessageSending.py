# import smtplib
# import ssl

# receiver_Email = input("Please enter receiver's email\n")
# senderEmail = input("Enter your email\n")
# password = input("Enter the password\n")

# message = input("Please write your message\n")

# messageBox = f'''
#     subject:Hello My Friend Afzal
#     {message}
# '''

# try:
#     context = ssl.create_default_context()

#     with smtplib.SMTP_SSL("smtp.gmail.com", 465, context=context) as server:
#         server.login(senderEmail, password)
#         server.sendmail(senderEmail, receiver_Email, messageBox)
# except Exception as e:
#     print(f"Error occurred: {e}")
# else:
#     print("Email sent sucessfully")


# above feature of using smtp protocol to send email is no longer supported by email services as we have hurdles
#like fill captchas and many more issue.

# so we will use Whatsapp instead


from twilio.rest import Client

account_sid = 'AC4249ed5173ea3e1fe49f482456e62acd'
auth_token = '5106bb0d135573944fe0318ac4982997'
client = Client(account_sid, auth_token)

message = client.messages.create(
    from_="whatsapp:+923431202791",  # Use double quotes here
    body="this is my trial message",
    to="whatsapp:+923264332114"      # Use double quotes here
)

print(f"Message sent with SID: {message.sid}")


#this works but it require funding to subscribe twilio accounts