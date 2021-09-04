from django.test import TestCase

from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from webdriver_manager.chrome import ChromeDriverManager


test_url = 'https://webdevblog.ru/nasledovanie'


class TestSmoke(TestCase):

    def test_input(self):
        driver = webdriver.Chrome(ChromeDriverManager().install())

        driver.get('http://localhost:8000/')
        input_url = driver.find_element_by_id('input_url')
        submit = driver.find_element_by_id('submit_form')
        
        input_url.send_keys(test_url)
        submit.send_keys(Keys.RETURN)

        assert 'Сокращенная ссылка' in driver.page_source

        driver.close()

    def test_input_negative(self):
        driver = webdriver.Chrome(ChromeDriverManager().install())

        params = ['', 'https://webdevblog.ru/', 'fffhheaeaejaekfk']
        for param in params:
            driver.get('http://localhost:8000/')
            input_url = driver.find_element_by_id('input_url')
            submit = driver.find_element_by_id('submit_form')

            input_url.send_keys(param)
            submit.send_keys(Keys.RETURN)
            assert 'Сокращенная ссылка' not in driver.page_source

        driver.close()
