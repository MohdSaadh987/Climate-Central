
# views.py
# views.py
from django.shortcuts import render, redirect
from .forms import UserRegistrationForm

def registration_view(request):
    if request.method == 'POST':
        form = UserRegistrationForm(request.POST)
        if form.is_valid():
            try:
                instance = form.save()  # Save the data to the database
                print("Form saved successfully:", instance)
            except Exception as e:
                print("Error saving form:", e)
            return redirect('registration_success')  # Redirect to a success page
        else:
            print("Form is not valid:", form.errors)
    else:
        form = UserRegistrationForm()
    return render(request, 'registration_template.html', {'form': form})


# views.py
from django.shortcuts import render

def registration_success(request):
    return render(request, 'registration_success.html')






# def social_links(request):
#     sl = Social.objects.all()
#     context = {
#         'sl': sl
#     }
#     return render(request, 'weather_api/base.html', context)
