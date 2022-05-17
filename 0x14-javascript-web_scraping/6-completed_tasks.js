#!/usr/bin/node
const axios = require('axios');
const url = process.argv[2];

axios.get(url)
  .then(({ data }) => {
    const taskForUser = {};
    data.forEach(e => {
      if (taskForUser[e.userId] === undefined) taskForUser[e.userId] = 0;
      if (e.completed) taskForUser[e.userId]++;
    });
    console.log(taskForUser);
  })
  .catch(err => console.log(err.message));
