from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.contrib.auth.models import User

# Create your views here.
@login_required
def user_profile(request):
    user = request.user
    bio = request.session.get('user_bio', "Professional dare-devil and challenge enthusiast. Always up for the next adventure! 🚀")
    location = getattr(user, 'location', None) or request.session.get('user_location', '')
    if request.method == "POST":
        first_name = request.POST.get('first_name', '').strip()
        last_name = request.POST.get('last_name', '').strip()
        bio = request.POST.get('bio', '').strip()
        location = request.POST.get('location', '').strip()
        user.first_name = first_name
        user.last_name = last_name
        # Save location if User model has it, else save to session
        if hasattr(user, 'location'):
            user.location = location
        user.save()
        request.session['user_bio'] = bio
        request.session['user_location'] = location
        messages.success(request, "Profile updated successfully!")
        return redirect('profile')
    context = {
        'profile_user': user,
        'is_own_profile': True,
        'bio': bio,
        'location': location,
    }
    return render(request, "profile.html", context)

def network(request):
    return render(request, "network.html")