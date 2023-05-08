API.json
-

Contains different sections for each connector (vendor) `sageOne` and `wooCom` respectively

The `authentication` object holds all the data required to make a connection to Sage One.

- If you do not have a test Sage One account please attempt to get one [here](https://accounting.sageone.co.za/Landing/Default.aspx)

- Likewise for WooCommerce, which requires a server to host and install the plugin on. Note the below tutorials are not bullet proof, I simply searched in google and took the 'best' one. Goodluck!
    - [Ubuntu](https://www.vultr.com/docs/how-to-install-woocommerce-on-ubuntu-20-04/)
    - [MacOS](https://skillcrush.com/blog/install-wordpress-mac/)

Exercise
-

Try to use google to find how to retrieve the respective authentication keys in `api.json`.

Product ID's and SKUs (`woo_product` and `sage_product`)
-

The Sage One and WooCommerce connectors uses pythons `request` module to retrieve the data from the respective endpoints

    - For WooCommerce we need the SKUs of exisitng products (simple products should not be private)
    - For SageOne we need the product IDs (Internal Identifiers)

Please place a generous amount in the .json file, but please note the program window only allows a certain amount as it is an absolute height not respective to the elements inside.

Config.json
-

This file will need to be configured with the credentials needed to connect to MySQL on the local machine.

If one key is left out the database connection to mysql will fail and no products will be retrieved.

Note:
    - The program automatically adds an `inventory` table with 5 products in them
    - These are stored inside a `productDump.json` to use inside the program

Customer.json
-

This file is populated when the user of the program enters credentials in the `Featured > Customer`
