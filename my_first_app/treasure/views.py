from django.shortcuts import render,redirect
from django.http import HttpResponse
import json

# Create your views here.

def start(request):
	
    return render(request,'treasure/start.html')
def input(request):
 global a
 global b
 global c 
 global val
 global ques
 val1=int(request.GET['a'])
 val2=int(request.GET['b'])
 val3=int(request.GET['c'])
 a=int(val1)
 b=int(val2)
 c=int(val3)
 return redirect(q1)

def q1(request):
	global ques
	ques=1
	global a
	a=b-c
	global val
	val=a
	return render(request,'treasure/questions.html',{'q':'What is the value of a if a=b-c ?'})
def q2(request):
	global ques
	ques=2
	global a
	a=c+b
	global val
	val=a
	return render(request,'treasure/questions.html',{'q':'What is the value of a if a=c+b ?'})
def q3(request):
	global ques
	ques=3
	global c
	c=b-a
	global val
	val=c
	return render(request,'treasure/questions.html',{'q':'What is the value of c if c=b-a ?'})
def q4(request):
	global ques
	ques=4
	global b
	b=a+c
	global val
	val=b
	return render(request,'treasure/questions.html',{'q':'What is the value of a if b=a+c ?'})	
def q5(request):
	global ques
	ques=5
	global c
	c=a-b
	global val
	val=c
	return render(request,'treasure/questions.html',{'q':'What is the value of a if c=a-b ?'})		
def iscorrect1(request):
 ans=request.GET['ans']
 tmp=int(ans)
 if tmp==val:
    if ques==1:
     return redirect(q2)
    elif ques==2:
     return redirect(q3)
    elif ques==3:
     return redirect(q4)
    elif ques==4:
     return redirect(q5) 
    else:
     return HttpResponse('Completed the test successfully. You have a Good Memory!!! Try with Bigger Numbers to Increase difficulty')
 else:
    if ques==1:
     return redirect(q1)
    elif ques==2:
     return redirect(q2)
    elif ques==3:
     return redirect(q3)
    elif ques==4:
     return redirect(q4)
    else:
     return redirect(q5)