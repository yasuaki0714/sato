
// ハンバーガーメニュー
$(function(){
  $('.sidebar__menu__btn').click(function(){
    $(this).toggleClass('.close')
    if($('.sidebar__menu__list').hasClass(".colse")){
      $('.sidebar__menu__list').removeClass('close');
      $('.sidebar__menu__list').removeClass('open');
    };
    
  });
});


// スライダー
$(function(){
  $('.footer__slider').slick({
    autoplay: true
  });
});


