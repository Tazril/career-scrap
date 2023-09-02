import requests

from base.apijobscrapper import APIJobScrapper


class PolygonJobScrapper(APIJobScrapper):

    def get_json_data(self, url):
        return requests.get(url).json()

    def get_name(self):
        return "Polygon"

    def get_image_url(self):
        return "https://assets-global.website-files.com/637359c81e22b715cec245ad/63dc31f8817a4a509d7635a7_Logo.svg"


    def get_jobs(self):
        url = 'https://api.lever.co/v0/postings/Polygon?mode=json'
        data = self.get_json_data(url)
        postings = []
        for doc in data:
            postings.append({})
            postings[-1]['title'] = doc['text']
            postings[-1]['url'] = doc['applyUrl']
            postings[-1]['location'] = doc['categories']['location']
        return postings


if __name__ == '__main__':
    print(PolygonJobScrapper().get_jobs())