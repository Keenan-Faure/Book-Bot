/**
 * Normalizes a url and returns it
 * @param {string} url 
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

module.exports = {
    normalizeURL
}