import pandas as pd
from selenium import webdriver
from selenium.webdriver.firefox.options import Options
from selenium.webdriver.common.by import By


# setting selenium options
options = Options()
options.headless = True # keep selenium from opening browser window
driver = webdriver.Firefox(executable_path='PATH TO GECKODRIVER.EXE, options=options)

# import the list of urls as a dataframe
url_list = pd.read_excel('C:\users\1sled\desktop\state_list', sheet_name='Sheet1', header=0)

for ind in url_list.index:
		if (url_list['STATE'][ind] == 'California') and ('planet url_list['WEBSITE'][ind] 
