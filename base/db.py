from abc import abstractmethod


class PostingDatabase:

    @abstractmethod
    def create_table(self):
        pass

    @abstractmethod
    def insert(self, name, location, url, company):
        pass

    @abstractmethod
    def get_all(self):
        pass

    @abstractmethod
    def get_count(self):
        pass

    @abstractmethod
    def get_company_list(self):
        pass

    @abstractmethod
    def get_by_company(self, company):
        pass

    @abstractmethod
    def remove_by_company(self, company):
        pass

    @abstractmethod
    def search(self, text):
        pass
