const { test, expect } = require('@jest/globals');
const { normalizeURL } = require('./crawl.js');
const { getURLsFromHtml } = require('./crawl.js');

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

/**
 * First Case
 * Absolute URL
 */
test('Get urls from HTML - Absolute URL', () => 
{
    expect(
        getURLsFromHtml(
            "<html><body><a href='https://blog.boot.dev'></a></body></html>",
            "https://blog.boot.dev")
    ).toStrictEqual(["https://blog.boot.dev/"]);
});

/**
 * Second Case
 * Absolute URL + query params + file_paths
 */
test('Get urls from HTML - Absolute URL + query params + file_paths', () => 
{
    expect(
        getURLsFromHtml(
            "<html><body><a href='https://blog.boot.dev/file/path?q=string'></a></body></html>",
            "https://blog.boot.dev")
    ).toStrictEqual(["https://blog.boot.dev/file/path?q=string"]);
});

/**
 * Third Case
 * Relative URL
 */
test('Get urls from HTML - Relative URL', () => 
{
    expect(
        getURLsFromHtml(
            "<html><body><a href='/xyz.html'></a></body></html>",
            "https://blog.boot.dev")
    ).toStrictEqual(["https://blog.boot.dev/xyz.html"]);
});

/**
 * Third Case
 * Multiple URLs - Absolute/Relative
 */
test('Get urls from HTML - Multiple URLs - Absolute/Relative', () => 
{
    expect(
        getURLsFromHtml(
            `<html>
                <body>
                    <a href='/xyz.html'></a>
                    <a href='https://blog.boot.dev'></a>
                    <a href='https://ez.com'></a>
                </body>
            </html>`,
            "https://blog.boot.dev")
    ).toStrictEqual(
        [
            "https://blog.boot.dev/xyz.html",
            "https://blog.boot.dev/",
            "https://ez.com/"
        ]
    );
});

