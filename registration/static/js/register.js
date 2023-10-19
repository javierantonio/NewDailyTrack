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
    document.getElementById("sregisterPage3").style.display = "none";
    document.getElementById("sregisterPage2").style.display = "block";
  
    document.getElementById("snextRegister2").style.display = "block";
    document.getElementById("sprevRegister3").style.display = "none";
  
  });
  $(".prevLogin").click(function(){
    window.location = "index.php?route=login";
  
  });

function specMinDate() {
  const datelimit = new Date();
  datelimit.setFullYear(datelimit.getFullYear() - 20);
  $('[type="date"]').attr('id', 'birthday').prop('max', function () {
    return new Date(datelimit).toJSON().split('T')[0];
  });
};

function patMinDate() {
  const datelimit = new Date();
  datelimit.setFullYear(datelimit.getFullYear() - 10);
  $('[type="date"]').prop('max', function () {
    return new Date(datelimit).toJSON().split('T')[0];
  });
};

function lNumMinDate() {
  const datelimit = new Date();
  const dateMin = new Date();
  const dateMax = new Date();
  datelimit.setFullYear(datelimit.getFullYear() - 20);
  dateMin.setFullYear(dateMin.getFullYear() +1);
  dateMax.setFullYear(dateMax.getFullYear() +4);
  $('#licenseExpiry').prop('max', function () {
    return new Date(dateMax).toJSON().split('T')[0];
  }).prop('min', function () {
    return new Date(dateMin).toJSON().split('T')[0];
  });
  // $('[type="date"]').attr('id', 'birthday').prop('max', function () {
  //   return new Date(datelimit).toJSON().split('T')[0];
  // });
  $('#birthday').prop('max', function () {
    return new Date(datelimit).toJSON().split('T')[0];
  });
};

$(function(){
  const licNum = document.getElementById("licenseNumber");
  if(!!licNum){
    lNumMinDate();
    // specMinDate();
  }else{
    patMinDate();
  }


});

function previewFile() {
  var preview = document.getElementById('prcIDPreview');
  var file = document.getElementById('prcID').files[0];
  var reader = new FileReader();

  reader.onloadend = function() {
      preview.src = reader.result;
      preview.style.display = 'block';
  }

  if (file) {
      reader.readAsDataURL(file);
  } else {
      preview.src = '';
      preview.style.display = 'none';
  }
}


function updateFileNameLabel(input) {
  var label = document.querySelector('label[for="' + input.id + '"]');
  if (input.files.length > 0) {
    var fileName = input.files[0].name;
    if (fileName.length > 35) {
      fileName = fileName.substring(0, 35 - 3) + '...';
    }
    label.innerHTML = fileName;
  } else {
    label.innerHTML = 'Choose file';
  }
}

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

function specDate(){
  const minBday = new Date();
  minBday.setFullYear(minBday.getFullYear() - 20);
  const birthDate = document.getElementById("birthday").value;
  // let date = new Date(birthDate);

  //   if (date > minBday) {
  //     alert("Invalid birthday!");
  //   }
}

$('input[type=date]').change(function () {
  if (document.getElementById("birthday")){
  specDate();
  }else{
    changedDate();
  }

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

