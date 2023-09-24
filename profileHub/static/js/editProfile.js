function changedDate() {
  const minorBday = new Date();
  minorBday.setFullYear(minorBday.getFullYear() - 18);
  const birthDate = document.getElementById("birthday").value;
  let date = new Date(birthDate);
  const labelContent = document.createTextNode("Guardian E-mail Address:");
  const divElement = Object.assign(document.createElement("div"), {
    id: "guardianEmail",
  });
  const labelElement = Object.assign(document.createElement("label"));
  const inputElement = Object.assign(document.createElement("input"), {
    id: "guardianEmail",
    name: "guardianEmail",
    type: "email",
    placeholder: "guardian@email.com",
  });
  // divElement.classList.add("form-group");
  inputElement.classList.add("form-control");
  inputElement.classList.add("form-control-user");
  labelElement.setAttribute("for", "guardianEmail");
  labelElement.appendChild(labelContent);

  inputElement.required = true;

  if (date > minorBday) {
    const existing = document.getElementById("guardianEmail");
    if (!!existing) {
      existing.remove();
    }
    const element = document.getElementById("guardianEmailForm");
    //adds the elements in the guardianEmailForm div
    element
      .appendChild(divElement)
      .appendChild(labelElement)
      .appendChild(inputElement);
  } else if (date <= minorBday) {
    const existing = document.getElementById("guardianEmail");
    existing.remove();
  }
}


var passwordCheckbox = document.getElementById("passwordChange");

passwordCheckbox.addEventListener("change", function changePassword() {
  // Password Form Input
  const divPassword = Object.assign(document.createElement("div"), {
    id: "password",
  });
  const passwordLabelContent = document.createTextNode("Password");
  const confirmPasswordLabelContent = document.createTextNode("Confirm Password");
  const passwordLabelElement = Object.assign(document.createElement("label"));
  const passwordInputElement = Object.assign(document.createElement("input"), {
    id: "password",
    name: "password",
    type: "password",
    placeholder: "********",
  });
  // Add attributes to the input element
  divPassword.classList.add("w-100");
  divPassword.classList.add("d-flex");
  divPassword.classList.add("flex-column");
  passwordInputElement.classList.add("form-control");  
  passwordLabelElement.setAttribute("for", "password");
  passwordLabelElement.appendChild(passwordLabelContent);
  passwordInputElement.required = true;

  //Confirm Password Form Input
  const divConfirmPassword = Object.assign(document.createElement("div"), {
    id: "confirmPassword",
  });
  const confirmPasswordLabelElement = Object.assign(
    document.createElement("label")
  );
  const confirmPasswordInputElement = Object.assign(
    document.createElement("input"),
    {
      id: "confirmPassword",
      name: "confirmPassword",
      type: "password",
      placeholder: "********",
    }
  );
  // Add attributes to the input element
  divConfirmPassword.classList.add("w-100");
  divConfirmPassword.classList.add("d-flex");
  divConfirmPassword.classList.add("flex-column");
  confirmPasswordInputElement.classList.add("form-control");
  confirmPasswordInputElement.classList.add("form-control-user");
  confirmPasswordLabelElement.setAttribute("for", "confirmPassword");
  confirmPasswordLabelElement.appendChild(confirmPasswordLabelContent);

  if (passwordCheckbox.checked) {
    // const existing = document.getElementById("guardianEmail");
    // if (!!existing) {
    //   existing.remove();
    // }
    const element = document.getElementById("passwordFormGroup");
    //adds the elements in the guardianEmailForm div
    element
      .appendChild(divPassword)
      .appendChild(passwordLabelElement)
      .appendChild(passwordInputElement);

      element
      .appendChild(divConfirmPassword)
      .appendChild(confirmPasswordLabelElement)
      .appendChild(confirmPasswordInputElement);
  } else {
    const passwordInput = document.getElementById("password");
    const confirmPasswordInput = document.getElementById("confirmPassword");
    passwordInput.remove();
    confirmPasswordInput.remove();
  }
});

