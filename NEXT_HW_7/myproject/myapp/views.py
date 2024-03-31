from django.shortcuts import render

# Create your views here.
def hello(request):
    # 로직 작성 부분
    return render(request, 'hello.html')