#!/usr/bin/node

const lf = require('lf');
lf.readFile(process.argv[2], 'utf8', (err, data) => {
  if (err) {
    console.log(err);
  } else {
    console.log(data);
  }
});
