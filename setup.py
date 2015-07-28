
from setuptools import setup, find_packages


REQUIREMENTS = [
    'Django>=1.7.8,<1.8',
    'pytz>=2011n',
    'django-hitcounter>=0.1.1',
    'django-tastypie>=0.12.1',
    'django-revproxy>=0.9.3',
    'django-haystack>=2.2',
    'Whoosh>=2.7.0',

    # Diazo
    'diazo>=1.0.5',

    # Celery
    'django-celery==3.1.16',

    ### Move out of colab (as plugins):

    # Deps for super_archives
    'etiquetando==0.1',
    'django-taggit>=0.12.1',
    'html2text>=3.200.3',
    'chardet>=1.0.1',

    # Deps for gitlab plugin
    'python-dateutil>=1.5',
    'requests',
]

TEST_REQUIREMENTS = [
    'coverage>=3.7.1',
    'coveralls>=0.5',
    'flake8>=2.3.0',
    'mock>=1.0.1',
]


EXCLUDE_FROM_PACKAGES = []


setup(
    name='colab',
    version='1.10.1',
    url='https://github.com/colab-community/colab',
    author='Sergio Oliveira',
    author_email='sergio@tracy.com.br',
    description='Collaboration platform for communities',
    license='LICENSE.txt',
    packages=find_packages(exclude=EXCLUDE_FROM_PACKAGES),
    include_package_data=True,
    entry_points={'console_scripts': [
        'colab-admin = colab.management:execute_from_command_line',
        'colab-init-config = colab.management:initconfig',
    ]},
    zip_safe=False,
    long_description=open('README.rst').read(),
    install_requires=REQUIREMENTS,
    tests_require=TEST_REQUIREMENTS,
    test_suite="tests.run.run_with_coverage",
    classifiers=[
        'Development Status :: 3 - Alpha',
        'Environment :: Web Environment',
        'Framework :: Django',
        'Intended Audience :: Developers',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Programming Language :: Python :: 2',
        'Programming Language :: Python :: 2.7',
        'Topic :: Internet :: WWW/HTTP',
        'Topic :: Internet :: WWW/HTTP :: Dynamic Content',
        'Topic :: Internet :: WWW/HTTP :: WSGI',
    ],
)
