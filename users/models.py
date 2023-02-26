from django.contrib.auth.models import AbstractUser
from django.db import models
from django.utils.translation import gettext_lazy as _
from users.validators import check_birth_date, check_email_address


class Location(models.Model):
    name = models.CharField(max_length=200, unique=True)
    lat = models.DecimalField(max_digits=8, decimal_places=6, null=True, blank=True)
    lng = models.DecimalField(max_digits=8, decimal_places=6, null=True, blank=True)

    class Meta:
        verbose_name = "Местоположение"
        verbose_name_plural = "Местоположения"

    def __str__(self):
        return self.name


class UserRoles(models.TextChoices):
    MEMBER = "member", _("member")
    MODERATOR = "moderator", _("moderator")
    ADMIN = "admin", _("admin")


# STAFF_ROLES = [UserRoles.MEMBER, UserRoles.MODERATOR, UserRoles.ADMIN]


class User(AbstractUser):
    role = models.CharField(choices=UserRoles.choices, default=UserRoles.MEMBER, max_length=9)
    age = models.PositiveSmallIntegerField(null=True)
    location = models.ManyToManyField(Location)
    birth_date = models.DateField(verbose_name="Дата рождения", validators=[check_birth_date],
                                  blank=True, null=True)
    email = models.EmailField(unique=True, blank=True, null=True, validators=[check_email_address])

    class Meta:
        verbose_name = "Пользователь"
        verbose_name_plural = "Пользователи"
        ordering = ["username"]

    def __str__(self):
        return self.username
