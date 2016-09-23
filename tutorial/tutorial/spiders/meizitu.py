#!/usr/bin/env python2.7
#encoding=utf8
import scrapy
import urllib
import sys 
from scrapy.loader import ItemLoader
from tutorial.items import MeizituItem


reload(sys) 
sys.setdefaultencoding('utf8')



class MeiziSspider(scrapy.spiders.Spider):
    name = 'meizi'
    allow_domain = ["meizitu.com"]
    start_urls = [
        "http://www.meizitu.com/",
#         "http://www.meizitu.com/a/list_1_1.html",
    ]
    
    #抓取首页
    def parse(self,response):
        try:
            #读取页面后去的总共分页数
            num_pages = int(response.xpath('//div[@id="wp_page_numbers"]//li/a//@href').extract()[-1].split("_")[-1].split(".")[0])
            print "页数:%s" %(num_pages,)
            base_url = "http://www.meizitu.com/a/list_1_{0}.html"
            #按照页数转交给scrapy.Request 分别处理
            for page in range(1,num_pages):
                yield scrapy.Request(base_url.format(page),callback = self.parse_page)
        except Exception,e:
            print "========================something Error happened:%s========================" %e
    #各分页中的内容
    def parse_page(self, response):
        for sel in response.xpath('//div[@class="pic"]'):
            href = sel.xpath('a//@href').extract()[0]
            yield scrapy.Request(href,callback = self.parse_img)
    #每个分页中有各个美女
    def parse_img(self, response):
        file_dir = '/home/suriealli/tmp/pic/'
        for img in response.xpath('//div[@id="picture"]//p/img//@src'):
            img_url = img.extract()
            file_name = img_url.split("/")[-4] + "_" + img_url.split("/")[-3] + "_" + img_url.split("/")[-2] + "_" + img_url.split("/")[-1]
            #下载
            urllib.urlretrieve(img_url, file_dir + file_name )
      
