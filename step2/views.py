from django.shortcuts import render
from django.http import HttpResponse
from django.shortcuts import render
from django.http import HttpResponseRedirect
from .forms import NameForm
from .models import Courier
# Create your views here.


def view_stuff(request):
    context_dict={'boldmessage': Courier.objects.all() }
    return render(request,'step2/view_stuff.html',context=context_dict)
    
    
    
    
    
    
