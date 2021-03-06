import unittest
import time

from selenium import webdriver
from selenium.webdriver.support.ui import Select
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
        self.assertIn('Select Category', driver.find_elements_by_xpath('//*[@id="form-user"]/div/div[1]/h3').text)

        #3 Click Quantity VVIP then buy 2 tickets
        vvip = Select(driver.find_element_by_id('ticket_1625_4905'))
        vvip.select_by_value('2')
        driver.find_element_by_id('buy_ticket').click()
        self.assertIn('Sign In', driver.find_element_by_xpath('//*[@id="form-register"]/div/div[2]/div/a').text)

        #4 Insert Data
        first = driver.find_element_by_xpath('//*[@id="form-register"]/div/div[4]/div[1]/div/div[1]/div/input')
        first.send_keys('Filza')
        last = driver.find_element_by_xpath('//*[@id="form-register"]/div/div[4]/div[1]/div/div[2]/div/input')
        last.send_keys('Valorisantyo')
        email = driver.find_element_by_xpath('//*[@id="form-register"]/div/div[4]/div[2]/input')
        email.send_keys('filza_79@yahoo.com')
        telephone = driver.find_element_by_xpath('//*[@id="form-register"]/div/div[4]/div[3]/input')
        telephone.send_keys('083873557966')
        ktp = driver.find_element_by_xpath('//*[@id="form-register"]/div/div[4]/div[4]/input')
        ktp.send_keys('123456789')
        wait(driver, 10).until(EC.element_to_be_clickable((By.XPATH,'//*[@id="form-register"]/div/div[4]/div[5]/div/div[2]/label/span'))).click()
        driver.execute_script('window.scrollTo(0, 500)')
        driver.find_element_by_xpath('//*[@id="form-register"]/div/div[6]/div/div/button').click()
        self.assertIn('Apply', driver.find_element_by_xpath('//*[@id="form-register"]/div/div[1]/div/div[2]/button').text)

        #5 Choose Gopay
        gopay = driver.find_element_by_xpath('//*[@id="payment-method"]/div[2]/div[1]/div[4]/label/span')
        gopay.click()
        driver.execute_script('window.scrollTo(0, 500)')
        time.sleep(5)
        self.assertEqual('Rp. 100.000', driver.find_element_by_xpath('//*[@id="form-register"]/div/div[4]/div/table/tbody/tr[1]/td[4]').text)
        wait(driver, 10).until(EC.element_to_be_clickable((By.ID, 'btn-submit'))).click()
        self.assertIn('Pay Now', driver.find_element_by_xpath('//*[@id="submit-button"]').text)

        #6 Checkout
        pay = driver.find_element_by_xpath('//*[@id="submit-button"]')
        pay.click()
        self.assertIn('GO-PAY Payment Instruction', driver.find_element_by_xpath('//*[@id="main"]/div[2]/div/div[1]/h4').text)

    def test_buy_vvip_without_login_alfamart(self):
        driver = self.driver
        #1 Visit https://neo.loket.com/widget/o8hjoycmq6yhsaj
        driver.get('https://neo.loket.com/widget/o8hjoycmq6yhsaj')
        self.assertIn('LOKET DEMO', self.driver.title)

        #2 Change language to English
        driver.find_element_by_xpath('//*[@id="main"]/div[1]/div/div[1]/a[2]').click()
        self.assertIn('Select Category', driver.find_elements_by_xpath('//*[@id="form-user"]/div/div[1]/h3').text)

        #3 Click Quantity VVIP 2 tickets
        vvip = Select(driver.find_element_by_id('ticket_1625_4905'))
        vvip.select_by_value('2')
        driver.find_element_by_id('buy_ticket').click()
        self.assertIn('Sign In', driver.find_element_by_xpath('//*[@id="form-register"]/div/div[2]/div/a').text)

        #4 Insert Data
        first = driver.find_element_by_xpath('//*[@id="form-register"]/div/div[4]/div[1]/div/div[1]/div/input')
        first.send_keys('Filza')
        last = driver.find_element_by_xpath('//*[@id="form-register"]/div/div[4]/div[1]/div/div[2]/div/input')
        last.send_keys('Valorisantyo')
        email = driver.find_element_by_xpath('//*[@id="form-register"]/div/div[4]/div[2]/input')
        email.send_keys('filza_79@yahoo.com')
        telephone = driver.find_element_by_xpath('//*[@id="form-register"]/div/div[4]/div[3]/input')
        telephone.send_keys('083873557966')
        ktp = driver.find_element_by_xpath('//*[@id="form-register"]/div/div[4]/div[4]/input')
        ktp.send_keys('123456789')
        wait(driver, 10).until(EC.element_to_be_clickable((By.XPATH,'//*[@id="form-register"]/div/div[4]/div[5]/div/div[2]/label/span'))).click()
        driver.execute_script('window.scrollTo(0, 500)')
        driver.find_element_by_xpath('//*[@id="form-register"]/div/div[6]/div/div/button').click()
        self.assertIn('Apply', driver.find_element_by_xpath('//*[@id="form-register"]/div/div[1]/div/div[2]/button').text)

        #5 Choose Alfamart
        alfamart = driver.find_element_by_xpath('//*[@id="payment-method"]/div[2]/div[1]/div[7]/label/span')
        alfamart.click()
        time.sleep(5)
        self.assertEqual('Rp. 100.000', driver.find_element_by_xpath('//*[@id="form-register"]/div/div[4]/div/table/tbody/tr[1]/td[4]').text)
        driver.execute_script('window.scrollTo(0, 500)')
        wait(driver, 10).until(EC.element_to_be_clickable((By.ID, 'btn-submit'))).click()
        self.assertIn('Alfamart', driver.find_element_by_xpath('//*[@id="main"]/div[2]/div/div[1]/h4').text)

    def test_for_negative_testing_gopay(self):
        driver = self.driver
        #1 Visit https://neo.loket.com/widget/o8hjoycmq6yhsaj
        driver.get('https://neo.loket.com/widget/o8hjoycmq6yhsaj')
        self.assertIn('LOKET DEMO', self.driver.title)

        #2 Change language to English
        driver.find_element_by_xpath('//*[@id="main"]/div[1]/div/div[1]/a[2]').click()
        self.assertIn('Category', driver.find_element_by_xpath('//*[@id="form-user"]/div/div[1]/h3').text)

        #3 Didn't click any ticket then click any ticket
        driver.find_element_by_id('buy_ticket').click()
        self.assertIn('choose', driver.find_element_by_xpath('//*[@id="form-user"]/div/div[1]').text)
        time.sleep(5)
        vvip = Select(driver.find_element_by_id('ticket_1625_4905'))
        vvip.select_by_value('2')
        driver.find_element_by_id('buy_ticket').click()
        wait(driver, 50)
        self.assertIn('Sign In', driver.find_element_by_xpath('//*[@id="form-register"]/div/div[2]/div/a').text)

        #4 Didn't insert first name
        last = driver.find_element_by_xpath('//*[@id="form-register"]/div/div[4]/div[1]/div/div[2]/div/input')
        last.send_keys('Valorisantyo')
        email = driver.find_element_by_xpath('//*[@id="form-register"]/div/div[4]/div[2]/input')
        email.send_keys('filza_79@yahoo.com')
        telephone = driver.find_element_by_xpath('//*[@id="form-register"]/div/div[4]/div[3]/input')
        telephone.send_keys('083873557966')
        ktp = driver.find_element_by_xpath('//*[@id="form-register"]/div/div[4]/div[4]/input')
        ktp.send_keys('123456789')
        wait(driver, 10).until(EC.element_to_be_clickable((By.XPATH,'//*[@id="form-register"]/div/div[4]/div[5]/div/div[2]/label/span'))).click()
        driver.execute_script('window.scrollTo(0, 500)')
        driver.find_element_by_xpath('//*[@id="form-register"]/div/div[6]/div/div/button').click()
        self.assertIn('Firstname', driver.find_element_by_xpath('//*[@id="form-register"]/div/div[4]/div[1]/div/div[1]/div/span').text)

        #5 Insert first name
        first = driver.find_element_by_xpath('//*[@id="form-register"]/div/div[4]/div[1]/div/div[1]/div/input')
        first.send_keys('Filza')
        time.sleep(10)
        driver.find_element_by_xpath('//*[@id="form-register"]/div/div[6]/div/div/button').click()

        #6 Choose Gopay
        gopay = driver.find_element_by_xpath('//*[@id="payment-method"]/div[2]/div[1]/div[4]/label/span')
        gopay.click()
        driver.execute_script('window.scrollTo(0, 500)')
        time.sleep(5)
        self.assertEqual('Rp. 100.000', driver.find_element_by_xpath('//*[@id="form-register"]/div/div[4]/div/table/tbody/tr[1]/td[4]').text)
        wait(driver, 10).until(EC.element_to_be_clickable((By.ID, 'btn-submit'))).click()
        self.assertIn('Pay Now', driver.find_element_by_xpath('//*[@id="submit-button"]').text)

        #7 Checkout
        pay = driver.find_element_by_xpath('//*[@id="submit-button"]')
        pay.click()
        self.assertIn('GO-PAY Payment Instruction', driver.find_element_by_xpath('//*[@id="main"]/div[2]/div/div[1]/h4').text)

    def tearDown(self):
        time.sleep(5)
        self.driver.close()


if __name__ == '__main__':
    unittest.main()