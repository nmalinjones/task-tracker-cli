import click 
import tabulate
import task_manager

@click.group()
def cli():
    pass

@click.command()
@click.argument("desc")
def add(desc : str):
    data_to_add = {}
    

cli.add_command(add)

if __name__ == '__main__':
    cli()