from abc import abstractmethod


class JobScrapper:
    @abstractmethod
    def get_name(self):
        pass

    @abstractmethod
    def get_image_url(self):
        pass

    @abstractmethod
    def get_jobs(self):
        pass
