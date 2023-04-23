const codes = document.querySelectorAll("code")

codes.forEach(element => {
    element.children[0].addEventListener("click", () => {
        navigator.clipboard.writeText(element.children[1].textContent)
    })
});