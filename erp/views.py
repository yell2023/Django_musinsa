from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.db import transaction
from .models import ProductModel, Inbound, Outbound
def home(request):
    user = request.user.is_authenticated  # 사용자가 인증을 받았는지 (로그인이 되어있는지)
    if user:
        return redirect('/product')
    else:
        return redirect('/sign-in')


@login_required
def product_view(request):
    if request.method == 'GET':  # 요청하는 방식이 GET 방식인지 확인하기
        user = request.user.is_authenticated  # 사용자가 로그인이 되어 있는지 확인하기
        if user:  # 로그인 한 사용자라면
            all_product = ProductModel.objects.all().order_by('-created_at')
            return render(request, 'erp/product_list.html',{'product': all_product})
        else:  # 로그인이 되어 있지 않다면
            return redirect('/sign-in')
    # 상품등록
    elif request.method == 'POST':  # 요청 방식이 POST 일때
        user = request.user  # 현재 로그인 한 사용자를 불러오기
        my_product = ProductModel()  # 제품 모델 가져오기
        my_product.author = user  # 모델에 사용자 저장
        my_product.product_id = request.POST.get('product_id', '')  # 저장
        my_product.product_name = request.POST.get('product_name', '')
        my_product.price = int(request.POST.get('price', '0'))
        my_product.size = request.POST.get('size', '')
        # selected_sizes = request.POST.getlist('size') # 체크박스에서 선택된 값을 리스트로 받아옴
        # if 'S' in selected_sizes:
        #     my_product.size = 'Small'
        # elif 'M' in selected_sizes:
        #     my_product.size = 'Medium'
        # elif 'L' in selected_sizes:
        #     my_product.size = 'Large'
        # else:
        #     my_product.size = 'Free'
        #
        my_product.save()
        return redirect('/product')



# 입고
@login_required
@transaction.atomic
def inbound_create(request):
# 상품 입고 view
# 입고 기록 생성

# 입고 수량 조정
    return ''

# 출고
@login_required
def outbound_create(request, product_id):
# 상품 출고 view
# 출고 기록 생성

# 재고 수량 조정
    return ''

# 입/출고 합산기능
@login_required
def inventory_view(request):
    if request.method == 'GET':  # 요청하는 방식이 GET 방식인지 확인하기
        user = request.user.is_authenticated  # 사용자가 로그인이 되어 있는지 확인하기
        if user:  # 로그인 한 사용자라면
            all_product = ProductModel.objects.all().order_by('-created_at')
            return render(request, 'erp/inventory.html', {'product': all_product})
        else:  # 로그인이 되어 있지 않다면
            return redirect('/sign-in')
        # 상품등록
    elif request.method == 'POST':  # 요청 방식이 POST 일때
        user = request.user  # 현재 로그인 한 사용자를 불러오기
        my_product = ProductModel()  # 제품 모델 가져오기
        my_product.author = user  # 모델에 사용자 저장
        my_product.product_id = request.POST.get('product_id', '')  # 저장
        my_product.product_name = request.POST.get('product_name', '')
        my_product.price = int(request.POST.get('price', '0'))
        my_product.size = request.POST.get('size', '')
        selected_sizes = request.POST.getlist('size')  # 체크박스에서 선택된 값을 리스트로 받아옴



# 총 입고 수량, 가격 계산

# 총 출고 수량, 가격 계산
    return render(request, 'erp/inventory.html')
