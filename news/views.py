from django.urls import reverse
from news.models import Post
from django.views.generic.edit import CreateView, DeleteView
from django.views.generic import ListView
from hitcount.views import HitCountDetailView
from comments.models import Comment
from comments.forms import CommentCreateForm
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views import View

class PostListView(ListView):
    paginate_by= 4
    model= Post
    context_object_name= 'posts_for_list'
    template_name= 'news/home.html'
    ordering= ['-date_of_publication']

    def get_context_data(self, *args, **kwargs):
        context= super().get_context_data(*args, *kwargs)
        context['AI']= Post.objects.filter(category='AI')
        context['Space']= Post.objects.filter(category='Space')
        context['Robotics']= Post.objects.filter(category='Robotics')
        context['General']= Post.objects.filter(category='General')
        context['posts']= Post.objects.all()
        return context

#Detail view of the post, plus hitcountdetailview
class PostDetailView(HitCountDetailView):
    model= Post
    template_name= 'news/detail.html'
    form_class= CommentCreateForm()
    context_object_name= 'one_post'
    slug_url_kwarg= 'post_slug'
    count_hit = True

    def get_queryset(self, *args, **kwargs):
        queryset= super().get_queryset(*args, **kwargs)
        queryset= queryset.filter(slug= self.kwargs['post_slug']) #one post
        return queryset

    def get_context_data(self, *args, **kwargs):
        context= super().get_context_data(*args, **kwargs)
        context['comments']= Post.objects.get(slug= self.kwargs['post_slug']).comments.all() #comments under the post
        context['posts']= Post.objects.all() #all posts for navbar
        context['form']= self.form_class #an empty form
        return context


#Creating comments
class CommentCreateView(LoginRequiredMixin, CreateView):
    model= Comment
    form_class= CommentCreateForm
    template_name= 'news/detail.html'

    def form_valid(self, form):
        form.instance.commentedby= self.request.user
        form.instance.under_the_post= Post.objects.get(slug= self.kwargs['post_slug'])
        return super(CommentCreateView, self).form_valid(form)

    def get_success_url(self):
        return reverse('post_detail', args=[self.kwargs['category'], self.kwargs['post_slug']])

#Main class in detail page
class PostCommentView(View):
    def post(self, request, *args, **kwargs):
        view= CommentCreateView.as_view()
        return view(request, *args, **kwargs)
        
    def get(self, request, *args, **kwargs):
        view= PostDetailView.as_view()
        return view(request, *args, **kwargs)


class CommentDeleteView(DeleteView):
    model= Comment
    pk_url_kwarg= 'commentpk'
    def get_success_url(self):
        return reverse('post_detail', args=[self.kwargs['category'], self.kwargs['post_slug']])


class CategoryListView(ListView):
    paginate_by= 3
    model= Post
    template_name= 'news/category.html'
    context_object_name= 'news_one_category'
    ordering= ['-date_of_publication']

    def get_queryset(self, *args, **kwargs):
        queryset= super().get_queryset(*args, **kwargs)
        qs= queryset.filter(category= self.kwargs['post_category'])
        return qs

    def get_context_data(self, *args, **kwargs):
        context= super().get_context_data(*args, **kwargs)
        context['posts']= Post.objects.all()
        context['main_category']= self.kwargs['post_category']
        return context