document.addEventListener("DOMContentLoaded", function() {
    setTimeout(function() {
        var flashMessages = document.querySelectorAll('.flash-messages .alert');
        flashMessages.forEach(function(flashMessage) {
            flashMessage.style.display = 'none';
        });
    }, 1500); // 5000 milliseconds = 5 seconds
});
