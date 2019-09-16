# -*- coding: utf-8 -*-
"""...
"""
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys


def main():
    options = webdriver.ChromeOptions()
    # options.add_argument('headless')
    options.add_argument('window-size=1920x1080')
    options.binary_location = '/usr/bin/google-chrome'
    browser = webdriver.Chrome(executable_path='/opt/google/chrome/chromedriver', chrome_options=options)
    browser.get('https://webapps1.chicago.gov/buildingrecords/home')
    agree_form = browser.find_element_by_id('agreement')
    radio1 = browser.find_element_by_xpath("//input[@id='rbnAgreement1']")
    radio1.click()
    submit_button = browser.find_element_by_xpath("//button[@id='submit']")
    submit_button.click()
    assert "Building Permit and Inspection Records" in browser.title
    text_box = browser.find_element_by_id('fullAddress')
    text_box.send_keys('1940 N WHIPPLE ST' + Keys.RETURN)
    assert 'Building Permit and Inspection Records' in browser.title
    body = browser.page_source
    return
'''
elem = browser.find_element_by_name('p')  # Find the search box
elem.send_keys('seleniumhq' + Keys.RETURN)
'''

if __name__ == '__main__':
    main()
    print('main - done')