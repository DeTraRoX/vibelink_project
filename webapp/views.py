from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login as auth_login, logout as auth_logout
from django.contrib import messages
from django.urls import reverse
from django.contrib.auth.decorators import login_required
from datetime import datetime
from .models import UserProfile, Friendship, Interest
from .forms import RegisterForm, ContactForm, UserLoginForm
from django.db.models import Q



def home(request):
    return render(request, 'webapp/home.html')


def register(request):
    if request.method == 'POST':
        first_name = request.POST.get('first_name')
        email = request.POST.get('email')
        password = request.POST.get('password')
        gender = request.POST.get('gender')
        month = request.POST.get('month')
        day = request.POST.get('day')
        year = request.POST.get('year')
        avatar = request.FILES.get('avatar')
        interest_ids = request.POST.getlist('interests')

        try:
            birthday = datetime.strptime(f"{year}-{month}-{day}", "%Y-%m-%d").date()
        except ValueError:
            return render(request, 'webapp/register.html', {
                'error': 'Invalid birthday format.',
                'interests': Interest.objects.all()
            })

        if User.objects.filter(email=email).exists() or User.objects.filter(username=email).exists():
            return render(request, 'webapp/register.html', {
                'error': 'Email already registered.',
                'interests': Interest.objects.all()
            })

        try:
            # Create user
            user = User.objects.create_user(username=email, email=email, password=password)
            user.first_name = first_name
            user.save()

            # Access UserProfile (auto-created via signal)
            profile = user.userprofile
            profile.gender = gender
            profile.birthday = birthday
            if avatar:
                profile.avatar = avatar
            profile.save()

            # Filter valid interests to avoid FK constraint errors
            valid_interests = Interest.objects.filter(id__in=interest_ids)
            profile.interests.set(valid_interests)

            # Authenticate and login user
            user = authenticate(request, username=email, password=password)
            if user:
                auth_login(request, user)
                return redirect('profile_suggest')  # redirect to friend suggestions page

        except Exception as e:
            return render(request, 'webapp/register.html', {
                'error': f'Error: {str(e)}',
                'interests': Interest.objects.all()
            })

    return render(request, 'webapp/register.html', {'interests': Interest.objects.all()})


def user_login(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)

        if user is not None:
            auth_login(request, user)
            next_url = request.GET.get('next', None)
            if next_url:
                return redirect(next_url)
            return redirect(reverse('suggestions'))

        messages.error(request, 'Invalid username or password.')

    return render(request, 'webapp/login.html')


def user_logout(request):
    auth_logout(request)
    return redirect('home')


def about_view(request):
    return render(request, 'webapp/about.html')


def contact_view(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            messages.success(request, "Thank you for reaching out! We'll get back to you soon.")
            return redirect('contact')
    else:
        form = ContactForm()

    return render(request, 'webapp/contact.html', {'form': form})


def forget_pass(request):
    return render(request, 'webapp/forget_pass.html')


@login_required
def suggest_friends(request):
    user = request.user
    profile, created = UserProfile.objects.get_or_create(user=user)

    my_interests = profile.interests.all()

    friendships = Friendship.objects.filter(Q(from_user=user) | Q(to_user=user))
    added_friends = [f.to_user if f.from_user == user else f.from_user for f in friendships]

    # Exclude self and already added friends
    candidates = User.objects.exclude(id=user.id).exclude(id__in=[f.id for f in added_friends])

    # Users with common interests
    with_common_interests = candidates.filter(
        userprofile__interests__in=my_interests
    ).distinct()

    # Users without any common interests
    without_common_interests = candidates.exclude(
        id__in=with_common_interests.values_list('id', flat=True)
    )

    # Combine lists: first users with interests, then others
    suggestions = list(with_common_interests) + list(without_common_interests)

    return render(request, 'webapp/suggestions.html', {
        'suggestions': suggestions,
        'added_friends': added_friends
    })

@login_required
def chat_view(request):
    friendships = Friendship.objects.filter(from_user=request.user) | Friendship.objects.filter(to_user=request.user)
    friends = []
    for f in friendships:
        friend_user = f.to_user if f.from_user == request.user else f.from_user
        friends.append({
            'id': friend_user.id,
            'username': friend_user.username,
            'avatar': friend_user.userprofile.avatar.url if hasattr(friend_user, 'userprofile') and friend_user.userprofile.avatar else None,
        })
    active_friend = friends[0] if friends else None
    return render(request, 'webapp/chat_page.html', {
        'friends': friends,
        'active_friend': active_friend,
    })


@login_required
def add_friend(request, user_id):
    to_user = get_object_or_404(User, id=user_id)
    if to_user == request.user:
        return redirect('suggest_friends')
    if Friendship.objects.filter(from_user=request.user, to_user=to_user).exists() or \
       Friendship.objects.filter(from_user=to_user, to_user=request.user).exists():
        return redirect('suggestions')
    Friendship.objects.create(from_user=request.user, to_user=to_user)
    return redirect('suggestions')
