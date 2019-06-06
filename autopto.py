from urllib.request import urlopen as uReq
from bs4 import BeautifulSoup as soup
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

#initialise panopto credentials

panopto_user = input("enter Panopto User: ")
panopto_password = input("enter Panopto Password")

#initialise links
spotify_url = 'https://open.spotify.com/browse/featured#_=_'
panopto_url = input("enter panopto url: ")

#ignore certification
options = webdriver.ChromeOptions()
options.add_argument('--ignore-certificate-errors')
options.add_argument('--ignore-ssl-errors')

#initialise browser credentials for panopto
p_browser = webdriver.Chrome("C:\\Users\\murth\\OneDrive\\Documents\\Python Scripts\\automate_panopto\\chromedriver.exe")
p_browser.get((panopto_url))

#auto log into panopto
username = p_browser.find_element_by_id('username')
username.send_keys(panopto_user)

pssword = p_browser.find_element_by_id('password_label')
pssword.send_keys(panopto_password)

log_in = p_browser.find_element_by_id('submitButton')
log_in.click()

#same for spotify
s_browser = webdriver.Chrome("C:\\Users\\murth\\OneDrive\\Documents\\Python Scripts\\automate_panopto\\chromedriver.exe")
s_browser.get((spotify_url))

#set counters
play_count = 0
pause_count = 0

continue_condition = input("Log in complete? ")#condition to manually input spotify log in
#run loop to check is panopto is playing
if continue_condition:
    while(1): #loop to check if panopto is playing
        p_html = soup(p_browser.page_source,"html.parser") #get relevant html code
        play_condition = p_html.find("div",{"id":"playButton"})
        pp = s_browser.find_element_by_xpath('//*[@id="main"]/div/div[4]/div[3]/footer/div/div[2]/div/div[1]/button[3]')

        if play_condition["title"] == "Play":

            if play_count == 0:
                time.sleep(1)
                pp.click()
                pause_count = 1

            play_count = play_count + 1

        elif play_condition["title"] == "Pause":
            if pause_count == 1:
                time.sleep(1)
                pp.click()
                play_count = 0
            pause_count = pause_count + 1

        #print(play_count,pause_count,play_condition["title"])
        time.sleep(0.5)
