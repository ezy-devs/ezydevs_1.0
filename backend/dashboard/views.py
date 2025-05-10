from django.shortcuts import render,redirect, get_object_or_404
from .models import *
from .forms import *
from django.contrib import messages
# Create your views here.

def dashboard(request):
    return render(request, 'dashboard/dashboard.html')

def testimonials_dashboard(request):
    testimonies = Testimonies.objects.all()
    return render(request, 'dashboard/testimonials.html', {'testimonies': testimonies})


def add_testimony(request):
    if request.method == 'POST':
        form = TestimoniesForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('testimonials_dashboard')
    else:
        form = TestimoniesForm()

    return render(request, 'dashboard/add_testimony.html', {'form': form})

def edit_testimony(request, id):
    testimony = get_object_or_404(Testimonies, id=id)
    if request.method == 'POST':
        form = TestimoniesForm(request.POST, request.FILES, instance=testimony)
        if form.is_valid():
            form.save()
            messages.success(request, 'Testimony updated successfully!')
            return redirect('testimonials_dashboard')
    else:
        form = TestimoniesForm(instance=testimony)

def delete_testimony(request, id):
    testimony = get_object_or_404(Testimonies, id=id)
    testimony.delete()
    messages.success(request, 'Testimony deleted successfully!')
    return redirect('testimonials_dashboard')
