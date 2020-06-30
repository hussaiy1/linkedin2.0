import requests
from bs4 import BeautifulSoup
import json
from recruiter_driver import *
import time as t
from selenium import webdriver
###https: // www.linkedin.com/voyager/api/growth/normInvitations
###POST
###emberEntityName: "growth/invitation/norm-invitation"
###invitee: {, …}
###com.linkedin.voyager.growth.invitation.InviteeProfile: {
###    profileId: "ACoAABl3-LQBgY1uJ_jVVpEq0grS_fDSgIJ1ZvU"}
###profileId: "ACoAABl3-LQBgY1uJ_jVVpEq0grS_fDSgIJ1ZvU"
###message: "hi yasser how are you"
###trackingId: "7DMdvPxNSQG/afCAZy5+gA=="


#has tracking ID https://www.linkedin.com/voyager/api/identity/miniprofiles/yasser-hussain-b58123bb


headers = {
    'user-agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_13_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/84.0.4147.45 Safari/537.36',
    'accept': 'application/json, text/javascript, */*; q=0.01',
    'referer': 'https://www.linkedin.com'
    }


with open('settings/config.json') as f:
  userSettings = json.load(f)

#Set username and password
email = userSettings['user'][0]['email']
password = userSettings['user'][0]['password']


#recruiter_driver = webDriver()
##Login to Linkedin
#recruiter_driver.login(LOGIN_URL, email, password)
##get cookies
#cookie = recruiter_driver.getCookie()
#
#cookies = {
#    'cookie': cookie
#}

def login(url, userEmail, userPassword):
    driver.get(url)
    username = driver.find_element_by_name('session_key')
    password = driver.find_element_by_name('session_password')
    username.send_keys(userEmail)
    password.send_keys(userPassword)
    driver.find_element_by_xpath("//button[@class='btn__primary--large from__button--floating']").click()

HOMEPAGE_URL = 'https://www.linkedin.com'
LOGIN_URL = 'https://www.linkedin.com/login'

driver = webdriver.Chrome(ChromeDriverManager().install())
driver.get('https://www.linkedin.com')
##Login to Linkedin

login(LOGIN_URL, email, password)
t.sleep(4)
cookies = driver.get_cookies()
cookie = ''

for i in range(len(cookies)):
    if cookies[i]['name'] == 'JSESSIONID':
        cookie += '{name}={value};'.format(name=cookies[i]['name'],value=cookies[i]['value'])
    else:
        pass

cookie=cookie.split('=')[1]
cookie=cookie.replace('"','')
csrf = cookie.replace(';', '')

realCookie = ''
for i in range(len(cookies)):
    cookie += '{name}={value};'.format(
        name=cookies[i]['name'],
        value=cookies[i]['value']
        )

client = requests.Session()

headers['csrf-token']: csrf

response = client.get('https://www.linkedin.com/voyager/api/identity/miniprofiles/yasser-hussain-b58123bb', headers=headers, cookies=realCookie)

with open('output.txt', 'w') as f:
    f.write(response.text)
    f.close
