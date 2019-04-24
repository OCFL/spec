"""Check validity of JSON examples in OCFL specification.

Intended to be used with Travis CI so has a zero exit code
on success, non-zero otherwise.
"""
import argparse
from bs4 import BeautifulSoup
import json
from json.decoder import JSONDecodeError
from jsonschema import validate
from jsonschema.exceptions import ValidationError
import os.path
import re
import sys

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

with open(os.path.join(args.spec_dir, 'index.html'), 'r') as fh:
    spec_html = fh.read()

spec = BeautifulSoup(spec_html, 'html.parser')

errors = 0
for id in ('example-minimal-inventory', 'example-versioned-inventory'):
    try:
        example_json = ''.join(spec.find(id=id).string)
        # expand sha512 examples to match SYNTAX (not content!)
        example_json = re.sub(r'([\da-fA-F]{6})\.\.\.([\da-fA-F]{3})',
                              r'\1' + 'a' * 119 + r'\2',
                              example_json)
        example = json.loads(example_json)
        validate(instance=example, schema=schema)
        print("%s -- OK" % (id))
    except JSONDecodeError as e:
        print("%s -- JSON PARSING FAILED" % (id))
        if args.verbose:
            print(str(e))
        errors += 1
    except ValidationError as e:
        print("%s -- JSON SCHEMA VALIDATION FAILED against %s" % (id, schema_file))
        if args.verbose:
            print(str(e))
        errors += 1

sys.exit(errors)
