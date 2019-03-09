var express = require('express');
var request = require('request');
var path = require("path");
var bodyParser = require('body-parser');
var app = express();
app.use(bodyParser.urlencoded({ extended: false }))
app.use(bodyParser.json());

app.use(express.static(__dirname + '/client/dist/'));

 app.post('/testalexa', function(req, res){

  res.send(JSON.stringify(
{
  "fulfillmentText": "This is a text response",
  "fulfillmentMessages": [
    {
      "text": {
        "text": ["How you going"],
      }
    }
  ],
  "source": "example.com",
  "payload": {
    "google": {
      "expectUserResponse": true,
      "richResponse": {
        "items": [
          {
            "simpleResponse": {
              "textToSpeech": "this is a simple response"
            }
          }
        ]
      }
    }
  }
})

  )}
);

app.listen(3000, ()=>{console.log('Running on 3000')});