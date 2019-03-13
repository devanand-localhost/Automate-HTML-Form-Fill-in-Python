# Automate Form Fill and Fetch Result using Mechanize, BeautifulSoup, re

import mechanize
from bs4 import BeautifulSoup
import re

URL = 'http://results.mmumullana.org/searchresult/27'

roll_number = 11162530

while(roll_number < 11162540):
    b = mechanize.Browser()
    b.set_handle_robots(False)
    # b.addheaders = [("User-agent","Mozilla/5.0")] #our identity 
    b.open(URL)
	
	# Select the First Form from Website
    b.select_form(nr=0)
	
	# Fill the form, with below details
    b['rollnumber'] = str(roll_number)
    b['phone_number'] = '00913326251522'
    b['email_address'] = 'nnka35as6as6co@5151asasc.com'
	
	# Send request to Server for Data
    html_data = b.submit()
	
	# Read Data coming from Server
    txt = html_data.read()

    soup = BeautifulSoup(txt, "html.parser")
	# Finding the table which has result
	
    table = soup.find('table', attrs={'class':'table'})
	
	# Fetching table Data from table
    if table:
        for data in table.find_all('td'):
            result = re.sub('[<td></td>]','',str(data))
            print(result, end = '               ')
    else:
        print("Not Found")
    
    print('\n')
    
    roll_number += 1