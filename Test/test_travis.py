from Pages.PageLinks import PageLinks
from Test.test_base import BaseTest


class TestProTipsLinks(BaseTest):

    def test_protips_header(self):
        self.pageLinks = PageLinks(self.driver)
        self.pageLinks.header_link()
        self.pageLinks.do_screenshot("PASSED.png")
        cover = self.pageLinks.page_cover()
        assert cover == self.pageLinks.page_cover()

    def test_protips_body(self):
        self.pageLinks = PageLinks(self.driver)
        self.pageLinks.body_link()
        self.pageLinks.do_screenshot("FAILED.png")
        cover = self.pageLinks.page_cover()
        assert cover == self.pageLinks.page_cover()
