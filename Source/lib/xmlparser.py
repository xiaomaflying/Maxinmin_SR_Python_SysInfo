import xml.etree.ElementTree as ET
from xml.etree.ElementTree import ParseError
import os


class XMLParser(object):
    def __init__(self, xml_path):
        if not os.path.exists(xml_path):
            raise Exception('Xml path : %s is not exist' % xml_path)
        self.path = xml_path

    def _check_xml_attrs(self, d):
        userinfo = d['info']
        args_required = ['ip', 'username', 'password', 'mail']
        for arg in args_required:
            if not arg in userinfo:
                raise ValueError("%s must be one of client attributes")

    def parse2obj(self):
        try:
            tree = ET.parse(self.path)
        except ParseError as e:
            msg = 'Error occur when parsed xml file : %s. Error info: %s' % (self.path, e.msg)
            raise TypeError(msg)
        root = tree.getroot()
        alerts = [child.attrib for child in root]
        result = {'info': root.attrib, 'alerts': alerts}
        self._check_xml_attrs(result)
        return result