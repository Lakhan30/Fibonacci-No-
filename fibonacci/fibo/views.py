from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
from django.views.decorators.csrf import csrf_exempt
import time

#Precalculation for 3000 numbers
a=1
b=1
list=[]
list.append(a)
list.append(b)
for i in range(2998):
    c=a+b
    list.append(c)
    a=b
    b=c

@csrf_exempt
def index(request):
    if request.method == "GET":
        print("get")
        return render(request,'fibo/index.html', {})

    else:
        print("post")
        n = int(request.POST.get('n'))
        start_time = time.time()
        #Calculation for next n-3000 numbers
        if(n>3000):
            a=list[2998]
            b=list[2999]

            for i in range(n-3000):
                c=a+b
                list.append(c)
                a=b
                b=c

        return render(request,'fibo/result.html',{"answer":list[:n], "n":n, "t":(time.time() - start_time)})


