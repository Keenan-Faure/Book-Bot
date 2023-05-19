import { appendFile, unlink, readFile, createReadStream, existsSync } from 'fs';
import * as readline from 'node:readline/promises';

/**
 * writes messages to a file for a user
 * @param {String} user 
 * @param {String} message 
 */
function updateHistory(user, message)
{
    path = 'history/' + user.toLowerCase() + '.log';
    if(existsSync(path))
    {
        appendFile(path, message, function (error)
        {
            if(error)
            {
                throw error;
            }
            console.log('Updated!');
        });
    }
    else
    {
        console.log("I/O Error | " + path + " does not exist")
    }
}

/**
 * Deletes the message history file for a user
 * @param {String} user 
 */
function deleteHistory(user)
{
    path = 'history/' + user.toLowerCase() + '.log';
    if(existsSync(path))
    {
        unlink(path, function (error)
        {
            if(error)
            {
                throw error;
            }
            console.log('File deleted!');
        });
    }
    else
    {
        console.log("I/O Error | " + path + " does not exist")
    }
}

/**
 * Deletes a specific message in the history for the user
 * @param {String} user
 * @param {Strig} message
 */
function deleteMessage(user, message)
{
    path = 'history/' + user.toLowerCase() + '.log';
    if(existsSync(path))
    {
        let readLiner = readline.createInterface(
        {
            input: createReadStream(path)
        });
        readLiner.on('line', function(line)
        {
            console.log(line);
        });
    }
    else
    {
        console.log("I/O Error | " + path + " does not exist")
    }
}

/**
 * Logs messages to the console, in a certain format
 * @param {Sting} message 
 * @param {String} error_type 
 */
function logger(message, error_type)
{
    
}

export default {
    deleteMessage,
    deleteHistory,
    updateHistory
}

deleteMessage('keenan', "Hey man how you doing");

