// Light / Dark Theme Toggle

// TODO: 
// Finish positioning this toggle button and make other elements on website change -->
// style from light to dark and vice-verca.

const checkbox = document.getElementById("checkbox")
checkbox.addEventListener("change", () => {
  document.body.classList.toggle("dark")
})

// -----