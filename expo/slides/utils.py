import os
from django.conf import settings

def load_from_file(module_path):
    """
    Load a python module from its absolute filesystem path
    Source: https://github.com/divio/django-cms/blob/develop/cms/utils/django_load.py
    """
    from imp import load_module, PY_SOURCE

    imported = None
    if module_path:
        with open(module_path, 'r') as openfile:
            imported = load_module("mod", openfile, module_path, ('imported', 'r', PY_SOURCE))
    return imported

def get_templates():
    templates = []
    if getattr(settings, 'SLIDES_TEMPLATES_DIR', False):
        tpldir = getattr(settings, 'SLIDES_TEMPLATES_DIR', False)
        # SLIDES_TEMPLATES_DIR can either be a string poiting to the templates directory
        # or a dictionary holding 'site: template dir' entries
        if isinstance(tpldir, dict):
            tpldir = tpldir[settings.SITE_ID]
        # We must extract the relative path of SLIDES_TEMPLATES_DIR to the neares
        # valid templates directory. Here we mimick what the filesystem and
        # app_directories template loaders do
        prefix = ''
        # Relative to TEMPLATE_DIRS for filesystem loader
        for basedir in settings.TEMPLATE_DIRS:
            if tpldir.find(basedir) == 0:
                prefix = tpldir.replace(basedir + os.sep, '')
                break
        # Relative to 'templates' directory that app_directory scans
        if not prefix:
            components = tpldir.split(os.sep)
            try:
                prefix = os.path.join(*components[components.index('templates') + 1:])
            except ValueError:
                # If templates is not found we use the directory name as prefix
                # and hope for the best
                prefix = os.path.basename(tpldir)
        config_path = os.path.join(tpldir, '__init__.py')
        # Try to load templates list and names from the template module
        # If module file is not present skip configuration and just dump the filenames as templates
        if os.path.isfile(config_path):
            template_module = load_from_file(config_path)
            templates = [(os.path.join(prefix, data[0].strip()), data[1]) for data in template_module.TEMPLATES.items()]
        else:
            templates = list((os.path.join(prefix, tpl), tpl) for tpl in os.listdir(tpldir))
    return templates
