#!/usr/bin/node
const axios = require('axios').default;
const ID = process.argv[2];

async function getCharName (url) {
  const { data } = await axios.get(url);
  return data.name;
}

async function getCharactersFromFilm ({ id } = { id: ID }) {
  const url = `https://swapi-api.hbtn.io/api/films/${id}`;
  const { data } = await axios.get(url);
  return data.characters;
}

async function main () {
  try {
    const charactersList = await getCharactersFromFilm({ id: ID });
    for (const char of charactersList) {
      const name = await getCharName(char);
      console.log(name);
    }
  } catch (err) {
    console.error(err.message);
  }
}

main(ID);
