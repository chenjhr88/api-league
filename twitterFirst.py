from bs4 import BeautifulSoup
from urllib.request import urlopen
import datetime

def tag_extractor(url, tag):

    xml_page = urlopen(url) 
    bs_obj = BeautifulSoup(xml_page, 'xml')
    
    return bs_obj.find(tag).getText()

# print(tag_extractor("http://w1.weather.gov/xml/current_obs/KORD.xml", "temp_f"))



def get_time():
    now = datetime.datetime.now() # stores current date and time into a variable
    now_string = now.strftime("%A, %B %d, %Y at %I:%M %p") # formats the date and time into a legible format
    return now_string

# print(get_time())

print("It is " + tag_extractor("http://w1.weather.gov/xml/current_obs/KORD.xml", "temp_f") + " F at " + get_time() + " at " + tag_extractor("http://w1.weather.gov/xml/current_obs/KORD.xml", "location"))