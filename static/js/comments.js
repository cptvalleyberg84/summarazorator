document.addEventListener('DOMContentLoaded', function () {
    const positiveBtn = document.getElementById('positive-btn');
    const negativeBtn = document.getElementById('negative-btn');
    const editButtons = document.getElementsByClassName("btn-edit");
    const deleteButtons = document.getElementsByClassName("btn-delete");
    const deleteModal = new bootstrap.Modal(document.getElementById("deleteModal"));
    const deleteConfirm = document.getElementById("deleteConfirm");
    const commentForm = document.getElementById('comment-form');
    const submitBtn = document.getElementById('submitBtn');
    const commentTypeInput = document.getElementById('comment_type');
    const commentFormElement = document.getElementById('commentForm');


    // Handle form submission collaboration form
    document.querySelectorAll('collaboration-form').forEach(form => {
        form.addEventListener('submit', function (e) {
            e.preventDefault();
            fetch(window.location.pathname, {
                method: 'POST',
                body: new FormData(form),
                headers: {
                    'X-CSRFToken': document.querySelector('[name=csrfmiddlewaretoken]').value
                }
            }).then(response => {
                if (response.ok) {
                    window.location.reload();
                }
            });
        });
    });

    // Handle positive reaction
    positiveBtn.addEventListener('click', function () {
        commentForm.style.display = 'block';
        submitBtn.className = 'btn btn-success';
        commentTypeInput.value = 'positive';
        submitBtn.innerHTML = '<i class="fas fa-thumbs-up"></i> Submit Positive Comment';
        // Reset form action in case it was previously set for editing
        commentFormElement.setAttribute('action', '');
    });

    // Handle negative reaction
    negativeBtn.addEventListener('click', function () {
        commentForm.style.display = 'block';
        submitBtn.className = 'btn btn-danger';
        commentTypeInput.value = 'negative';
        submitBtn.innerHTML = '<i class="fas fa-thumbs-down"></i> Submit Negative Comment';
        // Reset form action in case it was previously set for editing
        commentFormElement.setAttribute('action', '');
    });

    // Handle edit functionality
    for (let button of editButtons) {
        button.addEventListener("click", (e) => {
            let commentId = e.target.getAttribute("comment_id");
            let commentElement = document.getElementById(`comment${commentId}`);
            let commentContent = commentElement.querySelector('p').innerText.trim();
            let isPositive = commentElement.closest('.positive-side') !== null;

            // Show the comment form
            commentForm.style.display = 'block';

            // Set the comment text
            document.getElementById('id_body').value = commentContent;

            // Update form styling and text based on comment type
            if (isPositive) {
                submitBtn.className = 'btn btn-success';
                commentTypeInput.value = 'positive';
                submitBtn.innerHTML = '<i class="fas fa-thumbs-up"></i> Update Positive Comment';
            } else {
                submitBtn.className = 'btn btn-danger';
                commentTypeInput.value = 'negative';
                submitBtn.innerHTML = '<i class="fas fa-thumbs-down"></i> Update Negative Comment';
            }

            // Set the form action for editing
            commentFormElement.setAttribute('action', `edit_comment/${commentId}`);
        });
    }

    // Handle form submission
    commentFormElement.addEventListener('submit', function (e) {
        e.preventDefault();
        const action = this.getAttribute('action');
        const url = action ? action : window.location.pathname;

        fetch(url, {
            method: 'POST',
            body: new FormData(this),
            headers: {
                'X-CSRFToken': document.querySelector('[name=csrfmiddlewaretoken]').value
            }
        }).then(response => {
            if (response.ok) {
                window.location.reload();
            }
        });
    });

    // Handle delete functionality
    for (let button of deleteButtons) {
        button.addEventListener("click", (e) => {
            let commentId = e.target.getAttribute("comment_id");
            deleteConfirm.href = `delete_comment/${commentId}`;
            deleteModal.show();
        });
    }
});