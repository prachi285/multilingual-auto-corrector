import urllib2
import sys
from bs4 import BeautifulSoup

f = open('hinglish_clean.txt','w')
sys.stdout = f
with open('urls.txt') as links:
	for site in links:
		hdr = {'User-Agent': 'Mozilla/5.0'}
		req = urllib2.Request(site,headers=hdr)
		page = urllib2.urlopen(req)
		soup = BeautifulSoup(page, "html.parser")
		for tag in soup.find_all('p'):
			txt = tag.text.encode('utf-8')
			lines = txt.split('.')
			for sentence in lines:
				if(len(sentence)>20):
					print sentence.strip()
