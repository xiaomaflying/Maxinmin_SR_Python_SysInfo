import unittest
import subprocess
from lib.connectors import DBConnector
from tests.config import DB_CONFIG


def import_sql_script(conf, sql_script):
    cmd = ['mysql', '-h', conf['host'], '-u', conf['user'], ]
    if conf['password']:
        cmd.extend(['-p', conf['password']])
    with open(sql_script) as input_file:
        proc = subprocess.Popen(cmd, stdin=input_file, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    out, err = proc.communicate()
    if err:
        raise Exception("Mysql connect error : %s " % err)


class DBConnectorTest(unittest.TestCase):

    def setUp(self):
        sql_script = 'tests/data/db_scripts.sql'
        import_sql_script(DB_CONFIG, sql_script=sql_script)

    def tearDown(self):
        sql_script = 'tests/data/drop_db.sql'
        import_sql_script(DB_CONFIG, sql_script=sql_script)

    def test_init(self):
        conn = DBConnector(DB_CONFIG)
        self.assertTrue(conn)
        conn.close()

    def test_execute_insert_sql(self):
        conn = DBConnector(DB_CONFIG)
        conn.execute_insert_sql('127.0.0.1', 'maxinmin', 'firstbestma@126.com', 'xxx')
        cur = conn.conn.cursor()
        cur.execute("select count(*) from sysinfo")
        num = cur.fetchall()
        self.assertEqual(num[0][0], 1)
        conn.close()


if __name__ == '__main__':
    unittest.main()
