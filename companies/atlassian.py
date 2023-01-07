import requests

from base.apijobscrapper import APIJobScrapper


class AtlassianApiJobScrapper(APIJobScrapper):

    def get_json_data(self, url):
        return requests.get(url).json()['postings']

    def get_name(self):
        return "Atlassian"

    def get_image_url(self):
        return "https://assets.stickpng.com/images/62c6eb897a58a4aa1fb7709e.png"

    def get_jobs(self):
        url = 'https://www.atlassian.com/.rest/postings'
        data = self.get_json_data(url)
        postings = []
        for doc in data:
            postings.append({})
            postings[-1]['title'] = doc['text']
            postings[-1]['url'] = doc['urls']['applyUrl']
            postings[-1]['location'] = doc['categories']['location']
        return postings
