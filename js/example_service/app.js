// first you will need to follow the node install instructions found at:
// http://docs.uavaustin.org/guides/nodejs/getting-started/installation.html

var express = require('express');
var app = express();

app.get('/', function (req, res) {
    res.send('Hello World!');
});

app.listen(3000, function () {
    console.log('Example app listening on port 3000!');
});

// to run this, type "node app.js" in the kernel
// now go to http://localhost:3000/ in your browser!
