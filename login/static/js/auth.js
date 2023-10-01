$('#newAddress').val( $('#building,#street,#city,#province').map(function(){
    return $(this).val();
}).get().join(' ') );
// $(".minorCheck").click(function(){
//   var checkBox = document.getElementById("minorCheck");
//   var text = document.getElementById("guardianEmail");
//   if (checkBox.checked == true){
//     text.required = true;
//     $("#guardianEmail").attr('required', '');
//     text.style.display = "block";
//
//   } else {
//      text.style.display = "none";
//   }
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

$(document).ready(function(){
  const datelimit = new Date();
  const minorBday = new Date();
  const specAgeLimit = new Date();
  const lnumLimit = new Date();
  const lnumExp = new Date();
  lnumExp.setFullYear(lnumExp.getFullYear()+3);
  lnumLimit.setFullYear(lnumLimit.getFullYear()-3);
  datelimit.setFullYear(datelimit.getFullYear()-10);
  minorBday.setFullYear(minorBday.getFullYear()-18);
  specAgeLimit.setFullYear(specAgeLimit.getFullYear()-20);

  $('.spec-daterange').datepicker({
      format: 'MM dd, yyyy',
      todayHighlight: true,
      endDate: specAgeLimit
  });
  $('.spec-lnumrange').datepicker({
      format: 'MM dd, yyyy',
      todayHighlight: true,
      startDate: lnumLimit,
      endDate:lnumExp
  });
$('.input-daterange').datepicker({
    format: 'MM dd, yyyy',
    todayHighlight: true,
    endDate: datelimit
});



$("#newBday").datepicker().on('change', function(){
         var date =  $(this).datepicker('getDate');
         const labelContent = document.createTextNode("Guardian E-mail Address:");
         const divElement = Object.assign(
             document.createElement('div'),
             {
               id:'guardianEmail'
             }
           );

         const labelElement =Object.assign(
             document.createElement('label')
           );
         const inputElement =Object.assign(
             document.createElement('input'),
             { 	id:'guardianEmail',
               name:'guardianEmail',
               type:'text',
                 placeholder:'guardian@email.com'
             }
           );
           divElement.classList.add("form-group");
           labelElement.setAttribute("for","guardianEmail");
           labelElement.appendChild(labelContent);
           inputElement.classList.add("form-control");
           inputElement.classList.add("form-control-user");
           inputElement.required=true;
        // months are based 0


        if (date >  minorBday){
          const existing = document.getElementById("guardianEmail");
          if(!!existing){
            existing.remove();
          }
            // $("#div2").hide();
            // document.getElementById("guardianEmail").style.display = "block";
            const element = document.getElementById("guardianEmailForm");

            element.appendChild(divElement).appendChild(labelElement).appendChild(inputElement);
        }
        else if (date <=  minorBday){
            // $("#div2").hide();
            const existing = document.getElementById("guardianEmail");
            existing.remove();
        }
        // else if (date >= new Date(2014,2,1) && date <= new Date(2014,3,15)){
        //     // $("#div2").show();
        //     document.getElementById("guardianEmail").style.display = "block";
        // }
      });




});
const fileInput = document.getElementById("profile-pic");
  const preview = document.getElementById("preview");

  fileInput.addEventListener("change", function() {
  const file = fileInput.files[0];
  const reader = new FileReader();
  reader.addEventListener("load", function() {
    const image = new Image();
    image.src = reader.result;
    preview.innerHTML = "";
    preview.appendChild(image);
  });
  reader.readAsDataURL(file);
});

// $(".newBday").click(function(){
//   var checkBox = document.getElementById("minorCheck");
//   var text = document.getElementById("guardianEmail");
//   if (checkBox.checked == true){
//     text.style.display = "block";
//   } else {
//      text.style.display = "none";
//   }
// });

//TRIAL FOR DATEPICKER
// $('#datetimepicker2').datetimepicker();
//
// $('#getDate').click(function () {
//     console.log($('#datetimepicker2').data('date'))
//     $('#SelectedDate').text($('#datetimepicker2').data('date'))
// })
//
// var date = $('#datePicker').datepicker('getDate');
// $('#sub').on('click', function () {
//     alert(date);
// });

// var end = $('#newBday').val();
//     $('#newBday').datetimepicker();
//
//     // This will update the "end" variable as it changes.
//     $(document).on('change', '#newBday', function() {
//         end = $(this).val();
//         alert(end);
//         swal({
//             type: "success",
//             title: "Specialist Account successfully created!",
//             showConfirmButton: true,
//             confirmButtonText: "OK"
//             }).then(function(result){
//               });
//     });
//
//     $(document).on('click', '#sub', function () {
//         alert(end);
//         swal({
//             type: "success",
//             title: "Specialist Account successfully created!",
//             showConfirmButton: true,
//             confirmButtonText: "OK"
//             }).then(function(result){
//               });
//     });
//Function that was supposed to show the guardianEmail textbox
//if the date is less than 18years ago
// $(function() {
//       $('#newBday').datepicker({
//         onSelect: function() {
//           var date = ($("#newBday").datepicker('getDate')).toLocaleDateString();
//           checkRange(date);
//         }
//       });
//     });
//
//     function checkRange(date) {
//       // $('#guardianEmail').hide();
//       var checkDate = new Date(date);
//
//       var a = new Date('January 01, 2014');
//       if (checkDate<a){
//         document.getElementById('guardianEmail').style.display = "block";
//       }
//     }
//       //document.getElementById('guardianEmail').style.display = (checkDate<a) ? "block" : "none";
