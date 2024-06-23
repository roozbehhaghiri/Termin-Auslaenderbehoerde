import os
import time
import pygame
from Driver import BrowserDriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select, WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import WebDriverException

class Robot():
    def __init__(self, browser, nationality, typOfVisa , numberOfPeople="eine Person", liveWithPartner="nein"):
        # Assigning values to each field (attribute)
        self._nationality=nationality
        self._numberOfPeople=numberOfPeople
        self._liveWithPartner=liveWithPartner
        self._terminFounded=False
        self._webBrowser=browser
        self._typeOfVisa=typOfVisa

    # Starting the WebDriver based on the selected browser
    def __starrtingWebDriver(self):
        print(os.getenv("chromeDriverPath"))
        self._driver = BrowserDriver(os.getenv("chromeDriverPath"), "chrome").get_driver() if self._webBrowser == "Chrome" else BrowserDriver(os.getenv("safariDriverPath"), "safari").get_driver()

    def __openMainWebPage(self):
        # Opening the main webpage
        self._driver.get("https://otv.verwalt-berlin.de/ams/TerminBuchen")
        # Clicking the "Termin buchen" button
        self._driver.find_element(By.XPATH, '//*[@id="mainForm"]/div/div/div/div/div/div/div/div/div/div[1]/div[1]/div[2]/a').click()
        time.sleep(1)
 
    def __agreeingWithTheCondittions(self):
        time.sleep(2)
        #Agreeing with the terms and conditions
        self._driver.find_element(By.XPATH,'//*[@id="xi-div-1"]/div[4]/label[2]/p').click()
        time.sleep(1)
        #Clicking the "Weiter" Button 
        self._driver.find_element(By.ID, 'applicationForm:managedForm:proceed').click()

    # Filling out the appointment form
    def __feelingFormTerminBuchen(self):
        time.sleep(7)
        #Selecting nationality 
        select=Select(self._driver.find_element(By.ID, 'xi-sel-400'))
        select.select_by_visible_text(self._nationality)
        time.sleep(1)
        #Selecting number of person applying for visa
        select=Select(self._driver.find_element(By.ID, 'xi-sel-422'))
        select.select_by_visible_text(self._numberOfPeople)
        time.sleep(1)
        #Selecting whether living with the Family memeber
        select=Select(self._driver.find_element(By.ID, 'xi-sel-427'))
        select.select_by_visible_text("nein")
        time.sleep(3)
        self.__selectTypeOfVisa()
        WebDriverWait(self._driver, 5).until(EC.element_to_be_clickable((By.ID, "applicationForm:managedForm:proceed"))).click()

    # Selecting type of visa based on self._typeOfVisa    
    def __selectTypeOfVisa(self):
        match self._typeOfVisa:
            case "Study-verlängerung":
                self._driver.find_element(By.XPATH,'//*[@id="xi-div-30"]/div[2]/label[1]/p').click()
                time.sleep(1)
                self._driver.find_element(By.XPATH,'//*[@id="xi-div-30"]/div[8]/div[1]/div[1]/label[1]/p').click()
                time.sleep(1)
                self._driver.find_element(By.XPATH,'//*[@id="xi-div-30"]/div[8]/div[1]/div[2]/div[1]/div[5]/label[1]').click()
            case "Study-neue":
                self._driver.find_element(By.XPATH,'//*[@id="xi-div-30"]/div[1]/label[1]/p').click()
                time.sleep(1)
                self._driver.find_element(By.XPATH,'//*[@id="xi-div-30"]/div[7]/div[1]/div[1]/label[1]/p').click()
                time.sleep(1)
                self._driver.find_element(By.XPATH,'//*[@id="xi-div-30"]/div[7]/div[1]/div[2]/div[1]/div[5]/label[1]').click()
            case "Work-Ausbildung-verlängerung":
                self._driver.find_element(By.XPATH,'//*[@id="xi-div-30"]/div[2]/label[1]/p').click()
                time.sleep(1)
                self._driver.find_element(By.XPATH,'//*[@id="xi-div-30"]/div[8]/div[1]/div[3]/label[1]/p').click()
                time.sleep(1)
                self._driver.find_element(By.XPATH,'//*[@id="xi-div-30"]/div[8]/div[1]/div[4]/div[1]/div[2]/label[1]').click()
            case "Work-Ausbildung-neue":
                self._driver.find_element(By.XPATH,'//*[@id="xi-div-30"]/div[1]/label[1]/p').click()
                time.sleep(1)
                self._driver.find_element(By.XPATH,'//*[@id="xi-div-30"]/div[7]/div[1]/div[3]/label[1]/p').click()
                time.sleep(1)
                self._driver.find_element(By.XPATH,'//**[@id="xi-div-30"]/div[7]/div[1]/div[4]/div[1]/div[2]/label[1]').click()

    # Checking if appointment selection page is reached
    def __checkForTermin(self):
        time.sleep(17)
        return ("Terminauswahl" in self._driver.title)

    def run(self):
        #Checking the webpage till an appointment is found
        while(not self._terminFounded): 
            try:
                self.__starrtingWebDriver()
                self.__openMainWebPage()
                self.__agreeingWithTheCondittions()
                self.__feelingFormTerminBuchen()
                self._terminFounded=self.__checkForTermin()            
            except (WebDriverException, Exception) as e:
                print("error:", e)
                self._terminFounded = False
            finally:
                if self._terminFounded:
                    #Playing the sound when an appointment is found
                    self.__playSound()
                    time.sleep(30)
                if self._driver:
                    self._driver.close()
                    self._driver.quit()
                    
            time.sleep(3)

    #Playing sound
    def __playSound(self):
        pygame.init()
        my_sound = pygame.mixer.Sound("/Users/roozbeh/Desktop/Termin-Berlin/alarm.wav")
        my_sound.play()
        time.sleep(my_sound.get_length())


