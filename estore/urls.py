"""estore URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
# from api.views import ProductView,MorningView,EveningView,AddView,SubView,MulView
from api.views import CubeView,CheckView,FactView,WordcountView,PrimeView,\
    PallindromeView,ArmstrongView,ProductsView,ProductDetailsView,\
    ReviewsView,ReviewDetailsView
urlpatterns = [
    path('admin/', admin.site.urls),
    path("cube",CubeView.as_view()),
    path("check",CheckView.as_view()),
    path("fact",FactView.as_view()),
    path("word",WordcountView.as_view()),
    path("prime",PrimeView.as_view()),
    path("pallindrome",PallindromeView.as_view()),
    path("armstrong",ArmstrongView.as_view()),
    path("products",ProductsView.as_view()),
    path("products/<int:id>",ProductDetailsView.as_view()),
    path("reviews",ReviewsView.as_view()),
    path("reviews/<int:id>",ReviewDetailsView.as_view())
    # path("products",ProductView.as_view()),
    # path("morning",MorningView.as_view()),
    # path("evening",EveningView.as_view()),
    # path("add",AddView.as_view()),
    # path("sub",SubView.as_view()),
    # path("mul",MulView.as_view())
]
