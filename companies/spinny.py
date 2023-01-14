import requests
from bs4 import BeautifulSoup

from base.bsjobscrapper import BSJobScrapper


class SpinnyBSJobScrapper(BSJobScrapper):

    def get_content(self, url):
        return requests.get(url).content

    def get_name(self):
        return "Spinny"

    def get_image_url(self):
        return "https://instahyre-2.s3-ap-south-1.amazonaws.com/media/CACHE/images/images/office-photos/base/9259/b7255dbe92/Spinny_Logo/5b7f4098d2896d5049781e4100d7362f.jpg"

    def get_jobs(self):
        url = 'https://spinny.freshteam.com/jobs'
        content = self.get_content(url)
        soup = BeautifulSoup(content, 'html.parser')
        postings = []
        for child in soup.find_all('a', 'heading'):
            postings.append({})
            postings[-1]['title'] = child.find('div', 'job-title').get_text()
            loc = child.find('div', 'location-info').get_text().strip().split(' ')
            postings[-1]['location'] = (loc[0] + " " + loc[1]).strip()
            postings[-1]['url'] = 'https://spinny.freshteam.com/' + child['href']

        return postings
