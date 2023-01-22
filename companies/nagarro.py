import json

import requests
import xmltodict as xmltodict

from base.apijobscrapper import APIJobScrapper


class NagarroApiJobScrapper(APIJobScrapper):

    def get_json_data(self, url):
        return xmltodict.parse(requests.get(url).content)['feed']['entry']

    def get_name(self):
        return "Nagarro"

    def get_image_url(self):
        return "https://c.smartrecruiters.com/sr-company-logo-prod-dc5/61aa1e97c8432600c0c3e193/huge?r=s3-eu-central-1&_1659095796433"

    def get_jobs(self):
        url = 'https://hiringautomation.table.core.windows.net/CareerSiteDim?sv=2019-02-02&se=2099-10-13T20%3A47%3A00Z&sp=r&sig=%2FTWLo6vw7gzgOiS9b5wchECIjqFaaaIPV8Rs55P0W98%3D&tn=CareerSiteDim&$filter=Job_Country%20eq%20%27India%27'
        data = self.get_json_data(url)
        postings = []
        for doc in data:
            properties = doc['content']['m:properties']
            if properties['d:Job_Url']:
                postings.append({})
                postings[-1]['title'] = properties['d:Job_Title']
                postings[-1]['url'] = properties['d:Job_Url']
                postings[-1]['location'] = properties['d:Job_City'] + ", " + properties['d:Job_Country']
                continue
            sub_url = "https://hiringautomation.table.core.windows.net/CareerSiteFact?sv=2019-02-02&se=2988-10-13T20%3A45%3A00Z&sp=r&sig=3NkPpgrFoyiFf%2BIlH4qdCeurCy0qW5TZhNa59Szouaw%3D&tn=CareerSiteFact&$filter=Index eq '{}'".format(
                properties['d:RowKey'])
            sub_data = self.get_json_data(sub_url)
            for sub_doc in sub_data:
                postings.append({})
                sub_properties = sub_doc['content']['m:properties']
                postings[-1]['title'] = properties['d:Job_Title'] + " " + sub_properties['d:Experience_range']
                postings[-1]['url'] = sub_properties['d:Job_url']
                postings[-1]['location'] = properties['d:Job_City'] + ", " + properties['d:Job_Country']
        return postings
