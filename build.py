#!/usr/bin/env python

from jinja2 import Environment, FileSystemLoader

env = Environment(loader=FileSystemLoader('templates'))
template = env.get_template('slides.html')

def split_test_case(test_case):
    return test_case.split('\n\n\n')

def parse_test_suite(file_path):
    with open(file_path) as test_file:
        test_content = test_file.read()
    test_blocks = split_test_case(test_content)
    return test_blocks

fib_test_blocks = parse_test_suite('examples/fibonacci/test_fib.py')
complex_test_blocks = parse_test_suite('examples/complex/test_complex.py')

slides = template.render(fib=fib_test_blocks, complex=complex_test_blocks)
with open('slides.html', 'w') as output_file:
    output_file.write(slides)
