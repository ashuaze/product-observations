### 1/5

1/5

In payment products, “cancel” and “refund” can look like two paths to the same outcome: the customer keeps the money.

They are not the same system operation. Cancel stops a payment before completion. Refund moves money back after it succeeds.

### 2/5

2/5

Stripe's manual capture adds a reversible state. The payment method is authorized and funds are held, but the PaymentIntent remains requires_capture.

Capture commits the payment. Cancel releases the remaining capturable amount.

https://docs.stripe.com/payments/place-a-hold-on-a-payment-method

### 3/5

3/5

That safety state has a cost. Online card authorizations are usually valid for 7 days, only some payment methods support separate capture, and some issuers do not clearly distinguish a hold from a settled payment.

https://docs.stripe.com/payments/place-a-hold-on-a-payment-method

### 4/5

4/5

After a PaymentIntent succeeds, Stripe says it cannot be canceled. A refund is a new workflow: it uses the merchant's available balance, can remain pending or fail, and may take about 5–10 business days to appear.

https://docs.stripe.com/refunds

### 5/5

5/5

Design rule: when fulfillment is uncertain, delay commitment only if the hold cost is acceptable.

Before commit, offer cancellation. After commit, expose compensation as its own stateful process—with status, failure handling, and customer communication—not a fake “undo.”
