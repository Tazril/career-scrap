import threading
import time
from datetime import datetime

from data.repository import PostingRepository
from data.sqlite3db import SQLPostingDatabase
from scrappers import SCRAPPERS

THREAD_SLEEP_DURATION = 24 * 60 * 60  # 24 hours


class MainDriver(threading.Thread):
    repository = PostingRepository(SQLPostingDatabase())
    scrappers = SCRAPPERS

    def update_data(self):
        for scrapper in self.scrappers:
            try:
                name = scrapper.get_name()
                if self.repository.check_if_updated(name):
                    print("[MainDriver.update_data] Skipping: Update found within 24 hours for", name)
                    continue
                data = scrapper.get_jobs()
                print("[MainDriver.update_data] Updating Data for ", name)
                self.repository.update_postings(name, data)
            except Exception as e:
                print("[MainDriver.update_data] Exception Occurred for: " + scrapper.get_name() + " " + str(e))
                pass

    def get_postings(self):
        return self.repository.get_postings()

    def run(self):
        self.update_data()
        while True:
            time.sleep(THREAD_SLEEP_DURATION)
            print('[MainDriver.run] Starting Update: ', datetime.now())
            self.update_data()
            print('[MainDriver.run] Update Ended: ', datetime.now())
