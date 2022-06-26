import shutil
import os
import typer

def main():
    typer.confirm("are you sure you want to revert all worksheet files?", abort = True)
    src_directory = r"./protected/worksheets_backup/"
    dst_directory = r"./worksheets/"


    typer.secho("deleting files")
    # for file in os.listdir(dst_directory):
    #     path = os.path.join(dst_directory, file)
    #     try:
    #         shutil.rmtree(path)
    #     except OSError:
    #         os.remove(path)
    shutil.rmtree(dst_directory)

    typer.secho("rebuilding worksheets")
    shutil.copytree(src_directory, dst_directory)

    typer.secho("Completed successfully. Happy coding.")


if __name__ == "__main__":
    typer.run(main)