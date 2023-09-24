from django.db import models
from django.contrib.auth import get_user_model

User = get_user_model()

DIAGNOSED_WITH = [
    ('nothing', 'nothing'),
    ('covid', 'covid'),
    ('common cold', 'common cold'),
    ('stomach bug', 'stomach bug')
]

LIVES_AT = [
    ('kardon', 'kardon'),
    ('atlantic', 'atlantic'),
    ('university', 'university'),
    ('james_s_white', 'james_s_white'),
    ('j_h', 'j_h'),
    ('nineteen_forty', 'nineteen_forty'),
    ('conwell', 'conwell'),
    ('edge', 'edge'),
    ('morgan_hall', 'morgan_hall'),
    ('oxford_village', 'oxford_village'),
    ('thirteen', 'thirteen'),
    ('temple_towers', 'temple_towers'),
    ('beech', 'beech'),
]


class Report(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    diagnosed_with = models.CharField(max_length=20, choices=DIAGNOSED_WITH)
    lives_at = models.CharField(max_length=20, choices=LIVES_AT)
    symptoms = models.JSONField(default=dict)
    smoked = models.BooleanField()
    drank = models.BooleanField()
    around_sick = models.BooleanField()
    created_at = models.DateTimeField(auto_now_add=True)
    modified_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.user.name
