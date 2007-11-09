from setuptools import setup, find_packages

version = '0.1'

setup(name='cs.i18n',
      version=version,
      description="Some i18n customizations for Plone default language change forms",
      long_description="""\
We found ourselfs constantly change the way Plone and LinguaPlone show the language change forms. This product creates some basic customizations for these cases, using plain text language text links, based on the settings of a custom control-panel""",
      # Get more strings from http://www.python.org/pypi?%3Aaction=list_classifiers
      classifiers=[
        "Framework :: Plone",
        "Framework :: Zope2",
        "Framework :: Zope3",
        "Programming Language :: Python",
        "Topic :: Software Development :: Libraries :: Python Modules",
        ],
      keywords='plone i18n languagechange',
      author='Mikel Larreategi',
      author_email='mlarreategi@codesyntax.com',
      url='http://code.codesyntax.com/private/cs.i18n',
      license='BSD',
      packages=find_packages(exclude=['ez_setup']),
      namespace_packages=['cs'],
      include_package_data=True,
      zip_safe=False,
      install_requires=[
          'setuptools',
          # -*- Extra requirements: -*-
      ],
      entry_points="""
      # -*- Entry points: -*-
      """,
      )
