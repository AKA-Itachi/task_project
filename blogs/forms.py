from django.forms import ModelForm

from blogs.models import Comment
from blogs.models import blogs


class CommentModelForm(ModelForm):
    def clean_comment(self):
        data = self.cleaned_data['comment']
        # return the cleaned data.
        return data

    class Meta:
        model = Comment
        fields = ['comment', 'blog']
        labels = {'comment': ('Comment')}
        help_texts = {'comment': ('Enter your comment here')}


# Defining modelForm for "createBlogform"
class blogsCreateForm(ModelForm):
    class Meta:
        model = blogs
        exclude = ["author", "pub_date"]

