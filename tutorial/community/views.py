# Create your views here.
from django.shortcuts import render
from community.forms import * #form

#user request를 받는다
def write(request):
    if request.method=='POST':
        form=Form(request.POST)
        if form.is_valid():
            form.save()
    else: form=Form() #form 생성

    return render(request, 'write.html', {'form':form})
    #request를 rendering/ write.html로 보낼 것
    #전달하고자하는 변수명<-변수 그대로 작성 (전달함)
    #form 버튼 누르면 post 발생

def list(request):
    articleList=Article.objects.all() #Article의 table의 모든 column을 가져온다
    return render(request, 'list.html',{'articleList':articleList})

def view(request, num='1'):#default 게시물번호=1
    article=Article.objects.get(id=num)
    return render(request, 'view.html',{'article':article})
