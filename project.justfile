## Add your own just recipes here. This is imported by the main justfile.

# Overriding recipes from the root justfile by adding a recipe with the same
# name in this file is not possible until a known issue in just is fixed,
# https://github.com/casey/just/issues/2540

# Fix Python reserved keyword 'class' generated as an attribute name due to alias.
# This is needed because gen-python emits 'class:' and 'self.class' verbatim
# when the slot alias is 'class', which is a Python keyword.
fix-python-keywords:
        sed -i \
                -e 's/\bclass: Optional\b/_class: Optional/g' \
                -e 's/self\.class\b/self._class/g' \
                -e 's/NIST_SP_800_171\.class\b/NIST_SP_800_171["class"]/g' \
                {{pymodel}}/{{schema_name}}.py

# Validate a representative catalog document with the catalog schema.
# https://github.com/usnistgov/oscal-content/tree/main/nist.gov/SP800-171/rev3
validate-oscal:
        uv run linkml validate \
                -s src/nist_sp_800_171/schema/nist_sp_800_171.yaml \
                tests/data/nist/NIST_SP800-171_rev3_catalog.yaml

