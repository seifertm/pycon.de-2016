#!/usr/bin/env python

import re
from jinja2 import Environment, FileSystemLoader

class Task:
    def __init__(self, segment):
        pass

class CodeBlock:
    def __init__(self, segment):
        self.segment = segment
    
    def __str__(self):
        return self.segment

class Example:
    def __init__(self, title, blocks):
        self.title = title
        self.blocks = blocks
    
    def is_code_block(self, block):
        return isinstance(block, CodeBlock)


env = Environment(loader=FileSystemLoader('templates'))
template = env.get_template('slides.html')

def split_test_suite(test_suite):
    return re.split('\n{3,}', test_suite)

def remove_comments(test_suite):
    without_block_comments = re.sub(r'""".+?"""', '', test_suite, flags=re.DOTALL)
    without_inline_comments = re.sub('#[^!].+', '', without_block_comments)
    return without_inline_comments

def parse_test_suite(file_path):
    with open(file_path) as test_file:
        test_content = test_file.read()
    test_content_without_comments = remove_comments(test_content)
    segments = split_test_suite(test_content_without_comments)
    stripped_segments = [segment.strip() for segment in segments if segment]
    
    blocks = []
    for segment in stripped_segments:
        if segment.startswith('#!'):
            blocks.append(Task(segment))
        else:
            blocks.append(CodeBlock(segment))
    return blocks

fib_example = Example(title='Write the implementation',
                      blocks=parse_test_suite('examples/fibonacci/test_fib.py'))
complex_example = Example(title='Write the test',
                          blocks=parse_test_suite('examples/complex/test_complex.py'))
fraction_example = Example(title='Putting it together',
                           blocks=parse_test_suite('examples/fraction/test_fraction.py'))

slides = template.render(fib=fib_example, complex=complex_example, fraction=fraction_example)
with open('slides.html', 'w') as output_file:
    output_file.write(slides)
