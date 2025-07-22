# Hop3: A `pluggy`-based Plugin Architecture Demo

This repository contains a simple, illustrative example of a Python application (`hop3-host`) that uses a plugin (`hop3-plugin`) to extend its functionality. The core of this demonstration is the `pluggy` library, which is the same framework used by the popular testing tool `pytest`.

**Disclaimer:** This code is for educational purposes only. It is a simplified demonstration and is not intended for production use. The primary goal is to showcase the mechanics of plugin discovery and integration.

## Project Structure

The repository is organized as a workspace with two main packages:

*   `hop3-host`: A host application that defines extension points (hooks) for building and deploying applications. It knows nothing about the specifics of *how* to build or deploy; it only defines the interfaces (`protocols`).
*   `hop3-plugin`: An external plugin that provides concrete implementations (strategies) for building and deploying. In this example, it provides a Docker-based build strategy.

## Core Concepts Demonstrated

*   **Plugin Discovery:** The host application uses `pluggy` to discover and load plugins at runtime.
*   **Hook System:** The host defines "hook specifications" (`hookspecs`) that plugins can implement to provide new functionality.
*   **Separation of Concerns:** The host application is decoupled from the specific implementation details of its plugins. This allows for new build or deployment methods to be added without modifying the host's code.
*   **Protocols:** The use of `typing.Protocol` ensures that plugins adhere to the expected interface, providing a degree of static analysis and clarity.

## How to Run the Demo

This project uses `uv` for managing dependencies and the workspace.

### Setup

1.  **Install `uv`**: If you don't have it, install `uv` by following the official instructions.
2.  **Install Dependencies**: From the root of the project, install the packages in editable mode. This will also install `pluggy`.

    ```bash
    uv sync
    ```

### Running the Demo Script

The `hop3-host` package contains a small script, `demo.py`, to demonstrate the plugin system. It initializes the plugin manager and lists all registered plugins.

To run it:

```bash
python -m hop3_host.demo
```

The expected result is:

```
Registered plugins:
Total plugins: 1
- docker-plugin (builtins.type)```
```

### Plugin Discovery

To make the host application discover the plugin, an **entry point** has been added to the plugin's `pyproject.toml`.

The `hop3-plugin/pyproject.toml` file contains the following section:

```toml
[project.entry-points."hop3"]
smo = "hop3_plugin.plugin:DockerPlugin"
```

**Explanation:**

*   `[project.entry-points."hop3"]`: This tells Python's packaging system that this project provides plugins for the "hop3" entry point group.
*   `smo = "hop3_plugin.plugin:DockerPlugin"`: This registers the `SmoPlugin` class from the `hop3_plugin.plugin` module as a loadable plugin.
