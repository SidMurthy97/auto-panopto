## Introduction

This script utilises the Spotipy library (Spotify's Python library) and links it to the play/pause button on a given Panopto page. The script is meant to be used when studying, it begins Spotify playback when Panopto is paused and pauses it when Panopto is played. The script is also self restoring i.e so if both Spotify and Panopto happen to be paused at the same time, playing the Panopto video again restores the states of the counters for seamless transition between playback of Spotify and Panopto.

## Requirements

1. Python 3 or above
2. Chromedriver.exe for your vesion of chrome, the version in this repository is Chrome 80
3. Spotify premium
4. Valid credentials for Panopto 
5. Main libraries: Selenium, Spotipy, bs4 

## Set up 

1. Download Chromedriver.exe for your version of Chrome. The one in this repository is for Chrome 80. 
2. Prepare the URL for the recording you are trying to access

## Execution 

1. Execute the 'Autopto.py' script with two command line arguments, Spotify usernumber/username, Panopto username e.g Autopto.py            usernumber Panopto_username
2. This will open a new Chrome window alongside an authorisation window for Spotify. Give the Spotify API permission to access the          playback state of your spotify, then copy the redirect URL into the command line prompt. 
3. The next two prompts will be your Panopto password followed by the URL of the Panopto recording you are trying to watch 
4. The sript will automatically log you into Panopto and following successful authorisation, have access to your spotify playback
5. Once everything is loaded, you're good to go! 

## Extra Notes

1. The Spotify authorisation will ideally be only done the first time you run the script. Details will be stored in cache there after 

## Next Steps
2. Plans to make a Chrome extension for better integration with user flow. 
