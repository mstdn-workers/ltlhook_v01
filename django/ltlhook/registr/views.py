import random
import string
from django.shortcuts import render
from django.http import HttpResponse
from .models import HookReg
# Create your views here.

# generate dandom string
def random_string():
    seq = string.digits + string.ascii_lowercase + string.ascii_letters
    length = 32
    sr = random.SystemRandom()
    return ''.join([sr.choice(seq) for i in range(length)])

def registration(request):
    # POSTする
    return render(request, 'registr/registration.html')

def result(request):
    # 受け取ってDBに書き込む
    hook_url = request.POST['url']
    hook_username = request.POST['username']
    hook_secret = random_string()
    HookReg(to_url=hook_url, username=hook_username, secret=hook_secret).save()
    context = {
        'secret': hook_secret,
    }
    return render(request, 'registr/result.html', context)

def recv(request):
    return HttpResponse(request.POST.items())
