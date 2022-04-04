#!/usr/bin/node
exports.callMeMoby = function (x, clb) {
  for (let i = 0; i < x; i++) {
    clb();
  }
};
