# https://upload.wikimedia.org/wikipedia/commons/5/59/ZS_Associates.svg

import requests

from base.apijobscrapper import APIJobScrapper


class ZSAssociateScrapper(APIJobScrapper):

    def get_json_data(self, url):
        return requests.get(url).json()['jobs']

    def get_name(self):
        return "ZSAssociates"

    def get_image_url(self):
        return "https://upload.wikimedia.org/wikipedia/commons/5/59/ZS_Associates.svg"

    def get_jobs(self):
        url = 'https://jobs.zs.com/api/jobs'
        data = self.get_json_data(url)
        postings = []   
        for doc in data:
            postings.append({})
            postings[-1]['title'] = doc['data']['title']
            postings[-1]['url'] = doc['data']['apply_url']
            postings[-1]['location'] = doc['data']['full_location']
        return postings


if __name__ == '__main__':
    print(ZSAssociateScrapper().get_jobs())