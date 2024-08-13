import stripe
import json
from django.conf import settings
from rest_framework.views import APIView
from rest_framework import status, authentication, permissions
from rest_framework.decorators import (
    api_view,
    authentication_classes,
    permission_classes,
)
from rest_framework.response import Response
from .models import Order, OrderItem
from .serializers import OrderSerializer, MyOrderSerializer


@api_view(["POST"])
@authentication_classes([authentication.TokenAuthentication])
@permission_classes([permissions.IsAuthenticated])
def checkout(request):
    serializer = OrderSerializer(data=request.data)
    if serializer.is_valid():
        stripe.api_key = settings.STRIPE_SECRET_KEY
        paid_amount = sum(
            item["quantity"] * item["product"].price
            for item in serializer.validated_data["items"]
        )

        # Calculate the total amount to be charged
        try:
            paid_amount = sum(
                item.get("quantity") * item.get("product").price
                for item in serializer.validated_data["items"]
            )
        except AttributeError:
            return Response(
                {"error": "Invalid item data"}, status=status.HTTP_400_BAD_REQUEST
            )

        try:
            # Create the charge
            charge = stripe.Charge.create(
                amount=int(paid_amount * 100),  # Amount in cents
                currency="USD",
                description="Charge from Djakets",
                source=serializer.validated_data["stripe_token"],
            )

            # Save the order
            serializer.save(user=request.user, paid_amount=paid_amount)
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        except stripe.error.StripeError as e:
            # Handle Stripe-specific errors
            return Response({"error": str(e)}, status=status.HTTP_400_BAD_REQUEST)
        except Exception as e:
            # Handle other exceptions
            return Response({"error": str(e)}, status=status.HTTP_400_BAD_REQUEST)
    else:
        # Log and return serializer errors
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class OrderList(APIView):
    authentication_classes = [authentication.TokenAuthentication]
    permission_classes = [permissions.IsAuthenticated]

    def get(self, request, format=None):
        
        orders = Order.objects.filter(user=request.user)
        serializer = MyOrderSerializer(orders, many=True)
        return Response(serializer.data)
