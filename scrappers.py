from companies.amazon import AmazonApiJobScrapper
from companies.atlassian import AtlassianApiJobScrapper
from companies.cashfree import CashFreeBSJobScrapper
from companies.cred import CREDApiJobScrapper
from companies.drivetrain import DrivetrainBSJobScrapper
from companies.nutanix import NutanixApiJobScrapper
from companies.paytm import PaytmBSJobScrapper
from companies.phonepe import PhonePeApiJobScrapper
from companies.uber import UberApiJobScrapper
from companies.zeta import ZetaApiJobScrapper
from companies.coursera import CourseraBSJobScrapper

SCRAPPERS = [
    CREDApiJobScrapper(),
    AtlassianApiJobScrapper(),
    AmazonApiJobScrapper(),
    DrivetrainBSJobScrapper(),
    UberApiJobScrapper(),
    PhonePeApiJobScrapper(),
    ZetaApiJobScrapper(),
    NutanixApiJobScrapper(),
    PaytmBSJobScrapper(),
    CashFreeBSJobScrapper(),
    CourseraBSJobScrapper()
]

COMPANY_LOGO_MAP = {scrapper.get_name(): scrapper.get_image_url() for scrapper in SCRAPPERS}
