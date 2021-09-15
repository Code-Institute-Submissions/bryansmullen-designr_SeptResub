const stripePublicKey = document.getElementById('id_stripe_public_key').innerText.slice(1, -1);
const stripeSecretKey = document.getElementById('id_client_secret').innerText.slice(1, -1);
const stripe = Stripe(stripePublicKey);
const elements = stripe.elements();
const card = elements.create('card');

card.mount('#card-element')

card.addEventListener('change', e => {
    const errorDiv = document.getElementById('card-errors')
    if (e.error) {
        errorDiv.innerHTML = `<span>${e.error.message}</span>`
    } else {
        errorDiv.innerHTML = ''
    }
})

const form = document.getElementById('payment-form')

form.addEventListener('submit', async e => {
    e.preventDefault()
    card.update({'disabled': true});
        document.getElementById('submit-button').disabled = true

    const result = await stripe.confirmCardPayment(stripeSecretKey, {
        payment_method: {
            card: card,
        }
    })

    if (result.error) {
        const errorDiv = document.getElementById('card-errors')
        errorDiv.innerHTML = `<span>${result.error.message}</span>`
        card.update({'disabled': false});
        document.getElementById('submit-button').disabled = false
    } else {
        if (result.paymentIntent.status === 'succeeded') {
            form.submit();
        }
    }
})