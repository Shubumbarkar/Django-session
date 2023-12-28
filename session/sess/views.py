
from django.shortcuts import render,HttpResponse

# Create your views here.
def setsession(request):
    request.session['name']='Rahul'
    return render(request,'setsession.html')

def getsession(request):
    if 'name' in request.session:
      name=request.session['name']
      return render(request,'getsession.html',{'name':name})
    else:
        return HttpResponse('your session has expired')
def delsession(request):
    request.session.flush()
    request.session.clear_expired()
    return render(request,'delsession.html')