# -*- coding:utf-8 -*-
from mako import runtime, filters, cache
UNDEFINED = runtime.UNDEFINED
STOP_RENDERING = runtime.STOP_RENDERING
__M_dict_builtin = dict
__M_locals_builtin = locals
_magic_number = 10
_modified_time = 1659808696.8066008
_enable_loop = True
_template_filename = 'themes/planetoid/templates/post.tmpl'
_template_uri = 'post.tmpl'
_source_encoding = 'utf-8'
_exports = []


def render_body(context,**pageargs):
    __M_caller = context.caller_stack._push_frame()
    try:
        __M_locals = __M_dict_builtin(pageargs=pageargs)
        post = context.get('post', UNDEFINED)
        __M_writer = context.writer()
        __M_writer('<html>\n<head>\n<meta http-equiv="Refresh" content="0;url=')
        __M_writer(str(post.meta('link')))
        __M_writer('">\n</head>\n<body>\nRedirecting you to <a href="')
        __M_writer(str(post.meta('link')))
        __M_writer('">the original location.</a>\n</body>\n</html>\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


"""
__M_BEGIN_METADATA
{"filename": "themes/planetoid/templates/post.tmpl", "uri": "post.tmpl", "source_encoding": "utf-8", "line_map": {"16": 0, "22": 2, "23": 4, "24": 4, "25": 7, "26": 7, "32": 26}}
__M_END_METADATA
"""
