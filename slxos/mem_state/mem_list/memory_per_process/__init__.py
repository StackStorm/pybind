
from operator import attrgetter
import pyangbind.lib.xpathhelper as xpathhelper
from pyangbind.lib.yangtypes import RestrictedPrecisionDecimalType, RestrictedClassType, TypedListType
from pyangbind.lib.yangtypes import YANGBool, YANGListType, YANGDynClass, ReferenceType
from pyangbind.lib.base import PybindBase
from decimal import Decimal
from bitarray import bitarray
import __builtin__
class memory_per_process(PybindBase):
  """
  This class was auto-generated by the PythonClass plugin for PYANG
  from YANG module brocade-RAS-operational - based on the path /mem-state/mem-list/memory-per-process. Each member element of
  the container is represented as a class variable - with a specific
  YANG type.

  YANG Description:  Memory utilization per process 
  """
  __slots__ = ('_pybind_generated_by', '_path_helper', '_yang_name', '_rest_name', '_extmethods', '__memory_process_id','__memory_process_name','__memory_utilized','__memory_utilized_vsize','__memory_utilized_rss','__memory_utilized_pss',)

  _yang_name = 'memory-per-process'
  _rest_name = 'memory-per-process'

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
    self.__memory_utilized = YANGDynClass(base=RestrictedPrecisionDecimalType(precision=2), is_leaf=True, yang_name="memory-utilized", rest_name="memory-utilized", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='urn:brocade.com:mgmt:brocade-RAS-operational', defining_module='brocade-RAS-operational', yang_type='decimal64', is_config=False)
    self.__memory_utilized_vsize = YANGDynClass(base=RestrictedClassType(base_type=long, restriction_dict={'range': ['0..4294967295']}, int_size=32), is_leaf=True, yang_name="memory-utilized-vsize", rest_name="memory-utilized-vsize", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='urn:brocade.com:mgmt:brocade-RAS-operational', defining_module='brocade-RAS-operational', yang_type='uint32', is_config=False)
    self.__memory_process_name = YANGDynClass(base=unicode, is_leaf=True, yang_name="memory-process-name", rest_name="memory-process-name", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='urn:brocade.com:mgmt:brocade-RAS-operational', defining_module='brocade-RAS-operational', yang_type='string', is_config=False)
    self.__memory_process_id = YANGDynClass(base=RestrictedClassType(base_type=long, restriction_dict={'range': ['0..4294967295']}, int_size=32), is_leaf=True, yang_name="memory-process-id", rest_name="memory-process-id", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, is_keyval=True, namespace='urn:brocade.com:mgmt:brocade-RAS-operational', defining_module='brocade-RAS-operational', yang_type='uint32', is_config=False)
    self.__memory_utilized_pss = YANGDynClass(base=RestrictedClassType(base_type=long, restriction_dict={'range': ['0..4294967295']}, int_size=32), is_leaf=True, yang_name="memory-utilized-pss", rest_name="memory-utilized-pss", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='urn:brocade.com:mgmt:brocade-RAS-operational', defining_module='brocade-RAS-operational', yang_type='uint32', is_config=False)
    self.__memory_utilized_rss = YANGDynClass(base=RestrictedClassType(base_type=long, restriction_dict={'range': ['0..4294967295']}, int_size=32), is_leaf=True, yang_name="memory-utilized-rss", rest_name="memory-utilized-rss", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='urn:brocade.com:mgmt:brocade-RAS-operational', defining_module='brocade-RAS-operational', yang_type='uint32', is_config=False)

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
      return [u'mem-state', u'mem-list', u'memory-per-process']

  def _rest_path(self):
    if hasattr(self, "_parent"):
      if self._rest_name:
        return self._parent._rest_path()+[self._rest_name]
      else:
        return self._parent._rest_path()
    else:
      return [u'mem-state', u'mem-list', u'memory-per-process']

  def _get_memory_process_id(self):
    """
    Getter method for memory_process_id, mapped from YANG variable /mem_state/mem_list/memory_per_process/memory_process_id (uint32)

    YANG Description: Process ID
    """
    return self.__memory_process_id
      
  def _set_memory_process_id(self, v, load=False):
    """
    Setter method for memory_process_id, mapped from YANG variable /mem_state/mem_list/memory_per_process/memory_process_id (uint32)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_memory_process_id is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_memory_process_id() directly.

    YANG Description: Process ID
    """
    parent = getattr(self, "_parent", None)
    if parent is not None and load is False:
      raise AttributeError("Cannot set keys directly when" +
                             " within an instantiated list")

    if hasattr(v, "_utype"):
      v = v._utype(v)
    try:
      t = YANGDynClass(v,base=RestrictedClassType(base_type=long, restriction_dict={'range': ['0..4294967295']}, int_size=32), is_leaf=True, yang_name="memory-process-id", rest_name="memory-process-id", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, is_keyval=True, namespace='urn:brocade.com:mgmt:brocade-RAS-operational', defining_module='brocade-RAS-operational', yang_type='uint32', is_config=False)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """memory_process_id must be of a type compatible with uint32""",
          'defined-type': "uint32",
          'generated-type': """YANGDynClass(base=RestrictedClassType(base_type=long, restriction_dict={'range': ['0..4294967295']}, int_size=32), is_leaf=True, yang_name="memory-process-id", rest_name="memory-process-id", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, is_keyval=True, namespace='urn:brocade.com:mgmt:brocade-RAS-operational', defining_module='brocade-RAS-operational', yang_type='uint32', is_config=False)""",
        })

    self.__memory_process_id = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_memory_process_id(self):
    self.__memory_process_id = YANGDynClass(base=RestrictedClassType(base_type=long, restriction_dict={'range': ['0..4294967295']}, int_size=32), is_leaf=True, yang_name="memory-process-id", rest_name="memory-process-id", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, is_keyval=True, namespace='urn:brocade.com:mgmt:brocade-RAS-operational', defining_module='brocade-RAS-operational', yang_type='uint32', is_config=False)


  def _get_memory_process_name(self):
    """
    Getter method for memory_process_name, mapped from YANG variable /mem_state/mem_list/memory_per_process/memory_process_name (string)

    YANG Description: Process name
    """
    return self.__memory_process_name
      
  def _set_memory_process_name(self, v, load=False):
    """
    Setter method for memory_process_name, mapped from YANG variable /mem_state/mem_list/memory_per_process/memory_process_name (string)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_memory_process_name is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_memory_process_name() directly.

    YANG Description: Process name
    """
    if hasattr(v, "_utype"):
      v = v._utype(v)
    try:
      t = YANGDynClass(v,base=unicode, is_leaf=True, yang_name="memory-process-name", rest_name="memory-process-name", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='urn:brocade.com:mgmt:brocade-RAS-operational', defining_module='brocade-RAS-operational', yang_type='string', is_config=False)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """memory_process_name must be of a type compatible with string""",
          'defined-type': "string",
          'generated-type': """YANGDynClass(base=unicode, is_leaf=True, yang_name="memory-process-name", rest_name="memory-process-name", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='urn:brocade.com:mgmt:brocade-RAS-operational', defining_module='brocade-RAS-operational', yang_type='string', is_config=False)""",
        })

    self.__memory_process_name = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_memory_process_name(self):
    self.__memory_process_name = YANGDynClass(base=unicode, is_leaf=True, yang_name="memory-process-name", rest_name="memory-process-name", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='urn:brocade.com:mgmt:brocade-RAS-operational', defining_module='brocade-RAS-operational', yang_type='string', is_config=False)


  def _get_memory_utilized(self):
    """
    Getter method for memory_utilized, mapped from YANG variable /mem_state/mem_list/memory_per_process/memory_utilized (decimal64)

    YANG Description: Percentage of memory used by the process
    """
    return self.__memory_utilized
      
  def _set_memory_utilized(self, v, load=False):
    """
    Setter method for memory_utilized, mapped from YANG variable /mem_state/mem_list/memory_per_process/memory_utilized (decimal64)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_memory_utilized is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_memory_utilized() directly.

    YANG Description: Percentage of memory used by the process
    """
    if hasattr(v, "_utype"):
      v = v._utype(v)
    try:
      t = YANGDynClass(v,base=RestrictedPrecisionDecimalType(precision=2), is_leaf=True, yang_name="memory-utilized", rest_name="memory-utilized", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='urn:brocade.com:mgmt:brocade-RAS-operational', defining_module='brocade-RAS-operational', yang_type='decimal64', is_config=False)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """memory_utilized must be of a type compatible with decimal64""",
          'defined-type': "decimal64",
          'generated-type': """YANGDynClass(base=RestrictedPrecisionDecimalType(precision=2), is_leaf=True, yang_name="memory-utilized", rest_name="memory-utilized", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='urn:brocade.com:mgmt:brocade-RAS-operational', defining_module='brocade-RAS-operational', yang_type='decimal64', is_config=False)""",
        })

    self.__memory_utilized = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_memory_utilized(self):
    self.__memory_utilized = YANGDynClass(base=RestrictedPrecisionDecimalType(precision=2), is_leaf=True, yang_name="memory-utilized", rest_name="memory-utilized", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='urn:brocade.com:mgmt:brocade-RAS-operational', defining_module='brocade-RAS-operational', yang_type='decimal64', is_config=False)


  def _get_memory_utilized_vsize(self):
    """
    Getter method for memory_utilized_vsize, mapped from YANG variable /mem_state/mem_list/memory_per_process/memory_utilized_vsize (uint32)

    YANG Description: Virtual set size of the process in KB
    """
    return self.__memory_utilized_vsize
      
  def _set_memory_utilized_vsize(self, v, load=False):
    """
    Setter method for memory_utilized_vsize, mapped from YANG variable /mem_state/mem_list/memory_per_process/memory_utilized_vsize (uint32)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_memory_utilized_vsize is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_memory_utilized_vsize() directly.

    YANG Description: Virtual set size of the process in KB
    """
    if hasattr(v, "_utype"):
      v = v._utype(v)
    try:
      t = YANGDynClass(v,base=RestrictedClassType(base_type=long, restriction_dict={'range': ['0..4294967295']}, int_size=32), is_leaf=True, yang_name="memory-utilized-vsize", rest_name="memory-utilized-vsize", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='urn:brocade.com:mgmt:brocade-RAS-operational', defining_module='brocade-RAS-operational', yang_type='uint32', is_config=False)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """memory_utilized_vsize must be of a type compatible with uint32""",
          'defined-type': "uint32",
          'generated-type': """YANGDynClass(base=RestrictedClassType(base_type=long, restriction_dict={'range': ['0..4294967295']}, int_size=32), is_leaf=True, yang_name="memory-utilized-vsize", rest_name="memory-utilized-vsize", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='urn:brocade.com:mgmt:brocade-RAS-operational', defining_module='brocade-RAS-operational', yang_type='uint32', is_config=False)""",
        })

    self.__memory_utilized_vsize = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_memory_utilized_vsize(self):
    self.__memory_utilized_vsize = YANGDynClass(base=RestrictedClassType(base_type=long, restriction_dict={'range': ['0..4294967295']}, int_size=32), is_leaf=True, yang_name="memory-utilized-vsize", rest_name="memory-utilized-vsize", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='urn:brocade.com:mgmt:brocade-RAS-operational', defining_module='brocade-RAS-operational', yang_type='uint32', is_config=False)


  def _get_memory_utilized_rss(self):
    """
    Getter method for memory_utilized_rss, mapped from YANG variable /mem_state/mem_list/memory_per_process/memory_utilized_rss (uint32)

    YANG Description: Residual set size of the process in KB
    """
    return self.__memory_utilized_rss
      
  def _set_memory_utilized_rss(self, v, load=False):
    """
    Setter method for memory_utilized_rss, mapped from YANG variable /mem_state/mem_list/memory_per_process/memory_utilized_rss (uint32)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_memory_utilized_rss is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_memory_utilized_rss() directly.

    YANG Description: Residual set size of the process in KB
    """
    if hasattr(v, "_utype"):
      v = v._utype(v)
    try:
      t = YANGDynClass(v,base=RestrictedClassType(base_type=long, restriction_dict={'range': ['0..4294967295']}, int_size=32), is_leaf=True, yang_name="memory-utilized-rss", rest_name="memory-utilized-rss", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='urn:brocade.com:mgmt:brocade-RAS-operational', defining_module='brocade-RAS-operational', yang_type='uint32', is_config=False)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """memory_utilized_rss must be of a type compatible with uint32""",
          'defined-type': "uint32",
          'generated-type': """YANGDynClass(base=RestrictedClassType(base_type=long, restriction_dict={'range': ['0..4294967295']}, int_size=32), is_leaf=True, yang_name="memory-utilized-rss", rest_name="memory-utilized-rss", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='urn:brocade.com:mgmt:brocade-RAS-operational', defining_module='brocade-RAS-operational', yang_type='uint32', is_config=False)""",
        })

    self.__memory_utilized_rss = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_memory_utilized_rss(self):
    self.__memory_utilized_rss = YANGDynClass(base=RestrictedClassType(base_type=long, restriction_dict={'range': ['0..4294967295']}, int_size=32), is_leaf=True, yang_name="memory-utilized-rss", rest_name="memory-utilized-rss", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='urn:brocade.com:mgmt:brocade-RAS-operational', defining_module='brocade-RAS-operational', yang_type='uint32', is_config=False)


  def _get_memory_utilized_pss(self):
    """
    Getter method for memory_utilized_pss, mapped from YANG variable /mem_state/mem_list/memory_per_process/memory_utilized_pss (uint32)

    YANG Description: Proportional set size of the process in KB
    """
    return self.__memory_utilized_pss
      
  def _set_memory_utilized_pss(self, v, load=False):
    """
    Setter method for memory_utilized_pss, mapped from YANG variable /mem_state/mem_list/memory_per_process/memory_utilized_pss (uint32)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_memory_utilized_pss is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_memory_utilized_pss() directly.

    YANG Description: Proportional set size of the process in KB
    """
    if hasattr(v, "_utype"):
      v = v._utype(v)
    try:
      t = YANGDynClass(v,base=RestrictedClassType(base_type=long, restriction_dict={'range': ['0..4294967295']}, int_size=32), is_leaf=True, yang_name="memory-utilized-pss", rest_name="memory-utilized-pss", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='urn:brocade.com:mgmt:brocade-RAS-operational', defining_module='brocade-RAS-operational', yang_type='uint32', is_config=False)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """memory_utilized_pss must be of a type compatible with uint32""",
          'defined-type': "uint32",
          'generated-type': """YANGDynClass(base=RestrictedClassType(base_type=long, restriction_dict={'range': ['0..4294967295']}, int_size=32), is_leaf=True, yang_name="memory-utilized-pss", rest_name="memory-utilized-pss", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='urn:brocade.com:mgmt:brocade-RAS-operational', defining_module='brocade-RAS-operational', yang_type='uint32', is_config=False)""",
        })

    self.__memory_utilized_pss = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_memory_utilized_pss(self):
    self.__memory_utilized_pss = YANGDynClass(base=RestrictedClassType(base_type=long, restriction_dict={'range': ['0..4294967295']}, int_size=32), is_leaf=True, yang_name="memory-utilized-pss", rest_name="memory-utilized-pss", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='urn:brocade.com:mgmt:brocade-RAS-operational', defining_module='brocade-RAS-operational', yang_type='uint32', is_config=False)

  memory_process_id = __builtin__.property(_get_memory_process_id)
  memory_process_name = __builtin__.property(_get_memory_process_name)
  memory_utilized = __builtin__.property(_get_memory_utilized)
  memory_utilized_vsize = __builtin__.property(_get_memory_utilized_vsize)
  memory_utilized_rss = __builtin__.property(_get_memory_utilized_rss)
  memory_utilized_pss = __builtin__.property(_get_memory_utilized_pss)


  _pyangbind_elements = {'memory_process_id': memory_process_id, 'memory_process_name': memory_process_name, 'memory_utilized': memory_utilized, 'memory_utilized_vsize': memory_utilized_vsize, 'memory_utilized_rss': memory_utilized_rss, 'memory_utilized_pss': memory_utilized_pss, }


