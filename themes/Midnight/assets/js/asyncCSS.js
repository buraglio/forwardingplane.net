var links = document.getElementsByTagName( "link" );
for( var i = 0; i < links.length; i++ ){
    var link = links[i];
    // qualify links to those with rel=preload and as=style attrs
    if (link.getAttribute("rel") === "preload" && link.getAttribute("as") === "style") {
        loadCSS(link.getAttribute("href"));
    }
}

