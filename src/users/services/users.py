import profile
from pydoc import describe
from users.models import Profile, Skill
from django.db.models import QuerySet

# Get all profiles
def get_all_profiles() -> QuerySet:
    return Profile.objects.all()

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

# Get user projects
def get_user_projects(pk: str) -> QuerySet:
    profile = get_profile(pk)
    return profile.project_set.all()