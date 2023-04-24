Object.keys(htmlSnippets).forEach(key => {
    document.getElementById(`html-snippet-${key}`).children[1].textContent = htmlSnippets[key]
})