import requests

from base.apijobscrapper import APIJobScrapper


class UberApiJobScrapper(APIJobScrapper):

    def get_json_data(self, url):
        res = requests.post(url,
                            headers={
                                'x-csrf-token': 'x'},
                            json={
                                "params": {
                                    "location": [
                                        {
                                            "country": "IND",
                                            "region": "Karnataka",
                                            "city": "Bangalore"
                                        },
                                        {
                                            "country": "IND",
                                            "region": "Telangana",
                                            "city": "Hyderabad"
                                        },
                                        {
                                            "country": "IND",
                                            "region": "Haryana",
                                            "city": "Gurgaon"
                                        },
                                        {
                                            "country": "IND",
                                            "city": "Remote"
                                        },
                                        {
                                            "country": "IND",
                                            "region": "Maharashtra",
                                            "city": "Pune"
                                        },
                                        {
                                            "country": "IND",
                                            "region": "Delhi",
                                            "city": "New Delhi"
                                        },
                                        {
                                            "country": "IND",
                                            "region": "Andhra Pradesh",
                                            "city": "Visakhapatnam"
                                        }
                                    ],
                                    "department": [],
                                    "team": [],
                                    "programAndPlatform": [],
                                    "lineOfBusinessName": []
                                },
                                "limit": 200,
                                "page": 0
                            })
        return res.json()['data']['results']

    def get_name(self):
        return "Uber"

    def get_image_url(self):
        return "https://w7.pngwing.com/pngs/567/356/png-transparent-uber-logo-decal-lyft-business-text-people-logo.png"

    def get_jobs(self):
        url = 'https://www.uber.com/api/loadSearchJobsResults?localeCode=en'
        data = self.get_json_data(url)
        postings = []
        for doc in data:
            postings.append({})
            postings[-1]['title'] = (doc['title'])
            postings[-1]['location'] = (doc['location']['city'] + ", " + doc['location']['countryName'])
            postings[-1]['url'] = ('https://www.uber.com/global/en/careers/list/' + str(doc['id']))

        return postings
