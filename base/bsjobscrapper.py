from abc import abstractmethod

from base.jobscrapper import JobScrapper


class BSJobScrapper(JobScrapper):

    @abstractmethod
    def get_content(self, url):
        pass
