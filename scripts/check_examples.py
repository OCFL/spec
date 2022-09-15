"""Check validity of JSON examples in OCFL Markdown specification.

Intended to be used with Travis CI so has a zero exit code
on success, non-zero otherwise.
"""
import argparse
import json
from jsonschema import validate
from jsonschema.exceptions import ValidationError
import marko
import os.path
import re
import sys


def check_example(section, example_json):
    """Check example, return 1 for fail, 0 for OK."""
    # expand sha512 examples to match SYNTAX (not content!)
    example_json = re.sub(r'([\da-fA-F]{6})\.\.\.([\da-fA-F]{3})',
                          r'\1' + 'a' * 119 + r'\2',
                          example_json)
    try:
        example = json.loads(example_json)
    except Exception as e:  # wildly different exceptions in python 2 & 3
        print("%s -- JSON PARSING FAILED" % (section))
        if args.verbose:
            print(str(e))
        return 1
    try:
        validate(instance=example, schema=schema)
        print("Example in section %s -- OK" % (section))
    except ValidationError as e:
        print("Example in section %s -- JSON SCHEMA VALIDATION FAILED against %s" % (section, schema_file))
        if args.verbose:
            print(str(e))
        return 1
    return 0


parser = argparse.ArgumentParser(description="Check JSON in OCFL specification examples. Zero exit on success.",
                                 formatter_class=argparse.ArgumentDefaultsHelpFormatter)
parser.add_argument("-d", "--spec-dir", default="draft/spec",
                    help="Specification direct")
parser.add_argument("-v", "--verbose", action='store_true',
                    help="Be verbose, show output on success")
args = parser.parse_args()

schema_file = os.path.join(args.spec_dir, 'inventory_schema.json')
with open(schema_file, 'r') as fh:
    schema = json.load(fh)

md_file = os.path.join(args.spec_dir, 'index.md')
if not os.path.exists(md_file):
    print("No spec file " + md_file + ", nothing to do!")
    sys.exit(0)

with open(md_file, 'r') as fh:
    spec_md = fh.read()

errors = 0
spec = marko.parse(spec_md)
section = "unknown"
for element in spec.children:
    if type(element) == marko.block.Heading:
        section = element.children[0].children
    # FIXME: Structure of code block inside blockquotes doesn't
    # FIXME: seem the same as top level examples. Currently not
    # FIXME: validating json snippets in blockquotes
    # elif type(element) == marko.block.Quote:
    #    for sub_el in element.children:
    #        print(sub_el)
    #        if type(sub_el) == marko.block.FencedCode and element.lang == 'json':
    #            errors += check_example(section, rawtext.sub_el.children[0]children)
    elif type(element) == marko.block.FencedCode and element.lang == 'json':
        errors += check_example(section, element.children[0].children)

sys.exit(errors)
