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
        console.log("Result2: " + message.data);
        msgDiv.innerHTML = message.data;
        document.getElementById('messages').appendChild(msgDiv);
    }
}
const form = document.getElementById('form');
form.addEventListener('submit', (event) =>
{
    event.preventDefault();
    const message = document.getElementById('inputBox').value;
    ws.send(message);
    document.getElementById('inputBox').value = ''
})

async function query_url(url)
{
    const urlObj = new URL(url);
    let query_params = urlObj.search;
    if(query_params != "")
    {
        query_params = query_params.slice(1, -1);
        let queries = query_params.split("&");
        if(queries.length > 0)
        {
            for(let i = 0; i < queries.length; ++i)
            {
                let param = queries[i].split("=");
                if(param[0] == "user")
                {
                    console.log(await get_file());
                    const keys = Object.keys();
                    if(param[0] in keys)
                    {
                        console.log("yep");
                        return true;
                    }
                }
                return "user param not specified";
            }
        }
        return "No query params found";
    }
    return "No query params found";
}

async function get_file()
{
    let response = await fetch('./users.json');
    return response.json();
}