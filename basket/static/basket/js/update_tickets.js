$(document).ready(function () {
    $(".update_event").click(function () {
        var parent = $(this).parent();
        var currentTickets = parseInt(parent.text().split("Update")[0].trim());
        var date = $(this).data('date');
        var eventId = $(this).data('eventid');

        var postUrl = '/events/checker/';
        var postData = {
            'csrfmiddlewaretoken': csrfToken,
            'date': date,
            'event_id': eventId
        };

        $.post(postUrl, postData).done(function (data, status) {
            var currentUrl = window.location.href;
            formUrl = (currentUrl.split('basket')[0]) + `basket/update/${eventId}/`;
            console.log(formUrl);
            avaliableTickets = parseInt(data) + currentTickets;
            inputElement = `<form method="POST" action="${formUrl}">
                             <input type="hidden" name="date" value="${date}">
                             <input type="hidden" name="csrfmiddlewaretoken" value="${csrfToken}">
                             <div class="input-group">
                              <input type="number" min="0" max="${avaliableTickets}" name="ticket_quantity"class="form-control basket-input" value="${currentTickets}">
                              <div class="input-group-append d-none d-md-flex">
                               <button class="button" type="submit"><i class="fas fa-check"></i></button>
                              </div>
                             </div>
                            <div class="d-block d-md-none text-center heading-text text-s"><input type="submit" value="update" class="button"></div>
                            </form>`;
            parent.html(inputElement);
        }).fail(function () {
            location.reload();
        });
    });
});