import click

@click.command()
@click.option('--address', help='Address String')
def process_input(address):
    """ Takes and address string and displays a weather profile """
    click.echo("You Entered "+address)

if __name__ == '__main__':
    process_input()