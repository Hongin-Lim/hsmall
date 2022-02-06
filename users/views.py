

# Create your views here.
from django.contrib import auth
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User
from django.shortcuts import redirect, render


# def signup(request):
#     if request.method == 'POST':
#         if request.POST['password1'] == request.POST['password2']:
#             user = User.objects.create_user(
#                                             username=request.POST['username'],
#                                             password=request.POST['password1'],
#                                             email=request.POST['email'],)
#             auth.login(request, user)
#             return redirect('/hsmall/')
#         return render(request, 'users/signup.html')
#     return render(request, 'users/signup.html')

def signup(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)  # form = UserCreationForm(data = request.POST)도 가능합니다
        if form.is_valid():
            user = form.save()
            auth.login(request, user)
            return redirect('/hsmall')
        return redirect('/users/signup')

    else:
        form = UserCreationForm()
        return render(request, 'users/signup.html', {'form': form})


def auth_login(request, param):
    pass


def login(request) :
    if request.method=='POST' :
        # data는 forms.form 두번쨰 인자이므로 data = 은 생략 가능
        form = AuthenticationForm(request, data = request.POST) # 먼저 request 인자를 받아야함
        if form.is_valid() :
            # 세션 CREATE/ form.get_user는 User 객체 반환
            auth_login(request, form.get_user())
            return redirect('/hsmall') # 로그인 성공시 메인페이지 이동
    else :
        loginForm = AuthenticationForm()

    context = {
        'loginForm' : loginForm,
    }
    return render(request, 'users/login.html', context)