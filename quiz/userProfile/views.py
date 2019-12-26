from django.shortcuts import render


def profile(request):
    return render(request, template_name="profile.html")

def login(request):
    return render(request, template_name="login.html")



