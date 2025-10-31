import datetime as dt  # noqa: F401

from django.core.management.commands.shell import Command as BaseCommand
from django.db.models import __all__ as models_all


class Command(BaseCommand):
    def get_auto_imports(self):
        return super().get_auto_imports() + [
            "django.conf.settings",
            *[f"django.db.models.{name}" for name in models_all],
            "django.urls.reverse",
            "django.urls.resolve",
            "rich.inspect",
            "rich.print",
            "rich.print_json",
            "decimal.Decimal",
            f"{__name__}.dt",
        ]
