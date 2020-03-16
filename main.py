import sys
import controller.make_question

if __name__ == '__main__':
    if len(sys.argv) != 2:
        print("Usage : python main.py <your atcoder id>")
    else:
        controller.make_question.dairy_question(sys.argv[1])
