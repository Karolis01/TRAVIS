from selenium.webdriver.common.by import By
from Config.config import TestData
from Pages.BasePage import BasePage


class PageLinks(BasePage):

    PRO_TIPS_HEADER = (By.XPATH, "//div[@id='headerNav']//a[normalize-space()='PRO-tips']")
    PRO_TIPS_BODY = (By.XPATH, "//a[normalize-space()='PRO-tips for hyppig reisende']")
    SITE_WRAP = (By.ID, "siteWrapper")
    COVER = (By.ID, "thumbnail")

    def __init__(self, driver):
        super().__init__(driver)
        self.driver.get(TestData.BASE_URL)

    def header_link(self):
        self.do_click(self.PRO_TIPS_HEADER)

    def body_link(self):
        self.do_click(self.PRO_TIPS_BODY)

    def do_screenshot(self, text):
        self.take_screenshot(self.SITE_WRAP, text)

    def page_cover(self):
        self.get_page_cover(self.COVER)
