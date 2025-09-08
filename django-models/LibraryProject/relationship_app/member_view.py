from django.shortcuts import render, redirect
from django.contrib.auth.decorators import user_passes_test
from .utils.role_checker import is_member


@user_passes_test(lambda user: hasattr(user, 'userprofile') and user.userprofile.role == 'Member')
def memberview(request):
    return render(request, 'relationship_app/member_view.html')