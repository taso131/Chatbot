const commands = ['pinfo', 'hlppls', 'extendedhlppls', 'icantwait', 'idontwantitanymore', 'wenexpirelul', 'canipaywithbitcoins', 'isyourstuffevengood', 'howdoiusethisshhh', 'wenexpirelul', 'hlppls'];


function openChat() {
    loadText();
    document.getElementById('chatbox').style.display = 'block'
    $('btn-chat').hide();
}
function closeChat() {
    document.getElementById('chatbox').style.display = 'none'
    $('btn-chat').show();
}
function chatWithBot() {
    message = document.forms[0].elements["msg"].value;
    appendMessage('my-message', message);
    xhttp = new XMLHttpRequest();
    xhttp.open("POST", "needAnswer?message=" + message, true);
    xhttp.onload = function (e) {
        appendMessage('other-message', xhttp.responseText);
        if (commands.includes(message)) {
            newQuestion();
        }
    }
    xhttp.send();
    document.forms[0].elements["msg"].value = '';
}
function newQuestion() {
    xhttp = new XMLHttpRequest();
    xhttp.open("GET", "newQuestion", true);
    xhttp.onload = function (e) {
        appendMessage('other-message', xhttp.responseText);
    }
    xhttp.send();
}
function loadText() {
    xhttp = new XMLHttpRequest();
    xhttp.open("GET", "process", true);
    xhttp.onload = function (e) {
        appendMessage('other-message', xhttp.responseText);
    }
    xhttp.send();
}
function loadTime() {
    xhttp = new XMLHttpRequest();
    xhttp.open("GET", "time", true);
    xhttp.onload = function (e) {
        document.getElementById('other-message-time').innerHTML = xhttp.responseText;
    }
    xhttp.send();
}
function appendMessage(from, message) {
    const root = document.getElementById('chat-message-list');
    const newMessageRow = document.createElement('div');
    const newMessageText = document.createElement('div')
    const newText = document.createTextNode(message);
    newMessageRow.className = 'message-row ' + from;
    newMessageText.className = 'message-text';
    root.appendChild(newMessageRow);
    newMessageRow.appendChild(newMessageText);
    newMessageText.appendChild(newText);
}