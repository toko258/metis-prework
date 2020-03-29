# Environment management

We will be using Anaconda environments to manage the python packages that are
needed for our curriculum. You can think of an environment as a container for
the packages that you need to run code.

Environments can be useful when you have several different projects, each with
different software requirements. Environments let you separately the packages
used for each package and preserve them so that the project code will continue
to work in the future.

Today, we'll start by building our very first conda environment. Metis has a
list of the software needed to run all the code in our curriculum. We keep track
of this in the cloud, allowing you to easily get up and running.

## Setup

### Conda

First, you need to have anaconda installed in order for this to work. Check that
`conda` is installed by running `conda -V` from your terminal. You should
receive a response indicating your current `conda` version.

If you haven't already, install the appropriate miniconda for your system from
the link [here](https://docs.conda.io/en/latest/miniconda.html). **Be sure to
select the python 3.\* version**.

### Metis Environment

Now we'll run the code to install the metis environment.

First, let's check if `conda` needs to be updated:

```bash
conda update conda -y
```

Next, we need to install `anaconda-client` in order to load cloud environmentts.

```bash
conda install anaconda-client -y
```

Finally, install the Metis environment:

```bash
conda env create thisismetis/metis
```

The `nb_conda` package will automatically connect your conda environment to
jupytyer.

# How to use the Metis environment

When you open a new terminal, you should see a prompt similar to:

```bash
(base)$
```

This indicates that you are currently in the "base" environment. You can confirm
this with `conda info`.

## Switch to the Metis environment

**Before you can run Jupyter, you need to switch to the Metis environment.** You
can do this by running

```bash
(base)$ conda activate metis
(metis)$
```

You can then start Jupyter by running

```bash
(metis)$ jupyter notebook
```

When starting a new notebook in Jupyter, students should select "Kernel ->
Change Kernel -> metis" before running.
