#!/usr/bin/node

const requestModule = require('request');

const movieId = process.argv[2];
const apiUrl = 'https://swapi-api.hbtn.io/api/films/';

requestModule(apiUrl + movieId, function (error, response, body) {
  if (error) throw error;

  const characterUrls = JSON.parse(body).characters;
  printCharactersInOrder(characterUrls, 0);
});

function printCharactersInOrder (characterUrls, index) {
  if (index === characterUrls.length) return;

  requestModule(characterUrls[index], function (error, response, body) {
    if (error) throw error;

    const characterName = JSON.parse(body).name;
    console.log(characterName);

    printCharactersInOrder(characterUrls, index + 1);
  });
}
