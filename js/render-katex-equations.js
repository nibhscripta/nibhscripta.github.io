function renderEQ(equation, number) {
    katex.render(equation, document.getElementById(`equation-${number}`), {
        throwOnError: false
    });
}

window.addEventListener("load", () => {
    Object.keys(equations).forEach(key =>{
        renderEQ(equations[key], key)
    })
})