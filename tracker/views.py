from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.decorators import login_required
from .models import PeriodLog
from .decorators import user_required, admin_required
from datetime import datetime, timedelta
from django.utils import timezone

@login_required
def dashboard_redirect(request):
    if request.user.role == 'admin':
        return redirect('admin_dashboard')
    return redirect('user_dashboard')

@login_required
@user_required
def user_dashboard(request):
    last_log = PeriodLog.objects.filter(user=request.user).first()
    next_date = None
    if last_log:
        next_date = last_log.period_date + timedelta(days=28)
    
    current_date = timezone.now().date()
    # Check if period was already logged today
    already_logged = PeriodLog.objects.filter(user=request.user, period_date=current_date).exists()
    
    context = {
        'last_log': last_log,
        'next_date': next_date,
        'already_logged': already_logged,
    }
    return render(request, 'tracker/user_dashboard.html', context)

@login_required
@user_required
def log_period(request):
    if request.method == 'POST':
        period_date = timezone.now().date()
        # Prevent duplicate logs for the same day
        if not PeriodLog.objects.filter(user=request.user, period_date=period_date).exists():
            PeriodLog.objects.create(user=request.user, period_date=period_date)
    return redirect('user_dashboard')

@login_required
@admin_required
def admin_dashboard(request):
    all_logs = PeriodLog.objects.all().select_related('user').order_by('-period_date')
    context = {
        'all_logs': all_logs,
    }
    return render(request, 'tracker/admin_dashboard.html', context)

def logout_view(request):
    logout(request)
    return redirect('login')
