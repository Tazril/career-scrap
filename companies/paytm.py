import requests
from bs4 import BeautifulSoup

from base.bsjobscrapper import BSJobScrapper


class PaytmBSJobScrapper(BSJobScrapper):

    def get_content(self, url):
        return requests.get(url).content

    def get_name(self):
        return "Paytm"

    def get_image_url(self):
        return "https://1000logos.net/wp-content/uploads/2021/03/Paytm_Logo.png"

    def get_jobs(self):
        url = 'https://jobs.lever.co/paytm'
        content = self.get_content(url)
        soup = BeautifulSoup(content, 'html.parser')
        postings = []
        for child in soup.find_all('div', 'posting'):
            postings.append({})
            postings[-1]['title'] = child.find('h5').get_text()
            postings[-1]['location'] = child.find('span').get_text()
            postings[-1]['url'] = child.find('a')['href']
        return postings
