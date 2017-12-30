import mysql.connector
from .config import DB_CONFIG
import paramiko
import os


class DBConnector(object):
    def __init__(self, db_conf):
        self.db_conf = db_conf
        self.conn = self._connect()

    def _connect(self):
        conf = self.db_conf
        conn = mysql.connector.connect(
            user=conf['user'],
            password=conf['password'],
            host=conf['host'],
            port=conf['port'],
            database=conf['database'])
        return conn

    def execute_insert_sql(self, ip, user, email, info):
        cur = self.conn.cursor()
        cur.execute('insert into sysinfo (ip, user, email, info) values (%s, %s, %s, %s)', [ip, user, email, info])
        self.conn.commit()
        cur.close()

    def close(self):
        self.conn.close()


class SSHConnector(object):

    def __init__(self, config):
        host = config['ip']
        port = int(config.get('port', 22))
        user = config['username']
        passwd = config['password']
        self.ssh = paramiko.SSHClient()
        self.ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
        self.ssh.connect(host, port, user, passwd)

        t = paramiko.Transport((host, port))
        t.connect(username=user, password=passwd)
        self.sftp = paramiko.SFTPClient.from_transport(t)

    def upload_file(self, source, target):
        if os.path.exists(source):
            self.sftp.put(source, target)
        else:
            raise Exception('%s not found' % source)

    def exec_command(self, command):
        stdin, stdout, stderr = self.ssh.exec_command(command)
        return stdout.read(), stderr.read()

    def close(self):
        self.ssh.close()
        self.sftp.close()


if __name__ == '__main__':
    connector = DBConnector(DB_CONFIG)
    connector.execute_insert_sql('127.0.0.1', 'maxinmin', 'firstbestma@126.com', 'xxxxxx')
    connector.close()