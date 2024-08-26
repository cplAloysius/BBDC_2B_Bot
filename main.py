from selenium import webdriver
from selenium.webdriver.common.by import By
from time import sleep
from playsound import playsound
from inputimeout import inputimeout, TimeoutOccurred
import telebot
import os

count = 0
global choice
print("Please select an option:")
print("1. Practical")
print("2. RC")
print("3. Theory")
try:
    choice = inputimeout(prompt='Enter your choice: ', timeout=10)
except TimeoutOccurred:
    choice = 1

class bbdcBot():
    def __init__(self):
        self.driver = webdriver.Chrome()

    def login(self):
        while 1:
            try:
                self.driver.get('https://info.bbdc.sg/members-login/')
                try:
                    self.driver.find_element(by=By.XPATH, value='//*[@id="details-button"]').click()
                    self.driver.find_element(by=By.XPATH, value='//*[@id="proceed-link"]').click()
                except:
                    pass

                user_box = self.driver.find_element(by=By.XPATH, value='//*[@id="txtNRIC"]')
                pw_box = self.driver.find_element(by=By.XPATH, value='//*[@id="txtPassword"]')
                login_btn = self.driver.find_element(by=By.XPATH, value='//*[@id="loginbtn"]')

                # sleep(0.5)

		#change to your bbdc username and password
                user_box.send_keys('YOUR_BBDC_USERNAME')
                pw_box.send_keys('YOUR_BBDC_PASSWORD')
                login_btn.click()
                # sleep(3)

                send_btn = self.driver.find_element(by=By.XPATH, value='//*[@id="proceed-button"]')
                send_btn.click()
                # sleep(3)

                submit_btn = self.driver.find_element(by=By.XPATH,
                                                      value='/html/body/table[2]/tbody/tr[1]/td/form/table/tbody/tr[5]/td/input')
                submit_btn.click()
                # sleep(2)
                self.driver.switch_to.default_content()
                frame = self.driver.find_element(by=By.NAME, value='leftFrame')
                self.driver.switch_to.frame(frame)

                if choice == '3':
                    self.driver.find_element(by=By.XPATH, value='/html/body/table/tbody/tr/td/table/tbody/tr[18]/td[3]/a').click()
                    self.driver.switch_to.default_content()
                    mainframe = self.driver.find_element(by=By.NAME, value='mainFrame')
                    self.driver.switch_to.frame(mainframe)
                    self.driver.find_element(by=By.XPATH, value='/html/body/table/tbody/tr/td[2]/form/table/tbody/tr[11]/td/input').click()
                    self.driver.find_element(by=By.XPATH, value='/html/body/table/tbody/tr/td[2]/form/table/tbody/tr[14]/td/input').click()

                else:
                    self.driver.find_element(by=By.XPATH,
                                            value='/html/body/table/tbody/tr/td/table/tbody/tr[14]/td[3]/a').click()
                    self.driver.switch_to.default_content()
                    mainframe = self.driver.find_element(by=By.NAME, value='mainFrame')
                    self.driver.switch_to.frame(mainframe)

                month_btn = self.driver.find_element(by=By.NAME, value='allMonth')
                month_btn.click()
                ses_btn = self.driver.find_element(by=By.NAME, value='allSes')
                ses_btn.click()
                day_btn = self.driver.find_element(by=By.NAME, value='allDay')
                day_btn.click()

                if choice == '2':
                    rc_btn = self.driver.find_element(by=By.XPATH, value='/html/body/table/tbody/tr/td[2]/form/table/tbody/tr[1]/td[2]/input[2]')
                    rc_btn.click()
                else:
                    pass

                break
            except:
                continue

    def countSlots(self):
        slot = self.driver.find_elements(by=By.NAME, value='slot')
        x = len(slot)
        return x

    def refresh(self):
        global count
        token = 'YOUR_TELEGRAM_BOT_TOKEN'
        receiver_id = YOUR_TELEGRAM_CHAT_ID
        telBot = telebot.Bot(token)
        while 1:
            try:
                search_btn = self.driver.find_element(by=By.NAME, value='btnSearch')
                search_btn.click()
                # sleep(1)
                try:
                    self.driver.switch_to.alert.accept()
                except:
                    pass

                num = self.countSlots()
                if count == 0:
                    count = num
                elif count != num:
                    playsound('alarm.caf')
                    count = num
                    table = bot.driver.find_element(by=By.XPATH,
                                                    value='/html/body/table/tbody/tr/td[2]/form/table[1]/tbody/tr[10]/td/table')
                    self.driver.execute_script("arguments[0].scrollIntoView();", table)
                    table.screenshot('table.png')
                    ROOT_DIR = os.path.realpath(os.path.join(os.path.dirname(__file__),'..'))
                    table_location = ROOT_DIR + r"/table.png"
                    telBot.send_photo(receiver_id, photo=open(table_location, 'rb'),
                                     caption='Change in available slots.')

                    try:
                        x = inputimeout(prompt='Would you like to book?(y/n): ', timeout=10)
                        if x == 'y':
                            break
                    except TimeoutOccurred:
                        pass

                sleep(60)
                try: 
                    back_btn = self.driver.find_element(by=By.XPATH, value='/html/body/table/tbody/tr/td[2]/form/table[2]/tbody/tr[1]/td[1]/input[1]')
                    back_btn.click()
                except:
                    back_btn = self.driver.find_element(by=By.XPATH, value='/html/body/table/tbody/tr/td[2]/input')
                    back_btn.click()
                # sleep(2)
            except:
                self.login()


bot = bbdcBot()
bot.login()
bot.refresh()
