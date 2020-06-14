from urllib.request import urlopen as uReq
from bs4 import BeautifulSoup as soup
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
import getpass
import spotipy
import spotipy.util as util
import sys

def auto_log_in(panopto_user,panopto_password):

    username = p_browser.find_element_by_id('username')
    username.send_keys(panopto_user)

    pssword = p_browser.find_element_by_id('password_label')
    pssword.send_keys(panopto_password)

    log_in = p_browser.find_element_by_id('submitButton')
    log_in.click()

#scope
scope = 'user-read-playback-state user-modify-playback-state user-read-currently-playing'

#initialise  credentials 

# if len(sys.argv) > 1:
#     s_username = sys.argv[1]
#     panopto_user = sys.argv[2]
# else:
#     print("Usage: %s username" % (sys.argv[0],))
#     sys.exit()

s_username =  ''
panopto_user = ''

panopto_password = getpass.getpass("enter Panopto Password (will be hidden): ")

#initialise links
panopto_url = input("enter panopto url: ") #enter url of panopto recording 

token = util.prompt_for_user_token(s_username,scope,client_id='',client_secret='',redirect_uri='') #Spotify authenciation 
sp = spotipy.Spotify(auth=token)

#ignore certification
options = webdriver.ChromeOptions()
options.add_argument('--ignore-certificate-errors')
options.add_argument('--ignore-ssl-errors')

#initialise browser credentials for panopto
p_browser = webdriver.Chrome("") #change path to chromedriver based on your own machine
p_browser.get((panopto_url))

#auto log into panopto
auto_log_in(panopto_user,panopto_password)

play_count = 1
pause_count = 0

while(1): #loop to check if panopto is playing
    p_html = soup(p_browser.page_source,"html.parser") #get relevant html code
    play_condition = p_html.find("div",{"id":"playButton"})

    # print(play_count,pause_count)
    
    
    if play_condition["title"] == "Play": #if panopto is paused
        
        if sp.currently_playing()['is_playing']: #if spotify is already playing , continue
            pause_count = 0
        
        elif play_count == 0:
            sp.start_playback()
            pause_count = 0
            play_count = play_count + 1
        
        elif not sp.currently_playing()['is_playing']: #if spotify and panopto are paused
            pause_count = 1



    elif play_condition["title"] == "Pause": #if panopto is not paused
        
        play_count = 0
        
        
        if pause_count == 0:

            sp.pause_playback()
            
            pause_count = pause_count + 1
