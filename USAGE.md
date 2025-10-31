# Quick Start Guide

## Testing the Template

To test this Copier template locally:

```bash
# Install copier if you haven't already
pip install copier
# or
pipx install copier

# Generate a test project
copier copy /home/raf/src/fluo/copier-project /tmp/test-project

# Navigate to the generated project
cd /tmp/test-project

# Initialize git (recommended)
git init
git add .
git commit -m "Initial commit from template"
```

## What Changed from Cookiecutter?

### 1. Configuration File
- **Before**: `cookiecutter.json`
- **After**: `copier.yml`

### 2. Template Syntax
- **Before**: `{{ cookiecutter.variable_name }}`
- **After**: `{{ variable_name }}`

### 3. Boolean Values
- **Before**: `'y'` and `'n'` strings
- **After**: `true` and `false` booleans

### 4. Template Directory
- **Before**: `{{cookiecutter.project_dir}}/`
- **After**: `template/` (with `_subdirectory` config)

### 5. Conditional Files
- **Before**: Filename like `{% if cookiecutter.license == 'MIT' -%} COPYING {%- endif %}`
- **After**: Filename like `COPYING.MIT.jinja` with `_exclude` patterns

### 6. Hooks
- **Before**: `hooks/pre_gen_project.py`, `hooks/post_gen_project.py`
- **After**: `scripts/post_gen_project.py` with `_tasks` in `copier.yml`

### 7. File Extensions
- Template files that should be rendered use `.jinja` extension
- Final output removes the `.jinja` extension

## Example Usage

### Minimal Generation
```bash
copier copy . ../my-new-project
```

### With Answers File
Create a `answers.yml`:

```yaml
project_title: My Amazing Project
project_description: A great Django application
author: Your Name
email: your.email@example.com
use_djangorestframework: true
project_type: web
license: MIT
```

Then use it:

```bash
copier copy --data-file answers.yml . ../my-new-project
```

### Update Existing Project

After making changes to the template:

```bash
cd /path/to/existing/project
copier update
```

Copier will:
1. Remember your previous answers
2. Show you what changed in the template
3. Ask if you want to apply updates
4. Preserve your customizations

## Testing Different Configurations

### Web Project with DRF
```bash
copier copy . /tmp/test-drf-project \
  --data project_title="DRF Test" \
  --data use_djangorestframework=true
```

### Django CMS Project
```bash
copier copy . /tmp/test-cms-project \
  --data project_title="CMS Test" \
  --data project_type=django-cms
```

### Different License
```bash
copier copy . /tmp/test-apache-project \
  --data project_title="Apache Test" \
  --data license=Apache-2.0
```

## Troubleshooting

### Issue: Jinja2 extension not found
If you get an error about `jinja2_time.TimeExtension`:

```bash
pip install jinja2-time
```

### Issue: UV not found
If the post-generation script fails because UV is not installed:

```bash
# Install UV
pip install uv
# or
curl -LsSf https://astral.sh/uv/install.sh | sh
```

### Issue: Template not rendering
Check that:
1. Files have `.jinja` extension if they should be templated
2. Variables in `copier.yml` match those used in templates
3. No `cookiecutter.` prefix remains in templates

## Validation

To validate your template works correctly:

1. Generate a test project
2. Check that conditional files are included/excluded correctly
3. Verify all variables are substituted
4. Try running the generated project:

```bash
cd test-project
uv sync  # or pip install -r requirements.txt
python manage.py migrate
python manage.py runserver
```

## Common Customizations

### Add a New Variable

1. Add to `copier.yml`:
```yaml
my_new_variable:
  type: str
  help: Description of the variable
  default: default_value
```

2. Use in templates:
```python
MY_SETTING = "{{ my_new_variable }}"
```

### Add a Conditional File

1. Create the file in `template/` with `.jinja` extension
2. Add exclusion rule in `copier.yml`:
```yaml
_exclude:
  - "{% if not include_my_feature %}template/my_feature.py.jinja{% endif %}"
```

### Modify Post-Generation Hook

Edit `scripts/post_gen_project.py` to add custom logic:

```python
def main():
    project = Project()
    
    # Your custom logic here
    print("Running custom setup...")
    
    # Existing logic
    uv_add(project)
    # ...
```

## Next Steps

1. ✅ Template converted successfully
2. 🧪 Test the template with different configurations
3. 📝 Update README.md with project-specific information
4. 🚀 Commit to version control
5. 🌐 (Optional) Push to GitHub for remote usage
6. 🔄 Set up CI/CD for template testing

## Support

For issues or questions about:
- **Copier**: https://copier.readthedocs.io/
- **This template**: Check the README.md or create an issue

