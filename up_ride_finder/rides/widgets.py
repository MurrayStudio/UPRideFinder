# -*- coding: utf-8 -*-
import json

from django.forms.utils import flatatt
from django.forms.widgets import DateTimeInput
from django.utils.safestring import mark_safe
from django.utils.html import conditional_escape
from django.utils.encoding import force_text


class DateTimePicker(DateTimeInput):
    """
    django-bootstrap3-datetimepicker from https://github.com/tutorcruncher/django-bootstrap3-datetimepicker
    includes unmerged (as of 3/28/2017) patch from cehdeti and minor changes by UP Ride Finder Team.

    Licensed under the Apache License, Version 2.0 (the "License");
    you may not use this file except in compliance with the License.
    You may obtain a copy of the License at

     http://www.apache.org/licenses/LICENSE-2.0

    Unless required by applicable law or agreed to in writing, software
    distributed under the License is distributed on an "AS IS" BASIS,
    WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
    See the License for the specific language governing permissions and
    limitations under the License.
    """
    # http://momentjs.com/docs/#/parsing/string-format/
    # http://docs.python.org/2/library/datetime.html#strftime-strptime-behavior
    format_map = (
        ('DDD', r'%j'),
        ('DD', r'%d'),
        ('MMMM', r'%B'),
        ('MMM', r'%b'),
        ('MM', r'%m'),
        ('YYYY', r'%Y'),
        ('YY', r'%y'),
        ('HH', r'%H'),
        ('hh', r'%I'),
        ('mm', r'%M'),
        ('ss', r'%S'),
        ('a', r'%p'),
        ('ZZ', r'%z'),
    )

    @classmethod
    def conv_datetime_format_py2js(cls, format):
        for js, py in cls.format_map:
            format = format.replace(py, js)
        return format

    @classmethod
    def conv_datetime_format_js2py(cls, format):
        for js, py in cls.format_map:
            format = format.replace(js, py)
        return format

    html_template = """
    <div%(div_attrs)s>
      <input%(input_attrs)s/>
      <span class="input-group-addon">
        <span%(icon_attrs)s></span>
      </span>
    </div>"""

    js_template = """
    <script>
        (function(window) {
            var callback = function() {
                $(function(){$("#%(picker_id)s:has(input:not([readonly],[disabled]))").datetimepicker(%(options)s);});
            };
            if(window.addEventListener)
                window.addEventListener("load", callback, false);
            else if (window.attachEvent)
                window.attachEvent("onload", callback);
            else window.onload = callback;
        })(window);
    </script>"""

    def __init__(self, attrs=None, format=None, options=None, div_attrs=None, icon_attrs=None):
        if not icon_attrs:
            icon_attrs = {'class': 'glyphicon glyphicon-calendar'}
        if not div_attrs:
            div_attrs = {'class': 'input-group date'}
        if format is None and options and options.get('format'):
            format = self.conv_datetime_format_js2py(options.get('format'))
        super(DateTimePicker, self).__init__(attrs, format)
        if 'class' not in self.attrs:
            self.attrs['class'] = 'form-control'
        self.div_attrs = div_attrs and div_attrs.copy() or {}
        self.icon_attrs = icon_attrs and icon_attrs.copy() or {}
        self.picker_id = self.div_attrs.get('id') or None
        if options is False:  # datetimepicker will not be initalized when options is False
            self.options = False
        else:
            self.options = options and options.copy() or {}
            if format and not self.options.get('format') and not self.attrs.get('date-format'):
                self.options[
                    'format'] = self.conv_datetime_format_py2js(format)

    def render(self, name, value, attrs=None):
        if value is None:
            value = ''
        input_attrs = self.build_attrs(attrs, type=self.input_type, name=name)
        if value != '':
            # Only add the 'value' attribute if a value is non-empty.
            input_attrs['value'] = force_text(self._format_value(value))
        input_attrs = {key: conditional_escape(
            val) for key, val in input_attrs.items()}
        if not self.picker_id:
            self.picker_id = (input_attrs.get('id', '') +
                              '_pickers').replace(' ', '_')
        self.div_attrs['id'] = self.picker_id
        picker_id = conditional_escape(self.picker_id)
        div_attrs = {key: conditional_escape(
            val) for key, val in self.div_attrs.items()}
        icon_attrs = {key: conditional_escape(
            val) for key, val in self.icon_attrs.items()}
        html = self.html_template % dict(div_attrs=flatatt(div_attrs),
                                         input_attrs=flatatt(input_attrs),
                                         icon_attrs=flatatt(icon_attrs))
        if self.options:
            js = self.js_template % dict(
                picker_id=picker_id, options=json.dumps(self.options or {}))
        else:
            js = ''
        return mark_safe(force_text(html + js))
