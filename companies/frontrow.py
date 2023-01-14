import requests

from base.apijobscrapper import APIJobScrapper


class FrontRowApiJobScrapper(APIJobScrapper):

    def get_json_data(self, url):
        return requests.get(url).json()

    def get_name(self):
        return "FrontRow"

    def get_image_url(self):
        return "https://image.pitchbook.com/ECOj3UxVAWMnGXWlyN0Q16NuNzb1610613016318_200x200"

    def get_jobs(self):
        url = 'https://frontrow.kekahire.com/api/embedjobs/active/1b7199b8-4d91-4b16-a039-75937a62aa3a'
        data = self.get_json_data(url)
        postings = []
        for doc in data:
            postings.append({})
            postings[-1]['title'] = doc['title']
            postings[-1]['location'] = doc['jobLocations'][0]['name']
            postings[-1]['url'] = 'https://frontrow.kekahire.com/jobdetails/' + str(doc['id'])
        return postings
