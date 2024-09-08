#!/usr/bin/node

const request = require('request');

const movieId = process.argv[2];
const apiUrl = `https://swapi-api.alx-tools.com/api/films/${movieId}`;

// Send a GET request to fetch the movie details
request(apiUrl, (error, response, body) => {
  if (error) {
    console.error(error);
  } else {
    const filmData = JSON.parse(body);
    const characters = filmData.characters;
    printCharactersInOrder(characters);
  }
});

// Function to print characters in the correct order
function printCharactersInOrder(characters) {
  const promises = characters.map((characterUrl) => {
    return new Promise((resolve, reject) => {
      request(characterUrl, (error, response, body) => {
        if (error) {
          reject(error);
        } else {
          const characterData = JSON.parse(body);
          resolve(characterData.name);
        }
      });
    });
  });

  // Wait for all requests to finish and print names in order
  Promise.all(promises).then((names) => {
    names.forEach((name) => console.log(name));
  });
}
