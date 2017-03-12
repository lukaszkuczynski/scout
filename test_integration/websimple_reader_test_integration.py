from unittest import main, TestCase

from application.web_value_reader import WebSimpleReader


class WebSimpleReaderTestI(TestCase):

    def test_reader_givenWebResourceWithText_canReadIt(self):
        config = {
            "address": "https://www.nytimes.com",
            "xpath": "//li[contains(@class, 'todays-paper')]/a[1]/text()"
        }
        reader = WebSimpleReader(config)
        value = reader.read()
        self.assertIn('Today', str(value))
        self.assertIn('Paper', str(value))


if __name__ == '__main__':
    main()