# Gaming Rules Discovery

This repository combines **Rust** and **Python** components to explore ways of
discovering the hidden rules of games. Rust is intended for fast, type-safe core
logic, while Python offers a flexible environment for experimentation and data
analysis.

## Prerequisites

- [Rust](https://www.rust-lang.org/tools/install) and `cargo`
- Python 3.11 or newer
- `pip` for managing Python dependencies

## Setup

### Rust

Compile the Rust components (once added) with:

```bash
cargo build
```

### Python

Create a virtual environment and install Python dependencies:

```bash
python -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
```

## Sample Data

Place Heresy 3.0 sample images under `sample_data/images/`. This directory
will be used by a future AI-powered batch process that extracts and validates
rules data from the images. Only user-supplied HH3.0 images should be stored
here.

## Testing

Run the test suites for both languages:

```bash
cargo test
pytest
```

At present the repository only contains scaffolding. Add Rust crates under a
`rust/` directory and Python packages under a `python/` directory as the project
evolves.

