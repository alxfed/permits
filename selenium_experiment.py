# -*- coding: utf-8 -*-
"""...
"""
from selenium import webdriver

class RunFFTests():

    def testMethod(self):
        # Initiate the driver instance
        driver = webdriver.Firefox(executable_path="./geckodriver")

        driver.get("http://www.letskodeit.com")


def main():
    """
    :return: 
    """
    ff = RunFFTests()
    ff.testMethod()
    return


if __name__ == '__main__':
    main()
    print('main - done')