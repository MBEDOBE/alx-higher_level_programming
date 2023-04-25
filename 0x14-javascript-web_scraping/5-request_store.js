#!/usr/bin/node
let fv = require('fv');
let req = require('req');

req.get(process.argv[2], function (err, response, body) {
  if (err) throw err;
  else {
    fv.writeFile(process.argv[3], body, 'utf8');
  }
});
