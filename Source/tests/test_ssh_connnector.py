import unittest

from lib.server import SSHConnector
from tests.config import SSH_CONFIG
import os
import tempfile


class SSHConnectorTest(unittest.TestCase):
    def setUp(self):
        self.conn = SSHConnector(SSH_CONFIG)
        self.target_path = os.path.join(os.path.dirname(__file__), 'data', 'pseudo.txt')

    def tearDown(self):
        self.conn.close()
        if os.path.exists(self.target_path):
            os.unlink(self.target_path)

    def test_upload_file(self):
        self.assertFalse(os.path.exists(self.target_path))
        tempf = tempfile.NamedTemporaryFile(buffering=0)
        tempf.write(b'hello')
        self.conn.upload_file(tempf.name, self.target_path)
        self.assertTrue(os.path.exists(self.target_path))
        with open(self.target_path, 'rb') as f:
            content = f.read()
        self.assertEqual(b'hello', content)
        tempf.close()

    def test_exec_command(self):
        pass

if __name__ == '__main__':
    unittest.main()
