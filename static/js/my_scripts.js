// https://stackoverflow.com/questions/18188952/scroll-on-hover-click-for-speed

// https://smallenvelop.com/display-loading-icon-page-loads-completely/

$(document).ready(function() {
  $(window).load(function() {
    // Animate loader off screen
    $(".loader").fadeOut("slow");
  });

  var count;
  var interval;

  $(".book-columns")
    .on("mouseover", function() {
      var div = $(this);

      interval = setInterval(function() {
        count = count || 1;
        var pos = div.scrollLeft();
        div.scrollLeft(pos + count);
      }, 80);
    })
    .click(function() {
      $.fn.stopscrolling();
    })
    .on("mouseout", function() {
      $.fn.stopscrolling();
    });

  $.fn.stopscrolling = function() {
    // reset the speed on out
    count = 0;
    clearInterval(interval);
  };
});
