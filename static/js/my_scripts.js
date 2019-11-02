// I learned by reading this post how to scroll automatically on hover
// https://stackoverflow.com/questions/18188952/scroll-on-hover-click-for-speed

// I learned and used the code from from the following link in order to
// display a .gif icon while the page loads
// https://smallenvelop.com/display-loading-icon-page-loads-completely/


$(document).ready(function() {
  // code use to display loaded
  $(window).load(function() {
    // Animate loader off screen
    $(".loader").fadeOut("slow");
  });

  // code used to autoscroll books in all_books.html
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
