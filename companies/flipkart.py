import json

import requests

from base.apijobscrapper import APIJobScrapper
from base.constants import HEADERS


class FlipKartApiJobScrapper(APIJobScrapper):
    LIMIT = 10

    def get_json_data(self, url):
        pass

    @staticmethod
    def get_json_data_with_start(url, start):
        filter_data = {
            "paginationStartNo": start,
            "selectedCall": "sort",
            "sortCriteria": {
                "name": "modifiedDate",
                "isAscending": False
            }
        }
        payload = {
            "filterCri": json.dumps(filter_data),
            "domain": "www.flipkartcareers.com"
        }
        return requests.post(url, headers=HEADERS, data=payload).json()['data']['data']

    def get_name(self):
        return "FlipKart"

    def get_image_url(self):
        return "https://1000logos.net/wp-content/uploads/2021/02/Flipkart-logo.png"

    def get_jobs(self):
        url = 'https://api.zwayam.com/jobs/search'
        offset = 0
        postings = []
        while True:
            data = self.get_json_data_with_start(url, offset)
            for doc in data:
                postings.append({
                    "title": doc['_source']['jobTitle'],
                    "location": doc['_source']['location'],
                    "url": 'https://www.flipkartcareers.com/#!/job-view/' + doc['_source']['jobUrl']
                })
            if len(data) < self.LIMIT:
                break
            offset += self.LIMIT
        return postings

