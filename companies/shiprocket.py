import requests
from bs4 import BeautifulSoup

from base.bsjobscrapper import BSJobScrapper
from base.constants import HEADERS


class ShipRocketBSJobScrapper(BSJobScrapper):

    def get_content(self, url):
        return requests.get(url, headers=HEADERS).content

    def get_name(self):
        return "ShipRocket"

    def get_image_url(self):
        return "https://aftercolleges.com/wp-content/uploads/2022/12/Shiprocket-logo-1200x675.jpg"

    def get_jobs(self):
        url = 'https://careers.shiprocket.in/'
        content = self.get_content(url)
        soup = BeautifulSoup(content, 'html.parser')
        postings = []
        for child in soup.find_all('div', 'job'):
            if not child.find('h5'):
                continue
            postings.append({})
            postings[-1]['title'] = child.find('h5').get_text()
            postings[-1]['url'] = child.find('a')['href']
            postings[-1]['location'] = child.find('small').findNext('small').get_text()
        return postings
