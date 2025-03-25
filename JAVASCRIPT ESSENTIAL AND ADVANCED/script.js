document.addEventListener("DOMContentLoaded", function () {
    const form = document.getElementById("registrationForm");

    form.addEventListener("submit", function (event) {
        event.preventDefault(); // Prevent form submission

        validateForm();
    });

    // Restrict Mobile field to only numbers
    document.getElementById("mobile").addEventListener("keypress", function (event) {
        if (event.key < "0" || event.key > "9") {
            event.preventDefault();
        }
    });
});

function validateForm() {
    const fields = ["name", "email", "mobile"];
    let isValid = true;

    fields.forEach((field) => {
        const input = document.getElementById(field);
        const errorId = field + "-error";
        let errorElement = document.getElementById(errorId);

        // Remove existing error message if any
        if (errorElement) {
            errorElement.remove();
        }

        if (input.value.trim() === "") {
            isValid = false;
            errorElement = document.createElement("div");
            errorElement.id = errorId;
            errorElement.className = "error";
            errorElement.textContent = `${field} is required.`;
            input.parentNode.insertBefore(errorElement, input.nextSibling);
        }
    });

    if (isValid) {
        alert("Form submitted successfully!");
    }
}
