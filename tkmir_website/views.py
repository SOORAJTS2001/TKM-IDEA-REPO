from django.shortcuts import render
from django.contrib import messages
# Create your views here.
def index(request):
    return render(request, 'tkmir_website/index.html')
def log_reg(request):
    if request.method == "POST":
        mail = request.POST.get('login_email')
        password = request.POST.get('login_password')
    else:
        mail = request.GET.get('register_email')
        password = request.GET.get('register_password')
    if mail == 'sjts007@gmail.com' and password == '123456':
        messages.success(request, 'Login Successful')
    return render(request, 'tkmir_website/login_register.html')