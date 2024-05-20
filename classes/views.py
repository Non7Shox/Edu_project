from django.views.generic import TemplateView


class ClassesListView(TemplateView):
    template_name = 'classes/classes-list.html'
