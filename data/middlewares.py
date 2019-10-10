# -*- coding: utf-8 -*-

# Define here the models for your spider middleware
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/spider-middleware.html

import scrapy
from scrapy import signals
from scrapy.http import HtmlResponse
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from time import sleep
import re

options = webdriver.ChromeOptions()
# options.add_argument('headless')
options.add_argument('window-size=1920x1080')
options.binary_location = '/usr/bin/google-chrome'
browser = webdriver.Chrome(executable_path='/opt/google/chrome/chromedriver', chrome_options=options)

class DataSpiderMiddleware(object):
    # Not all methods need to be defined. If a method is not defined,
    # scrapy acts as if the spider middleware does not modify the
    # passed objects.

    @classmethod
    def from_crawler(cls, crawler):
        # This method is used by Scrapy to create your spiders.
        s = cls()
        crawler.signals.connect(s.spider_opened, signal=signals.spider_opened)
        return s

    def process_spider_input(self, response, spider):
        # Called for each response that goes through the spider
        # middleware and into the spider.

        # Should return None or raise an exception.
        return None

    def process_spider_output(self, response, result, spider):
        # Called with the results returned from the Spider, after
        # it has processed the response.

        # Must return an iterable of Request, dict or Item objects.
        for i in result:
            yield i

    def process_spider_exception(self, response, exception, spider):
        # Called when a spider or process_spider_input() method
        # (from other spider middleware) raises an exception.

        # Should return either None or an iterable of Response, dict
        # or Item objects.
        pass

    def process_start_requests(self, start_requests, spider):
        # Called with the start requests of the spider, and works
        # similarly to the process_spider_output() method, except
        # that it doesn’t have a response associated.

        # Must return only requests (not items).
        for r in start_requests:
            yield r

    def spider_opened(self, spider):
        spider.logger.info('Spider opened: %s' % spider.name)


class DataDownloaderMiddleware(object):
    # Not all methods need to be defined. If a method is not defined,
    # scrapy acts as if the downloader middleware does not modify the
    # passed objects.

    @classmethod
    def from_crawler(cls, crawler):
        # This method is used by Scrapy to create your spiders.
        s = cls()
        crawler.signals.connect(s.spider_opened, signal=signals.spider_opened)
        return s

    def process_request(self, request, spider):
        home_url = 'https://webapps1.chicago.gov/buildingrecords'
        mls_url = 'https://connectmls3.mredllc.com'
        # Called for each request that goes through the downloader
        # middleware.
        # Must either:
        # - return None: continue processing this request
        # - or return a Response object
        # - or return a Request object
        # - or raise IgnoreRequest: process_exception() methods of
        #   installed downloader middleware will be called
        if request.url.startswith(home_url):
            address = request.cb_kwargs['full_address']
            browser.get('https://webapps1.chicago.gov/buildingrecords/home')
            radio1 = browser.find_element_by_xpath("//input[@id='rbnAgreement1']")
            radio1.click()
            submit_button = browser.find_element_by_xpath("//button[@id='submit']")
            submit_button.click()
            assert "Building Permit and Inspection Records" in browser.title
            text_box = browser.find_element_by_id('fullAddress')
            text_box.send_keys(address + Keys.RETURN)
            sleep(1)
            whre_i_am_now = browser.current_url
            body = browser.page_source
            # minify html
            body = body.replace('\t', '')
            body = body.replace('\n', '')
            body = re.sub('>\s*<', '><',body, 0, re.M)
            # minify html
            '''
            if whre_i_am_now == search_url:
                pass
            elif whre_i_am_now == not_found_url:
                self.logger.info(f'No search result for address: {address}!')
            else:
                self.logger.info('No search result, but no validation too! Something is wrong...')
            '''
            return HtmlResponse(whre_i_am_now, body=body, encoding='utf-8', request=request)
        elif request.url.startswith(mls_url):
            parameter = request.cb_kwargs['parameter']
            browser.get(request.url)
            whre_i_am_now = browser.current_url
            body = browser.page_source
            # minify html
            body = body.replace('\t', '')
            body = body.replace('\n', '')
            body = re.sub('>\s*<', '><', body, 0, re.M)
            # minify html
            return HtmlResponse(whre_i_am_now, body=body, encoding='utf-8', request=request)
        else:
            return None

    def process_response(self, request, response, spider):
        # Called with the response returned from the downloader.

        # Must either;
        # - return a Response object
        # - return a Request object
        # - or raise IgnoreRequest
        return response

    def process_exception(self, request, exception, spider):
        # Called when a download handler or a process_request()
        # (from other downloader middleware) raises an exception.

        # Must either:
        # - return None: continue processing this exception
        # - return a Response object: stops process_exception() chain
        # - return a Request object: stops process_exception() chain
        pass

    def spider_opened(self, spider):
        spider.logger.info('Spider opened: %s' % spider.name)
