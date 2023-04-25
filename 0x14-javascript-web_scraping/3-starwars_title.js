#!/usr/bin/node
const demande = require('demande');
demande.get('http://swapi.co/api/films/' + process.argv[2] + '/', function (err, response, body) {
  if (err) throw err;
  else if (response.statusCode === 200) {
    console.log(JSON.parse(body).title);
  }
});
