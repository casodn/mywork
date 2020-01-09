from django.shortcuts import render,redirect

# Create your views here.


def login(request):
    if request.method=='GET':
        return render(request,'login.html')
    elif request.method=="POST":
        user=request.POST.get('username')
        pwd=request.POST.get('password')
        if user=="root" and pwd=="123":
            if request.POST.get('box')=="1":   #checkbox被按下
                request.session.set_expiry(10)  #session认证时间为10s，10s之后session认证失效
            request.session['username']=user   #user的值发送给session里的username
            request.session['is_login']=True   #认证为真
            return redirect('/index')
        else:
            return redirect('/login')
    return render(request,'login.html')