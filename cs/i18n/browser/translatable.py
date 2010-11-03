try:
    from Products.LinguaPlone.browser.selector import TranslatableLanguageSelector as LSBase
except ImportError:
    from plone.app.i18n.locales.browser.selector import LanguageSelector as LSBase

from Products.Five.browser.pagetemplatefile import ZopeTwoPageTemplateFile

from zope.i18n.interfaces import IUserPreferredLanguages
from zope.component import getMultiAdapter
from Acquisition import aq_inner
from ZTUtils import make_query

class TranslatableLanguageSelector(LSBase):
    render = ZopeTwoPageTemplateFile('templates/translatablelanguageselector.pt')

    def languages(self):
        context = aq_inner(self.context)
        results = LSBase.languages(self)
        supported_langs = [v['code'] for v in results]
        missing = set([str(c) for c in supported_langs])
        translations = self._translations(missing)

        # We want to preserve the current template / view as used for the
        # current object and also use it for the other languages
        append_path = self._findpath(context.getPhysicalPath(),
                                     self.request.get('PATH_INFO', ''))
        formvariables = self._formvariables(self.request.form)
        try:
            all_translations = context.getTranslations(review_state=False)
        except:
            return []
        
        not_translated = missing.difference(all_translations.keys())
        for item in results:
            if item['code'] in not_translated:            
                item['unavailable'] = True
        

        for data in results:
            code = str(data['code'])
            data['translated'] = code in translations

            try:
                appendtourl = '/'.join(append_path)
                if data.get('unavailable', False):
                    appendtourl += '/not_available'
                    formvariables['uid'] = context.UID()
                else:
                    try:
                        del formvariables['uid']
                    except KeyError:
                        pass
                    
                if self.set_language:
                    appendtourl += '?' + make_query(formvariables,
                                                    dict(set_language=code))
                elif formvariables:
                    appendtourl += '?' + make_query(formvariables)
            except UnicodeError:
                appendtourl = '/'.join(append_path)
                if self.set_language:
                    appendtourl += '?set_language=%s' % code

            if data['translated']:
                trans = translations[code]
                state = getMultiAdapter((trans, self.request),
                        name='plone_context_state')
                data['url'] = state.canonical_object_url() + appendtourl
            else:
                state = getMultiAdapter((context, self.request),
                        name='plone_context_state')
                try:
                    data['url'] = state.canonical_object_url() + appendtourl
                except AttributeError:
                    data['url'] = context.absolute_url() + appendtourl

        return results

