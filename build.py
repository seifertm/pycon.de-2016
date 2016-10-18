#!/usr/bin/env python

import re
from jinja2 import Environment, FileSystemLoader

class Example:
    def __init__(self, code_blocks):
        self.code_blocks = code_blocks
    
    def __iter__(self):
        return iter(self.code_blocks)

env = Environment(loader=FileSystemLoader('templates'))
template = env.get_template('slides.html')

def split_test_suite(test_suite):
    return re.split('\n{3,}', test_suite)

def remove_comments(test_suite):
    without_block_comments = re.sub(r'""".+?"""', '', test_suite, flags=re.DOTALL)
    without_inline_comments = re.sub('#.+', '', without_block_comments)
    return without_inline_comments

def parse_test_suite(file_path):
    with open(file_path) as test_file:
        test_content = test_file.read()
    test_content_without_comments = remove_comments(test_content)
    test_blocks = split_test_suite(test_content_without_comments)
    stripped_test_blocks = [test_block.strip() for test_block in test_blocks if test_block]
    return Example(stripped_test_blocks)

fib_example = parse_test_suite('examples/fibonacci/test_fib.py')
complex_example = parse_test_suite('examples/complex/test_complex.py')
fraction_example = parse_test_suite('examples/fraction/test_fraction.py')

slides = template.render(fib=fib_example, complex=complex_example, fraction=fraction_example)
with open('slides.html', 'w') as output_file:
    output_file.write(slides)
