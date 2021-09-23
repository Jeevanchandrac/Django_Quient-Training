/*-------------------- Testimonals  -------------------*/
$(document).ready(function () {

    $("#owl-example").owlCarousel();
  
  });
  
  $(document).ready(function(){
    $("#testimonial-slider").owlCarousel({
        items:1,
        itemsDesktop:[1000,2],
        itemsDesktopSmall:[979,1],
        itemsTablet:[768,1],
        pagination:true,
        navigation:false,
        slideSpeed:1000,
        singleItem:true,
        transitionStyle:"goDown",
        navigationText:["",""],
        autoPlay:true
    });
  });
  
  /*--------------------	gallery -------------------*/
  
  $(document).ready(function () {
  
    $(".filter-button").click(function () {
      var value = $(this).attr('data-filter');
  
      if (value == "all") {
        $('.filter').show('1000');
      }
      else {
        $(".filter").not('.' + value).hide('3000');
        $('.filter').filter('.' + value).show('3000');
  
      }
  
      if ($(".filter-button").removeClass("active")) {
        $(this).removeClass("active");
      }
      $(this).addClass("active");
    });
  });
  
  
  $(document).ready(function () {
    $(".fancybox").fancybox({
      openEffect: "none",
      closeEffect: "none"
    });
  });
 
  
  
  