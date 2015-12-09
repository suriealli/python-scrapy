#encoding=utf-8
import urllib
import requests
import random
import os
import sys 
reload(sys) 
sys.setdefaultencoding('utf-8')
from BeautifulSoup import BeautifulSoup
def getAllJsLink():
	url = 'http://www.baidu.com/'
	r = requests.get(url)
	html = r.text
	soup = BeautifulSoup(html)
	liResult = soup.findAll('script')
	for js in liResult:
		link = js.get('src')
        jsName = random.uniform(10, 20)
        filesavepath = 'tmp/%s' % jsName 
        urllib.urlretrieve(url,filesavepath,download)
        print filesavepath 
def download(a, b, c):  
    per = 100.0 * a * b / c  
    if per > 100:  
        per = 100 
    print '%.2f%%' % per
#if __name__ == '__main__':
getAllJsLink()
