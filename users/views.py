

# Create your views here.
from django.contrib import auth
from django.contrib.auth import login, logout
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User
from django.forms import forms
from django.shortcuts import redirect, render

#이메일, 이름 추가

def signup(request):
    # signup 으로 POST 요청이 왔을 때, 새로운 유저를 만드는 절차를 밟는다.
    if request.method == 'POST':
        # password와 confirm에 입력된 값이 같다면
        if request.POST['password'] == request.POST['confirm']:
            # user 객체를 새로 생성
            user = User.objects.create_user(username=request.POST['username'], password=request.POST['password'])
            # 로그인 한다
            auth.login(request, user)
            return redirect('/hsmall')
    # signup으로 GET 요청이 왔을 때, 회원가입 화면을 띄워준다.
    return render(request, 'users/signup.html')

# class UserForm(UserCreationForm):
#     email = forms.EmailField(label="이메일")
#
# class Meta:
#     model = User
#     fields = ("username", "password1", "password2", "email")
# def signup(request):
#     if request.method == 'POST':
#         form = UserCreationForm(request.POST)  # form = UserCreationForm(data = request.POST)도 가능합니다
#         if form.is_valid():
#             user = form.save()
#             auth.login(request, user)
#             return redirect('/hsmall')
#         return redirect('/users/signup')
#
#     else:
#         form = UserCreationForm()
#         return render(request, 'users/signup.html', {'form': form})


def auth_login(request, param):
    pass


def userLogin(request) :
    if request.method=='POST' :
        # data는 forms.form 두번쨰 인자이므로 data = 은 생략 가능
        form = AuthenticationForm(request, data = request.POST) # 먼저 request 인자를 받아야함
        if form.is_valid() :
            # 세션 CREATE/ form.get_user는 User 객체 반환
            login(request, form.get_user())
            return redirect('/hsmall') # 로그인 성공시 메인페이지 이동
    else :
        loginForm = AuthenticationForm()

    context = {
        'loginForm' : loginForm,
    }
    return render(request, 'users/login.html', context)

# 로그아웃
# @login_required(login_url='/users/login')
def userLogout(request):
    logout(request)
    return redirect('/hsmall')