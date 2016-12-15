
from operator import attrgetter
import pyangbind.lib.xpathhelper as xpathhelper
from pyangbind.lib.yangtypes import RestrictedPrecisionDecimalType, RestrictedClassType, TypedListType
from pyangbind.lib.yangtypes import YANGBool, YANGListType, YANGDynClass, ReferenceType
from pyangbind.lib.base import PybindBase
from decimal import Decimal
from bitarray import bitarray
import __builtin__
import sub_pools
class pools(PybindBase):
  """
  This class was auto-generated by the PythonClass plugin for PYANG
  from YANG module brocade-mpls-operational - based on the path /mpls-state/memory/pools. Each member element of
  the container is represented as a class variable - with a specific
  YANG type.

  YANG Description: Memory pools
  """
  __slots__ = ('_pybind_generated_by', '_path_helper', '_yang_name', '_rest_name', '_extmethods', '__pool_index','__sub_pools',)

  _yang_name = 'pools'
  _rest_name = 'pools'

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
    self.__pool_index = YANGDynClass(base=RestrictedClassType(base_type=long, restriction_dict={'range': ['0..4294967295']}, int_size=32), is_leaf=True, yang_name="pool-index", rest_name="pool-index", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, is_keyval=True, namespace='urn:brocade.com:mgmt:brocade-mpls-operational', defining_module='brocade-mpls-operational', yang_type='uint32', is_config=False)
    self.__sub_pools = YANGDynClass(base=YANGListType("sub_pool_index",sub_pools.sub_pools, yang_name="sub-pools", rest_name="sub-pools", parent=self, is_container='list', user_ordered=False, path_helper=self._path_helper, yang_keys='sub-pool-index', extensions={u'tailf-common': {u'callpoint': u'mpls-mem-sub-pools', u'cli-suppress-show-path': None}}), is_container='list', yang_name="sub-pools", rest_name="sub-pools", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'callpoint': u'mpls-mem-sub-pools', u'cli-suppress-show-path': None}}, namespace='urn:brocade.com:mgmt:brocade-mpls-operational', defining_module='brocade-mpls-operational', yang_type='list', is_config=False)

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
      return [u'mpls-state', u'memory', u'pools']

  def _rest_path(self):
    if hasattr(self, "_parent"):
      if self._rest_name:
        return self._parent._rest_path()+[self._rest_name]
      else:
        return self._parent._rest_path()
    else:
      return [u'mpls-state', u'memory', u'pools']

  def _get_pool_index(self):
    """
    Getter method for pool_index, mapped from YANG variable /mpls_state/memory/pools/pool_index (uint32)

    YANG Description: Pool index
    """
    return self.__pool_index
      
  def _set_pool_index(self, v, load=False):
    """
    Setter method for pool_index, mapped from YANG variable /mpls_state/memory/pools/pool_index (uint32)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_pool_index is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_pool_index() directly.

    YANG Description: Pool index
    """
    parent = getattr(self, "_parent", None)
    if parent is not None and load is False:
      raise AttributeError("Cannot set keys directly when" +
                             " within an instantiated list")

    if hasattr(v, "_utype"):
      v = v._utype(v)
    try:
      t = YANGDynClass(v,base=RestrictedClassType(base_type=long, restriction_dict={'range': ['0..4294967295']}, int_size=32), is_leaf=True, yang_name="pool-index", rest_name="pool-index", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, is_keyval=True, namespace='urn:brocade.com:mgmt:brocade-mpls-operational', defining_module='brocade-mpls-operational', yang_type='uint32', is_config=False)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """pool_index must be of a type compatible with uint32""",
          'defined-type': "uint32",
          'generated-type': """YANGDynClass(base=RestrictedClassType(base_type=long, restriction_dict={'range': ['0..4294967295']}, int_size=32), is_leaf=True, yang_name="pool-index", rest_name="pool-index", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, is_keyval=True, namespace='urn:brocade.com:mgmt:brocade-mpls-operational', defining_module='brocade-mpls-operational', yang_type='uint32', is_config=False)""",
        })

    self.__pool_index = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_pool_index(self):
    self.__pool_index = YANGDynClass(base=RestrictedClassType(base_type=long, restriction_dict={'range': ['0..4294967295']}, int_size=32), is_leaf=True, yang_name="pool-index", rest_name="pool-index", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, is_keyval=True, namespace='urn:brocade.com:mgmt:brocade-mpls-operational', defining_module='brocade-mpls-operational', yang_type='uint32', is_config=False)


  def _get_sub_pools(self):
    """
    Getter method for sub_pools, mapped from YANG variable /mpls_state/memory/pools/sub_pools (list)

    YANG Description: Memory sub pools
    """
    return self.__sub_pools
      
  def _set_sub_pools(self, v, load=False):
    """
    Setter method for sub_pools, mapped from YANG variable /mpls_state/memory/pools/sub_pools (list)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_sub_pools is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_sub_pools() directly.

    YANG Description: Memory sub pools
    """
    if hasattr(v, "_utype"):
      v = v._utype(v)
    try:
      t = YANGDynClass(v,base=YANGListType("sub_pool_index",sub_pools.sub_pools, yang_name="sub-pools", rest_name="sub-pools", parent=self, is_container='list', user_ordered=False, path_helper=self._path_helper, yang_keys='sub-pool-index', extensions={u'tailf-common': {u'callpoint': u'mpls-mem-sub-pools', u'cli-suppress-show-path': None}}), is_container='list', yang_name="sub-pools", rest_name="sub-pools", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'callpoint': u'mpls-mem-sub-pools', u'cli-suppress-show-path': None}}, namespace='urn:brocade.com:mgmt:brocade-mpls-operational', defining_module='brocade-mpls-operational', yang_type='list', is_config=False)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """sub_pools must be of a type compatible with list""",
          'defined-type': "list",
          'generated-type': """YANGDynClass(base=YANGListType("sub_pool_index",sub_pools.sub_pools, yang_name="sub-pools", rest_name="sub-pools", parent=self, is_container='list', user_ordered=False, path_helper=self._path_helper, yang_keys='sub-pool-index', extensions={u'tailf-common': {u'callpoint': u'mpls-mem-sub-pools', u'cli-suppress-show-path': None}}), is_container='list', yang_name="sub-pools", rest_name="sub-pools", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'callpoint': u'mpls-mem-sub-pools', u'cli-suppress-show-path': None}}, namespace='urn:brocade.com:mgmt:brocade-mpls-operational', defining_module='brocade-mpls-operational', yang_type='list', is_config=False)""",
        })

    self.__sub_pools = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_sub_pools(self):
    self.__sub_pools = YANGDynClass(base=YANGListType("sub_pool_index",sub_pools.sub_pools, yang_name="sub-pools", rest_name="sub-pools", parent=self, is_container='list', user_ordered=False, path_helper=self._path_helper, yang_keys='sub-pool-index', extensions={u'tailf-common': {u'callpoint': u'mpls-mem-sub-pools', u'cli-suppress-show-path': None}}), is_container='list', yang_name="sub-pools", rest_name="sub-pools", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'callpoint': u'mpls-mem-sub-pools', u'cli-suppress-show-path': None}}, namespace='urn:brocade.com:mgmt:brocade-mpls-operational', defining_module='brocade-mpls-operational', yang_type='list', is_config=False)

  pool_index = __builtin__.property(_get_pool_index)
  sub_pools = __builtin__.property(_get_sub_pools)


  _pyangbind_elements = {'pool_index': pool_index, 'sub_pools': sub_pools, }


