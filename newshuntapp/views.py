from django.shortcuts import render
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.utils import timezone

# from articles.models import Article

# Create your views here.

from django.http import HttpResponse

from newshuntapp.forms import *
from newshuntapp.models import *

def register(request):
	# Get the context from the request.
    #context = RequestContext(request)

    # A HTTP POST?
    if request.method == 'POST':
        reg_user = UserForm(request.POST)
        reg_user.role='Reader'
        # Have we been provided with a valid form?
        if reg_user.is_valid():
            # Save the new category to the database.
            reg_user.save()
            reg_user = UserForm()
        else:
            # The supplied form contained errors - just print them to the terminal.
            print reg_user.errors
            reg_user = UserForm()
    else:
        # If the request was not a POST, display the form to enter details.
        reg_user = UserForm()

    # Bad form (or form details), no form supplied...
    # Render the form with error messages (if any).
    return render(request, "index.html", {'form': reg_user})


def addArticle(request):

	if request.method == 'POST':
		new_article = ArticleForm(request.POST)

		if new_article.is_valid():
			new_article.save()
			new_article = ArticleForm()
		else:            
			print new_article.errors
			new_article = ArticleForm()
	else:
		new_article = ArticleForm()
        
	return render(request, "addarticle.html", {'form': new_article})


class ArticleListView(ListView):

    model = Article

    def get_context_data(self, **kwargs):
        context = super(ArticleListView, self).get_context_data(**kwargs)
        context['now'] = timezone.now()
        return context