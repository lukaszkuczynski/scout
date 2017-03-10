from mission import Mission
from abc import abstractmethod
from lxml import html
import requests

class ValueReaderFactory():
    def __init__(self, mission):
        self.config = mission['mission']['source']

    def reader(self):
        '''
        :return: Reader for mission provided
        '''
        # changeit
        if 'websimple' in self.config:
            return WebSimpleReader(self.config['websimple'])
        elif 'static_value' in self.config:
            return StaticValueReader(self.config['static_value'])
        else:
            raise Exception("undefined reader")


class ValueReader:
    def __init__(self, config):
        self.config = config

    @abstractmethod
    def read(self):
        pass


class StaticValueReader(ValueReader):

    def read(self):
        return self.config


class WebSimpleReader(ValueReader):

    def read(self):
        page = requests.get(self.config['address'])
        tree = html.fromstring(page.content)
        value = tree.xpath(self.config['xpath'])
        return value

