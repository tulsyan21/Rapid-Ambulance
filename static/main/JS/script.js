jQuery(document).ready(function ($) {
    var alterClass = function () {
        var ww = document.body.clientWidth;
        if (ww < 800) {
            $('#collapseOne').removeClass('show');
        } else if (ww >= 401) {
            $('#collapseOne').addClass('show');
        };
    };
    $(window).resize(function () {
        alterClass();
    });
    //Fire it when the page first loads:
    alterClass();
});

// navigator.geolocation.getCurrentPosition(function (location) {
//     $('#Latitude').text(location.coords.latitude)
//     $('#Longitude').text(location.coords.longitude)
//     $('#Accuracy').text(location.coords.accuracy)
    
    
//     // console.log(location.coords.latitude);
//     // console.log(location.coords.longitude);
//     // console.log(location.coords.accuracy);
// });