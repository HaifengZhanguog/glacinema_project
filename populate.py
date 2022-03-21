import os

os.environ.setdefault('DJANGO_SETTINGS_MODULE',
                      'team_project.settings')

import django

django.setup()
from GlaCine.models import *
from django.contrib.auth.models import User


def populate_cinema(cinemas_info):
    for info in cinemas_info:
        c = Cinema.objects.get_or_create(name=info['name'], visit=info['visit'])[0]
        c.picture = info['picture']
        c.save()
    return


def populate():

    admin = User.objects.get_or_create(username='admin')[0]
    admin.set_password('123456')
    admin.is_staff = True
    admin.is_superuser=True
    admin.save()

    cinemas_info = [
        {
            'name': 'Matchbox Cineclub', 'picture': 'images/Matchbox Cineclub.jpg', 'visit': 99999
        },
        {
            'name': 'Glasgow Film Theatre', 'picture': 'images/Glasgow Film Theatre.jpg', 'visit': 99
        },
        {
            'name': 'The Scottish National Theatre Of Variety', 'picture': 'images/The Scottish National Theatre Of Variety.jpg', 'visit': 44
        },
        {
            'name': 'Cineworld Cinema Glasgow Renfrew Street', 'picture': 'images/Cineworld Cinema Glasgow Renfrew Street.jpg', 'visit': 50
        },
        {
            'name': 'ODEON Luxe Glasgow Quay', 'picture': 'images/ODEON Luxe Glasgow Quay.jpg', 'visit': 662
        },
        {
            'name': 'Cineworld Cinema Glasgow IMAX at GSC', 'picture': 'images/Cineworld Cinema Glasgow IMAX at GSC.jpg', 'visit': 530
        },

        {
            'name': 'Grosvenor Cinema', 'picture': 'images/Grosvenor Cinema.jpg', 'visit': 123
        },
        {
            'name': 'ODEON Braehead', 'picture': 'images/ODEON Luxe Glasgow Quay.jpg', 'visit': 222
        },
        {
            'name': 'ODEON Braehead wes', 'picture': 'images/ODEON Luxe Glasgow Quay.jpg', 'visit': 226
        },

    ]


    populate_cinema(cinemas_info)


if __name__ == '__main__':
    print('Starting population script...')
    populate()