from django.urls import reverse_lazy
from django.views.generic.edit import CreateView
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import authenticate, login
class ClientRegistrationView(CreateView):
    template_name = 'clients/client/registration.html'  
    form_class = UserCreationForm
    success_url = reverse_lazy('shop:product_home')
    def form_valid(self, form):
        result = super().form_valid(form)
        cd = form.cleaned_data
        user = authenticate(username=cd['username'],
                         password=cd['password1'])
        login(self.request, user)
        return result