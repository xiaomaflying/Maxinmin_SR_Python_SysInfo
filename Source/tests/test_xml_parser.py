import unittest
from lib.xmlparser import XMLParser
import os


class XMLParserTest(unittest.TestCase):

    def test_parse_right_xml_string(self):
        xml_path = os.path.join(os.path.dirname(__file__), 'data/conf.xml')
        parser = XMLParser(xml_path)
        obj = parser.parse2obj()
        self.assertIn('info', obj)
        self.assertIn('alerts', obj)
        self.assertEqual(len(obj['alerts']), 2)
        self.assertEqual(obj['info']['ip'], '127.0.0.1')
        self.assertEqual(obj['info']['username'], 'maxinmin')
        self.assertEqual(obj['info']['password'], 'maxinmin')
        self.assertEqual(obj['info']['mail'], 'asa@asda.com')

    def test_parse_wrong_xml_string(self):
        xml_path = os.path.join(os.path.dirname(__file__), 'data/wrong_conf.xml')
        parser = XMLParser(xml_path)
        with self.assertRaises(TypeError):
            parser.parse2obj()


if __name__ == '__main__':
    unittest.main()
