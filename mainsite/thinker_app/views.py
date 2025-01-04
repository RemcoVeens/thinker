from django.views.generic import TemplateView
# Create your views here.
class home(TemplateView):
    template_name= "base/home.html"
