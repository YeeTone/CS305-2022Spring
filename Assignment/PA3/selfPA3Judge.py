import sys
import difflib
import argparse


def read_file(file_name):
    try:
        file_handle = open(file_name, 'r')
        text = file_handle.read().splitlines()
        file_handle.close()
        return text
    except IOError as error:
        print('Read file Error: {0}'.format(error))
        sys.exit()


def compare_file(file1_name, file2_name):
    if file1_name == "" or file2_name == "":
        sys.exit()
    text1_lines = read_file(file1_name)
    text2_lines = read_file(file2_name)
    diff = difflib.HtmlDiff()
    result = diff.make_file(text1_lines, text2_lines)
    try:
        with open('result.html', 'w') as result_file:
            result_file.write(result)
    except IOError as error:
        print('写入html文件错误:{0}'.format(error))


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description='selfPA3Judge.py -s file1 -d file2 ')
    parser.add_argument('-s', dest='source_file', type=str, help='源文件')
    parser.add_argument('-d', dest='dest_file', type=str, help='目标文件')
    args = parser.parse_args()

    if not args.source_file or not args.dest_file:
        print("源文件或者目标文件为空")
        parser.usage()

    source_file = args.source_file
    dest_file = args.dest_file
    compare_file(source_file, dest_file)