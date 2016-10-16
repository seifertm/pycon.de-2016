#!/usr/bin/env python

from jinja2 import Environment, FileSystemLoader

env = Environment(loader=FileSystemLoader('templates'))
template = env.get_template('slides.html')

slides = template.render()
with open('slides.html', 'w') as output_file:
    output_file.write(slides)
