from django.shortcuts import render,redirect

# Create your views here.



from django.shortcuts import render
from .forms import StudentApplicationForm

def student_application(request):
    form = StudentApplicationForm()  
    if request.method == 'POST':
        form = StudentApplicationForm(request.POST)
        if form.is_valid():
            form.save()
           
            return render(request, 'myclarkeform/clarke_form.html')  # Replace 'success.html' with your success template
    # If it's a GET request or the form is invalid, render the form template with the form
    return render(request, 'myclarkeform/clarke_form.html', {'form': form})
