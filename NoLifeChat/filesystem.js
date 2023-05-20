const { appendFile, unlink } = require('fs/promises');
const { existsSync, createReadStream } = require('fs');
const readline = require('node:readline/promises');

let FOLDER_NAME = 'chat_history/';

/**
 * writes messages to a file for a user
 * @param {String} user 
 * @param {String} message 
 */
async function updateHistory(user, message)
{
    let path = FOLDER_NAME + user.toLowerCase() + '.log';
    await appendFile(path, message + "\n", function (error)
    {
        if(error)
        {
            throw error;
        }
        logger("info", "file at " + path + " was UPDATED")
    });
    return true;
}

/**
 * Deletes the message history file for a user
 * @param {String} user 
 */
async function deleteHistory(user)
{
    let path = FOLDER_NAME + user.toLowerCase() + '.log';
    if(existsSync(path))
    {
        await unlink(path, function (error)
        {
            if(error)
            {
                throw error;
            }
        });
        logger("info", "file at " + path + " was DELETED");
        return true;
    }
    else
    {
        logger("I/O Error", path + " does not exist");
        return false;
    }
}

/**
 * Deletes a specific message in the history for the user
 * @param {String} user
 * @param {Strig} message
 */
async function deleteMessage(user, message)
{
    let messages = [];
    let path = FOLDER_NAME + user.toLowerCase() + '.log';
    if(existsSync(path))
    {
        messages = await readChatHistory(user, message);
        await deleteHistory(user, test);
        for(let i = 0; i < messages.length; ++i)
        {
            await updateHistory(user, messages[i], test);
        }
        return true;
    }
    else
    {
        logger("I/O Error", path + " does not exist");
        return false;
    }
}

/**
 * Reads the log file saved in system for that user
 * Ignores the string in message
 * @param {String} user 
 * @param {String} message
 * @returns {Array}
 */
async function readChatHistory(user, ignoreText=false, message)
{
    let path = FOLDER_NAME + user.toLowerCase() + '.log';
    if(existsSync(path))
    {
        let messages = [];
        const fileStream = createReadStream(path);
        const rl = readline.createInterface(
        {
            input: fileStream,
            crlfDelay: Infinity,
        });
        for await (const line of rl)
        {
            if(!ignoreText)
            {
                if(line.toLowerCase() != message.toLowerCase())
                {
                    messages.push(line);
                }
            }
            else
            {
                messages.push(line);
            }
        }
        return messages;
    }
    else
    {
        return [];
    }
} 

/**
 * Logs messages to the console, in the format
 * `[AppName] [type] message | date/time stamp`
 * @param {Sting} message 
 * @param {String} type 
 */
function logger(type, message)
{
    console.log("[NoLifeChat] [" + type + "]" + " " + message + " | " + new Date());
}

//make styles for the index.html
//make extra buttons and link them with the functions here

module.exports = {
    logger,
    deleteHistory,
    deleteMessage,
    updateHistory,
    readChatHistory
}


