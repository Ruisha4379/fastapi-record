## MongoDB Instructions
*(skip this section and see below for MySQL Instructions if coming from MySQL course)*

- Enter `touch mongodb-org-3.6.repo` into the terminal
- Now open the **mongodb-org-3.6.repo** file in your code editor (select it from the left-hand file menu) and paste the following into it then save the file:

```
[mongodb-org-3.6]
name=MongoDB Repository
baseurl=https://repo.mongodb.org/yum/amazon/2013.03/mongodb-org/3.6/x86_64/
gpgcheck=1
enabled=1
gpgkey=https://www.mongodb.org/static/pgp/server-3.6.asc
```

- Now run the following in your terminal:

```
sudo mv mongodb-org-3.6.repo /etc/yum.repos.d
sudo yum install -y mongodb-org
```
- Close the **mongodb-org-3.6.repo** file and press **Close tab** when prompted
- Change directories back into root ~ by entering `cd` into the terminal then enter the following commands:

```
mkdir data
echo 'mongod --dbpath=data --nojournal' > mongod
chmod a+x mongod
```

- Now test mongod with `./mongod`
- Remember, you must first enter `cd` to change directories into root ~ before running `./mongod`
- Don't forget to shut down ./mongod with `ctrl + c` each time you're done working

That's it! You're all set :)
