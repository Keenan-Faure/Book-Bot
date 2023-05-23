const { createServer } = require('http');
const staticHandler = require('serve-handler');
const { WebSocketServer } = require('ws');
const ws = require('ws');

//serves a public folder named `public`
const server = createServer((req, res) =>
{
    return staticHandler(req, res, { public: 'public' })
});

//creates the server
const wss = new WebSocketServer({ server })
wss.on('connection', (client) =>
{
    client.on('message', (msg) =>
    {
        broadcast(msg);
    });
})

//sends the message to clients currently connected
function broadcast(msg)
{
    for (const client of wss.clients)
    {
        if (client.readyState === ws.OPEN)
        {
            client.send(msg);
        }
    }
}

//listens on the entered port or by default 8080
server.listen(process.argv[2] || 8080, () =>
{
    console.log(`server listening...`);
})