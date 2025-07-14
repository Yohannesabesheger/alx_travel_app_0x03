## Chapa Payment Integration

This project integrates Chapa API to allow users to make travel bookings with secure payment.

### Endpoints

- `POST /api/payment/initiate/`: Initiate a new payment
- `GET /api/payment/verify/?tx_ref=...`: Verify payment status

### Environment Variables

- `CHAPA_SECRET_KEY`: Your secret API key from Chapa

### Models

- `Payment`: Stores transaction ID, booking reference, status, amount, email

### Testing

Use Chapa sandbox credentials for testing:
- [Sandbox API](https://developer.chapa.co/docs/sandbox/)

Screenshots and logs can be found under `/docs/screenshots`.
