from django.shortcuts import render,redirect
from .models import Resepti, Vaihe, ReseptiAines
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.models import User

#LOGIN
def loginview(request):
    return render(request, 'loginpage.html')

def login_action(request):
    usern = request.POST['username']
    passw = request.POST['password']
    user = authenticate(username = usern,password = passw)
    if user:
        login(request,user)
        return redirect('reseptit')  # Use redirect instead of render
    else:
        return render(request,'loginerror.html')

def logout_action(request):
    logout(request)
    return render(request,'loginpage.html')

def registerview(request):
    return render(request, 'registerpage.html')

def register_action(request):
    usern = request.POST['username']
    passw = request.POST['password']
    
    if User.objects.filter(username=usern).exists():
        return render(request,'loginerror.html', {'error': 'Käyttäjänimi on jo käytössä.'})
    else:
        User.objects.create_user(username = usern, password = passw)
        user = authenticate(username=usern, password=passw)
        if user:
            login(request,user)
            return redirect('reseptit')
        else:
            return redirect('login')  # Redirect to login view if authentication fails


#RESEPTIT

def reseptit(request):
    reseptit = Resepti.objects.all()
    context = {
        'reseptit': reseptit,
    }
    return render(request, 'reseptit.html', context)

def poista_resepti(request,id):
    resepti = Resepti.objects.get(id=id)
    resepti.delete()

    return redirect('reseptit')  # Use redirect instead of render


def muokkaa_resepti(request,id):
    resepti = Resepti.objects.get(id=id)
    context = {'resepti': resepti}
    return render(request, 'resepti.html', context)


def uusi_resepti(request):
    return render(request, 'resepti.html' )


def tallenna_resepti(request):
    resepti_id = request.POST.get('resepti_id')
    resepti_nimi = request.POST['nimi']
    resepti_kuvaus = request.POST['kuvaus']

    aines_nimet = request.POST.getlist('aines_nimi[]')
    maarat = request.POST.getlist('maara[]')
    yksikot = request.POST.getlist('yksikko[]')
    
    vaihe_kuvaukset = request.POST.getlist('vaihe_kuvaus[]')
    vaihe_ajat = request.POST.getlist('vaihe_aika[]')

    if resepti_id:  # Editing existing
        resepti = Resepti.objects.get(id=resepti_id)
        resepti.nimi = resepti_nimi
        resepti.kuvaus = resepti_kuvaus
        resepti.ainekset.clear()
        resepti.vaiheet.clear()
    else:  # New recipe
        resepti = Resepti.objects.create(nimi=resepti_nimi, kuvaus=resepti_kuvaus)
    

    for nimi, maara, yksikko in zip(aines_nimet, maarat, yksikot):
            if nimi.strip():  # skip empty rows
                aines_obj = ReseptiAines.objects.create(
                    aines=nimi,
                    maara=maara or 0,
                    yksikko=yksikko
                )
                resepti.ainekset.add(aines_obj)


    totaali_aika = 0
    
    for index, (kuvaus, aika) in enumerate(zip(vaihe_kuvaukset, vaihe_ajat), start=1):
        if kuvaus.strip():
            vaihe_obj = Vaihe.objects.create(
                kuvaus=kuvaus,
                aika_minuuttia=int(aika or 0),
            )
            resepti.vaiheet.add(vaihe_obj)
            totaali_aika += int(aika or 0)

    resepti.aika_minuuttia = totaali_aika
    resepti.save()


    return redirect('reseptit')  # Use redirect instead of render
