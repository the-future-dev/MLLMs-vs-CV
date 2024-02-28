var http = require('http');
var url = require('url');
var fs = require('fs');
var path = require('path');

var port = 8080;
var frontDirectory = "./frontend";

http.createServer(function (request, response) {
    try {
        var requestUrl = url.parse(request.url);
        var fsPath = frontDirectory+path.normalize(requestUrl.pathname);

        if (requestUrl.pathname  == '/') {
            fsPath = frontDirectory + '/index.html';
        };

        var fileStream = fs.createReadStream(fsPath);
        
        fileStream.pipe(response);
        
        fileStream.on('open', function() {
             response.writeHead(200);
        });

        fileStream.on('error',function(e) {
             response.writeHead(404);     // assume the file doesn't exist
             response.end();
        });

   } catch(e) {
        response.writeHead(500);
        response.end();
        console.log(e.stack);
   };

}).listen(port);

console.log("Running on http://localhost:"+port);