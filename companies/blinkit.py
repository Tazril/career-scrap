import requests
from bs4 import BeautifulSoup

from base.bsjobscrapper import BSJobScrapper
from base.constants import HEADERS


class BlinkItBSJobScrapper(BSJobScrapper):

    def get_content(self, url):
        return requests.get(url, headers=HEADERS).content

    def get_name(self):
        return "BlinkIt"

    def get_image_url(self):
        return "https://blinkit.com/careers/sites/default/files/blinkit_logo.png"

    def get_jobs(self):
        url = 'https://blinkit.com/careers/jobs'
        content = self.get_content(url)
        soup = BeautifulSoup(content, 'html.parser')
        postings = []
        for child in soup.find_all('div', 'row-job-listing'):
            postings.append({})
            a_links = child.find_all('a')
            postings[-1]['title'] = a_links[0].get_text()
            postings[-1]['location'] = a_links[-1].get_text()
            postings[-1]['url'] = 'https://blinkit.com/careers' + a_links[0]['href']
        return postings