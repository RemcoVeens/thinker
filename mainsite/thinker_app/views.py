from django.views.generic import TemplateView
from .models import Thought

class home(TemplateView):
    template_name= "base/home.html"

    def get_context_data(self, **kwargs):
        context =  super().get_context_data(**kwargs)
        context["thoughts"] = Thought.objects.all()
        return context

    def get(self, request, *args, **kwargs):
        return super().get(request, *args, **kwargs)
