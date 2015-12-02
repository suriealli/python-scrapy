#!/usr/bin/python2.7
#encoding=utf8

from scrapy.contrib.spiders import CrawlSpider,Rule
from scrapy.contrib.linkextractors import LinkExtractor
import scrapy


class TorrentItem(scrapy.Item):
	url = scrapy.Field()
	name = scrapy.Field()
	description = scrapy.Field()
	size = scrapy.Field()

class MininovaSpider(CrawlSpider):
	name = 'mininova'
	allow_domain = ['mininova.org']
	start_urls = ['http://www.mininova.org/today']
	rules = [Rule(LinkExtrator(allow=['/tor/\d+']),'parse_torrent')]
	def parse_torrent(self,response):
		torrent = TorrentIten()
		torrent['url'] = response.url
		torrent['name'] = response.xpath("//h1/text()").extract()
		torrent['description'] = response.xpath("//div[@id='description']").extract()
		torrent['size'] = response.xpath("//div[@id='info-left']/p[2]/text()[2]").extract()
		return torrent
