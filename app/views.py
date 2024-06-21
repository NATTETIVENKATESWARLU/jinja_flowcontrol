from django.shortcuts import render

# Create your views here.
def if_state(request):
    d={'a':18}
    return render(request,'if_state.html',d)

def else_state(request):
    d={'a':18,'b':20}
    return render(request,'else.html',d)

def elif_(request):
    d={'a':18,'b':200,'c':100}
    return render(request,'elif.html',d)

def nested_(request):
    d={'a':18,'b':1000,'c':100}
    return render(request,'nested.html',d)

def loop_(request):
    d=[{'a':18,'b':1000,'c':100},{'a':18,'b':1000,'c':100},{'a':18,'b':1000,'c':100},{'a':18,'b':1000,'c':100}]
    topic={'d':d}
    return render(request,'loop.html',topic)
