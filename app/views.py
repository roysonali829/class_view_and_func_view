from django.shortcuts import render

from django.http import HttpResponse
from django.views.generic import View,TemplateView
from app.forms import *

# Create your views here.

#using fbv string view
def fbv_view(request):
    return HttpResponse('this is fbv view')

#using cbv sting view
class Cbv_view(View):
    def get(self,request):
        return HttpResponse('this is cbv view')

#html page by using fbv
def fbv_page(request):
    return render(request,'fbv_page.html')

#html page by using cbv
class cbv_page(View):
    def get(self,request):
        return render(request,'cbv_page.html')

#insert by using fbv
def insert_by_fbv(request):
    SFO = StudentForm()
    d = {'SFO':SFO}
    if request.method == 'POST':
        SDO = StudentForm(request.POST)
        if SDO.is_valid():
            SDO.save()
            return HttpResponse('data inserted')
    return render(request,'insert_by_fbv.html',d)

#insert by using cbv
class insert_by_cbv(View):
    def get(self,request):
        SFO = StudentForm()
        d = {'SFO':SFO}
        return render(request,'insert_by_cbv.html',d)
    def post(self,request):
        SDO = StudentForm(request.POST)
        if SDO.is_valid():
            SDO.save()
            return HttpResponse('data inserted')

# render html page using template view
class cbv_temp(TemplateView):
    template_name='cbv_temp.html'