import requests
from lxml import html

from application.value_reader import ValueReader


class WebSimpleReader(ValueReader):

    def read(self):
        page = requests.get(self.config['address'])
        tree = html.fromstring(page.content)
        value = tree.xpath(self.config['xpath'])
        return value




class WebArticleReader(ValueReader):

    def read(self):
        list = []
        page = requests.get(self.config['address'])
        tree = html.fromstring(page.content)
        articles = tree.xpath(self.config['articles_xpath'])
        for article in articles:
            heading_path = self.config['heading_xpath']
            details_href_path = self.config['details_href_xpath']
            content_path = self.config['content_xpath']
            heading = article.xpath(heading_path)
            if heading: heading = heading[0]
            details_href = article.xpath(details_href_path)
            if details_href: details_href = details_href[0]
            content = article.xpath(content_path)
            if content: content = content[0]
            list.append({
                'heading': heading,
                'details_href': details_href,
                'content': content
            })
        return list