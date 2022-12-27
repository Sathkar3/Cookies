from django.shortcuts import render

# Create your views here.


def name_view(request):
	response = render(request,'app1/name.html')
	return response


def age_view(request):
	name=request.GET['name']
	response = render(request,'app1/age.html')
	response.set_cookie('name',name)
	return response



def city_view(request):
	age=request.GET['age']
	response = render(request,'app1/city.html')
	response.set_cookie('age',age)
	return response



def home_view(request):
	city=request.GET['city']
	name=request.COOKIES['name']
	age=request.COOKIES['age']
	response = render(request,'app1/home.html',{'n':name,'a':age,'c':city})
	return response



