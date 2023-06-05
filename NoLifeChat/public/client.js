
//for each browser that opens
//on this port/url it creates a WebSocket
const ws = new WebSocket(`ws://${window.document.location.host}`);

ws.binaryType = "blob";

ws.addEventListener("open", (event) =>
{
    console.log("Websocket connection opened");
});

ws.addEventListener("close", (event) =>
{
    console.log("Websocket connection closed");
});

ws.onmessage = (message) =>
{
    const msgDiv = document.createElement('div');
    msgDiv.classList.add('msgCtn');
    if(message.data instanceof Blob)
    {
        reader = new FileReader();
        reader.onload = () => {
            msgDiv.innerHTML = reader.result;
            document.getElementById('messages').appendChild(msgDiv);
        };
        reader.readAsText(message.data);
    }
    else
    {
        msgDiv.innerHTML = message;
        document.getElementById('messages').appendChild(msgDiv);
    }
}
const form = document.getElementById('form');
form.addEventListener('submit', (event) =>
{
    event.preventDefault();
    const message = document.getElementById('inputBox').value;
    ws.send("[" + get_user() + "] " + message);
    document.getElementById('inputBox').value = ''
})

async function query_url(url)
{
    const urlObj = new URL(url);
    let query_params = urlObj.search;
    if(query_params != "")
    {
        query_params = query_params.slice(1, query_params.length);
        let queries = query_params.split("&");
        if(queries.length > 0)
        {
            for(let i = 0; i < queries.length; ++i)
            {
                let param = queries[i].split("=");
                if(param[0] == "user")
                {
                    let file = await get_file();
                    const keys = Object.keys(file);
                    if(keys.includes(param[1]))
                    {
                        password = (prompt("Please enter your password:"));
                        return (password == file[param[1]]) ? true : 'Incorrect password, please refresh page'
                    }
                    return 'Undefined username, please refresh page';
                }
                return "incorrect param key, expected 'user', please refresh";
            }
        }
        return "no query params";
    }
    return "http://localhost:{{port}}/?{{user}}={{username}}"
}

function get_user()
{
    const urlObj = new URL(window.location.href);
    let query_params = urlObj.search;
    if(query_params != "")
    {
        query_params = query_params.slice(1, query_params.length);
        let queries = query_params.split("&");
        if(queries.length > 0)
        {
            for(let i = 0; i < queries.length; ++i)
            {
                let param = queries[i].split("=");
                if(param[0] == "user")
                {
                    return param[1];
                }
                return "incorrect param key, expected 'user', please refresh";
            }
        }
        return "";
    }
    return ""
}

async function get_file()
{
    let response = await fetch('./users.json');
    return response.json();
}

/**
 * Main function that runs
 */
async function run()
{
    const response = await query_url(window.location.href);
    if(response != true)
    {
        remove_dom(response);
    }
    else
    {
        alert("Login Successful!");
    }
}

/**
 * removes the DOM if the password is incorrect
 * @param {String} message 
 */
function remove_dom(message)
{
    document.querySelector('.container').remove();
    element = document.createElement('a');
    element.style.fontSize = "22px";
    element.style.textDecoration = "none";
    element.href = window.location.href;
    if(message){element.innerHTML = message; }
    else{ element.innerHTML = 'Incorrect password, please refresh page'; }
    document.body.appendChild(element);
}

/**
 * Logs messages to the console, in the format
 * `[AppName] [user] [type] message | date/time stamp`
 * @param {Sting} message 
 * @param {String} type 
 */
function logger_chat(type, message, user="")
{
    return "[" + user + "] " + message;
}