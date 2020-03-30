from django.shortcuts import render
import time
from django.http import HttpResponse
from django.http import HttpResponseRedirect
from django.urls import reverse
from django.shortcuts import get_object_or_404
from .models import CReview,PReview,Course,Professor
from django.contrib.auth.forms import UserCreationForm

#https://www.ling.upenn.edu/courses/Spring_2003/ling538/Lecnotes/ADfn1.htm
#https://www.d.umn.edu/~gshute/logic/barrel-shifter.xhtml
#A common usage of a barrel shifter is in the hardware implementation of floating-point arithmetic. For a floating-point add or subtract operation, the significands of the two numbers must be aligned, which requires shifting the smaller number to the right, increasing its exponent, until it matches the exponent of the larger number. This is done by subtracting the exponents and using the barrel shifter to shift the smaller number to the right by the difference, in one cycle. If a simple shifter were used, shifting by n bit positions would require n clock cycles.
#A Java applet which simulates a barrel-shifter - https://tams.informatik.uni-hamburg.de/applets/hades/webdemos/10-gates/60-barrel/shifter8.html
#https://iitd-plos.github.io/col718/ref/arm-instructionset.pdf
#https://developer.arm.com/docs/ddi0210/c/introduction/instruction-set-summary/arm-instruction-summary
#https://e-vent.mit.edu/

def account(request):
    return render(request, 'core/profile.html',{'user':request.user})

def bleh(request,course_id):
    i = get_object_or_404(Course,pk=course_id)
    if request.user.is_authenticated():
        return render(request, 'core/review.html',{'Course':i,'user':request.user})
    else:
        return HttpResponseRedirect(reverse('core:login'))    

def blep(request,proffesor_id):
    i = get_object_or_404(Professor,pk=proffesor_id)
    if request.user.is_authenticated():
        return render(request, 'core/reviewp.html',{'Professor':i,'user':request.user})
    else:
        return HttpResponseRedirect(reverse('core:login'))    
    

def index(request):
    course_list=Course.objects.order_by('Name')
    prof_list=Professor.objects.order_by('Name')
    context = {
        'course_list' : course_list,
        'prof_list' : prof_list,
        'user' : request.user
    }
    return render(request,'core/index.html',context)

def detailc(request,course_id):
    i = get_object_or_404(Course,pk=course_id)
    return render(request, 'core/detail.html',{'dic':i,'user':request.user})

def detailp(request,proffesor_id):
    i = get_object_or_404(Professor,pk=proffesor_id)
    return render(request, 'core/detailp.html',{'dic':i,'user':request.user})

def reviewc(request, course_id):
    reviewt = request.POST.get( 're1', None )
    y = request.POST.get( 'ano', None )
    if y=="anonymous":
        temp = CReview(question=Course.objects.get(pk=course_id),review_text=reviewt,author=request.user,is_ano=True)
    else:
        temp = CReview(question=Course.objects.get(pk=course_id),review_text=reviewt,author=request.user,is_ano=False)    
    temp.save()
    return HttpResponseRedirect(reverse('core:detailc',args=course_id))

def reviewp(request, proffesor_id):
    reviewt = request.POST.get( 're1', None )
    y = request.POST.get( 'ano', None )
    if y=="anonymous":
        temp = PReview(question=Professor.objects.get(pk=proffesor_id),review_text=reviewt,author=request.user,is_ano=True)
    else:
        temp = PReview(question=Professor.objects.get(pk=proffesor_id),review_text=reviewt,author=request.user,is_ano=False) 
    temp.save()
    return HttpResponseRedirect(reverse('core:detailp',args=proffesor_id))


def register(request):
    if request.method=='POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('core:index'))
    else:
        form = UserCreationForm()        
        args={'form':form}
        return render(request,'core/reg.html',args)