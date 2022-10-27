import time
from loguru import logger
from SeleniumBaseClass import SeleniumBaseClass


class BaseClass(SeleniumBaseClass):

    def __init__(self):
        SeleniumBaseClass.__init__(self)

    def run_main_page(self):
        self.driver.get('http://google.com')