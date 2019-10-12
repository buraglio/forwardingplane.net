{{- $host := $.Site.Params.matomo.host -}}
var _paq = _paq || [];
_paq.push(['trackPageView']);
_paq.push(['enableLinkTracking']);
(function() {
    var u="{{ $host }}/";
    _paq.push(['setTrackerUrl', u+'piwik.php']);
    _paq.push(['setSiteId', '{{ $.Site.Params.matomo.site_id | default 1 }}']);
    var d=document, g=d.createElement('script'), s=d.getElementsByTagName('script')[0];
    g.type='text/javascript'; g.async=true; g.defer=true; g.src=u+'piwik.js'; s.parentNode.insertBefore(g,s);
})();
function ajax(url) {
    return new Promise(function(resolve, reject){
        var req = new XMLHttpRequest();
        req.open("GET", url, true);
        req.withCredentials = true;
        req.onload = function() {
            var status = req.status;
            if (status === 200)
                resolve(req.response);
            else
                reject(status);
        };
        req.send(null);
    });
}

function isTracked(data) {
    var dom = (new DOMParser()).parseFromString(data, "application/xml");
    return dom.getElementsByTagName("result")[0].innerHTML === "1"
}

function updateAnalyticsText() {
    ajax('{{ $host | safeJS }}/index.php?module=API&method=AjaxOptOut.isTracked')
    .then(function(data){
        console.log("Update: " + isTracked(data));
        document.getElementById("toggle-tracking").innerText = isTracked(data) ? "{{ i18n "optOut" | title }}" : "{{ i18n "optIn" | title }}";
    });
}

function toggleHandler(event) {
    event.preventDefault();
    event.stopPropagation();
    ajax("{{ $host | safeJS }}/index.php?module=API&method=AjaxOptOut.isTracked")
    .then(function(data) {
        console.log("Toggle: " + isTracked(data));
        ajax('{{ $host | safeJS }}/index.php?module=API&method=AjaxOptOut.do' + (isTracked(data) ? 'Ignore' : 'Track')).then(updateAnalyticsText);
    });
}

document.getElementById("toggle-tracking").addEventListener("click", toggleHandler);
window.addEventListener("load", updateAnalyticsText);

