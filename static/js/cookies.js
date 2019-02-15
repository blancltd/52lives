var cookie_accept = document.querySelector('.cookie-notice__button_yes'),
    cookie_decline = document.querySelector('.cookie-notice__button_no');

// this cookie is used to determine if other cookies are saved
if (cookie_accept) {
    cookie_accept.addEventListener('click', function(e) {
        var date_plus_one_year = new Date(
            new Date().getTime() + 365 * 24 * 60 * 60 * 1000
        ).toGMTString();

        document.cookie =
            'cookies_accepted=true' +
            ';' +
            'expires=' +
            date_plus_one_year +
            ';path=/';
        location.reload();
    });
}

if (cookie_decline) {
    cookie_decline.addEventListener('click', function(e) {
        var date_plus_one_year = new Date(
            new Date().getTime() + 365 * 24 * 60 * 60 * 1000
        ).toGMTString();

        document.cookie =
            'cookies_accepted=false' +
            ';' +
            'expires=' +
            date_plus_one_year +
            ';path=/';
        location.reload();
    });
}
