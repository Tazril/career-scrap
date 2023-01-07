import requests

from base.apijobscrapper import APIJobScrapper


class AmazonApiJobScrapper(APIJobScrapper):
    LIMIT = 100

    def get_json_data(self, url):
        return requests.get(url).json()['jobs']

    def get_name(self):
        return "Amazon"

    def get_image_url(self):
        return "https://upload.wikimedia.org/wikipedia/commons/thumb/4/4a/Amazon_icon.svg/2500px-Amazon_icon.svg.png"

    def get_jobs(self):
        url = 'https://www.amazon.jobs/en-gb/search.json?country=IND&result_limit=100'
        offset = 0
        postings = []
        while True:
            url_with_offset = url + '&offset=' + str(offset)
            data = self.get_json_data(url_with_offset)
            for doc in data:
                postings.append({"title": doc['title'], "location": doc['location'], "url": doc['url_next_step']})
            if len(data) < self.LIMIT:
                break
            offset += self.LIMIT
        return postings
