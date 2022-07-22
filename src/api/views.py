from rest_framework.response import Response
from rest_framework.decorators import api_view
from .serializers import UserSerializer, AddressSerializer
from app.models import User
from django.db.models import Count


@api_view(["GET"])
def get_user(request):
    admin = request.query_params.get("admin", "false").lower() == "true"

    if admin:
        users = (
            User.objects
            .filter(address__isnull=False)
            .values("uid", "first_name", "last_name")
            .annotate(address_count=Count("uid"))
        )
    else:
        users = User.objects.all()

    serializer = UserSerializer(users, many=True)
    return Response(serializer.data)


@api_view(["POST"])
def add_address(request):
    serializer = AddressSerializer(data=request.data)

    if serializer.is_valid(raise_exception=True):
        serializer.save()
        return Response(serializer.data)