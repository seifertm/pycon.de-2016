#!/usr/bin/env python

import re
from jinja2 import Environment, FileSystemLoader

class Task:
    def __init__(self, segment):
        self.text = segment.strip('#!')
    
    def __str__(self):
        return self.text

class CodeBlock:
    def __init__(self, segment):
        self.segment = segment
    
    def __str__(self):
        return self.segment

class Example:
    def __init__(self, title, task, blocks):
        self.title = title
        self.task = task
        self.blocks = blocks
    
    def is_code_block(self, block):
        return isinstance(block, CodeBlock)


env = Environment(loader=FileSystemLoader('templates'), extensions=['jinja2.ext.with_'])
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

fib_example = Example(title='Write the implementation I',
                      task='Implement the Fibonacci sequence. Copy the test cases into your test suite, one by one, and watch the new test fail. Type the simplest implementation that makes the currenty test work without breaking previous tests.',
                      blocks=parse_test_suite('examples/fibonacci/test_fib.py'))
complex_example = Example(title='Write the implementation II',
                          task='Implement a representation for complex numbers. Just as in the previous example, copy each test into your test suite, one after another and make the test work in the easiest way possible. Do not forget to refactor before adding a new test to your test suite.',
                          blocks=parse_test_suite('examples/complex/test_complex.py'))
fraction_example = Example(title='Write the tests',
                           task='Implement a representation for fractions. This time, the bodies of the tests are not provided. You have to implement them yourself according to the specification provided by the test name.',
                           blocks=parse_test_suite('examples/fraction/test_fraction.py'))

slides = template.render(examples=[fib_example, complex_example, fraction_example])
with open('slides.html', 'w') as output_file:
    output_file.write(slides)
