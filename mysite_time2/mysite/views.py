from django.http import HttpResponse
import datetime


def current_datetime(request):
	now = datetime.datetime.now()
	html = "<html><head><meta charset='utf-8'></head><body>现在的时间是%s<body/>" % now
	return HttpResponse(html)


# offset是从匹配的URL里提取出来的，提取的字符总是字符串
# 因为urls.py中正则表达式 (\d{1,2}) 只提取数字字符。 这也是URL配置的另一个好处：提供了清晰的输入数据有效性确认。
def hours_ahead(request, offset):
	offset = int(offset) # 将字符串转换为整数
	dt = datetime.datetime.now() + datetime.timedelta(hours=offset)
	html = "<html><head><meta charset='utf-8'></head><body>推迟%s小时，以后的时间是%s<body>" % (offset, dt)
	return HttpResponse(html)



