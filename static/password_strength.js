document.getElementById("password").addEventListener("input", function() {
    const password = this.value;
    const strength = checkPasswordStrength(password);
    
    const strengthDiv = document.getElementById("passwordStrength");
    strengthDiv.innerHTML = `Strength: ${strength.text}`;
    strengthDiv.style.color = strength.color;
});

function checkPasswordStrength(password) {
    let strength = { text: "Weak", color: "red" };

    // Check length
    if (password.length >= 8) {
        strength.text = "Medium";
        strength.color = "orange";
    }
    
    // Check for uppercase, lowercase, number, and special characters
    if (/[A-Z]/.test(password) && /[a-z]/.test(password) && /\d/.test(password) && /[!@#$%^&*(),.?":{}|<>]/.test(password)) {
        strength.text = "Strong";
        strength.color = "green";
    }

    return strength;
}
