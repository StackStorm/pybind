
from operator import attrgetter
import pyangbind.lib.xpathhelper as xpathhelper
from pyangbind.lib.yangtypes import RestrictedPrecisionDecimalType, RestrictedClassType, TypedListType
from pyangbind.lib.yangtypes import YANGBool, YANGListType, YANGDynClass, ReferenceType
from pyangbind.lib.base import PybindBase
from decimal import Decimal
from bitarray import bitarray
import __builtin__
class access_group(PybindBase):
  """
  This class was auto-generated by the PythonClass plugin for PYANG
  from YANG module brocade-interface - based on the path /interface/fortygigabitethernet/mac/access-group. Each member element of
  the container is represented as a class variable - with a specific
  YANG type.
  """
  __slots__ = ('_pybind_generated_by', '_path_helper', '_yang_name', '_rest_name', '_extmethods', '__mac_access_list','__mac_direction','__traffic_type',)

  _yang_name = 'access-group'
  _rest_name = 'access-group'

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
    self.__mac_direction = YANGDynClass(base=RestrictedClassType(base_type=unicode,                                     restriction_type="dict_key",                                     restriction_arg={u'out': {'value': 2}, u'in': {'value': 1}},), is_leaf=True, yang_name="mac-direction", rest_name="mac-direction", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'cli-full-command': None, u'cli-drop-node-name': None, u'cli-full-no': None}}, is_keyval=True, namespace='urn:brocade.com:mgmt:brocade-mac-access-list', defining_module='brocade-mac-access-list', yang_type='enumeration', is_config=True)
    self.__traffic_type = YANGDynClass(base=RestrictedClassType(base_type=unicode,                                     restriction_type="dict_key",                                     restriction_arg={u'routed': {'value': 3}, u'switched': {'value': 2}},), is_leaf=True, yang_name="traffic-type", rest_name="traffic-type", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'cli-full-command': None, u'cli-drop-node-name': None, u'cli-full-no': None}}, namespace='urn:brocade.com:mgmt:brocade-mac-access-list', defining_module='brocade-mac-access-list', yang_type='enumeration', is_config=True)
    self.__mac_access_list = YANGDynClass(base=RestrictedClassType(base_type=unicode, restriction_dict={'pattern': u'[a-zA-Z0-9]{1}([-a-zA-Z0-9_]{0,62})', 'length': [u'1..63']}), is_leaf=True, yang_name="mac-access-list", rest_name="mac-access-list", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'info': u'ACL_NAME;; Access List Name (Max 63)', u'cli-drop-node-name': None, u'cli-incomplete-no': None, u'cli-incomplete-command': None}}, is_keyval=True, namespace='urn:brocade.com:mgmt:brocade-mac-access-list', defining_module='brocade-mac-access-list', yang_type='mac-acl-name', is_config=True)

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
      return [u'interface', u'fortygigabitethernet', u'mac', u'access-group']

  def _rest_path(self):
    if hasattr(self, "_parent"):
      if self._rest_name:
        return self._parent._rest_path()+[self._rest_name]
      else:
        return self._parent._rest_path()
    else:
      return [u'interface', u'FortyGigabitEthernet', u'mac', u'access-group']

  def _get_mac_access_list(self):
    """
    Getter method for mac_access_list, mapped from YANG variable /interface/fortygigabitethernet/mac/access_group/mac_access_list (mac-acl-name)
    """
    return self.__mac_access_list
      
  def _set_mac_access_list(self, v, load=False):
    """
    Setter method for mac_access_list, mapped from YANG variable /interface/fortygigabitethernet/mac/access_group/mac_access_list (mac-acl-name)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_mac_access_list is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_mac_access_list() directly.
    """
    parent = getattr(self, "_parent", None)
    if parent is not None and load is False:
      raise AttributeError("Cannot set keys directly when" +
                             " within an instantiated list")

    if hasattr(v, "_utype"):
      v = v._utype(v)
    try:
      t = YANGDynClass(v,base=RestrictedClassType(base_type=unicode, restriction_dict={'pattern': u'[a-zA-Z0-9]{1}([-a-zA-Z0-9_]{0,62})', 'length': [u'1..63']}), is_leaf=True, yang_name="mac-access-list", rest_name="mac-access-list", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'info': u'ACL_NAME;; Access List Name (Max 63)', u'cli-drop-node-name': None, u'cli-incomplete-no': None, u'cli-incomplete-command': None}}, is_keyval=True, namespace='urn:brocade.com:mgmt:brocade-mac-access-list', defining_module='brocade-mac-access-list', yang_type='mac-acl-name', is_config=True)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """mac_access_list must be of a type compatible with mac-acl-name""",
          'defined-type': "brocade-mac-access-list:mac-acl-name",
          'generated-type': """YANGDynClass(base=RestrictedClassType(base_type=unicode, restriction_dict={'pattern': u'[a-zA-Z0-9]{1}([-a-zA-Z0-9_]{0,62})', 'length': [u'1..63']}), is_leaf=True, yang_name="mac-access-list", rest_name="mac-access-list", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'info': u'ACL_NAME;; Access List Name (Max 63)', u'cli-drop-node-name': None, u'cli-incomplete-no': None, u'cli-incomplete-command': None}}, is_keyval=True, namespace='urn:brocade.com:mgmt:brocade-mac-access-list', defining_module='brocade-mac-access-list', yang_type='mac-acl-name', is_config=True)""",
        })

    self.__mac_access_list = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_mac_access_list(self):
    self.__mac_access_list = YANGDynClass(base=RestrictedClassType(base_type=unicode, restriction_dict={'pattern': u'[a-zA-Z0-9]{1}([-a-zA-Z0-9_]{0,62})', 'length': [u'1..63']}), is_leaf=True, yang_name="mac-access-list", rest_name="mac-access-list", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'info': u'ACL_NAME;; Access List Name (Max 63)', u'cli-drop-node-name': None, u'cli-incomplete-no': None, u'cli-incomplete-command': None}}, is_keyval=True, namespace='urn:brocade.com:mgmt:brocade-mac-access-list', defining_module='brocade-mac-access-list', yang_type='mac-acl-name', is_config=True)


  def _get_mac_direction(self):
    """
    Getter method for mac_direction, mapped from YANG variable /interface/fortygigabitethernet/mac/access_group/mac_direction (enumeration)
    """
    return self.__mac_direction
      
  def _set_mac_direction(self, v, load=False):
    """
    Setter method for mac_direction, mapped from YANG variable /interface/fortygigabitethernet/mac/access_group/mac_direction (enumeration)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_mac_direction is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_mac_direction() directly.
    """
    parent = getattr(self, "_parent", None)
    if parent is not None and load is False:
      raise AttributeError("Cannot set keys directly when" +
                             " within an instantiated list")

    if hasattr(v, "_utype"):
      v = v._utype(v)
    try:
      t = YANGDynClass(v,base=RestrictedClassType(base_type=unicode,                                     restriction_type="dict_key",                                     restriction_arg={u'out': {'value': 2}, u'in': {'value': 1}},), is_leaf=True, yang_name="mac-direction", rest_name="mac-direction", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'cli-full-command': None, u'cli-drop-node-name': None, u'cli-full-no': None}}, is_keyval=True, namespace='urn:brocade.com:mgmt:brocade-mac-access-list', defining_module='brocade-mac-access-list', yang_type='enumeration', is_config=True)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """mac_direction must be of a type compatible with enumeration""",
          'defined-type': "brocade-mac-access-list:enumeration",
          'generated-type': """YANGDynClass(base=RestrictedClassType(base_type=unicode,                                     restriction_type="dict_key",                                     restriction_arg={u'out': {'value': 2}, u'in': {'value': 1}},), is_leaf=True, yang_name="mac-direction", rest_name="mac-direction", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'cli-full-command': None, u'cli-drop-node-name': None, u'cli-full-no': None}}, is_keyval=True, namespace='urn:brocade.com:mgmt:brocade-mac-access-list', defining_module='brocade-mac-access-list', yang_type='enumeration', is_config=True)""",
        })

    self.__mac_direction = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_mac_direction(self):
    self.__mac_direction = YANGDynClass(base=RestrictedClassType(base_type=unicode,                                     restriction_type="dict_key",                                     restriction_arg={u'out': {'value': 2}, u'in': {'value': 1}},), is_leaf=True, yang_name="mac-direction", rest_name="mac-direction", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'cli-full-command': None, u'cli-drop-node-name': None, u'cli-full-no': None}}, is_keyval=True, namespace='urn:brocade.com:mgmt:brocade-mac-access-list', defining_module='brocade-mac-access-list', yang_type='enumeration', is_config=True)


  def _get_traffic_type(self):
    """
    Getter method for traffic_type, mapped from YANG variable /interface/fortygigabitethernet/mac/access_group/traffic_type (enumeration)
    """
    return self.__traffic_type
      
  def _set_traffic_type(self, v, load=False):
    """
    Setter method for traffic_type, mapped from YANG variable /interface/fortygigabitethernet/mac/access_group/traffic_type (enumeration)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_traffic_type is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_traffic_type() directly.
    """
    if hasattr(v, "_utype"):
      v = v._utype(v)
    try:
      t = YANGDynClass(v,base=RestrictedClassType(base_type=unicode,                                     restriction_type="dict_key",                                     restriction_arg={u'routed': {'value': 3}, u'switched': {'value': 2}},), is_leaf=True, yang_name="traffic-type", rest_name="traffic-type", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'cli-full-command': None, u'cli-drop-node-name': None, u'cli-full-no': None}}, namespace='urn:brocade.com:mgmt:brocade-mac-access-list', defining_module='brocade-mac-access-list', yang_type='enumeration', is_config=True)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """traffic_type must be of a type compatible with enumeration""",
          'defined-type': "brocade-mac-access-list:enumeration",
          'generated-type': """YANGDynClass(base=RestrictedClassType(base_type=unicode,                                     restriction_type="dict_key",                                     restriction_arg={u'routed': {'value': 3}, u'switched': {'value': 2}},), is_leaf=True, yang_name="traffic-type", rest_name="traffic-type", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'cli-full-command': None, u'cli-drop-node-name': None, u'cli-full-no': None}}, namespace='urn:brocade.com:mgmt:brocade-mac-access-list', defining_module='brocade-mac-access-list', yang_type='enumeration', is_config=True)""",
        })

    self.__traffic_type = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_traffic_type(self):
    self.__traffic_type = YANGDynClass(base=RestrictedClassType(base_type=unicode,                                     restriction_type="dict_key",                                     restriction_arg={u'routed': {'value': 3}, u'switched': {'value': 2}},), is_leaf=True, yang_name="traffic-type", rest_name="traffic-type", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'cli-full-command': None, u'cli-drop-node-name': None, u'cli-full-no': None}}, namespace='urn:brocade.com:mgmt:brocade-mac-access-list', defining_module='brocade-mac-access-list', yang_type='enumeration', is_config=True)

  mac_access_list = __builtin__.property(_get_mac_access_list, _set_mac_access_list)
  mac_direction = __builtin__.property(_get_mac_direction, _set_mac_direction)
  traffic_type = __builtin__.property(_get_traffic_type, _set_traffic_type)


  _pyangbind_elements = {'mac_access_list': mac_access_list, 'mac_direction': mac_direction, 'traffic_type': traffic_type, }


