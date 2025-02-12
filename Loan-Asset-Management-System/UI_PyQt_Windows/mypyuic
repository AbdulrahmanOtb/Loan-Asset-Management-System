#!/usr/bin/python3

__author__ = 'saud'
import os, sys, argcomplete, argparse
from string import Template
# import ntpath
QTWindowClasses = ['QMainWindow', 'QDialog', 'QWidget']
CompilerMode = 'pyqt5'

class CI():
    Name = 0
    superClasses = 1
    WedgetType = 2

def get_class_name(txt):
    """
    @param txt: the line that contain the word class
    @type txt: str
    @return: the name of the class
    @rtype: str
    """
    b = txt.index('class')
    e = txt.index('(')
    s = txt[b+5:e]
    # s = txt.__getslice__(b+5, e)
    s = s.strip(' ')
    return s


def get_subclasses(cls, pyfileBuff):
    """
    @param cls:
    @type cls: list
    @param pyfileBuff:
    @type pyfileBuff:  list
    @return:
    @rtype: list
    """
    subclasses = []
    lineN = cls[1]
    lineTxt = pyfileBuff[lineN+1]
    """@type: str """
    for i in range(len(pyfileBuff)):
        lineTxt = pyfileBuff[i]
        """@type: str """
        if lineTxt.__contains__('if __name__ == "__main__":'):
            lineTxt = pyfileBuff[i+3]
            b = lineTxt.find('= QtGui.') + len('= QtGui.')
            e = lineTxt.find(')')
            txt = lineTxt[b:e-1]
            txt = txt.strip(' ')
            subclasses.append('QtGui.' + txt)
            subclasses.append(cls[0])
    return subclasses
def get_subclasses_PyQt5(cls, pyfileBuff):
    """
    @param cls:
    @type cls: list
    @param pyfileBuff:
    @type pyfileBuff:  list
    @return:
    @rtype: list
    """
    subclasses = []
    lineN = cls[1]
    lineTxt = pyfileBuff[lineN+1]
    """@type: str """
    for i in range(len(pyfileBuff)):
        lineTxt = pyfileBuff[i]
        """@type: str """
        if lineTxt.__contains__('if __name__ == "__main__":'):
            lineTxt = pyfileBuff[i+3]
            b = lineTxt.find('= QtWidgets.') + len('= QtWidgets.')
            e = lineTxt.find(')')
            txt = lineTxt[b:e-1]
            txt = txt.strip(' ')
            subclasses.append('QtWidgets.' + txt)
            subclasses.append(cls[0])
    return subclasses


def find_all_classes(pyfileBuff):
    """
    @param pyfileBuff: the python file buffer to search in
    @type pyfileBuff: list
    @return: return a list that contains the pair of [classname, line number]
    @rtype: list
    """
    classes = []
    for i in range(len(pyfileBuff)):
        l = pyfileBuff[i]
        """@type: str """
        if l.__contains__('class'):
            #print i+1, 'Class found at this line', l
            classes.append([get_class_name(l), i])
    return classes


def generate_uiClass(name, subclasses):
    """
    @param name: the name of the generated class (e.g, Form1)
    @type name: str
    @param subclasses: the classes that is needed to be inherited
    @type subclasses: list
    @return: a formatted python code as str object
    @rtype: str
    """
    QTwedgit = subclasses[0]
    subs = ''
    for cls in subclasses:
        subs += cls + ', '
    subs = subs[:-2]
    #print subs
    code = Template("""
class $name ($subs):
    def __init__(self):
        $QTwedgit.__init__(self)
        self = self.setupUi(self)

    \n""")
    s = code.substitute(name=name, subs=subs, QTwedgit=QTwedgit)
    return s

def pyfile2ClassName(filename):
  e = filename.find('.')
  CName = filename[:e] if e > 0 else filename
  return CName


def UI_Compile(ifile, className, compiler='pyside-uic'):
  """
  @type ifile: str
  @type className: str
  @rtype : bool
  """
  RetBuffer = ''
  cmd = '{cc} {ifile} -x'.format(cc=compiler, ifile=ifile)
  # buff = commands.getoutput(cmd) #type: str
  buff = os.popen(cmd).read() #type: str

  # print(buff)
  lines = buff.split('\n')
  classes = find_all_classes(lines)
  if className == 'className':
    className = classes[0][0].replace("Ui_", '')
  Codes = []
  for cls in classes:
      if CompilerMode == 'pyqt5':
        subclses = get_subclasses_PyQt5(cls, pyfileBuff=lines)
      elif CompilerMode == 'pyside2':
        subclses = get_subclasses(cls, pyfileBuff=lines)
      else:
        subclses = get_subclasses(cls, pyfileBuff=lines)

      code = generate_uiClass(className, subclses)
      Codes.append(code)
      #print(code)
      ins = buff.find('if __name__ == "__main__":')
      RetBuffer = buff[:ins -1] + code + buff[ins:]
      #print(RetBuffer)

  return RetBuffer


def EnvironCompleter():
    return ([v for v in os.environ])

x= EnvironCompleter()

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description='compile Qt4.ui files to .py files')
    parser.add_argument('ifile', help='the input file to be compiled')
    parser.add_argument('-o', '--out', help='the output file')
    parser.add_argument('-m', '--mode', help='To specify how to compile th ui. use one of the following [pyside, pyqt4, pyqt5]; default: pyside')

    # parser.add_argument('display', choices=['Dis', 'W', 'DisW'], help='They way the output is generated')
    #group = parser.add_mutually_exclusive_group()
    # parser.add_argument('-o', '--output', help='the compiled output .py file')
    # parser.add_argument('-d', '--display',  action='store_true', help='display the compiled file rather than save it to a file')

    argcomplete.autocomplete(parser)
    args = parser.parse_args()


    if not os.path.isfile(args.ifile):
      print('The input file does not exist')
      exit(0)

    # path, FileName = ntpath.split(args.ofile)
    if args.out:
      ClassName = pyfile2ClassName(args.out)
    else:
      ClassName = 'className'

    mode = args.mode
    if not mode:
      cmd = 'pyside-uic'
    else:
      if mode == 'pyside':
        cmd = 'pyside-uic'
      elif mode == 'pyqt4':
        cmd ='pyuic4'
      elif mode == 'pyqt5':
        cmd ='pyuic5'
      else:
        print('mode (%s) is not recognized' % mode)
        exit(0)

    # retV = commands.getoutput(cmd)
    retV = os.popen(cmd).read()
    if 'No command' in retV or 'not found' in retV:
      print('This mode (%s) is not available in your system, please use your package manager to install it' % mode)
      exit(0)

    compiler = cmd

    # print("Compiling %s" % (args.ifile))
    compiled_py = UI_Compile(args.ifile, ClassName, compiler)  # type: str

    if args.out:
      try:
        OF = open(args.out, mode='wb')
        OF.write(compiled_py.encode())
        OF.flush()
        OF.close()
      except:
        print('Error: can not write to the output file: %s' % args.out)
    else:
      print(compiled_py)

