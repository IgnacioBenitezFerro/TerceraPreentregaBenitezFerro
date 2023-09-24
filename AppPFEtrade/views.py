from django.shortcuts import render
from django.http import HttpResponse
from AppPFEtrade.models import Market, Buyer, Seller

# Create your views here.

def market(request):
     
     return render(request, "AppPFEtrade/market.html")

def buyer(request):
    
    return render(request, "AppPFEtrade/buyer.html")

def seller(request):
    
    return render(request, "AppPFEtrade/seller.html")

def inicio(request):
    
   return render(request, "AppPFEtrade/inicio.html")

def prueba(request):
    
    return render(request, "AppPFEtrade/padre.html")

def marketForm(request):
    
    if request.method == "POST":
        
      market = Market(position=request.POST["pos"],
                      ticker=request.POST["tck"],
                      price=request.POST["pri"])
      
      market.save()
      
      return render(request, "AppPFEtrade/inicio.html")

    
    return render(request,"AppPFEtrade/marketform.html" )


def buyerForm(request):
    
    if request.method == "POST":
        
      market = Buyer(nombre=request.POST["name"],
                    apellido=request.POST["srname"],
                    mail=request.POST["mail"],
                    ticker=request.POST["tcker"],
                    precio=request.POST["price"])
      
      market.save()
      
      return render(request, "AppPFEtrade/inicio.html")

    
    return render(request,"AppPFEtrade/buyerform.html" )


def sellerForm(request):
    
    if request.method == "POST":
        
      market = Seller(nombre=request.POST["name"],
                    apellido=request.POST["srname"],
                    mail=request.POST["mail"],
                    ticker=request.POST["tcker"],
                    precio=request.POST["price"])
      
      market.save()
      
      return render(request, "AppPFEtrade/inicio.html")

    
    return render(request,"AppPFEtrade/sellerform.html" )
  
  
def searchTicker(request):
  
  return render(request, "AppPFEtrade/market.html")
  
  
def matches(request): 
  
  if request.GET["ticker"]:
    
    ticker=request.GET["ticker"]
    markets = Market.objects.filter(ticker__iexact=ticker)
    
    return render(request, "AppPFEtrade/market.html", {"ticker" : ticker, "markets" : markets})
  
  else:
    
    ans = "No fullfilled data!"
    
  return HttpResponse(ans)
    
  

