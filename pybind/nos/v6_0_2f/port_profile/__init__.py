
from operator import attrgetter
import pyangbind.lib.xpathhelper as xpathhelper
from pyangbind.lib.yangtypes import RestrictedPrecisionDecimalType, RestrictedClassType, TypedListType
from pyangbind.lib.yangtypes import YANGBool, YANGListType, YANGDynClass, ReferenceType
from pyangbind.lib.base import PybindBase
from decimal import Decimal
from bitarray import bitarray
import __builtin__
import allow
import vlan_profile
import fcoe_profile
import qos_profile
import security_profile
import restrict_flooding_container
class port_profile(PybindBase):
  """
  This class was auto-generated by the PythonClass plugin for PYANG
  from YANG module brocade-port-profile - based on the path /port-profile. Each member element of
  the container is represented as a class variable - with a specific
  YANG type.

  YANG Description: The list of port-profiles in the managed device. Each row
represents port profile name and its subprofiles.
  """
  __slots__ = ('_pybind_generated_by', '_path_helper', '_yang_name', '_rest_name', '_extmethods', '__name','__allow','__vlan_profile','__fcoe_profile','__qos_profile','__security_profile','__restrict_flooding_container',)

  _yang_name = 'port-profile'
  _rest_name = 'port-profile'

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
    self.__name = YANGDynClass(base=RestrictedClassType(base_type=unicode, restriction_dict={'pattern': u'[a-zA-Z]{1}([-a-zA-Z0-9\\.\\\\\\\\@#\\+\\*\\(\\)=\\{~\\}%<>=$_\\[\\]\\|]{0,127})'}), is_leaf=True, yang_name="name", rest_name="name", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'info': u'Port-profile name (Max Size - 128)'}}, is_keyval=True, namespace='urn:brocade.com:mgmt:brocade-port-profile', defining_module='brocade-port-profile', yang_type='common-def:name-string128', is_config=True)
    self.__fcoe_profile = YANGDynClass(base=fcoe_profile.fcoe_profile, is_container='container', presence=True, yang_name="fcoe-profile", rest_name="fcoe-profile", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'cli-full-command': None, u'cli-add-mode': None, u'callpoint': u'fcoe-profile-config', u'info': u'FCoE profile', u'cli-full-no': None}}, namespace='urn:brocade.com:mgmt:brocade-port-profile', defining_module='brocade-port-profile', yang_type='container', is_config=True)
    self.__restrict_flooding_container = YANGDynClass(base=restrict_flooding_container.restrict_flooding_container, is_container='container', presence=False, yang_name="restrict-flooding-container", rest_name="", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'cli-drop-node-name': None, u'display-when': u'../name = "default"'}}, namespace='urn:brocade.com:mgmt:brocade-port-profile', defining_module='brocade-port-profile', yang_type='container', is_config=True)
    self.__vlan_profile = YANGDynClass(base=vlan_profile.vlan_profile, is_container='container', presence=True, yang_name="vlan-profile", rest_name="vlan-profile", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'cli-full-command': None, u'cli-add-mode': None, u'callpoint': u'vlan-profile-config', u'info': u'VLAN profile', u'cli-full-no': None}}, namespace='urn:brocade.com:mgmt:brocade-port-profile', defining_module='brocade-port-profile', yang_type='container', is_config=True)
    self.__allow = YANGDynClass(base=allow.allow, is_container='container', presence=False, yang_name="allow", rest_name="allow", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'info': u'Allow/Drop non-profiled macs', u'display-when': u'../name = "default"', u'cli-incomplete-no': None}}, namespace='urn:brocade.com:mgmt:brocade-port-profile', defining_module='brocade-port-profile', yang_type='container', is_config=True)
    self.__qos_profile = YANGDynClass(base=qos_profile.qos_profile, is_container='container', presence=True, yang_name="qos-profile", rest_name="qos-profile", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'cli-full-command': None, u'cli-add-mode': None, u'cli-full-no': None, u'info': u'QoS profile', u'callpoint': u'qos-profile-config'}}, namespace='urn:brocade.com:mgmt:brocade-port-profile', defining_module='brocade-port-profile', yang_type='container', is_config=True)
    self.__security_profile = YANGDynClass(base=security_profile.security_profile, is_container='container', presence=True, yang_name="security-profile", rest_name="security-profile", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'cli-full-command': None, u'cli-add-mode': None, u'cli-full-no': None, u'info': u'Security profile', u'callpoint': u'security-profile-config'}}, namespace='urn:brocade.com:mgmt:brocade-port-profile', defining_module='brocade-port-profile', yang_type='container', is_config=True)

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
      return [u'port-profile']

  def _rest_path(self):
    if hasattr(self, "_parent"):
      if self._rest_name:
        return self._parent._rest_path()+[self._rest_name]
      else:
        return self._parent._rest_path()
    else:
      return [u'port-profile']

  def _get_name(self):
    """
    Getter method for name, mapped from YANG variable /port_profile/name (common-def:name-string128)

    YANG Description: The name of the port-profile.
    """
    return self.__name
      
  def _set_name(self, v, load=False):
    """
    Setter method for name, mapped from YANG variable /port_profile/name (common-def:name-string128)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_name is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_name() directly.

    YANG Description: The name of the port-profile.
    """
    parent = getattr(self, "_parent", None)
    if parent is not None and load is False:
      raise AttributeError("Cannot set keys directly when" +
                             " within an instantiated list")

    if hasattr(v, "_utype"):
      v = v._utype(v)
    try:
      t = YANGDynClass(v,base=RestrictedClassType(base_type=unicode, restriction_dict={'pattern': u'[a-zA-Z]{1}([-a-zA-Z0-9\\.\\\\\\\\@#\\+\\*\\(\\)=\\{~\\}%<>=$_\\[\\]\\|]{0,127})'}), is_leaf=True, yang_name="name", rest_name="name", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'info': u'Port-profile name (Max Size - 128)'}}, is_keyval=True, namespace='urn:brocade.com:mgmt:brocade-port-profile', defining_module='brocade-port-profile', yang_type='common-def:name-string128', is_config=True)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """name must be of a type compatible with common-def:name-string128""",
          'defined-type': "common-def:name-string128",
          'generated-type': """YANGDynClass(base=RestrictedClassType(base_type=unicode, restriction_dict={'pattern': u'[a-zA-Z]{1}([-a-zA-Z0-9\\.\\\\\\\\@#\\+\\*\\(\\)=\\{~\\}%<>=$_\\[\\]\\|]{0,127})'}), is_leaf=True, yang_name="name", rest_name="name", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'info': u'Port-profile name (Max Size - 128)'}}, is_keyval=True, namespace='urn:brocade.com:mgmt:brocade-port-profile', defining_module='brocade-port-profile', yang_type='common-def:name-string128', is_config=True)""",
        })

    self.__name = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_name(self):
    self.__name = YANGDynClass(base=RestrictedClassType(base_type=unicode, restriction_dict={'pattern': u'[a-zA-Z]{1}([-a-zA-Z0-9\\.\\\\\\\\@#\\+\\*\\(\\)=\\{~\\}%<>=$_\\[\\]\\|]{0,127})'}), is_leaf=True, yang_name="name", rest_name="name", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'info': u'Port-profile name (Max Size - 128)'}}, is_keyval=True, namespace='urn:brocade.com:mgmt:brocade-port-profile', defining_module='brocade-port-profile', yang_type='common-def:name-string128', is_config=True)


  def _get_allow(self):
    """
    Getter method for allow, mapped from YANG variable /port_profile/allow (container)

    YANG Description: Allow/Drop non-profiled macs
    """
    return self.__allow
      
  def _set_allow(self, v, load=False):
    """
    Setter method for allow, mapped from YANG variable /port_profile/allow (container)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_allow is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_allow() directly.

    YANG Description: Allow/Drop non-profiled macs
    """
    if hasattr(v, "_utype"):
      v = v._utype(v)
    try:
      t = YANGDynClass(v,base=allow.allow, is_container='container', presence=False, yang_name="allow", rest_name="allow", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'info': u'Allow/Drop non-profiled macs', u'display-when': u'../name = "default"', u'cli-incomplete-no': None}}, namespace='urn:brocade.com:mgmt:brocade-port-profile', defining_module='brocade-port-profile', yang_type='container', is_config=True)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """allow must be of a type compatible with container""",
          'defined-type': "container",
          'generated-type': """YANGDynClass(base=allow.allow, is_container='container', presence=False, yang_name="allow", rest_name="allow", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'info': u'Allow/Drop non-profiled macs', u'display-when': u'../name = "default"', u'cli-incomplete-no': None}}, namespace='urn:brocade.com:mgmt:brocade-port-profile', defining_module='brocade-port-profile', yang_type='container', is_config=True)""",
        })

    self.__allow = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_allow(self):
    self.__allow = YANGDynClass(base=allow.allow, is_container='container', presence=False, yang_name="allow", rest_name="allow", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'info': u'Allow/Drop non-profiled macs', u'display-when': u'../name = "default"', u'cli-incomplete-no': None}}, namespace='urn:brocade.com:mgmt:brocade-port-profile', defining_module='brocade-port-profile', yang_type='container', is_config=True)


  def _get_vlan_profile(self):
    """
    Getter method for vlan_profile, mapped from YANG variable /port_profile/vlan_profile (container)

    YANG Description: The Vlan profile.
    """
    return self.__vlan_profile
      
  def _set_vlan_profile(self, v, load=False):
    """
    Setter method for vlan_profile, mapped from YANG variable /port_profile/vlan_profile (container)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_vlan_profile is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_vlan_profile() directly.

    YANG Description: The Vlan profile.
    """
    if hasattr(v, "_utype"):
      v = v._utype(v)
    try:
      t = YANGDynClass(v,base=vlan_profile.vlan_profile, is_container='container', presence=True, yang_name="vlan-profile", rest_name="vlan-profile", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'cli-full-command': None, u'cli-add-mode': None, u'callpoint': u'vlan-profile-config', u'info': u'VLAN profile', u'cli-full-no': None}}, namespace='urn:brocade.com:mgmt:brocade-port-profile', defining_module='brocade-port-profile', yang_type='container', is_config=True)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """vlan_profile must be of a type compatible with container""",
          'defined-type': "container",
          'generated-type': """YANGDynClass(base=vlan_profile.vlan_profile, is_container='container', presence=True, yang_name="vlan-profile", rest_name="vlan-profile", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'cli-full-command': None, u'cli-add-mode': None, u'callpoint': u'vlan-profile-config', u'info': u'VLAN profile', u'cli-full-no': None}}, namespace='urn:brocade.com:mgmt:brocade-port-profile', defining_module='brocade-port-profile', yang_type='container', is_config=True)""",
        })

    self.__vlan_profile = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_vlan_profile(self):
    self.__vlan_profile = YANGDynClass(base=vlan_profile.vlan_profile, is_container='container', presence=True, yang_name="vlan-profile", rest_name="vlan-profile", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'cli-full-command': None, u'cli-add-mode': None, u'callpoint': u'vlan-profile-config', u'info': u'VLAN profile', u'cli-full-no': None}}, namespace='urn:brocade.com:mgmt:brocade-port-profile', defining_module='brocade-port-profile', yang_type='container', is_config=True)


  def _get_fcoe_profile(self):
    """
    Getter method for fcoe_profile, mapped from YANG variable /port_profile/fcoe_profile (container)

    YANG Description: The FCoE profile.
    """
    return self.__fcoe_profile
      
  def _set_fcoe_profile(self, v, load=False):
    """
    Setter method for fcoe_profile, mapped from YANG variable /port_profile/fcoe_profile (container)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_fcoe_profile is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_fcoe_profile() directly.

    YANG Description: The FCoE profile.
    """
    if hasattr(v, "_utype"):
      v = v._utype(v)
    try:
      t = YANGDynClass(v,base=fcoe_profile.fcoe_profile, is_container='container', presence=True, yang_name="fcoe-profile", rest_name="fcoe-profile", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'cli-full-command': None, u'cli-add-mode': None, u'callpoint': u'fcoe-profile-config', u'info': u'FCoE profile', u'cli-full-no': None}}, namespace='urn:brocade.com:mgmt:brocade-port-profile', defining_module='brocade-port-profile', yang_type='container', is_config=True)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """fcoe_profile must be of a type compatible with container""",
          'defined-type': "container",
          'generated-type': """YANGDynClass(base=fcoe_profile.fcoe_profile, is_container='container', presence=True, yang_name="fcoe-profile", rest_name="fcoe-profile", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'cli-full-command': None, u'cli-add-mode': None, u'callpoint': u'fcoe-profile-config', u'info': u'FCoE profile', u'cli-full-no': None}}, namespace='urn:brocade.com:mgmt:brocade-port-profile', defining_module='brocade-port-profile', yang_type='container', is_config=True)""",
        })

    self.__fcoe_profile = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_fcoe_profile(self):
    self.__fcoe_profile = YANGDynClass(base=fcoe_profile.fcoe_profile, is_container='container', presence=True, yang_name="fcoe-profile", rest_name="fcoe-profile", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'cli-full-command': None, u'cli-add-mode': None, u'callpoint': u'fcoe-profile-config', u'info': u'FCoE profile', u'cli-full-no': None}}, namespace='urn:brocade.com:mgmt:brocade-port-profile', defining_module='brocade-port-profile', yang_type='container', is_config=True)


  def _get_qos_profile(self):
    """
    Getter method for qos_profile, mapped from YANG variable /port_profile/qos_profile (container)

    YANG Description: The QoS profile.
    """
    return self.__qos_profile
      
  def _set_qos_profile(self, v, load=False):
    """
    Setter method for qos_profile, mapped from YANG variable /port_profile/qos_profile (container)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_qos_profile is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_qos_profile() directly.

    YANG Description: The QoS profile.
    """
    if hasattr(v, "_utype"):
      v = v._utype(v)
    try:
      t = YANGDynClass(v,base=qos_profile.qos_profile, is_container='container', presence=True, yang_name="qos-profile", rest_name="qos-profile", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'cli-full-command': None, u'cli-add-mode': None, u'cli-full-no': None, u'info': u'QoS profile', u'callpoint': u'qos-profile-config'}}, namespace='urn:brocade.com:mgmt:brocade-port-profile', defining_module='brocade-port-profile', yang_type='container', is_config=True)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """qos_profile must be of a type compatible with container""",
          'defined-type': "container",
          'generated-type': """YANGDynClass(base=qos_profile.qos_profile, is_container='container', presence=True, yang_name="qos-profile", rest_name="qos-profile", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'cli-full-command': None, u'cli-add-mode': None, u'cli-full-no': None, u'info': u'QoS profile', u'callpoint': u'qos-profile-config'}}, namespace='urn:brocade.com:mgmt:brocade-port-profile', defining_module='brocade-port-profile', yang_type='container', is_config=True)""",
        })

    self.__qos_profile = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_qos_profile(self):
    self.__qos_profile = YANGDynClass(base=qos_profile.qos_profile, is_container='container', presence=True, yang_name="qos-profile", rest_name="qos-profile", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'cli-full-command': None, u'cli-add-mode': None, u'cli-full-no': None, u'info': u'QoS profile', u'callpoint': u'qos-profile-config'}}, namespace='urn:brocade.com:mgmt:brocade-port-profile', defining_module='brocade-port-profile', yang_type='container', is_config=True)


  def _get_security_profile(self):
    """
    Getter method for security_profile, mapped from YANG variable /port_profile/security_profile (container)

    YANG Description: The Security profile.
    """
    return self.__security_profile
      
  def _set_security_profile(self, v, load=False):
    """
    Setter method for security_profile, mapped from YANG variable /port_profile/security_profile (container)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_security_profile is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_security_profile() directly.

    YANG Description: The Security profile.
    """
    if hasattr(v, "_utype"):
      v = v._utype(v)
    try:
      t = YANGDynClass(v,base=security_profile.security_profile, is_container='container', presence=True, yang_name="security-profile", rest_name="security-profile", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'cli-full-command': None, u'cli-add-mode': None, u'cli-full-no': None, u'info': u'Security profile', u'callpoint': u'security-profile-config'}}, namespace='urn:brocade.com:mgmt:brocade-port-profile', defining_module='brocade-port-profile', yang_type='container', is_config=True)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """security_profile must be of a type compatible with container""",
          'defined-type': "container",
          'generated-type': """YANGDynClass(base=security_profile.security_profile, is_container='container', presence=True, yang_name="security-profile", rest_name="security-profile", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'cli-full-command': None, u'cli-add-mode': None, u'cli-full-no': None, u'info': u'Security profile', u'callpoint': u'security-profile-config'}}, namespace='urn:brocade.com:mgmt:brocade-port-profile', defining_module='brocade-port-profile', yang_type='container', is_config=True)""",
        })

    self.__security_profile = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_security_profile(self):
    self.__security_profile = YANGDynClass(base=security_profile.security_profile, is_container='container', presence=True, yang_name="security-profile", rest_name="security-profile", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'cli-full-command': None, u'cli-add-mode': None, u'cli-full-no': None, u'info': u'Security profile', u'callpoint': u'security-profile-config'}}, namespace='urn:brocade.com:mgmt:brocade-port-profile', defining_module='brocade-port-profile', yang_type='container', is_config=True)


  def _get_restrict_flooding_container(self):
    """
    Getter method for restrict_flooding_container, mapped from YANG variable /port_profile/restrict_flooding_container (container)
    """
    return self.__restrict_flooding_container
      
  def _set_restrict_flooding_container(self, v, load=False):
    """
    Setter method for restrict_flooding_container, mapped from YANG variable /port_profile/restrict_flooding_container (container)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_restrict_flooding_container is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_restrict_flooding_container() directly.
    """
    if hasattr(v, "_utype"):
      v = v._utype(v)
    try:
      t = YANGDynClass(v,base=restrict_flooding_container.restrict_flooding_container, is_container='container', presence=False, yang_name="restrict-flooding-container", rest_name="", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'cli-drop-node-name': None, u'display-when': u'../name = "default"'}}, namespace='urn:brocade.com:mgmt:brocade-port-profile', defining_module='brocade-port-profile', yang_type='container', is_config=True)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """restrict_flooding_container must be of a type compatible with container""",
          'defined-type': "container",
          'generated-type': """YANGDynClass(base=restrict_flooding_container.restrict_flooding_container, is_container='container', presence=False, yang_name="restrict-flooding-container", rest_name="", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'cli-drop-node-name': None, u'display-when': u'../name = "default"'}}, namespace='urn:brocade.com:mgmt:brocade-port-profile', defining_module='brocade-port-profile', yang_type='container', is_config=True)""",
        })

    self.__restrict_flooding_container = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_restrict_flooding_container(self):
    self.__restrict_flooding_container = YANGDynClass(base=restrict_flooding_container.restrict_flooding_container, is_container='container', presence=False, yang_name="restrict-flooding-container", rest_name="", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'cli-drop-node-name': None, u'display-when': u'../name = "default"'}}, namespace='urn:brocade.com:mgmt:brocade-port-profile', defining_module='brocade-port-profile', yang_type='container', is_config=True)

  name = __builtin__.property(_get_name, _set_name)
  allow = __builtin__.property(_get_allow, _set_allow)
  vlan_profile = __builtin__.property(_get_vlan_profile, _set_vlan_profile)
  fcoe_profile = __builtin__.property(_get_fcoe_profile, _set_fcoe_profile)
  qos_profile = __builtin__.property(_get_qos_profile, _set_qos_profile)
  security_profile = __builtin__.property(_get_security_profile, _set_security_profile)
  restrict_flooding_container = __builtin__.property(_get_restrict_flooding_container, _set_restrict_flooding_container)


  _pyangbind_elements = {'name': name, 'allow': allow, 'vlan_profile': vlan_profile, 'fcoe_profile': fcoe_profile, 'qos_profile': qos_profile, 'security_profile': security_profile, 'restrict_flooding_container': restrict_flooding_container, }


