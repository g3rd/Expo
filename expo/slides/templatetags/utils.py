from __future__ import unicode_literals
from django.template import Library, Node, TemplateSyntaxError
from django.conf import settings
from django.template.loader import select_template
from django.template.base import token_kwargs, compile_string


register = Library()


@register.tag
def multi_include(parser, token):
    bits = token.split_contents()
    if len(bits) < 2:
        raise TemplateSyntaxError(
            "%r tag takes at least one argument: the name of the template to be included." % bits[0])

    template_expressions, extra_index = _template_expressions(bits)

    template_expressions = [compile_quote_string(path) for path in template_expressions]

    options = {}
    remaining_bits = bits[extra_index:]
    while remaining_bits:
        option = remaining_bits.pop(0)
        if option in options:
            raise TemplateSyntaxError('The %r option was specified more '
                                      'than once.' % option)
        if option == 'with':
            value = token_kwargs(remaining_bits, parser, support_legacy=False)
            if not value:
                raise TemplateSyntaxError('"with" in %r tag needs at least '
                                          'one keyword argument.' % bits[0])
        elif option == 'only':
            value = True
        else:
            raise TemplateSyntaxError('Unknown argument for %r tag: %r.' %
                                      (bits[0], option))
        options[option] = value
    isolated_context = options.get('only', False)
    namemap = options.get('with', {})
    return MultiIncludeNode(template_expressions, extra_context=namemap,
                            isolated_context=isolated_context)


class MultiIncludeNode(Node):
    def __init__(self, template_name_list, *args, **kwargs):
        self.template_name_list = template_name_list
        self.extra_context = kwargs.pop('extra_context', {})
        self.isolated_context = kwargs.pop('isolated_context', False)
        super(MultiIncludeNode, self).__init__(*args, **kwargs)

    def render_template(self, template, context):
        values = dict([(name, var.resolve(context)) for name, var
                       in self.extra_context.iteritems()])
        if self.isolated_context:
            return template.render(context.new(values))
        context.update(values)
        output = template.render(context)
        context.pop()
        return output

    def render(self, context):
        try:
            template_names = [exp.render(context) for exp in self.template_name_list]
            template = select_template(template_names)
            return self.render_template(template, context)
        except:
            if settings.TEMPLATE_DEBUG:
                raise
            return ''


def _template_expressions(bits):
    extra_index = len(bits)
    keyword_indexes = []
    for keyword in ['with', 'only']:
        try:
            keyword_indexes.append(bits.index(keyword))
        except ValueError:
            pass
    if keyword_indexes:
        extra_index = min(keyword_indexes)
    return bits[1:extra_index], extra_index


def compile_quote_string(path):
    if path[0] in ('"', "'") and path[-1] == path[0]:
        return compile_string(path[1:-1], "")
    else:
        raise TemplateSyntaxError('String must contain quotes')
