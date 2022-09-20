from django.shortcuts import render

# Create your views here.


from rest_framework.views import APIView
from rest_framework.response import Response


from api.models import Books,Reviews
from api.serializers import BookSerializer,ReviewSerializer



class ProductsView(APIView):

    def get(self,request,*arg,**kwargs):
        qs=Books.objects.all()
        serializer=BookSerializer(qs,many=True)

        return Response(data=serializer.data)


    # def post(self,request,*args,**kwargs):
    #     bname=request.data.get("name")
    #     bauthor=request.data.get("publisher")
    #     bprice=request.data.get("price")
    #     bpublisher=request.data.get("publisher")
    #     Books.objects.create(name=bname,author=bauthor,price=bprice,publisher=bpublisher)
    #     return Response(data="Created")



    def post(self,request,*args,**kwargs):
        serilaizer=BookSerializer(data=request.data)
        if serilaizer.is_valid():
            Books.objects.create(**serilaizer.validated_data)
            return Response(data=serilaizer.data)
        else:
            return Response(data=serilaizer.errors)






class ProductDetailsView(APIView):

    def get(self,request,*args,**kwargs):
        id=kwargs.get("id")
        book=Books.objects.get(id=id)
        serializer=BookSerializer(book,many=False)
        return Response(data=serializer.data)


    def delete(self,request,*args,**kwargs):
        id=kwargs.get("id")
        Books.objects.get(id=id).delete()
        return Response(data="Deleted")



    def put(self,request,*args,**kwargs):
        id=kwargs.get("id")
        serializer=BookSerializer(data=request.data)
        if serializer.is_valid():
            Books.objects.filter(id=id).update(**serializer.validated_data)
            return Response(data=serializer.data)
        else:
            return Response(data=serializer.errors)






class ReviewsView(APIView):

    def get(self,request,*args,**kwargs):
        reviews=Reviews.objects.all()
        serilaizer=ReviewSerializer(reviews,many=True)
        return Response(data=serilaizer.data)



    def post(self,request,*args,**kwargs):
        serializer=ReviewSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(data=serializer.data)
        else:
            return Response(data=serializer.errors)



class ReviewDetailsView(APIView):
    def get(self,request,*args,**kwargs):
        id=kwargs.get("id")
        qs=Reviews.objects.get(id=id)
        serializer=ReviewSerializer(qs,many=False)
        return Response(data=serializer.data)

    def put(self,request,*args,**kwargs):
        id=kwargs.get("id")
        object=Reviews.objects.get(id=id)
        serializer=ReviewSerializer(instance=object,data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(data=serializer.data)
        else:
            return Response(data=serializer.errors)



    def delete(self,request,*args,**kwargs):
        id=kwargs.get("id")
        Reviews.objects.get(id=id).delete()
        return Response(data="deleted")










# class ProductView(APIView):
#     def get(self,request,*args,**kwargs):
#         return Response({"msg":"inside products get"})
#
#
#
# class MorningView(APIView):
#     def get(self,request,*args,**kwargs):
#         return Response({"msg":"good morning"})
#
#
# class EveningView(APIView):
#     def get(self,request,*args,**kwargs):
#         return Response({"msg":"Good Evening"})
#
#
# class AddView(APIView):
#     def post(self,request,*args,**kwargs):
#         n1=request.data.get("num1")
#         n2=request.data.get("num2")
#         res=int(n1)+int(n2)
#         return Response({"result":res})
#
#
# class SubView(APIView):
#     def post(self,request,*args,**kwargs):
#         n1=request.data.get("num1")
#         n2=request.data.get("num2")
#         res=int(n1)-int(n2)
#         return Response({"result":res})
#
#
#
# class MulView(APIView):
#     def post(self,request,*args,**kwargs):
#         n1=request.data.get("num1")
#         n2=request.data.get("num2")
#         res=n1%n2
#         return Response({"result":res})
#
#
# """class AddView(APIView):
#     def post(self,request,*args,**kwargs):
#         print(request.data.get("num1"))
#         print(request.data.get("num2"))
#
#         return Response({"msg":"Inside post"})"""


class CubeView(APIView):
    def post(self,request,*args,**kwargs):
        n=int(request.data.get("num"))
        res=n**3
        return Response({"result":res})



class CheckView(APIView):
    def post(self,request,*args,**kwargs):
        n=int(request.data.get("num"))
        if n%2==0:
            return Response({"result":"Even"})
        else:
            return Response({"result":"Odd"})

class FactView(APIView):
    def post(self,request,*args,**kwargs):
        n=int(request.data.get("num"))
        res=1
        for n in range(1,n+1):
            res=res*n
        return Response(data=res)


class WordcountView(APIView):
    def post(self,request,*args,**kwargs):
        txt=request.data.get("text")
        words=txt.split(" ")
        wc={}
        for w in words:
            if w in wc:
                wc[w]+=1
            else:
                wc[w]=1

        return Response(data=wc)




class PrimeView(APIView):
    def post(self,request,*args,**kwargs):
        n=int(request.data.get("num"))
        f=0
        for i in range(1,n+1):
            if n%i==0:
                f=f+1
        if f==2:
            return Response({"result":"Prime"})
        else:
            return Response({"result":"Not Prime"})




class PallindromeView(APIView):
    def post(self,request,*args,**kwargs):
        n=int(request.data.get("num"))
        rvs=0
        m=n
        while n>0:
            r=n%10
            rvs=rvs*10+r
            n=n//10
        if m==rvs:
            return Response({"result":"Pallindrome"})
        else:
            return Response({"result":"Not Pallindrome"})



class ArmstrongView(APIView):
    def post(self,request,*args,**kwargs):
        a=int(request.data.get("num"))
        res=0
        b=a
        while a>0:
            c=a%10
            res=res+c*c*c
            a=a//10
        if b==res:
            return Response({"result":"Armstrong Number"})
        else:
            return Response({"result":"Not Armstrong Number"})

