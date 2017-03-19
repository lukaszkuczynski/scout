from unittest import TestCase, main


class LibTest(TestCase):

    def test_libs(self):
        import lxml
        print(lxml)
        import requests
        print(requests.__version__)

if __name__ == '__main__':
    main()