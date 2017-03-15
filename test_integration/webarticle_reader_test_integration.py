from unittest import main, TestCase

from application.web_value_reader import WebArticleReader


class WebArticleReaderTestI(TestCase):

    def test_reader_from_nytimes_returns_more_than_1_article(self):
        config = {
            "address": "https://www.nytimes.com",
            "articles_xpath": "//article[contains(@class, 'story')]",
            "heading_xpath": ".//h2[contains(@class, 'story-heading')]//a//text()",
            "details_href_xpath": ".//h2[contains(@class, 'story-heading')]//a//@href",
            "content_xpath": ".//p[contains(@class, 'summary')]//text()"
        }
        reader = WebArticleReader(config)
        value = reader.read()
        self.assertGreater(len(value), 0)


if __name__ == '__main__':
    main()