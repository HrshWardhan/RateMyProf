from django.http import HttpResponse,HttpResponsePermanentRedirect,HttpResponseRedirect
from django.urls import reverse
import random
def hello_world(request):
    return HttpResponse("Hello World")

def root_page(request):
    return HttpResponse("Home Page")

def redirec(request):
    return HttpResponseRedirect(reverse('core:account'))

def random_number(request,max_rand=100):
    random_number = random.randrange(0,int(max_rand))

    msg = "Random number Between 0 and %s : %d" %(max_rand,random_number)

    return HttpResponse(msg)