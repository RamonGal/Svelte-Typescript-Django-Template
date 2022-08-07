from django.shortcuts import render
from django.http import HttpResponse
from django.db.models import Q
from django.contrib.auth.decorators import login_required

@login_required
def example_view(request):
    context = {}
    
    return render(request, "", context)
    