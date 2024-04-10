document.addEventListener("DOMContentLoaded", function () {
  
  const password = document.getElementById("password");
  const toggle = document.getElementById("iconoTogglePassword");

  toggle.addEventListener("click", () => {
    if (password.type === "password") {
      password.type = "text";
      toggle.src=togglePasswordIcono;
    }else {
      password.type = "password";
      toggle.src =togglePasswordIconoOculta;
    }
  });
});
