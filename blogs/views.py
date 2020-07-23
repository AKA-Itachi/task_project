from django.shortcuts import render, get_object_or_404
from django.http import HttpResponseRedirect
from django.urls import reverse
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic.edit import CreateView


from blogs.models import blogs, Author, Comment
from django.views import generic
from blogs.forms import CommentModelForm


def index(request):
    """View function for home page of site."""

    # Generate counts of some of the main objects
    num_blogs = blogs.objects.all().count()
    num_authors = Author.objects.all().count()
    num_comments = Comment.objects.all().count()
    num_visits = request.session.get('num_visits', 0)
    request.session['num_visits'] = num_visits + 1
    
    context = {
        'num_books': num_blogs,
        'num_authors': num_authors,
        'num_comments': num_comments,
        'num_visits': num_visits,
    }

    # Render the HTML template index.html with the data in the context variable
    return render(request, 'index.html', context=context)

class BlogsListView(generic.ListView):
    model = blogs #model that we are using the class for
    paginate_by = 5
    context_object_name = 'blogs_list' #template variable name
    queryset = blogs.objects.all()
    template_name = 'blogs/blogs_name_list.html'

class BlogsDetailView(generic.DetailView):
    model = blogs

class AuthorListView(generic.ListView):
    model = Author #model that we are using the class for
    context_object_name = 'author_list' #template variable name
    queryset = Author.objects.all()
    template_name = 'blogs/Author_name_list.html'

class AuthorDetailView(generic.DetailView):
    model = Author

class BlogCommentCreate(LoginRequiredMixin, CreateView):
    """
    Form for adding a blog comment. Requires login. 
    """
    model = Comment
    fields = ['comment',]

    def get_context_data(self, **kwargs):
        """
        Add associated blog to form template so can display its title in HTML.
        """
        # Call the base implementation first to get a context
        context = super(BlogCommentCreate, self).get_context_data(**kwargs)
        # Get the blog from id and add it to the context
        context['blogs'] = get_object_or_404(blogs, pk = self.kwargs['pk'])
        return context
        
    def form_valid(self, form):
        """
        Add user and associated blog to form data before setting it as valid (so it is saved to model)
        """
        #Add logged-in user as user of comment
        form.instance.user = self.request.user
        #Associate comment with blog based on passed id
        form.instance.blog=get_object_or_404(blogs, pk = self.kwargs['pk'])
        # Call super-class form validation behaviour
        return super(BlogCommentCreate, self).form_valid(form)

    def get_success_url(self): 
        """
        After posting comment return to associated blog.
        """
        return reverse('blogs-detail', kwargs={'pk': self.kwargs['pk'],})

