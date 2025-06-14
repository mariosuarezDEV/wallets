from allauth.account.views import SignupView
from .forms import CustomSignupForm
# Create your views here.

class MyCustomSignupView(SignupView):
    template_name = 'registro.html'
    form_class = CustomSignupForm
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['form'] = self.form_class()
        return context