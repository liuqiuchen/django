from django.shortcuts import render

# Create your views here.
# 写一个首页的视图
def home(request):
	return render(request, 'home.html')