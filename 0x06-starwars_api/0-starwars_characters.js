#!/usr/bin/node
const request = require('request');

// Check if a movie ID was provided
if (process.argv.length !== 3) {
  console.log('Usage: ./0-starwars_characters.js <movie_id>');
  process.exit(1);
}

const movieId = process.argv[2];

// Define the URL for the Star Wars API
const url = `https://swapi.dev/api/films/${movieId}/`;

// Make a request to the Star Wars API
request(url, (error, response, body) => {
  if (error) {
    console.error('Error:', error);
    return;
  }

  if (response.statusCode !== 200) {
    console.error('Failed to fetch data. Status code:', response.statusCode);
    return;
  }

  try {
    const film = JSON.parse(body);
    const characterUrls = film.characters;

    // Fetch character names
    characterUrls.forEach((characterUrl) => {
      request(characterUrl, (error, response, body) => {
        if (error) {
          console.error('Error:', error);
          return;
        }

        if (response.statusCode !== 200) {
          console.error('Failed to fetch data. Status code:', response.statusCode);
          return;
        }

        try {
          const character = JSON.parse(body);
          console.log(character.name);
        } catch (e) {
          console.error('Failed to parse character data:', e);
        }
      });
    });
  } catch (e) {
    console.error('Failed to parse film data:', e);
  }
});
