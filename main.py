URL = "http://programmer100.pythonanywhere.com/tours/"
import requests 
import selectorlib
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
    with open("data.txt","a") as file:
        file.write(extracted + "\n")

def read_extracted():
    with open("data.txt","r") as file:
        content = file.read()
    return content

scraped = scrape()
extracted = extract(scraped)
if extracted != "No upcoming tours":
    if extracted not in read_extracted():
        send_email()
        store(extracted)
        
print(extracted)