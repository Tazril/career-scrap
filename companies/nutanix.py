import requests

from base.apijobscrapper import APIJobScrapper


class NutanixApiJobScrapper(APIJobScrapper):
    LIMIT = 10

    def get_json_data(self, url):
        return requests.get(url).json()['positions']

    def get_name(self):
        return "Nutanix"

    def get_image_url(self):
        return "https://1000logos.net/wp-content/uploads/2020/05/Logo-Nutanix.jpg"

    def get_jobs(self):
        url = 'https://nutanix.eightfold.ai/api/apply/v2/jobs?num=10&location=India'
        offset = 0
        postings = []
        while True:
            url_with_offset = url + '&start=' + str(offset)
            data = self.get_json_data(url_with_offset)
            for doc in data:
                apply_url = 'https://nutanix.eightfold.ai/careers?location=India&pid=' + str(doc['id'])
                postings.append({"title": doc['name'], "location": doc['location'], "url": apply_url})
            if len(data) < self.LIMIT:
                break
            offset += self.LIMIT
        return postings
