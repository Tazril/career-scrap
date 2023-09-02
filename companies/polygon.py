import requests

from base.apijobscrapper import APIJobScrapper


class PolygonJobScrapper(APIJobScrapper):

    def get_json_data(self, url):
        return requests.get(url).json()

    def get_name(self):
        return "Polygon"

    def get_image_url(self):
        return "https://upload.wikimedia.org/wikipedia/commons/thumb/2/24/Polygon_blockchain_logo.png/1200px-Polygon_blockchain_logo.png?20220903072413"


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