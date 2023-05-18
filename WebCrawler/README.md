WebCrawler
#

JavaScript application that generates an "internal links" report for any website on the internet by crawling each page of the site.

Prerequistes
-

- `install npm`

Once you navigated to root of directory (`./WebCrawler`) then run `npm install` uses package.json to install packages 

How to run application
-

Navigate to the folder and run the below command
```
npm run start $ENTER_START_SITE_HERE
```

where `$ENTER_START_SITE_HERE` is the site that we will start the crawling on.

Output
-
The program generates a report that logs to the console of the sites that were visited (in desc order) in the format below

`Found ${count} internal links to ${url}`

Thank you for reading \o/
