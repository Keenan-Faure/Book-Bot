const { test, expect } = require('@jest/globals');
const { deleteMessage } = require('./filesystem.js');
const { deleteHistory } = require('./filesystem.js');
const { updateHistory } = require('./filesystem.js');
const { readChatHistory } = require('./filesystem.js');

const { existsSync } = require('fs');

/**
 * First Case
 * File does not exist - does checks
 */
test('Deletes a user"s chat history - File does not exist', async () => 
{
    if(existsSync('chat_history/test_user.log'))
    {
        expect(
            await deleteHistory('test_user')
        ).toBe(true);
    }
    else
    {
        expect(
            await deleteHistory('test_user')
        ).toBe(false);
    }
});

/**
 * Second Case
 * File does exist (manually creates the file)
 */
test('Deletes a user"s chat history - File does exist', async () => 
{
    await updateHistory('test_user', 'Test text');
    expect(
        await deleteHistory('test_user')
    ).toBe(true);
});

/**
 * First Case
 * Reads log file for user
 */
test('Reads log file for user - file does not exist', async () => 
{
    expect(
        await readChatHistory('test_user')
    ).toStrictEqual([]);
});

/**
 * Second Case
 * Reads log file for user
 */
test('Reads log file for user - file does exist', async () => 
{
    await updateHistory('test_user', 'Test text');
    expect(
        await readChatHistory('test_user', true)
    ).toStrictEqual(["Test text"]);
});

/**
 * First Case
 * Deletes a chat message from the history
 */
test('Deletes chat message from history - File does not exist', async () => 
{
    await deleteHistory('test_user');
    expect(
        await deleteMessage('test_user', "Test text")
    ).toBe(false);
});

/**
 * Second Case
 * Deletes a chat message from the history
 */
test('Deletes chat message from history - File does exist', async () => 
{
    await updateHistory('test_user', 'Test text');
    expect(
        await deleteMessage('test_user', "Test text")
    ).toBe(true);
});






