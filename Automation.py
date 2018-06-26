import unittest
import time

from selenium import webdriver
from selenium.webdriver.support.ui import Select
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait as wait
from selenium.webdriver.support import expected_conditions as EC

class Automation(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome()
        self.driver.set_page_load_timeout(30)

    def test_buy_vvip_without_login_gopay(self):
        driver = self.driver
        #1 Visit https://neo.loket.com/widget/o8hjoycmq6yhsaj
        driver.get('https://neo.loket.com/widget/o8hjoycmq6yhsaj')
        self.assertIn('LOKET DEMO', self.driver.title)

        #2 Change language to English
        driver.find_element_by_xpath('//*[@id="main"]/div[1]/div/div[1]/a[2]').click()

        #2 Click Quantity VVIP then buy 1 ticket
        vvip = Select(driver.find_element_by_id('ticket_1625_4905'))
        vvip.select_by_value('1')
        driver.find_element_by_id('buy_ticket').click()
        self.assertIn('Next', driver.find_element_by_xpath('//*[@id="form-register"]/div/div[6]/div/div/button').text)

        #3 Insert Data
        first = driver.find_element_by_xpath('//*[@id="form-register"]/div/div[4]/div[1]/div/div[1]/div/input')
        first.send_keys('Filza')
        last = driver.find_element_by_xpath('//*[@id="form-register"]/div/div[4]/div[1]/div/div[2]/div/input')
        last.send_keys('Valorisantyo')
        email = driver.find_element_by_xpath('//*[@id="form-register"]/div/div[4]/div[2]/input')
        email.send_keys('!')
        telephone = driver.find_element_by_xpath('//*[@id="form-register"]/div/div[4]/div[3]/input')
        telephone.send_keys('083873557966')
        ktp = driver.find_element_by_xpath('//*[@id="form-register"]/div/div[4]/div[4]/input')
        ktp.send_keys('3276050408950005')
        wait(driver, 10).until(EC.element_to_be_clickable((By.XPATH,'//*[@id="form-register"]/div/div[4]/div[5]/div/div[2]/label/span'))).click()
        driver.find_element_by_xpath('//*[@id="form-register"]/div/div[6]/div/div/button').click()

        #4 Choose Gopay
        gopay = driver.find_element_by_xpath('//*[@id="payment-method"]/div[2]/div[1]/div[4]/label/span')
        gopay.click()
        wait(driver, 10).until(EC.element_to_be_clickable((By.ID, 'btn-submit'))).click()
        self.assertIn('Pay Now', driver.find_element_by_xpath('//*[@id="submit-button"]').text)

        #5 Checkout
        pay = driver.find_element_by_xpath('//*[@id="submit-button"]')
        pay.click()

    def test_buy_vvip_without_login_alfamart(self):
        driver = self.driver
        #1 Visit https://neo.loket.com/widget/o8hjoycmq6yhsaj
        driver.get('https://neo.loket.com/widget/o8hjoycmq6yhsaj')
        self.assertIn('LOKET DEMO', self.driver.title)

        #2 Change language to English
        driver.find_element_by_xpath('//*[@id="main"]/div[1]/div/div[1]/a[2]').click()

        #2 Click Quantity VVIP then buy 1 ticket
        vvip = Select(driver.find_element_by_id('ticket_1625_4905'))
        vvip.select_by_value('1')
        driver.find_element_by_id('buy_ticket').click()
        self.assertIn('Next', driver.find_element_by_xpath('//*[@id="form-register"]/div/div[6]/div/div/button').text)

        #3 Insert Data
        first = driver.find_element_by_xpath('//*[@id="form-register"]/div/div[4]/div[1]/div/div[1]/div/input')
        first.send_keys('Filza')
        last = driver.find_element_by_xpath('//*[@id="form-register"]/div/div[4]/div[1]/div/div[2]/div/input')
        last.send_keys('Valorisantyo')
        email = driver.find_element_by_xpath('//*[@id="form-register"]/div/div[4]/div[2]/input')
        email.send_keys('filza_79@yahoo.com')
        telephone = driver.find_element_by_xpath('//*[@id="form-register"]/div/div[4]/div[3]/input')
        telephone.send_keys('083873557966')
        ktp = driver.find_element_by_xpath('//*[@id="form-register"]/div/div[4]/div[4]/input')
        ktp.send_keys('3276050408950005')
        wait(driver, 10).until(EC.element_to_be_clickable((By.XPATH,'//*[@id="form-register"]/div/div[4]/div[5]/div/div[2]/label/span'))).click()
        driver.find_element_by_xpath('//*[@id="form-register"]/div/div[6]/div/div/button').click()

        #4 Choose Alfamart
        alfamart = driver.find_element_by_xpath('//*[@id="payment-method"]/div[2]/div[1]/div[7]/label/span')
        alfamart.click()
        wait(driver, 10).until(EC.element_to_be_clickable((By.ID, 'btn-submit'))).click()
        self.assertIn('Alfamart', driver.find_element_by_xpath('//*[@id="main"]/div[2]/div/div[1]/h4').text)

    def tearDown(self):
        time.sleep(5)
        self.driver.close()


if __name__ == '__main__':
    unittest.main()