from unittest import TestCase, main


class LibTest(TestCase):

    def test_libs(self):
        import lxml
        print(lxml)
        import requests
        print("requests " + requests.__version__)
        import pymongo
        print("pymongo "+ pymongo.get_version_string())

if __name__ == '__main__':
    main()