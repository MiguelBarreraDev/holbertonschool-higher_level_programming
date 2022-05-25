$.ajax('https://swapi-api.hbtn.io/api/films/?format=json')
  .done(({ results }) => {
    results.forEach(({ title }) => {
      $(`<li>${title}</li>`).appendTo('ul#list_movies');
    });
  })
  .catch(err => console.log(err.statusText));
