from recruiter_driver import *
import time as t

#recruiter_driver = webDriver()
#print(recruiter_driver.driver.get_cookies())
LOGIN_URL = 'https://www.linkedin.com/login'

class connect(object):
    def __init__(self):
        self.driver = webdriver.Chrome(ChromeDriverManager().install())
        self.driver.get('https://www.linkedin.com')

    def login(self, userEmail, userPassword):
        self.driver.get(LOGIN_URL)
        username = self.driver.find_element_by_name('session_key')
        password = self.driver.find_element_by_name('session_password')
        username.send_keys(userEmail)
        password.send_keys(userPassword)
        self.driver.find_element_by_xpath("//button[@class='btn__primary--large from__button--floating']").click()

    def redirect(self, url2):
        self.driver.get(url2)

    def souper(self, url2):
        self.driver.get(url2)
        content = self.driver.page_source.encode('utf-8').strip()
        soup = BeautifulSoup(content, "html5lib")
        connector=soup.find('button', {'class':'pv-s-profile-actions pv-s-profile-actions--connect ml2 artdeco-button artdeco-button--2 artdeco-button--primary ember-view'})
        return connector

    ##Linkedin Coonect1
    def connect1(self):
        self.driver.find_element_by_xpath("//button[@class='ml2 pv-s-profile-actions__overflow-toggle artdeco-button artdeco-button--muted artdeco-button--2 artdeco-button--secondary artdeco-dropdown__trigger artdeco-dropdown__trigger--placement-bottom ember-view']").click()
        t.sleep(2)
        self.driver.find_element_by_xpath("//div[@class='pv-s-profile-actions pv-s-profile-actions--connect pv-s-profile-actions__overflow-button full-width text-align-left artdeco-dropdown__item artdeco-dropdown__item--is-dropdown ember-view']").click()
    ##Linkedin Coonect2
    def connect2(self):
        self.driver.find_element_by_xpath("//button[@class='pv-s-profile-actions pv-s-profile-actions--connect ml2 artdeco-button artdeco-button--2 artdeco-button--primary ember-view']").click()
    ##Linkedin message
    def message(self,msg):
        self.driver.find_element_by_xpath("//button[@class='mr1 artdeco-button artdeco-button--muted artdeco-button--3 artdeco-button--secondary ember-view']").click()
        self.driver.find_element_by_name('message').send_keys(msg)
        self.driver.find_element_by_xpath("//button[@class='ml1 artdeco-button artdeco-button--3 artdeco-button--primary ember-view']").click()

    def relogin(self,usrname, pwrd):
        url = 'https://www.linkedin.com/login?fromSignIn=true&trk=guest_homepage-basic_nav-header-signin'
        self.driver.get(url)
        username = self.driver.find_element_by_id('username')
        password = self.driver.find_element_by_id('password')
        username.clear()
        username.send_keys(usrname)
        password.send_keys(pwrd)
        self.driver.find_element_by_xpath("//button[@class='btn__primary--large from__button--floating']").click()
