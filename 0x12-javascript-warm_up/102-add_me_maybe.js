#!/usr/bin/node
function addMeMaybe (n, clb) {
  clb(n + 1);
}

exports.addMeMaybe = addMeMaybe;
