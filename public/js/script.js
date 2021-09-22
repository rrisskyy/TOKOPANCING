
const swiper = new Swiper('.swiper', {
  slidesPerView: 1,
  spaceBetween: 0,
  loop:true,
  // init: false,
  pagination: {
    el: '.swiper-pagination',
    clickable: true,
  },
  breakpoints: {
    640: {
      slidesPerView: 1,
      spaceBetween: 0,
    },
    856: {
      slidesPerView: 2,
      spaceBetween: 0,
    },
    1152: {
      slidesPerView: 3,
      spaceBetween: 0,
    },
    1556: {
      slidesPerView: 4,
      spaceBetween: 0,
    },
  },
  // navigation: {
  //   nextEl: '.swiper-button-next',
  //   prevEl: '.swiper-button-prev',
  // },

});

const swiper1 = new Swiper('.swiper1', {
  spaceBetween: 30,
  centeredSlides: true,
  loop: true,
  autoplay: {
    delay: 2500,
    disableOnInteraction: false,
  },  
  navigation: {
    nextEl: '.swiper-button-next',
    prevEl: '.swiper-button-prev',
  },
  pagination: {
    el: '.swiper-pagination',
    clickable: true,
  }
});

