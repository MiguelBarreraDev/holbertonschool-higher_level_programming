#!/usr/bin/node
const callMeMoby = function (x, clb) {
  for (let i = 0; i < x; i++) {
    clb();
  }
};
exports.callMeMoby = callMeMoby;
