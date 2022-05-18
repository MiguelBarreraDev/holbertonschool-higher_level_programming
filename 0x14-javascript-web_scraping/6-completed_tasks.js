#!/usr/bin/node
const axios = require('axios');
const apiUrl = process.argv[2];
const result = {};

axios.get(apiUrl)
  .then(({ data }) => {
    data.forEach(task => {
      if (result[task.userId] === undefined) result[task.userId] = 0;
      if (task.completed) result[task.userId]++;
    });
    console.log(result);
  })
  .catch(({ message }) => console.log(message));
