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

$(document).ready(function(){
  $("#newBday").change(function(){
    var birthdate = new Date($("#newBday").val());
    var today = new Date();
    var age = Math.floor((today - birthdate) / (365.25 * 24 * 60 * 60 * 1000));
    if (age < 18){
      $("#guardianEmailField").show();
      $("input[name='guardianEmail']").prop("required", true);
    }else{
      $("#guardianEmailField").hide();
      $("input[name='guardianEmail']").prop("required", false);
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
    document.getElementById("sregisterPage3").style.display = "block";
    document.getElementById("sregisterPage2").style.display = "none";
  
    document.getElementById("snextRegister2").style.display = "block";
    document.getElementById("sprevRegister3").style.display = "none";
  
  });
  $(".prevLogin").click(function(){
    window.location = "index.php?route=login";
  
  });
  