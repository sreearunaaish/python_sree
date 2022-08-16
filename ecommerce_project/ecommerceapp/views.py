from django.http import HttpResponse
from django.shortcuts import render, get_object_or_404
from django.core.paginator import Paginator,EmptyPage,InvalidPage

from .models import Category,Product
#from . models import food_items,food_juices

# Create your views here.


def allprod_cat(request,c_slug=None):
      c_page=None
      products_list=None
      if c_slug!= None:
          c_page=get_object_or_404(Category,slug=c_slug)
          products_list=Product.objects.all().filter(category=c_page,available=True)
      else:
            products_list=Product.objects.all().filter(available=True)
      paginator=Paginator(products_list,6)
      try:
          page=int(request.GET.get('page','1'))
      except:
          page=1
      try:
          products=paginator.page(page)
      except (EmptyPage,InvalidPage):
          products=paginator.page(paginator.num_pages)
      return render(request,'category.html',{'category':c_page,'products':products})

def prodetail(request,c_slug,product_slug):
    try:
        product=Product.objects.get(category__slug=c_slug,slug=product_slug)
    except Exception as e:
        raise e

    return  render(request,'product.html',{'product':product})









    #return render(request,'arithmetic_prbm.html')
# def arith_metic(request):
#
#      val1 = int(request.GET.get("number1", ""))
#      val2 = int(request.GET.get("number2", ""))
#      res_add=val1+val2
#      res_sub=val1-val2
#      res_mul = val1 * val2
#      res_div = val1 /val2
#      return render(request,"arithmetic_result.html",{'result_add':res_add,'result_sub':res_sub,'result_mul':res_mul,'result_div':res_div})
#










'''
def index(request):
    return render(request,'home.html')
def about(request):
    return render(request,'about.html')
def contact(request):
    return render(request,'contact.html')

#def detail(request):
   # return HttpResponse('Welcome to the customer detail page')
def contact(request):
    return HttpResponse('Thank you for visiting the site')
'''