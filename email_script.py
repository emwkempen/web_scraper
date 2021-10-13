import smtplib, ssl

port = 465  # For SSL
smtp_server = "smtp.gmail.com"
sender_email = 'nc894fienjcvqieopwv@gmail.com'
password = '+zYS2gz/]e^L=UD@'
receiver_email = 'emwkempen@gmail.com'\
    , 'sietskevliet@gmail.com'

test_elem1 = 'first line'
test_elem2 = 'second line'

subject = 'New Listing'
message = f'{test_elem1} \n'\
          f'{test_elem2}'

test_message = "From: Emiel Kempi\nSubject: %s\n\n%s""" % (subject, message)


def send_email(message):
    # subject = 'Subject: New Pararius Listing!'

    # message = f'{subject} \n\n {body}'
    context = ssl.create_default_context()
    with smtplib.SMTP_SSL(smtp_server, port, context=context) as server:
        server.login(sender_email, password)
        server.sendmail(sender_email, receiver_email, message)

