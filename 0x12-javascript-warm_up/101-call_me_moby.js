#!/usr/bin/node
function callMeMoby (x, clb) {
  for (let i = 0; i < x; i++) {
    clb();
  }
}
module.exports = { callMeMoby };
