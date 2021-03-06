from decimal import Decimal

from attr import evolve
from django.db.models import F
from mappers import Mapper

from bookshelf import models
from bookshelf.entities import Profile
from bookshelf.entities import ProfileId


config = {
    "primary_key": "id",
    "first_name": ("user", "first_name"),
    "last_name": ("user", "last_name"),
    "email": ("user", "email"),
    "date_joined": ("user", "date_joined"),
}

mapper = Mapper(Profile, models.Profile, config,)


@mapper.reader
def load_profile(profile_id: ProfileId) -> Profile:
    return models.Profile.objects.filter(pk=profile_id)


@mapper.reader
def create_profile(user) -> Profile:
    # FIXME: Do not fetch the same data twice.
    created = models.Profile.objects.create(user=user, balance=0)
    return models.Profile.objects.filter(pk=created.pk)


def add_balance(profile: Profile, amount: Decimal) -> Profile:
    # TODO: Use update returning queryset.
    models.Profile.objects.filter(pk=profile.primary_key).update(
        balance=F("balance") + amount
    )
    return evolve(profile, balance=profile.balance + amount)


def decrease_balance(profile, amount):
    # TODO: Use update returning queryset.
    models.Profile.objects.filter(pk=profile.primary_key).update(
        balance=F("balance") - amount
    )
    return evolve(profile, balance=profile.balance - amount)
