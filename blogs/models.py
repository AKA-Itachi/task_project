from django.db import models
from django.contrib.auth.models import User

# Used to generate URLs by reversing the URL patterns
from django.urls import reverse


class blogs(models.Model):
    """Model representing a blog"""
    title = models.CharField(max_length=200)
    description = models.TextField(max_length=1000, help_text='Enter a brief description')
    photo = models.ImageField(upload_to='uploads/')
    # slug = models.SlugField('',max_length=60)

    # Foreign Key used because blog can only have one author, but authors can have multiple blogs
    author = models.ForeignKey('Author', on_delete=models.SET_NULL, null=True)

    pub_date = models.DateTimeField('Publish Date', auto_now=True)

    class Meta:
        ordering = ['-pub_date']

    def __str__(self):
        """String for representing the Model object."""
        return self.title

    def get_absolute_url(self):
        """Returns the url to access a detail record for this blog."""
        return reverse('blogs-detail', args=[str(self.id)])


class Author(models.Model):
    """Model representing an author."""
    name = models.CharField(max_length=100)
    date_of_birth = models.DateField(null=True, blank=True)
    bio = models.TextField('Bio', max_length=700)

    class Meta:
        ordering = ['name']

    def get_absolute_url(self):
        """Returns the url to access a particular author instance."""
        return reverse('author-detail', args=[str(self.id)])

    def __str__(self):
        """String for representing the Model object."""
        return f'{self.id}, {self.name}'

class Comment(models.Model):
    """Model representing a comment on the blog."""
    comment = models.TextField(max_length=300, help_text='Enter a your comment')
    blog = models.ForeignKey('blogs',on_delete=models.SET_NULL, null=True)
    comment_date = models.DateTimeField('Comment Date',auto_now_add=True)
    user = models.ForeignKey(User,on_delete=models.SET_NULL, null=True, blank = True)

    class Meta:
        ordering = ['comment_date']

    def __str__(self):
        """String for representing the Model object."""
        return self.comment
