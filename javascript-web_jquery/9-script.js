$(document).ready(function() {
  const apiUrl = 'https://hellosalut.stefanbohacek.dev/?lang=fr';
  $.get(apiUrl, function(data) {
    const translation = data.hello;
    $('#hello').text(translation);
  });
});
