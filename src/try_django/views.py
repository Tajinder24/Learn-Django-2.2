from django.http import HttpResponse
from django.shortcuts import render
from django.template.loader import get_template
# DRY - > Dont Repeat Yourself

def home_page(request):
	data = "Home"
	context = {"title":data}
	if request.user.is_authenticated:
		context["mylist"] = [1,2,3,4,5]
	return render(request, "home.html", context)
	#return HttpResponse("<h1>Hello World!!</h1>")

def about_page(request):
	return render(request, "about.html", {"title":"About Us"})

def contact_page(request):
	return render(request, "contact.html", {"title":"Contact Us"})


def test_page(request):
	#to render templates from txt or other files
	context = {"title" : "Testing Page"}
	template_name = "home.html"
	template_obj = get_template(template_name)
	rendered_item = template_obj.render(context)
	return HttpResponse(rendered_item) #render(request, "contact.html", {"title":"Contact Us"})