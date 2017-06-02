# This file was automatically generated by SWIG (http://www.swig.org).
# Version 3.0.12
#
# Do not make changes to this file unless you know what you are doing--modify
# the SWIG interface file instead.

from sys import version_info as _swig_python_version_info
if _swig_python_version_info >= (2, 7, 0):
    def swig_import_helper():
        import importlib
        pkg = __name__.rpartition('.')[0]
        mname = '.'.join((pkg, '_graphkernelsCpy')).lstrip('.')
        try:
            return importlib.import_module(mname)
        except ImportError:
            return importlib.import_module('_graphkernelsCpy')
    _graphkernelsCpy = swig_import_helper()
    del swig_import_helper
elif _swig_python_version_info >= (2, 6, 0):
    def swig_import_helper():
        from os.path import dirname
        import imp
        fp = None
        try:
            fp, pathname, description = imp.find_module('_graphkernelsCpy', [dirname(__file__)])
        except ImportError:
            import _graphkernelsCpy
            return _graphkernelsCpy
        try:
            _mod = imp.load_module('_graphkernelsCpy', fp, pathname, description)
        finally:
            if fp is not None:
                fp.close()
        return _mod
    _graphkernelsCpy = swig_import_helper()
    del swig_import_helper
else:
    import _graphkernelsCpy
del _swig_python_version_info

try:
    _swig_property = property
except NameError:
    pass  # Python < 2.2 doesn't have 'property'.

try:
    import builtins as __builtin__
except ImportError:
    import __builtin__

def _swig_setattr_nondynamic(self, class_type, name, value, static=1):
    if (name == "thisown"):
        return self.this.own(value)
    if (name == "this"):
        if type(value).__name__ == 'SwigPyObject':
            self.__dict__[name] = value
            return
    method = class_type.__swig_setmethods__.get(name, None)
    if method:
        return method(self, value)
    if (not static):
        if _newclass:
            object.__setattr__(self, name, value)
        else:
            self.__dict__[name] = value
    else:
        raise AttributeError("You cannot add attributes to %s" % self)


def _swig_setattr(self, class_type, name, value):
    return _swig_setattr_nondynamic(self, class_type, name, value, 0)


def _swig_getattr(self, class_type, name):
    if (name == "thisown"):
        return self.this.own()
    method = class_type.__swig_getmethods__.get(name, None)
    if method:
        return method(self)
    raise AttributeError("'%s' object has no attribute '%s'" % (class_type.__name__, name))


def _swig_repr(self):
    try:
        strthis = "proxy of " + self.this.__repr__()
    except __builtin__.Exception:
        strthis = ""
    return "<%s.%s; %s >" % (self.__class__.__module__, self.__class__.__name__, strthis,)

try:
    _object = object
    _newclass = 1
except __builtin__.Exception:
    class _object:
        pass
    _newclass = 0

class SwigPyIterator(_object):
    __swig_setmethods__ = {}
    __setattr__ = lambda self, name, value: _swig_setattr(self, SwigPyIterator, name, value)
    __swig_getmethods__ = {}
    __getattr__ = lambda self, name: _swig_getattr(self, SwigPyIterator, name)

    def __init__(self, *args, **kwargs):
        raise AttributeError("No constructor defined - class is abstract")
    __repr__ = _swig_repr
    __swig_destroy__ = _graphkernelsCpy.delete_SwigPyIterator
    __del__ = lambda self: None

    def value(self):
        return _graphkernelsCpy.SwigPyIterator_value(self)

    def incr(self, n=1):
        return _graphkernelsCpy.SwigPyIterator_incr(self, n)

    def decr(self, n=1):
        return _graphkernelsCpy.SwigPyIterator_decr(self, n)

    def distance(self, x):
        return _graphkernelsCpy.SwigPyIterator_distance(self, x)

    def equal(self, x):
        return _graphkernelsCpy.SwigPyIterator_equal(self, x)

    def copy(self):
        return _graphkernelsCpy.SwigPyIterator_copy(self)

    def next(self):
        return _graphkernelsCpy.SwigPyIterator_next(self)

    def __next__(self):
        return _graphkernelsCpy.SwigPyIterator___next__(self)

    def previous(self):
        return _graphkernelsCpy.SwigPyIterator_previous(self)

    def advance(self, n):
        return _graphkernelsCpy.SwigPyIterator_advance(self, n)

    def __eq__(self, x):
        return _graphkernelsCpy.SwigPyIterator___eq__(self, x)

    def __ne__(self, x):
        return _graphkernelsCpy.SwigPyIterator___ne__(self, x)

    def __iadd__(self, n):
        return _graphkernelsCpy.SwigPyIterator___iadd__(self, n)

    def __isub__(self, n):
        return _graphkernelsCpy.SwigPyIterator___isub__(self, n)

    def __add__(self, n):
        return _graphkernelsCpy.SwigPyIterator___add__(self, n)

    def __sub__(self, *args):
        return _graphkernelsCpy.SwigPyIterator___sub__(self, *args)
    def __iter__(self):
        return self
SwigPyIterator_swigregister = _graphkernelsCpy.SwigPyIterator_swigregister
SwigPyIterator_swigregister(SwigPyIterator)

SHARED_PTR_DISOWN = _graphkernelsCpy.SHARED_PTR_DISOWN
class IntVector(_object):
    __swig_setmethods__ = {}
    __setattr__ = lambda self, name, value: _swig_setattr(self, IntVector, name, value)
    __swig_getmethods__ = {}
    __getattr__ = lambda self, name: _swig_getattr(self, IntVector, name)
    __repr__ = _swig_repr

    def iterator(self):
        return _graphkernelsCpy.IntVector_iterator(self)
    def __iter__(self):
        return self.iterator()

    def __nonzero__(self):
        return _graphkernelsCpy.IntVector___nonzero__(self)

    def __bool__(self):
        return _graphkernelsCpy.IntVector___bool__(self)

    def __len__(self):
        return _graphkernelsCpy.IntVector___len__(self)

    def __getslice__(self, i, j):
        return _graphkernelsCpy.IntVector___getslice__(self, i, j)

    def __setslice__(self, *args):
        return _graphkernelsCpy.IntVector___setslice__(self, *args)

    def __delslice__(self, i, j):
        return _graphkernelsCpy.IntVector___delslice__(self, i, j)

    def __delitem__(self, *args):
        return _graphkernelsCpy.IntVector___delitem__(self, *args)

    def __getitem__(self, *args):
        return _graphkernelsCpy.IntVector___getitem__(self, *args)

    def __setitem__(self, *args):
        return _graphkernelsCpy.IntVector___setitem__(self, *args)

    def pop(self):
        return _graphkernelsCpy.IntVector_pop(self)

    def append(self, x):
        return _graphkernelsCpy.IntVector_append(self, x)

    def empty(self):
        return _graphkernelsCpy.IntVector_empty(self)

    def size(self):
        return _graphkernelsCpy.IntVector_size(self)

    def swap(self, v):
        return _graphkernelsCpy.IntVector_swap(self, v)

    def begin(self):
        return _graphkernelsCpy.IntVector_begin(self)

    def end(self):
        return _graphkernelsCpy.IntVector_end(self)

    def rbegin(self):
        return _graphkernelsCpy.IntVector_rbegin(self)

    def rend(self):
        return _graphkernelsCpy.IntVector_rend(self)

    def clear(self):
        return _graphkernelsCpy.IntVector_clear(self)

    def get_allocator(self):
        return _graphkernelsCpy.IntVector_get_allocator(self)

    def pop_back(self):
        return _graphkernelsCpy.IntVector_pop_back(self)

    def erase(self, *args):
        return _graphkernelsCpy.IntVector_erase(self, *args)

    def __init__(self, *args):
        this = _graphkernelsCpy.new_IntVector(*args)
        try:
            self.this.append(this)
        except __builtin__.Exception:
            self.this = this

    def push_back(self, x):
        return _graphkernelsCpy.IntVector_push_back(self, x)

    def front(self):
        return _graphkernelsCpy.IntVector_front(self)

    def back(self):
        return _graphkernelsCpy.IntVector_back(self)

    def assign(self, n, x):
        return _graphkernelsCpy.IntVector_assign(self, n, x)

    def resize(self, *args):
        return _graphkernelsCpy.IntVector_resize(self, *args)

    def insert(self, *args):
        return _graphkernelsCpy.IntVector_insert(self, *args)

    def reserve(self, n):
        return _graphkernelsCpy.IntVector_reserve(self, n)

    def capacity(self):
        return _graphkernelsCpy.IntVector_capacity(self)
    __swig_destroy__ = _graphkernelsCpy.delete_IntVector
    __del__ = lambda self: None
IntVector_swigregister = _graphkernelsCpy.IntVector_swigregister
IntVector_swigregister(IntVector)

class IntIntVector(_object):
    __swig_setmethods__ = {}
    __setattr__ = lambda self, name, value: _swig_setattr(self, IntIntVector, name, value)
    __swig_getmethods__ = {}
    __getattr__ = lambda self, name: _swig_getattr(self, IntIntVector, name)
    __repr__ = _swig_repr

    def iterator(self):
        return _graphkernelsCpy.IntIntVector_iterator(self)
    def __iter__(self):
        return self.iterator()

    def __nonzero__(self):
        return _graphkernelsCpy.IntIntVector___nonzero__(self)

    def __bool__(self):
        return _graphkernelsCpy.IntIntVector___bool__(self)

    def __len__(self):
        return _graphkernelsCpy.IntIntVector___len__(self)

    def __getslice__(self, i, j):
        return _graphkernelsCpy.IntIntVector___getslice__(self, i, j)

    def __setslice__(self, *args):
        return _graphkernelsCpy.IntIntVector___setslice__(self, *args)

    def __delslice__(self, i, j):
        return _graphkernelsCpy.IntIntVector___delslice__(self, i, j)

    def __delitem__(self, *args):
        return _graphkernelsCpy.IntIntVector___delitem__(self, *args)

    def __getitem__(self, *args):
        return _graphkernelsCpy.IntIntVector___getitem__(self, *args)

    def __setitem__(self, *args):
        return _graphkernelsCpy.IntIntVector___setitem__(self, *args)

    def pop(self):
        return _graphkernelsCpy.IntIntVector_pop(self)

    def append(self, x):
        return _graphkernelsCpy.IntIntVector_append(self, x)

    def empty(self):
        return _graphkernelsCpy.IntIntVector_empty(self)

    def size(self):
        return _graphkernelsCpy.IntIntVector_size(self)

    def swap(self, v):
        return _graphkernelsCpy.IntIntVector_swap(self, v)

    def begin(self):
        return _graphkernelsCpy.IntIntVector_begin(self)

    def end(self):
        return _graphkernelsCpy.IntIntVector_end(self)

    def rbegin(self):
        return _graphkernelsCpy.IntIntVector_rbegin(self)

    def rend(self):
        return _graphkernelsCpy.IntIntVector_rend(self)

    def clear(self):
        return _graphkernelsCpy.IntIntVector_clear(self)

    def get_allocator(self):
        return _graphkernelsCpy.IntIntVector_get_allocator(self)

    def pop_back(self):
        return _graphkernelsCpy.IntIntVector_pop_back(self)

    def erase(self, *args):
        return _graphkernelsCpy.IntIntVector_erase(self, *args)

    def __init__(self, *args):
        this = _graphkernelsCpy.new_IntIntVector(*args)
        try:
            self.this.append(this)
        except __builtin__.Exception:
            self.this = this

    def push_back(self, x):
        return _graphkernelsCpy.IntIntVector_push_back(self, x)

    def front(self):
        return _graphkernelsCpy.IntIntVector_front(self)

    def back(self):
        return _graphkernelsCpy.IntIntVector_back(self)

    def assign(self, n, x):
        return _graphkernelsCpy.IntIntVector_assign(self, n, x)

    def resize(self, *args):
        return _graphkernelsCpy.IntIntVector_resize(self, *args)

    def insert(self, *args):
        return _graphkernelsCpy.IntIntVector_insert(self, *args)

    def reserve(self, n):
        return _graphkernelsCpy.IntIntVector_reserve(self, n)

    def capacity(self):
        return _graphkernelsCpy.IntIntVector_capacity(self)
    __swig_destroy__ = _graphkernelsCpy.delete_IntIntVector
    __del__ = lambda self: None
IntIntVector_swigregister = _graphkernelsCpy.IntIntVector_swigregister
IntIntVector_swigregister(IntIntVector)

class FloatVector(_object):
    __swig_setmethods__ = {}
    __setattr__ = lambda self, name, value: _swig_setattr(self, FloatVector, name, value)
    __swig_getmethods__ = {}
    __getattr__ = lambda self, name: _swig_getattr(self, FloatVector, name)
    __repr__ = _swig_repr

    def iterator(self):
        return _graphkernelsCpy.FloatVector_iterator(self)
    def __iter__(self):
        return self.iterator()

    def __nonzero__(self):
        return _graphkernelsCpy.FloatVector___nonzero__(self)

    def __bool__(self):
        return _graphkernelsCpy.FloatVector___bool__(self)

    def __len__(self):
        return _graphkernelsCpy.FloatVector___len__(self)

    def __getslice__(self, i, j):
        return _graphkernelsCpy.FloatVector___getslice__(self, i, j)

    def __setslice__(self, *args):
        return _graphkernelsCpy.FloatVector___setslice__(self, *args)

    def __delslice__(self, i, j):
        return _graphkernelsCpy.FloatVector___delslice__(self, i, j)

    def __delitem__(self, *args):
        return _graphkernelsCpy.FloatVector___delitem__(self, *args)

    def __getitem__(self, *args):
        return _graphkernelsCpy.FloatVector___getitem__(self, *args)

    def __setitem__(self, *args):
        return _graphkernelsCpy.FloatVector___setitem__(self, *args)

    def pop(self):
        return _graphkernelsCpy.FloatVector_pop(self)

    def append(self, x):
        return _graphkernelsCpy.FloatVector_append(self, x)

    def empty(self):
        return _graphkernelsCpy.FloatVector_empty(self)

    def size(self):
        return _graphkernelsCpy.FloatVector_size(self)

    def swap(self, v):
        return _graphkernelsCpy.FloatVector_swap(self, v)

    def begin(self):
        return _graphkernelsCpy.FloatVector_begin(self)

    def end(self):
        return _graphkernelsCpy.FloatVector_end(self)

    def rbegin(self):
        return _graphkernelsCpy.FloatVector_rbegin(self)

    def rend(self):
        return _graphkernelsCpy.FloatVector_rend(self)

    def clear(self):
        return _graphkernelsCpy.FloatVector_clear(self)

    def get_allocator(self):
        return _graphkernelsCpy.FloatVector_get_allocator(self)

    def pop_back(self):
        return _graphkernelsCpy.FloatVector_pop_back(self)

    def erase(self, *args):
        return _graphkernelsCpy.FloatVector_erase(self, *args)

    def __init__(self, *args):
        this = _graphkernelsCpy.new_FloatVector(*args)
        try:
            self.this.append(this)
        except __builtin__.Exception:
            self.this = this

    def push_back(self, x):
        return _graphkernelsCpy.FloatVector_push_back(self, x)

    def front(self):
        return _graphkernelsCpy.FloatVector_front(self)

    def back(self):
        return _graphkernelsCpy.FloatVector_back(self)

    def assign(self, n, x):
        return _graphkernelsCpy.FloatVector_assign(self, n, x)

    def resize(self, *args):
        return _graphkernelsCpy.FloatVector_resize(self, *args)

    def insert(self, *args):
        return _graphkernelsCpy.FloatVector_insert(self, *args)

    def reserve(self, n):
        return _graphkernelsCpy.FloatVector_reserve(self, n)

    def capacity(self):
        return _graphkernelsCpy.FloatVector_capacity(self)
    __swig_destroy__ = _graphkernelsCpy.delete_FloatVector
    __del__ = lambda self: None
FloatVector_swigregister = _graphkernelsCpy.FloatVector_swigregister
FloatVector_swigregister(FloatVector)

class DoubleVector(_object):
    __swig_setmethods__ = {}
    __setattr__ = lambda self, name, value: _swig_setattr(self, DoubleVector, name, value)
    __swig_getmethods__ = {}
    __getattr__ = lambda self, name: _swig_getattr(self, DoubleVector, name)
    __repr__ = _swig_repr

    def iterator(self):
        return _graphkernelsCpy.DoubleVector_iterator(self)
    def __iter__(self):
        return self.iterator()

    def __nonzero__(self):
        return _graphkernelsCpy.DoubleVector___nonzero__(self)

    def __bool__(self):
        return _graphkernelsCpy.DoubleVector___bool__(self)

    def __len__(self):
        return _graphkernelsCpy.DoubleVector___len__(self)

    def __getslice__(self, i, j):
        return _graphkernelsCpy.DoubleVector___getslice__(self, i, j)

    def __setslice__(self, *args):
        return _graphkernelsCpy.DoubleVector___setslice__(self, *args)

    def __delslice__(self, i, j):
        return _graphkernelsCpy.DoubleVector___delslice__(self, i, j)

    def __delitem__(self, *args):
        return _graphkernelsCpy.DoubleVector___delitem__(self, *args)

    def __getitem__(self, *args):
        return _graphkernelsCpy.DoubleVector___getitem__(self, *args)

    def __setitem__(self, *args):
        return _graphkernelsCpy.DoubleVector___setitem__(self, *args)

    def pop(self):
        return _graphkernelsCpy.DoubleVector_pop(self)

    def append(self, x):
        return _graphkernelsCpy.DoubleVector_append(self, x)

    def empty(self):
        return _graphkernelsCpy.DoubleVector_empty(self)

    def size(self):
        return _graphkernelsCpy.DoubleVector_size(self)

    def swap(self, v):
        return _graphkernelsCpy.DoubleVector_swap(self, v)

    def begin(self):
        return _graphkernelsCpy.DoubleVector_begin(self)

    def end(self):
        return _graphkernelsCpy.DoubleVector_end(self)

    def rbegin(self):
        return _graphkernelsCpy.DoubleVector_rbegin(self)

    def rend(self):
        return _graphkernelsCpy.DoubleVector_rend(self)

    def clear(self):
        return _graphkernelsCpy.DoubleVector_clear(self)

    def get_allocator(self):
        return _graphkernelsCpy.DoubleVector_get_allocator(self)

    def pop_back(self):
        return _graphkernelsCpy.DoubleVector_pop_back(self)

    def erase(self, *args):
        return _graphkernelsCpy.DoubleVector_erase(self, *args)

    def __init__(self, *args):
        this = _graphkernelsCpy.new_DoubleVector(*args)
        try:
            self.this.append(this)
        except __builtin__.Exception:
            self.this = this

    def push_back(self, x):
        return _graphkernelsCpy.DoubleVector_push_back(self, x)

    def front(self):
        return _graphkernelsCpy.DoubleVector_front(self)

    def back(self):
        return _graphkernelsCpy.DoubleVector_back(self)

    def assign(self, n, x):
        return _graphkernelsCpy.DoubleVector_assign(self, n, x)

    def resize(self, *args):
        return _graphkernelsCpy.DoubleVector_resize(self, *args)

    def insert(self, *args):
        return _graphkernelsCpy.DoubleVector_insert(self, *args)

    def reserve(self, n):
        return _graphkernelsCpy.DoubleVector_reserve(self, n)

    def capacity(self):
        return _graphkernelsCpy.DoubleVector_capacity(self)
    __swig_destroy__ = _graphkernelsCpy.delete_DoubleVector
    __del__ = lambda self: None
DoubleVector_swigregister = _graphkernelsCpy.DoubleVector_swigregister
DoubleVector_swigregister(DoubleVector)

class VecMatrixXi(_object):
    __swig_setmethods__ = {}
    __setattr__ = lambda self, name, value: _swig_setattr(self, VecMatrixXi, name, value)
    __swig_getmethods__ = {}
    __getattr__ = lambda self, name: _swig_getattr(self, VecMatrixXi, name)
    __repr__ = _swig_repr

    def iterator(self):
        return _graphkernelsCpy.VecMatrixXi_iterator(self)
    def __iter__(self):
        return self.iterator()

    def __nonzero__(self):
        return _graphkernelsCpy.VecMatrixXi___nonzero__(self)

    def __bool__(self):
        return _graphkernelsCpy.VecMatrixXi___bool__(self)

    def __len__(self):
        return _graphkernelsCpy.VecMatrixXi___len__(self)

    def __getslice__(self, i, j):
        return _graphkernelsCpy.VecMatrixXi___getslice__(self, i, j)

    def __setslice__(self, *args):
        return _graphkernelsCpy.VecMatrixXi___setslice__(self, *args)

    def __delslice__(self, i, j):
        return _graphkernelsCpy.VecMatrixXi___delslice__(self, i, j)

    def __delitem__(self, *args):
        return _graphkernelsCpy.VecMatrixXi___delitem__(self, *args)

    def __getitem__(self, *args):
        return _graphkernelsCpy.VecMatrixXi___getitem__(self, *args)

    def __setitem__(self, *args):
        return _graphkernelsCpy.VecMatrixXi___setitem__(self, *args)

    def pop(self):
        return _graphkernelsCpy.VecMatrixXi_pop(self)

    def append(self, x):
        return _graphkernelsCpy.VecMatrixXi_append(self, x)

    def empty(self):
        return _graphkernelsCpy.VecMatrixXi_empty(self)

    def size(self):
        return _graphkernelsCpy.VecMatrixXi_size(self)

    def swap(self, v):
        return _graphkernelsCpy.VecMatrixXi_swap(self, v)

    def begin(self):
        return _graphkernelsCpy.VecMatrixXi_begin(self)

    def end(self):
        return _graphkernelsCpy.VecMatrixXi_end(self)

    def rbegin(self):
        return _graphkernelsCpy.VecMatrixXi_rbegin(self)

    def rend(self):
        return _graphkernelsCpy.VecMatrixXi_rend(self)

    def clear(self):
        return _graphkernelsCpy.VecMatrixXi_clear(self)

    def get_allocator(self):
        return _graphkernelsCpy.VecMatrixXi_get_allocator(self)

    def pop_back(self):
        return _graphkernelsCpy.VecMatrixXi_pop_back(self)

    def erase(self, *args):
        return _graphkernelsCpy.VecMatrixXi_erase(self, *args)

    def __init__(self, *args):
        this = _graphkernelsCpy.new_VecMatrixXi(*args)
        try:
            self.this.append(this)
        except __builtin__.Exception:
            self.this = this

    def push_back(self, x):
        return _graphkernelsCpy.VecMatrixXi_push_back(self, x)

    def front(self):
        return _graphkernelsCpy.VecMatrixXi_front(self)

    def back(self):
        return _graphkernelsCpy.VecMatrixXi_back(self)

    def assign(self, n, x):
        return _graphkernelsCpy.VecMatrixXi_assign(self, n, x)

    def resize(self, *args):
        return _graphkernelsCpy.VecMatrixXi_resize(self, *args)

    def insert(self, *args):
        return _graphkernelsCpy.VecMatrixXi_insert(self, *args)

    def reserve(self, n):
        return _graphkernelsCpy.VecMatrixXi_reserve(self, n)

    def capacity(self):
        return _graphkernelsCpy.VecMatrixXi_capacity(self)
    __swig_destroy__ = _graphkernelsCpy.delete_VecMatrixXi
    __del__ = lambda self: None
VecMatrixXi_swigregister = _graphkernelsCpy.VecMatrixXi_swigregister
VecMatrixXi_swigregister(VecMatrixXi)


def selectLinearGaussian(h1, h2, sigma):
    return _graphkernelsCpy.selectLinearGaussian(h1, h2, sigma)
selectLinearGaussian = _graphkernelsCpy.selectLinearGaussian

def productMapping(e1, e2, v1_label, v2_label, H):
    return _graphkernelsCpy.productMapping(e1, e2, v1_label, v2_label, H)
productMapping = _graphkernelsCpy.productMapping

def bucketsort(x, index, label_max):
    return _graphkernelsCpy.bucketsort(x, index, label_max)
bucketsort = _graphkernelsCpy.bucketsort

def edgeHistogramKernel(e1, e2, sigma):
    return _graphkernelsCpy.edgeHistogramKernel(e1, e2, sigma)
edgeHistogramKernel = _graphkernelsCpy.edgeHistogramKernel

def vertexHistogramKernel(v1_label, v2_label, sigma):
    return _graphkernelsCpy.vertexHistogramKernel(v1_label, v2_label, sigma)
vertexHistogramKernel = _graphkernelsCpy.vertexHistogramKernel

def vertexEdgeHistogramKernel(e1, e2, v1_label, v2_label, sigma):
    return _graphkernelsCpy.vertexEdgeHistogramKernel(e1, e2, v1_label, v2_label, sigma)
vertexEdgeHistogramKernel = _graphkernelsCpy.vertexEdgeHistogramKernel

def vertexVertexEdgeHistogramKernel(e1, e2, v1_label, v2_label, arg5):
    return _graphkernelsCpy.vertexVertexEdgeHistogramKernel(e1, e2, v1_label, v2_label, arg5)
vertexVertexEdgeHistogramKernel = _graphkernelsCpy.vertexVertexEdgeHistogramKernel

def WLKernelMatrix(E, V_label, num_v, num_e, degree_max, h_max):
    return _graphkernelsCpy.WLKernelMatrix(E, V_label, num_v, num_e, degree_max, h_max)
WLKernelMatrix = _graphkernelsCpy.WLKernelMatrix

def computeKernelValue(e1, e2, v1_label, v2_label, par, kernel_type):
    return _graphkernelsCpy.computeKernelValue(e1, e2, v1_label, v2_label, par, kernel_type)
computeKernelValue = _graphkernelsCpy.computeKernelValue

def CalculateKernelPy(E, V_label, V_count, E_count, D_max, par, kernel_type):
    return _graphkernelsCpy.CalculateKernelPy(E, V_label, V_count, E_count, D_max, par, kernel_type)
CalculateKernelPy = _graphkernelsCpy.CalculateKernelPy
# This file is compatible with both classic and new-style classes.


