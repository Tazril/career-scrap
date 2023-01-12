import requests
from bs4 import BeautifulSoup

from base.bsjobscrapper import BSJobScrapper


class CourseraBSJobScrapper(BSJobScrapper):

    def get_content(self, url):
        return requests.get(url).content

    def get_name(self):
        return "Coursera"

    def get_image_url(self):
        return "https://w7.pngwing.com/pngs/898/376/png-transparent-united-states-coursera-massive-open-online-course-education-united-states-blue-text-trademark.png"

    def get_jobs(self):
        url = 'https://boards.greenhouse.io/embed/job_board?for=coursera'
        content = self.get_content(url)
        soup = BeautifulSoup(content, 'html.parser')
        postings = []
        for child in soup.find_all('div', class_="opening"):
            postings.append({})
            postings[-1]['title'] = child.find('a').get_text().strip()
            postings[-1]['location'] = child.find('span').get_text().strip()
            postings[-1]['url'] = child.find('a')['href']
        return postings
