moneroBox = document.getElementById("monero-sidebar-box");

function showMonero() {
    moneroBox.classList.remove("hide")
}

function hideMonero() {
    moneroBox.classList.add("hide")
}

function toggleMonero() {
    moneroBox.classList.toggle("hide")
}

var cpyWallet = document.getElementById('copy-monero-wallet');

if (cpyWallet !== null) {
    if (typeof ClipboardJS === 'function') {
        var clipboard = new ClipboardJS(cpyWallet);
        clipboard.on('success', function(e){
            cpyWallet.children[0].classList.remove('fa-copy');
            cpyWallet.children[0].classList.add('fa-clipboard-check');
            e.clearSelection()
        });
    } else {
        cpyWallet.children[0].classList.remove('fa-copy');
        cpyWallet.children[0].classList.add('fa-hand-point-left');
        cpyWallet.addEventListener('click', function() {
            var input=document.getElementById('monero-wallet-address');
            input.focus();input.select()
        });
    }
}

document.getElementById("monero-sidebar-button").addEventListener("click",toggleMonero);