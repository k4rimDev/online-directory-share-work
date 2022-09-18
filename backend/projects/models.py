from django.db import models
from django.db.models import QuerySet

from users.models import Profile
import uuid

class Project(models.Model):
    owner = models.ForeignKey(Profile, null=True, blank=True, on_delete=models.CASCADE)
    title = models.CharField(max_length=128)
    description = models.TextField(null=True, blank=True)
    featured_image = models.ImageField(null=True, blank=True, default="default.jpg")
    demo_link = models.URLField(max_length=2000, null=True, blank=True)  
    source_link = models.URLField(max_length=200, null=True, blank=True)
    tags = models.ManyToManyField('Tag', blank=True)
    vote_total = models.IntegerField(default=0, null=True, blank=True)
    vote_ratio = models.IntegerField(default=0, null=True, blank=True)
    created = models.DateTimeField(auto_now_add=True)
    id = models.UUIDField(default=uuid.uuid4, primary_key=True, editable=False, unique=True)

    def __str__(self) -> str:
        return self.title

    class Meta:
        ordering = ["-vote_ratio", "-vote_total", "title"]

    @property
    def image_url(self):
        try:
            image_url = self.featured_image.url
        except:
            image_url = ''
        
        return image_url

    @property
    def get_all_reviewers(self) -> QuerySet: 
        queryset = self.review_set.all().values_list("owner__id", flat=True)
        return queryset

    @property
    def get_vote_count(self): 
        reviews = self.review_set.all()
        up_votes = reviews.filter(value='up').count()
        total_votes = reviews.count() 

        ratio = (up_votes / total_votes) * 100

        self.vote_ratio = float(ratio)
        self.vote_total = total_votes

        self.save()
    
class Review(models.Model):
    VOTE_TYPE = (
        ('up', 'Up Vote'),
        ('down', 'Down Vote')
    )
    owner = models.ForeignKey(Profile, on_delete=models.CASCADE, null=True) 
    project = models.ForeignKey(Project, on_delete=models.CASCADE)
    body = models.TextField(null=True, blank=True)
    value = models.CharField(max_length=200, choices=VOTE_TYPE )
    created = models.DateTimeField(auto_now_add=True)
    id = models.UUIDField(default=uuid.uuid4, primary_key=True, editable=False, unique=True)

    class Meta:
        unique_together = [['owner', 'project']]

    def __str__(self) -> str:
        return self.value


class Tag(models.Model):
    name = models.CharField(max_length=128)
    created = models.DateTimeField(auto_now_add=True)
    id = models.UUIDField(default=uuid.uuid4, primary_key=True, editable=False, unique=True)

    def __str__(self) -> str:
        return self.name