from rest_framework import generics
from rest_framework.permissions import IsAuthenticated
from ..models import Basket
from ..serializers import BasketSerializer


class BasketList(generics.ListCreateAPIView):
    # queryset = Category.objects.all()
    # serializer_class = CategorySerializer2
    permission_classes = (IsAuthenticated, )

    def get_queryset(self):
        return Basket.objects.for_user(self.request.user)

    def get_serializer_class(self):
        return BasketSerializer

    def perform_create(self, serializer):
        serializer.save(created_by=self.request.user)


class BasketDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Basket.objects.all()
    serializer_class = BasketSerializer