# Django Project Template (Copier)

This is a Django project template powered by [Copier](https://copier.readthedocs.io/). It has been converted from Cookiecutter to provide better update capabilities and modern templating features.

## Features

- 🚀 Modern Django project structure
- 📦 UV package management support
- 🎨 Optional Django CMS support
- 🔌 Optional Django REST Framework
- 🖼️ Optional sorl-thumbnail for image handling
- 🎭 Optional Vue.js integration
- 🗄️ PostgreSQL support
- 📝 Multiple license options (MIT, BSD-3, Apache-2.0, GPL-3.0)
- 🔧 Automated dependency installation with post-generation hooks

## Requirements

- Python 3.8+
- [Copier](https://github.com/copier-org/copier) (`pip install copier` or `pipx install copier`)
- [UV](https://github.com/astral-sh/uv) (recommended for dependency management)

## Usage

### Create a New Project

```bash
# Using copier directly
copier copy /path/to/this/template /path/to/destination

# Or from a git repository (if hosted)
copier copy https://github.com/yourusername/copier-project.git /path/to/destination
```

### Update an Existing Project

One of Copier's main advantages is easy template updates:

```bash
cd /path/to/your/project
copier update
```

## Template Variables

The template will prompt you for the following information:

- **project_name**: Your project title (e.g., "My New Project")
- **project_description**: Brief description of your project
- **project_slug**: Python package name (default: "web")
- **db_name**: Database name
- **db_user**: Database username
- **db_password**: Database password
- **admin**: Admin type (default: "default")
- **language_code**: Language code (default: "en-us")
- **timezone**: Timezone (default: "Europe/Rome")
- **author**: Your name
- **email**: Your email address
- **use_cookielaw**: Include cookie law compliance (yes/no)
- **use_djangorestframework**: Include Django REST Framework (yes/no)
- **use_sorl_thumbnail**: Include sorl-thumbnail (yes/no)
- **use_widget_tweaks**: Include django-widget-tweaks (yes/no)
- **use_vuejs**: Include Vue.js (yes/no)
- **use_postgresql**: Use PostgreSQL (yes/no)
- **project_type**: Choose between "web" or "django-cms"
- **license**: Choose license (MIT, BSD-3, Apache-2.0, GPL-3.0, Other)

## Project Structure

```
your-project/
├── template/                    # Template files
│   ├── {{ project_slug }}/      # Django app directory
│   ├── project/                 # Project settings
│   ├── _requirements/           # Requirements files
│   ├── manage.py
│   ├── pyproject.toml
│   └── COPYING.*                # License files (conditional)
├── scripts/                     # Generation scripts
│   └── post_gen_project.py      # Post-generation hook
├── copier.yml                   # Copier configuration
└── README.md                    # This file
```

## Post-Generation Steps

After generating your project, the template automatically:

1. Installs dependencies using UV from requirements files
2. Removes temporary `_requirements/` directory
3. Sets up the project structure

### Manual Steps

You may need to:

1. Create a virtual environment (if not using UV)
2. Run migrations: `python manage.py migrate`
3. Create a superuser: `python manage.py createsuperuser`
4. Collect static files: `python manage.py collectstatic`

## Differences from Cookiecutter Version

This Copier version provides several improvements:

1. **Easy Updates**: Update your project when the template changes
2. **Better Conditionals**: Cleaner handling of optional files
3. **Simplified Syntax**: No `cookiecutter.` prefix in templates
4. **Modern Features**: Better support for modern Python tooling
5. **Type-aware Questions**: Boolean questions use true/false instead of 'y'/'n'

## Converting from Cookiecutter

If you have an existing Cookiecutter-based project and want to use Copier for future updates:

1. Back up your project
2. Note your customizations
3. Generate a fresh project with Copier using the same configuration
4. Manually merge your customizations

## Development

### Template Structure

- `copier.yml`: Main configuration file defining all variables and behavior
- `template/`: Directory containing all template files
- `scripts/`: Python scripts run during generation
- `.jinja` extension: Files that should be rendered as templates

### Conditional Files

Files are conditionally included/excluded based on your choices:

- CMS settings: Only if `project_type == 'django-cms'`
- DRF settings: Only if `use_djangorestframework == true`
- License files: Only the selected license is included

### Updating the Template

1. Modify files in the `template/` directory
2. Update `copier.yml` for new variables
3. Test with: `copier copy . /tmp/test-project`

## License

This template is licensed under the MIT License. The generated projects will have the license you choose during generation.

## Credits

Converted from Cookiecutter template by Raffaele Salmaso.

## Resources

- [Copier Documentation](https://copier.readthedocs.io/)
- [Django Documentation](https://docs.djangoproject.com/)
- [UV Documentation](https://github.com/astral-sh/uv)

