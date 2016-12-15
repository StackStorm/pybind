
from operator import attrgetter
import pyangbind.lib.xpathhelper as xpathhelper
from pyangbind.lib.yangtypes import RestrictedPrecisionDecimalType, RestrictedClassType, TypedListType
from pyangbind.lib.yangtypes import YANGBool, YANGListType, YANGDynClass, ReferenceType
from pyangbind.lib.base import PybindBase
from decimal import Decimal
from bitarray import bitarray
import __builtin__
import database
import router_id_map
class te(PybindBase):
  """
  This class was auto-generated by the PythonClass plugin for PYANG
  from YANG module brocade-mpls-operational - based on the path /mpls-state/te. Each member element of
  the container is represented as a class variable - with a specific
  YANG type.

  YANG Description: MPLS Traffic Engineering Operational Information
  """
  __slots__ = ('_pybind_generated_by', '_path_helper', '_yang_name', '_rest_name', '_extmethods', '__ospf_te_enabled','__isis_te_enabled','__ospf_area_id','__isis_level_id','__database','__router_id_map',)

  _yang_name = 'te'
  _rest_name = 'te'

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
    self.__router_id_map = YANGDynClass(base=YANGListType("ip_address",router_id_map.router_id_map, yang_name="router-id-map", rest_name="router-id-map", parent=self, is_container='list', user_ordered=False, path_helper=self._path_helper, yang_keys='ip-address', extensions={u'tailf-common': {u'callpoint': u'mpls-te-router-id-map', u'cli-suppress-show-path': None}}), is_container='list', yang_name="router-id-map", rest_name="router-id-map", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'callpoint': u'mpls-te-router-id-map', u'cli-suppress-show-path': None}}, namespace='urn:brocade.com:mgmt:brocade-mpls-operational', defining_module='brocade-mpls-operational', yang_type='list', is_config=False)
    self.__database = YANGDynClass(base=database.database, is_container='container', yang_name="database", rest_name="database", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'callpoint': u'mpls-te-database', u'cli-suppress-show-path': None}}, namespace='urn:brocade.com:mgmt:brocade-mpls-operational', defining_module='brocade-mpls-operational', yang_type='container', is_config=False)
    self.__isis_level_id = YANGDynClass(base=RestrictedClassType(base_type=long, restriction_dict={'range': ['0..4294967295']}, int_size=32), is_leaf=True, yang_name="isis-level-id", rest_name="isis-level-id", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='urn:brocade.com:mgmt:brocade-mpls-operational', defining_module='brocade-mpls-operational', yang_type='uint32', is_config=False)
    self.__ospf_area_id = YANGDynClass(base=RestrictedClassType(base_type=unicode, restriction_dict={'pattern': u'(([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])\\.){3}([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])(%[\\p{N}\\p{L}]+)?'}), is_leaf=True, yang_name="ospf-area-id", rest_name="ospf-area-id", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='urn:brocade.com:mgmt:brocade-mpls-operational', defining_module='brocade-mpls-operational', yang_type='inet:ipv4-address', is_config=False)
    self.__isis_te_enabled = YANGDynClass(base=YANGBool, is_leaf=True, yang_name="isis-te-enabled", rest_name="isis-te-enabled", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='urn:brocade.com:mgmt:brocade-mpls-operational', defining_module='brocade-mpls-operational', yang_type='boolean', is_config=False)
    self.__ospf_te_enabled = YANGDynClass(base=YANGBool, is_leaf=True, yang_name="ospf-te-enabled", rest_name="ospf-te-enabled", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='urn:brocade.com:mgmt:brocade-mpls-operational', defining_module='brocade-mpls-operational', yang_type='boolean', is_config=False)

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
      return [u'mpls-state', u'te']

  def _rest_path(self):
    if hasattr(self, "_parent"):
      if self._rest_name:
        return self._parent._rest_path()+[self._rest_name]
      else:
        return self._parent._rest_path()
    else:
      return [u'mpls-state', u'te']

  def _get_ospf_te_enabled(self):
    """
    Getter method for ospf_te_enabled, mapped from YANG variable /mpls_state/te/ospf_te_enabled (boolean)

    YANG Description: OSPF TE is configured
    """
    return self.__ospf_te_enabled
      
  def _set_ospf_te_enabled(self, v, load=False):
    """
    Setter method for ospf_te_enabled, mapped from YANG variable /mpls_state/te/ospf_te_enabled (boolean)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_ospf_te_enabled is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_ospf_te_enabled() directly.

    YANG Description: OSPF TE is configured
    """
    if hasattr(v, "_utype"):
      v = v._utype(v)
    try:
      t = YANGDynClass(v,base=YANGBool, is_leaf=True, yang_name="ospf-te-enabled", rest_name="ospf-te-enabled", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='urn:brocade.com:mgmt:brocade-mpls-operational', defining_module='brocade-mpls-operational', yang_type='boolean', is_config=False)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """ospf_te_enabled must be of a type compatible with boolean""",
          'defined-type': "boolean",
          'generated-type': """YANGDynClass(base=YANGBool, is_leaf=True, yang_name="ospf-te-enabled", rest_name="ospf-te-enabled", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='urn:brocade.com:mgmt:brocade-mpls-operational', defining_module='brocade-mpls-operational', yang_type='boolean', is_config=False)""",
        })

    self.__ospf_te_enabled = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_ospf_te_enabled(self):
    self.__ospf_te_enabled = YANGDynClass(base=YANGBool, is_leaf=True, yang_name="ospf-te-enabled", rest_name="ospf-te-enabled", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='urn:brocade.com:mgmt:brocade-mpls-operational', defining_module='brocade-mpls-operational', yang_type='boolean', is_config=False)


  def _get_isis_te_enabled(self):
    """
    Getter method for isis_te_enabled, mapped from YANG variable /mpls_state/te/isis_te_enabled (boolean)

    YANG Description: ISIS TE is configured
    """
    return self.__isis_te_enabled
      
  def _set_isis_te_enabled(self, v, load=False):
    """
    Setter method for isis_te_enabled, mapped from YANG variable /mpls_state/te/isis_te_enabled (boolean)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_isis_te_enabled is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_isis_te_enabled() directly.

    YANG Description: ISIS TE is configured
    """
    if hasattr(v, "_utype"):
      v = v._utype(v)
    try:
      t = YANGDynClass(v,base=YANGBool, is_leaf=True, yang_name="isis-te-enabled", rest_name="isis-te-enabled", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='urn:brocade.com:mgmt:brocade-mpls-operational', defining_module='brocade-mpls-operational', yang_type='boolean', is_config=False)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """isis_te_enabled must be of a type compatible with boolean""",
          'defined-type': "boolean",
          'generated-type': """YANGDynClass(base=YANGBool, is_leaf=True, yang_name="isis-te-enabled", rest_name="isis-te-enabled", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='urn:brocade.com:mgmt:brocade-mpls-operational', defining_module='brocade-mpls-operational', yang_type='boolean', is_config=False)""",
        })

    self.__isis_te_enabled = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_isis_te_enabled(self):
    self.__isis_te_enabled = YANGDynClass(base=YANGBool, is_leaf=True, yang_name="isis-te-enabled", rest_name="isis-te-enabled", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='urn:brocade.com:mgmt:brocade-mpls-operational', defining_module='brocade-mpls-operational', yang_type='boolean', is_config=False)


  def _get_ospf_area_id(self):
    """
    Getter method for ospf_area_id, mapped from YANG variable /mpls_state/te/ospf_area_id (inet:ipv4-address)

    YANG Description: Area Id of OSPF TE
    """
    return self.__ospf_area_id
      
  def _set_ospf_area_id(self, v, load=False):
    """
    Setter method for ospf_area_id, mapped from YANG variable /mpls_state/te/ospf_area_id (inet:ipv4-address)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_ospf_area_id is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_ospf_area_id() directly.

    YANG Description: Area Id of OSPF TE
    """
    if hasattr(v, "_utype"):
      v = v._utype(v)
    try:
      t = YANGDynClass(v,base=RestrictedClassType(base_type=unicode, restriction_dict={'pattern': u'(([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])\\.){3}([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])(%[\\p{N}\\p{L}]+)?'}), is_leaf=True, yang_name="ospf-area-id", rest_name="ospf-area-id", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='urn:brocade.com:mgmt:brocade-mpls-operational', defining_module='brocade-mpls-operational', yang_type='inet:ipv4-address', is_config=False)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """ospf_area_id must be of a type compatible with inet:ipv4-address""",
          'defined-type': "inet:ipv4-address",
          'generated-type': """YANGDynClass(base=RestrictedClassType(base_type=unicode, restriction_dict={'pattern': u'(([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])\\.){3}([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])(%[\\p{N}\\p{L}]+)?'}), is_leaf=True, yang_name="ospf-area-id", rest_name="ospf-area-id", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='urn:brocade.com:mgmt:brocade-mpls-operational', defining_module='brocade-mpls-operational', yang_type='inet:ipv4-address', is_config=False)""",
        })

    self.__ospf_area_id = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_ospf_area_id(self):
    self.__ospf_area_id = YANGDynClass(base=RestrictedClassType(base_type=unicode, restriction_dict={'pattern': u'(([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])\\.){3}([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])(%[\\p{N}\\p{L}]+)?'}), is_leaf=True, yang_name="ospf-area-id", rest_name="ospf-area-id", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='urn:brocade.com:mgmt:brocade-mpls-operational', defining_module='brocade-mpls-operational', yang_type='inet:ipv4-address', is_config=False)


  def _get_isis_level_id(self):
    """
    Getter method for isis_level_id, mapped from YANG variable /mpls_state/te/isis_level_id (uint32)

    YANG Description: Level Id of ISIS TE
    """
    return self.__isis_level_id
      
  def _set_isis_level_id(self, v, load=False):
    """
    Setter method for isis_level_id, mapped from YANG variable /mpls_state/te/isis_level_id (uint32)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_isis_level_id is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_isis_level_id() directly.

    YANG Description: Level Id of ISIS TE
    """
    if hasattr(v, "_utype"):
      v = v._utype(v)
    try:
      t = YANGDynClass(v,base=RestrictedClassType(base_type=long, restriction_dict={'range': ['0..4294967295']}, int_size=32), is_leaf=True, yang_name="isis-level-id", rest_name="isis-level-id", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='urn:brocade.com:mgmt:brocade-mpls-operational', defining_module='brocade-mpls-operational', yang_type='uint32', is_config=False)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """isis_level_id must be of a type compatible with uint32""",
          'defined-type': "uint32",
          'generated-type': """YANGDynClass(base=RestrictedClassType(base_type=long, restriction_dict={'range': ['0..4294967295']}, int_size=32), is_leaf=True, yang_name="isis-level-id", rest_name="isis-level-id", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='urn:brocade.com:mgmt:brocade-mpls-operational', defining_module='brocade-mpls-operational', yang_type='uint32', is_config=False)""",
        })

    self.__isis_level_id = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_isis_level_id(self):
    self.__isis_level_id = YANGDynClass(base=RestrictedClassType(base_type=long, restriction_dict={'range': ['0..4294967295']}, int_size=32), is_leaf=True, yang_name="isis-level-id", rest_name="isis-level-id", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='urn:brocade.com:mgmt:brocade-mpls-operational', defining_module='brocade-mpls-operational', yang_type='uint32', is_config=False)


  def _get_database(self):
    """
    Getter method for database, mapped from YANG variable /mpls_state/te/database (container)

    YANG Description: MPLS TE Database Operational Information
    """
    return self.__database
      
  def _set_database(self, v, load=False):
    """
    Setter method for database, mapped from YANG variable /mpls_state/te/database (container)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_database is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_database() directly.

    YANG Description: MPLS TE Database Operational Information
    """
    if hasattr(v, "_utype"):
      v = v._utype(v)
    try:
      t = YANGDynClass(v,base=database.database, is_container='container', yang_name="database", rest_name="database", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'callpoint': u'mpls-te-database', u'cli-suppress-show-path': None}}, namespace='urn:brocade.com:mgmt:brocade-mpls-operational', defining_module='brocade-mpls-operational', yang_type='container', is_config=False)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """database must be of a type compatible with container""",
          'defined-type': "container",
          'generated-type': """YANGDynClass(base=database.database, is_container='container', yang_name="database", rest_name="database", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'callpoint': u'mpls-te-database', u'cli-suppress-show-path': None}}, namespace='urn:brocade.com:mgmt:brocade-mpls-operational', defining_module='brocade-mpls-operational', yang_type='container', is_config=False)""",
        })

    self.__database = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_database(self):
    self.__database = YANGDynClass(base=database.database, is_container='container', yang_name="database", rest_name="database", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'callpoint': u'mpls-te-database', u'cli-suppress-show-path': None}}, namespace='urn:brocade.com:mgmt:brocade-mpls-operational', defining_module='brocade-mpls-operational', yang_type='container', is_config=False)


  def _get_router_id_map(self):
    """
    Getter method for router_id_map, mapped from YANG variable /mpls_state/te/router_id_map (list)

    YANG Description: MPLS TE Router Id mapping brief Operational Information
    """
    return self.__router_id_map
      
  def _set_router_id_map(self, v, load=False):
    """
    Setter method for router_id_map, mapped from YANG variable /mpls_state/te/router_id_map (list)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_router_id_map is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_router_id_map() directly.

    YANG Description: MPLS TE Router Id mapping brief Operational Information
    """
    if hasattr(v, "_utype"):
      v = v._utype(v)
    try:
      t = YANGDynClass(v,base=YANGListType("ip_address",router_id_map.router_id_map, yang_name="router-id-map", rest_name="router-id-map", parent=self, is_container='list', user_ordered=False, path_helper=self._path_helper, yang_keys='ip-address', extensions={u'tailf-common': {u'callpoint': u'mpls-te-router-id-map', u'cli-suppress-show-path': None}}), is_container='list', yang_name="router-id-map", rest_name="router-id-map", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'callpoint': u'mpls-te-router-id-map', u'cli-suppress-show-path': None}}, namespace='urn:brocade.com:mgmt:brocade-mpls-operational', defining_module='brocade-mpls-operational', yang_type='list', is_config=False)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """router_id_map must be of a type compatible with list""",
          'defined-type': "list",
          'generated-type': """YANGDynClass(base=YANGListType("ip_address",router_id_map.router_id_map, yang_name="router-id-map", rest_name="router-id-map", parent=self, is_container='list', user_ordered=False, path_helper=self._path_helper, yang_keys='ip-address', extensions={u'tailf-common': {u'callpoint': u'mpls-te-router-id-map', u'cli-suppress-show-path': None}}), is_container='list', yang_name="router-id-map", rest_name="router-id-map", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'callpoint': u'mpls-te-router-id-map', u'cli-suppress-show-path': None}}, namespace='urn:brocade.com:mgmt:brocade-mpls-operational', defining_module='brocade-mpls-operational', yang_type='list', is_config=False)""",
        })

    self.__router_id_map = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_router_id_map(self):
    self.__router_id_map = YANGDynClass(base=YANGListType("ip_address",router_id_map.router_id_map, yang_name="router-id-map", rest_name="router-id-map", parent=self, is_container='list', user_ordered=False, path_helper=self._path_helper, yang_keys='ip-address', extensions={u'tailf-common': {u'callpoint': u'mpls-te-router-id-map', u'cli-suppress-show-path': None}}), is_container='list', yang_name="router-id-map", rest_name="router-id-map", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'callpoint': u'mpls-te-router-id-map', u'cli-suppress-show-path': None}}, namespace='urn:brocade.com:mgmt:brocade-mpls-operational', defining_module='brocade-mpls-operational', yang_type='list', is_config=False)

  ospf_te_enabled = __builtin__.property(_get_ospf_te_enabled)
  isis_te_enabled = __builtin__.property(_get_isis_te_enabled)
  ospf_area_id = __builtin__.property(_get_ospf_area_id)
  isis_level_id = __builtin__.property(_get_isis_level_id)
  database = __builtin__.property(_get_database)
  router_id_map = __builtin__.property(_get_router_id_map)


  _pyangbind_elements = {'ospf_te_enabled': ospf_te_enabled, 'isis_te_enabled': isis_te_enabled, 'ospf_area_id': ospf_area_id, 'isis_level_id': isis_level_id, 'database': database, 'router_id_map': router_id_map, }


