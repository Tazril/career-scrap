import requests

from base.apijobscrapper import APIJobScrapper


class RazorpayApiJobScrapper(APIJobScrapper):

    def get_json_data(self, url):
        return requests.get(url).json()['jobs']

    def get_name(self):
        return "Razorpay"

    def get_image_url(self):
        return "https://razorpay.com/jobs/images/logos/logo.svg"

    def get_jobs(self):
        url = 'https://boards-api.greenhouse.io/v1/boards/razorpaysoftwareprivatelimited/jobs'
        data = self.get_json_data(url)
        postings = []
        for doc in data:
            postings.append({})
            postings[-1]['title'] = doc['title']
            postings[-1]['url'] = doc['absolute_url']
            postings[-1]['location'] = doc['location']['name']
        return postings


if __name__ == '__main__':
    print(RazorpayApiJobScrapper().get_jobs())