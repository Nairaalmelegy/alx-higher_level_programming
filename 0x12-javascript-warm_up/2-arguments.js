#!/usr/bin/node

if (process.argv.length === 2) {
  // if there are any other elements next to the script name
  console.log('No argument');
} else if (process.argv.length === 3) {
  // There is one next to the script name
  console.log('Argument found');
} else {
  // if there is more
  console.log('Arguments found');
}
