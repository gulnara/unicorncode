import sys
from unicorn_tokenizer import *
import unicorn_tokenizer
from cStringIO import StringIO


def parse(value):
	old_stdout = sys.stdout
	sys.stdout = mystdout = StringIO()
	unicorn_tokenize(value)
	try:
		tree = parsing()
	except:
		print unicorn_tokenizer.tokens
		raise

	tree.eval()
	sys.stdout = old_stdout
	return mystdout.getvalue()