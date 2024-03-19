import sys
import re

def md_html_heading(input):
    
    md_headings = [r'^######\s+(.*)$', r'^#####\s+(.*)$', r'^####\s+(.*)$', r'^###\s+(.*)$', r'^##\s+(.*)$', r'^#\s+(.*)$']
    html_headings = [r'<h6>\1</h6>', r'<h5>\1</h5>', r'<h4>\1</h4>', r'<h3>\1</h3>', r'<h2>\1</h2>', r'<h1>\1</h1>']

    for index, regex in enumerate(md_headings):
        replace = html_headings[index]
        input = re.sub(regex,replace , input, flags=re.MULTILINE)

    return input

def md_html_bold_italic(input):
    input = re.sub(r'(\*\*|__)(.*?)\1', r'<b>\2</b>', input,flags=re.MULTILINE)
    input = re.sub(r'(\*|_)(.*?)\1', r'<i>\2</i>', input,flags=re.MULTILINE)

    return input


def md_html_unordered(md_text):
    html_text = ""
    started_ul = False
    for line in md_text.split("\n"):
        if re.match(r"^\s*- (.*)$", line):
            if not started_ul:
                started_ul = True
                html_text += "<ul>\n"
            line = re.sub(r"^\s*- (.*)$", "\t<li>\\1</li>", line)
            html_text += line + "\n"
        else:
            if started_ul:
                started_ul = False
                html_text += "</ul>\n"
            html_text += line + "\n"
    return html_text

def md_hmtl_ordered(md_text):
    html_text = ""
    started_ol = False
    for line in md_text.split("\n"):
        if re.match(r"^\s*\d+\.\s+(.*)$", line):
            if not started_ol:
                started_ol = True
                html_text += "<ol>\n"
            line = re.sub(r"^\s*\d+\.\s+(.*)$", "\t<li>\\1</li>", line)
            html_text += line + "\n"
        else:
            if started_ol:
                started_ol = False
                html_text += "</ol>\n"
            html_text += line + "\n"
    return html_text


def md_html_link(input):
    regex = r'\[(.*?)\]\((.*?)\)'
    output = r'<a src="\2">\1</a>'

    input = re.sub(regex, output,  input, flags=re.MULTILINE)
    return input

def md_html_image(input):
    regex = r'!\[(.*?)\]\((.*?)\)'
    output = r'<img src="\2" alt="\1"/>'

    input = re.sub(regex, output,  input, flags=re.MULTILINE)
    return input


def parse_md(input):

    result = md_html_heading(input)
    result = md_html_bold_italic(result)
    result = md_hmtl_ordered(result)
    result = md_html_unordered(result)
    result = md_html_image(result)
    result = md_html_link(result)
    
    return result
    


def main():
    markdown_text = sys.stdin.read()

    print(parse_md(markdown_text))

if __name__ == "__main__":
    main()