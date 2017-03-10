from unittest import main, TestCase
from value_reader import ValueReaderFactory, StaticValueReader, WebSimpleReader

class ValueReaderFactoryTest(TestCase):

    def test_factory_givenWebSimpleInConfig_returnsWebSimpleReader(self):
        config = {
            'mission': {
                'source': {
                    'websimple': {}
                }
            }
        }
        reader = ValueReaderFactory(config).reader()
        self.assertIsInstance(reader, WebSimpleReader)


    def test_factory_givenWebSimpleInConfig_returnsWebSimpleReader(self):
        config = {
            'mission': {
                'source': {
                        'static_value': {}
                }
            }
        }
        reader = ValueReaderFactory(config).reader()
        self.assertIsInstance(reader, StaticValueReader)


if __name__ == '__main__':
    main()