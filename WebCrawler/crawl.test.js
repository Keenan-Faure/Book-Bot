const { test, expect } = require('@jest/globals')
const { normalizeURL } = require('./crawl.js')

/**
 * First Case
 * Https + query params
 */
test('Normalizes a URL - Https + query params', () => 
{
    expect(
        normalizeURL("https://www.youtube.com/watch?v=kH-jVqC5-wg&t=6970s")
    ).toBe("www.youtube.com/watch");
});

/**
 * Second Case
 * Http + query params
 */
test('Normalizes a URL - Http + query params', () => 
{
    expect(
        normalizeURL("http://www.youtube.com/watch?v=kH-jVqC5-wg&t=6970s")
    ).toBe("www.youtube.com/watch");
});

/**
 * Third Case
 * No protocol
 */
test('Normalizes a URL - No protocol', () => 
{
    expect(
        normalizeURL("www.youtube.com/watch?v=kH-jVqC5-wg&t=6970s")
    ).toBe("");
});

