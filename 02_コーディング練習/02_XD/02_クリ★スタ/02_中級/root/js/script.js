$('.slick01').slick({
  // autoplay: true,
  // autoplaySpeed: 5000,
  variableWidth: true,
  centerMode: true,
  responsive: [{
    breakpoint: 768,
    settings: {
      centerMode: true,
    }
  }]
});


$(function () {
  const ua = navigator.userAgent;
  if (ua.indexOf('iPhone') > -1 || (ua.indexOf('Android') > -1 && ua.indexOf('Mobile') > -1)) {
    $(function(){
      $(window).scroll(function(){
        if($(this).scrollTop() > 291){
          $('.header').addClass('fixed');
        } else {
          $('.header').removeClass('fixed');
        }
      });
    });
  } else {
    $(function(){
      $(window).scroll(function(){
        if($(this).scrollTop() > 652){
          $('.header').addClass('fixed');
        } else {
          $('.header').removeClass('fixed');
        }
      });
    });
  }
});

// スムーズスクロール
$(function(){
  $('a[href^="#"]').click(function(){
    var speed = 500;
    var href = $(this).attr("href");
    var target = $(href == "#" || href == "" ? 'html' : href);
    var position = target.offset().top;
    $("html, body").animate({scrollTop:position}, speed, "swing");
    return false;
  });
});

//ハンバーガーメニュー
$('.headerNavToggle').on('click',function(){
  $('.headerNavToggle, .headerNav').toggleClass('show');
});

// リンクをクリックしたらメニューを閉じる
$('#headerNavList a[href]').on('click', function(event) {
  $('.headerNavToggle').trigger('click');
});
