import requests

from base.apijobscrapper import APIJobScrapper


class CREDApiJobScrapper(APIJobScrapper):

    def get_json_data(self, url):
        return requests.get(url).json()

    def get_name(self):
        return "CRED"

    def get_image_url(self):
        return "https://play-lh.googleusercontent.com/r2ZbsIr5sQ7Wtl1T6eevyWj4KS7QbezF7JYB9gxQnLWbf0K4kU7qaLNcJLLUh0WG-3pK"

    def get_jobs(self):
        url = 'https://api.lever.co/v0/postings/cred?mode=json'
        data = self.get_json_data(url)
        postings = []
        for doc in data:
            postings.append({})
            postings[-1]['title'] = doc['text']
            postings[-1]['url'] = doc['applyUrl']
            postings[-1]['location'] = doc['categories']['location']
        return postings
