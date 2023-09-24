from django.urls import path 
from AppPFEtrade.views import * 


urlpatterns = [
    
    path("inicio/",inicio, name = "Inicio" ),
    path('market/', market, name = "Market"),
    path('buyer/', buyer, name = "Buyer"),
    path('seller/', seller , name = "Seller"),
    path('marketform/', marketForm, name = "mktform"),
    path('buyerform/', buyerForm, name = "byrform"),
    path('sellerform/', sellerForm, name = "slrform"),
    path('searcht/', searchTicker, name = "srchticker"),
    path("result/", matches, name="match"),
    
   
]