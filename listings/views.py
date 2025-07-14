import requests
import uuid
from django.conf import settings
from rest_framework.views import APIView
from rest_framework.response import Response
from .models import Payment
from rest_framework import status as http_status

class InitiatePaymentView(APIView):
    def post(self, request):
        email = request.data.get("email")
        amount = request.data.get("amount")
        booking_reference = str(uuid.uuid4())

        payload = {
            "amount": str(amount),
            "currency": "ETB",
            "email": email,
            "first_name": "Traveler",
            "last_name": "User",
            "tx_ref": booking_reference,
            "callback_url": "http://localhost:8000/api/payment/verify/",
            "return_url": "http://localhost:8000/payment-complete/",
            "customization[title]": "Travel Booking Payment",
        }

        headers = {
            "Authorization": f"Bearer {settings.CHAPA_SECRET_KEY}"
        }

        chapa_response = requests.post(
            "https://api.chapa.co/v1/transaction/initialize",
            json=payload,
            headers=headers
        )

        if chapa_response.status_code == 200:
            data = chapa_response.json()["data"]
            Payment.objects.create(
                booking_reference=booking_reference,
                amount=amount,
                email=email,
                transaction_id=data["tx_ref"],
                status="Pending"
            )
            return Response(data, status=http_status.HTTP_200_OK)
        else:
            return Response({"error": "Payment initialization failed."}, status=http_status.HTTP_400_BAD_REQUEST)
