from django.http.response import HttpResponse
from django.shortcuts import render,redirect
from django.contrib import messages
import mysql.connector as sql

email=""
password=""

# Create your views here.
def login_fun(request):
    global email,password
    if request.method == "POST":
        m=sql.connect(host="localhost",user="root",passwd="12345678",database="website" )
        cursor=m.cursor()
        d=request.POST
        for key,value in d.items():
           
            if key=="Email":
                email=value
            if key=="Password":
                password=value 
           

        c="select * from users where email='{}' and password='{}'".format(email,password,)
        cursor.execute(c)
        t=tuple(cursor.fetchall())
        if t==():
            return render(request,'error.html')
        else:
            return render(request,"logout.html")

    
    return render(request,'login.html')

# Create your views here.
