from django.db.models import QuerySet, Q
from django.http import HttpRequest

from users.models import Profile, Skill, Message


# Get all profiles
def get_all_profiles() -> QuerySet:
    return Profile.objects.all()

# Get filtered profiles
def get_filtered_profiles(search_query: str) -> QuerySet:
    skills = Skill.objects.filter(name__icontains=search_query)
    return Profile.objects.distinct().filter(
        Q(name__icontains = search_query) | 
        Q(short_info__icontains = search_query) | 
        Q(skill__in = skills)
        )

# Get profile by uuid
def get_profile(pk: str) -> QuerySet:
    return Profile.objects.filter(id = pk).first()

# Get top skills of profile
def get_top_skills_profile(pk: str) -> QuerySet:
    profile = get_profile(pk)
    return profile.skill_set.exclude(description__exact="")

# Get other skills of profile
def get_other_skills_profile(pk: str) -> QuerySet:
    profile = get_profile(pk)
    return profile.skill_set.filter(description="")

# Get other skills of profile
def get_all_skills_profile(pk: str) -> QuerySet:
    profile = get_profile(pk)
    return profile.skill_set.all()

# Get skill by pk
def get_skill(pk: str) -> QuerySet:
    return Skill.objects.filter(pk=pk).first()

# Get user projects
def get_user_projects(pk: str) -> QuerySet:
    profile = get_profile(pk)
    return profile.project_set.all()

# Get all messages
def get_all_messages(profile: Profile) -> QuerySet:
    return profile.messages.all()

# Get message by id
def get_message(request: HttpRequest, pk: str) -> QuerySet:
    profile = request.user.profile
    return profile.messages.get(id=pk)

