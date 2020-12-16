    $('#date_input').keypress(function(event) {
       event.preventDefault();
       return false;
    });

    var today = new Date()
    var dd = today.getDate() +2;
    var mm = today.getMonth() +1;
    var yy = today.getFullYear();

    var startDate = dd + '/'+ mm + '/'+ yy;
    dd = dd -2
    yy = yy +1
    var endDate = dd + '/' + mm + '/' + yy;

    console.log(startDate)
    $('#data_input').datepicker({
        format: "dd/mm/yyyy",
        orientation: 'bottom',
        maxViewMode: 0,
        weekStart: 1,
        startDate: startDate,
        endDate: endDate,
    });