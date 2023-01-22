import requests

from base.apijobscrapper import APIJobScrapper


class ZohoApiJobScrapper(APIJobScrapper):

    def get_json_data(self, url):
        return requests.get(url).json()['data']

    def get_name(self):
        return "Zoho"

    def get_image_url(self):
        return "https://www.zohowebstatic.com/sites/default/files/zoho-logo-zh-2x.png"

    def get_jobs(self):
        url = 'https://careers.zohocorp.com/recruit/v2/public/Job_Openings?pagename=Careers&source=CareerSite&extra_fields=%5B%22Remote_Job%22%5D'
        data = self.get_json_data(url)
        postings = []
        for doc in data:
            postings.append({})
            postings[-1]['title'] = doc['Posting_Title']
            postings[-1]['url'] = doc['$url']
            postings[-1]['location'] = doc['City'] + ", " + doc['Country1']
        return postings


if __name__ == '__main__':
    print(ZohoApiJobScrapper().get_jobs())
