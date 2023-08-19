import click
@click.group()
@click.version_option()
def cli():
    pass

@cli.command()
@click.option('--idea', '-i', help='Initial musical idea example: "C D C"', \
        required=True)
@click.option('--scale', '-s', help='Scale associated with the idea')
@click.option('--output', '-o', help='Output file name', default='output.mid')
def compose(idea, scale, output):
    """Compose a melody based on an initial idea."""
    from musicality_cli.cli_manager import compose_with_GA
    click.echo('Composing melody based on idea: {}'.format(idea))
    compose_with_GA(idea, scale, output)
