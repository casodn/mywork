from django.shortcuts import render,redirect

# Create your views here.


def login(request):
    if request.method=='GET':
        return render(request,'login.html')
    elif request.method=="POST":
        user=request.POST.get('username')
        pwd=request.POST.get('password')
        if user=="root" and pwd=="123":
            if request.POST.get('box')=="1":   #checkbox������
                request.session.set_expiry(10)  #session��֤ʱ��Ϊ10s��10s֮��session��֤ʧЧ
            request.session['username']=user   #user��ֵ���͸�session���username
            request.session['is_login']=True   #��֤Ϊ��
            return redirect('/index')
        else:
            return redirect('/login')
    return render(request,'login.html')