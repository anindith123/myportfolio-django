from django.shortcuts import render
from .models import Contact
from django.http import HttpResponseRedirect
from django.views.decorators.csrf import csrf_exempt

@csrf_exempt
def contact(request):
    print("*****************************")
    print(request.POST)
    print("*****************************")

    if request.method == "POST":
        
            post = Contact(request.POST)
            if post.is_valid():

            

        
                post.save()
                return HttpResponse("success")
    



# Create your views here.
