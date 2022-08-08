import importlib
import subprocess as sp
import time

import click
import pandas as pd
from rich.console import Console
from rich.progress import track

console = Console()

approaches = [
    "with_python",
    "with_numpy",
    "with_cython",
    "with_pythran",
    "with_pythran_omp",
    "with_numba",
    "with_pybind11",
    "with_dask",
    "with_cupy",
]


@click.command()
@click.argument("module_name", type=click.Choice(approaches))
def main(module_name):
    console.print("Benchmarking with different number of rows ...")
    rows_results = {
        "Number of Rows": [],
        "Approach": [],
        "Computational Time (sec)": [],
    }
    module = importlib.import_module(module_name)

    # Warm up
    data = module.create_data(1000, 1)
    for _ in range(5):
        module.arc_length(data)

    for n_rows in track(
        range(1000000, 10000001, 500000), description=module_name, console=console
    ):
        data = module.create_data(n_rows, 3)
        # 20 trials
        for _ in range(20):
            start = time.perf_counter()
            module.arc_length(data)
            end = time.perf_counter()
            rows_results["Number of Rows"].append(n_rows)
            rows_results["Approach"].append(module_name)
            rows_results["Computational Time (sec)"].append(end - start)

    time.sleep(1)

    df = pd.DataFrame(rows_results)
    df.to_csv("data/{}.rows.csv".format(module_name))

    console.print("Benchmarking with different number of columns ...")
    cols_results = {
        "Number of Columns": [],
        "Approach": [],
        "Computational Time (sec)": [],
    }

    # Warm up
    data = module.create_data(1000, 1)
    for _ in range(5):
        module.arc_length(data)

    for n_rows in track(
        range(1000, 10001, 500), description=module_name, console=console
    ):
        data = module.create_data(n_rows, 10000)
        # 20 trials
        for _ in range(20):
            start = time.perf_counter()
            module.arc_length(data)
            end = time.perf_counter()
            cols_results["Number of Columns"].append(n_rows)
            cols_results["Approach"].append(module_name)
            cols_results["Computational Time (sec)"].append(end - start)

    df = pd.DataFrame(cols_results)
    df.to_csv("data/{}.cols.csv".format(module_name))

    console.print("[bold green]Done.")


if __name__ == "__main__":
    main()
