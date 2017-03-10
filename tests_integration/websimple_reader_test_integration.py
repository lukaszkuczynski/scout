from unittest import main, TestCase
from value_reader import WebSimpleReader

class WebSimpleReaderTestI(TestCase):

    def test_reader_givenWebResourceWithText_canReadIt(self):
        config = {
            'websimple': {
                "address": "https://www.nytimes.com",
                "xpath": "//li[contains(@class, 'todays-paper')]/a"
            }
        }
        reader = WebSimpleReader(config)

        reader.read()


if __name__ == '__main__':
    main()