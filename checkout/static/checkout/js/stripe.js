$(document).ready(function () {
     // Getting the key and client_secret values
    var stripe_public_key = $("#id_stripe_public_key").text().slice(1, -1)
    var client_secret = $("#id_client_secret").text().slice(1, -1)

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

    // Form action after submit


})