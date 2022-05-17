#!/usr/bin/node
const axios = require('axios');
const apiUrl = process.argv[2];
const idOfWedgedAntilles = 'https://swapi-api.hbtn.io/api/people/18/';

(async (films = []) => {
  try {
    const { data } = await axios.get(apiUrl);
    const { results } = data;
    films = results.filter(film => film.characters.includes(idOfWedgedAntilles));
    console.log(films.length);
  } catch (err) {
    console.error(err.message);
  }
})();
