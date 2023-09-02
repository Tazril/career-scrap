import requests
from bs4 import BeautifulSoup

from base.bsjobscrapper import BSJobScrapper
from base.constants import HEADERS


class GoogleBSJobScrapper(BSJobScrapper):

    def get_content(self, url):
        return requests.get(url, headers=HEADERS).content

    def get_name(self):
        return "Google"

    def get_image_url(self):
        return "https://www.freepnglogos.com/uploads/google-logo-png/google-logo-png-suite-everything-you-need-know-about-google-newest-0.png"

    def get_jobs(self):
        url = 'https://www.google.com/about/careers/applications/jobs/results/?location=Bengaluru,%20Karnataka,%20India&jlo=en-US&hl=en'
        content = self.get_content(url)
        soup = BeautifulSoup(content, 'html.parser')
        postings = []
        for child in soup.find_all('div',class_='sMn82b'):
            postings.append({})
            postings[-1]['title'] = child.find("h3" , class_= "QJPWVe").get_text()
            postings[-1]['location'] = child.find("span" , class_= "r0wTof").get_text()
            postings[-1]['url'] = 'https://www.google.com/about/careers/applications/' + child.find("a" , class_= "WpHeLc VfPpkd-mRLv6 VfPpkd-RLmnJb")['href']
        return postings


if __name__ == '__main__':
    print(GoogleBSJobScrapper().get_jobs())
