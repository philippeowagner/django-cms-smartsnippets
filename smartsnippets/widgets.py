from django.template.loader import render_to_string
from django.template import RequestContext
from smartsnippets.widgets_pool import widget_pool
from smartsnippets.widgets_base import SmartSnippetWidgetBase
from models import DropDownVariable

class TextField(SmartSnippetWidgetBase):
    name = 'Text Field'
    
    def render(self, request):
        context_instance = RequestContext(request)
        return render_to_string('smartsnippets/widgets/textfield/widget.html',
                                    {'field': self.variable},
                                    context_instance=context_instance)


class TextAreaField(SmartSnippetWidgetBase):
    name = 'TextArea Field'
    
    def render(self, request):
        context_instance = RequestContext(request)
        return render_to_string('smartsnippets/widgets/textareafield/widget.html',
                                    {'field': self.variable},
                                    context_instance=context_instance)


class DropDownField(SmartSnippetWidgetBase):
    name = 'DropDown Field'
    model = DropDownVariable
    
    def render(self, request):
        context_instance = RequestContext(request)
        return render_to_string('smartsnippets/widgets/dropdownfield/widget.html',
                                {'field': self.variable},
                                    context_instance=context_instance)

widget_pool.register_widget(TextField)
widget_pool.register_widget(TextAreaField)
widget_pool.register_widget(DropDownField)