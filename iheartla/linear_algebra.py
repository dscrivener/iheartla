from .la_parser.parser import compile_la_file, compile_la_content, ParserTypeEnum
from .la_tools.la_logger import LaLogger, LoggerTypeEnum
import logging
import argparse
DEBUG = False   # log level


def show_gui():
    from .la_gui.frame import wx, MainWindow
    app = wx.App(False)
    MainWindow(None, "I❤️LA")
    app.MainLoop()


def compile_la(content):
    return compile_la_content(content, ParserTypeEnum.NUMPY|ParserTypeEnum.EIGEN|ParserTypeEnum.LATEX)


if __name__ == '__main__':
    if DEBUG:
        LaLogger.getInstance().set_level(logging.INFO)
    else:
        LaLogger.getInstance().set_level(logging.ERROR)
    arg_parser = argparse.ArgumentParser(description='I Heart LA')
    arg_parser.add_argument('-o', '--output', help='The output language', choices = ['numpy', 'eigen', 'latex'])
    # arg_parser.add_argument('-i', '--input', help='File name containing I heart LA source code')
    arg_parser.add_argument('--GUI', action='store_true', help='Launch the GUI editor')
    arg_parser.add_argument('input', nargs='*', help='The I Heart LA files to compile.')
    args = arg_parser.parse_args()
    if args.GUI:
        show_gui()
    elif args.input:
        parser_type = ParserTypeEnum.DEFAULT
        out_dict = {"numpy": ParserTypeEnum.NUMPY, "eigen": ParserTypeEnum.EIGEN, "latex": ParserTypeEnum.LATEX}
        if args.output:
            out_list = args.output.split(",")
            for out in out_list:
                assert out in out_dict, "Parameters after -o or --output can only be numpy, eigen or latex"
                parser_type = parser_type | out_dict[out]
        for input in args.input: compile_la_file(input, parser_type)
    else:
        show_gui()