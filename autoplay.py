from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
gmail =  input("Enter your email: ")
password = input("Enter your password:")
PATH = "C:\\Users\NameOfUser\Desktop\chromedriver.exe" # Varies where you need downloaded the chrome driver and change this to your specific directory.
browser = webdriver.Chrome(PATH)
browser.get('https://accounts.google.com/signin/v2/identifier?service=youtube&uilel=3&passive=true&continue=https%3A%2F%2Fwww.youtube.com%2Fsignin%3Faction_handle_signin%3Dtrue%26app%3Ddesktop%26hl%3Den%26next%3Dhttps%253A%252F%252Fwww.youtube.com%252F&hl=en&ec=65620&flowName=GlifWebSignIn&flowEntry=ServiceLogin')

s = browser.find_element_by_tag_name('input')
s.send_keys(gmail)
s.send_keys(Keys.ENTER)
time.sleep(8)

s = browser.find_element_by_name('password')
s.click()
s.send_keys(password)
s.send_keys(Keys.ENTER)
time.sleep(8)

l = browser.find_element_by_link_text('Library')
l.click() #Library
time.sleep(8)

wl = browser.find_element_by_link_text('Watch later')
wl.click() #Watch later
time.sleep(10)
elements = browser.find_elements_by_tag_name('button')
pa = ''
for element in elements:
    if(element.get_attribute('aria-label') =='Shuffle play'):
        pa = element
pa.click() # Play All
