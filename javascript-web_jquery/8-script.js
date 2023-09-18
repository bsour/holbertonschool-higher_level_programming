$(document).ready(function() {
  const apiUrl = 'https://swapi-api.hbtn.io/api/films/?format=json';
  
  $.get(apiUrl, function(data) {
    const movies = data.results;
    const $listMovies = $('#list_movies');
    
    $.each(movies, function(index, movie) {
      const movieTitle = movie.title;
      const $li = $('<li>').text(movieTitle);
      $listMovies.append($li);
    });
  });
});
