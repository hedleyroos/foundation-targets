from setuptools import setup, find_packages

setup(
    name='foundationtargets',
    description='',
    version='',
    author='',
    license='BSD',
    url='',
    packages = find_packages(),
    dependency_links = [
    ],
    install_requires = [
#        'M2Crypto',    # disable since Fedora currently has problems building
        'simplejson',
        'django-ckeditor',
        'panya-contact',
        'django-tinymce',
        'django-preferences',
        'django-publisher',
        'django-recaptcha',
        'panya',
        'django-registration',
        'django-profile',
        'panya-social',
        'django-secretballot',
        'panya-post',
        'south',
    ],
)
