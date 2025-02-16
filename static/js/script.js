// Get elements
const loginToggle = document.getElementById("login-toggle");
const signupToggle = document.getElementById("signup-toggle");
const formsWrapper = document.querySelector(".forms-wrapper");
const loginForm = document.getElementById("login-form");

// Add event listeners for toggling
loginToggle.addEventListener("click", () => {
  formsWrapper.classList.remove("sign-up-mode"); // Reset to show login form
  loginToggle.classList.add("active");
  signupToggle.classList.remove("active");
});

signupToggle.addEventListener("click", () => {
  formsWrapper.classList.add("sign-up-mode"); // Shift to show signup form
  signupToggle.classList.add("active");
  loginToggle.classList.remove("active");
});

// Add event listener for login form submission
loginForm.addEventListener("submit", (event) => {
  event.preventDefault(); // Prevent the default form submission behavior

  // Validate inputs
  const email = document.getElementById("login-email").value;
  const password = document.getElementById("login-password").value;

  if (email.trim() === "" || password.trim() === "") {
    alert("Please fill in all fields before logging in.");
    return;
  }

  // Redirect to dashboard
  window.location.href = "/dashboard";
});