#!/usr/bin/env python2.7

import scrapy

class BdSpider(scrapy.spiders.Spider):
        name = "baidu"
        allow_domain = ["baidu.com"]
        start_urls = [
                "http://www.baidu.com/",
        ]
        def parse(self,response):
#                filename = response.url.split("/")[-2]
#                with open(filename,'wb') as f:
#                        f.write(response.body)
            for sel in response.xpath('//ul/li'):
               css = sel.xpath('//link[@type="text/css"]').extract()
                #title = sel.xpath('a/text()').extract()
               # link = sel.xpath('a/@href').extract()
               # desc = sel.xpath('text()').extract()
               print css
               # print title, link, desc
