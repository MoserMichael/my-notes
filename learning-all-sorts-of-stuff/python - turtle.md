Python turtle package on OSX

    - install python via brew

    brew install python3

    - get version
    
    /opt/homebrew/bin/python3 --version
    Python 3.11.4

    - install python tkinter binding for the same version!

    brew install python-tk@3.11

--

Most member functions of the Turtle class (and Screen class) are also available as global functions. Here is how they do it in the turtle module:

Interesting form of metaprogramming in python: see https://github.com/python/cpython/blob/3.11/Lib/turtle.py
 

    - pass names of functions to _make_global_funcs  

_tg_turtle_functions = ['back', 'backward', 'begin_fill', 'begin_poly', 'bk',
        'circle', 'clear', 'clearstamp', 'clearstamps', 'clone', 'color',
        'degrees', 'distance', 'dot', 'down', 'end_fill', 'end_poly', 'fd',
        'fillcolor', 'filling', 'forward', 'get_poly', 'getpen', 'getscreen', 'get_shapepoly',
        'getturtle', 'goto', 'heading', 'hideturtle', 'home', 'ht', 'isdown',
        'isvisible', 'left', 'lt', 'onclick', 'ondrag', 'onrelease', 'pd',
        'pen', 'pencolor', 'pendown', 'pensize', 'penup', 'pos', 'position',
        'pu', 'radians', 'right', 'reset', 'resizemode', 'rt',
        'seth', 'setheading', 'setpos', 'setposition', 'settiltangle',
        'setundobuffer', 'setx', 'sety', 'shape', 'shapesize', 'shapetransform', 'shearfactor', 'showturtle',
        'speed', 'st', 'stamp', 'tilt', 'tiltangle', 'towards',
        'turtlesize', 'undo', 'undobufferentries', 'up', 'width',
        'write', 'xcor', 'ycor']

_make_global_funcs(_tg_turtle_functions, Turtle,
                   'Turtle._pen', 'Turtle()', _turtle_docrevise)

        - _make_global_funcs  formats the code of the global forwarding functions as a string
        - the generated function chesk if the global variable Turtle._pen is set, if not then it creates a turtle and puts it into this variable
        - then calls the method with the same name as that of generated global with parameters / forwards the call.
        - the parameter list is is retrieved from the class objects (getmethod / getmethparlist)
        - exec( VARIABLE_WITH_FUNCTION_CODE )  - interprets the function.
        - some fudging with the docstrings.

__func_body = """\
def {name}{paramslist}:
    if {obj} is None:
        if not TurtleScreen._RUNNING:
            TurtleScreen._RUNNING = True
            raise Terminator
        {obj} = {init}
    try:
        return {obj}.{name}{argslist}
    except TK.TclError:
        if not TurtleScreen._RUNNING:
            TurtleScreen._RUNNING = True
            raise Terminator
        raise
"""

def _make_global_funcs(functions, cls, obj, init, docrevise):
    for methodname in functions:
        method = getattr(cls, methodname)
        pl1, pl2 = getmethparlist(method)
        if pl1 == "":
            print(">>>>>>", pl1, pl2)
            continue
        defstr = __func_body.format(obj=obj, init=init, name=methodname,
                                    paramslist=pl1, argslist=pl2)
        exec(defstr, globals())
        globals()[methodname].__doc__ = docrevise(method.__doc__)


