
from operator import attrgetter
import pyangbind.lib.xpathhelper as xpathhelper
from pyangbind.lib.yangtypes import RestrictedPrecisionDecimalType, RestrictedClassType, TypedListType
from pyangbind.lib.yangtypes import YANGBool, YANGListType, YANGDynClass, ReferenceType
from pyangbind.lib.base import PybindBase
from decimal import Decimal
from bitarray import bitarray
import __builtin__
class router_id_map(PybindBase):
  """
  This class was auto-generated by the PythonClass plugin for PYANG
  from YANG module brocade-mpls-operational - based on the path /mpls-state/te/router-id-map. Each member element of
  the container is represented as a class variable - with a specific
  YANG type.

  YANG Description: MPLS TE Router Id mapping brief Operational Information
  """
  __slots__ = ('_pybind_generated_by', '_path_helper', '_yang_name', '_extmethods', '__ip_address','__router_id','__resolved','__igp_isis','__igp_ospf','__isis_level','__ospf_area','__origin_ted','__origin_path','__origin_lsp','__origin_other',)

  _yang_name = 'router-id-map'

  _pybind_generated_by = 'container'

  def __init__(self, *args, **kwargs):

    helper = kwargs.pop("path_helper", None)
    if helper is False:
      self._path_helper = False
    elif helper is not None and isinstance(helper, xpathhelper.YANGPathHelper):
      self._path_helper = helper
    elif hasattr(self, "_parent"):
      helper = getattr(self._parent, "_path_helper", False)
      self._path_helper = helper
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
    self.__router_id = YANGDynClass(base=RestrictedClassType(base_type=unicode, restriction_dict={'pattern': u'(([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])\\.){3}([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])(%[\\p{N}\\p{L}]+)?'}), is_leaf=True, yang_name="router-id", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='urn:brocade.com:mgmt:brocade-mpls-operational', defining_module='brocade-mpls-operational', yang_type='inet:ipv4-address', is_config=False)
    self.__resolved = YANGDynClass(base=YANGBool, is_leaf=True, yang_name="resolved", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='urn:brocade.com:mgmt:brocade-mpls-operational', defining_module='brocade-mpls-operational', yang_type='boolean', is_config=False)
    self.__igp_ospf = YANGDynClass(base=YANGBool, is_leaf=True, yang_name="igp-ospf", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='urn:brocade.com:mgmt:brocade-mpls-operational', defining_module='brocade-mpls-operational', yang_type='boolean', is_config=False)
    self.__origin_path = YANGDynClass(base=RestrictedClassType(base_type=long, restriction_dict={'range': ['0..4294967295']}, int_size=32), is_leaf=True, yang_name="origin-path", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='urn:brocade.com:mgmt:brocade-mpls-operational', defining_module='brocade-mpls-operational', yang_type='uint32', is_config=False)
    self.__origin_lsp = YANGDynClass(base=RestrictedClassType(base_type=long, restriction_dict={'range': ['0..4294967295']}, int_size=32), is_leaf=True, yang_name="origin-lsp", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='urn:brocade.com:mgmt:brocade-mpls-operational', defining_module='brocade-mpls-operational', yang_type='uint32', is_config=False)
    self.__isis_level = YANGDynClass(base=RestrictedClassType(base_type=long, restriction_dict={'range': ['0..4294967295']}, int_size=32), is_leaf=True, yang_name="isis-level", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='urn:brocade.com:mgmt:brocade-mpls-operational', defining_module='brocade-mpls-operational', yang_type='uint32', is_config=False)
    self.__ospf_area = YANGDynClass(base=RestrictedClassType(base_type=unicode, restriction_dict={'pattern': u'(([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])\\.){3}([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])(%[\\p{N}\\p{L}]+)?'}), is_leaf=True, yang_name="ospf-area", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='urn:brocade.com:mgmt:brocade-mpls-operational', defining_module='brocade-mpls-operational', yang_type='inet:ipv4-address', is_config=False)
    self.__origin_ted = YANGDynClass(base=YANGBool, is_leaf=True, yang_name="origin-ted", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='urn:brocade.com:mgmt:brocade-mpls-operational', defining_module='brocade-mpls-operational', yang_type='boolean', is_config=False)
    self.__igp_isis = YANGDynClass(base=YANGBool, is_leaf=True, yang_name="igp-isis", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='urn:brocade.com:mgmt:brocade-mpls-operational', defining_module='brocade-mpls-operational', yang_type='boolean', is_config=False)
    self.__ip_address = YANGDynClass(base=RestrictedClassType(base_type=unicode, restriction_dict={'pattern': u'(([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])\\.){3}([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])(%[\\p{N}\\p{L}]+)?'}), is_leaf=True, yang_name="ip-address", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, is_keyval=True, namespace='urn:brocade.com:mgmt:brocade-mpls-operational', defining_module='brocade-mpls-operational', yang_type='inet:ipv4-address', is_config=False)
    self.__origin_other = YANGDynClass(base=YANGBool, is_leaf=True, yang_name="origin-other", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='urn:brocade.com:mgmt:brocade-mpls-operational', defining_module='brocade-mpls-operational', yang_type='boolean', is_config=False)

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
      return [u'mpls-state', u'te', u'router-id-map']

  def _rest_path(self):
    if hasattr(self, "_supplied_register_path"):
      return [self._supplied_register_path]
    if hasattr(self, "_parent"):
      return self._parent._rest_path()+[self._yang_name]
    else:
      return [u'mpls-state', u'te', u'router-id-map']

  def _get_ip_address(self):
    """
    Getter method for ip_address, mapped from YANG variable /mpls_state/te/router_id_map/ip_address (inet:ipv4-address)

    YANG Description: IP Address
    """
    return self.__ip_address
      
  def _set_ip_address(self, v, load=False):
    """
    Setter method for ip_address, mapped from YANG variable /mpls_state/te/router_id_map/ip_address (inet:ipv4-address)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_ip_address is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_ip_address() directly.

    YANG Description: IP Address
    """
    parent = getattr(self, "_parent", None)
    if parent is not None and load is False:
      raise AttributeError("Cannot set keys directly when" +
                             " within an instantiated list")

    try:
      t = YANGDynClass(v,base=RestrictedClassType(base_type=unicode, restriction_dict={'pattern': u'(([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])\\.){3}([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])(%[\\p{N}\\p{L}]+)?'}), is_leaf=True, yang_name="ip-address", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, is_keyval=True, namespace='urn:brocade.com:mgmt:brocade-mpls-operational', defining_module='brocade-mpls-operational', yang_type='inet:ipv4-address', is_config=False)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """ip_address must be of a type compatible with inet:ipv4-address""",
          'defined-type': "inet:ipv4-address",
          'generated-type': """YANGDynClass(base=RestrictedClassType(base_type=unicode, restriction_dict={'pattern': u'(([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])\\.){3}([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])(%[\\p{N}\\p{L}]+)?'}), is_leaf=True, yang_name="ip-address", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, is_keyval=True, namespace='urn:brocade.com:mgmt:brocade-mpls-operational', defining_module='brocade-mpls-operational', yang_type='inet:ipv4-address', is_config=False)""",
        })

    self.__ip_address = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_ip_address(self):
    self.__ip_address = YANGDynClass(base=RestrictedClassType(base_type=unicode, restriction_dict={'pattern': u'(([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])\\.){3}([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])(%[\\p{N}\\p{L}]+)?'}), is_leaf=True, yang_name="ip-address", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, is_keyval=True, namespace='urn:brocade.com:mgmt:brocade-mpls-operational', defining_module='brocade-mpls-operational', yang_type='inet:ipv4-address', is_config=False)


  def _get_router_id(self):
    """
    Getter method for router_id, mapped from YANG variable /mpls_state/te/router_id_map/router_id (inet:ipv4-address)

    YANG Description: Router Id
    """
    return self.__router_id
      
  def _set_router_id(self, v, load=False):
    """
    Setter method for router_id, mapped from YANG variable /mpls_state/te/router_id_map/router_id (inet:ipv4-address)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_router_id is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_router_id() directly.

    YANG Description: Router Id
    """
    try:
      t = YANGDynClass(v,base=RestrictedClassType(base_type=unicode, restriction_dict={'pattern': u'(([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])\\.){3}([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])(%[\\p{N}\\p{L}]+)?'}), is_leaf=True, yang_name="router-id", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='urn:brocade.com:mgmt:brocade-mpls-operational', defining_module='brocade-mpls-operational', yang_type='inet:ipv4-address', is_config=False)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """router_id must be of a type compatible with inet:ipv4-address""",
          'defined-type': "inet:ipv4-address",
          'generated-type': """YANGDynClass(base=RestrictedClassType(base_type=unicode, restriction_dict={'pattern': u'(([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])\\.){3}([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])(%[\\p{N}\\p{L}]+)?'}), is_leaf=True, yang_name="router-id", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='urn:brocade.com:mgmt:brocade-mpls-operational', defining_module='brocade-mpls-operational', yang_type='inet:ipv4-address', is_config=False)""",
        })

    self.__router_id = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_router_id(self):
    self.__router_id = YANGDynClass(base=RestrictedClassType(base_type=unicode, restriction_dict={'pattern': u'(([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])\\.){3}([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])(%[\\p{N}\\p{L}]+)?'}), is_leaf=True, yang_name="router-id", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='urn:brocade.com:mgmt:brocade-mpls-operational', defining_module='brocade-mpls-operational', yang_type='inet:ipv4-address', is_config=False)


  def _get_resolved(self):
    """
    Getter method for resolved, mapped from YANG variable /mpls_state/te/router_id_map/resolved (boolean)

    YANG Description: Resolved status
    """
    return self.__resolved
      
  def _set_resolved(self, v, load=False):
    """
    Setter method for resolved, mapped from YANG variable /mpls_state/te/router_id_map/resolved (boolean)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_resolved is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_resolved() directly.

    YANG Description: Resolved status
    """
    try:
      t = YANGDynClass(v,base=YANGBool, is_leaf=True, yang_name="resolved", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='urn:brocade.com:mgmt:brocade-mpls-operational', defining_module='brocade-mpls-operational', yang_type='boolean', is_config=False)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """resolved must be of a type compatible with boolean""",
          'defined-type': "boolean",
          'generated-type': """YANGDynClass(base=YANGBool, is_leaf=True, yang_name="resolved", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='urn:brocade.com:mgmt:brocade-mpls-operational', defining_module='brocade-mpls-operational', yang_type='boolean', is_config=False)""",
        })

    self.__resolved = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_resolved(self):
    self.__resolved = YANGDynClass(base=YANGBool, is_leaf=True, yang_name="resolved", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='urn:brocade.com:mgmt:brocade-mpls-operational', defining_module='brocade-mpls-operational', yang_type='boolean', is_config=False)


  def _get_igp_isis(self):
    """
    Getter method for igp_isis, mapped from YANG variable /mpls_state/te/router_id_map/igp_isis (boolean)

    YANG Description: Resolved by ISIS
    """
    return self.__igp_isis
      
  def _set_igp_isis(self, v, load=False):
    """
    Setter method for igp_isis, mapped from YANG variable /mpls_state/te/router_id_map/igp_isis (boolean)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_igp_isis is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_igp_isis() directly.

    YANG Description: Resolved by ISIS
    """
    try:
      t = YANGDynClass(v,base=YANGBool, is_leaf=True, yang_name="igp-isis", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='urn:brocade.com:mgmt:brocade-mpls-operational', defining_module='brocade-mpls-operational', yang_type='boolean', is_config=False)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """igp_isis must be of a type compatible with boolean""",
          'defined-type': "boolean",
          'generated-type': """YANGDynClass(base=YANGBool, is_leaf=True, yang_name="igp-isis", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='urn:brocade.com:mgmt:brocade-mpls-operational', defining_module='brocade-mpls-operational', yang_type='boolean', is_config=False)""",
        })

    self.__igp_isis = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_igp_isis(self):
    self.__igp_isis = YANGDynClass(base=YANGBool, is_leaf=True, yang_name="igp-isis", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='urn:brocade.com:mgmt:brocade-mpls-operational', defining_module='brocade-mpls-operational', yang_type='boolean', is_config=False)


  def _get_igp_ospf(self):
    """
    Getter method for igp_ospf, mapped from YANG variable /mpls_state/te/router_id_map/igp_ospf (boolean)

    YANG Description: Resolved by OSPF
    """
    return self.__igp_ospf
      
  def _set_igp_ospf(self, v, load=False):
    """
    Setter method for igp_ospf, mapped from YANG variable /mpls_state/te/router_id_map/igp_ospf (boolean)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_igp_ospf is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_igp_ospf() directly.

    YANG Description: Resolved by OSPF
    """
    try:
      t = YANGDynClass(v,base=YANGBool, is_leaf=True, yang_name="igp-ospf", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='urn:brocade.com:mgmt:brocade-mpls-operational', defining_module='brocade-mpls-operational', yang_type='boolean', is_config=False)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """igp_ospf must be of a type compatible with boolean""",
          'defined-type': "boolean",
          'generated-type': """YANGDynClass(base=YANGBool, is_leaf=True, yang_name="igp-ospf", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='urn:brocade.com:mgmt:brocade-mpls-operational', defining_module='brocade-mpls-operational', yang_type='boolean', is_config=False)""",
        })

    self.__igp_ospf = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_igp_ospf(self):
    self.__igp_ospf = YANGDynClass(base=YANGBool, is_leaf=True, yang_name="igp-ospf", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='urn:brocade.com:mgmt:brocade-mpls-operational', defining_module='brocade-mpls-operational', yang_type='boolean', is_config=False)


  def _get_isis_level(self):
    """
    Getter method for isis_level, mapped from YANG variable /mpls_state/te/router_id_map/isis_level (uint32)

    YANG Description: Resolved ISIS Level
    """
    return self.__isis_level
      
  def _set_isis_level(self, v, load=False):
    """
    Setter method for isis_level, mapped from YANG variable /mpls_state/te/router_id_map/isis_level (uint32)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_isis_level is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_isis_level() directly.

    YANG Description: Resolved ISIS Level
    """
    try:
      t = YANGDynClass(v,base=RestrictedClassType(base_type=long, restriction_dict={'range': ['0..4294967295']}, int_size=32), is_leaf=True, yang_name="isis-level", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='urn:brocade.com:mgmt:brocade-mpls-operational', defining_module='brocade-mpls-operational', yang_type='uint32', is_config=False)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """isis_level must be of a type compatible with uint32""",
          'defined-type': "uint32",
          'generated-type': """YANGDynClass(base=RestrictedClassType(base_type=long, restriction_dict={'range': ['0..4294967295']}, int_size=32), is_leaf=True, yang_name="isis-level", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='urn:brocade.com:mgmt:brocade-mpls-operational', defining_module='brocade-mpls-operational', yang_type='uint32', is_config=False)""",
        })

    self.__isis_level = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_isis_level(self):
    self.__isis_level = YANGDynClass(base=RestrictedClassType(base_type=long, restriction_dict={'range': ['0..4294967295']}, int_size=32), is_leaf=True, yang_name="isis-level", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='urn:brocade.com:mgmt:brocade-mpls-operational', defining_module='brocade-mpls-operational', yang_type='uint32', is_config=False)


  def _get_ospf_area(self):
    """
    Getter method for ospf_area, mapped from YANG variable /mpls_state/te/router_id_map/ospf_area (inet:ipv4-address)

    YANG Description: Resolved OSPF area id
    """
    return self.__ospf_area
      
  def _set_ospf_area(self, v, load=False):
    """
    Setter method for ospf_area, mapped from YANG variable /mpls_state/te/router_id_map/ospf_area (inet:ipv4-address)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_ospf_area is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_ospf_area() directly.

    YANG Description: Resolved OSPF area id
    """
    try:
      t = YANGDynClass(v,base=RestrictedClassType(base_type=unicode, restriction_dict={'pattern': u'(([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])\\.){3}([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])(%[\\p{N}\\p{L}]+)?'}), is_leaf=True, yang_name="ospf-area", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='urn:brocade.com:mgmt:brocade-mpls-operational', defining_module='brocade-mpls-operational', yang_type='inet:ipv4-address', is_config=False)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """ospf_area must be of a type compatible with inet:ipv4-address""",
          'defined-type': "inet:ipv4-address",
          'generated-type': """YANGDynClass(base=RestrictedClassType(base_type=unicode, restriction_dict={'pattern': u'(([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])\\.){3}([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])(%[\\p{N}\\p{L}]+)?'}), is_leaf=True, yang_name="ospf-area", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='urn:brocade.com:mgmt:brocade-mpls-operational', defining_module='brocade-mpls-operational', yang_type='inet:ipv4-address', is_config=False)""",
        })

    self.__ospf_area = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_ospf_area(self):
    self.__ospf_area = YANGDynClass(base=RestrictedClassType(base_type=unicode, restriction_dict={'pattern': u'(([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])\\.){3}([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])(%[\\p{N}\\p{L}]+)?'}), is_leaf=True, yang_name="ospf-area", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='urn:brocade.com:mgmt:brocade-mpls-operational', defining_module='brocade-mpls-operational', yang_type='inet:ipv4-address', is_config=False)


  def _get_origin_ted(self):
    """
    Getter method for origin_ted, mapped from YANG variable /mpls_state/te/router_id_map/origin_ted (boolean)

    YANG Description: IP origined from TED
    """
    return self.__origin_ted
      
  def _set_origin_ted(self, v, load=False):
    """
    Setter method for origin_ted, mapped from YANG variable /mpls_state/te/router_id_map/origin_ted (boolean)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_origin_ted is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_origin_ted() directly.

    YANG Description: IP origined from TED
    """
    try:
      t = YANGDynClass(v,base=YANGBool, is_leaf=True, yang_name="origin-ted", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='urn:brocade.com:mgmt:brocade-mpls-operational', defining_module='brocade-mpls-operational', yang_type='boolean', is_config=False)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """origin_ted must be of a type compatible with boolean""",
          'defined-type': "boolean",
          'generated-type': """YANGDynClass(base=YANGBool, is_leaf=True, yang_name="origin-ted", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='urn:brocade.com:mgmt:brocade-mpls-operational', defining_module='brocade-mpls-operational', yang_type='boolean', is_config=False)""",
        })

    self.__origin_ted = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_origin_ted(self):
    self.__origin_ted = YANGDynClass(base=YANGBool, is_leaf=True, yang_name="origin-ted", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='urn:brocade.com:mgmt:brocade-mpls-operational', defining_module='brocade-mpls-operational', yang_type='boolean', is_config=False)


  def _get_origin_path(self):
    """
    Getter method for origin_path, mapped from YANG variable /mpls_state/te/router_id_map/origin_path (uint32)

    YANG Description: IP origined from Path hop
    """
    return self.__origin_path
      
  def _set_origin_path(self, v, load=False):
    """
    Setter method for origin_path, mapped from YANG variable /mpls_state/te/router_id_map/origin_path (uint32)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_origin_path is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_origin_path() directly.

    YANG Description: IP origined from Path hop
    """
    try:
      t = YANGDynClass(v,base=RestrictedClassType(base_type=long, restriction_dict={'range': ['0..4294967295']}, int_size=32), is_leaf=True, yang_name="origin-path", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='urn:brocade.com:mgmt:brocade-mpls-operational', defining_module='brocade-mpls-operational', yang_type='uint32', is_config=False)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """origin_path must be of a type compatible with uint32""",
          'defined-type': "uint32",
          'generated-type': """YANGDynClass(base=RestrictedClassType(base_type=long, restriction_dict={'range': ['0..4294967295']}, int_size=32), is_leaf=True, yang_name="origin-path", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='urn:brocade.com:mgmt:brocade-mpls-operational', defining_module='brocade-mpls-operational', yang_type='uint32', is_config=False)""",
        })

    self.__origin_path = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_origin_path(self):
    self.__origin_path = YANGDynClass(base=RestrictedClassType(base_type=long, restriction_dict={'range': ['0..4294967295']}, int_size=32), is_leaf=True, yang_name="origin-path", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='urn:brocade.com:mgmt:brocade-mpls-operational', defining_module='brocade-mpls-operational', yang_type='uint32', is_config=False)


  def _get_origin_lsp(self):
    """
    Getter method for origin_lsp, mapped from YANG variable /mpls_state/te/router_id_map/origin_lsp (uint32)

    YANG Description: IP origined from LSP to address
    """
    return self.__origin_lsp
      
  def _set_origin_lsp(self, v, load=False):
    """
    Setter method for origin_lsp, mapped from YANG variable /mpls_state/te/router_id_map/origin_lsp (uint32)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_origin_lsp is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_origin_lsp() directly.

    YANG Description: IP origined from LSP to address
    """
    try:
      t = YANGDynClass(v,base=RestrictedClassType(base_type=long, restriction_dict={'range': ['0..4294967295']}, int_size=32), is_leaf=True, yang_name="origin-lsp", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='urn:brocade.com:mgmt:brocade-mpls-operational', defining_module='brocade-mpls-operational', yang_type='uint32', is_config=False)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """origin_lsp must be of a type compatible with uint32""",
          'defined-type': "uint32",
          'generated-type': """YANGDynClass(base=RestrictedClassType(base_type=long, restriction_dict={'range': ['0..4294967295']}, int_size=32), is_leaf=True, yang_name="origin-lsp", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='urn:brocade.com:mgmt:brocade-mpls-operational', defining_module='brocade-mpls-operational', yang_type='uint32', is_config=False)""",
        })

    self.__origin_lsp = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_origin_lsp(self):
    self.__origin_lsp = YANGDynClass(base=RestrictedClassType(base_type=long, restriction_dict={'range': ['0..4294967295']}, int_size=32), is_leaf=True, yang_name="origin-lsp", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='urn:brocade.com:mgmt:brocade-mpls-operational', defining_module='brocade-mpls-operational', yang_type='uint32', is_config=False)


  def _get_origin_other(self):
    """
    Getter method for origin_other, mapped from YANG variable /mpls_state/te/router_id_map/origin_other (boolean)

    YANG Description: IP origined from other sources
    """
    return self.__origin_other
      
  def _set_origin_other(self, v, load=False):
    """
    Setter method for origin_other, mapped from YANG variable /mpls_state/te/router_id_map/origin_other (boolean)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_origin_other is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_origin_other() directly.

    YANG Description: IP origined from other sources
    """
    try:
      t = YANGDynClass(v,base=YANGBool, is_leaf=True, yang_name="origin-other", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='urn:brocade.com:mgmt:brocade-mpls-operational', defining_module='brocade-mpls-operational', yang_type='boolean', is_config=False)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """origin_other must be of a type compatible with boolean""",
          'defined-type': "boolean",
          'generated-type': """YANGDynClass(base=YANGBool, is_leaf=True, yang_name="origin-other", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='urn:brocade.com:mgmt:brocade-mpls-operational', defining_module='brocade-mpls-operational', yang_type='boolean', is_config=False)""",
        })

    self.__origin_other = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_origin_other(self):
    self.__origin_other = YANGDynClass(base=YANGBool, is_leaf=True, yang_name="origin-other", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='urn:brocade.com:mgmt:brocade-mpls-operational', defining_module='brocade-mpls-operational', yang_type='boolean', is_config=False)

  ip_address = __builtin__.property(_get_ip_address)
  router_id = __builtin__.property(_get_router_id)
  resolved = __builtin__.property(_get_resolved)
  igp_isis = __builtin__.property(_get_igp_isis)
  igp_ospf = __builtin__.property(_get_igp_ospf)
  isis_level = __builtin__.property(_get_isis_level)
  ospf_area = __builtin__.property(_get_ospf_area)
  origin_ted = __builtin__.property(_get_origin_ted)
  origin_path = __builtin__.property(_get_origin_path)
  origin_lsp = __builtin__.property(_get_origin_lsp)
  origin_other = __builtin__.property(_get_origin_other)


  _pyangbind_elements = {'ip_address': ip_address, 'router_id': router_id, 'resolved': resolved, 'igp_isis': igp_isis, 'igp_ospf': igp_ospf, 'isis_level': isis_level, 'ospf_area': ospf_area, 'origin_ted': origin_ted, 'origin_path': origin_path, 'origin_lsp': origin_lsp, 'origin_other': origin_other, }

