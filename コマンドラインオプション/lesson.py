from optparse import OptionParser


def main():
    parser = OptionParser(usage='usage: %prog [options] arg1 arg2')
    parser.add_option('-f', '--file', action='store', type='string', dest='filename', help='File name')
    parser.add_option('-n', '--num', action='store', type='int', dest='num')
    parser.add_option('-v', action='store_true', dest='verbose')
    options, args = parser.parse_args()
    print(options)
    print(args)


if __name__ == '__main__':
    main()
