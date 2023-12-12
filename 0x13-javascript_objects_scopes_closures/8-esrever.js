#!/usr/bin/node
exports.esrever = function (list) {
  let length = list.length - 1;
  let x = 0;
  while ((length - x) > 0) {
    const tmp = list[length];
    list[length] = list[x];
    list[x] = tmp;
    x++;
    length--;
  }
  return list;
};
