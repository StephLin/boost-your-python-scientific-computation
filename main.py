import subprocess as sp

import inquirer
from rich.console import Console

console = Console()

question = inquirer.List(
    "mode",
    "Select a mode: ",
    [
        "with_python",
        "with_cython",
        "with_pythran",
        "with_numpy",
        "with_pythran_numpy",
        "with_numba",
        "with_numba_aot",
        "with_numba_guvectorize",
        "with_dask",
        "with_pybind11",
        "with_cupy",
        "exit",
    ],
)

try:
    while True:
        answer = inquirer.prompt([question])
        mode = answer["mode"] if answer is not None else "exit"

        if mode == "exit":
            break

        console.print("----- [light_green]{}[/] -----".format(mode))
        cmd = "cd {} && python main.py".format(mode)
        console.print("[bright_black]$ {}".format(cmd))
        p = sp.run(cmd, shell=True)
        if p.returncode == 0:
            console.print(
                "----- [light_green]Exit with returncode {}[/] -----\n".format(
                    p.returncode
                )
            )
        else:
            console.print(
                "----- [bold red]Exit with returncode {}[/] -----\n".format(
                    p.returncode
                )
            )

except KeyboardInterrupt:
    pass

finally:
    console.print("[light_green]Bye ;)")
