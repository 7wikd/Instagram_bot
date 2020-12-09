from selenium import webdriver
from selenium.webdriver.common.by import By
from time import sleep
from info import username,pw,uname
class Bot():
    def __init__(self):
        self.driver = webdriver.Chrome()
        self.uname = uname
        self.driver.get("https://instagram.com/")
        sleep(2)

    def login(self):
        self.driver.find_element_by_xpath('//button[span="Log in with Facebook"]').click()
        self.driver.find_element_by_xpath('//*[@id="email"]').send_keys(username)
        self.driver.find_element_by_xpath('//*[@id="pass"]').send_keys(pw)
        self.driver.find_element_by_xpath('//button[@type="submit"]').click()        
        sleep(15)
        self.driver.find_element_by_xpath('//button[@class="aOOlW   HoLwm "]').click()
    
    sleep(5)
    
    def post_login(self):
        #Visit your profile
        self.driver.find_element_by_xpath("//a[contains(@href,'/{}')]".format(self.uname))\
            .click()
        
        sleep(2)
        
        #Get list of followers

        self.driver.find_element_by_xpath("//a[contains(@href,'/{}/followers')]".format(self.uname)).click()
        followers = self.__get_names()
        sleep(2)
        self.driver.find_element_by_xpath('/html/body/div[4]/div/div/div[1]/div/div[2]/button').click()
        sleep(2)

        #Get list of those you follow

        self.driver.find_element_by_xpath("//a[contains(@href,'/{}/following')]".format(self.uname)).click()
        following = self.__get_names()
        sleep(2)
        self.driver.find_element_by_xpath('/html/body/div[4]/div/div/div[1]/div/div[2]/button').click()
        sleep(2)
        
        #List of people not following

        not_following_back = [user for user in following if user not in followers]
        print(not_following_back)
    
    def __get_names(self):
        sleep(2)
        scroll_box = self.driver.find_element_by_xpath("/html/body/div[4]/div/div/div[2]")
        last_ht, ht = 0, 1
        while last_ht != ht:
            last_ht = ht
            sleep(1)
            ht = self.driver.execute_script("""
                arguments[0].scrollTo(0, arguments[0].scrollHeight); 
                return arguments[0].scrollHeight;
                """, scroll_box)
        links = scroll_box.find_elements_by_tag_name('a')
        names = [name.text for name in links if name.text != '']
        return names

bot = Bot()
bot.login()
bot.post_login()