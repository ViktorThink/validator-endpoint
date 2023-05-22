from typing import Annotated
import typer

from btvep.db import api_keys
import os


app = typer.Typer(
    help=f"""
    Update and read config values. Config values available:\n
    \n
    \t- hotkey_mnemonic\n\n

    Example usage:\n
    - btvep config set hotkey_mnemonic "my mnemonic"\n
    - btvep config get hotkey_mnemonic

"""
)


@app.callback(no_args_is_help=True)
def main():
    pass


@app.command()
def set(
    key: Annotated[
        str,
        typer.Argument(
            help="The config key to set.",
        ),
    ],
    value: Annotated[
        str,
        typer.Argument(
            help="The config value to set.",
        ),
    ],
):
    """
    Set a config value.
    """

    # handle mnemonic
    # This will currently overwrite the entire .env file.
    # TODO: Add a better way to save config values. Maybe a json file or in db.
    if key == "hotkey_mnemonic":
        # write to .env relative to this file
        with open(os.path.join(os.path.dirname(__file__), "../.env"), "w") as f:
            f.write(f"HOTKEY_MNEMONIC={value}")
        return
    else:
        # Raise error with typer
        raise typer.BadParameter(f"""Unknown config key: {key}""")


@app.command()
def get(
    key: Annotated[
        str,
        typer.Argument(
            help="The config key to get.",
        ),
    ] = None,
):
    """
    Prints a config value.
    """

    # handle mnemonic
    if key == "hotkey_mnemonic":
        # read to .env relative to this file
        with open(os.path.join(os.path.dirname(__file__), "../.env"), "r") as f:
            print(f.read().split("=")[1])
    else:
        # Raise error with typer
        raise typer.BadParameter(f"""Unknown config key: {key}""")