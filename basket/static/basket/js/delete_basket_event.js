$(document).ready(function () {
    $('.remove_event').click(function (e) {
        var date = $(this).attr('id').split('_')[0];
        var eventId = $(this).attr('id').split('_')[1];
        var url = `/basket/remove/${eventId}/`;
        var data = { 'csrfmiddlewaretoken': csrfToken, 'date': date };

        $.post(url, data).done(function () {
            location.reload();
        });
    });
});