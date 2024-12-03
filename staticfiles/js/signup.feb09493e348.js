document.addEventListener('DOMContentLoaded', function () {
    const checkbox = document.getElementById('guidelines-accepted');
    const signupButton = document.getElementById('signup-button');

    if (checkbox && signupButton) {
        checkbox.addEventListener('change', function () {
            signupButton.disabled = !this.checked;

            if (this.checked) {
                signupButton.classList.add('btn-active');
            } else {
                signupButton.classList.remove('btn-active');
            }
        });
    }
});