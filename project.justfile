## Add your own just recipes here. This is imported by the main justfile.

# Overriding recipes from the root justfile by adding a recipe with the same
# name in this file is not possible until a known issue in just is fixed,
# https://github.com/casey/just/issues/2540

# ============ Knowledge bundle: the adapted domain schema ============

# `.lokf/nist-sp-800-171.yaml` is the copy `lokf adapt` writes from the schema
# so that it can sit beside `.lokf/lokf.yaml` (`lokf adapt --help` lists the
# moves). The roots are the classes a knowledge concept may use as its
# `type`: the family, the security requirement and the organization-defined
# parameter, the three elements that SP 800-171 gives an identifier and that
# other documents, such as a system security plan or an assessment, cite. A
# statement item, an assessment objective, an assessment method and a
# reference belong to one requirement, so they stay inlined in it, and
# Sp800171Publication is the document that holds them all. The recipes run
# the `lokf` the sidecar's floor pins (0.9.0 or later); LOKF_CMD runs
# another, such as a checkout:
# LOKF_CMD="uv run --project ../lokf lokf" just lokf-adapt
lokf_cmd := env_var_or_default("LOKF_CMD", "uv run --project .lokf lokf")
lokf_adapt_roots := "--root Sp800171Family --root Sp800171Requirement --root Sp800171Parameter"

# Rewrite .lokf/nist-sp-800-171.yaml from the schema (run after every schema change)
[group('knowledge bundle')]
lokf-adapt:
  {{lokf_cmd}} adapt {{source_schema_path}} {{lokf_adapt_roots}} --lokf .lokf/lokf.yaml -o .lokf/nist-sp-800-171.yaml

# Fail when .lokf/nist-sp-800-171.yaml is stale against the schema or .lokf/lokf.yaml
[group('knowledge bundle')]
lokf-adapt-check:
  {{lokf_cmd}} adapt {{source_schema_path}} {{lokf_adapt_roots}} --lokf .lokf/lokf.yaml -o .lokf/nist-sp-800-171.yaml --check
