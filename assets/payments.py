import stripe

stripe.api_key = "YOUR_STRIPE_API_KEY"


def create_payment_intent(amount, currency):
    intent = stripe.PaymentIntent.create(
        amount=amount,
        currency=currency,
    )
    return intent.client_secret
