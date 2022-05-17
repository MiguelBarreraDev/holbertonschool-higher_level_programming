#!/usr/bin/node
const axios = require('axios');
const apiUrl = process.argv[2];
const idOfWedgedAntilles = 'https://swapi-api.hbtn.io/api/people/18/';

axios.get(apiUrl)
  .then(({ data }) => {
    const results = data.results;
    const films = results.filter(film => film.characters.includes(idOfWedgedAntilles));
    console.log(films.length);
  })
  .catch(err => console.log(err.message));
