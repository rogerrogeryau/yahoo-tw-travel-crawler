# -*- coding: utf-8 -*-
import scrapy
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from scrapy.selector import Selector
from scrapy.http import Request
import time
from yahoo_travel.items import YahooTravelItem


class TravelPageSpider(scrapy.Spider):
    name = 'travel_page'
    allowed_domains = ['travel.yahoo.com.tw']
    start_urls = ['http://travel.yahoo.com.tw/tagged/%E5%8F%B0%E5%8C%97?guccounter=1']
    
    def __init__(self):
    	#open browser
    	self.driver = webdriver.Firefox()
    	


    def parse(self, response):
    	#request url in variable "start_urls"
    	self.driver.get(response.url)
    	
    	#scroll to the bottom of the page for 30 times in order to fetch new posts
    	#trigger javascript to fetch content
    	for _ in range(70):
	    	#mimic the action of pressing "END" button in a physical keyboard 
	    	self.driver.find_element_by_xpath('//body').send_keys(Keys.CONTROL+Keys.END)
	    	#idle 0.5 seconds for loading new content
	    	time.sleep(0.5)
    	
    	#create instance of item, used for storing scraped data
    	item = YahooTravelItem()

    	###############################################################
    	# self.driver.close()
    	# html_source  = self.driver.body
    	# data = sel.encode('utf-8')                                   #irrelevant code snippet

    	# html = data.xpath('//text()').extract()

    	# data = sel.xpath('//*').extract()[1]
    	###############################################################

    	#all html code scraped
    	# html = self.driver.page_source


    	#all html code scraped
    	data = self.driver.execute_script("return document.body.outerHTML;")
    	#pass to Selector for xpath query
    	sel = Selector(text = data)

    	#containers for all post
    	containers = sel.xpath('//div[@class="item_block"]')
    	for container in containers:
    		# item['title'] = container.xpath('.//div[@class="item_txt"]//text()').extract()
    		
    		#post title
    		item['title'] = container.xpath('.//div[@class="item_txt"]/div[starts-with(@class,"item_topic")]//text()').extract_first()
    		#post url
    		url = container.xpath('./a/@href').extract_first()
    		abs_url = response.urljoin(url)
    		item['url'] = abs_url
    		#item of two keys is created 
    		yield item

    	# content = sel.xpath('//a//text()').extract()

    	
    	
    	#close selenium browser
    	self.driver.quit()

