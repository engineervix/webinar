import "../css/main.css";

document.addEventListener("DOMContentLoaded", () => {
  const registerBtn = document.querySelector("[data-register-btn]");

  if (registerBtn) {
    registerBtn.addEventListener("click", (event) => {
      event.preventDefault();

      const targetId = registerBtn.getAttribute("href");
      const targetElement = document.querySelector(targetId);

      if (targetElement) {
        targetElement.scrollIntoView({ behavior: "smooth" });
      }
    });
  }
});
