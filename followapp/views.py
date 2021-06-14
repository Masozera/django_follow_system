from django.shortcuts import render, get_object_or_404
from django.urls import reverse_lazy
from django.views.generic import CreateView, View
from django.contrib.auth.decorators import login_required

from .models import CustomUser, Contact
from .forms import CustomUserCreationForm
from common.decorators import ajax_required

from django.http import JsonResponse
from django.views.decorators.http import require_POST




# Create your views here.

class  SignUpView(CreateView):
    form_class = CustomUserCreationForm
    success_url = reverse_lazy('login')
    template_name = 'signup.html'

@login_required
def user_list(request):
    users = CustomUser.objects.filter(is_active=True)
    return render(request,'user/list.html',{'users': users})
    
@login_required
def user_detail(request, username):
    user = get_object_or_404(CustomUser,username=username,is_active=True)
    return render(request,'user/detail.html',{'user': user})

@ajax_required
@require_POST
@login_required
def user_follow(request):
    user_id = request.POST.get('id')
    
