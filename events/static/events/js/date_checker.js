$(document).ready(function () {

    var postUrl = '/events/checker/'
    var csrfToken = $('input[name="csrfmiddlewaretoken"]').val();
    var eventId = $('#booking-form form').attr('action').split("/")[3]
    var infoBox = document.getElementById('ticket-info');

    dateCheck = function (date) {
        var postData = {
            'csrfmiddlewaretoken': csrfToken,
            'date': date,
            'event_id': eventId
        }
        $("#ticket_input").val("")
        if ($("#ticket_input").attr("disabled")) {
            $("#ticket_input").attr("disabled", false)
        }
        $(infoBox).html(' ')
        $.post(postUrl, postData).done(function (data, status) {
            data = parseInt(data)
            if (data == 0) {
                $("#ticket_input").attr("disabled", true)
                var infoMessage = `<strong>Please pick another date</strong>`
                $(infoBox).html(infoMessage)
            } else if(data <= 5) {
                var infoMessage = `<strong>Warning, only ${data} tickets remaining.`
                $(infoBox).html(infoMessage)
            } else {
                var infoMessage = `<strong>${data} tickets remaining</strong>`
                $(infoBox).html(infoMessage)
            }
            $("#ticket_input").attr("max", data)
        }).fail(function () {
            location.reload()
        });
    };
});
