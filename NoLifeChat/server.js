import { createServer } from 'http';
import staticHandler from 'serve-handler';
import ws, { WebSocketServer } from 'ws';

//serves a public folder named `public`
const server = createServer((req, res) =>
{
    return staticHandler(req, res, { public: 'public' })
});

//creates the server
const wss = new WebSocketServer({ server })
wss.on('connection', (client) =>
{
    console.log('Client connected !')
    client.on('message', (msg) =>
    {
        console.log(`Message:${msg}`);
        broadcast(msg)
    })
})

//sends the message to clients currently connected
function broadcast(msg)
{
    for (const client of wss.clients)
    {
        if (client.readyState === ws.OPEN)
        {
            client.send(msg)
        }
    }
}

//listens on the entered port or by default 8080
server.listen(process.argv[2] || 8080, () =>
{
    console.log(`server listening...`);
})