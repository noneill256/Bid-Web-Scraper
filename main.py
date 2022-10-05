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
	# if it's a CA state and a planetbid website
	if (url_list['STATE'][ind] == 'California') and ((url_list['WEBSITE'][ind]).split('/')[2] == 'www.planetbids.com'):

	# the full url to visit			   
	url = 'pbsystem.planetbids.com/portal/' + (url_list['WEBSITE'][ind])[-5:) + '/bo/bo-search'
	driver.get(url)
	assert 'planetbids' in driver.title
	
	# finding the value we want
	element = driver.find_element(By.XPATH, '/html/body/div[5]/div[2]/div[1]')
	element = element.text
	# should return 'Found # bids'
			
	num_bids = element[1] # the number of bids
																
