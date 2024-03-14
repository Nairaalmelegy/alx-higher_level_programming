#!/usr/bin/node

if (process.argv[2] === undefined) {
  // check if there is no arguments found
  console.log('No argument');
} else {
  console.log(process.argv[2]);
}
