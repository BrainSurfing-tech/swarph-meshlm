# swarph-meshlm

Simon Willison `llm` plugin exposing swarph-mesh primitives. Installs as an `llm` plugin so existing `llm` users get swarph-mesh participation without a separate binary.

```bash
llm install swarph-meshlm
llm swarph-ask droplet "what's the current OMEGA regime?"
```

This is one of three repos in the v0.3.x architecture:

| Repo | Role |
|---|---|
| [`swarph-mesh`](https://github.com/darw007d/swarph-mesh) | Substrate Python package — Protocol + adapters + SwarphCall + MeshClient |
| [`swarph-cli`](https://github.com/darw007d/swarph-cli) | The `swarph` standalone binary |
| [`swarph-meshlm`](https://github.com/darw007d/swarph-meshlm) | This repo — `llm` plugin (same primitives via Simon's plugin host) |

## Status

**v0.0.1 — SCAFFOLD.** Plugin registration only via `[project.entry-points.llm]`. Live `llm.hookimpl` `register_commands` / `register_models` implementations ship in Phase 7 of PLAN.md once the substrate is mature.

## Spec

→ [hedge-fund-mcp / research/swarph_cli/PLAN.md §11](https://github.com/darw007d/hedge-fund-mcp/blob/main/research/swarph_cli/PLAN.md) (bonus path — `llm` plugin)

## Why both `swarph-cli` AND `swarph-meshlm`?

Different distribution channels for the same primitives. Users already on Simon's `llm` get swarph-mesh participation by `llm install swarph-meshlm` — no second tool to learn. Users on a fresh box can `pip install swarph-cli` for a standalone binary. Both share the substrate, so a peer using `llm` and a peer using `swarph` see the same mesh state.

## Install (dev)

```bash
git clone https://github.com/darw007d/swarph-meshlm
cd swarph-meshlm
python -m venv venv && source venv/bin/activate
pip install -e ".[dev]"
pytest
llm plugins  # should list swarph-meshlm
```

## License

MIT. Pierre Samson + Claude Opus, 2026.
