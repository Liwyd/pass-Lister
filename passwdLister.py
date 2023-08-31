import os, sys, time, argparse, random, platform
def Print():
    Cls = '\x1b[0m'
    Colors = [31, 30, 31,  31, 30]
    introduce = '''PassList maker -- liwyd
usage:

-w   --KeyWords     help=keyWords to iterate
-c   --characters   help=characters to join
-d   --data         help=data to iterate
-out --output       help=output of wordlist file

'''
    for N, Line in enumerate(introduce.split('\n')):
        sys.stdout.write('\x1b[1;%dm%s%s\n' %
                         (random.choice(Colors), Line, Cls))
        time.sleep(0.08)
def clear():
    current_os = platform.system()
    if current_os == 'Windows':
        os.system("cls")
    else:
        os.system("clear")   
def createWordList(characters:str, data:str, KeyWords:str, output:str) -> str:
    st = time.time()
    
    data_list = data.split(',')
    word_list = KeyWords.split(',')
    character_list = characters.split(',')
    with open(f'{output}', 'a') as file:
        for EveryWord in word_list:
            file.write(EveryWord+'\n')
        for FirstData in data_list:
            for SecData in data_list:
                for chra in character_list:
                    file.write(FirstData+SecData+'\n')
                    file.write(FirstData+chra+SecData+'\n')
        file.close()
    clear()
    print('[ELAPSED]: %s min'%('{:.2f}'.format(((time.time())-st)/60)))
    print (f"-> '{output}'")


if __name__ == '__main__':
    parser = argparse.ArgumentParser(
        formatter_class=argparse.RawTextHelpFormatter,
        description='Python Wordlist Generator')
    parser.add_argument(
        '-w', '--KeyWords',
        default=None, help='keyWords to iterate')
    parser.add_argument(
        '-c', '--characters',
        default=None, help='characters to join')
    parser.add_argument(
        '-d', '--data',
        default=None, help='data to iterate')
    parser.add_argument(
        '-out', '--output',
        default='output/wordlist.txt', help='output of wordlist file.')

    args = parser.parse_args()
    if args.KeyWords is None or args.data is None or args.characters is None:
        Print()
        print('[FAILED]: you can not leave the --characters, --data and --KeyWords empty !')
        sys.exit()


    createWordList(args.characters, args.data, args.KeyWords, args.output)