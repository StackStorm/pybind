
from operator import attrgetter
import pyangbind.lib.xpathhelper as xpathhelper
from pyangbind.lib.yangtypes import RestrictedPrecisionDecimalType, RestrictedClassType, TypedListType
from pyangbind.lib.yangtypes import YANGBool, YANGListType, YANGDynClass, ReferenceType
from pyangbind.lib.base import PybindBase
from decimal import Decimal
from bitarray import bitarray
import __builtin__
class stats(PybindBase):
  """
  This class was auto-generated by the PythonClass plugin for PYANG
  from YANG module brocade-mpls-operational - based on the path /mpls-state/memory/stats. Each member element of
  the container is represented as a class variable - with a specific
  YANG type.

  YANG Description: 1
  """
  __slots__ = ('_pybind_generated_by', '_path_helper', '_yang_name', '_rest_name', '_extmethods', '__mem_stats_index','__mem_type','__num_alloc','__total_bytes','__total_allocs','__total_frees','__peak_alloc','__alloc_fails','__free_fails',)

  _yang_name = 'stats'
  _rest_name = 'stats'

  _pybind_generated_by = 'container'

  def __init__(self, *args, **kwargs):

    path_helper_ = kwargs.pop("path_helper", None)
    if path_helper_ is False:
      self._path_helper = False
    elif path_helper_ is not None and isinstance(path_helper_, xpathhelper.YANGPathHelper):
      self._path_helper = path_helper_
    elif hasattr(self, "_parent"):
      path_helper_ = getattr(self._parent, "_path_helper", False)
      self._path_helper = path_helper_
    else:
      self._path_helper = False

    extmethods = kwargs.pop("extmethods", None)
    if extmethods is False:
      self._extmethods = False
    elif extmethods is not None and isinstance(extmethods, dict):
      self._extmethods = extmethods
    elif hasattr(self, "_parent"):
      extmethods = getattr(self._parent, "_extmethods", None)
      self._extmethods = extmethods
    else:
      self._extmethods = False
    self.__total_frees = YANGDynClass(base=RestrictedClassType(base_type=long, restriction_dict={'range': ['0..4294967295']}, int_size=32), is_leaf=True, yang_name="total-frees", rest_name="total-frees", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='urn:brocade.com:mgmt:brocade-mpls-operational', defining_module='brocade-mpls-operational', yang_type='uint32', is_config=False)
    self.__alloc_fails = YANGDynClass(base=RestrictedClassType(base_type=long, restriction_dict={'range': ['0..4294967295']}, int_size=32), is_leaf=True, yang_name="alloc-fails", rest_name="alloc-fails", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='urn:brocade.com:mgmt:brocade-mpls-operational', defining_module='brocade-mpls-operational', yang_type='uint32', is_config=False)
    self.__peak_alloc = YANGDynClass(base=RestrictedClassType(base_type=long, restriction_dict={'range': ['0..4294967295']}, int_size=32), is_leaf=True, yang_name="peak-alloc", rest_name="peak-alloc", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='urn:brocade.com:mgmt:brocade-mpls-operational', defining_module='brocade-mpls-operational', yang_type='uint32', is_config=False)
    self.__total_allocs = YANGDynClass(base=RestrictedClassType(base_type=long, restriction_dict={'range': ['0..4294967295']}, int_size=32), is_leaf=True, yang_name="total-allocs", rest_name="total-allocs", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='urn:brocade.com:mgmt:brocade-mpls-operational', defining_module='brocade-mpls-operational', yang_type='uint32', is_config=False)
    self.__mem_stats_index = YANGDynClass(base=RestrictedClassType(base_type=long, restriction_dict={'range': ['0..4294967295']}, int_size=32), is_leaf=True, yang_name="mem-stats-index", rest_name="mem-stats-index", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, is_keyval=True, namespace='urn:brocade.com:mgmt:brocade-mpls-operational', defining_module='brocade-mpls-operational', yang_type='uint32', is_config=False)
    self.__num_alloc = YANGDynClass(base=RestrictedClassType(base_type=long, restriction_dict={'range': ['0..4294967295']}, int_size=32), is_leaf=True, yang_name="num-alloc", rest_name="num-alloc", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='urn:brocade.com:mgmt:brocade-mpls-operational', defining_module='brocade-mpls-operational', yang_type='uint32', is_config=False)
    self.__free_fails = YANGDynClass(base=RestrictedClassType(base_type=long, restriction_dict={'range': ['0..4294967295']}, int_size=32), is_leaf=True, yang_name="free-fails", rest_name="free-fails", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='urn:brocade.com:mgmt:brocade-mpls-operational', defining_module='brocade-mpls-operational', yang_type='uint32', is_config=False)
    self.__total_bytes = YANGDynClass(base=RestrictedClassType(base_type=long, restriction_dict={'range': ['0..4294967295']}, int_size=32), is_leaf=True, yang_name="total-bytes", rest_name="total-bytes", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='urn:brocade.com:mgmt:brocade-mpls-operational', defining_module='brocade-mpls-operational', yang_type='uint32', is_config=False)
    self.__mem_type = YANGDynClass(base=unicode, is_leaf=True, yang_name="mem-type", rest_name="mem-type", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='urn:brocade.com:mgmt:brocade-mpls-operational', defining_module='brocade-mpls-operational', yang_type='string', is_config=False)

    load = kwargs.pop("load", None)
    if args:
      if len(args) > 1:
        raise TypeError("cannot create a YANG container with >1 argument")
      all_attr = True
      for e in self._pyangbind_elements:
        if not hasattr(args[0], e):
          all_attr = False
          break
      if not all_attr:
        raise ValueError("Supplied object did not have the correct attributes")
      for e in self._pyangbind_elements:
        nobj = getattr(args[0], e)
        if nobj._changed() is False:
          continue
        setmethod = getattr(self, "_set_%s" % e)
        if load is None:
          setmethod(getattr(args[0], e))
        else:
          setmethod(getattr(args[0], e), load=load)

  def _path(self):
    if hasattr(self, "_parent"):
      return self._parent._path()+[self._yang_name]
    else:
      return [u'mpls-state', u'memory', u'stats']

  def _rest_path(self):
    if hasattr(self, "_parent"):
      if self._rest_name:
        return self._parent._rest_path()+[self._rest_name]
      else:
        return self._parent._rest_path()
    else:
      return [u'mpls-state', u'memory', u'stats']

  def _get_mem_stats_index(self):
    """
    Getter method for mem_stats_index, mapped from YANG variable /mpls_state/memory/stats/mem_stats_index (uint32)

    YANG Description: Memory stats index
    """
    return self.__mem_stats_index
      
  def _set_mem_stats_index(self, v, load=False):
    """
    Setter method for mem_stats_index, mapped from YANG variable /mpls_state/memory/stats/mem_stats_index (uint32)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_mem_stats_index is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_mem_stats_index() directly.

    YANG Description: Memory stats index
    """
    parent = getattr(self, "_parent", None)
    if parent is not None and load is False:
      raise AttributeError("Cannot set keys directly when" +
                             " within an instantiated list")

    if hasattr(v, "_utype"):
      v = v._utype(v)
    try:
      t = YANGDynClass(v,base=RestrictedClassType(base_type=long, restriction_dict={'range': ['0..4294967295']}, int_size=32), is_leaf=True, yang_name="mem-stats-index", rest_name="mem-stats-index", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, is_keyval=True, namespace='urn:brocade.com:mgmt:brocade-mpls-operational', defining_module='brocade-mpls-operational', yang_type='uint32', is_config=False)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """mem_stats_index must be of a type compatible with uint32""",
          'defined-type': "uint32",
          'generated-type': """YANGDynClass(base=RestrictedClassType(base_type=long, restriction_dict={'range': ['0..4294967295']}, int_size=32), is_leaf=True, yang_name="mem-stats-index", rest_name="mem-stats-index", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, is_keyval=True, namespace='urn:brocade.com:mgmt:brocade-mpls-operational', defining_module='brocade-mpls-operational', yang_type='uint32', is_config=False)""",
        })

    self.__mem_stats_index = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_mem_stats_index(self):
    self.__mem_stats_index = YANGDynClass(base=RestrictedClassType(base_type=long, restriction_dict={'range': ['0..4294967295']}, int_size=32), is_leaf=True, yang_name="mem-stats-index", rest_name="mem-stats-index", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, is_keyval=True, namespace='urn:brocade.com:mgmt:brocade-mpls-operational', defining_module='brocade-mpls-operational', yang_type='uint32', is_config=False)


  def _get_mem_type(self):
    """
    Getter method for mem_type, mapped from YANG variable /mpls_state/memory/stats/mem_type (string)

    YANG Description: Memory type
    """
    return self.__mem_type
      
  def _set_mem_type(self, v, load=False):
    """
    Setter method for mem_type, mapped from YANG variable /mpls_state/memory/stats/mem_type (string)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_mem_type is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_mem_type() directly.

    YANG Description: Memory type
    """
    if hasattr(v, "_utype"):
      v = v._utype(v)
    try:
      t = YANGDynClass(v,base=unicode, is_leaf=True, yang_name="mem-type", rest_name="mem-type", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='urn:brocade.com:mgmt:brocade-mpls-operational', defining_module='brocade-mpls-operational', yang_type='string', is_config=False)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """mem_type must be of a type compatible with string""",
          'defined-type': "string",
          'generated-type': """YANGDynClass(base=unicode, is_leaf=True, yang_name="mem-type", rest_name="mem-type", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='urn:brocade.com:mgmt:brocade-mpls-operational', defining_module='brocade-mpls-operational', yang_type='string', is_config=False)""",
        })

    self.__mem_type = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_mem_type(self):
    self.__mem_type = YANGDynClass(base=unicode, is_leaf=True, yang_name="mem-type", rest_name="mem-type", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='urn:brocade.com:mgmt:brocade-mpls-operational', defining_module='brocade-mpls-operational', yang_type='string', is_config=False)


  def _get_num_alloc(self):
    """
    Getter method for num_alloc, mapped from YANG variable /mpls_state/memory/stats/num_alloc (uint32)

    YANG Description: Number of allocations
    """
    return self.__num_alloc
      
  def _set_num_alloc(self, v, load=False):
    """
    Setter method for num_alloc, mapped from YANG variable /mpls_state/memory/stats/num_alloc (uint32)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_num_alloc is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_num_alloc() directly.

    YANG Description: Number of allocations
    """
    if hasattr(v, "_utype"):
      v = v._utype(v)
    try:
      t = YANGDynClass(v,base=RestrictedClassType(base_type=long, restriction_dict={'range': ['0..4294967295']}, int_size=32), is_leaf=True, yang_name="num-alloc", rest_name="num-alloc", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='urn:brocade.com:mgmt:brocade-mpls-operational', defining_module='brocade-mpls-operational', yang_type='uint32', is_config=False)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """num_alloc must be of a type compatible with uint32""",
          'defined-type': "uint32",
          'generated-type': """YANGDynClass(base=RestrictedClassType(base_type=long, restriction_dict={'range': ['0..4294967295']}, int_size=32), is_leaf=True, yang_name="num-alloc", rest_name="num-alloc", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='urn:brocade.com:mgmt:brocade-mpls-operational', defining_module='brocade-mpls-operational', yang_type='uint32', is_config=False)""",
        })

    self.__num_alloc = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_num_alloc(self):
    self.__num_alloc = YANGDynClass(base=RestrictedClassType(base_type=long, restriction_dict={'range': ['0..4294967295']}, int_size=32), is_leaf=True, yang_name="num-alloc", rest_name="num-alloc", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='urn:brocade.com:mgmt:brocade-mpls-operational', defining_module='brocade-mpls-operational', yang_type='uint32', is_config=False)


  def _get_total_bytes(self):
    """
    Getter method for total_bytes, mapped from YANG variable /mpls_state/memory/stats/total_bytes (uint32)

    YANG Description: Total bytes
    """
    return self.__total_bytes
      
  def _set_total_bytes(self, v, load=False):
    """
    Setter method for total_bytes, mapped from YANG variable /mpls_state/memory/stats/total_bytes (uint32)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_total_bytes is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_total_bytes() directly.

    YANG Description: Total bytes
    """
    if hasattr(v, "_utype"):
      v = v._utype(v)
    try:
      t = YANGDynClass(v,base=RestrictedClassType(base_type=long, restriction_dict={'range': ['0..4294967295']}, int_size=32), is_leaf=True, yang_name="total-bytes", rest_name="total-bytes", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='urn:brocade.com:mgmt:brocade-mpls-operational', defining_module='brocade-mpls-operational', yang_type='uint32', is_config=False)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """total_bytes must be of a type compatible with uint32""",
          'defined-type': "uint32",
          'generated-type': """YANGDynClass(base=RestrictedClassType(base_type=long, restriction_dict={'range': ['0..4294967295']}, int_size=32), is_leaf=True, yang_name="total-bytes", rest_name="total-bytes", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='urn:brocade.com:mgmt:brocade-mpls-operational', defining_module='brocade-mpls-operational', yang_type='uint32', is_config=False)""",
        })

    self.__total_bytes = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_total_bytes(self):
    self.__total_bytes = YANGDynClass(base=RestrictedClassType(base_type=long, restriction_dict={'range': ['0..4294967295']}, int_size=32), is_leaf=True, yang_name="total-bytes", rest_name="total-bytes", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='urn:brocade.com:mgmt:brocade-mpls-operational', defining_module='brocade-mpls-operational', yang_type='uint32', is_config=False)


  def _get_total_allocs(self):
    """
    Getter method for total_allocs, mapped from YANG variable /mpls_state/memory/stats/total_allocs (uint32)

    YANG Description: Total allocations
    """
    return self.__total_allocs
      
  def _set_total_allocs(self, v, load=False):
    """
    Setter method for total_allocs, mapped from YANG variable /mpls_state/memory/stats/total_allocs (uint32)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_total_allocs is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_total_allocs() directly.

    YANG Description: Total allocations
    """
    if hasattr(v, "_utype"):
      v = v._utype(v)
    try:
      t = YANGDynClass(v,base=RestrictedClassType(base_type=long, restriction_dict={'range': ['0..4294967295']}, int_size=32), is_leaf=True, yang_name="total-allocs", rest_name="total-allocs", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='urn:brocade.com:mgmt:brocade-mpls-operational', defining_module='brocade-mpls-operational', yang_type='uint32', is_config=False)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """total_allocs must be of a type compatible with uint32""",
          'defined-type': "uint32",
          'generated-type': """YANGDynClass(base=RestrictedClassType(base_type=long, restriction_dict={'range': ['0..4294967295']}, int_size=32), is_leaf=True, yang_name="total-allocs", rest_name="total-allocs", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='urn:brocade.com:mgmt:brocade-mpls-operational', defining_module='brocade-mpls-operational', yang_type='uint32', is_config=False)""",
        })

    self.__total_allocs = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_total_allocs(self):
    self.__total_allocs = YANGDynClass(base=RestrictedClassType(base_type=long, restriction_dict={'range': ['0..4294967295']}, int_size=32), is_leaf=True, yang_name="total-allocs", rest_name="total-allocs", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='urn:brocade.com:mgmt:brocade-mpls-operational', defining_module='brocade-mpls-operational', yang_type='uint32', is_config=False)


  def _get_total_frees(self):
    """
    Getter method for total_frees, mapped from YANG variable /mpls_state/memory/stats/total_frees (uint32)

    YANG Description: Total frees
    """
    return self.__total_frees
      
  def _set_total_frees(self, v, load=False):
    """
    Setter method for total_frees, mapped from YANG variable /mpls_state/memory/stats/total_frees (uint32)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_total_frees is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_total_frees() directly.

    YANG Description: Total frees
    """
    if hasattr(v, "_utype"):
      v = v._utype(v)
    try:
      t = YANGDynClass(v,base=RestrictedClassType(base_type=long, restriction_dict={'range': ['0..4294967295']}, int_size=32), is_leaf=True, yang_name="total-frees", rest_name="total-frees", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='urn:brocade.com:mgmt:brocade-mpls-operational', defining_module='brocade-mpls-operational', yang_type='uint32', is_config=False)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """total_frees must be of a type compatible with uint32""",
          'defined-type': "uint32",
          'generated-type': """YANGDynClass(base=RestrictedClassType(base_type=long, restriction_dict={'range': ['0..4294967295']}, int_size=32), is_leaf=True, yang_name="total-frees", rest_name="total-frees", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='urn:brocade.com:mgmt:brocade-mpls-operational', defining_module='brocade-mpls-operational', yang_type='uint32', is_config=False)""",
        })

    self.__total_frees = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_total_frees(self):
    self.__total_frees = YANGDynClass(base=RestrictedClassType(base_type=long, restriction_dict={'range': ['0..4294967295']}, int_size=32), is_leaf=True, yang_name="total-frees", rest_name="total-frees", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='urn:brocade.com:mgmt:brocade-mpls-operational', defining_module='brocade-mpls-operational', yang_type='uint32', is_config=False)


  def _get_peak_alloc(self):
    """
    Getter method for peak_alloc, mapped from YANG variable /mpls_state/memory/stats/peak_alloc (uint32)

    YANG Description: Peak allocations
    """
    return self.__peak_alloc
      
  def _set_peak_alloc(self, v, load=False):
    """
    Setter method for peak_alloc, mapped from YANG variable /mpls_state/memory/stats/peak_alloc (uint32)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_peak_alloc is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_peak_alloc() directly.

    YANG Description: Peak allocations
    """
    if hasattr(v, "_utype"):
      v = v._utype(v)
    try:
      t = YANGDynClass(v,base=RestrictedClassType(base_type=long, restriction_dict={'range': ['0..4294967295']}, int_size=32), is_leaf=True, yang_name="peak-alloc", rest_name="peak-alloc", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='urn:brocade.com:mgmt:brocade-mpls-operational', defining_module='brocade-mpls-operational', yang_type='uint32', is_config=False)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """peak_alloc must be of a type compatible with uint32""",
          'defined-type': "uint32",
          'generated-type': """YANGDynClass(base=RestrictedClassType(base_type=long, restriction_dict={'range': ['0..4294967295']}, int_size=32), is_leaf=True, yang_name="peak-alloc", rest_name="peak-alloc", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='urn:brocade.com:mgmt:brocade-mpls-operational', defining_module='brocade-mpls-operational', yang_type='uint32', is_config=False)""",
        })

    self.__peak_alloc = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_peak_alloc(self):
    self.__peak_alloc = YANGDynClass(base=RestrictedClassType(base_type=long, restriction_dict={'range': ['0..4294967295']}, int_size=32), is_leaf=True, yang_name="peak-alloc", rest_name="peak-alloc", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='urn:brocade.com:mgmt:brocade-mpls-operational', defining_module='brocade-mpls-operational', yang_type='uint32', is_config=False)


  def _get_alloc_fails(self):
    """
    Getter method for alloc_fails, mapped from YANG variable /mpls_state/memory/stats/alloc_fails (uint32)

    YANG Description: Allocation Fails
    """
    return self.__alloc_fails
      
  def _set_alloc_fails(self, v, load=False):
    """
    Setter method for alloc_fails, mapped from YANG variable /mpls_state/memory/stats/alloc_fails (uint32)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_alloc_fails is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_alloc_fails() directly.

    YANG Description: Allocation Fails
    """
    if hasattr(v, "_utype"):
      v = v._utype(v)
    try:
      t = YANGDynClass(v,base=RestrictedClassType(base_type=long, restriction_dict={'range': ['0..4294967295']}, int_size=32), is_leaf=True, yang_name="alloc-fails", rest_name="alloc-fails", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='urn:brocade.com:mgmt:brocade-mpls-operational', defining_module='brocade-mpls-operational', yang_type='uint32', is_config=False)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """alloc_fails must be of a type compatible with uint32""",
          'defined-type': "uint32",
          'generated-type': """YANGDynClass(base=RestrictedClassType(base_type=long, restriction_dict={'range': ['0..4294967295']}, int_size=32), is_leaf=True, yang_name="alloc-fails", rest_name="alloc-fails", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='urn:brocade.com:mgmt:brocade-mpls-operational', defining_module='brocade-mpls-operational', yang_type='uint32', is_config=False)""",
        })

    self.__alloc_fails = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_alloc_fails(self):
    self.__alloc_fails = YANGDynClass(base=RestrictedClassType(base_type=long, restriction_dict={'range': ['0..4294967295']}, int_size=32), is_leaf=True, yang_name="alloc-fails", rest_name="alloc-fails", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='urn:brocade.com:mgmt:brocade-mpls-operational', defining_module='brocade-mpls-operational', yang_type='uint32', is_config=False)


  def _get_free_fails(self):
    """
    Getter method for free_fails, mapped from YANG variable /mpls_state/memory/stats/free_fails (uint32)

    YANG Description: Free fails
    """
    return self.__free_fails
      
  def _set_free_fails(self, v, load=False):
    """
    Setter method for free_fails, mapped from YANG variable /mpls_state/memory/stats/free_fails (uint32)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_free_fails is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_free_fails() directly.

    YANG Description: Free fails
    """
    if hasattr(v, "_utype"):
      v = v._utype(v)
    try:
      t = YANGDynClass(v,base=RestrictedClassType(base_type=long, restriction_dict={'range': ['0..4294967295']}, int_size=32), is_leaf=True, yang_name="free-fails", rest_name="free-fails", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='urn:brocade.com:mgmt:brocade-mpls-operational', defining_module='brocade-mpls-operational', yang_type='uint32', is_config=False)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """free_fails must be of a type compatible with uint32""",
          'defined-type': "uint32",
          'generated-type': """YANGDynClass(base=RestrictedClassType(base_type=long, restriction_dict={'range': ['0..4294967295']}, int_size=32), is_leaf=True, yang_name="free-fails", rest_name="free-fails", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='urn:brocade.com:mgmt:brocade-mpls-operational', defining_module='brocade-mpls-operational', yang_type='uint32', is_config=False)""",
        })

    self.__free_fails = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_free_fails(self):
    self.__free_fails = YANGDynClass(base=RestrictedClassType(base_type=long, restriction_dict={'range': ['0..4294967295']}, int_size=32), is_leaf=True, yang_name="free-fails", rest_name="free-fails", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='urn:brocade.com:mgmt:brocade-mpls-operational', defining_module='brocade-mpls-operational', yang_type='uint32', is_config=False)

  mem_stats_index = __builtin__.property(_get_mem_stats_index)
  mem_type = __builtin__.property(_get_mem_type)
  num_alloc = __builtin__.property(_get_num_alloc)
  total_bytes = __builtin__.property(_get_total_bytes)
  total_allocs = __builtin__.property(_get_total_allocs)
  total_frees = __builtin__.property(_get_total_frees)
  peak_alloc = __builtin__.property(_get_peak_alloc)
  alloc_fails = __builtin__.property(_get_alloc_fails)
  free_fails = __builtin__.property(_get_free_fails)


  _pyangbind_elements = {'mem_stats_index': mem_stats_index, 'mem_type': mem_type, 'num_alloc': num_alloc, 'total_bytes': total_bytes, 'total_allocs': total_allocs, 'total_frees': total_frees, 'peak_alloc': peak_alloc, 'alloc_fails': alloc_fails, 'free_fails': free_fails, }

