import requests
from lxml import html

from value_reader import ValueReader


class WebSimpleReader(ValueReader):

    def read(self):
        page = requests.get(self.config['address'])
        tree = html.fromstring(page.content)
        value = tree.xpath(self.config['xpath'])
        return value