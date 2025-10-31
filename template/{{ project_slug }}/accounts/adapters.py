from allauth.socialaccount.adapter import DefaultSocialAccountAdapter
from allauth.socialaccount.models import SocialLogin
from django import forms
from django.conf import settings
from django.core.exceptions import ValidationError
from django.http import HttpRequest

from .accounts.models import User


class SocialAccountAdapter(DefaultSocialAccountAdapter):
    def pre_social_login(self, request: HttpRequest, sociallogin: SocialLogin) -> None:
        """
        Invoked just after a user successfully authenticates via a
        social provider, but before the login is actually processed
        (and before the pre_social_login signal is emitted).
        """

        email = sociallogin.account.extra_data.get("email")

        if settings.ACCOUNTS_ALLOWED_USER_EMAILS == "__all__":
            allowed_domains = settings.ACCOUNTS_ALLOWED_DOMAINS
            if allowed_domains and email and not email.endswith(allowed_domains):
                raise ValidationError(
                    f"Email non autorizzata. Usa un indirizzo fra i seguenti: {', '.join(allowed_domains)}."
                )
        else:
            if email not in settings.ACCOUNTS_ALLOWED_USER_EMAILS:
                raise ValidationError("Utente non autorizzato.")

    def save_user(self, request: HttpRequest, sociallogin: SocialLogin, form: forms.Form | None = None) -> User:
        """
        Saves a newly signed up social login. In case of auto-signup,
        the signup form is not available.
        """

        user = super().save_user(request, sociallogin, form)

        user.is_superuser = True
        user.is_staff = True
        user.save()

        return user

    def populate_user(self, request: HttpRequest, sociallogin: SocialLogin, data) -> User:
        """
        Hook that can be used to further populate the user instance.
        """

        user = super().populate_user(request, sociallogin, data)
        user.username = data.get("email").split("@")[0]

        return user
