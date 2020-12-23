const formValidation = (() => {
    const username = document.querySelector("input[name='username']");
    const password = document.querySelector("input[name='password']");
    let isValid = true;

    function checkUsername() {
        const p = document.createElement('p');
        p.classList.add('error');
        if (username.value === '') {
            isValid = false;
            username.style.border = '2px solid red';
            p.textContent = 'This field is required.';
            username.parentNode.appendChild(p);
            return;
        }
    }

    function checkPassword() {
        const p = document.createElement('p');
        p.classList.add('error');
        if (password.value === '') {
            isValid = false;
            password.style.border = '2px solid red';
            p.textContent = 'This field is required.';
            password.parentNode.appendChild(p);
            return;
        }
    }

    function resetStyle() {
        const inputs = document.querySelectorAll('input');
        inputs.forEach((input) => {
            input.style = '';
            try {
                input.parentNode.removeChild(input.parentNode.querySelector('.error'));
                input.parentNode.removeChild(input.parentNode.querySelector('.error'));
            } catch {}
        });
    }

    function checkForm(e) {
        const form = document.querySelector('form');
        e.preventDefault();
        isValid = true;
        resetStyle();
        checkUsername();
        checkPassword();
        if (isValid) {
            form.submit();
        }
    }

    username.addEventListener('change', checkUsername);
    password.addEventListener('change', checkPassword);

    document.querySelector('input[name="login"]').addEventListener('click', checkForm);
})();
