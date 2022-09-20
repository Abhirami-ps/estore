from rest_framework import serializers
from api.models import Reviews



class BookSerializer(serializers.Serializer):
    id=serializers.IntegerField(read_only=True)
    name=serializers.CharField()
    author=serializers.CharField()
    price=serializers.IntegerField()
    publisher=serializers.CharField()
    qty=serializers.IntegerField()


    def validate(self, data):
        err_list=[]
        price=data.get("price")
        qty=data.get("qty")
        if qty not in range(1,500):
            err_list.append(serializers.ValidationError("invalid qty"))
        if price not in range(50,1000):
            err_list.append(serializers.ValidationError("invalid price"))
        if err_list:
            raise serializers.ValidationError(err_list)

        return data


    # def validate_price(self,value):
    #     if value not in range(50,1000):
    #         raise serializers.ValidationError("invalid price")
    #     return value
    #
    # def validate_qty(self,value):
    #     if value not in range(1,500):
    #         raise serializers.ValidationError("invalid qty")
    #     return value




class ReviewSerializer(serializers.ModelSerializer):
    created_date=serializers.CharField(read_only=True)

    class Meta:
        model=Reviews
        fields="__all__"
        # exclude=("created_date",)
        # fields=["book","user","comment","rating"]





