#!/usr/bin/env python

from jinja2 import Environment, FileSystemLoader

env = Environment(loader=FileSystemLoader('templates'))
template = env.get_template('slides.html')

with open('examples/fibonacci/test_fib.py') as test_fib_file:
    test_fib = test_fib_file.read()
    fib_test_blocks = test_fib.split('\n\n\n')

with open('examples/complex/test_complex.py') as test_complex_file:
    test_complex = test_complex_file.read()
    complex_test_blocks = test_complex.split('\n\n\n')

slides = template.render(fib=fib_test_blocks, complex=complex_test_blocks)
with open('slides.html', 'w') as output_file:
    output_file.write(slides)
