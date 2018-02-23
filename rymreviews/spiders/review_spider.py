import scrapy
import datetime
import time as timer
from scrapy.spiders import Spider
from scrapy.selector import Selector
from datetime import date, time
from rymreviews.items import RymreviewsItem

class rymSpider(Spider):
	name = "rym"
	allowed_domains = ["rateyourmusic.com"]
	urls = []

	def start_requests(self):
		pagecounter = range(1,40)
		url_pattern = "https://rateyourmusic.com/release/album/the-beatles/a-hard-days-night-84/reviews/{page}"

		for page in pagecounter:
			self.urls.append(url_pattern.format(page=page))

		for url in self.urls:
			yield scrapy.Request(url=url, callback=self.parse)
			
	def parse(self, response):
		sel = Selector(response)
		sites = sel.xpath('.//div[@id="reviews_shell"]')
		items = []
		for site in sites:
			item = RymreviewsItem()
			print("hello")
			print(site.xpath('//div[@class="review_body "]/span').extract())
			item['review'] = site.xpath('//div[@class="review_body "]/span').extract() #rank
			print("goodbye")
			items.append(item)
		return items
		