
from operator import attrgetter
import pyangbind.lib.xpathhelper as xpathhelper
from pyangbind.lib.yangtypes import RestrictedPrecisionDecimalType, RestrictedClassType, TypedListType
from pyangbind.lib.yangtypes import YANGBool, YANGListType, YANGDynClass, ReferenceType
from pyangbind.lib.base import PybindBase
from decimal import Decimal
from bitarray import bitarray
import __builtin__
import ipv6_route_entry
class ipv6_routes(PybindBase):
  """
  This class was auto-generated by the PythonClass plugin for PYANG
  from YANG module brocade-isis-operational - based on the path /isis-state/ipv6-routes. Each member element of
  the container is represented as a class variable - with a specific
  YANG type.

  YANG Description: ISIS IPv6 Route Table
  """
  __slots__ = ('_pybind_generated_by', '_path_helper', '_yang_name', '_rest_name', '_extmethods', '__level1_route_count','__level2_route_count','__ecmp_route_count','__ipv6_route_entry',)

  _yang_name = 'ipv6-routes'
  _rest_name = 'ipv6-routes'

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
    self.__level2_route_count = YANGDynClass(base=RestrictedClassType(base_type=long, restriction_dict={'range': ['0..4294967295']}, int_size=32), is_leaf=True, yang_name="level2-route-count", rest_name="level2-route-count", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='urn:brocade.com:mgmt:brocade-isis-operational', defining_module='brocade-isis-operational', yang_type='uint32', is_config=False)
    self.__ecmp_route_count = YANGDynClass(base=RestrictedClassType(base_type=long, restriction_dict={'range': ['0..4294967295']}, int_size=32), is_leaf=True, yang_name="ecmp-route-count", rest_name="ecmp-route-count", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='urn:brocade.com:mgmt:brocade-isis-operational', defining_module='brocade-isis-operational', yang_type='uint32', is_config=False)
    self.__ipv6_route_entry = YANGDynClass(base=YANGListType("ipv6_dest_addr ipv6_prefix_len",ipv6_route_entry.ipv6_route_entry, yang_name="ipv6-route-entry", rest_name="ipv6-route-entry", parent=self, is_container='list', user_ordered=False, path_helper=self._path_helper, yang_keys='ipv6-dest-addr ipv6-prefix-len', extensions={u'tailf-common': {u'callpoint': u'isis-ipv6-route', u'cli-suppress-show-path': None}}), is_container='list', yang_name="ipv6-route-entry", rest_name="ipv6-route-entry", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'callpoint': u'isis-ipv6-route', u'cli-suppress-show-path': None}}, namespace='urn:brocade.com:mgmt:brocade-isis-operational', defining_module='brocade-isis-operational', yang_type='list', is_config=False)
    self.__level1_route_count = YANGDynClass(base=RestrictedClassType(base_type=long, restriction_dict={'range': ['0..4294967295']}, int_size=32), is_leaf=True, yang_name="level1-route-count", rest_name="level1-route-count", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='urn:brocade.com:mgmt:brocade-isis-operational', defining_module='brocade-isis-operational', yang_type='uint32', is_config=False)

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
      return [u'isis-state', u'ipv6-routes']

  def _rest_path(self):
    if hasattr(self, "_parent"):
      if self._rest_name:
        return self._parent._rest_path()+[self._rest_name]
      else:
        return self._parent._rest_path()
    else:
      return [u'isis-state', u'ipv6-routes']

  def _get_level1_route_count(self):
    """
    Getter method for level1_route_count, mapped from YANG variable /isis_state/ipv6_routes/level1_route_count (uint32)

    YANG Description: Number of Level-1 Routes 
    """
    return self.__level1_route_count
      
  def _set_level1_route_count(self, v, load=False):
    """
    Setter method for level1_route_count, mapped from YANG variable /isis_state/ipv6_routes/level1_route_count (uint32)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_level1_route_count is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_level1_route_count() directly.

    YANG Description: Number of Level-1 Routes 
    """
    if hasattr(v, "_utype"):
      v = v._utype(v)
    try:
      t = YANGDynClass(v,base=RestrictedClassType(base_type=long, restriction_dict={'range': ['0..4294967295']}, int_size=32), is_leaf=True, yang_name="level1-route-count", rest_name="level1-route-count", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='urn:brocade.com:mgmt:brocade-isis-operational', defining_module='brocade-isis-operational', yang_type='uint32', is_config=False)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """level1_route_count must be of a type compatible with uint32""",
          'defined-type': "uint32",
          'generated-type': """YANGDynClass(base=RestrictedClassType(base_type=long, restriction_dict={'range': ['0..4294967295']}, int_size=32), is_leaf=True, yang_name="level1-route-count", rest_name="level1-route-count", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='urn:brocade.com:mgmt:brocade-isis-operational', defining_module='brocade-isis-operational', yang_type='uint32', is_config=False)""",
        })

    self.__level1_route_count = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_level1_route_count(self):
    self.__level1_route_count = YANGDynClass(base=RestrictedClassType(base_type=long, restriction_dict={'range': ['0..4294967295']}, int_size=32), is_leaf=True, yang_name="level1-route-count", rest_name="level1-route-count", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='urn:brocade.com:mgmt:brocade-isis-operational', defining_module='brocade-isis-operational', yang_type='uint32', is_config=False)


  def _get_level2_route_count(self):
    """
    Getter method for level2_route_count, mapped from YANG variable /isis_state/ipv6_routes/level2_route_count (uint32)

    YANG Description: Number of Level-1 Routes 
    """
    return self.__level2_route_count
      
  def _set_level2_route_count(self, v, load=False):
    """
    Setter method for level2_route_count, mapped from YANG variable /isis_state/ipv6_routes/level2_route_count (uint32)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_level2_route_count is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_level2_route_count() directly.

    YANG Description: Number of Level-1 Routes 
    """
    if hasattr(v, "_utype"):
      v = v._utype(v)
    try:
      t = YANGDynClass(v,base=RestrictedClassType(base_type=long, restriction_dict={'range': ['0..4294967295']}, int_size=32), is_leaf=True, yang_name="level2-route-count", rest_name="level2-route-count", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='urn:brocade.com:mgmt:brocade-isis-operational', defining_module='brocade-isis-operational', yang_type='uint32', is_config=False)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """level2_route_count must be of a type compatible with uint32""",
          'defined-type': "uint32",
          'generated-type': """YANGDynClass(base=RestrictedClassType(base_type=long, restriction_dict={'range': ['0..4294967295']}, int_size=32), is_leaf=True, yang_name="level2-route-count", rest_name="level2-route-count", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='urn:brocade.com:mgmt:brocade-isis-operational', defining_module='brocade-isis-operational', yang_type='uint32', is_config=False)""",
        })

    self.__level2_route_count = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_level2_route_count(self):
    self.__level2_route_count = YANGDynClass(base=RestrictedClassType(base_type=long, restriction_dict={'range': ['0..4294967295']}, int_size=32), is_leaf=True, yang_name="level2-route-count", rest_name="level2-route-count", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='urn:brocade.com:mgmt:brocade-isis-operational', defining_module='brocade-isis-operational', yang_type='uint32', is_config=False)


  def _get_ecmp_route_count(self):
    """
    Getter method for ecmp_route_count, mapped from YANG variable /isis_state/ipv6_routes/ecmp_route_count (uint32)

    YANG Description: Equal-cost multi-path Routes 
    """
    return self.__ecmp_route_count
      
  def _set_ecmp_route_count(self, v, load=False):
    """
    Setter method for ecmp_route_count, mapped from YANG variable /isis_state/ipv6_routes/ecmp_route_count (uint32)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_ecmp_route_count is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_ecmp_route_count() directly.

    YANG Description: Equal-cost multi-path Routes 
    """
    if hasattr(v, "_utype"):
      v = v._utype(v)
    try:
      t = YANGDynClass(v,base=RestrictedClassType(base_type=long, restriction_dict={'range': ['0..4294967295']}, int_size=32), is_leaf=True, yang_name="ecmp-route-count", rest_name="ecmp-route-count", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='urn:brocade.com:mgmt:brocade-isis-operational', defining_module='brocade-isis-operational', yang_type='uint32', is_config=False)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """ecmp_route_count must be of a type compatible with uint32""",
          'defined-type': "uint32",
          'generated-type': """YANGDynClass(base=RestrictedClassType(base_type=long, restriction_dict={'range': ['0..4294967295']}, int_size=32), is_leaf=True, yang_name="ecmp-route-count", rest_name="ecmp-route-count", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='urn:brocade.com:mgmt:brocade-isis-operational', defining_module='brocade-isis-operational', yang_type='uint32', is_config=False)""",
        })

    self.__ecmp_route_count = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_ecmp_route_count(self):
    self.__ecmp_route_count = YANGDynClass(base=RestrictedClassType(base_type=long, restriction_dict={'range': ['0..4294967295']}, int_size=32), is_leaf=True, yang_name="ecmp-route-count", rest_name="ecmp-route-count", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='urn:brocade.com:mgmt:brocade-isis-operational', defining_module='brocade-isis-operational', yang_type='uint32', is_config=False)


  def _get_ipv6_route_entry(self):
    """
    Getter method for ipv6_route_entry, mapped from YANG variable /isis_state/ipv6_routes/ipv6_route_entry (list)

    YANG Description: ISIS IPv6 Route Entry
    """
    return self.__ipv6_route_entry
      
  def _set_ipv6_route_entry(self, v, load=False):
    """
    Setter method for ipv6_route_entry, mapped from YANG variable /isis_state/ipv6_routes/ipv6_route_entry (list)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_ipv6_route_entry is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_ipv6_route_entry() directly.

    YANG Description: ISIS IPv6 Route Entry
    """
    if hasattr(v, "_utype"):
      v = v._utype(v)
    try:
      t = YANGDynClass(v,base=YANGListType("ipv6_dest_addr ipv6_prefix_len",ipv6_route_entry.ipv6_route_entry, yang_name="ipv6-route-entry", rest_name="ipv6-route-entry", parent=self, is_container='list', user_ordered=False, path_helper=self._path_helper, yang_keys='ipv6-dest-addr ipv6-prefix-len', extensions={u'tailf-common': {u'callpoint': u'isis-ipv6-route', u'cli-suppress-show-path': None}}), is_container='list', yang_name="ipv6-route-entry", rest_name="ipv6-route-entry", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'callpoint': u'isis-ipv6-route', u'cli-suppress-show-path': None}}, namespace='urn:brocade.com:mgmt:brocade-isis-operational', defining_module='brocade-isis-operational', yang_type='list', is_config=False)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """ipv6_route_entry must be of a type compatible with list""",
          'defined-type': "list",
          'generated-type': """YANGDynClass(base=YANGListType("ipv6_dest_addr ipv6_prefix_len",ipv6_route_entry.ipv6_route_entry, yang_name="ipv6-route-entry", rest_name="ipv6-route-entry", parent=self, is_container='list', user_ordered=False, path_helper=self._path_helper, yang_keys='ipv6-dest-addr ipv6-prefix-len', extensions={u'tailf-common': {u'callpoint': u'isis-ipv6-route', u'cli-suppress-show-path': None}}), is_container='list', yang_name="ipv6-route-entry", rest_name="ipv6-route-entry", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'callpoint': u'isis-ipv6-route', u'cli-suppress-show-path': None}}, namespace='urn:brocade.com:mgmt:brocade-isis-operational', defining_module='brocade-isis-operational', yang_type='list', is_config=False)""",
        })

    self.__ipv6_route_entry = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_ipv6_route_entry(self):
    self.__ipv6_route_entry = YANGDynClass(base=YANGListType("ipv6_dest_addr ipv6_prefix_len",ipv6_route_entry.ipv6_route_entry, yang_name="ipv6-route-entry", rest_name="ipv6-route-entry", parent=self, is_container='list', user_ordered=False, path_helper=self._path_helper, yang_keys='ipv6-dest-addr ipv6-prefix-len', extensions={u'tailf-common': {u'callpoint': u'isis-ipv6-route', u'cli-suppress-show-path': None}}), is_container='list', yang_name="ipv6-route-entry", rest_name="ipv6-route-entry", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'callpoint': u'isis-ipv6-route', u'cli-suppress-show-path': None}}, namespace='urn:brocade.com:mgmt:brocade-isis-operational', defining_module='brocade-isis-operational', yang_type='list', is_config=False)

  level1_route_count = __builtin__.property(_get_level1_route_count)
  level2_route_count = __builtin__.property(_get_level2_route_count)
  ecmp_route_count = __builtin__.property(_get_ecmp_route_count)
  ipv6_route_entry = __builtin__.property(_get_ipv6_route_entry)


  _pyangbind_elements = {'level1_route_count': level1_route_count, 'level2_route_count': level2_route_count, 'ecmp_route_count': ecmp_route_count, 'ipv6_route_entry': ipv6_route_entry, }


