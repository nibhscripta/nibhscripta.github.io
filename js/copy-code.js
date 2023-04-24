const codeSnippetBlocks = document.querySelectorAll("code")

codeSnippetBlocks.forEach(codeSnippetELement => {
    codeSnippetELement.children[0].addEventListener("click", () => {
        navigator.clipboard.writeText(codeSnippetELement.children[1].textContent)
    })
});