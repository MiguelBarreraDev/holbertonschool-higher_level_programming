$(window).on('load', function () {
  $.ajax('https://fourtonfish.com/hellosalut/?lang=fr')
    .done(data => $('div#hello').append(data.hello))
    .fail(err => console.log(err));
});
