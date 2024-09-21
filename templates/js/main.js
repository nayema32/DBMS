$(document).ready(function(){
	//wow js
	new WOW().init();
	//owl carousel
	$('.owl-carousel').owlCarousel({
		loop:true,
		margin:10,
		nav:true,
		dots:false,
		autoplay:true,
		autoplayTimeout:2000,
		autoplayHoverPause:true,
		responsive:{
			0:{
				items:1
			},
			600:{
				items:3
			},
			1000:{
				items:5
			}
		}
	});
	//Scroll Top
	$(window).scroll(function(){
		if($(this).scrollTop()>200){
			$(".back_to_top").fadeIn();
		}else
		{
			$(".back_to_top").fadeOut();
		}
		
	});
	$(".back_to_top").click(function(){
		$("html,body").animate({scrollTop:0},1000);
	});
	//counter up
	$('.counter').counterUp();
});