# Vividity as a Git Submodule

You can easily use Vividity as a [Git submodule](https://git-scm.com/book/en/v2/Git-Tools-Submodules).


<br>


## Setup

Add Vividity to your repo:

```console
git submodule add https://github.com/Sup2point0/vividity
```

If it hasn’t already, clone the submodule:

```console
git submodule update --init
```

Ensure [Python 3.12 or higher](https://www.python.org) is installed.


<br>


## Usage

If your project has this structure:

```
./
   vividity/
      export/
         ...
      ...
   ...
   README.md
```

To export colour palettes, use Python to run `export`. You can export to CSS, SCSS, JS, or any combination of the 3.

```console
python vividity/export css
```

```console
python vividity/export scss js
```
