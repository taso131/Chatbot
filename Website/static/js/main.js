function openChat() {
    document.getElementById('chatbox').style.display = 'block'
    $('btn-chat').hide();
    $.ajax({
        type: 'POST',
        url: 'Chatbot/main.py',
        data
    })
}
function closeChat() {
    document.getElementById('chatbox').style.display = 'none'
    $('btn-chat').show();
}