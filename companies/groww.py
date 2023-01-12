import requests

from base.apijobscrapper import APIJobScrapper


class GrowwApiJobScrapper(APIJobScrapper):

    def get_json_data(self, url):
        return requests.get(url).json()['pageProps']['jobsData']['rows']

    def get_name(self):
        return "Groww"

    def get_image_url(self):
        return "https://skillate-profile-pictures.s3.ap-south-1.amazonaws.com/org__203/bd4adee3-293a-4e95-8c33-e3a42984465b__logo_dark_groww.png"

    def get_jobs(self):
        url = 'https://groww.skillate.com/_next/data/eX2vk7Jg6G84MeQuT1B8n/jobs.json?pageSize=1000&page=0'
        data = self.get_json_data(url)
        postings = []
        for doc in data:
            postings.append({})
            postings[-1]['title'] = doc['title']
            postings[-1]['url'] = doc['code']
            postings[-1]['location'] = 'https://groww.skillate.com/jobs/' + str(doc['id'])
        return postings
