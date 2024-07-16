import os
import pathlib
import pytest
import re

def test_exists_graph_py():
    assert pathlib.Path('./graph.py').is_file()

@pytest.fixture(scope='session')
def graph_py_content():
    with open('./graph.py') as f:
        content = f.read()
    return content

def test_graph_py_has_plot(graph_py_content):
    assert re.search(r'\.plot(.*)', graph_py_content)

def test_graph_py_has_getfigure(graph_py_content):
    assert re.search(r'\.get_figure(.*)', graph_py_content)

def test_graph_py_has_savefig(graph_py_content):
    assert re.search(r'\.savefig(.*)', graph_py_content)

def test_graph_py_use_of_extra(graph_py_content):    
    assert re.search('title', graph_py_content)    
    assert re.search('label', graph_py_content)

def test_graph_py_exec_no_argument():
    result = os.popen('python3 graph.py').read()
    assert re.search('error', result, re.IGNORECASE)

def test_graph_py_exec_bad_symbol():
    result = os.popen('python3 graph.py LOKOL').read()
    assert re.search('error', result, re.IGNORECASE)


@pytest.fixture(scope='session')
def graph_py_result():
    result = os.popen('python3 graph.py CASH.to').read()
    yield result
    os.popen('rm CASH.to.png')

def test_graph_py_exec_valid_symbol(graph_py_result):
    assert len(graph_py_result) == 0, "Output unncessary when symbol is valid"

def test_graph_py_exec_image_created():
    assert pathlib.Path('./CASH.to.png').is_file()
