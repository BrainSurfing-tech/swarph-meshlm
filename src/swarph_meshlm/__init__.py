"""swarph-meshlm — Simon Willison ``llm`` plugin exposing swarph-mesh primitives.

The ``llm`` plugin host (see https://llm.datasette.io/en/stable/plugins/index.html)
is a mature plugin architecture — installing this package registers
``swarph-meshlm`` as an ``llm`` plugin and exposes ``llm swarph-ask
<peer>``-style commands without a separate binary.

Architecture per PLAN.md §11 (bonus path) — same ``MeshClient`` +
``SwarphCall`` substrate as ``swarph-cli``, just wired through ``llm``'s
plugin host instead of a standalone argparse layer. Three-repo
v0.3.x split:

* ``swarph-mesh`` (substrate)   — Protocol + adapters + MeshClient
* ``swarph-cli`` (binary)       — the ``swarph`` CLI
* ``swarph-meshlm`` (this)      — ``llm`` plugin

v0.0.1 ships only the plugin registration stub. Live ``llm.hookimpl``
``register_commands`` / ``register_models`` implementations land in
Phase 7 of PLAN.md once the substrate is mature.
"""

from __future__ import annotations

__version__ = "0.0.1"

# llm.hookimpl decorator is registered at import time when llm is
# present. We intentionally don't import llm at module load to keep
# the package importable in test environments without the full
# llm host installed (see test fixtures).

__all__ = ["__version__"]
