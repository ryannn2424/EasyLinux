exit_seq = '\033[0m'

def red(string):
    esc_seq = '\033[31m'
    string = esc_seq + string + exit_seq
    return string

def green(string):
    esc_seq = '\033[32m'
    string = esc_seq + string + exit_seq
    return string
    
def blue(string):
    esc_seq = '\033[34m'
    string = esc_seq + string + exit_seq
    return string

def yellow(string):
    esc_seq = '\033[33m'
    string = esc_seq + string + exit_seq
    return string
    
def magenta(string):
    esc_seq = '\033[35m'
    string = esc_seq + string + exit_seq
    return string

def cyan(string):
    esc_seq = '\033[36m'
    string = esc_seq + string + exit_seq
    return string

def black(string):
    esc_seq = '\033[30m'
    string = esc_seq + string + exit_seq
    return string
