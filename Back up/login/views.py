from django.http import HttpResponse
from django.shortcuts import render


def home(request):
    return HTTPResponse('<h1>Login Page</h1>')
