# Gaming Rules Discovery

This repository contains a hybrid **Python** and **Rust** stack for exploring the
rules of Horus Heresy 3.0 from user supplied images.

* `python_service/` – OCR, embeddings, and batch harvest utilities built with FastAPI.
* `rust_service/` – high speed parsing and validation of OCR output.
* `postgres/` – schema definitions for storing harvested data.

## Prerequisites

- [Rust](https://www.rust-lang.org/tools/install) and `cargo`
- Python 3.11 or newer
- `pip` for managing Python dependencies
- [Docker](https://docs.docker.com/get-docker/)
- [Docker Compose](https://docs.docker.com/compose/)
- `make`

## Setup

### Rust

Compile and run the Rust tests to verify the environment:

```bash
cargo test --manifest-path rust_service/Cargo.toml
```

### Python

Create a virtual environment and install Python dependencies:

```bash
python -m venv .venv
source .venv/bin/activate
pip install -r python_service/requirements.txt
```

## Sample Data

Place Heresy 3.0 sample images under `sample_data/images/`. This directory will
be used by the batch process that extracts and validates rules data from the
images. Only user-supplied HH3.0 images should be stored here.

## Building

Build the Docker images for the Python, Rust, and PostgreSQL services:

```bash
make build
```

## Running

Start all services in the background:

```bash
make up
```

Harvest a directory of sample images (defaults to `sample_data/images`):

```bash
make harvest DIR=sample_data/images
```

This generates `harvest_results.json` and `harvest_report.html` under the project root.

Shut everything down when finished:

```bash
make down
```

## Testing

Run the test suites for both languages:

```bash
make test
```

## Continuous Integration

GitHub Actions builds the Docker images and runs the full test suite on each
push or pull request. See `.github/workflows/ci.yml` for details.
