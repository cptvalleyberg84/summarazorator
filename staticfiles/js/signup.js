document.addEventListener('DOMContentLoaded', function () {
    const checkbox = document.getElementById('guidelinesAccepted');
    const signupButton = document.getElementById('signupButton');

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