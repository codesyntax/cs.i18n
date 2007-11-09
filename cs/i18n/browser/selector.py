
from plone.app.i18n.locales.languageselector import LanguageSelector as LSBase

class LanguageSelector(LSBase):
    render = ZopeTwoPageTemplateFile('templates/languageselector.pt')
