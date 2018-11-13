from django.shortcuts import render
from django.http import HttpResponse
from django.views.generic import View
from .forms import message
# Create your views here.
class index(View):
	def get(self,request):
		form=message()
		return render(request,'index.html',context={"form":form})

	def post(self,request):
		form=message(request.POST)
		if form.is_valid():
			title=form.cleaned_data.get('title')
			content=form.cleaned_data.get('content')
			email=form.cleaned_data.get('email')
			reply=form.cleaned_data.get('reply')
			print ("="*20)
			print (title)
			print (content)
			print (email)
			print (reply)
			print ("="*20)
			return HttpResponse("success!")
		else:
			print (form.errors)
			return HttpResponse("Error!")