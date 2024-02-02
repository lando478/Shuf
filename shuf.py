# !/usr/local/cs/bin/python3
"""
Randomly shuffles user input or file content based on commands used. Please run script with -h or --help to learn more. 
"""
import random
import argparse
import string
import sys

#small restrictions because not mentioned in spec
# my program does not accept arguments prior to -e or -i flag. 
# my program does not redirect to to a file such as the original shuf command, this was also not mentioed in spec!
# my program had small issue when running loop or user input, it insers the escape charcter ^D or ^C. This was not mentioed to clean up so i figured it is okay!
def readFile(fileName, count, repeat=False):
      try:
            with open(fileName, 'r') as f:
                   lines = [line.rstrip('\n') for line in f.readlines()]
            random.shuffle(lines)
            if repeat == False:
                  for line in lines[:count]:
                        print(line)
            else:
                  if count is None:
                        repeater(lines, None)
                  else:
                        repeater(lines, count)
      except FileNotFoundError:
             print("shuf {}: No such file or directory".format(fileName))



def inputRange(count, inputRange, repeat=False):
      try:
            start, end = map(int, inputRange.split('-'))
      except ValueError:
            print("Invalid range format. Please use 'start'end' where both start and end are integers.")
            return
      if start > end:
            print("Invalid range. Start value should be less than or equal to the end value.")
            return
      
      ranged_list = list(range(int(start), int(end) + 1))
      random.shuffle(ranged_list)
      if repeat == False:
            if count is None:
                  for item in ranged_list:
                        print(item)
            else:
              ranged_list =  headCount(count, ranged_list)
              for item in ranged_list:
                        print(item)
      else:
              # first case: no inputRange, so just repeat until C-c is presed, making sure to shuffle. 
            if count is None:
                  repeater(ranged_list, None)
            else:
               repeater(ranged_list, count)

def echo(inputRange,items=None, repeat=False):
      if items is not None and repeat == False:
            random.shuffle(items)
            if inputRange is None:
                  for item in items:
                        print(item)
            else:
              items =  headCount(inputRange, items)
              for item in items:
                        print(item)
      else:
            # first case: no inputRange, so just repeat until C-c is presed, making sure to shuffle. 
            if inputRange is None:
                  repeater(items, None)
            else:
               repeater(items, inputRange)
                   
           
             
def headCount(count, words):
            return words[:count]


def repeater(items, numLines):
      if numLines is None:
            try:
                  while True:
                        random.shuffle(items)
                        for item in items:
                              if item != '^C':
                                    print(item)
            except KeyboardInterrupt:
             sys.exit(0)
      else:
            newItems = []
            for _ in range(numLines):
                  random.shuffle(items)
                  #by doing items[0] we are taking care of head, making sure we are appending the head of shuffled items!
                  newItems.append(items[0])
            for item in newItems:
                  print(item)
            
    
            
def main():
    parser = argparse.ArgumentParser(
        prog='Shuf',
        description='Output lines selected randomly from a file',
        epilog='End of Help')

    group = parser.add_mutually_exclusive_group()
    group.add_argument('-e', '--echo', default=None, nargs='+', help="echo the shuffled input lines'")
    group.add_argument('-i', '--input-range', default=None, help="Specify a range of input lines to be shuffled (e.g., 1-10)")
    parser.add_argument('-n', '--head-count', action="store", dest="numlines", type=int, default=None, help="specify a head count")
    parser.add_argument('-r', '--repeat', action='store_true',dest="repeat", default=False, help="Repeat output lines (when specified, allow repetitions).")
    parser.add_argument('FILE', nargs='?', default='-', help="Input file, default is stdin")
    args = parser.parse_args()
    lines = []

    #if statment for echo
    if args.echo:
            echo(args.numlines, args.echo, args.repeat)
    
    elif args.input_range:
            inputRange(args.numlines, args.input_range, args.repeat)
    elif args.FILE is None or args.FILE == '-':
            try:
                  for line in sys.stdin:
                        lines.append(line)
            except EOFError:
                  pass  # Handle the EOFError gracefully

            random.shuffle(lines)
            for line in lines:
                 print(line, end='')
    else:
      readFile(args.FILE, args.numlines, args.repeat)

      


                             
if __name__ == "__main__":
    main()


