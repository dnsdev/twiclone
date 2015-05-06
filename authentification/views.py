from django.shortcuts import render
from django.views import generic
from .forms import LoginForm


class LoginView(generic.FormView):
    template_name = 'authentification/login.html'
    form_class = LoginForm
    success_url = '/'

    def form_valid(self, form):
        form.check_password()
        return super(LoginView, self).form_valid(form)


def login(request):
    return render(request, 'authentification/login.html', None)


def logout(request):
    return render(request, 'authentification/logout.html', None)