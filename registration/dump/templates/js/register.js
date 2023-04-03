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
  