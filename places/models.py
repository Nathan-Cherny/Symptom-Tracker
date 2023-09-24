from django.db import models

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


class Place(models.Model):
    name = models.CharField(max_length=20, choices=LIVES_AT)
    health_score = models.IntegerField()

    def __str__(self):
        return self.name
