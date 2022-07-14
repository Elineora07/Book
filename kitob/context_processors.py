from account.form import LoginForm

def login_form(request):
    form = LoginForm()
    if request.session.get('login_error'):
        username = request.session.get("login_error")
        del request.session['login_error']
    
        
        form = LoginForm(data={"username": username, "password": "123123"})
        
        form.is_valid()
        form.add_error('password', "Login va/yoki parol noto'g'ri")
        
    return {
        "LOGIN_FORM": form
    }