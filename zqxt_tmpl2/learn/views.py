from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

# 写一个首页的视图
def home(request):
	'''
	# 显示一个基本的字符串在网页上
	string = u"我在自强学堂学习Django，用它来建站"
	return render(request, 'home.html', {'string': string})
	'''

	'''
	TutorialList = ["HTML", "CSS", "jQuery", "Python", "Django"]
	return render(request, 'home.html', {'TutorialList': TutorialList})
	'''

	'''
	# 显示字典中的内容
	info_dict = {'site': u'自强学堂', 'content': u'各种IT技术教程'}
	return render(request, 'home.html', {'info_dict': info_dict})
	'''

	List = map(str, range(100)) # 一个长度为100的List
	return render(request, 'home.html', {'List': List})












