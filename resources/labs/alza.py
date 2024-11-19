from selenium import webdriver
from selenium.webdriver.common.by import By
import os
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

url = "https://www.alza.cz/iphone-16-pro-128gb-cerny-titan-d12541644.htm"
driver = webdriver.Chrome()
# open url
driver.get(url)
# wait for page to load
driver.implicitly_wait(3)

# find element by class name
price = driver.find_element(by=By.CLASS_NAME, value="price-box__price")
# price_xpath = driver.find_element(by=By.XPATH, value="/html/body/div[3]/div/div/div[2]/div[4]/div/div/div[3]/div[6]/div[5]/div[1]/div[1]/div[1]/div/span/span")

# print price
print(f"Price CLASS NAME: {price.text}")
# print(f"Price XPATH: {price_xpath.text}")


# get email password from environment variable
PASSWORD = os.environ.get("MAIL_PWD")


# send email function
def send_email(subject, body, sender_email, receiver_email, smtp_server, port, password):
    # Create a MIME object
    message = MIMEMultipart()
    message["From"] = sender_email
    message["To"] = receiver_email
    message["Subject"] = subject

    # Add body to email
    message.attach(MIMEText(body, 'plain'))

    # Create secure connection with server and send email
    context = smtplib.ssl.create_default_context()
    with smtplib.SMTP_SSL(smtp_server, port, context=context) as server:
        server.login(sender_email, password)
        server.sendmail(sender_email, receiver_email, message.as_string())


# Example usage
send_email(
    subject="Alza price",
    body=f"iPhone price is: {price.text}",
    sender_email="oop.email@seznam.cz",
    receiver_email="oop.email@seznam.cz",
    smtp_server="smtp.seznam.cz",
    port=465,  # commonly used port for SSL
    password=PASSWORD
)

# close browser
driver.quit()
