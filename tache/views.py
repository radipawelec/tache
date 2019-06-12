from django.shortcuts import render, HttpResponse, redirect, get_object_or_404, HttpResponseRedirect
from random import randint
from django.urls import reverse_lazy, reverse, resolve
from django.contrib.auth import login, authenticate
import requests
# from django.views.generic import *
# from .forms import *
# from .models import *
from bootstrap_modal_forms.generic import BSModalCreateView, BSModalLoginView, BSModalUpdateView
from .forms import *
from .context_processor import *
# from django.views.generic.base import View
from django.contrib.auth.decorators import login_required



#
def home(request):
    # if request.method == "POST":
    #     form = AddBoard(request.POST)
    #     if form.is_valid():
    #         board = form.save(commit=False)
    #         board.save()
    #         return redirect('home')
    # else:
    #     form = AddBoard()
    try:
        all_boards = ListBoard.objects.filter(board_active_status=True)
        context = {'all_boards':all_boards}
        return render(request,'tache/homepage.html', context)
    except:
        return HttpResponse("ops.")

def lists(request):
    active_lists = ListList.objects.filter(list_active_status=True)
    r = requests.get(
        'https://api.unsplash.com/search/photos?query=productivity&client_id=442287216c5e6d28aa3dbd89e277650fe21e57232dc00e5efe1490943f76aa8c')
    r = r.json()
    end = (len(r['results']) - 1)
    x = randint(0, end)
    background = (r['results'][x]['urls']['full'])
    print(background)
    context = {'active_lists': active_lists, 'background':background}
    return render(request, 'tache/lists.html', context)


# def add_board(request):
#     if request.method == "POST":
#         form = AddBoard(request.POST)
#         if form.is_valid():
#             board = form.save(commit=False)
#             board.save()
#             return redirect('home')
#     else:
#         form = AddBoard()
#     return render(request, 'tache/new_board.html', {'form': form} )
#




class BookCreateView(BSModalCreateView):
    template_name = 'tache/new_board.html'
    form_class = AddBoard
    success_message = 'Success: Book was created.'
    success_url = reverse_lazy('home')


class ListCreate(BSModalCreateView):
    def get_success_url(self):
        return reverse_lazy('board',
                            kwargs={'board_id': self.kwargs.get('board_id', None)}, )
    template_name = 'tache/create_list.html'
    form_class = AddList
    # success_url = reverse_lazy('board', kwargs={'board_id':})

def board(request, board_id):
    try:
        bg = ListBoard.objects.get(pk=board_id)
        active_lists = ListList.objects.filter(list_active_status=True, list_board=board_id)
        context = {'active_lists': active_lists, 'bg':bg }
        return render(request, 'tache/board.html', context)
    except ListList.DoesNotExist:
        return redirect('home')


class SignUpView(BSModalCreateView):
    form_class = CustomUserCreationForm
    template_name = 'tache/signup.html'
    success_message = 'Success: Sign up succeeded. You can now Log in.'
    success_url = reverse_lazy('home')


class CustomLoginView(BSModalLoginView):
    authentication_form = CustomAuthenticationForm
    template_name = 'tache/login.html'
    success_message = 'Success: You were successfully logged in.'
    extra_context = dict(success_url=reverse_lazy('home'))


class CardCreate(BSModalCreateView):
    def get_success_url(self):
        return reverse_lazy('board',
                            kwargs={'board_id': self.kwargs.get('board_id', None)}, )
    template_name = 'tache/create_card.html'
    form_class = AddCard




#
# class DeleteView(View):
#     def post(self, request, *args, **kwargs):
#         card = get_object_or_404(ListList, pk=request.POST['single_list.pk'])
#         print(card)
#         card.delete()
#         return HttpResponseRedirect('/')
#
@login_required
def delete(request, list_id, board):
    r = request.POST.dict()
    list = r.get('list_id')
    q = get_object_or_404(ListList, pk=list)
    id = r.get("board")
    q.delete()

    return redirect('board', id)

@login_required
def delete_board(request, board):
    r = request.POST.dict()
    id = r.get("board")
    q = get_object_or_404(ListBoard, pk=id)
    q.delete()

    return redirect('home')


class SetBackground(BSModalUpdateView):
    model = ListBoard
    template_name = 'tache/set_wallpaper.html'
    form_class = SetBackground
    success_message = 'Success: Book was updated.'

    def get_success_url(self):
        return reverse_lazy('board',
                            kwargs={'board_id': self.kwargs.get('pk', None)}, )

def login_request(request):
    if request.method == 'POST':
        form = AuthenticationForm(request=request, data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect('home')
            else:
                return render(request, "tahce/login2.html", {"form": form})
        else:
            return render(request, "tache/login2.html", {"form": form})
    form = AuthenticationForm()
    return render(request, "tache/login2.html", {"form": form})
