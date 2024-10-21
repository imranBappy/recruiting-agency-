(function () {
  function main() {
    const menuBtn = document.getElementById("menu-btn");
    const topnav = document.getElementById("topnav");

    
    


    menuBtn.addEventListener("click", () => {
      if (topnav.dataset.isopen === 'false') {
        topnav.classList.replace("-top-[1000px]","top-16")
        menuBtn.classList.replace("fa-xmark", "fa-bars")
        topnav.dataset.isopen = 'true'
      } else {
        menuBtn.classList.replace("fa-bars", "fa-xmark")
        topnav.dataset.isopen = 'false'
        topnav.classList.replace("top-16", "-top-[1000px]")
      }
    });

    const swiperEl = document.querySelector("#swiper-container2");
    Object.assign(swiperEl, {
      slidesPerView: 3,
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


  var swiper = new Swiper(".mySwiper2", {
    navigation: {
      nextEl: ".swiper-button-next",
      prevEl: ".swiper-button-prev",
    },
    autoHeight: false,
    autoplay: {
      delay: 5000,
    },
    slidesPerView: 3,
    spaceBetween: 30,
    pagination: {
      el: ".swiper-pagination",
      clickable: true,
    },
  });




function dropdownBtn(btnId, menuId) {

  const ele = document.getElementById(btnId, menuId)
  const dropdown = document.getElementById(menuId)

  if (ele.dataset.isopen === 'false') {
    ele.classList.replace("fa-plus", "fa-minus")
    dropdown.classList.replace("hidden", "block")
    ele.dataset.isopen = 'true'
  } else {
    ele.classList.replace("fa-minus", "fa-plus")
    dropdown.classList.replace("block", "hidden")
    ele.dataset.isopen = 'false'
  }
}