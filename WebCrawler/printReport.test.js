const { test, expect } = require('@jest/globals');
const { sortObject } = require('./printReport.js');

/**
 * First Case
 * Object with values
 */
test('Sorts an object desc - Object with values', () => 
{
    expect(
        sortObject({
            "a": 5,
            "abcs": 1
        })
    ).toStrictEqual({
        "abcs": 1,
        "a": 5
    });
});

/**
 * Second Case
 * Empty Object
 */
test('Sorts an object desc - Empty Object', () => 
{
    expect(
        sortObject({})
    ).toStrictEqual({});
});

