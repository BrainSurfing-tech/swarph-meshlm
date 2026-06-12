# swarph-meshlm

**Join a multi-LLM mesh from inside [Simon Willison's `llm`](https://llm.datasette.io).** A plugin that exposes [`swarph-mesh`](https://github.com/BrainSurfing-tech/swarph-mesh) primitives as `llm` commands — so if you already live in `llm`, you can talk to a mesh of agents (Claude, GPT, Gemini, and peers) without installing a separate binary.

```bash
llm install swarph-meshlm
llm swarph-ask alice "summarize the open PRs and reply when done"
```

This is one of three repos in the v0.3.x architecture:

| Repo | Role |
|---|---|
| [`swarph-mesh`](https://github.com/BrainSurfing-tech/swarph-mesh) | Substrate Python package — Protocol + adapters + SwarphCall + MeshClient |
| [`swarph-cli`](https://github.com/BrainSurfing-tech/swarph-cli) | The `swarph` standalone binary |
| [`swarph-meshlm`](https://github.com/BrainSurfing-tech/swarph-meshlm) | This repo — `llm` plugin (same primitives via Simon's plugin host) |

## Status

**v0.0.1 — SCAFFOLD.** Plugin registration only via `[project.entry-points.llm]`. The live `llm.hookimpl` `register_commands` / `register_models` implementations land as the substrate matures.

## Why both `swarph-cli` AND `swarph-meshlm`?

Different distribution channels for the same primitives. Users already on Simon's `llm` get swarph-mesh participation by `llm install swarph-meshlm` — no second tool to learn. Users on a fresh box can `pip install swarph-cli` for a standalone binary. Both share the substrate, so a peer using `llm` and a peer using `swarph` see the same mesh state.

## Install (dev)

```bash
git clone https://github.com/BrainSurfing-tech/swarph-meshlm
cd swarph-meshlm
python -m venv venv && source venv/bin/activate
pip install -e ".[dev]"
pytest
llm plugins  # should list swarph-meshlm
```

## License

MIT. Pierre Samson + Claude Opus, 2026.
