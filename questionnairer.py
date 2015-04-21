"""Program to run simple questionnairs

Note: All TODO items need to be addressed, and TODO comments removed

"""

import argparse
import sys
import os.path import exists
import time


# NOTE: API (what functions are named, their arguments and return values) is
#       only suggestive.
#
#       Feel free to change everything for this homework.
os.chdir('home/ashlee/psyc161-hw2/questionnaires/sample1.txt')

def read_questions(input_file):
    """Reads questions and answer choices from the input_file
    """
    # Questions will be a list where each item consists of a list where first
    # element is the question, and the 2nd one -- available choices.
    questions = []
    answ = []
    with open(input_file) as f:
        for line in f.readlines():
            if line == '#':
                continue
            elif line[] == '-':
                editQ = line.lstrip('_')
                questions.append(editQ)
            elif line[] == ' *':
                editA = line.lstrip(' *')
                answ.append(editA)
            else:
                print 'improper question format'

        pass
    return questions


def present_questions(questions):
    """ for each question in questions print them one by one
    """
    answers, timings = [], []
    for ask in len(questions):
        start = time.time()
        Print questions[ask]
        rxntime = (time.time() - start)
        response = answ[1]


    # TODO
    return answers, timings


def write_answers(output_file, questions, answers, timings):
    """write the responses to each question in a file
    """
    with open(output_file, 'w') as f:
        answ = []
        for ask in len(questions)
            str2write = '-{}\n * []\n *'
            f.write(str2write)
            answ = answ + 1
        pass # TODO


def parse_options(argv):
    """I do not understand this section
    """
    # TODO:  __doc__ can give you the docstring of this file -- use it
    #        for description?

    # Define command line options we know
    parser = argparse.ArgumentParser(description="Simple questionnair runner")
    parser.add_argument('input_file',
                        help='Input file containing questionnair')
    parser.add_argument('-o', '--output_file',
                        help='Output file to store answers')

    # Parse command line options
    return parser.parse_args(argv[1:])


# We moved out this functionality into a separate function, so we could
# automatically test its correct function
def main(argv):
    """Main body of the program
    """
    args = parse_options(argv)
    if not os.path.exists(args.input_file):
        # Error messages are usually output to "standard error", not "standard
        # output", so we will write to the stderr directly as if it was a file.
        # .write() does not add a newline (\n) so we have to do it
        sys.stderr.write("File %s not found\n" % args.input_file)
        raise SystemExit(4)

    if not args.output_file:
        raise ValueError("Please provide the output file")

    questions = read_questions(args.input_file)
    answers, timings = present_questions(questions)

    write_answers(args.output_file, questions, answers, timings)


#
# Testing routines
#
from nose.tools import assert_equal, assert_raises


def test_read_questions():
    assert_equal(read_questions('sample1.txt'),
                 [['What is your name darling?'],
                 ['Have you slept well today?', 'yes', 'no'],
                 ['Rate from 1 (hate it) to 5 (love it) how much you like to '
                  'press buttons?', '1', '2', '3', '4', '5']])
    pass

def test_present_questions():
    """ tests present_questions function
    """
    (ans, times) = present_questions([['What is your name darling?'],
                                      ['Have you slept well today?', 'yes', 'no'],
                                      ['Rate from 1 (hate it) to 5 (love it) how much for you like to press buttons?', '1', '2','3', '4', '5']], testing=True)
    assert_equal(ans, ['Billy Gates Junior', 'yes', '1'])
    assert_equal(times[0:] < [0.1]*3, True)
    pass


def test_parse_argv():
    assert_raises(TypeError, parse_options, 'sample1.txt', 1)
    assert_raises(TypeError, parse_options, 1, 'output.txt')

    pass # TODO - verify that given correct options, you get correct

def test_main():
    # Just run it and see it not fail -- we return nothing.  It is a "smoke test"
    assert_equal(main(["questionnairer.py", "-o", "test_write.txt", "sample1.txt"], testing=True),
                 None)
    asset_raises(ValueError, main, [questionnairer.py, sample1.txt], testing=True)

    # TODO: super-extra credit: figure out how to test execution of main with
    # "--help".


if __name__ == '__main__':
    # this section will run read_questions et al.
    main(sys.argv)
