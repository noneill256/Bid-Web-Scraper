# find how to get a whole column of data from openpyxl; alternatively, just use a column of it as a dataframe
# find how to insert a whole array of data into an excel sheet

""" first, just create a new sheet with the new column
	then, program this to do the subtraction stuff and add a list to the desired column """

import pandas as pd
import numpy as pd
from selenium import webdriver
from selenium.webdriver.firefox.options import Options
from selenium.webdriver.common.by import By
from openpyxl import Workbook, load_workbook
from openpyxl.utils import get_column_letter


# setting selenium options
options = Options()
options.headless = True # keep selenium from opening browser window
driver = webdriver.Firefox(executable_path='PATH TO GECKODRIVER.EXE, options=options)

# import the list of urls as a dataframe
url_list = pd.read_excel('C:\users\1sled\desktop\state_list', sheet_name='Sheet1', header=0)

# import the workbook we'll be editing
# wb = load_workbook('C:\users\1sled\desktop\state_list')
# wb = wb['Sheet1']
													
# create empty lists we'll update
num_bids_list = np.array([])
old_num_bids_list = np.array([])
													 
# scroll through each url 
for ind in url_list.index:
	# if it's a CA state and a planetbid website
	if (url_list['STATE'][ind] == 'California') and ((url_list['WEBSITE'][ind]).split('/')[2] == 'www.planetbids.com'):

		# generate the full url to visit			   
		url = 'pbsystem.planetbids.com/portal/' + (url_list['WEBSITE'][ind])[-5:) + '/bo/bo-search'
		driver.get(url)
		assert 'planetbids' in driver.title

		# finding the value we want
		element = driver.find_element(By.XPATH, '/html/body/div[5]/div[2]/div[1]')
		element = element.text
		# should return 'Found # bids'

		# the current number of bids
		num_bids = element[1] # the number of bids
		num_bids_list = np.append(num_bids_list, num_bids)
	else:
		num_bids_list = np.append(num_bids_list, '')
																															 
url_list['old num of bids'] = Series(num_bids_list) # adds a column to the initial dataframe
url_list.to_excel('c:/users/1sled/desktop/updated_states_list.xlsx', index=False)																	 
																			 
 
