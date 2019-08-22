from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from time import sleep, strftime
from random import randint
import pandas as pd


#Change this to your own chromedriver path!
chromedriver_path = 'C:/Users/Shubham/Desktop/insta/chromedriver.exe'
webdriver = webdriver.Chrome(executable_path=chromedriver_path)
sleep(2)
webdriver.get('https://www.instagram.com/accounts/login/?source=auth_switcher')
sleep(2)


username = webdriver.find_element_by_name('username')
username.send_keys('your_username')
password = webdriver.find_element_by_name('password')
password.send_keys('your_password')


elem = webdriver.find_element_by_xpath("//button[@type='submit']")
elem.click()
sleep(2)

webdriver.get('https://www.instagram.com/accounts/access_tool/current_follow_requests')

sleep(3)

a=[];
elem= webdriver.find_element_by_xpath("//button[@type='button']")

try:
    while(elem):
        elem.click()
        sleep(2)


except:
    b1 = webdriver.find_elements_by_xpath("//div[@class='-utLf']")
    for i in b1:
        print(i.text)
        a.append(i.text)


for i in a:
    webdriver.get('https://www.instagram.com/'+ i)
    sleep(2)
    b1 = webdriver.find_element_by_xpath("//button[@class='BY3EC  _0mzm- sqdOP  L3NKy   _8A5w5    ']")
    b1.click();
    c1 = webdriver.find_element_by_xpath("//button[@class='aOOlW -Cab_   ']")
    c1.click();
    sleep(1)
    

