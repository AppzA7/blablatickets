from django.shortcuts import render
from django.http import HttpResponse
from django.shortcuts import render
from django.http import HttpResponseRedirect
from .forms import NameForm
from .models import Tickets
from django.contrib.auth.decorators import login_required
# Create your views here.

@login_required
def view_stuff(request):
    context_dict={'boldmessage': Tickets.objects.all() }
    return render(request,'step2/view_tickets.html',context=context_dict)
    
@login_required
def fetch_data(request):
        if request.method == 'POST':
        print request.POST
        train_requested=request.POST['yolo']
        return HttpResponseRedirect('/home/')

    
    
