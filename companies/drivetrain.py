import requests
from bs4 import BeautifulSoup

from base.bsjobscrapper import BSJobScrapper


class DrivetrainBSJobScrapper(BSJobScrapper):

    def get_content(self, url):
        return requests.get(url).content

    def get_name(self):
        return "Drivetrain"

    def get_image_url(self):
        return "https://uploads-ssl.webflow.com/61d81b5dd6d1f64d264edd49/634bcb4b8246d88452283944_dt-logo-color.webp"

    def get_jobs(self):
        url = 'https://careers.drivetrain.ai/jobsb'
        content = self.get_content(url)
        soup = BeautifulSoup(content, 'html.parser')
        postings = []
        for child in soup.find_all('a', 'heading'):
            postings.append({})
            postings[-1]['title'] = child.find('div', 'job-list-info').find('div', 'job-title').get_text()
            postings[-1]['location'] = child.find('div', 'location-info').get_text().strip().split(' ')[0].strip()
            postings[-1]['url'] = 'https://careers.drivetrain.ai/' + child['href']
        return postings
