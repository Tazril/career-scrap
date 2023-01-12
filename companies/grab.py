import json

import requests
from bs4 import BeautifulSoup

from base.bsjobscrapper import BSJobScrapper


class GrabBSJobScrapper(BSJobScrapper):

    def get_content(self, url):
        return requests.get(url).content

    def get_name(self):
        return "Grab"

    def get_image_url(self):
        return "https://grab.careers/wp-content/themes/grab/assets/images/brand_logo.png"

    def get_jobs(self):
        url = 'https://grab.careers/jobs'
        content = self.get_content(url)
        soup = BeautifulSoup(content, 'html.parser')
        postings = []
        for child in soup.find_all('script'):
            for line in child.get_text().split('\n'):
                if line.startswith('window.jobsList = '):
                    data = json.loads(line[18:])
                    for doc in data:
                        postings.append({})
                        postings[-1]['title'] = doc['title']
                        locations = json.loads(doc['locations'])
                        postings[-1]['location'] = locations[0]['locationName'] + ", " + locations[0]['country']
                        postings[-1]['url'] = 'https://grab.careers/jobs/job-details/?id=' + doc['reference']
        return postings
