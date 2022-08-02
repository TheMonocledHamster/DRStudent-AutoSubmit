from multiprocessing.connection import wait
from statistics import mode
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
from selenium.webdriver import ActionChains
import time
import logging

class DeepRacerStudent:

    def __init__(self,config):
        self.email = config['email']
        self.password = config['password']
        self.model_recency = config['model_recency']
        self.email_name= "email"
        self.password_name = "password"
        self.login_button_id = "SignInBtn"
        self.annoy_xpath = "/html/body/div[1]/div/div[1]/div/div/div/div/button[2]"
        self.join_race_xpath = "/html/body/div[2]/div/div[2]/main/div[3]/div/div[5]/div/div/div[2]/div[2]/div[2]/div/div/div[3]/div/button"
        self.race_again_xpath = "/html/body/div[2]/div/div[2]/main/div[3]/div/div[2]/div/div/div/div[1]/div/div[1]/div[2]/div/div[2]/button"
        self.model_selection_xpath = "/html/body/div[2]/div/div[2]/main/div[3]/div/div[1]/div/div[2]/div/div/div/div[2]/div/div[2]/div/div/div[1]/button"
        self.model_xpath = "/html/body/div[2]/div/div[2]/main/div[3]/div/div[1]/div/div[2]/div/div/div/div[2]/div/div[2]/div/div/div[2]/div/div/div/ul/li[{}]".format(self.model_recency)
        self.enter_race_xpath = "/html/body/div[2]/div/div[2]/main/div[3]/div/div[2]/div/button[2]"
        
        

    def submit(self):
        try:
            self.set_up()
            self.open()
            self.login()
            self.race()
        except Exception as e:
            raise e
        finally:
            self.tear_down()


    def set_up(self):
        self.driver = webdriver.Firefox(executable_path="./driver/geckodriver.exe")
        self.actor = ActionChains(self.driver)
        self.wait = WebDriverWait(self.driver,30)


    def open(self):
        self.driver.get("https://student.deepracer.com/")
        self.wait.until(EC.element_to_be_clickable((By.ID,"SignInBtn")))


    def login(self):
        time.sleep(2)
        email_box = self.driver.find_element(By.NAME,self.email_name)
        email_box.clear()
        email_box.send_keys(self.email)
        time.sleep(2)
        password_box = self.driver.find_element(By.NAME,self.password_name)
        password_box.clear()
        password_box.send_keys(self.password)
        time.sleep(1)
        login_button = self.driver.find_element(By.ID,self.login_button_id)
        login_button.click()
        time.sleep(10)


    def race(self):
        self.wait.until(EC.element_to_be_clickable((By.XPATH,self.join_race_xpath)))
        self.driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
        try:
            self.driver.find_element(By.XPATH,self.annoy_xpath).click()
        except:
            pass
        join_button = self.driver.find_element(By.XPATH,self.join_race_xpath)
        self.actor.move_to_element(join_button)
        time.sleep(3)
        join_button.click()
        try:
            self.wait.until(EC.element_to_be_clickable((By.XPATH,self.race_again_xpath)))
        except:
            self.driver.refresh()
            time.sleep(10)
        race_button = self.driver.find_element(By.XPATH,self.race_again_xpath)
        time.sleep(3)
        race_button.click()
        self.wait.until(EC.element_to_be_clickable((By.XPATH,self.model_selection_xpath)))
        model_selection = self.driver.find_element(By.XPATH,self.model_selection_xpath)
        time.sleep(1)
        model_selection.click()
        model = self.driver.find_element(By.XPATH,self.model_xpath)
        time.sleep(1)
        model.click()
        time.sleep(2)
        race_button = self.driver.find_element(By.XPATH,self.enter_race_xpath)
        race_button.click()
        time.sleep(10)


    def tear_down(self):
        self.driver.quit()