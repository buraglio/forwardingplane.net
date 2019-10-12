var elems = document.getElementsByClassName('katex-container');
for (var i = 0; i < elems.length; i++) {
    renderMathInElement(
        elems[i],
        { delimiters: [
                {left: "$$", right: "$$", display: true},
                {left: "\\[", right: "\\]", display: true},
                {left: "$", right: "$", display: false},
                {left: "\\(", right: "\\)", display: false}
            ]}
    );
}