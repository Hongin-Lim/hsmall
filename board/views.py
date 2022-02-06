from django.db.models import Q
from django.shortcuts import render, redirect

# Create your views here.
from board.form import BoardForm
from board.models import Board


def base (request):
    return render(request, 'layout/base.html')

def hsmall (request):
    return render(request, 'board/hsmall.html')

def register(request):
    if request.method == 'GET':
        boardForm = BoardForm()
        return render(request, 'board/register.html',
                      {'boardForm': boardForm})
    elif request.method == 'POST':
        boardForm = BoardForm(request.POST)

        if boardForm.is_valid():
            board = boardForm.save(commit=False)
            board.writer = request.user
            board.save()
            return redirect('/board/register')
        else:
            return redirect('/board/register')


def posts(request):
    posts = Board.objects.all()

    return render(request, 'board/list.html',
                            {'posts':posts})

def login(request):
    return render(request, 'users/login.html')