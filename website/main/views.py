from django.shortcuts import render
from django. http import HttpResponse
# Create your views here.

def u_login(respnse): #function for user login
	return render(respnse,"main/PayvebLogin.html", {})

def u_reg(respnse): #function for user registeration
	return render(respnse,"main/PayvebUserReg.html", {})

#def retail(response):
	#return render(response, "main/.html", {})
	