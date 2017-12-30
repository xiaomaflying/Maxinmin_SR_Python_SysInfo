Required of Client

1. Support linux-like system client.
2. Client must have python executable binary which path is /usr/local/bin/python3 default (
you can config the python path in config.py: CLIENT_PYTHON_PATH).
3. Client must have the python lib which are in requirements.txt


Test platform

All python script are well tested in Mac OS (Darwin).


How to run tests

1. Before run tests
    1) You must make sure you mysql server is running. I will test the db connector using mysql database. So please make
    sure that you can access you mysql database with the right config such as host, port, user, password.
    2) You must make sure the sshd server is running. I will ssh login myself to test the ssh function. Please make sure
    you can ssh you local machine. Note: OS X comes with sshd, you only need to enable it in System Preferences,
    under Sharing by clicking on Remote Login.
    3) To change the mysql configuration please change the variable DB_CONFIG in Source/tests/config.py
    4) To change the ssh configuration please change the variable SSH_CONFIG in Source/tests/config.py

2. Run tests
    cd Source/;
    python3 -m uniitest tests


How to run

1. cd Maxinmin_SR_Python_SysInfo/Source
2. python3 collect_data.py