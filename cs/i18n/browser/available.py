from Acquisition import aq_inner
from Products.Five.browser import BrowserView

from Products.CMFCore.utils import getToolByName


class NotAvailableLanguage(BrowserView):
    def get_translation_items(self):
        context = aq_inner(self.context)
        lang = context.Language()
        uid_cat = getToolByName(context, 'uid_catalog')
        uid = self.request.get('uid', None)
        if uid is not None:
            objects = uid_cat(UID=uid)
            if objects:
                obj = objects[0].getObject()
                return [v for k,v in obj.getTranslations(review_state=False).items() if k != lang]

        return []

    def language_name(self, lang):
        context = aq_inner(self.context)
        portal_languages = getToolByName(context, 'portal_languages')
        info = portal_languages.getAvailableLanguageInformation().get(lang, None)
        if info is not None:
            return info.get('native', u'')

        return ''
    
