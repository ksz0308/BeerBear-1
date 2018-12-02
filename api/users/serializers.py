from django.contrib.auth import get_user_model
from rest_framework.serializers import (
    ModelSerializer,
    SerializerMethodField,
    ImageField
)
from beers.models import Beer
from beers.serializers import BeerSerializer
from beershops.models import BeerShop
from beershops.serializers import BeershopSerializer
User = get_user_model()

class UserSerializer(ModelSerializer):
    favorite_beer_list = SerializerMethodField()
    favorite_beershop_list = SerializerMethodField()
    class Meta:
        model = User
        fields = ('pk', 'qr', 'favorite_beer_list', 'favorite_beershop_list')

    def get_favorite_beer_list(self,obj):
        beerList = obj.favorite_beer_list.all()
        serializer = BeerSerializer(beerList, many=True)
        return serializer.data
    def get_favorite_beershop_list(self, obj):
        beerShopList = obj.favorite_beershop_list.all() 
        serializer = BeershopSerializer(beerShopList, many=True)
        return serializer.data

