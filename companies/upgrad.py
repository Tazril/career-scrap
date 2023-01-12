import requests

from base.apijobscrapper import APIJobScrapper


class UpGradApiJobScrapper(APIJobScrapper):

    def get_json_data(self, url):
        return requests.get(url).json()['message']['jobs']

    def get_name(self):
        return "UpGrad"

    def get_image_url(self):
        return "https://images.livemint.com/img/2022/08/22/600x338/10_(10)_1661170470531_1661170477841_1661170477841.jpg"

    def get_jobs(self):
        url = 'https://upgrad.darwinbox.in/ms/candidateapi/job?page=1&limit=1000&companyId=main'
        data = self.get_json_data(url)
        postings = []
        for doc in data:
            postings.append({})
            postings[-1]['title'] = doc['title']
            postings[-1]['location'] = doc['officelocation_show_arr']
            postings[-1]['url'] = 'https://upgrad.darwinbox.in/ms/candidate/main/careers/' + doc['id']
        return postings
