from django.http.response import HttpResponse
from django.shortcuts import render,redirect
from django.contrib import messages
import mysql.connector as sql

name=""
user_name =""
email=""
phone=""
password=""
c_password=""




# Create your views here.
def signup_fun(request):
    global name,user_name,email,phone,password,c_password
    if request.method == "POST":
        m=sql.connect(host="localhost",user="root",passwd="12345678",database="website" )
        cursor=m.cursor()
        d=request.POST
        for key,value in d.items():
            if key=="Full_name":
                name=value
            if key=="User_name":
                user_name=value
            if key=="Email":
                email=value
            if key=="Phone":
                phone=value
            if key=="Password":
                password=value 
            if key=="Confrim_password":
                c_password=value  

        c="insert into users Values('{}','{}','{}','{}','{}','{}')".format(name,user_name,email,phone,password,c_password)
        cursor.execute(c)
        m.commit() 

    return render(request,'home.html',{})

