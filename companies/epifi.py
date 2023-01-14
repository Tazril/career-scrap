import requests
from bs4 import BeautifulSoup

from base.bsjobscrapper import BSJobScrapper


class EpiFiBSJobScrapper(BSJobScrapper):

    def get_content(self, url):
        return requests.get(url).content

    def get_name(self):
        return "EpiFi"

    def get_image_url(self):
        return "https://lever-client-logos.s3.us-west-2.amazonaws.com/b1a67862-9e17-4f38-896f-347e051e94b3-1612511026673.png"

    def get_jobs(self):
        url = 'https://jobs.lever.co/epifi'
        content = self.get_content(url)
        soup = BeautifulSoup(content, 'html.parser')
        postings = []
        for child in soup.find_all('div', 'posting'):
            postings.append({})
            postings[-1]['title'] = child.find('a', 'posting-title').find('h5').get_text()
            postings[-1]['location'] = child.find('span').get_text()
            postings[-1]['url'] = child.find('a', 'posting-title')['href']

        return postings
