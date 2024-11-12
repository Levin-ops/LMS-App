// Changing navbar style on scroll

window.addEventListener("scroll", () => {
  document
    .querySelector("nav")
    .classList.toggle("window_scroll", window.scrollY > 0);
});

// Show faq answer

const faqs = document.querySelectorAll(".faq");

faqs.forEach((faq) => {
  faq.addEventListener("click", () => {
    faq.classList.toggle("show");

    const icon = faq.querySelector(".faqs_icon i");

    if (icon.className === "uil uil-plus") {
      icon.className = "uil uil-minus";
    } else {
      icon.className = "uil uil-plus";
    }
  });
});

// display Nav

const navMenu = document.querySelector(".nav_menu");
const menuBtn = document.querySelector("#open_menu_btn");
const closeBtn = document.querySelector("#close_menu_btn");

menuBtn.addEventListener("click", () => {
  navMenu.style.display = "flex";
  closeBtn.style.display = "inline-block";
  menuBtn.style.display = "none";
});

// close Menu
const closeNav = () => {
  navMenu.style.display = "none";
  closeBtn.style.display = "none";
  menuBtn.style.display = "inline-block";
};

closeBtn.addEventListener("click", closeNav);
