
from operator import attrgetter
import pyangbind.lib.xpathhelper as xpathhelper
from pyangbind.lib.yangtypes import RestrictedPrecisionDecimalType, RestrictedClassType, TypedListType
from pyangbind.lib.yangtypes import YANGBool, YANGListType, YANGDynClass, ReferenceType
from pyangbind.lib.base import PybindBase
from decimal import Decimal
from bitarray import bitarray
import __builtin__
class fcoe_interface_bind(PybindBase):
  """
  This class was auto-generated by the PythonClass plugin for PYANG
  from YANG module brocade-interface - based on the path /interface/fcoe/fcoe-interface-bind. Each member element of
  the container is represented as a class variable - with a specific
  YANG type.

  YANG Description: Bind the FCoE interface to a Physical Ethernet Port.
  """
  __slots__ = ('_pybind_generated_by', '_path_helper', '_yang_name', '_rest_name', '_extmethods', '__fcoe_interface_bind_te','__fcoe_interface_bind_fo','__fcoe_interface_bind_po','__fcoe_interface_bind_mac','__fcoe_interface_bind_hu','__fcoe_interface_bind_name',)

  _yang_name = 'fcoe-interface-bind'
  _rest_name = 'bind'

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
    self.__fcoe_interface_bind_name = YANGDynClass(base=RestrictedClassType(base_type=unicode, restriction_dict={'length': [u'0..32']}), default=unicode(""), is_leaf=True, yang_name="fcoe-interface-bind-name", rest_name="", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'cli-drop-node-name': None}}, namespace='urn:brocade.com:mgmt:brocade-fcoe', defining_module='brocade-fcoe', yang_type='string', is_config=True)
    self.__fcoe_interface_bind_hu = YANGDynClass(base=YANGBool, is_leaf=True, yang_name="fcoe-interface-bind-hu", rest_name="HundredGigabitEthernet", parent=self, choice=(u'fcoe-interface-bind-type', u'fcoe-interface-bind-hu'), path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'info': u'Bind to HundredGigabitEthernet port', u'alt-name': u'HundredGigabitEthernet', u'sort-priority': u'RUNNCFG_INTERFACE_LEVEL_BASIC_CONFIG', u'cli-incomplete-command': None}}, namespace='urn:brocade.com:mgmt:brocade-fcoe', defining_module='brocade-fcoe', yang_type='empty', is_config=True)
    self.__fcoe_interface_bind_mac = YANGDynClass(base=YANGBool, is_leaf=True, yang_name="fcoe-interface-bind-mac", rest_name="mac-address", parent=self, choice=(u'fcoe-interface-bind-type', u'fcoe-interface-bind-mac'), path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'info': u'Bind to an Enode Mac-address', u'alt-name': u'mac-address', u'sort-priority': u'RUNNCFG_INTERFACE_LEVEL_BASIC_CONFIG', u'cli-incomplete-command': None}}, namespace='urn:brocade.com:mgmt:brocade-fcoe', defining_module='brocade-fcoe', yang_type='empty', is_config=True)
    self.__fcoe_interface_bind_po = YANGDynClass(base=YANGBool, is_leaf=True, yang_name="fcoe-interface-bind-po", rest_name="Port-channel", parent=self, choice=(u'fcoe-interface-bind-type', u'fcoe-interface-bind-po'), path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'info': u'Bind to Port-channel', u'alt-name': u'Port-channel', u'sort-priority': u'RUNNCFG_INTERFACE_LEVEL_BASIC_CONFIG', u'cli-incomplete-command': None}}, namespace='urn:brocade.com:mgmt:brocade-fcoe', defining_module='brocade-fcoe', yang_type='empty', is_config=True)
    self.__fcoe_interface_bind_fo = YANGDynClass(base=YANGBool, is_leaf=True, yang_name="fcoe-interface-bind-fo", rest_name="FortyGigabitEthernet", parent=self, choice=(u'fcoe-interface-bind-type', u'fcoe-interface-bind-fo'), path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'info': u'Bind to FortyGigabitEthernet port', u'alt-name': u'FortyGigabitEthernet', u'sort-priority': u'RUNNCFG_INTERFACE_LEVEL_BASIC_CONFIG', u'cli-incomplete-command': None}}, namespace='urn:brocade.com:mgmt:brocade-fcoe', defining_module='brocade-fcoe', yang_type='empty', is_config=True)
    self.__fcoe_interface_bind_te = YANGDynClass(base=YANGBool, is_leaf=True, yang_name="fcoe-interface-bind-te", rest_name="TenGigabitEthernet", parent=self, choice=(u'fcoe-interface-bind-type', u'fcoe-interface-bind-te'), path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'info': u'Bind to TenGigabitEthernet port', u'alt-name': u'TenGigabitEthernet', u'sort-priority': u'RUNNCFG_INTERFACE_LEVEL_BASIC_CONFIG', u'cli-incomplete-command': None}}, namespace='urn:brocade.com:mgmt:brocade-fcoe', defining_module='brocade-fcoe', yang_type='empty', is_config=True)

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
      return [u'interface', u'fcoe', u'fcoe-interface-bind']

  def _rest_path(self):
    if hasattr(self, "_parent"):
      if self._rest_name:
        return self._parent._rest_path()+[self._rest_name]
      else:
        return self._parent._rest_path()
    else:
      return [u'interface', u'Fcoe', u'bind']

  def _get_fcoe_interface_bind_te(self):
    """
    Getter method for fcoe_interface_bind_te, mapped from YANG variable /interface/fcoe/fcoe_interface_bind/fcoe_interface_bind_te (empty)

    YANG Description: Bind to TenGigabitEthernet port
    """
    return self.__fcoe_interface_bind_te
      
  def _set_fcoe_interface_bind_te(self, v, load=False):
    """
    Setter method for fcoe_interface_bind_te, mapped from YANG variable /interface/fcoe/fcoe_interface_bind/fcoe_interface_bind_te (empty)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_fcoe_interface_bind_te is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_fcoe_interface_bind_te() directly.

    YANG Description: Bind to TenGigabitEthernet port
    """
    if hasattr(v, "_utype"):
      v = v._utype(v)
    try:
      t = YANGDynClass(v,base=YANGBool, is_leaf=True, yang_name="fcoe-interface-bind-te", rest_name="TenGigabitEthernet", parent=self, choice=(u'fcoe-interface-bind-type', u'fcoe-interface-bind-te'), path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'info': u'Bind to TenGigabitEthernet port', u'alt-name': u'TenGigabitEthernet', u'sort-priority': u'RUNNCFG_INTERFACE_LEVEL_BASIC_CONFIG', u'cli-incomplete-command': None}}, namespace='urn:brocade.com:mgmt:brocade-fcoe', defining_module='brocade-fcoe', yang_type='empty', is_config=True)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """fcoe_interface_bind_te must be of a type compatible with empty""",
          'defined-type': "empty",
          'generated-type': """YANGDynClass(base=YANGBool, is_leaf=True, yang_name="fcoe-interface-bind-te", rest_name="TenGigabitEthernet", parent=self, choice=(u'fcoe-interface-bind-type', u'fcoe-interface-bind-te'), path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'info': u'Bind to TenGigabitEthernet port', u'alt-name': u'TenGigabitEthernet', u'sort-priority': u'RUNNCFG_INTERFACE_LEVEL_BASIC_CONFIG', u'cli-incomplete-command': None}}, namespace='urn:brocade.com:mgmt:brocade-fcoe', defining_module='brocade-fcoe', yang_type='empty', is_config=True)""",
        })

    self.__fcoe_interface_bind_te = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_fcoe_interface_bind_te(self):
    self.__fcoe_interface_bind_te = YANGDynClass(base=YANGBool, is_leaf=True, yang_name="fcoe-interface-bind-te", rest_name="TenGigabitEthernet", parent=self, choice=(u'fcoe-interface-bind-type', u'fcoe-interface-bind-te'), path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'info': u'Bind to TenGigabitEthernet port', u'alt-name': u'TenGigabitEthernet', u'sort-priority': u'RUNNCFG_INTERFACE_LEVEL_BASIC_CONFIG', u'cli-incomplete-command': None}}, namespace='urn:brocade.com:mgmt:brocade-fcoe', defining_module='brocade-fcoe', yang_type='empty', is_config=True)


  def _get_fcoe_interface_bind_fo(self):
    """
    Getter method for fcoe_interface_bind_fo, mapped from YANG variable /interface/fcoe/fcoe_interface_bind/fcoe_interface_bind_fo (empty)

    YANG Description: Bind to FortyGigabitEthernet port
    """
    return self.__fcoe_interface_bind_fo
      
  def _set_fcoe_interface_bind_fo(self, v, load=False):
    """
    Setter method for fcoe_interface_bind_fo, mapped from YANG variable /interface/fcoe/fcoe_interface_bind/fcoe_interface_bind_fo (empty)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_fcoe_interface_bind_fo is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_fcoe_interface_bind_fo() directly.

    YANG Description: Bind to FortyGigabitEthernet port
    """
    if hasattr(v, "_utype"):
      v = v._utype(v)
    try:
      t = YANGDynClass(v,base=YANGBool, is_leaf=True, yang_name="fcoe-interface-bind-fo", rest_name="FortyGigabitEthernet", parent=self, choice=(u'fcoe-interface-bind-type', u'fcoe-interface-bind-fo'), path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'info': u'Bind to FortyGigabitEthernet port', u'alt-name': u'FortyGigabitEthernet', u'sort-priority': u'RUNNCFG_INTERFACE_LEVEL_BASIC_CONFIG', u'cli-incomplete-command': None}}, namespace='urn:brocade.com:mgmt:brocade-fcoe', defining_module='brocade-fcoe', yang_type='empty', is_config=True)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """fcoe_interface_bind_fo must be of a type compatible with empty""",
          'defined-type': "empty",
          'generated-type': """YANGDynClass(base=YANGBool, is_leaf=True, yang_name="fcoe-interface-bind-fo", rest_name="FortyGigabitEthernet", parent=self, choice=(u'fcoe-interface-bind-type', u'fcoe-interface-bind-fo'), path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'info': u'Bind to FortyGigabitEthernet port', u'alt-name': u'FortyGigabitEthernet', u'sort-priority': u'RUNNCFG_INTERFACE_LEVEL_BASIC_CONFIG', u'cli-incomplete-command': None}}, namespace='urn:brocade.com:mgmt:brocade-fcoe', defining_module='brocade-fcoe', yang_type='empty', is_config=True)""",
        })

    self.__fcoe_interface_bind_fo = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_fcoe_interface_bind_fo(self):
    self.__fcoe_interface_bind_fo = YANGDynClass(base=YANGBool, is_leaf=True, yang_name="fcoe-interface-bind-fo", rest_name="FortyGigabitEthernet", parent=self, choice=(u'fcoe-interface-bind-type', u'fcoe-interface-bind-fo'), path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'info': u'Bind to FortyGigabitEthernet port', u'alt-name': u'FortyGigabitEthernet', u'sort-priority': u'RUNNCFG_INTERFACE_LEVEL_BASIC_CONFIG', u'cli-incomplete-command': None}}, namespace='urn:brocade.com:mgmt:brocade-fcoe', defining_module='brocade-fcoe', yang_type='empty', is_config=True)


  def _get_fcoe_interface_bind_po(self):
    """
    Getter method for fcoe_interface_bind_po, mapped from YANG variable /interface/fcoe/fcoe_interface_bind/fcoe_interface_bind_po (empty)

    YANG Description: Bind to Port-channel
    """
    return self.__fcoe_interface_bind_po
      
  def _set_fcoe_interface_bind_po(self, v, load=False):
    """
    Setter method for fcoe_interface_bind_po, mapped from YANG variable /interface/fcoe/fcoe_interface_bind/fcoe_interface_bind_po (empty)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_fcoe_interface_bind_po is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_fcoe_interface_bind_po() directly.

    YANG Description: Bind to Port-channel
    """
    if hasattr(v, "_utype"):
      v = v._utype(v)
    try:
      t = YANGDynClass(v,base=YANGBool, is_leaf=True, yang_name="fcoe-interface-bind-po", rest_name="Port-channel", parent=self, choice=(u'fcoe-interface-bind-type', u'fcoe-interface-bind-po'), path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'info': u'Bind to Port-channel', u'alt-name': u'Port-channel', u'sort-priority': u'RUNNCFG_INTERFACE_LEVEL_BASIC_CONFIG', u'cli-incomplete-command': None}}, namespace='urn:brocade.com:mgmt:brocade-fcoe', defining_module='brocade-fcoe', yang_type='empty', is_config=True)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """fcoe_interface_bind_po must be of a type compatible with empty""",
          'defined-type': "empty",
          'generated-type': """YANGDynClass(base=YANGBool, is_leaf=True, yang_name="fcoe-interface-bind-po", rest_name="Port-channel", parent=self, choice=(u'fcoe-interface-bind-type', u'fcoe-interface-bind-po'), path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'info': u'Bind to Port-channel', u'alt-name': u'Port-channel', u'sort-priority': u'RUNNCFG_INTERFACE_LEVEL_BASIC_CONFIG', u'cli-incomplete-command': None}}, namespace='urn:brocade.com:mgmt:brocade-fcoe', defining_module='brocade-fcoe', yang_type='empty', is_config=True)""",
        })

    self.__fcoe_interface_bind_po = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_fcoe_interface_bind_po(self):
    self.__fcoe_interface_bind_po = YANGDynClass(base=YANGBool, is_leaf=True, yang_name="fcoe-interface-bind-po", rest_name="Port-channel", parent=self, choice=(u'fcoe-interface-bind-type', u'fcoe-interface-bind-po'), path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'info': u'Bind to Port-channel', u'alt-name': u'Port-channel', u'sort-priority': u'RUNNCFG_INTERFACE_LEVEL_BASIC_CONFIG', u'cli-incomplete-command': None}}, namespace='urn:brocade.com:mgmt:brocade-fcoe', defining_module='brocade-fcoe', yang_type='empty', is_config=True)


  def _get_fcoe_interface_bind_mac(self):
    """
    Getter method for fcoe_interface_bind_mac, mapped from YANG variable /interface/fcoe/fcoe_interface_bind/fcoe_interface_bind_mac (empty)

    YANG Description: Bind to an Enode Mac-address
    """
    return self.__fcoe_interface_bind_mac
      
  def _set_fcoe_interface_bind_mac(self, v, load=False):
    """
    Setter method for fcoe_interface_bind_mac, mapped from YANG variable /interface/fcoe/fcoe_interface_bind/fcoe_interface_bind_mac (empty)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_fcoe_interface_bind_mac is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_fcoe_interface_bind_mac() directly.

    YANG Description: Bind to an Enode Mac-address
    """
    if hasattr(v, "_utype"):
      v = v._utype(v)
    try:
      t = YANGDynClass(v,base=YANGBool, is_leaf=True, yang_name="fcoe-interface-bind-mac", rest_name="mac-address", parent=self, choice=(u'fcoe-interface-bind-type', u'fcoe-interface-bind-mac'), path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'info': u'Bind to an Enode Mac-address', u'alt-name': u'mac-address', u'sort-priority': u'RUNNCFG_INTERFACE_LEVEL_BASIC_CONFIG', u'cli-incomplete-command': None}}, namespace='urn:brocade.com:mgmt:brocade-fcoe', defining_module='brocade-fcoe', yang_type='empty', is_config=True)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """fcoe_interface_bind_mac must be of a type compatible with empty""",
          'defined-type': "empty",
          'generated-type': """YANGDynClass(base=YANGBool, is_leaf=True, yang_name="fcoe-interface-bind-mac", rest_name="mac-address", parent=self, choice=(u'fcoe-interface-bind-type', u'fcoe-interface-bind-mac'), path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'info': u'Bind to an Enode Mac-address', u'alt-name': u'mac-address', u'sort-priority': u'RUNNCFG_INTERFACE_LEVEL_BASIC_CONFIG', u'cli-incomplete-command': None}}, namespace='urn:brocade.com:mgmt:brocade-fcoe', defining_module='brocade-fcoe', yang_type='empty', is_config=True)""",
        })

    self.__fcoe_interface_bind_mac = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_fcoe_interface_bind_mac(self):
    self.__fcoe_interface_bind_mac = YANGDynClass(base=YANGBool, is_leaf=True, yang_name="fcoe-interface-bind-mac", rest_name="mac-address", parent=self, choice=(u'fcoe-interface-bind-type', u'fcoe-interface-bind-mac'), path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'info': u'Bind to an Enode Mac-address', u'alt-name': u'mac-address', u'sort-priority': u'RUNNCFG_INTERFACE_LEVEL_BASIC_CONFIG', u'cli-incomplete-command': None}}, namespace='urn:brocade.com:mgmt:brocade-fcoe', defining_module='brocade-fcoe', yang_type='empty', is_config=True)


  def _get_fcoe_interface_bind_hu(self):
    """
    Getter method for fcoe_interface_bind_hu, mapped from YANG variable /interface/fcoe/fcoe_interface_bind/fcoe_interface_bind_hu (empty)

    YANG Description: Bind to HundredGigabitEthernet port
    """
    return self.__fcoe_interface_bind_hu
      
  def _set_fcoe_interface_bind_hu(self, v, load=False):
    """
    Setter method for fcoe_interface_bind_hu, mapped from YANG variable /interface/fcoe/fcoe_interface_bind/fcoe_interface_bind_hu (empty)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_fcoe_interface_bind_hu is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_fcoe_interface_bind_hu() directly.

    YANG Description: Bind to HundredGigabitEthernet port
    """
    if hasattr(v, "_utype"):
      v = v._utype(v)
    try:
      t = YANGDynClass(v,base=YANGBool, is_leaf=True, yang_name="fcoe-interface-bind-hu", rest_name="HundredGigabitEthernet", parent=self, choice=(u'fcoe-interface-bind-type', u'fcoe-interface-bind-hu'), path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'info': u'Bind to HundredGigabitEthernet port', u'alt-name': u'HundredGigabitEthernet', u'sort-priority': u'RUNNCFG_INTERFACE_LEVEL_BASIC_CONFIG', u'cli-incomplete-command': None}}, namespace='urn:brocade.com:mgmt:brocade-fcoe', defining_module='brocade-fcoe', yang_type='empty', is_config=True)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """fcoe_interface_bind_hu must be of a type compatible with empty""",
          'defined-type': "empty",
          'generated-type': """YANGDynClass(base=YANGBool, is_leaf=True, yang_name="fcoe-interface-bind-hu", rest_name="HundredGigabitEthernet", parent=self, choice=(u'fcoe-interface-bind-type', u'fcoe-interface-bind-hu'), path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'info': u'Bind to HundredGigabitEthernet port', u'alt-name': u'HundredGigabitEthernet', u'sort-priority': u'RUNNCFG_INTERFACE_LEVEL_BASIC_CONFIG', u'cli-incomplete-command': None}}, namespace='urn:brocade.com:mgmt:brocade-fcoe', defining_module='brocade-fcoe', yang_type='empty', is_config=True)""",
        })

    self.__fcoe_interface_bind_hu = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_fcoe_interface_bind_hu(self):
    self.__fcoe_interface_bind_hu = YANGDynClass(base=YANGBool, is_leaf=True, yang_name="fcoe-interface-bind-hu", rest_name="HundredGigabitEthernet", parent=self, choice=(u'fcoe-interface-bind-type', u'fcoe-interface-bind-hu'), path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'info': u'Bind to HundredGigabitEthernet port', u'alt-name': u'HundredGigabitEthernet', u'sort-priority': u'RUNNCFG_INTERFACE_LEVEL_BASIC_CONFIG', u'cli-incomplete-command': None}}, namespace='urn:brocade.com:mgmt:brocade-fcoe', defining_module='brocade-fcoe', yang_type='empty', is_config=True)


  def _get_fcoe_interface_bind_name(self):
    """
    Getter method for fcoe_interface_bind_name, mapped from YANG variable /interface/fcoe/fcoe_interface_bind/fcoe_interface_bind_name (string)

    YANG Description: Interface name or Enode mac address
    """
    return self.__fcoe_interface_bind_name
      
  def _set_fcoe_interface_bind_name(self, v, load=False):
    """
    Setter method for fcoe_interface_bind_name, mapped from YANG variable /interface/fcoe/fcoe_interface_bind/fcoe_interface_bind_name (string)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_fcoe_interface_bind_name is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_fcoe_interface_bind_name() directly.

    YANG Description: Interface name or Enode mac address
    """
    if hasattr(v, "_utype"):
      v = v._utype(v)
    try:
      t = YANGDynClass(v,base=RestrictedClassType(base_type=unicode, restriction_dict={'length': [u'0..32']}), default=unicode(""), is_leaf=True, yang_name="fcoe-interface-bind-name", rest_name="", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'cli-drop-node-name': None}}, namespace='urn:brocade.com:mgmt:brocade-fcoe', defining_module='brocade-fcoe', yang_type='string', is_config=True)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """fcoe_interface_bind_name must be of a type compatible with string""",
          'defined-type': "string",
          'generated-type': """YANGDynClass(base=RestrictedClassType(base_type=unicode, restriction_dict={'length': [u'0..32']}), default=unicode(""), is_leaf=True, yang_name="fcoe-interface-bind-name", rest_name="", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'cli-drop-node-name': None}}, namespace='urn:brocade.com:mgmt:brocade-fcoe', defining_module='brocade-fcoe', yang_type='string', is_config=True)""",
        })

    self.__fcoe_interface_bind_name = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_fcoe_interface_bind_name(self):
    self.__fcoe_interface_bind_name = YANGDynClass(base=RestrictedClassType(base_type=unicode, restriction_dict={'length': [u'0..32']}), default=unicode(""), is_leaf=True, yang_name="fcoe-interface-bind-name", rest_name="", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'cli-drop-node-name': None}}, namespace='urn:brocade.com:mgmt:brocade-fcoe', defining_module='brocade-fcoe', yang_type='string', is_config=True)

  fcoe_interface_bind_te = __builtin__.property(_get_fcoe_interface_bind_te, _set_fcoe_interface_bind_te)
  fcoe_interface_bind_fo = __builtin__.property(_get_fcoe_interface_bind_fo, _set_fcoe_interface_bind_fo)
  fcoe_interface_bind_po = __builtin__.property(_get_fcoe_interface_bind_po, _set_fcoe_interface_bind_po)
  fcoe_interface_bind_mac = __builtin__.property(_get_fcoe_interface_bind_mac, _set_fcoe_interface_bind_mac)
  fcoe_interface_bind_hu = __builtin__.property(_get_fcoe_interface_bind_hu, _set_fcoe_interface_bind_hu)
  fcoe_interface_bind_name = __builtin__.property(_get_fcoe_interface_bind_name, _set_fcoe_interface_bind_name)

  __choices__ = {u'fcoe-interface-bind-type': {u'fcoe-interface-bind-mac': [u'fcoe_interface_bind_mac'], u'fcoe-interface-bind-te': [u'fcoe_interface_bind_te'], u'fcoe-interface-bind-fo': [u'fcoe_interface_bind_fo'], u'fcoe-interface-bind-hu': [u'fcoe_interface_bind_hu'], u'fcoe-interface-bind-po': [u'fcoe_interface_bind_po']}}
  _pyangbind_elements = {'fcoe_interface_bind_te': fcoe_interface_bind_te, 'fcoe_interface_bind_fo': fcoe_interface_bind_fo, 'fcoe_interface_bind_po': fcoe_interface_bind_po, 'fcoe_interface_bind_mac': fcoe_interface_bind_mac, 'fcoe_interface_bind_hu': fcoe_interface_bind_hu, 'fcoe_interface_bind_name': fcoe_interface_bind_name, }


