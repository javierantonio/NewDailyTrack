$(document).ready(function () {
  $(".dashboardModalAppt").click(function () {
    var id = $(this).val();
    // var userid=$('#userid'+id).text();
    var name = $("#username" + id).text();
    // var apptdate=$('#apptdate'+id).text();
    var apptdatetime = $("#datetime" + id).text();
    var apptsched =
      $("#apptdate" + id).text() + " - " + $("#appttime" + id).text();
    // var appttime=$('#appttime'+id).text();
    var status = $("#status" + id).text();
    var venue = $("#venue" + id).text();
    var concern = $("#concern" + id).text();
    $("#dashboardModal").modal("show");
    $("#status").val(status);
    $("#patname").val(name);
    $("#idPat").val(id);
    // $('#apptdate').val(apptdate);
    $("#apptdatetime").val(apptdatetime);
    $("#apptsched").val(apptsched);
    $("#venue").val(venue);
    $("#concern").val(concern);
  });
  $('#dashboardModal').modal('hide');
});
