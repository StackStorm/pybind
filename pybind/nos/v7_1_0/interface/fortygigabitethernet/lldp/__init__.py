
from operator import attrgetter
import pyangbind.lib.xpathhelper as xpathhelper
from pyangbind.lib.yangtypes import RestrictedPrecisionDecimalType, RestrictedClassType, TypedListType
from pyangbind.lib.yangtypes import YANGBool, YANGListType, YANGDynClass, ReferenceType
from pyangbind.lib.base import PybindBase
from decimal import Decimal
from bitarray import bitarray
import __builtin__
import cee
class lldp(PybindBase):
  """
  This class was auto-generated by the PythonClass plugin for PYANG
  from YANG module brocade-interface - based on the path /interface/fortygigabitethernet/lldp. Each member element of
  the container is represented as a class variable - with a specific
  YANG type.
  """
  __slots__ = ('_pybind_generated_by', '_path_helper', '_yang_name', '_rest_name', '_extmethods', '__cee','__dcbx_version','__disable','__iscsi_priority','__profile',)

  _yang_name = 'lldp'
  _rest_name = 'lldp'

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
    self.__dcbx_version = YANGDynClass(base=RestrictedClassType(base_type=unicode,                                     restriction_type="dict_key",                                     restriction_arg={u'auto': {'value': 0}, u'cee': {'value': 1}},), default=unicode("auto"), is_leaf=True, yang_name="dcbx-version", rest_name="dcbx-version", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'cli-full-command': None, u'info': u'Set up DCBX Version'}}, namespace='urn:brocade.com:mgmt:brocade-lldp', defining_module='brocade-lldp', yang_type='enumeration', is_config=True)
    self.__iscsi_priority = YANGDynClass(base=RestrictedClassType(base_type=RestrictedClassType(base_type=long, restriction_dict={'range': ['0..4294967295']}, int_size=32), restriction_dict={'range': [u'0..7']}), default=RestrictedClassType(base_type=long, restriction_dict={'range': ['0..4294967295']}, int_size=32)(4), is_leaf=True, yang_name="iscsi-priority", rest_name="iscsi-priority", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'cli-full-command': None, u'info': u'Configure the Ethernet priority to advertise for iSCSI on this interface'}}, namespace='urn:brocade.com:mgmt:brocade-lldp', defining_module='brocade-lldp', yang_type='uint32', is_config=True)
    self.__cee = YANGDynClass(base=cee.cee, is_container='container', presence=False, yang_name="cee", rest_name="cee", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'hidden': u'debug', u'cli-suppress-no': None}}, namespace='urn:brocade.com:mgmt:brocade-lldp', defining_module='brocade-lldp', yang_type='container', is_config=True)
    self.__disable = YANGDynClass(base=YANGBool, is_leaf=True, yang_name="disable", rest_name="disable", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'cli-full-command': None, u'info': u'Disable LLDP on the Interface.'}}, namespace='urn:brocade.com:mgmt:brocade-lldp', defining_module='brocade-lldp', yang_type='empty', is_config=True)
    self.__profile = YANGDynClass(base=RestrictedClassType(base_type=unicode, restriction_dict={'pattern': u'(\\S)+', 'length': [u'1..32']}), is_leaf=True, yang_name="profile", rest_name="profile", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'cli-full-command': None, u'info': u'The LLDP profile on the interface.'}}, namespace='urn:brocade.com:mgmt:brocade-lldp', defining_module='brocade-lldp', yang_type='string', is_config=True)

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
      return [u'interface', u'fortygigabitethernet', u'lldp']

  def _rest_path(self):
    if hasattr(self, "_parent"):
      if self._rest_name:
        return self._parent._rest_path()+[self._rest_name]
      else:
        return self._parent._rest_path()
    else:
      return [u'interface', u'FortyGigabitEthernet', u'lldp']

  def _get_cee(self):
    """
    Getter method for cee, mapped from YANG variable /interface/fortygigabitethernet/lldp/cee (container)

    YANG Description: Generate CEE capable event
    """
    return self.__cee
      
  def _set_cee(self, v, load=False):
    """
    Setter method for cee, mapped from YANG variable /interface/fortygigabitethernet/lldp/cee (container)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_cee is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_cee() directly.

    YANG Description: Generate CEE capable event
    """
    if hasattr(v, "_utype"):
      v = v._utype(v)
    try:
      t = YANGDynClass(v,base=cee.cee, is_container='container', presence=False, yang_name="cee", rest_name="cee", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'hidden': u'debug', u'cli-suppress-no': None}}, namespace='urn:brocade.com:mgmt:brocade-lldp', defining_module='brocade-lldp', yang_type='container', is_config=True)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """cee must be of a type compatible with container""",
          'defined-type': "container",
          'generated-type': """YANGDynClass(base=cee.cee, is_container='container', presence=False, yang_name="cee", rest_name="cee", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'hidden': u'debug', u'cli-suppress-no': None}}, namespace='urn:brocade.com:mgmt:brocade-lldp', defining_module='brocade-lldp', yang_type='container', is_config=True)""",
        })

    self.__cee = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_cee(self):
    self.__cee = YANGDynClass(base=cee.cee, is_container='container', presence=False, yang_name="cee", rest_name="cee", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'hidden': u'debug', u'cli-suppress-no': None}}, namespace='urn:brocade.com:mgmt:brocade-lldp', defining_module='brocade-lldp', yang_type='container', is_config=True)


  def _get_dcbx_version(self):
    """
    Getter method for dcbx_version, mapped from YANG variable /interface/fortygigabitethernet/lldp/dcbx_version (enumeration)
    """
    return self.__dcbx_version
      
  def _set_dcbx_version(self, v, load=False):
    """
    Setter method for dcbx_version, mapped from YANG variable /interface/fortygigabitethernet/lldp/dcbx_version (enumeration)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_dcbx_version is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_dcbx_version() directly.
    """
    if hasattr(v, "_utype"):
      v = v._utype(v)
    try:
      t = YANGDynClass(v,base=RestrictedClassType(base_type=unicode,                                     restriction_type="dict_key",                                     restriction_arg={u'auto': {'value': 0}, u'cee': {'value': 1}},), default=unicode("auto"), is_leaf=True, yang_name="dcbx-version", rest_name="dcbx-version", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'cli-full-command': None, u'info': u'Set up DCBX Version'}}, namespace='urn:brocade.com:mgmt:brocade-lldp', defining_module='brocade-lldp', yang_type='enumeration', is_config=True)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """dcbx_version must be of a type compatible with enumeration""",
          'defined-type': "brocade-lldp:enumeration",
          'generated-type': """YANGDynClass(base=RestrictedClassType(base_type=unicode,                                     restriction_type="dict_key",                                     restriction_arg={u'auto': {'value': 0}, u'cee': {'value': 1}},), default=unicode("auto"), is_leaf=True, yang_name="dcbx-version", rest_name="dcbx-version", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'cli-full-command': None, u'info': u'Set up DCBX Version'}}, namespace='urn:brocade.com:mgmt:brocade-lldp', defining_module='brocade-lldp', yang_type='enumeration', is_config=True)""",
        })

    self.__dcbx_version = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_dcbx_version(self):
    self.__dcbx_version = YANGDynClass(base=RestrictedClassType(base_type=unicode,                                     restriction_type="dict_key",                                     restriction_arg={u'auto': {'value': 0}, u'cee': {'value': 1}},), default=unicode("auto"), is_leaf=True, yang_name="dcbx-version", rest_name="dcbx-version", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'cli-full-command': None, u'info': u'Set up DCBX Version'}}, namespace='urn:brocade.com:mgmt:brocade-lldp', defining_module='brocade-lldp', yang_type='enumeration', is_config=True)


  def _get_disable(self):
    """
    Getter method for disable, mapped from YANG variable /interface/fortygigabitethernet/lldp/disable (empty)
    """
    return self.__disable
      
  def _set_disable(self, v, load=False):
    """
    Setter method for disable, mapped from YANG variable /interface/fortygigabitethernet/lldp/disable (empty)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_disable is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_disable() directly.
    """
    if hasattr(v, "_utype"):
      v = v._utype(v)
    try:
      t = YANGDynClass(v,base=YANGBool, is_leaf=True, yang_name="disable", rest_name="disable", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'cli-full-command': None, u'info': u'Disable LLDP on the Interface.'}}, namespace='urn:brocade.com:mgmt:brocade-lldp', defining_module='brocade-lldp', yang_type='empty', is_config=True)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """disable must be of a type compatible with empty""",
          'defined-type': "empty",
          'generated-type': """YANGDynClass(base=YANGBool, is_leaf=True, yang_name="disable", rest_name="disable", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'cli-full-command': None, u'info': u'Disable LLDP on the Interface.'}}, namespace='urn:brocade.com:mgmt:brocade-lldp', defining_module='brocade-lldp', yang_type='empty', is_config=True)""",
        })

    self.__disable = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_disable(self):
    self.__disable = YANGDynClass(base=YANGBool, is_leaf=True, yang_name="disable", rest_name="disable", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'cli-full-command': None, u'info': u'Disable LLDP on the Interface.'}}, namespace='urn:brocade.com:mgmt:brocade-lldp', defining_module='brocade-lldp', yang_type='empty', is_config=True)


  def _get_iscsi_priority(self):
    """
    Getter method for iscsi_priority, mapped from YANG variable /interface/fortygigabitethernet/lldp/iscsi_priority (uint32)
    """
    return self.__iscsi_priority
      
  def _set_iscsi_priority(self, v, load=False):
    """
    Setter method for iscsi_priority, mapped from YANG variable /interface/fortygigabitethernet/lldp/iscsi_priority (uint32)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_iscsi_priority is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_iscsi_priority() directly.
    """
    if hasattr(v, "_utype"):
      v = v._utype(v)
    try:
      t = YANGDynClass(v,base=RestrictedClassType(base_type=RestrictedClassType(base_type=long, restriction_dict={'range': ['0..4294967295']}, int_size=32), restriction_dict={'range': [u'0..7']}), default=RestrictedClassType(base_type=long, restriction_dict={'range': ['0..4294967295']}, int_size=32)(4), is_leaf=True, yang_name="iscsi-priority", rest_name="iscsi-priority", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'cli-full-command': None, u'info': u'Configure the Ethernet priority to advertise for iSCSI on this interface'}}, namespace='urn:brocade.com:mgmt:brocade-lldp', defining_module='brocade-lldp', yang_type='uint32', is_config=True)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """iscsi_priority must be of a type compatible with uint32""",
          'defined-type': "uint32",
          'generated-type': """YANGDynClass(base=RestrictedClassType(base_type=RestrictedClassType(base_type=long, restriction_dict={'range': ['0..4294967295']}, int_size=32), restriction_dict={'range': [u'0..7']}), default=RestrictedClassType(base_type=long, restriction_dict={'range': ['0..4294967295']}, int_size=32)(4), is_leaf=True, yang_name="iscsi-priority", rest_name="iscsi-priority", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'cli-full-command': None, u'info': u'Configure the Ethernet priority to advertise for iSCSI on this interface'}}, namespace='urn:brocade.com:mgmt:brocade-lldp', defining_module='brocade-lldp', yang_type='uint32', is_config=True)""",
        })

    self.__iscsi_priority = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_iscsi_priority(self):
    self.__iscsi_priority = YANGDynClass(base=RestrictedClassType(base_type=RestrictedClassType(base_type=long, restriction_dict={'range': ['0..4294967295']}, int_size=32), restriction_dict={'range': [u'0..7']}), default=RestrictedClassType(base_type=long, restriction_dict={'range': ['0..4294967295']}, int_size=32)(4), is_leaf=True, yang_name="iscsi-priority", rest_name="iscsi-priority", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'cli-full-command': None, u'info': u'Configure the Ethernet priority to advertise for iSCSI on this interface'}}, namespace='urn:brocade.com:mgmt:brocade-lldp', defining_module='brocade-lldp', yang_type='uint32', is_config=True)


  def _get_profile(self):
    """
    Getter method for profile, mapped from YANG variable /interface/fortygigabitethernet/lldp/profile (string)
    """
    return self.__profile
      
  def _set_profile(self, v, load=False):
    """
    Setter method for profile, mapped from YANG variable /interface/fortygigabitethernet/lldp/profile (string)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_profile is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_profile() directly.
    """
    if hasattr(v, "_utype"):
      v = v._utype(v)
    try:
      t = YANGDynClass(v,base=RestrictedClassType(base_type=unicode, restriction_dict={'pattern': u'(\\S)+', 'length': [u'1..32']}), is_leaf=True, yang_name="profile", rest_name="profile", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'cli-full-command': None, u'info': u'The LLDP profile on the interface.'}}, namespace='urn:brocade.com:mgmt:brocade-lldp', defining_module='brocade-lldp', yang_type='string', is_config=True)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """profile must be of a type compatible with string""",
          'defined-type': "string",
          'generated-type': """YANGDynClass(base=RestrictedClassType(base_type=unicode, restriction_dict={'pattern': u'(\\S)+', 'length': [u'1..32']}), is_leaf=True, yang_name="profile", rest_name="profile", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'cli-full-command': None, u'info': u'The LLDP profile on the interface.'}}, namespace='urn:brocade.com:mgmt:brocade-lldp', defining_module='brocade-lldp', yang_type='string', is_config=True)""",
        })

    self.__profile = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_profile(self):
    self.__profile = YANGDynClass(base=RestrictedClassType(base_type=unicode, restriction_dict={'pattern': u'(\\S)+', 'length': [u'1..32']}), is_leaf=True, yang_name="profile", rest_name="profile", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'cli-full-command': None, u'info': u'The LLDP profile on the interface.'}}, namespace='urn:brocade.com:mgmt:brocade-lldp', defining_module='brocade-lldp', yang_type='string', is_config=True)

  cee = __builtin__.property(_get_cee, _set_cee)
  dcbx_version = __builtin__.property(_get_dcbx_version, _set_dcbx_version)
  disable = __builtin__.property(_get_disable, _set_disable)
  iscsi_priority = __builtin__.property(_get_iscsi_priority, _set_iscsi_priority)
  profile = __builtin__.property(_get_profile, _set_profile)


  _pyangbind_elements = {'cee': cee, 'dcbx_version': dcbx_version, 'disable': disable, 'iscsi_priority': iscsi_priority, 'profile': profile, }


