from django.shortcuts import render, get_object_or_404, redirect
from django.utils import timezone
from .models import Info, Comment
from .forms import InfoForm, CommentForm
from django.contrib.auth.decorators import login_required

# Create your views here.
def info_list(request):
    infos = Info.objects.all().order_by('-shared_date')
    return render(request, 'info_sharing_app/info_list.html', {'infos': infos})

def readme(request):
    return render(request, 'info_sharing_app/readme.html', {})

def info_detail(request, pk):
    info = get_object_or_404(Info, pk=pk)
    return render(request, 'info_sharing_app/info_detail.html', {'info': info})

@login_required
def info_new(request):
    if request.method == "POST":
        form = InfoForm(request.POST)
        if form.is_valid():
            info = form.save(commit=False)
            info.shared_date = timezone.now()
            info.save()
            return redirect('info_detail', pk=info.pk)
    else:
        form = InfoForm()
    return render(request, 'info_sharing_app/info_edit.html', {'form': form})

@login_required
def info_edit(request, pk):
    info = get_object_or_404(Info, pk=pk)
    if request.method == "POST":
        form = InfoForm(request.POST, instance=info)
        if form.is_valid():
            info = form.save(commit=False)
            info.updated_date = timezone.now()
            info.save()
            return redirect('info_detail', pk=info.pk)
    else:
        form = InfoForm(instance=info)
    return render(request, 'info_sharing_app/info_edit.html', {'form': form})

@login_required
def info_remove(request, pk):
    info = get_object_or_404(Info, pk=pk)
    info.delete()
    return redirect('info_list')

@login_required
def add_comment(request, pk):
    info = get_object_or_404(Info, pk=pk)
    if request.method == "POST":
        form = CommentForm(request.POST)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.info = info
            comment.save()
            return redirect('info_detail', pk=info.pk)
    else:
        form = CommentForm()
    return render(request, 'info_sharing_app/add_comment.html', {'info': info, 'form': form})
