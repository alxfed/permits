# -*- coding: utf-8 -*-
"""...
"""
from selenium import webdriver

class RunFFTests():

    def testMethod(self):
        # Initiate the driver instance
        # options = webdriver.ChromeOptions()
        # options.add_argument('headless')# for Firefox it is '-headless')
        driver = webdriver.Chrome(executable_path="./chromedriver") # , options=options)
        driver.get("http://www.google.com")


def main():
    """
    :return: 
    """
    ff = RunFFTests()
    ff.testMethod()
    print('ok')
    return


if __name__ == '__main__':
    main()
    print('main - done')