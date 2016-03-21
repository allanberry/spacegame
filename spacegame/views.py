from django.views.generic.base import TemplateView

class ViewMixin(object):
    '''
    Mixin for shared functionality across views.
    '''
 
    def nav_relative(self, *args, **kwargs):
        '''
        A data structure to allow local wayfinding
        This defines the structure.  Meant to be heavily amended in subclass.
        '''
        return [
            {'name': 'Home',
             'url': reverse_lazy('home')},
        ]

    def page_title(self):
        return 'Spacegame'

    def window_title(self):
        return self.page_title()


class HomeView(ViewMixin, TemplateView):
    '''
    The main home page.
    '''
    template_name = "spacegame/home.html"
    def window_title(self):
        return 'Home'

    def page_title(self):
        return 'Welcome to Spacegame'


class GameView(ViewMixin, TemplateView):
    '''
    The game page.
    '''
    template_name = "spacegame/game.html"
    def window_title(self):
        return 'Game On'