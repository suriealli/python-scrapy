#!/usr/bin/python2.7
#encoding=utf8
import scrapy

class DmozSpider(scrapy.spiders.Spider):
	name = "dmoz"
	allow_domain = ["dmoz.org"]
	start_urls = [
		"http://www.dmoz.org/Computers/Programming/Languages/Python/Books/",
		"http://www.dmoz.org/Computers/Programming/Languages/Python/Resources/"
	]
	def parse(self,response):
            for sel in response.xpath('//ul/li'):
                title = sel.xpath('a/text()').extract()
                link = sel.xpath('a/@href').extract()
                desc = sel.xpath('text()').extract()
                print title, link, desc

#		filename = response.url.split("/")[-2]
#		with open(filename,'wb') as f:
#			f.write(response.body)
