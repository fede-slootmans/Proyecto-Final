from .forms import RegistroUsuarioForm
from django.contrib.auth.views import LoginView, LogoutView
from django.views.generic import CreateView
from django.contrib import messages
from django.shortcuts import redirect
from django.urls import reverse

# Create your views here.

class RegistrarUsuario(CreateView):
    template_name = 'registration/registrar.html'
    form_class = RegistroUsuarioForm

    def form_valid(self, form):
        messages.success(self.request, 'Registro exitoso. Por favor, inicia sesión.')
        form.save()

        return redirect('apps.usuario:registrar')

class LoginUsuario(LoginView):
    template_name = 'registration/login.html'

    def get_success_url(self):
        messages.success(self.request, 'Login existoso.')

        return reverse('apps.usuario:login')

class LogoutUsuario(LogoutView):
    template_name = 'registration/logout.html'

    def get_success_url(self):
        messages.success(self.request, 'Logout exitoso')

        return reverse('apps.usuario:logout')
    
#sin embargo, cuando mejores el código en
#tu proyecto puedes usar, por ejemplo, SweetAlert para mostrar un mensaje emergente
#del registro exitoso y que se redirija a la página de iniciar sesión (puedes buscar
# en la documentación de Django e investigar
#sobre mensajes: https://docs.djangoproject.
#com/en/4.2/ref/contrib/messages/ y sobre
#mensajes SweeAlert: https://lipis.github.io/
#bootstrap-sweetalert/). Lo mismo puedes
#hacer para “login”, “logout” o “contacto” e
#incluso para “comentarios” (app que crearemos luego).