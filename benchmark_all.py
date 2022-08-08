import importlib
import os
import subprocess as sp
import subprocess as sb
import sys

import click
import inquirer
import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns
from rich.console import Console
from rich.progress import track

PYTHON_EXECUTABLE = sys.executable
DIR = os.path.dirname(os.path.abspath(__file__))

# figure size in inches
sns.set(rc={"figure.figsize": (8, 6)})

console = Console()

approaches = [
    # "with_python",
    "with_numpy",
    # "with_cython",
    "with_pythran",
    "with_pythran_omp",
    "with_numba",
    "with_pybind11",
    # "with_dask",
    # "with_cupy",
]


@click.command()
@click.option("--skip-computation", is_flag=True, default=False)
def main(skip_computation: bool):
    if not skip_computation:
        for name in approaches:
            command = " ".join(
                [PYTHON_EXECUTABLE, os.path.join(DIR, "benchmark.py"), name]
            )
            console.print("[bright_yellow]$ {}".format(command))
            sb.run(command, shell=True)

    df = None
    for name in approaches:
        if df is None:
            df = pd.read_csv("data/{}.rows.csv".format(name))
        else:
            df = df.append(
                pd.read_csv("data/{}.rows.csv".format(name)), ignore_index=True
            )

    rel = sns.relplot(
        x="Number of Rows",
        y="Computational Time (sec)",
        hue="Approach",
        kind="line",
        data=df,
    )
    rel.fig.gca().set_title("Arc Length Computation of size N x 3")
    plt.savefig("data/rows.png", dpi=200, bbox_inches="tight")

    df = None
    for name in approaches:
        if df is None:
            df = pd.read_csv("data/{}.cols.csv".format(name))
        else:
            df = df.append(
                pd.read_csv("data/{}.cols.csv".format(name)), ignore_index=True
            )

    rel = sns.relplot(
        x="Number of Columns",
        y="Computational Time (sec)",
        hue="Approach",
        kind="line",
        data=df,
    )
    rel.fig.gca().set_title("Arc Length Computation of size 10000 x M")
    plt.savefig("data/cols.png", dpi=200, bbox_inches="tight")

    console.print("[bold green]Done.")


if __name__ == "__main__":
    main()
