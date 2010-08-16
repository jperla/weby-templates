#!/usr/bin/env python 
import weby_templates as weby
from weby_templates.templates.lib import html

@weby.template()
def main(p):
    with p(html.html()):
        with p(html.head()):
            p(html.title('Weby templates'))
        with p(html.body({'style':'max-width:600px'})):
            p(html.h1('Weby templates'))

            p(html.p(u"""
                Weby Templates are used in production on websites that have garnered over 500,000 uniques a month.  They are incredibly easy to work with.  They are the "templates for lazy people".  They have 3 main benefits:
            """))

            with p(html.ul()):
                p(html.li(u'easier'))
                p(html.li(u'faster'))
                p(html.li(u'more flexible'))
                #p(html.li(u'shorter'))
                #p(html.li(u'safer') # when it has object cleaning

            p(html.p(u"""
                The main codebase is implemented in 100 source lines of code.  Extensive libraries only add just a couple hundred other lines of code. It is simple.  It ensures that all tags have closing tags.  It is compiled and fast.  It is unicode compliant and safe.  You can be fully fluent within 5 minutes since it is just Python and a transparent library.
            """))

            p(easier())
            p(faster())
            p(more_flexible())


            p(faq())

@weby.template()
def faq(p):
    p(html.h2('FAQ'))
    p(split_paragraphs(u"""
        """ + html.b('Q: I get this unicode error: "Always work with Unicode", what is this?') + u"""

        A: Weby Templates are unicode compliant.

        I love Python, but Python 2.x made some poor assumptions when it comes to unicode compliance which some other languages like Ruby do not suffer from.  It contains both str and unicode types, and their interaction can sometimes cause problems.

        Python 3.x fixes this by only having one string datatype: unicode.  This greatly simplifies everything, but most code is still on the 2.x branch.  To avoid annoying and difficult to debug situations, Weby Templates always outputs unicode, and it only accepts unicode.  It does not try to intelligently or magically deal with improper strings; magic like that is hard to debug.  The developer will explicitly deal with that before passing strings to Weby Templates. Explicit is better than implicit.

        As a tip, make sure you always use unicode throughout your app, and only encode/decode strings when you are inputting/outputting data to the world.  For reading from files, use the 'codecs' package in the standard library.  Make sure that you read and understand this """ + html.a('excellent article about Unicode from Joel Spolsky', {'href': 'http://www.joelonsoftware.com/articles/Unicode.html'}) + """.

        """ + html.b('Q: I like that Django Templates constrain me.  It helps me ensure that I keep templates strictly within an MVC framework.  Can I do this with Weby Templates?') + u"""

        First, since it is possible and even easy for some calls in Django Templates to have side effects, so be aware that it only provides the illusion of constraints. In fact, database calls and state mutation can be embedded in the calls.  The template language merely encourages an MVC style which template writers often adhere to.

        Second, in practice, we have used Weby Templates and similarly are encouraged to write in an MVC style due to the nature of the tool.  Mature app developers naturally have no compelling reason to violate the MVC framework, when it makes the most sense. Moreover, arguments are passed explicity to templates in the function arguments, unlike in Django where they are implicit and unpythonic, and the structure of with statements and accumulator naturally encourage an MVC style separation.
        
        Finally, since sometimes bits of html are generated in views (links, messages, etc), you can use the same template library and filters to generate these snippets as you use in your templates. Thus, you don't repeating yourself and have less, tighter code.  You do not need a separate file to generate a separate 1-line template, just add a 1-line function to your Python scripts.
        """
    ))

@weby.template()
def more_flexible(p):
    p(html.h2(u'More Flexible'))
    p(split_paragraphs(u"""
        Weby Templates are just Python functions which return strings.  """ + html.b(u'It makes no other assumptions.  ') + u"""That means that you can write HTML templates with it using the minimal HTML lib, or you can write standards-compliant XML with the XML lib, or you can write your emails, or you can write your own helper functions to generate documents in a custom format!


        Also, unlike in other languages, writing filters and nested subtemplates or modules of arbitrary nesting or which take an arbitrary number of inputs is simple: just write such a function that returns a string, and optionally use the Weby Template decorator if that makes your life easier.  Usually it does.  Every filter is just a Python function that accepts a string and returns a string.  How do you interface with this?  How do you truncate?  How do you pretty print?  The answer is obvious and in the standard lib.

        Just accumulate an object, or even just create a unicode string generator.  Any function that returns a string will be a template.  For example, each of many_hellos_* methods below are all valid, equivalent weby templates:
    """))
    
    with p((u'<pre><code>', u'</code></pre>')):
        p(ur"""
            import weby_templates as weby

            def many_hellos(num=10):
                return ('Hello, World!\n' * num)

            def many_hellos_redux(num=10):
                def many_hellos_generator(num=10):
                    for i in range(num):
                        yield 'Hello, World!\n'

                return u''.join(many_hellos_generator(num))

            @weby.template()
            def many_hellos_decorated(p, num=10):
                for i in range(num):
                    p(u'Hello, World!')
                
            @weby.template()
            def many_hellos_decorated(p, num=10):
                for i in range(num):
                    # raw function does not append newline
                    p.raw(u'Hello, World!\n')

            @weby.template()
            def many_hellos_decorated(p, num=10):
                for i in range(num):
                    # raw function does not append newline
                    p.raw(u'Hello, World!\n')




            # a sub-template (equivalent to Django filter, Django sub-templates, and Ruby helpers)
            # Since they are just functions, they can be nested, of course
            @weby.template()
            def add_greeting(p, thing):
                p.raw(u'Hello, %s!' % thing)

            # the main template, which calls the sub-template
            @weby.template()
            def many_hellos_subtemplate(p, num=10):
                for i in range(num):
                    p(add_greeting('World'))
        """)

@weby.template()
def easier(p):
    p(html.h2(u'Easier'))
    p(html.p(u"""
       Writing with weby templates takes less than 3 minutes to learn.  Below is a sample:
    """))

    with p(html.table({'width':'80%'})):
        with p(html.tr({'width': '100%'})):
            with p(html.td({'width':'40%', 'valign': 'top'})):
                with p((u'<pre><code>', u'</code></pre>')):
                    p(html.h("""
import weby_templates as weby
from weby_templates.templates.lib import html

@weby.template()
def index(p):
    with p(html.html()):
        with p(html.head()):
            p(html.title('Hello, World!'))
        with p(html.body()):
            p(html.h1('Hello, World!'))
            p(html.p('Please choose from the following items:'))
            with p(html.ul()):
                p(html.li('Lorem'))
                p(html.li('Ipsum'))
                p(html.li('Dolor'))
            with p(html.div({'class':'footer'})):
                p(u'About | Links | ... | ')
                    """))
            with p(html.td({'width':'20%', 'valign': 'top'})):
                p(u'&nbsp;')
            with p(html.td({'width':'40%', 'valign': 'top'})):
                with p((u'<pre><code>', u'</code></pre>')):
                    p(html.h(u"""
<html>
    <head>
        <title>Hello, World!</title>
    </head>
    <body>
        <h1>Hello, World!</h1>
        <p>
            Please choose from the following items:
        </p>
        <ul>
            <li>Lorem</li>
            <li>Ipsum</li>
            <li>Dolor</li>
        </ul>
        <div class="footer">
            About | Links | ... | 
        </div>
    </body>
</html>
                    """))

    p(split_paragraphs(u"""
        Fundamentally, weby templates are based on 3 simple concepts.  
    """))

    with p(html.ol()):
        p(html.li(u"""
        First, use Python to its fullest.  Weby does not invent a new esoteric language for you to learn. You know enough useful ones already.  For mature developers, using the full power of Python makes things obvious and intuitive.  Moreover, the simplicity allows the core code of Weby Templates to be just 100 lines.  

        Every template is just a function that returns a unicode string.  A template is just a string, not a fancy programming language or a complicated environmental-variable dependent rigamarole.  Just call any functino that returns a string.
        """))

        p(html.li(u"""
        Second, we include a decorator to make building the string easier.  @weby.template() is a decorator that adds a first argument to the function.  This first argument is an accumulator, conventionally named 'p', as in 'print'.  With it, you can basically print out each html element in the text.  It can also work with the 'with' statement in Python to ensure that all tags are properly enclosed.
        """))

        p(html.li(u"""
        Finally, straightforward helper libraries exist that make writing html or xml or using filters (functions that accept and output strings) easier.  For example, the html library is extremely useful.  Every html tag has an analogous function in the html library, as seen above.  The first argument are the content words, and the second argument is a dictionary of the attributes.  If the tag is in a with statement, then the first argument is just the dictionary of the attributes of the tag (since the contents are contained within the with statement.  That's all of the documentation you need to be productive in the library.
        """))

    p(split_paragraphs(u"""
        This README is generated with Weby templates if you want more examples.

    """ + html.code('./README.py > README.html') + u"""

    or

    """ + html.code('./README.py | ./weby_templates/tools/beautifier.py > README.html') + u"""
"""))

@weby.template()
def faster(p):
    p(html.h2('Faster'))
    p(split_paragraphs(u"""
        Weby templates are written in Python, and they compile to bytecode.  
        
        Moreover, they utilize the complete Python stack, so you can use the Python debugger tools, source code checkers, and your nromal build process.  

        You get the whole python compiler and optimizer speeding up your templates.
    """))

import re
@weby.template()
def split_paragraphs(p, long_text):
    """Splits on double newlines.  
    Returns the text htmlized with <p> elements.
    """
    paragraphs = re.split('\\n\s*\\n', long_text)
    for paragraph in paragraphs:
        p(html.p(paragraph))

if __name__=='__main__':
    print main()
