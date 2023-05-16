const { url } = require('inspector');
const { JSDOM } = require('jsdom');
const { isArray } = require('util');

/**
 * Normalizes a url and returns it
 * @param {String} url must be a URL
 * @returns {String} returnPath
 */
function normalizeURL(url)
{
    try
    {
        const protocols = [
            "http",
            "https"
        ];
        const urlObject = new URL(url);
        if(protocols.includes(urlObject.protocol.substring(0,urlObject.protocol.length-1)))
        {
            hostName = urlObject.hostname.toLowerCase();
            let paths = urlObject.pathname.split("/");
            let pathsToAppend = [];
            for(let i = 0; i < paths.length; ++i)
            {
                if(paths[i] == "" && i == 0)
                {
                    pathsToAppend.push("");
                }
                else if(paths[i] != "")
                {
                    pathsToAppend.push(paths[i]);
                }
            }
            let returnPath = hostName;
            for(let j = 0; j < pathsToAppend.length; ++j)
            {
                if(j == 0)
                {
                    returnPath = returnPath + pathsToAppend[j];
                    continue;
                }
                returnPath = returnPath + "/" + pathsToAppend[j];
            }
            return returnPath;
        }
    }
    catch(error)
    {
        console.log(error.message);
        return "";
    }
}

/**
 * It returns an un-normalized array of all the URLs found within the HTML.
 * @param {String} htmlBody 
 * @param {String} baseURL
 * @returns {Array} urlList
 */
function getURLsFromHtml(htmlBody, baseURL)
{
    dom = new JSDOM(htmlBody);
    urls = dom.window.document.querySelectorAll('a');
    urlList = [];

    for(let i = 0; i < urls.length; ++i)
    {
        //check if the first char is forward slash
        if(urls[i].href.charAt(0) == "/")
        {
            //convert relative to absolute
            urlList.push(baseURL + urls[i].href);
        }
        else if(urls[i].href.slice(0,8) == "https://")
        {
            urlList.push(urls[i].href);
        }
        else if(urls[i].href.slice(0,7) == "http://")
        {
            urlList.push(urls[i].href);
        }
        else
        {
            console.log("Error | " + urls[i].href + " is not a URL");
        }
    }
    return urlList;
}

/**
 * 
 * @param {String} baseUrl 
 * @param {String} url 
 * @param {Object} pages 
 */
async function crawlPage(baseUrl, currentURL, pages)
{
    try
    {
        let current_url = new URL(currentURL);
        let base_url = new URL(baseUrl);

        console.log('Current URL | ' + currentURL);
        console.log('Current URL hostname | ' + current_url.hostname);
        console.log('base URL | ' + baseUrl);
        console.log('base URL hostname | ' + base_url.hostname);

        if(current_url.hostname != base_url.hostname)
        {
            return pages;
        }
        let current_url_norm = normalizeURL(current_url);
        console.log('Normalized URL | ' + current_url_norm);
        if(Object.keys(pages).includes(current_url_norm))
        {
            pages.current_url_norm ++;
            return pages;
        }
        const response = await fetch(currentURL,
        {
            method: 'GET',
            mode: 'cors',
            headers: 
            {
                'Content-Type': 'text/html'
            }
        });
        if(!response.ok)
        {
            console.log(response.status + " | Error Occured while trying to fetch");
            return;
        }
        headersString = response.headers.get('content-type');
        if(!headersString.includes("text/html"))
        {
            console.log("Unexpected content-type");
            return;
        }
        body_html = await response.text();

        //gets all the urls from the current page
        let urls = getURLsFromHtml(body_html, currentURL);
        while(urls.length > 0)
        {
            pages = await crawlPage(baseUrl, urls.pop(), pages);
        }
        return pages;
    }
    catch(Error)
    {
        console.log(Error.message);
    }
    return pages;
}

module.exports = {
    normalizeURL,
    getURLsFromHtml,
    crawlPage
}