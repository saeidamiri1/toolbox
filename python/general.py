import time 
def timeit(fn): 
    # *args and **kwargs are to support positional and named arguments of fn
    def get_time(*args, **kwargs): 
        start = time.time() 
        output = fn(*args, **kwargs)
        print(f"Time taken in {fn.__name__}: {time.time() - start:.7f}")
        return output  # make sure that the decorator returns the output of fn
    return get_time

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
        
