# Exercism Solutions

A collection of my solutions for [Exercism](https://exercism.org) coding challenges across multiple programming languages.

## Usage

### Initial Setup

Configure the Exercism CLI:

```bash
exercism configure --token=$EXERCISM_TOKEN --workspace /Users/$USER/MEGA/projects/exercism
```

### Download an Exercise

```bash
# Format: exercism download --exercise=<exercise-name> --track=<language>
exercism download --exercise=hello-world --track=python
```

## Tracks

### Python

The Python track uses `uv` for dependency management and `ruff` for linting.

```bash
# Run tests for a specific exercise
make test TEST=python/hello-world

# Run all Python tests
make test

# Lint and format Python code
make lint
```

### Go

Navigate to the exercise directory and use standard Go commands:

```bash
cd go/hello-world
go test
```

### Elixir

Navigate to the exercise directory and use Mix:

```bash
cd elixir/hello-world
elixir hello_world_test.exs
```

## Available Commands

The project includes a `Makefile` with helpful commands:

| Command | Description |
|---------|-------------|
| `make help` | Show all available commands |
| `make lint` | Format and fix Python code using ruff |
| `make test` | Run all Python tests |
| `make test TEST=path/to/exercise` | Run tests for a specific Python exercise |

## Project Structure

```
exercism/
├── python/          # Python track exercises
│   ├── hello-world/
│   ├── leap/
│   └── ...
├── go/             # Go track exercises
│   ├── hello-world/
│   └── ...
├── elixir/         # Elixir track exercises
│   ├── hello-world/
│   └── ...
├── Makefile        # Automation commands
└── README.md       # You are here!
```

## How to use

1. **Download** an exercise using the Exercism CLI
2. **Navigate** to the exercise directory
3. **Implement** your solution
4. **Test** your implementation
5. **Submit** your solution: `exercism submit path/to/solution.file`
