document.addEventListener('DOMContentLoaded', function() {
  let b = document.getElementById("addP");
  b.addEventListener("click", () => {
    let part = document.getElementById("id_email")
    let form = document.getElementById("form")
    clone = part.cloneNode(true)
    clone.value = ""
    form.appendChild(clone)
})
});