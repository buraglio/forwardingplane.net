var header = document.getElementById("site-header").getElementsByTagName("header")[0];
var title = document.getElementById("site-title-container");
var thumbnail = document.getElementById("site-thumbnail");
// Make constant because it is 0 when hidden
var thumbnailTimeout;
function showHideThumbnail() {
    if (!thumbnailTimeout) {
        thumbnailTimeout = setTimeout(function() {
            thumbnailTimeout = null;
            const THUMB_WIDTH = parseInt(thumbnail.getAttribute("data-width")) + parseInt((window.getComputedStyle(thumbnail)).getPropertyValue("padding-right"));
            const HEADER_PADDING = parseInt(window.getComputedStyle(header).getPropertyValue("padding-right"), 10) + parseInt(window.getComputedStyle(header).getPropertyValue("padding-left"), 10);
            const TITLE_WIDTH = parseInt(window.getComputedStyle(title).getPropertyValue("margin-left"), 10) + parseInt(window.getComputedStyle(title).getPropertyValue("margin-right"), 10) + parseInt(window.getComputedStyle(title).getPropertyValue("padding-left"), 10) + parseInt(window.getComputedStyle(title).getPropertyValue("padding-right"), 10);
            contentWidth = THUMB_WIDTH + HEADER_PADDING + TITLE_WIDTH + title.scrollWidth
            if (contentWidth > header.scrollWidth) {
                thumbnail.classList.add("hide");
                header.classList.add("small-text-center");
                header.classList.add("align-center")
                header.classList.remove("small-text-left");
            } else {
                header.classList.add("small-text-left");
                header.classList.remove("small-text-center");
                header.classList.remove("align-center");
                thumbnail.classList.remove("hide");
            }
        }, 70);
    }
}
window.addEventListener("load", showHideThumbnail);
window.addEventListener("resize", showHideThumbnail);
