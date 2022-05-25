$(window).on('load', () => {
  $('input#btn_translate').on('click', () => {
    const code = $('input#language_code').val();
    $.ajax(`https://www.fourtonfish.com/hellosalut/?lang=${code}`)
      .done(data => $('div#hello').text(data.hello))
      .fail(err => console.log(err));
  });
});
