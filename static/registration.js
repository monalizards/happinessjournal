// Perform checks and provide feedback on frontend during registration
// query elements
const usernameInput = document.querySelector("#username")
const emailInput = document.querySelector("#email")
const passwordInput = document.querySelector("#password")
const confirmInput = document.querySelector("#confirm")
const birthdayInput = document.querySelector("#birthday")
const usernameCheck = document.querySelector("#username-check")
const emailCheck = document.querySelector("#email-check")
const passwordCheck = document.querySelector("#password-check")
const confirmCheck = document.querySelector("#confirm-check")
const birthdayCheck = document.querySelector("#birthday-check")

// helper functions to validate username and email with regular expressions
// username must only only letters and numbers
const validateUsername = username => {
    const re = /^[a-zA-Z0-9]{1,}$/
    return re.test(username);
}

// email must be in the correct format
const validateEmail = email => {
    const re = /^(([^<>()\[\]\\.,;:\s@"]+(\.[^<>()\[\]\\.,;:\s@"]+)*)|(".+"))@((\[[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}\])|(([a-zA-Z\-0-9]+\.)+[a-zA-Z]{2,}))$/;
    return re.test(email.toLowerCase());
}

usernameInput.addEventListener('keyup', e => {
    if (!validateUsername(usernameInput.value)) {
        usernameCheck.innerHTML = "Username must contain only letters or numbers"
    } else {
        usernameCheck.innerHTML = ''
    }
})

emailInput.addEventListener('keyup', e => {
    if (!validateEmail(emailInput.value)) {
        emailCheck.innerHTML = "Invalid email address"
    } else {
        emailCheck.innerHTML = ''
    }
})

// password must be at least 5 characters
passwordInput.addEventListener('keyup', e => {
    if (passwordInput.value.length < 5) {
        passwordCheck.innerHTML = "Password needs to be at least 5 characters"
    } else {
        passwordCheck.innerHTML = ''
    }
})

// password and confirmation must match
confirmInput.addEventListener('keyup', e => {
    if (confirmInput.value !== passwordInput.value) {
        confirmCheck.innerHTML = "Password do not match"
    } else {
        confirmCheck.innerHTML = ''
    }
})

// birthday must be earlier than today's date
birthdayInput.addEventListener('input', e => {
    const birthday = new Date(birthdayInput.value)
    const now = new Date();
    if (dateFns.isAfter(birthday, now)) {
        birthdayCheck.innerHTML = 'Invalid date (unless you are born in the future)'
    } else {
        birthdayCheck.innerHTML = ''
    }
})