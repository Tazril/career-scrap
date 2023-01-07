import requests

from base.apijobscrapper import APIJobScrapper


class ZetaApiJobScrapper(APIJobScrapper):

    def get_json_data(self, url):
        return requests.get(url).json()

    def get_name(self):
        return "Zeta"

    def get_image_url(self):
        return "https://upload.wikimedia.org/wikipedia/commons/1/18/Zeta_Services_logo.png"

    def get_jobs(self):
        url = 'https://api.lever.co/v0/postings/zeta?group=team&mode=json'
        data = self.get_json_data(url)
        postings = []
        for dept in data:
            for doc in dept['postings']:
                postings.append({})
                postings[-1]['title'] = doc['text']
                postings[-1]['url'] = doc['hostedUrl']
                postings[-1]['location'] = doc['categories']['location']
        return postings
