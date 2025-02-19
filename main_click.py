import click
from clearml import Task

@click.command()
@click.option('--count', default=1, help='Number of greetings.')
@click.option('--name', default='hehe', prompt='Your name', help='The person to greet.')
def hello(count, name):
    task = Task.init(project_name='examples', task_name='Click single command')

    for x in range(count):
        click.echo("Hello {}!".format(name))


if __name__ == '__main__':
    hello()
