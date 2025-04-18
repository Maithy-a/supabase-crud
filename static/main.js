document.addEventListener('DOMContentLoaded', () => {
    document.querySelectorAll('.edit-button').forEach(button => {
        button.addEventListener('click', () => {
            const row = button.closest('tr');
            row.querySelectorAll('.view-mode').forEach(el => el.classList.add('hidden'));
            row.querySelectorAll('.edit-mode').forEach(el => el.classList.remove('hidden'));
            row.querySelector('.action-buttons').classList.add('hidden');
            row.querySelector('.edit-form').classList.remove('hidden');
        });
    });

    document.querySelectorAll('.edit-form').forEach(form => {
        form.addEventListener('submit', () => {
            const row = form.closest('tr');
            const name = row.querySelector('input[name="name"]').value;
            const email = row.querySelector('input[name="email"]').value;
            form.querySelector('.hidden-name').value = name;
            form.querySelector('.hidden-email').value = email;
        });
    });
});