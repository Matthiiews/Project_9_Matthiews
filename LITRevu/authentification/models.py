from django.contrib.auth.models import AbstractUser
from django.db import models
from django.utils.translation import gettext_lazy as _


class User(AbstractUser):
    """Create USer instance"""


class UserFollows(models.Model):
    """Follow and followed by model"""

    user = models.ForeignKey("authentification.User",
                             on_delete=models.CASCADE,
                             related_name='following',
                             verbose_name=_("user"))

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
