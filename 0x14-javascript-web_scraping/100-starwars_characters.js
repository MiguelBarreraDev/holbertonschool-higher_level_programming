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
  let nameList = [];

  try {
    const charactersList = await getCharactersFromFilm({id: ID});
    for (let char of charactersList) {
      let name = await getCharName(char);
      nameList.push(name);
    }
  } catch (err) {
    console.error(err.message);
    return err;
  }

  console.log(nameList.join("\n"));
  return 1;
}

main(ID);
