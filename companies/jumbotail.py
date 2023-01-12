import requests
from bs4 import BeautifulSoup

from base.bsjobscrapper import BSJobScrapper


class JumboTailBSJobScrapper(BSJobScrapper):

    def get_content(self, url):
        return requests.get(url).content

    def get_name(self):
        return "JumboTail"

    def get_image_url(self):
        return "https://s3-ap-southeast-1.amazonaws.com/images-jt/jumbotail-logo.png"

    def get_jobs(self):
        url = 'https://jumbotail.com/careers/'
        content = self.get_content(url)
        soup = BeautifulSoup(content, 'html.parser')
        postings = []
        for child in soup.find_all('div', 'vc_row'):
            postings.append({})
            postings[-1]['title'] = child.find('h4').get_text()
            postings[-1]['location'] = 'Bangalore, India'
            postings[-1]['url'] = child.find('a')['href']
        return postings
