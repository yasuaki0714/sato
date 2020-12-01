// ハンバーガーメニュー
$('.headerMenuToggle').on('click',function() {
  $('.headerMenuToggle, .headerNav').toggleClass('show');
});

// リンクをクリックしたらメニューを閉じる
$('#headerNavList a[href]').on('click', function(event) {
  $('.headerMenuToggle').trigger('click');
});

// スクロールしたら背景色変更 SP/PC
$(function () {
  const ua = navigator.userAgent;
  if (ua.indexOf('iPhone') > -1 || (ua.indexOf('Android') > -1 && ua.indexOf('Mobile') > -1)) {
    $(function(){
      $(window).scroll(function(){
        if($(this).scrollTop() > 291){
          $('#headerMenuWrap').addClass('colorChange');
        } else {
          $('#headerMenuWrap').removeClass('colorChange');
        }
      });
    });
  } else {
    $(function(){
      $(window).scroll(function(){
        if($(this).scrollTop() > 566){
          $('#headerMenuWrap').addClass('colorChange');
        } else {
          $('#headerMenuWrap').removeClass('colorChange');
        }
      });
    });
  }
})

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