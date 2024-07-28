URL = "http://programmer100.pythonanywhere.com/tours/"
import requests 
import selectorlib
from send_email import send_email
import time
import sqlite3

connection = sqlite3.connect("data.db")


HEADERS = {
    'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/39.0.2171.95 Safari/537.36'}
def scrape(URL = URL):
    response = requests.get(URL,headers=HEADERS)
    source = response.text
    return source

def extract(source):
    extractor = selectorlib.Extractor.from_yaml_file("extract.yaml")
    value = extractor.extract(source)["tours"]
    return value

def send_email():
    print("Email sent!")

def store(extracted):
    row = extracted.split(",")
    row = [a.strip() for a in row] 
    #band,city,date = row
    cursor = connection.cursor()
    cursor.execute("INSERT INTO events values(?,?,?)",row)
    connection.commit()


def read_extracted(extracted):
    row = extracted.split(",")
    row = [a.strip() for a in row] 
    band,city,date = row
    
    
    cursor = connection.cursor()

    cursor.execute("SELECT * FROM events where band = ? and city = ? and date = ?",(band,city,date))
    result = cursor.fetchall()
    return result

while True:
    scraped = scrape()
    extracted = extract(scraped)
    if extracted != "No upcoming tours":
        row = read_extracted(extracted)
        print(row)
        if not row:
            #send_email(extracted)
            store(extracted)
            
    print(extracted)
    time.sleep(1)