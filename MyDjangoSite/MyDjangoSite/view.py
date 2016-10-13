from django.shortcuts import render_to_response
def user_info(request):
    name = 'zbw'
    age = 24
    #t = get_template('user_info.html')
    #html = t.render(Context(locals()))
    #return HttpResponse(html)
    return render_to_response('user_info.html', locals()) # 加locals()才能显示模板数据