from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
import time

driver = True

class Youlikehits_bot:

    def setUp(self):
        self.driver = webdriver.Chrome('./chromedriver')
    
    def __init__(self, username, password, twitter_username, twitter_password):
        self.username = username
        self.password = password
        self.twitter_username = twitter_username
        self.twitter_password = twitter_password
        self.driver = driver

    def youlikehits_login(self):
        driver = self.driver
        driver.get('https://www.youlikehits.com/login.php')
        
        try:
            username = driver.find_element_by_id('username')
            password = driver.find_element_by_id('password')
        except:
            time.sleep(3)
            username = driver.find_element_by_id('username')
            password = driver.find_element_by_id('password')
    
        username.clear()
        password.clear()
        username.send_keys(self.username)
        password.send_keys(self.password)
        password.send_keys(Keys.RETURN)
        time.sleep(1)
        
    def follow_user(self):
        driver = self.driver
        driver.get('https://www.youlikehits.com/twitter2.php')
                
        try:
            follow_button = driver.find_element_by_xpath('/html/body/div/table[2]/tbody/tr/td/table[1]/tbody/tr/td/table[3]/tbody/tr[2]/td/center/div[1]/div[1]/center/center/a[1]')
        except:
            time.sleep(3)    
            follow_button = driver.find_element_by_xpath('/html/body/div/table[2]/tbody/tr/td/table[1]/tbody/tr/td/table[3]/tbody/tr[2]/td/center/div[1]/div[1]/center/center/a[1]')
        
        follow_button.click()
        time.sleep(6)

    def twitter_login(self):
        driver = self.driver
        driver.switch_to.window(driver.window_handles[1])

        try:
            input_twitter_username = driver.find_element_by_name('session[username_or_email]')
            input_twitter_password = driver.find_element_by_name('session[password]')
        except:
            time.sleep(3)    
            input_twitter_username = driver.find_element_by_name('session[username_or_email]')
            input_twitter_password = driver.find_element_by_name('session[password]')

        input_twitter_username.send_keys(self.twitter_username)
        input_twitter_password.send_keys(self.twitter_password)
        input_twitter_password.send_keys(Keys.RETURN)

    def follow_twitter_user(self):
        driver = self.driver

        try:
            follow_twitter_button = driver.find_element_by_xpath("(//span[text()='Follow']/ancestor::div[@role='button'])[1]")
        except:
            time.sleep(3)
            follow_twitter_button = driver.find_element_by_xpath("(//span[text()='Follow']/ancestor::div[@role='button'])[1]")

        follow_twitter_button.click()
        driver.close()

    def confirm_user(self):
        driver = self.driver
        driver.switch_to.window(driver.window_handles[0])

        try:
            confirm_user_button = driver.find_element_by_xpath('/html/body/div/table[2]/tbody/tr/td/table[1]/tbody/tr/td/table[3]/tbody/tr[2]/td/center/div[1]/div[1]/center/center/a[2]')
        except:
            time.sleep(3)   
            confirm_user_button = driver.find_element_by_xpath('/html/body/div/table[2]/tbody/tr/td/table[1]/tbody/tr/td/table[3]/tbody/tr[2]/td/center/div[1]/div[1]/center/center/a[2]')

        confirm_user_button.click()
        time.sleep(1)
        driver.quit()

if __name__ == "__main__":

    username = input("Youlikehits.com Username: ")
    password = input("Youlikehits.com Password: ")
    twitter_username = input("Twitter Username: ")
    twitter_password = input("Twitter Password: ")
            
    for i in range(3):
        
        bot = Youlikehits_bot(username, password, twitter_username, twitter_password)

        bot.setUp() 
        bot.youlikehits_login()
        bot.follow_user()
        bot.twitter_login()        
        bot.follow_twitter_user()
        bot.confirm_user()
