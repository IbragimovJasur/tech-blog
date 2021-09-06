from django.views.generic import CreateView
from .forms import MessageCreateForm
from news.models import Post
from django.contrib.auth.mixins import LoginRequiredMixin

class MessageCreateView(LoginRequiredMixin, CreateView):
    form_class= MessageCreateForm
    template_name= 'contactus/contact.html'
    success_url= '/contact'

    def form_valid(self, form):
        if self.request.user.is_authenticated:
            form.instance.sentby= self.request.user
        return super(MessageCreateView, self).form_valid(form)
       
    def get_context_data(self, *args, **kwargs):
        context= super().get_context_data(*args, **kwargs)
        context['posts']= Post.objects.all()
        return context