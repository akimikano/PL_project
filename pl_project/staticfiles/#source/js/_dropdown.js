$(function () {
    $(".dropToggle").on("click", function (e) {
        $(".dropToggleContent").toggleClass("show");
    });
    $(document).on("click", function (e) {
        if ($(e.target).is(".dropToggle, .dropToggle .item") === false) {
            $(".dropToggleContent").removeClass("show");
        }
    });
});


$(function () {
    $(".menu-wrapper").on("click", function (e) {
        $(".hamburger-menu").toggleClass("animate");
        $(".hamburger-menu-dropdown").toggleClass("show");
    });
    $(document).on("click", function (e) {
        if ($(e.target).is(".menu-wrapper, .hamburger-menu-dropdown, .hamburger-menu") === false) {
            $(".hamburger-menu").removeClass("animate");
            $(".hamburger-menu-dropdown").removeClass("show");
        }
    });
});


// select your header or whatever element you wish
const header = document.querySelector("header");

const headroom = new Headroom(header);
headroom.init();

AOS.init({
    duration: 1000,
    easing: 'ease-out-back',
});


$(document).ready(function(){
    $( "a.scrollLink" ).click(function( event ) {
        event.preventDefault();
        $("html, body").animate({ scrollTop: $($(this).attr("href")).offset().top - 80}, 500);
    });
});