$('.slick01').slick({
  autoplay:true,
  autoplaySpeed:1000000000,
  dots:true,
  dotsClass: 'slide-dots',
  responsive: [
    {
      breakpoint: 768,
      settings: {
        arrows: false,
      }
    }
  ]
});



$(function() {
  let tabs = $(".tab");
  $(".tab").on("click", function() {
    $(".active").removeClass(".active");
    const index = tabs.index(this);
    $(".tabBox01").removeClass("show").eq(index).addClass("show"); 
  })
})