import json
import requests
from bs4 import BeautifulSoup
from recruiter_driver import *
import time as t
import math
from messaging import messaging
from connection_request import connect
from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import ElementNotInteractableException
from datetime import datetime
from colorama import init, Fore, Back, Style

#Define Request Headers
headers = {
    'user-agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_13_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/84.0.4147.45 Safari/537.36',
    'accept': 'application/json, text/javascript, */*; q=0.01'
    }

userAccounts=['Richard.abbott@europa-it-search.com','alidaanyalnaik@hotmail.co.uk', 'roy-khan@hotmail.com', 'aqeel_365@hotmail.com']

profile=[]
pending=[]
fail=[]

with open('message.json', 'r') as jsonf:
  text = json.load(jsonf)

## Import User Details
with open('settings/config.json') as f:
  userSettings = json.load(f)

#Set username and password
email = userSettings['user'][0]['email']
password = userSettings['user'][0]['password']

HOMEPAGE_URL = 'https://www.linkedin.com'
LOGIN_URL='https://www.linkedin.com/login'


def makeApiLink(searchHistoryId, searchCacheKey, searchRequestId, searchSessionId, linkContext, doExplain, origin, start):
    link = 'https://www.linkedin.com/recruiter/api/smartsearch?searchHistoryId={}&searchCacheKey={}&searchRequestId={}&searchSessionId={}&linkContext={}&doExplain={}&origin={}&start={}'.format(
        searchHistoryId, searchCacheKey, searchRequestId, searchSessionId, linkContext, doExplain, origin, start)
    return link


def apiLink(x):
  search_info['start'] = x
  apiLink = makeApiLink(search_info['searchHistoryId'], search_info['searchCacheKey'], search_info['searchRequestId'],
  search_info['searchSessionId'], search_info['linkContext'], search_info['doExplain'], search_info['origin'], x)
  response = client.get(apiLink, headers=headers,cookies=cookies, data=search_info)
  recruiterSearch = response.json()
  searchResults = recruiterSearch['result']['searchResults']
  for i in range(len(searchResults)):
    recruiterProfiles.append(searchResults[i]['findAuthInputModel']['asUrlParam'])

if __name__ == "__main__":
  #Open Driver
  recruiter_driver = webDriver()
  #Login to Linkedin
  recruiter_driver.login(LOGIN_URL, email, password)
  dateTimeObj = datetime.now()
  print(Fore.GREEN + '[{}] Logging into Linkedin'.format(str(dateTimeObj)))

  #Launch recruiter
  recruiter_driver.changeURL('https://www.linkedin.com/cap/dashboard/home')
  input(Fore.YELLOW + 'Please complete your search criteria in the browser window and then press Enter ')
  t.sleep(4)
  searchURL= recruiter_driver.getURL()
  t.sleep(4)
  cookie = recruiter_driver.getCookie()
  dateTimeObj = datetime.now()
  print(Fore.YELLOW + '[{}] Getting Cookie'.format(str(dateTimeObj)))

  link = searchURL.split('&')
  
  cookies = {
      'cookie': cookie
    }

  client = requests.Session()

  search_info_key = ['searchHistoryId', 'searchCacheKey', 'searchRequestId','searchSessionId', 'linkContext', 'doExplain', 'origin', 'start']
  search_info_value = []
  for i in range(len(search_info_key)):
    search_info_value.append(link[i].split('=')[1])

  search_info = {}

  for i in range(len(search_info_key)):
    search_info[search_info_key[i]] = search_info_value[i]
  
  recruiterProfiles = []

  apiLink(0)
  headcount = recruiter_driver.profileCount()
  totalPages = (int(headcount))/25

  dateTimeObj = datetime.now()
  print(Fore.YELLOW + '[{}] {} Candidates'.format(str(dateTimeObj), headcount))
  print(Fore.YELLOW + '[{}] {} Total Pages'.format(str(dateTimeObj), totalPages))

  if totalPages > 40:
    for k in range(1,39):
      apiLink(k*25)
  else:
    for k in range(1, math.ceil(totalPages)):
      apiLink(k*25)

  dateTimeObj = datetime.now()
  print(Fore.CYAN + '[{}] Getting Recruiter Profile Links'.format(str(dateTimeObj)))

  for j in range(len(recruiterProfiles)):
    link = 'https://www.linkedin.com/recruiter/profile/{}'.format(recruiterProfiles[j])
    recruiter_driver.changeURL(link)
    t.sleep(3)
    profile.append(recruiter_driver.publicURL())
    dateTimeObj = datetime.now()
    print(Fore.YELLOW + '[{}] Getting Linkedin Profile # {}'.format(str(dateTimeObj),j))
  
  accountNumb = 0
  account = userAccounts[accountNumb]
  connect=connect()
  connect.login(account, 'Europa007')

  for i in range(len(profile)):
    connect.redirect(profile[i])
    dateTimeObj = datetime.now()
    print(Fore.BLUE + '[{}] Next Profile '.format(str(dateTimeObj)))
    searchConnect=connect.souper(profile[i])
    if searchConnect != None:
      try:
        t.sleep(4)
        connect.connect2()
        connectMsg = text['jobTitle'] + '\n' + text['greeting'] + ' ' + ',\n' + text['msg']
        connect.message(connectMsg)
        dateTimeObj = datetime.now()
        print(Fore.GREEN + '[{}] Connection Sent Successfully '.format(str(dateTimeObj)))
      except NoSuchElementException:
        pending.append(profile[i])
        dateTimeObj = datetime.now()
        print(Fore.YELLOW + '[{}] Maybe Connection Request Already Sent '.format(str(dateTimeObj)))
      except ElementNotInteractableException:
        fail.append(profile[i])
        dateTimeObj = datetime.now()
        print(Fore.RED + '[{}] Failed To Connect '.format(str(dateTimeObj)))
    else:
      try:
        t.sleep(4)
        connect.connect1()
        connectMsg = text['jobTitle'] + '\n' + text['greeting'] + ' ' + ',\n' + text['msg']
        connect.message(connectMsg)
        dateTimeObj = datetime.now()
        print(Fore.GREEN + '[{}] Connection Sent Successfully '.format(str(dateTimeObj)))
      except NoSuchElementException:
        pending.append(profile[i])
        dateTimeObj = datetime.now()
        print(Fore.YELLOW + '[{}] Maybe Connection Request Already Sent '.format(str(dateTimeObj)))
      except ElementNotInteractableException:
        fail.append(profile[i])
        dateTimeObj = datetime.now()
        print(Fore.RED + '[{}] Failed To Connect '.format(str(dateTimeObj)))

    if accountCounter%100==0:
      accountNumb +=1

      if accountNumb == (len(userAccounts)):
        accountNumb = 0
      
      account= userAccounts[accountNumb]
      dateTimeObj = datetime.now()
      print(Fore.CYAN + '[{}] Changing Account to {} '.format(str(dateTimeObj), account))
      connect.relogin(userAccounts[accountNumb], 'Europa007')

      t.sleep(2)
    else:
      pass
dateTimeObj = datetime.now()
print(Fore.GREEN + '[{}] Process Complete '.format(str(dateTimeObj)))



#has tracking ID https://www.linkedin.com/voyager/api/identity/miniprofiles/yasser-hussain-b58123bb
