===========================

https://en.wikipedia.org/wiki/WebSocket

    - bi-directional communication
         https://www.rfc-editor.org/rfc/rfc6455 - the doc

    - initially over http, then client sends header: 'Connection: Upgrade' 'Upgrade: websocket' + additional headers, in order to change from http to websocket protocol.

        Request:

            GET /chat HTTP/1.1
            Host: server.example.com
            Upgrade: websocket
            Connection: Upgrade
            Sec-WebSocket-Key: dGhlIHNhbXBsZSBub25jZQ==
            Origin: http://example.com
            Sec-WebSocket-Protocol: chat, superchat
            Sec-WebSocket-Version: 13

        Response:  Sec-WebSocket-Accept value is some sha signature over the request value Sec-WebSocket-Key + <some uuid>
    
            HTTP/1.1 101 Switching Protocols
            Upgrade: websocket
            Connection: Upgrade
            Sec-WebSocket-Accept: s3pPLMBiTxaQ9kYGzzhZRbK+xOo=

 
       Further requests in WebSocket are in frames
            (bi directional - either part can send)

        - php Ratchet: 

            // bad news: you can't just upgrade a http connection of you php web request handler. You need to make a standalone script that listens to incoming WebSocket request.

            // simple chat server (that's how they do event driven stuff)

            $server =  Ratchet\Server\IoServer::factory(     // creates listening socke0wwt and event loop wrapper (IoServer), 
                                                             // the connect events are handled and create IoConnection)
                new Ratchet\Http\HttpServer(                 // parses http messages             
                    new Ratchet\WebSocket\WsServer(          // parsing of websocket handshake and frame messages 
                        new Chat()                           // application level class that handles messages
                    )
                ),
                8080
             );
             $server->run(); // run event loop.

            // server side action goes here
            class WsServer implements HttpServerInterface {

                
                // ComponentInterface - the application that consumes messages
                public function __construct(ComponentInterface $component) {

                public function onOpen(ConnectionInterface $conn, RequestInterface $request = null) {

                    // handle handshake
                    \Ratchet\RFC6455\Handshake\ServerNegotiator - handshake method ::: does the handshake.


        
        - Ratchet: working with sockets:
            
            Ratchet\Server\IoConnection - asynchronous socket handler
                - constructor receives derived class of \\React\\Socket\\ConnectionInterface

                - \React\Socket\Connection // wraps a stream/socket so that it does the ConnectionInterface!
                        public function __construct($resource, LoopInterface $loop)

        - every server passed to a ratched event loop handles:

            interface MessageInterface {

                function onMessage(ConnectionInterface $clientConnection, $msg);

