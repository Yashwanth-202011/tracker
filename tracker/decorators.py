from django.shortcuts import redirect
from django.contrib.auth.decorators import user_passes_test

def user_required(view_func):
    def wrapper(request, *args, **kwargs):
        if request.user.is_authenticated and request.user.role == 'user':
            return view_func(request, *args, **kwargs)
        return redirect('login')
    return wrapper

def admin_required(view_func):
    def wrapper(request, *args, **kwargs):
        if request.user.is_authenticated and request.user.role == 'admin':
            return view_func(request, *args, **kwargs)
        return redirect('login')
    return wrapper
