Introduction:

MLVD is a platform to meet the needs of users to detect whether a certain contract contains some kind of vulnerability. 
The system is developed based on Python language and Django framework, providing users with a network platform to detect whether there are vulnerabilities in smart contracts on Ether. 
The platform includes a user management module, a data management module, and a vulnerability detection module, which can detect vulnerabilities in access control, integer overflow, denial of service, transaction order dependency, re-entry, timestamp dependency, and unchecked call return values.

Installation steps:
1. Decompress the system source code package, open the decompressed source code file with pycharm.
2. In the pycharm software terminal, type: pip3 install pymysql.
3. If the system has mysql, create database djangoproject, the command is create database djangoproject charset=utf8; Otherwise, install mysql first.
4. After creating the djangoproject library, enter the following command in the pycharm terminal: python3 manage.py makemigrations, the role of the models file (source code has been written) to generate a migration file, and then in the pycharm terminal enter the implementation of the following command: python3 manage.py migrate, this command will migrate the contents of the file into the database, generate tables or modify the field attributes.
5. Check the djangoproject database tables, if it contains web_smartcontract, web_timecontract, web_txcontract, web_uncheckcontract, web_users then it is successful.
6. After the above installation is successful, run the manage.py file and wait for pycharm to finish starting, then you can open http://127.0.0.1:8080 in your browser to enter the web interface of the programme, and you can use the administrator account to log in.


