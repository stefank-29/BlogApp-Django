const formValidation = (() => {
    const username = document.querySelector("input[name='username']");
    const email = document.querySelector("input[name='email']");
    const password = document.querySelector("input[name='password1']");
    const confirmPassword = document.querySelector("input[name='password2']");
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

    function checkEmail() {
        const p = document.createElement('p');
        p.classList.add('error');
        const reg = /^(([^<>()\[\]\\.,;:\s@"]+(\.[^<>()\[\]\\.,;:\s@"]+)*)|(".+"))@((\[[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}\])|(([a-zA-Z\-0-9]+\.)+[a-zA-Z]{2,}))$/;
        if (email.value === '') {
            isValid = false;
            email.style.border = '2px solid red';
            p.textContent = 'This field is required.';
            email.parentNode.appendChild(p);
            return;
        }
        if (reg.test(String(email.value).toLowerCase())) {
            return;
        } else {
            isValid = false;
            p.textContent = 'Please enter a valid email address.';
            email.parentNode.appendChild(p);
            return;
        }
    }

    function checkPassword() {
        const p = document.createElement('p');
        p.classList.add('error');
        const reg = /^(?=.*\d)(?=.*[a-z])(?=.*[A-Z]).{8,}$/;
        if (password.value === '') {
            isValid = false;
            password.style.border = '2px solid red';
            p.textContent = 'This field is required.';
            password.parentNode.appendChild(p);
            return;
        }
        if (reg.test(String(password.value))) {
            return;
        } else {
            isValid = false;
            p.textContent =
                'Your password must contain at least 8 characters and contain one uppercase letter, one lowercase letter, and a digit.';
            password.parentNode.appendChild(p);
            return;
        }
    }
    function checkConfirmedPassword() {
        const p = document.createElement('p');
        p.classList.add('error');
        const reg = /^(?=.*\d)(?=.*[a-z])(?=.*[A-Z])[0-9a-zA-Z]{8,}$/;
        if (confirmPassword.value === '') {
            isValid = false;
            confirmPassword.style.border = '2px solid red';
            p.textContent = 'This field is required.';
            confirmPassword.parentNode.appendChild(p);
            return;
        }
        if (confirmPassword.value === password.value) {
            return;
        } else {
            isValid = false;
            p.textContent = 'Please make sure your passwords match.';
            confirmPassword.parentNode.appendChild(p);
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
        checkEmail();
        checkPassword();
        checkConfirmedPassword();
        if (isValid) {
            form.submit();
        }
    }

    username.addEventListener('change', checkUsername);
    email.addEventListener('change', checkEmail);
    password.addEventListener('change', checkPassword);
    confirmPassword.addEventListener('change', checkConfirmedPassword);

    document.querySelector('input[name="register"]').addEventListener('click', checkForm);
})();
