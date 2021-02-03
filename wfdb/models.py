from django.db import models


class URL(models.Model):
    created = models.DateTimeField(auto_now_add=True)
    url = models.URLField()
    ALLOW = 1
    BLOCK = 2
    ACTION_CHOICES = [
        (ALLOW, 'Allow'),
        (BLOCK, 'Block'),
    ]
    action = models.IntegerField(choices=ACTION_CHOICES, default=ALLOW)
    comment = models.TextField(blank=True)

    def __str__(self):
        return f'{self.url} ({self.get_action_display()})'

    class Meta:
        ordering = ['created']
