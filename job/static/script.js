(function () {
  function main() {
    const menuBtn = document.getElementById("menu-btn");
    const topnav = document.getElementById("topnav");

    menuBtn.addEventListener("click", () => {
      if (topnav.style.display === "none") {
        topnav.style.display = "block";
      } else {
        topnav.style.display = "none";
      }
    });

    const swiperEl = document.querySelector("#swiper-container");
    Object.assign(swiperEl, {
      slidesPerView: 1,
      spaceBetween: 10,
      pagination: {
        clickable: true,
      },
      breakpoints: {
        640: {
          slidesPerView: 2,
          spaceBetween: 20,
        },
        768: {
          slidesPerView: 4,
          spaceBetween: 40,
        },
        1024: {
          slidesPerView: 5,
          spaceBetween: 50,
        },
      },
    });
    swiperEl.initialize();
  }
  document.addEventListener("DOMContentLoaded", main);
})();
