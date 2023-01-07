from abc import abstractmethod

from base.jobscrapper import JobScrapper


class APIJobScrapper(JobScrapper):

    @abstractmethod
    def get_json_data(self, url):
        pass
