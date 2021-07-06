from commentapp.decorators import comment_ownership_required
from django.views.generic import DeleteView
from commentapp.forms import CommentCreationForm
from django.shortcuts import render
from django.utils.decorators import method_decorator

# Create your views here.
from django.views.generic import CreateView
from django.urls import reverse
from commentapp.models import Comment
from articleapp.models import Article


class CommentCreateView(CreateView):
    model = Comment
    form_class = CommentCreationForm
    template_name = 'commentapp/create.html'

    def form_valid(self, form):
        temp_comment = form.save(commit=False)
        temp_comment.article = Article.objects.get(pk=self.request.POST['article_pk'])
        # temp_comment.article = Article.objects.get(pk=form.cleaned_data['article_pk'])    # article_pk는 model에 없기 때문에 form.cleaned로는 사용 불가(기록되지 않음)
        temp_comment.writer = self.request.user
        temp_comment.save()
        return super().form_valid(form)
 
    def get_success_url(self):
        return reverse('articleapp:detail', kwargs={ 'pk': self.object.article.pk })

@method_decorator(comment_ownership_required, 'get')
@method_decorator(comment_ownership_required, 'post')
class CommentDeleteView(DeleteView):
    model = Comment
    context_object_name = 'target_comment'
    template_name = 'commentapp/delete.html'
    
    def get_success_url(self):
        return reverse('articleapp:detail', kwargs={ 'pk': self.object.article.pk })