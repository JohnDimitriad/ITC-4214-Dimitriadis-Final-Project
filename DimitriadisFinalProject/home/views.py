from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate, logout, update_session_auth_hash
from django.contrib.auth.models import User
from django.contrib import messages
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
    if request.method == 'POST':
        user = request.user
        form = EditProfileForm(request.POST, instance=user)
        # Get password fields from the request
        password = request.POST.get('password')
        confirm_password = request.POST.get('confirm_password')
        if form.is_valid():
            if password and confirm_password:  # Check if password fields are filled
                if password == confirm_password:
                    user.set_password(password)
                else:
                    messages.error(request, "Passwords do not match.")
                    return redirect('home:edit_profile')

            form.save()
            update_session_auth_hash(request, user)  # Prevent logout after password change
            messages.success(request, "Profile updated successfully.")
            return redirect('home:profile')
        else:
            messages.error(request, "Please correct the errors below.")
    else:
        form = EditProfileForm(instance=request.user)
    return render(request, 'home/edit_profile.html', {'form': form})

@login_required
def logout_view(request):
    logout(request)
    return redirect('home:login')