
from operator import attrgetter
import pyangbind.lib.xpathhelper as xpathhelper
from pyangbind.lib.yangtypes import RestrictedPrecisionDecimalType, RestrictedClassType, TypedListType
from pyangbind.lib.yangtypes import YANGBool, YANGListType, YANGDynClass, ReferenceType
from pyangbind.lib.base import PybindBase
from decimal import Decimal
from bitarray import bitarray
import __builtin__
import auto_recovery
class mac_move(PybindBase):
  """
  This class was auto-generated by the PythonClass plugin for PYANG
  from YANG module brocade-mac-address-table - based on the path /mac-address-table/mac-move. Each member element of
  the container is represented as a class variable - with a specific
  YANG type.

  YANG Description: MAC move
  """
  __slots__ = ('_pybind_generated_by', '_path_helper', '_yang_name', '_rest_name', '_extmethods', '__mac_move_detect_enable','__mac_move_limit','__mac_move_action','__auto_recovery',)

  _yang_name = 'mac-move'
  _rest_name = 'mac-move'

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
    self.__auto_recovery = YANGDynClass(base=auto_recovery.auto_recovery, is_container='container', yang_name="auto-recovery", rest_name="auto-recovery", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'info': u'Auto recovery of port on MAC move'}}, namespace='urn:brocade.com:mgmt:brocade-mac-address-table', defining_module='brocade-mac-address-table', yang_type='container', is_config=True)
    self.__mac_move_detect_enable = YANGDynClass(base=YANGBool, is_leaf=True, yang_name="mac-move-detect-enable", rest_name="detect", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'info': u'Enable MAC move detect', u'cli-full-command': None, u'alt-name': u'detect'}}, namespace='urn:brocade.com:mgmt:brocade-mac-address-table', defining_module='brocade-mac-address-table', yang_type='empty', is_config=True)
    self.__mac_move_limit = YANGDynClass(base=RestrictedClassType(base_type=RestrictedClassType(base_type=long, restriction_dict={'range': ['0..4294967295']}, int_size=32), restriction_dict={'range': [u'5..500']}), default=RestrictedClassType(base_type=long, restriction_dict={'range': ['0..4294967295']}, int_size=32)(20), is_leaf=True, yang_name="mac-move-limit", rest_name="limit", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'info': u'MAC move detect limit (default = 20)', u'cli-full-command': None, u'alt-name': u'limit'}}, namespace='urn:brocade.com:mgmt:brocade-mac-address-table', defining_module='brocade-mac-address-table', yang_type='uint32', is_config=True)
    self.__mac_move_action = YANGDynClass(base=RestrictedClassType(base_type=unicode,                                     restriction_type="dict_key",                                     restriction_arg={u'raslog': {'value': 2}, u'shutdown': {'value': 1}},), default=unicode("shutdown"), is_leaf=True, yang_name="mac-move-action", rest_name="action", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'info': u'Action on MAC move', u'cli-full-command': None, u'alt-name': u'action'}}, namespace='urn:brocade.com:mgmt:brocade-mac-address-table', defining_module='brocade-mac-address-table', yang_type='enumeration', is_config=True)

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
      return [u'mac-address-table', u'mac-move']

  def _rest_path(self):
    if hasattr(self, "_parent"):
      if self._rest_name:
        return self._parent._rest_path()+[self._rest_name]
      else:
        return self._parent._rest_path()
    else:
      return [u'mac-address-table', u'mac-move']

  def _get_mac_move_detect_enable(self):
    """
    Getter method for mac_move_detect_enable, mapped from YANG variable /mac_address_table/mac_move/mac_move_detect_enable (empty)

    YANG Description: Enable MAC move detect
    """
    return self.__mac_move_detect_enable
      
  def _set_mac_move_detect_enable(self, v, load=False):
    """
    Setter method for mac_move_detect_enable, mapped from YANG variable /mac_address_table/mac_move/mac_move_detect_enable (empty)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_mac_move_detect_enable is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_mac_move_detect_enable() directly.

    YANG Description: Enable MAC move detect
    """
    if hasattr(v, "_utype"):
      v = v._utype(v)
    try:
      t = YANGDynClass(v,base=YANGBool, is_leaf=True, yang_name="mac-move-detect-enable", rest_name="detect", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'info': u'Enable MAC move detect', u'cli-full-command': None, u'alt-name': u'detect'}}, namespace='urn:brocade.com:mgmt:brocade-mac-address-table', defining_module='brocade-mac-address-table', yang_type='empty', is_config=True)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """mac_move_detect_enable must be of a type compatible with empty""",
          'defined-type': "empty",
          'generated-type': """YANGDynClass(base=YANGBool, is_leaf=True, yang_name="mac-move-detect-enable", rest_name="detect", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'info': u'Enable MAC move detect', u'cli-full-command': None, u'alt-name': u'detect'}}, namespace='urn:brocade.com:mgmt:brocade-mac-address-table', defining_module='brocade-mac-address-table', yang_type='empty', is_config=True)""",
        })

    self.__mac_move_detect_enable = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_mac_move_detect_enable(self):
    self.__mac_move_detect_enable = YANGDynClass(base=YANGBool, is_leaf=True, yang_name="mac-move-detect-enable", rest_name="detect", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'info': u'Enable MAC move detect', u'cli-full-command': None, u'alt-name': u'detect'}}, namespace='urn:brocade.com:mgmt:brocade-mac-address-table', defining_module='brocade-mac-address-table', yang_type='empty', is_config=True)


  def _get_mac_move_limit(self):
    """
    Getter method for mac_move_limit, mapped from YANG variable /mac_address_table/mac_move/mac_move_limit (uint32)

    YANG Description: MAC move detect limit (default = 20)
    """
    return self.__mac_move_limit
      
  def _set_mac_move_limit(self, v, load=False):
    """
    Setter method for mac_move_limit, mapped from YANG variable /mac_address_table/mac_move/mac_move_limit (uint32)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_mac_move_limit is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_mac_move_limit() directly.

    YANG Description: MAC move detect limit (default = 20)
    """
    if hasattr(v, "_utype"):
      v = v._utype(v)
    try:
      t = YANGDynClass(v,base=RestrictedClassType(base_type=RestrictedClassType(base_type=long, restriction_dict={'range': ['0..4294967295']}, int_size=32), restriction_dict={'range': [u'5..500']}), default=RestrictedClassType(base_type=long, restriction_dict={'range': ['0..4294967295']}, int_size=32)(20), is_leaf=True, yang_name="mac-move-limit", rest_name="limit", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'info': u'MAC move detect limit (default = 20)', u'cli-full-command': None, u'alt-name': u'limit'}}, namespace='urn:brocade.com:mgmt:brocade-mac-address-table', defining_module='brocade-mac-address-table', yang_type='uint32', is_config=True)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """mac_move_limit must be of a type compatible with uint32""",
          'defined-type': "uint32",
          'generated-type': """YANGDynClass(base=RestrictedClassType(base_type=RestrictedClassType(base_type=long, restriction_dict={'range': ['0..4294967295']}, int_size=32), restriction_dict={'range': [u'5..500']}), default=RestrictedClassType(base_type=long, restriction_dict={'range': ['0..4294967295']}, int_size=32)(20), is_leaf=True, yang_name="mac-move-limit", rest_name="limit", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'info': u'MAC move detect limit (default = 20)', u'cli-full-command': None, u'alt-name': u'limit'}}, namespace='urn:brocade.com:mgmt:brocade-mac-address-table', defining_module='brocade-mac-address-table', yang_type='uint32', is_config=True)""",
        })

    self.__mac_move_limit = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_mac_move_limit(self):
    self.__mac_move_limit = YANGDynClass(base=RestrictedClassType(base_type=RestrictedClassType(base_type=long, restriction_dict={'range': ['0..4294967295']}, int_size=32), restriction_dict={'range': [u'5..500']}), default=RestrictedClassType(base_type=long, restriction_dict={'range': ['0..4294967295']}, int_size=32)(20), is_leaf=True, yang_name="mac-move-limit", rest_name="limit", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'info': u'MAC move detect limit (default = 20)', u'cli-full-command': None, u'alt-name': u'limit'}}, namespace='urn:brocade.com:mgmt:brocade-mac-address-table', defining_module='brocade-mac-address-table', yang_type='uint32', is_config=True)


  def _get_mac_move_action(self):
    """
    Getter method for mac_move_action, mapped from YANG variable /mac_address_table/mac_move/mac_move_action (enumeration)

    YANG Description: Action on MAC move
    """
    return self.__mac_move_action
      
  def _set_mac_move_action(self, v, load=False):
    """
    Setter method for mac_move_action, mapped from YANG variable /mac_address_table/mac_move/mac_move_action (enumeration)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_mac_move_action is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_mac_move_action() directly.

    YANG Description: Action on MAC move
    """
    if hasattr(v, "_utype"):
      v = v._utype(v)
    try:
      t = YANGDynClass(v,base=RestrictedClassType(base_type=unicode,                                     restriction_type="dict_key",                                     restriction_arg={u'raslog': {'value': 2}, u'shutdown': {'value': 1}},), default=unicode("shutdown"), is_leaf=True, yang_name="mac-move-action", rest_name="action", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'info': u'Action on MAC move', u'cli-full-command': None, u'alt-name': u'action'}}, namespace='urn:brocade.com:mgmt:brocade-mac-address-table', defining_module='brocade-mac-address-table', yang_type='enumeration', is_config=True)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """mac_move_action must be of a type compatible with enumeration""",
          'defined-type': "brocade-mac-address-table:enumeration",
          'generated-type': """YANGDynClass(base=RestrictedClassType(base_type=unicode,                                     restriction_type="dict_key",                                     restriction_arg={u'raslog': {'value': 2}, u'shutdown': {'value': 1}},), default=unicode("shutdown"), is_leaf=True, yang_name="mac-move-action", rest_name="action", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'info': u'Action on MAC move', u'cli-full-command': None, u'alt-name': u'action'}}, namespace='urn:brocade.com:mgmt:brocade-mac-address-table', defining_module='brocade-mac-address-table', yang_type='enumeration', is_config=True)""",
        })

    self.__mac_move_action = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_mac_move_action(self):
    self.__mac_move_action = YANGDynClass(base=RestrictedClassType(base_type=unicode,                                     restriction_type="dict_key",                                     restriction_arg={u'raslog': {'value': 2}, u'shutdown': {'value': 1}},), default=unicode("shutdown"), is_leaf=True, yang_name="mac-move-action", rest_name="action", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'info': u'Action on MAC move', u'cli-full-command': None, u'alt-name': u'action'}}, namespace='urn:brocade.com:mgmt:brocade-mac-address-table', defining_module='brocade-mac-address-table', yang_type='enumeration', is_config=True)


  def _get_auto_recovery(self):
    """
    Getter method for auto_recovery, mapped from YANG variable /mac_address_table/mac_move/auto_recovery (container)

    YANG Description: Auto recovery of port on MAC move
    """
    return self.__auto_recovery
      
  def _set_auto_recovery(self, v, load=False):
    """
    Setter method for auto_recovery, mapped from YANG variable /mac_address_table/mac_move/auto_recovery (container)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_auto_recovery is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_auto_recovery() directly.

    YANG Description: Auto recovery of port on MAC move
    """
    if hasattr(v, "_utype"):
      v = v._utype(v)
    try:
      t = YANGDynClass(v,base=auto_recovery.auto_recovery, is_container='container', yang_name="auto-recovery", rest_name="auto-recovery", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'info': u'Auto recovery of port on MAC move'}}, namespace='urn:brocade.com:mgmt:brocade-mac-address-table', defining_module='brocade-mac-address-table', yang_type='container', is_config=True)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """auto_recovery must be of a type compatible with container""",
          'defined-type': "container",
          'generated-type': """YANGDynClass(base=auto_recovery.auto_recovery, is_container='container', yang_name="auto-recovery", rest_name="auto-recovery", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'info': u'Auto recovery of port on MAC move'}}, namespace='urn:brocade.com:mgmt:brocade-mac-address-table', defining_module='brocade-mac-address-table', yang_type='container', is_config=True)""",
        })

    self.__auto_recovery = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_auto_recovery(self):
    self.__auto_recovery = YANGDynClass(base=auto_recovery.auto_recovery, is_container='container', yang_name="auto-recovery", rest_name="auto-recovery", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'info': u'Auto recovery of port on MAC move'}}, namespace='urn:brocade.com:mgmt:brocade-mac-address-table', defining_module='brocade-mac-address-table', yang_type='container', is_config=True)

  mac_move_detect_enable = __builtin__.property(_get_mac_move_detect_enable, _set_mac_move_detect_enable)
  mac_move_limit = __builtin__.property(_get_mac_move_limit, _set_mac_move_limit)
  mac_move_action = __builtin__.property(_get_mac_move_action, _set_mac_move_action)
  auto_recovery = __builtin__.property(_get_auto_recovery, _set_auto_recovery)


  _pyangbind_elements = {'mac_move_detect_enable': mac_move_detect_enable, 'mac_move_limit': mac_move_limit, 'mac_move_action': mac_move_action, 'auto_recovery': auto_recovery, }


