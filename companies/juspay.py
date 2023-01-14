import requests
from bs4 import BeautifulSoup

from base.bsjobscrapper import BSJobScrapper
from base.constants import HEADERS


class JuspayBSJobScrapper(BSJobScrapper):

    def get_content(self, url):
        return requests.get(url, headers=HEADERS).content

    def get_name(self):
        return "Juspay"

    def get_image_url(self):
        return "https://cashinvoice.it/funding-smes/wp-content/uploads/sites/6/2020/07/juspay.png"

    def get_jobs(self):
        url = 'https://juspay.in/careers'
        content = self.get_content(url)
        soup = BeautifulSoup(content, 'html.parser')
        postings = []
        for child in soup.find_all('article', 'opening__desc'):
            postings.append({})
            postings[-1]['title'] = child.find('h4').get_text()
            postings[-1]['location'] = child.find('article', 'opening__location').get_text()
            postings[-1]['url'] = 'https://juspay.in/' + child.find('a')['href']
        return postings


if __name__ == '__main__':
    print(JuspayBSJobScrapper().get_jobs())
