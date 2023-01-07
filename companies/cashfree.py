import requests
from bs4 import BeautifulSoup

from base.bsjobscrapper import BSJobScrapper


class CashFreeBSJobScrapper(BSJobScrapper):

    def get_content(self, url):
        return requests.get(url).content

    def get_name(self):
        return "CashFree"

    def get_image_url(self):
        return "https://assets.website-files.com/615adf96b54a6623a41c1721/61790b8a155452bc000cc2a9_cashfree_2.png"

    def get_jobs(self):
        url = 'https://www.cashfree.com/careers'
        content = self.get_content(url)
        soup = BeautifulSoup(content, 'html.parser')
        postings = []
        for child in soup.find_all('div', 'position'):
            postings.append({})
            postings[-1]['title'] = child.find('h4').get_text()
            postings[-1]['location'] = child.find('p').get_text().strip()
            postings[-1]['url'] = url + child.find('a')['href']
        return postings
