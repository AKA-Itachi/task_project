$(function () {

    $(".js-create-blog").click(function () {
      $.ajax({
        url: '/blogs/create/',
        type: 'get',
        dataType: 'json',
        beforeSend: function () {
          $("#modal-blog").modal("show");
        },
        success: function (data) {
          $("#modal-blog .modal-content").html(data.html_form);
        }
      });
    });

    $("#modal-blog").on("submit", ".js-blog-create-form", function () {
      var form = $(this);
      $.ajax({
        url: form.attr("action"),
        data: form.serialize(),
        type: form.attr("method"),
        dataType: 'json',
        success: function (data) {
          if (data.form_is_valid) {
            alert("Blog created!");  // <-- This is just a placeholder for now
          }
          else {
            $("#modal-blog .modal-content").html(data.html_form);
          }
        }
      });
      return false;
    });
  });

