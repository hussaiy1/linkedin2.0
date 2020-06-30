from webdriver_manager.chrome import ChromeDriverManager
from selenium import webdriver
from bs4 import BeautifulSoup

##improve efficiency!! 
# 1. Login with selenium
# 2. Get cookies 
# 3.#send cookies with request 
# 4. Make profile url





class webDriver(object):

    def __init__(self):
        self.driver = webdriver.Chrome(ChromeDriverManager().install())
        self.driver.get('https://www.linkedin.com')

    def login(self, url, userEmail, userPassword):
        self.driver.get(url)
        username = self.driver.find_element_by_name('session_key')
        password = self.driver.find_element_by_name('session_password')
        username.send_keys(userEmail)
        password.send_keys(userPassword)
        self.driver.find_element_by_xpath("//button[@class='btn__primary--large from__button--floating']").click()

    def changeURL(self, url):
        self.driver.get(url)

    def getCookie(self):
        cookies=self.driver.get_cookies()
        cookie = ''
        for i in range (len(cookies)):
            cookie += '{name}={value};'.format(
                name=cookies[i]['name'],
                value=cookies[i]['value']
            )
        return cookie
    
    def savedCookie(self):
        cookies = self.driver.get_cookies()
        return cookies

    def getURL(self):
        return(self.driver.current_url)

    def profileCount(self):
        content = self.driver.page_source.encode('utf-8').strip()
        soup = BeautifulSoup(content, "html5lib")
        headCount = soup.find('h2', attrs={'id': 'search-info'}).get_text()
        headCount = headCount.replace(" candidates", " ")
        headCount = headCount.replace(",", "")
        return(headCount)

    def publicURL(self):
        content = self.driver.page_source.encode('utf-8').strip()
        soup = BeautifulSoup(content, "html5lib")
        publicProfile = soup.find('li', attrs={'class': 'public-profile searchable'})
        if publicProfile != None:
            publicURL = publicProfile.find('a')['href']
            return publicURL
            #print(publicURL)
            #with open('profiles.txt', 'a') as f:
            #    f.write('%s\n' % publicURL)
            #    f.close()
