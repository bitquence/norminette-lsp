# norminette for 42 schools

> (bitquence) LSP note: you are free to use this, but do keep in mind that it
> was quickly hacked together by a soon-to-be student for his own purposes, and
> that issues and small kinks may pop up.
> I don't intend on opening a PR on the main repo as this feature is quite
> niche and may interest only a few students.

## Install

Requires python3.8+ (3.8, 3.9, 3.10, 3.11)

### Directly inside your global commands

Install using pip.
```shell
python3 -m pip install --upgrade pip setuptools
python3 -m pip install norminette
```

To upgrade an existing install, use
```shell
python3 -m pip install --upgrade norminette
```

## Usage

- Runs on the current folder and any subfolder:

```
norminette
```

- Runs on the given filename(s):

```
norminette filename.[c/h]
```

- Prevents stopping on various blocking errors:

```
norminette -d
```

- Outputs all the debug logging:

```
norminette -dd
```

## LSP Server Usage

Use the following code snippets to receive real-time warnings and norm errors
from `norminette` from within your text editor.

Keep in mind that the LSP server will only report diagnostics for files
containing a valid 42 header.

### Neovim (built-in LSP client)

```
vim.lsp.start({
    name = 'norminette',
    cmd = { 'norminette', '--lsp-server' },
    filetypes = { "c", "h" },
})
```

## Docker usage

```
docker build -t norminette .
cd ~/42/ft_printf
docker run -v $PWD:/code norminette /code
```

If you encounter an error or an incorrect output, you can:
 - Open an issue on github 
 - Post a message on the dedicated slack channel (#norminette-v3-beta)
    

Please try to include as much information as possible (the file on which it crashed, etc)

Feel free to do pull requests if you want to help as well. Make sure that run_test.sh properly runs after your modifications.

## Run for development

This new version uses poetry as a dependency manager.

If you want to contribute:

```shell
poetry install

# Run dev norminette
poetry run norminette

# Or... with virtual env
source .venv/bin/activate
norminette

# Run tests
poetry run pytest
```
