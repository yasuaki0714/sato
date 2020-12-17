//　ハンバーガーメニュー
$('.spMenuToggle').on('click',function() {
  $('.spMenuToggle, .spNav, .open, .close').toggleClass('show');
});

//　ページ内検索　モーダル
$('.surchBtn').on('click',function() {
  $('.surchMordal').toggleClass('show');
});

$(function(){
  $('.surchMordal').click(function(){
    $('.surchMordal').toggleClass('show');
  });
  $('#searchform').on('click', function(e){
    e.stopPropagation();
  })
});

// スムーズスクロール
$('a[href^="#"]').click(function(){
  var speed = 500;
  var href= $(this).attr("href");
  var target = $(href == "#" || href == "" ? 'html' : href);
  var position = target.offset().top;
  $("html, body").animate({scrollTop:position}, speed, "swing");
  return false;
});

// スクロールするとページトップボタンが現れる PC
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
$('.slick01').slick({
  dots: true,
  arrows: true,
  prevArrow:'<div class="prev">＜</div>',
	nextArrow:'<div class="next">＞</div>',
  autoplay: true,
  autoplaySpeed: 5000,
  centerMode: true,
  centerPadding: '5%',
  responsive: [{
    breakpoint: 767,
    settings: {
      arrows: false,
      centerMode: false,
      centerPadding: '0',
    }
  }]
});

$('.slick02').slick({
  dots: true,
  infinite: false,
  centerPadding: '50px',
  slidesToShow: 3,
  slidesToScroll: 3,
  variableWidth: true,
  arrows: true,
  prevArrow:'<div class="prev">＜</div>',
	nextArrow:'<div class="next">＞</div>',
});

$('.slick03').slick({
  dots: true,
  infinite: false,
  centerPadding: '50px',
  slidesToShow: 2,
  slidesToScroll: 2,
});