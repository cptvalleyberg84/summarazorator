// Smooth auto-hide Django messages
document.addEventListener('DOMContentLoaded', function () {
    const messages = document.querySelectorAll('.alert');

    messages.forEach(function (message) {
        // Initial fade in
        message.style.opacity = '1';

        setTimeout(function () {
            // Add fade-out class for smooth transition
            message.classList.add('fade-out');

            // Remove the element after animation completes
            setTimeout(function () {
                message.remove();
            }, 600); // Match this with CSS transition duration
        }, 3000);
    });

    // Handle manual close button
    document.querySelectorAll('.btn-close').forEach(function (button) {
        button.addEventListener('click', function () {
            const alert = this.closest('.alert');
            alert.classList.add('fade-out');
            setTimeout(function () {
                alert.remove();
            }, 600);
        });
    });
});