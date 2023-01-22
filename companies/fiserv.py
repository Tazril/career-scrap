import requests

from base.apijobscrapper import APIJobScrapper


class FiservApiJobScrapper(APIJobScrapper):
    body = {
        "appliedFacets": {
            "locations": [
                "2acf2f683f7d0124ebdd22de3d543803",
                "232579cc3213101ab8b0290eecec059c",
                "2acf2f683f7d01a9576386de3d548b03",
                "2acf2f683f7d01b39c8726df3d541804",
                "2acf2f683f7d01cbdf6d0fde3d542803",
                "9845595a26eb1061162afe3560a53f54"
            ]
        },
        "limit": 20,
        "offset": 0,
        "searchText": ""
    }

    def get_json_data(self, url):
        return requests.post(url, json=self.body).json()['jobPostings']

    def get_name(self):
        return "Fiserv"

    def get_image_url(self):
        return "https://fiserv.wd5.myworkdayjobs.com/EXT/assets/logo"

    def get_jobs(self):
        url = 'https://fiserv.wd5.myworkdayjobs.com/wday/cxs/fiserv/EXT/jobs'
        data = self.get_json_data(url)
        postings = []
        for doc in data:
            postings.append({})
            postings[-1]['title'] = doc['title']
            postings[-1]['url'] = 'https://fiserv.wd5.myworkdayjobs.com/en-US/EXT' + doc['externalPath']
            postings[-1]['location'] = doc['locationsText']
        return postings

