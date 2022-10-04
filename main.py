import pandas as pd
from selenium import webdriver
from selenium.webdriver.firefox.options import Options
from selenium.webdriver.common.by import By


# setting selenium options
options = Options()
options.headless = True # keep selenium from opening browser window
driver = webdriver.Firefox(executable_path='PATH TO GECKODRIVER.EXE, options=options)

# import the list of urls
url_list = pd.read_excel('C:\users\1sled\desktop\state_list')
