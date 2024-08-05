from django.shortcuts import render, redirect, get_object_or_404
from .models import User
from .forms import UserForm
from .forms import Userreponse
from django.db.models import Q
from .models import User_info, User


    
from django.db.models import Q
from django.shortcuts import render, redirect
from django.contrib import messages
from .models import User_info, User

def user_list(request):
    user_id = request.session.get('user_id')
    if not user_id:
        return redirect('login')
    
    user = User_info.objects.get(id=user_id)
    
    description_query = request.GET.get('description')
    type_query = request.GET.get('type')
    selection_query = request.GET.get('selection')
    status_query = request.GET.get('status')
    response_query = request.GET.get('response')
    date_of_Add_query = request.GET.get('date_of_Add')




    
    if user.is_admin:
        context = {'user': user}
        return render(request, 'menu.html', context)
    else:
        records = User.objects.filter(user=user)
        
        if description_query:
            records = records.filter(description__icontains=description_query)
        if type_query:
            records = records.filter(type__icontains=type_query)
        if selection_query:
            records = records.filter(selection__icontains=selection_query)
        if status_query:
            records = records.filter(status__icontains=status_query)    
        if response_query:
            records = records.filter(response__icontains=response_query)
        if date_of_Add_query:
            records = records.filter(date_of_Add__icontains=date_of_Add_query)
            
        z = sum(1 for x in records if x.response)

        if z == 0:
            messages.error(request, 'AUCUN MESSAGE')
        else:
            messages.error(request, 'VOUS AVEZ UN NOUVEAU MESSAGE')
        
        context = {'records': records, 'user': user}
        return render(request, 'Listingpage.html', context)

def user_reclamation(request):
    user_id = request.session.get('user_id')

    # Récupérer l'objet utilisateur
    user = User_info.objects.get(id=user_id)

    # Requête de recherche
    description_query = request.GET.get('description')
    type_query = request.GET.get('type')
    selection_query = request.GET.get('selection')
    status_query = request.GET.get('status')
    response_query = request.GET.get('response')
    date_of_Add_query = request.GET.get('date_of_Add')
    name_query = request.GET.get('name')

    # Filtrer les réclamations en fonction des critères de recherche
    records = User.objects.all()
    
    if name_query:
        # Filtrer en fonction du nom de l'utilisateur associé
        records = records.filter(user__name__icontains=name_query)
    if description_query:
        records = records.filter(description__icontains=description_query)
    if type_query:
        records = records.filter(type__icontains=type_query)
    if selection_query:
        records = records.filter(selection__icontains=selection_query)
    if status_query:
        records = records.filter(status__icontains=status_query)
    if response_query:
        records = records.filter(response__icontains=response_query)
    if date_of_Add_query:
        records = records.filter(date_of_Add__icontains=date_of_Add_query)

    context = {'records': records, 'user': user}
    return render(request, 'validation.html', context)

    


def mise(request):
    user_id = request.session.get('user_id')

    # Récupérer l'objet utilisateur
    user = User_info.objects.get(id=user_id)

    email_query = request.GET.get('email')
    mobile_number_query = request.GET.get('mobile_number')
    codeaffectation_query = request.GET.get('codeaffectation')
    password_query = request.GET.get('password')
    name_query = request.GET.get('name')

    # Si l'utilisateur est un administrateur, récupérer toutes les réclamations

    records = User_info.objects.all()
    if name_query:
        # Filtrer en fonction du nom de l'utilisateur associé
        records = records.filter(name__icontains=name_query)
    if email_query:
        records = records.filter(email__icontains=email_query)
    if mobile_number_query:
        records = records.filter(mobile_number__icontains=mobile_number_query)
    if codeaffectation_query:
        records = records.filter(codeaffectation__intituler__icontains=codeaffectation_query)
    if password_query:
        records = records.filter(password__icontains=password_query)

    context = {'records': records, 'user': user}
    return render(request, 'miseuser.html', context)

    
    
  

def AddUser(request):
    user_id = request.session.get('user_id')
    if not user_id:
        return redirect('login')  # Rediriger vers la page de connexion si l'utilisateur n'est pas connecté

    user = User_info.objects.get(id=user_id)

    if request.method == "POST":
        form = UserForm(request.POST or None, request.FILES or None)
        if form.is_valid():
            reclamation= form.save(commit=False)
            reclamation.user = user
            reclamation.save()
            return redirect('/')
    else:
        form = UserForm()

    context = {'form': form}
    return render(request, 'Add.html', context)

#add users
from .forms import miseuser 
def Mise_add(request):
    user_id = request.session.get('user_id')
    if not user_id:
        return redirect('login')  # Rediriger vers la page de connexion si l'utilisateur n'est pas connecté

    user = User_info.objects.get(id=user_id)

    if request.method == "POST":
        form = miseuser(request.POST or None, request.FILES or None)
        if form.is_valid():
            reclamation= form.save(commit=False)
            reclamation.user = user
            reclamation.save()
            return redirect('/')
    else:
        form = miseuser()

    context = {'form': form}
    return render(request, 'miseadd.html', context)

#mise edit user
def MiseeditUser(request, id=None):
    one_rec = get_object_or_404(User_info, pk=id)
    form = miseuser(request.POST or None, request.FILES or None, instance=one_rec)
    if form.is_valid():
        form.save()
        return redirect('/')
    mydict = {'form': form}
    return render(request, 'editmise.html', context=mydict)

def miseDelete(request, eid=None):
    one_rec = get_object_or_404(User_info, pk=eid)
    if request.method == "POST":
        one_rec.delete()
        return redirect('/')
    return render(request, 'Deletemise.html')


def addreponse(request, id=None):
    one_rec = get_object_or_404(User, pk=id)
    form = Userreponse(request.POST or None, request.FILES or None, instance=one_rec)
    if form.is_valid():
        form.save()
        return redirect('/Reclam')
    mydict = {'form': form}
    return render(request, 'reponse.html', context=mydict)


def EditUser(request, id=None):
    one_rec = get_object_or_404(User, pk=id)
    form = UserForm(request.POST or None, request.FILES or None, instance=one_rec)
    if form.is_valid():
        form.save()
        return redirect('/')
    mydict = {'form': form}
    return render(request, 'Edit.html', context=mydict)






def DeleteUser(request, eid=None):
    one_rec = get_object_or_404(User, pk=eid)
    if request.method == "POST":
        one_rec.delete()
        return redirect('/')
    return render(request, 'Delete.html')


def miseDelete(request, eid=None):
    one_rec = get_object_or_404(User_info, pk=eid)
    if request.method == "POST":
        one_rec.delete()
        return redirect('/')
    return render(request, 'Deletemise.html')


def ViewUser(request, eid=None):
    one_rec = get_object_or_404(User, pk=eid)
    mydict = {'user': one_rec}
    return render(request, 'View.html', context=mydict)

def Viewadmin(request, eid=None):
    one_rec = get_object_or_404(User, pk=eid)
    mydict = {'user': one_rec}
    return render(request, 'Viewsadmin.html', context=mydict)
from django.shortcuts import render, redirect
from django.contrib import messages
from .models import User_info

def user_login(request):
    if request.method == "POST":
        email = request.POST.get('email')
        password = request.POST.get('password')
        
        try:
            # Rechercher l'utilisateur par email
            user = User_info.objects.get(email=email)
            # Vérifier le mot de passe
            if user.password == password:
                # Enregistrer l'ID de l'utilisateur dans la session
                request.session['user_id'] = user.id
                return redirect('user_list')  # Redirection vers 'user_list' après une connexion réussie
            else:
                messages.error(request, 'Invalid Information')
        except User_info.DoesNotExist:
            messages.error(request, 'Invalid Information')
        
        return redirect('/login/')

    return render(request, 'login.html')




from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .models import ChatMessage, User_info, User

@login_required
def chat_view(request, user_id):
    user_info = User_info.objects.get(pk=user_id)
    user = User.objects.get(user=user_info)  # Associe User à User_info
    messages = ChatMessage.objects.filter(user=user_info).order_by('timestamp')

    if request.method == 'POST':
        message_content = request.POST.get('message')
        is_admin = request.user.is_staff  # ou toute autre logique pour vérifier si l'utilisateur est admin
        ChatMessage.objects.create(user=user_info, message=message_content, is_admin=is_admin)
        return redirect('chat_view', user_id=user_id)
    
    return render(request, 'chat.html', {'user_info': user_info, 'user': user, 'messages': messages})



def chat_view_user(request, user_id):
    user_info = User_info.objects.get(pk=user_id)
    user = User.objects.get(user=user_info)  # Associe User à User_info
    messages = ChatMessage.objects.filter(user=user_info).order_by('timestamp')

    if request.method == 'POST':
        message_content = request.POST.get('message')
        is_admin = request.user.is_staff  # ou toute autre logique pour vérifier si l'utilisateur est admin
        ChatMessage.objects.create(user=user_info, message=message_content, is_admin=is_admin)
        return redirect('chat_view', user_id=user_id)
    
    return render(request, 'chatuser.html', {'user_info': user_info, 'user': user, 'messages': messages})


def princip(request):
    return render(request, 'principal.html')









