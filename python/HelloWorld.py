import argparse

def main(parser):
    parser.add_argument('--name',default='Big, Big World')
    print('Hello,')
    args=parser.parse_args()
    print(args.name, '!')
    
main(argparse.ArgumentParser())
