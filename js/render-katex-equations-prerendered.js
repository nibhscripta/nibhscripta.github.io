window.addEventListener("load", () => {
    Object.keys(equationsPreRendered).forEach(key =>{
        document.getElementById(`equation-${key}`).innerHTML = equationsPreRendered[key]
    })
})