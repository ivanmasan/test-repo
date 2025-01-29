import argparse
from clearml import Task

def hello(count, name):
    task = Task.init(project_name='examples', task_name='Argparse single command')
    
    for _ in range(count):
        print(f"Hello {name}!")

def main():
    parser = argparse.ArgumentParser(description='Greet a user a specified number of times.')
    parser.add_argument('--count', type=int, default=1, help='Number of greetings.')
    parser.add_argument('--name', required=True, help='The person to greet.')
    
    args = parser.parse_args()
    hello(args.count, args.name)

if __name__ == '__main__':
    main()
