import base64
import json

import requests

from base.apijobscrapper import APIJobScrapper


class PharmEasyApiJobScrapper(APIJobScrapper):

    def get_json_data(self, url):
        return requests.post(url, json={
            "source": "careers",
            "code": "",
            "filterByBuId": -1
        }).json()['reqDetailsBOList']

    def get_name(self):
        return "PharmEasy"

    def get_image_url(self):
        return "https://upload.wikimedia.org/wikipedia/commons/3/3a/PharmEasy_logo.png"

    def get_jobs(self):
        url = 'https://pharmeasy.mynexthire.com/employer/careers/reqlist/get'
        data = self.get_json_data(url)
        postings = []
        for doc in data:
            postings.append({})
            params = {"pageType": "jd", "cvSource": "careers", "reqId": doc['reqId'],
                      "requester": {"id": "", "code": "", "name": ""}, "page": "careers", "bufilter": -1,
                      "customFields": {}}
            json_str = json.dumps(params)
            query_bytes = base64.b64encode(json_str.encode("ascii"))
            postings[-1]['title'] = doc['reqTitle']
            postings[-1]['url'] = 'https://pharmeasy.in/careers/jobs/?p=' + query_bytes.decode("ascii")
            postings[-1]['location'] = doc['location']
        return postings
