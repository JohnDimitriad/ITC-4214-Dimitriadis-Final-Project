from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib.auth.forms import UserChangeForm
from django.contrib.auth.decorators import login_required
from .forms import EditProfileForm



def login_view(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('home:index')  # Redirect to home page after successful login
        else:
            return render(request, 'home/login.html', {'error': 'Invalid credentials'})
    return render(request, 'home/login.html')


def register(request):
    if request.method == 'POST':
        username = request.POST['username']
        email = request.POST['email']
        password = request.POST['password']
        confirm_password = request.POST['confirm_password']
        
        # Check if passwords match
        if password != confirm_password:
            messages.error(request, "Passwords do not match.")
            return render(request, 'home/register.html')
        
        # Check if the username already exists
        if User.objects.filter(username=username).exists():
            messages.error(request, "Username already exists.")
            return render(request, 'home/register.html')

        # Check if the email is already in use
        if User.objects.filter(email=email).exists():
            messages.error(request, "Email is already in use.")
            return render(request, 'home/register.html')

        # Create the user
        try:
            user = User.objects.create_user(username=username, email=email, password=password)
            user.save()
            messages.success(request, "Registration successful. You can now log in.")
            return redirect('home:login')  # Redirect to the login page
        except Exception as e:
            messages.error(request, f"An error occurred: {str(e)}")
            return render(request, 'home/register.html')

    # Render the registration page for GET requests
    return render(request, 'home/register.html')

def home(request):
    return render(request, 'home/index.html')

@login_required
def profile(request):
    return render(request, 'home/profile.html')

@login_required
def edit_profile(request):
    user = request.user
    if request.method == 'POST':
        form = UserChangeForm(request.POST, instance=user)
        if form.is_valid():
            form.save()
            messages.success(request, 'Your profile has been updated successfully.')
            return redirect('home:profile')  # Redirect to the profile page
        else:
            messages.error(request, 'There was an error updating your profile.')
    else:
        form = UserChangeForm(instance=user)

    return render(request, 'home/edit_profile.html', {'form': form})


@login_required
def logout_view(request):
    logout(request)
    return redirect('home:login')