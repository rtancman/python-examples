# python-examples
Test Python features &amp; examples

# How to run

This project uses the [asdf](https://asdf-vm.com/) to manager Python and Poetry versions. You need to instal asdf first. Follow the instructions [here](https://asdf-vm.com/guide/getting-started.html#_1-install-dependencies) to install asdf.

1. Install the Python version:

```
asdf install python 3.12.5
```

2. Install the Poetry version:

Now we need to install the [asdf Poetry plugin](https://github.com/asdf-community/asdf-poetry). See bellow:

```bash
asdf plugin-add poetry https://github.com/asdf-community/asdf-poetry.git
asdf install poetry 1.8.3
```

3. Check the correct versions:

```bash
python -V
poetry -V
```