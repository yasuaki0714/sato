// スムーズスクロール
$('a[href^="#"]').click(function(){
  var speed = 500;
  var href= $(this).attr("href");
  var target = $(href == "#" || href == "" ? 'html' : href);
  var position = target.offset().top;
  $("html, body").animate({scrollTop:position}, speed, "swing");
  return false;
});

// スクロールするとページトップボタンが現れる
$(function(){
  var topBtn = $('#pageTopBtn');
  topBtn.hide();
  $(window).scroll(function(){
    if($(this).scrollTop() > 100){
      topBtn.fadeIn();
    } else {
      topBtn.fadeOut();
    }
  })
});


$('.slick01').slick({
  dots: true,
  // autoplay: true,
  // autoplaySpeed: 500,
  centerMode: true,
  centerPadding: '80px',
});

$('.slick02').slick({
  dots: true,
  infinite: false,
  centerPadding: '50px',
  slidesToShow: 3,
  slidesToScroll: 3,
});

$('.slick03').slick({
  dots: true,
  infinite: false,
  centerPadding: '50px',
  slidesToShow: 2,
  slidesToScroll: 2,
});