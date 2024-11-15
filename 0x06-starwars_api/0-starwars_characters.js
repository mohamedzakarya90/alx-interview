#!/usr/bin/node
/**
 * The wrapper function for requesting object that allows it
 * for working with async and await
 * param   {String} url -> site url
 * returns {Promise}    -> promising object which resolves
 *                         with the parsed JSON response
 *                         and rejecting with request error
 */
function makeRequest (url) {
  const request = require('request');
  return new Promise((resolve, reject) => {
    request.get(url, (error, response, body) => {
      if (error) reject(error);
      else resolve(JSON.parse(body));
    });
  });
}

/**
 * The entry point -> making requests to the star wars API
 * movie info based on the movie ID which is passed as CLI parameter
 * retrieving movie character info and it then prints their names
 * which is in order of appearance in initial response
 */
async function main () {
  const args = process.argv;

  if (args.length < 3) return;

  const movieUrl = 'https://swapi-api.alx-tools.com/api/films/' + args[2];
  const movie = await makeRequest(movieUrl);

  if (movie.characters === undefined) return;
  for (const characterUrl of movie.characters) {
    const character = await makeRequest(characterUrl);
    console.log(character.name);
  }
}

main();
