from django.db import models

class LegendaryMomentManager(models.Manager):
    def create_legendary_moment(self, title, description, date, boxscore_url=None, video_url=None):
        legendary_moment = self.create(
            title=title,
            description=description,
            date=date,
            boxscore_url=boxscore_url,
            video_url=video_url
        )
        return legendary_moment
class LegendaryMoment(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()
    date = models.DateField()
    boxscore_url = models.URLField(blank=True, null=True)
    video_url = models.URLField(blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    objects = LegendaryMomentManager()
    def __str__(self):
        return self.title
