from django.utils.translation import gettext_lazy as _
import readenv

USE_I18N = True
# LOCALE_PATHS = []
USE_TZ = True
TIME_ZONE = readenv.str("TIME_ZONE", "Europe/Rome")

LANGUAGES = [
    ("it", _("Italian")),
    ("en", _("English")),
]
LANGUAGE_CODE = readenv.str("LANGUAGE_CODE", "en")

__all__ = [key for key in locals() if key.isupper()]
