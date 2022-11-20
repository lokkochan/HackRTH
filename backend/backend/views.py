import os
import json
import hashlib
import mimetypes
import posixpath
from pathlib import Path

import django.views.static
from django.http import Http404, HttpResponseNotModified
from django.utils._os import safe_join
from django.utils.http import http_date
from django.utils.translation import gettext
from django.http import FileResponse, JsonResponse, HttpResponseNotFound
from django.shortcuts import render

from .data import data, save_data


# Rewrite for json
def serve(request, path, document_root=None, show_indexes=False):
    """
    Serve static files below a given point in the directory structure.

    To use, put a URL pattern such as::

        from django.views.static import serve

        path('<path:path>', serve, {'document_root': '/path/to/my/files/'})

    in your URLconf. You must provide the ``document_root`` param. You may
    also set ``show_indexes`` to ``True`` if you'd like to serve a basic index
    of the directory.  This index view will use the template hardcoded below,
    but if you'd like to override it, you can create a template called
    ``static/directory_index.html``.
    """
    path = posixpath.normpath(path).lstrip('/')
    joined_path = safe_join(document_root, path)
    fullpath = Path(joined_path)
    if fullpath.is_dir():
        if show_indexes:
            return django.views.static.directory_index(path, fullpath)
        raise Http404(gettext("Directory indexes are not allowed here."))
    if not fullpath.exists():
        raise Http404(gettext('“%(path)s” does not exist') % {'path': fullpath})
    # Respect the If-Modified-Since header.
    statobj = fullpath.stat()
    if not django.views.static.was_modified_since(
            request.META.get('HTTP_IF_MODIFIED_SINCE'), statobj.st_mtime, statobj.st_size):
        return HttpResponseNotModified()
    content_type, encoding = mimetypes.guess_type(str(fullpath))
    content_type = content_type or 'application/octet-stream'
    response = FileResponse(fullpath.open('rb'), content_type=content_type)
    response.headers["Last-Modified"] = http_date(statobj.st_mtime)
    if encoding:
        response.headers["Content-Encoding"] = encoding
    return response


def return_html(html_path, js_names=None):
    return lambda request: render(request, html_path, **({'context': {'js': generate_js_elements(js_names)}} if js_names is not None else {}))


def generate_js_elements(js_dirs: (tuple, list)):
    return_ = ''
    for js_dir in js_dirs:
        h = hashlib.md5(open(f"static/js/{js_dir}.js", 'rb').read()).hexdigest()
        return_ += f'<script type="text/javascript" src="/static/js/{js_dir}.js?hash={h}"></script>'
    return return_


def submit(request):  # Use code
    global data
    code = str(request.GET['code'])
    if code in data['codes'].keys():
        points = data['codes'].pop(code)
        save_data(data)
        return JsonResponse({'success': 0, 'points': points})
    else:
        return JsonResponse({'success': 1, 'error': 'Code not found'})


def add_code(request):
    code = request.GET['code']
    points = request.GET['points']
    data['codes'][str(code)] =  points
    save_data(data)
    return JsonResponse({'success': 0})
