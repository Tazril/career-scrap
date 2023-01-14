import requests
from bs4 import BeautifulSoup

from base.bsjobscrapper import BSJobScrapper


class LensKartBSJobScrapper(BSJobScrapper):

    def get_content(self, url):
        return requests.get(url).content

    def get_name(self):
        return "LensKart"

    def get_image_url(self):
        return "https://d27i7n2isjbnbi.cloudfront.net/careers/photos/253015/thumb_photo_1640683370.jpeg"

    def get_jobs(self):
        url = 'https://hiring.lenskart.com/#section-156409'
        content = self.get_content(url)
        soup = BeautifulSoup(content, 'html.parser')
        postings = []
        for child in soup.find_all('a', 'job__row'):
            postings.append({})
            postings[-1]['title'] = child.find('h5', 'title').get_text().strip()
            postings[-1]['location'] = child.find('span', 'location').get_text().strip()
            postings[-1]['url'] = 'https://hiring.lenskart.com/' + child['href']

        return postings
