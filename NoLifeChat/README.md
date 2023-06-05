NoLifeChat
#

JavaScript web-based chat application that allows for two or more users to converse.

Prerequistes
-

- `install npm`

Once you navigated to root of directory (`./NoLifeChat`) then run `npm install` uses package.json to install packages 

How to run application
-

Navigate to the folder and run the below command
```
npm start $port
```

where `$port` is the port number that we will be using.

How to use
-

The program uses a `users.json` file inside the `public` folder to allow for certain users to converse. Note that only users that are defined there may be part of the chat.

The format of the `users.json` file is as follows:

```
{{username}}:{{password}}
```

The username is specified by entering `?user={{username}}` in the browser in the url below:

```
http://localhost:$port/
```
Once the page has been opened a prompt will ask for a password which is defined in the `users.json` file.

If the correct password has been entered you can converse with your friends!

Otherwise if the incorrect password is entered, following the refresh prompt allows you to try again.

Tests
-

To run tests on the filesystems.js file please enter

```
npm run test
```

Note that the filesystem functionality has not been implemented as of yet. Maybe in future versions

Thank you for reading \o/
