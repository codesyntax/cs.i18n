from Products.Five.browser.pagetemplatefile import ZopeTwoPageTemplateFile
from plone.app.i18n.locales.browser.selector import LanguageSelector as LSBase

class LanguageSelector(LSBase):
    render = ZopeTwoPageTemplateFile('templates/languageselector.pt')


    def languages(self):
        """ Returns list of languages """

        if self.tool is None:
            return []

        bound = self.tool.getLanguageBindings()
        current = bound[0]

        supported = self.tool.getSupportedLanguages()

        lang_info = self.tool.getAvailableLanguageInformation()
        languages = []
        for lang in supported:
            data = {}
            data['code'] = lang
            if lang == current:
                data['selected'] = True
            else:
                data['selected'] = False
            data['flag'] = lang_info.get(lang).get(u'flag', None)
            data['name'] = lang_info.get(lang).get(u'name', None)
            data['native'] = lang_info.get(lang).get(u'native', None)
            
            languages.append(data)

        return languages
