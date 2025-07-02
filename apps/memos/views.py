from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from .models import Memo
from .forms import MemoForm

@login_required
def memo_list(request):
    memos = Memo.objects.filter(user=request.user)
    return render(request, 'memos/memo_list.html', {'memos': memos})

@login_required
def memo_detail(request, pk):
    memo = get_object_or_404(Memo, pk=pk, user=request.user)
    return render(request, 'memos/memo_detail.html', {'memo': memo})

@login_required
def memo_create(request):
    if request.method == 'POST':
        form = MemoForm(request.POST)
        if form.is_valid():
            memo = form.save(commit=False)
            memo.user = request.user
            memo.save()
            return redirect('memo_list')
    else:
        form = MemoForm()
    return render(request, 'memos/memo_form.html', {'form': form})

@login_required
def memo_update(request, pk):
    memo = get_object_or_404(Memo, pk=pk, user=request.user)
    if request.method == 'POST':
        form = MemoForm(request.POST, instance=memo)
        if form.is_valid():
            form.save()
            return redirect('memo_list')
    else:
        form = MemoForm(instance=memo)
    return render(request, 'memos/memo_form.html', {'form': form})

@login_required
def memo_delete(request, pk):
    memo = get_object_or_404(Memo, pk=pk, user=request.user)
    if request.method == 'POST':
        memo.delete()
        return redirect('memo_list')
    return render(request, 'memos/memo_confirm_delete.html', {'memo': memo})

@login_required
def memo_edit(request, id):
    memo = get_object_or_404(Memo, id=id, user=request.user)
    if request.method == 'POST':
        form = MemoForm(request.POST, instance=memo)
        if form.is_valid():
            form.save()
            return redirect('memo_detail', id=memo.id)
    else:
        form = MemoForm(instance=memo)
    return render(request, 'memos/memo_form.html', {'form': form})
