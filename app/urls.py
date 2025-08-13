from django.urls import path
from .views import register_action, registerview, loginview, login_action, logout_action, reseptit, uusi_resepti, poista_resepti,muokkaa_resepti, tallenna_resepti

urlpatterns = [
    path('',loginview),
    path('login/',loginview),
	path('login-action/',login_action),

	path('logout/',logout_action),

	path('register/', registerview, name='register'),
    path('register-action/', register_action, name='register-action'),

    
    path('reseptit/', reseptit, name = 'reseptit'),

    path('uusi-resepti/', uusi_resepti, name = 'uusi_resepti'),
    path('tallenna-resepti/', tallenna_resepti, name = 'tallenna_resepti'),

    path('poista-resepti/<int:id>/', poista_resepti),

    path('muokkaa-resepti/<int:id>/', muokkaa_resepti),
]