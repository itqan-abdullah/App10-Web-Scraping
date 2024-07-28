import smtplib, ssl
import os


def send_email(message):
    host = "smtp.gmail.com"
    port = 465

    username = "rajataqqi@gmail.com"
    password = "here_goes_your_gmail_password"

    receiver = "rajataqqi@gmail.com"
    context = ssl.create_default_context()

    with smtplib.SMTP_SSL(host, port, context=context) as server:
        server.login(username, password)
        server.sendmail(username, receiver, message)

git config --global user.email "miabdullah.bsc20seecs@seecs.edu.pk"
git config --global user.name "Muhammad Itqan Abdullah"