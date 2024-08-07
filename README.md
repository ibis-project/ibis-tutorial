# Ibis Tutorial SciPy 2024

Previous iterations of this tutorial have been given at:

- PyCon 2024 ([YouTube recording](https://youtu.be/1ND6COslBKU))
- PyData NYC 2023 ([YouTube recording](https://youtu.be/TyopbrmlZx8))
- EuroSciPy 2023 ([YouTube recording](https://youtu.be/tkejUD5Uq40))

## Join our Zulip!

The Ibis team uses Zulip to answer questions and chat!  You can join using this
invitation link:

https://ibis-project.zulipchat.com/join/3pri2odw4bt4764icmphtdv6/

## Codespace Setup

This tutorial is designed to be run via GitHub codespaces.

First, create a codespace in the repository:

![](https://github.com/ibis-project/ibis-tutorial/assets/3596999/46349375-948d-453c-b02b-c0f6b8d76b9d)

Then, click back to the repo tab, and then select `Open in JupyterLab`

![](https://github.com/ibis-project/ibis-tutorial/assets/3596999/ca5b926f-7794-4948-ade3-2a9be4edd69a)

## Local Setup

You can also run the tutorial locally!  To do so, you'll want to create a
virtual environment and then install the tutorial dependencies using one of the
tools below:

### Clone this repository

```sh
git clone https://github.com/ibis-project/ibis-tutorial.git
cd ibis-tutorial
```


### Install dependencies

We recommend using `pixi`, or `conda` / `mamba`, but `pip` works, too!

#### pixi

The first time you run this it should download all the required dependencies.

``` sh
pixi shell
```

#### conda / mamba

```sh
mamba env create -f environment.yml
```

#### pip

```sh
python -m pip install -r requirements.txt
```

