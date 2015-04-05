import argparse
import re

def main(**kwargs):
    parser = argparse.ArgumentParser(description='Run a command', version='%(prog)s 1.0')
    parser.add_argument('command', type=str, help='Command name')
    parser.add_argument('parameters', type=str, nargs='*', help='Parameters')
    # parser.add_argument('infiles', nargs='+', type=str, help='Input text files')
    # parser.add_argument('--out', type=str, default='temp.txt', help='name of output file')
    args = parser.parse_args()
    # args_dict = vars(parser.parse_args())
    if args.command == 'create':
        password = args.parameters[1]
        if len(password) >= 6 and len(password) <= 16 and re.compile('\d').search(password) and re.compile('[a-z]').search(password) and re.compile('[A-Z]').search(password):
            print 'Account Created'
        else:
            print 'Invalid Password'
    else:
        parser.print_help()



if __name__ == '__main__':
    main()