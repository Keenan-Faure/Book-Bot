Grocer Simulator
-
#

A basic simulation that allows the user to buy certain products at a Super Market. 

There exists three vendors each with their own data retrival methods

- Sage One (API)
- Internal (MySQL)
- WooCommerce (API)

Prerequisites:
-

make sure you have a mysql and python installation on the machine that will be running the program.

For Mac users ([brew](https://brew.sh)):

```
brew install mysql
brew install python
```

For Ubuntu Users (WSL) ([apt-get](https://www.digitalocean.com/community/tutorials/how-to-install-mysql-on-ubuntu-20-04)):

```
sudo apt install mysql-server
sudo apt install python3
```

confirm installation by typing in `mysql -V`

Next, install mysql connector for python using pip3

```
pip3 install mysql-connector-python
```

for images

```
pip3 install Pillow
```

for curl requests

```
pip3 install requests 
```

How to run the program:
-
Once you are in the directory of the project run the command below

```
python3 src/main.py
```

Enabling SageOne and WooCommerce Vendors:
-

These vendors require specific and private information. Please visit the `api.json` file inside `src/api` folder and view it's structure.

If you are confused with the structure kindly visit the README.md files on how to get them started.
