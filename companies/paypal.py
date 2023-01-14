import requests

from base.apijobscrapper import APIJobScrapper


class PayPalApiJobScrapper(APIJobScrapper):
    LIMIT = 10

    def get_json_data(self, url):
        return requests.get(url).json()['positions']

    def get_name(self):
        return "PayPal"

    def get_image_url(self):
        return "https://upload.wikimedia.org/wikipedia/commons/a/a4/Paypal_2014_logo.png"

    def get_jobs(self):
        url = 'https://paypal.eightfold.ai/api/apply/v2/jobs?Country=india&num=10'
        offset = 0
        postings = []
        while True:
            url_with_offset = url + '&start=' + str(offset)
            data = self.get_json_data(url_with_offset)
            for doc in data:
                postings.append({
                    "title": doc['name'],
                    "location": doc['location'],
                    "url": 'https://paypal.eightfold.ai/careers/job?domain=paypal.com&pid=' + str(doc['id'])
                })
            if len(data) < self.LIMIT:
                break
            offset += self.LIMIT
        return postings
