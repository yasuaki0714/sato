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

// カルーセル
$(function(){
  $('.center-item').slick({
    infinite: true,
    dots: true,
    arrows: true,
    slidesToshow: 1,
    centerMode: true,
    centerPadding: '100px',
    autoplay: true,
    responsive: [{
      breakpoint: 480,
      settings: {
        enterMode: false,
      }
    }]
  });
});