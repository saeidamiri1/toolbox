import time 
def timeit(fn): 
    # *args and **kwargs are to support positional and named arguments of fn
    def get_time(*args, **kwargs): 
        start = time.time() 
        output = fn(*args, **kwargs)
        print(f"Time taken in {fn.__name__}: {time.time() - start:.7f}")
        return output  # make sure that the decorator returns the output of fn
    return get_time
@timeit
def pow(a, b):
    return(a**b)

pow(10, 10)
###
dollarizer = lambda x: float(x[1:-1])

def eval_adv(expr):
# df['X'] = df.X.map(eval_adv)
    try:
        eval (expr)
    except (SyntaxError, NameError, TypeError, ZeroDivisionError):
        pass


def ls_run(): 
    locals_stored = set(locals())
    for name in locals_stored:
        val = eval(name)
        print(name, "is", type(val), "and is equal to ", val)

  
def xls_reader(file, worksheet=0):
    import xlrd
    wosh = xlrd.open_workbook(file, on_demand=True).sheets()[sheet]
    for irow in range(wosh.nrows):
        yield map(str, wosh.row_values(irow))
 
def cls():
 for name in dir():
    if not name.startswith('_'):
        del globals()[name]
        

##
# Download zip file 
import os.path
from os import path
import zipfile
download = 'pass_to_file.zip'
file_name = './file.zip'
if (not path.exists(file_name)):
    with urllib.request.urlopen(download) as response, open(file_name, 'wb') as out_file:
        data = response.read()
        out_file.write(data)
with zipfile.ZipFile(file_name, 'r') as zip_ref:
    zip_ref.extractall('file')
    
##
import gzip
open_function = lambda f: gzip.open(f,"rt") if f[-3:] == ".gz" else open(f)



#

# Built-in modules #
import re, hashlib, unicodedata

# One liners #
flatter = lambda x: [item for sublist in x for item in sublist]

################################################################################
def sanitize_text(text):
    """Make a safe representation of a string.
    Note: the `\s` special character matches any whitespace character.
    This is equivalent to the set [\t\n\r\f\v] as well as ` ` (whitespace)."""
    # First replace characters that have specific effects with their repr #
    text = re.sub("(\s)", lambda m: repr(m.group(0)).strip("'"), text)
    # Make it a unicode string (the try supports python 2 and 3) #
    try: text = text.decode('utf-8')
    except AttributeError: pass
    # Normalize it “
    text = unicodedata.normalize('NFC', text)
    return text

###############################################################################
def natural_sort(item):
    """
    Sort strings that contain numbers correctly. Works in Python 2 and 3.

    >>> l = ['v1.3.12', 'v1.3.3', 'v1.2.5', 'v1.2.15', 'v1.2.3', 'v1.2.1']
    >>> l.sort(key=natural_sort)
    >>> l.__repr__()
    "['v1.2.1', 'v1.2.3', 'v1.2.5', 'v1.2.15', 'v1.3.3', 'v1.3.12']"
    """
    dre = re.compile(r'(\d+)')
    return [int(s) if s.isdigit() else s.lower() for s in re.split(dre, item)]

################################################################################
def md5sum(file_path, blocksize=65536):
    """Compute the md5 of a file. Pretty fast."""
    result = hashlib.md5()
    with open(file_path, "rb") as f:
        chunk = f.read(blocksize)
        while chunk:
            result.update(chunk)
            chunk = f.read(blocksize)
    return result.hexdigest()
##############################################################################
#!/usr/bin/python
import subprocess, sys, shlex

def main(argv):
  args = shlex.split(argv)
  op = subprocess.Popen(args,stdout=subprocess.PIPE)
  result, err =  op.communicate()
  op.wait()
  tw = op.returncode
  # Use the result , error and return code here for extra processing



if __name__ == "__main__":
  main(sys.argv[1])


def run_sub_(cmd):
    import subprocess
    res = subprocess.Popen(cmd, shell=True, stdout=subprocess.PIPE)
    out = res.stdout.readlines()
    return ([x.strip().decode("utf-8") for x in out])

run_sub_('ls')
