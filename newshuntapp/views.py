from django.shortcuts import render

# Create your views here.

from django.http import HttpResponse

from newshuntapp.forms import UserForm

def register(request):
	# Get the context from the request.
    #context = RequestContext(request)

    # A HTTP POST?
    if request.method == 'POST':
        print(request.POST)
        reg_user = UserForm(request.POST)
        # Have we been provided with a valid form?
        if reg_user.is_valid():
            # Save the new category to the database.
            reg_user.role='Reader'
            reg_user.save(commit=True)
        else:
            # The supplied form contained errors - just print them to the terminal.
            print reg_user.errors
    else:
        # If the request was not a POST, display the form to enter details.
        reg_user = UserForm()

    # Bad form (or form details), no form supplied...
    # Render the form with error messages (if any).
    #return render_to_response('index.html', {'user': user}, context)
    #return render(request, 'index.html', {'reg_user' : reg_user})
    return render(request, "index.html", {'form': reg_user})