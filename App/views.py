from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import login, logout
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.decorators import login_required
from django.views.decorators.http import require_POST
from .forms import TeamSignUpForm, SubmissionForm
from django.contrib.admin.views.decorators import staff_member_required
from . import models






def home_view(request):
    return render(request, 'home.html')


@login_required
def success_view(request):
    return render(request, 'success.html')


def signup_view(request):
    if request.method == 'POST':
        form = TeamSignUpForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.set_password(form.cleaned_data['password'])
            user.save()
            login(request, user)
            return redirect('home')
    else:
        form = TeamSignUpForm()
    return render(request, 'signup.html', {'form': form})


def login_view(request):
    if request.method == 'POST':
        form = AuthenticationForm(data=request.POST)
        if form.is_valid():
            login(request, form.get_user())
            return redirect('home')
    else:
        form = AuthenticationForm()
    return render(request, 'login.html', {'form': form})


@require_POST
def logout_view(request):
    logout(request)
    return redirect('login')


@login_required
def submission_view(request):
    existing = getattr(request.user, 'submission', None)
    if request.method == 'POST':
        form = SubmissionForm(request.POST, instance=existing)
        if form.is_valid():
            sub = form.save(commit=False)
            sub.team = request.user
            sub.save()
            return render(request, 'success.html')
    else:
        form = SubmissionForm(instance=existing)
    return render(request, 'submission.html', {'form': form})


@staff_member_required
def teams_list_view(request):
    teams = models.Team.objects.all().select_related('challenge', 'submission')
    challenges = models.Challenge.objects.all()
    
    challenge_filter = request.GET.get('challenge')
    uni_filter = request.GET.get('university')

    if challenge_filter:
        teams = teams.filter(challenge_id=challenge_filter)
    if uni_filter:
        teams = teams.filter(university__icontains=uni_filter)

    return render(request, 'teams_list.html', {
        'teams': teams,
        'challenges': challenges,
    })


@staff_member_required
def submission_list_view(request):
    submissions = models.Submission.objects.select_related('team').order_by('-submitted_at')
    return render(request, 'submissions_list.html', {'submissions': submissions})


def tracks_list_view(request):
    """Displays the 5 main mission sectors."""
    tracks = models.Track.objects.all().prefetch_related('challenges')[:5]
    return render(request, 'tracks_list.html', {'tracks': tracks})


def track_detail_view(request, track_id):
    """Briefing for a specific track and its 2 associated challenges."""
    track = get_object_or_404(models.Track, pk=track_id)
    return render(request, 'track_detail.html', {'track': track})


def Comitee_Team(request):
    return render(request, 'Committee_Competitio.html')


def Courses(request):
    return render(request, 'Courses.html')


def AstroCode2025(request):
    return render(request, '2025.html')