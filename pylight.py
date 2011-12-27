from pygments import highlight
from pygments.lexers import *
from pygments.formatters import get_formatter_by_name


def pylight(args):
    if 'source' not in args:
        return False
    try:
        lexer     = detect_lexer(args)
        formatter = detect_formatter(args)
        return { 'lexer': lexer.name,
                 'body': highlight(args['source'], lexer, formatter) }
    except:
        return False


def detect_lexer(args):
    if 'lang' in args:
        return get_lexer_by_name(args['lang'])
    elif 'mimetype' in args:
        return get_lexer_for_mimetype(args['mimetype'])
    elif 'filename' in args:
        return guess_lexer_for_filename(args['filename'],
                                        args['source'])
    else:
        return guess_lexer(args['source'])


def detect_formatter(args):
    if 'format' in args:
        return get_formatter_by_name(args['format'])
    else:
        return get_formatter_by_name('html')
