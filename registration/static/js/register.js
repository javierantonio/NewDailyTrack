$(document).ready(function(){
  $("#confPassword").keyup(function(){
    var password = $("#newPassword").val();
    var confirmPassword = $("#confPassword").val();
    if (password != confirmPassword){
      $("#confPasswordError").html("Passwords do not match!").show();
      $("#submitButton").prop("disabled", true);
    }else{
      $("#confPasswordError").html("").hide();
      $("#submitButton").prop("disabled", false);
    }
  });
});
//
// $(document).ready(function(){
//   $("#newBday").change(function(){
//     var birthdate = new Date($("#newBday").val());
//     var today = new Date();
//     var age = Math.floor((today - birthdate) / (365.25 * 24 * 60 * 60 * 1000));
//     if (age < 18){
//       $("#guardianEmailField").show();
//       $("input[name='guardianEmail']").prop("required", true);
//     }else{
//       $("#guardianEmailField").hide();
//       $("input[name='guardianEmail']").prop("required", false);
//     }
//   });
// });






$(".nextRegister").click(function(){
    document.getElementById("registerPage1").style.display = "none";
    document.getElementById("registerPage2").style.display = "block";
  
    document.getElementById("nextRegister").style.display = "none";
    document.getElementById("prevRegister").style.display = "block";
  
  });
  $(".prevRegister").click(function(){
    document.getElementById("registerPage1").style.display = "block";
    document.getElementById("registerPage2").style.display = "none";
  
    document.getElementById("nextRegister").style.display = "block";
    document.getElementById("prevRegister").style.display = "none";
  
  });
  $(".nextSRegister").click(function(){
    document.getElementById("sregisterPage1").style.display = "none";
    document.getElementById("sregisterPage2").style.display = "block";
  
    document.getElementById("snextRegister").style.display = "none";
    document.getElementById("sprevRegister").style.display = "block";
  
  });
  $(".nextSRegister2").click(function(){
    document.getElementById("sregisterPage2").style.display = "none";
    document.getElementById("sregisterPage3").style.display = "block";
  
    document.getElementById("snextRegister3").style.display = "none";
    document.getElementById("sprevRegister2").style.display = "block";
  
  });
  $(".prevSRegister").click(function(){
    document.getElementById("sregisterPage1").style.display = "block";
    document.getElementById("sregisterPage2").style.display = "none";
  
    document.getElementById("snextRegister").style.display = "block";
    document.getElementById("sprevRegister").style.display = "none";
  
  });
  $(".prevSRegister2").click(function(){
    document.getElementById("sregisterPage3").style.display = "block";
    document.getElementById("sregisterPage2").style.display = "none";
  
    document.getElementById("snextRegister2").style.display = "block";
    document.getElementById("sprevRegister3").style.display = "none";
  
  });
  $(".prevLogin").click(function(){
    window.location = "index.php?route=login";
  
  });

$(function(){
  const datelimit = new Date();
  datelimit.setFullYear(datelimit.getFullYear() - 10);
    $('[type="date"]').prop('max', function(){
        return new Date(datelimit).toJSON().split('T')[0];
    });
});

function changedDate(){
  const minorBday = new Date();
  minorBday.setFullYear(minorBday.getFullYear() - 18);
  const birthDate = document.getElementById("birthday").value;
  let date = new Date(birthDate);
  const labelContent = document.createTextNode("Guardian E-mail Address:");
    const divElement = Object.assign(document.createElement('div'), {id: 'guardianEmail'});
    const labelElement = Object.assign(document.createElement('label'));
    const inputElement = Object.assign(document.createElement('input'),
        {
          id: 'guardianEmail',
          name: 'guardianEmail',
          type: 'email',
          placeholder: 'guardian@email.com'
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
      element.appendChild(divElement).appendChild(labelElement).appendChild(inputElement);
    } else if (date <= minorBday) {
      const existing = document.getElementById("guardianEmail");
      existing.remove();
    }
}


$('input[type=date]').change(function () {
  changedDate();
});

$('input[type=date]').keypress(function (e) {
    $(this).off('change blur');

    $(this).blur(function () {
       changedDate();
    });

    if (e.keyCode === 13) {
        changedDate();
    }
});

