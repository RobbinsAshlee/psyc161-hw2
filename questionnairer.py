"""Program to run simple questionnaires

Note: All TODO items need to be addressed, and TODO comments removed

"""

import argparse
import sys
from os.path import exists
import time


# NOTE: API (what functions are named, their arguments and return values) is
#       only suggestive.
#
#       Feel free to change everything for this homework.


def read_questions(input_file):
    """Reads questions and answer choices from the input_file
    """
    # Questions will be a list where each item consists of a list where first
    # element is the question, and the 2nd one -- available choices.
    questions = []
    answers_right = []
    with open(input_file) as f:
        line = f.readlines()
        for line in lines:
            if line.startswith('#'):
                continue
            elif line.startswith('-'):
                editQ = line.lstrip('_')
                questions.append(editQ)
            elif line.startswith('  *'):
                editA = line.lstrip(' *')
                answers_right.append(editA)
            else:
                assert ValueError('incorrect question format')

    return questions


def present_questions(questions, testing_input =None):
    """ for each question in questions print them one by one
    """
    answers, timings = [], []
    user_input = testing_input or raw_input()
    for ask in questions:
        start = time.time()
        if questions[1] == 0 or testing_input:
            answers.append(user_input(questions[0]))
            if testing_input:
                time.sleep(0.05)
                continue
        else:
            user_response = str(usr_input(question[0])).lower()
            while user_response not in answers_right[0]:
                print "Provide an acceptable answer:",
                print str(question[0])).lower()
            answers.append(user_response)
        rxntime = time.time() - start
        timings.append(rxntime)
    return answers, timings


def write_answers(output_file, questions, answers, timings):
    """write the responses to each question in a file
    """
    with open(output_file, 'w') as f:
        for (questions, answer), answer, timing in zip(questions, answer, timings):
            f.writelines('-%s\n' % questions)
            f.writelines(" * %s\n" + % answer)
            f.writelines(" * response time: %f\n" % timings)
        f.close()



def parse_options(argv):
    """command line options for parsing the document
    """

    # Define command line options we know
    parser = argparse.ArgumentParser(description=mainDocString)
    parser.add_argument('input_file',
                        help='Input file containing questionnaire')
    parser.add_argument('-o', '--output_file',
                        help='Output file to store answers')

    # Parse command line options
    return parser.parse_args(argv[1:])


# We moved out this functionality into a separate function, so we could
# automatically test its correct function
def main(argv, testing_input=None):
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
    answers, timings = present_questions(questions,
                                        testing_input=simulated_rae_input)

    write_answers(args.output_file, questions, answers, timings)


#
# Testing routines
#
from nose.tools import assert_equal, assert_raises

def dummy(question):
    return 'this is not an answer'

def test_read_questions(input_file):
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

    pass #verify that given correct options, you get correct

def test_main():
    assert_equal(main['questionnairer.py', '-o', 'NOSETEST.txt', 'sample1.txt'],
                 input_func=dummy), none)
    assert_raises(ValueError, main ['questionnairer.py', 'sample1.txt'], input_func=dummy)
    assert_raises(ValueError, main, ['questionnairer.py', '-o', 'NotCorrect.txt', 'questionnaires/sample1errors.txt'],
                input_func=dummy)
    pass

if __name__ == '__main__':
    # this section will run read_questions and start the function
    main(sys.argv)
