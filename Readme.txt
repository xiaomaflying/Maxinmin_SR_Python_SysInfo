
Python packages dependency

1. Central server (Mac OS) dependency packages is in the Source/requirements.txt. You can install with `pip3 install -r requirements.txt`
2. Windows client dependency packages is in the Source/client_requirements.txt.


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
    python3 -m unittest discover


How to run the main script

1. Before run (Check the configuration that the system needed)
    1) You must make sure you mysql server is running. I will test the db connector using mysql database. So please make
    sure that you can access you mysql database with the right config such as host, port, user, password.
    2) Make sure you have a SMTP server and the authority to send email. 
    3) To change the mysql configuration please change the variable DB_CONFIG in Source/lib/config.py
    4) To change the sending email configuration please change the variable EMAIL_CONFIG in Source/lib/config.py

2. Before run (Check the xml configurations)
    1) The windows client address and login infomations are stored in the Source/lib/data directory with *.xml format.
    2) One xml file is refer to one windows client. You can config the ip, ssh port, ssh username, ssh password and the email address
    where will be received.
    3) Make sure that you can login every windows client in the local machine which is the place where the main script will run.

3. Window client dependency
    1) python3 is required
    2) python packages in Source/client_requirements.txt must be installed.

4. Run the main script
    1) cd Maxinmin_SR_Python_SysInfo/Source
    2) Init the database: import the db_scripts.sql to mysql. In my case: `mysql -uroot < db_scripts.sql`
    2) python3 collect_data.py


Issues I have faced 

1. Windows client is hard to install. I used virtual machine to run the windows system.
2. Because I worked in the linux system in all my working time, I am not familier the win32api. So it take long time on install windows system and virtual machine software
and study the windows api to get the events from windows client.


Feedback

An assignment with less dependency is better maybe.
