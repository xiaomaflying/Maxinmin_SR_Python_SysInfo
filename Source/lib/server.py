# This is a server script.

import json

from cryptography.fernet import Fernet
from .send_email import send_mail
from . import config as cf
from .connectors import DBConnector
from .connectors import SSHConnector
from .xmlparser import XMLParser


CRYPTO_KEY = b'mWK49Y-bLpaycw7xXaTO_IoFs_8vBeQtSepE0qbIva8='


def parse2text(d):
    s = []
    s.append("<p>Memory Percent: %.2f%%</p>" % d.get('mem_percent'))
    s.append("<p>CPU Percent: %.2f%%</p>" % d.get('cpu_percent'))
    s.append("<p>Uptime: %ds</p>" % int(d.get('uptime')))
    s.append("<div>%s</div>" % d.get('log_content'))
    return '\n'.join(s)


def run(xml_path):
    # Read the xml config
    config = XMLParser(xml_path)
    config_obj = config.parse2obj()
    email_to_list = [config_obj['info']['mail'], ]

    # Establish the connection to the windows client
    conn = SSHConnector(config_obj['info'])
    tmp_dirname = b'SysInfo'
    conn.exec_command(b'mkdir ' + tmp_dirname)
    scripts = [b'get_windows_events.py', b'client.py', ]

    print('Uploading the client files & Collecting data from windows client ...')
    for script in scripts:
        client_path = b'%s/%s' % (tmp_dirname, script)
        source_path = b'%s/%s' % (b'lib', script)
        conn.upload_file(source_path, client_path)

        cmd = [b'python', client_path]
        stdoutdata, stderrdata = conn.exec_command(b' '.join(cmd))

    if stderrdata:
        raise Exception("Error occure when get infomation in client : %s. Error info: %s" % \
                        (config_obj['info']['ip'], stderrdata))

    print('Finish collecting data ')

    # Decrypted the data
    plain_text = Fernet(CRYPTO_KEY).decrypt(stdoutdata)
    plain_text = plain_text.decode()
    sysinfo = json.loads(plain_text)
    email_content = parse2text(sysinfo)

    # Insert the statistic data into database
    connector = DBConnector(cf.DB_CONFIG)
    info = config_obj['info']
    connector.execute_insert_sql(info['ip'], info['username'], info['mail'], plain_text)
    connector.close()
    conn.close()

    # Send Email to the user
    print('Sending Email ...')
    send_mail(email_content, 'System Info', email_to_list)
    print('Success! Check the email and have a coffee to celebrate.')


def main_flows(conf_dir):
    import threading
    import glob
    conf_pattern = conf_dir + '/*.xml'
    xml_files = glob.glob(conf_pattern)
    for f in xml_files:
        t = threading.Thread(target=run, args=(f,))
        t.start()
