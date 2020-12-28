$(document).ready(function () {
    // Getting the key and client_secret values
    var stripe_public_key = $("#id_stripe_public_key").text().slice(1, -1);
    var client_secret = $("#id_client_secret").text().slice(1, -1);

    // Creating the card
    var stripe = Stripe(stripe_public_key);
    var elements = stripe.elements();

    var style = {
        base: {
            color: '#495057',
            fontFamily: '"Lora", serif',
            fontSmoothing: 'antialiased',
            backgroundColor: 'white',
            fontSize: '16px',
            '::placeholder': {
                color: '#A7B4BC'
            }
        },
        invalid: {
            color: '#ff6961',
            iconColor: '#ff6961'
        }
    };

    var card = elements.create('card', { style: style });
    card.mount('#card-element');

    //Handles card errors on input
    card.addEventListener('change', function (event) {
        var errorBox = document.getElementById('card-errors');
        if (event.error) {
            var errorMessage = `
            <span class="heading-text text-s"><strong>${event.error.message}</strong></span>
        `;
            $(errorBox).html(errorMessage);
        } else {
            errorBox.textContent = '';
        }
    });

    // Form action after submit
    var form = document.getElementById("checkout-form");
    form.addEventListener('submit', function (event) {
        event.preventDefault()
        card.update({ 'disabled': true })
        $("#checkout-form .button").attr('disabled', true)

        // This section validates the form data and basket before taking payment
        var postUrl = '/checkout/checkout_validator/'
        var formData = {
            "first_name": $("input[name='first_name']").val(),
            "last_name": $("input[name='last_name']").val(),
            "email": $("input[name='email']").val(),
            "phone_number": $("input[name='phone_number']").val()
        };
        var csrfToken = $('input[name="csrfmiddlewaretoken"]').val();
        postData = {
            'csrfmiddlewaretoken': csrfToken,
            'formData': formData,
        }

        $.post(postUrl, postData).done(function () {
            //This section validates the form data and basket before taking payment
            var postUrl = '/checkout/save_checkout_data/'
            var formData = {
                "first_name": $("input[name='first_name']").val(),
                "last_name": $("input[name='last_name']").val(),
                "email": $("input[name='email']").val(),
                "phone_number": $("input[name='phone_number']").val(),
                "pid": client_secret.split("_secret")[0]
            };
            var csrfToken = $('input[name="csrfmiddlewaretoken"]').val();
            postData = {
                'csrfmiddlewaretoken': csrfToken,
                'formData': formData,
            }
            $.post(postUrl, postData).done(function () {
                stripe.confirmCardPayment(client_secret, {
                    payment_method: {
                        card: card
                    }
                }).then(function (paymentResult) {
                    if (paymentResult.error) {
                        var errorBox = document.getElementById('card-errors');
                        var errorMessage = `
                                <span class="heading-text text-s"><strong>${paymentResult.error.message}</strong></span>
                                 `;
                        $(errorBox).html(errorMessage);
                        card.update({ 'disabled': false })
                        $("#checkout-form .button").attr('disabled', false)
                    } else {
                        if (paymentResult.paymentIntent.status == 'succeeded') {
                            //form.submit()
                        }
                    }
                });
            }).fail(function () {
                location.reload()
            });
        }).fail(function () {
            location.reload()
        });
    })
})