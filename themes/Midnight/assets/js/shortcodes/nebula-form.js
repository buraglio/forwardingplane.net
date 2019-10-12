function formSubmitFunc(form) {
    return function(e){
        e.preventDefault();
        e.stopPropagation();
        e.returnValue = false
        
        var xhr = new XMLHttpRequest();
        
        var stat = document.getElementById(form.getAttribute("name") + "-status");
        stat.classList.add("hide");

        xhr.addEventListener("load", function(e){
            if (xhr.status == 200) {
                stat.innerHTML = "<p>Form submitted!</p>";
            } else {
                stat.innerHTML = "<p>Error occurred while processing form.</p><p>" +
                    xhr.responseText + "</p>"
            }
            stat.classList.remove("hide");
        });
        
        xhr.addEventListener("error", function(e){
            stat.innerHTML = "<p>A server error occurred. <em>The form was not submitted.</em> Please try again later.</p>"
            stat.classList.remove("hide");
        });
       
        // Use "action" and not "data-action" for cases of no javascript
        xhr.open("POST", form.getAttribute("action"));
        
        var data = new FormData(form);
        
        xhr.send(data);
        return false
    }
}

var forms = document.getElementsByTagName("form");
for (var i = 0; i < forms.length; i++) {
    var form = forms[i];
    var submit = document.getElementById(form.getAttribute("name") + "-submit");
    submit.addEventListener("click", formSubmitFunc(form));
}
