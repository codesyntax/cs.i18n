from Products.Five.browser.pagetemplatefile import ZopeTwoPageTemplateFile
from plone.app.i18n.locales.browser.selector import LanguageSelector as LSBase

class LanguageSelector(LSBase):
    render = ZopeTwoPageTemplateFile('templates/languageselector.pt')
