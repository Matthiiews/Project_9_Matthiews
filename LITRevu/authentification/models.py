from django.contrib.auth.models import AbstractUser
from django.db import models
from django.utils.translation import gettext_lazy as _


class User(AbstractUser):
    """Classe représentant un utilisateur personnalisé héritant
    de la classe AbstractUser
    """


class UserFollows(models.Model):
    """Modèle pour gérer les relations de suivi entre utilisateurs."""

    # Utilisateur qui effectue le suivi
    user = models.ForeignKey("authentification.User",
                             on_delete=models.CASCADE,
                             related_name='following',
                             verbose_name=_("user"))

    # Utilisateur suivi
    followed_user = models.ForeignKey("authentification.User",
                                      on_delete=models.CASCADE,
                                      related_name='flolowed_by',
                                      verbose_name=_("follower"))

    class Meta:
        verbose_name = "UserFollow"
        verbose_name_plural = "UserFollows"
        # ensures we don't get multiple UserFollows instances
        # for unique user-user_followed pairs
        unique_together = ('user', 'followed_user', )

    def __str__(self):
        return f"{self.user} - is following: {self.followed_user}"
