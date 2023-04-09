from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import UserModel
from django.contrib.auth import get_user_model #사용자가 있는지 검사하는 함수
from django.contrib import auth # 사용자 auth 기능
from django.contrib.auth.decorators import login_required


# Create your views here.


def sign_up_view(request): # 회원가입
    if request.method == 'GET':  # GET 메서드로 요청이 들어 올 경우
        return render(request, 'accounts/signup.html')

    # 회원가입기능
    elif request.method == 'POST':  # POST 메서드로 요청이 들어 올 경우
        username = request.POST.get('username', None) # html에서 name값을 넣고, 파라미터에 아무것도 없으면 none을 넣겠다는 뜻ㅁ
        password = request.POST.get('password', None)
        password2 = request.POST.get('password2', None)
        department = request.POST.get('department', None)


        if password != password2:
            return render(request, 'accounts/signup.html')
        else:
            exist_user = get_user_model().objects.filter(username=username)
            if exist_user:
                return render(request, 'accounts/signup.html')  # 사용자가 존재하기 때문에 사용자를 저장하지 않고 회원가입 페이지를 다시 띄움
            else:
                UserModel.objects.create_user(username=username, password=password, department=department) #
                return redirect('/sign-in')  # 회원가입이 완료되었으므로 로그인 페이지로 이동


def sign_in_view(request):
    if request.method == 'POST':
        username = request.POST.get('username', None)
        password = request.POST.get('password', None)

        me = auth.authenticate(request, username=username, password=password)  # 사용자 불러오기
        if me is not None:  # 저장된 사용자의 패스워드와 입력받은 패스워드 비교
            auth.login(request, me)
            return redirect('/')
        else:
            return redirect('/sign-in')  # 로그인 실패

    elif request.method == 'GET':
        user = request.user.is_authenticated  # 사용자가 로그인 되어 있는지 검사
        if user:  # 로그인이 되어 있다면
            return redirect('/')
        else:  # 로그인이 되어 있지 않다면
            return render(request, 'accounts/signin.html')

@login_required
def logout(request):
    auth.logout(request) # 인증 되어있는 정보를 없애기
    return redirect("/")