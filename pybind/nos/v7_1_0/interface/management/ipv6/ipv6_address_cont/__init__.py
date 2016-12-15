
from operator import attrgetter
import pyangbind.lib.xpathhelper as xpathhelper
from pyangbind.lib.yangtypes import RestrictedPrecisionDecimalType, RestrictedClassType, TypedListType
from pyangbind.lib.yangtypes import YANGBool, YANGListType, YANGDynClass, ReferenceType
from pyangbind.lib.base import PybindBase
from decimal import Decimal
from bitarray import bitarray
import __builtin__
import ipv6_global_cont
class ipv6_address_cont(PybindBase):
  """
  This class was auto-generated by the PythonClass plugin for PYANG
  from YANG module brocade-interface - based on the path /interface/management/ipv6/ipv6-address-cont. Each member element of
  the container is represented as a class variable - with a specific
  YANG type.

  YANG Description: The IPv6 address configuration for this 
management interface.
  """
  __slots__ = ('_pybind_generated_by', '_path_helper', '_yang_name', '_rest_name', '_extmethods', '__ipv6_global_cont','__autoconfig','__dhcpv6',)

  _yang_name = 'ipv6-address-cont'
  _rest_name = 'address'

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
    self.__dhcpv6 = YANGDynClass(base=YANGBool, is_leaf=True, yang_name="dhcpv6", rest_name="dhcp", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'cli-full-command': None, u'info': u'ipv6 DHCP enabling', u'alt-name': u'dhcp', u'cli-show-no': None}}, namespace='urn:brocade.com:mgmt:brocade-interface', defining_module='brocade-interface', yang_type='empty', is_config=True)
    self.__autoconfig = YANGDynClass(base=YANGBool, is_leaf=True, yang_name="autoconfig", rest_name="autoconfig", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'cli-full-command': None, u'info': u'Auto-configuration enabling.', u'cli-show-no': None}}, namespace='urn:brocade.com:mgmt:brocade-interface', defining_module='brocade-interface', yang_type='empty', is_config=True)
    self.__ipv6_global_cont = YANGDynClass(base=ipv6_global_cont.ipv6_global_cont, is_container='container', yang_name="ipv6-global-cont", rest_name="", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'cli-compact-syntax': None, u'cli-drop-node-name': None, u'cli-sequence-commands': None}}, namespace='urn:brocade.com:mgmt:brocade-interface', defining_module='brocade-interface', yang_type='container', is_config=True)

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
      return [u'interface', u'management', u'ipv6', u'ipv6-address-cont']

  def _rest_path(self):
    if hasattr(self, "_parent"):
      if self._rest_name:
        return self._parent._rest_path()+[self._rest_name]
      else:
        return self._parent._rest_path()
    else:
      return [u'interface', u'Management', u'ipv6', u'address']

  def _get_ipv6_global_cont(self):
    """
    Getter method for ipv6_global_cont, mapped from YANG variable /interface/management/ipv6/ipv6_address_cont/ipv6_global_cont (container)
    """
    return self.__ipv6_global_cont
      
  def _set_ipv6_global_cont(self, v, load=False):
    """
    Setter method for ipv6_global_cont, mapped from YANG variable /interface/management/ipv6/ipv6_address_cont/ipv6_global_cont (container)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_ipv6_global_cont is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_ipv6_global_cont() directly.
    """
    if hasattr(v, "_utype"):
      v = v._utype(v)
    try:
      t = YANGDynClass(v,base=ipv6_global_cont.ipv6_global_cont, is_container='container', yang_name="ipv6-global-cont", rest_name="", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'cli-compact-syntax': None, u'cli-drop-node-name': None, u'cli-sequence-commands': None}}, namespace='urn:brocade.com:mgmt:brocade-interface', defining_module='brocade-interface', yang_type='container', is_config=True)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """ipv6_global_cont must be of a type compatible with container""",
          'defined-type': "container",
          'generated-type': """YANGDynClass(base=ipv6_global_cont.ipv6_global_cont, is_container='container', yang_name="ipv6-global-cont", rest_name="", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'cli-compact-syntax': None, u'cli-drop-node-name': None, u'cli-sequence-commands': None}}, namespace='urn:brocade.com:mgmt:brocade-interface', defining_module='brocade-interface', yang_type='container', is_config=True)""",
        })

    self.__ipv6_global_cont = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_ipv6_global_cont(self):
    self.__ipv6_global_cont = YANGDynClass(base=ipv6_global_cont.ipv6_global_cont, is_container='container', yang_name="ipv6-global-cont", rest_name="", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'cli-compact-syntax': None, u'cli-drop-node-name': None, u'cli-sequence-commands': None}}, namespace='urn:brocade.com:mgmt:brocade-interface', defining_module='brocade-interface', yang_type='container', is_config=True)


  def _get_autoconfig(self):
    """
    Getter method for autoconfig, mapped from YANG variable /interface/management/ipv6/ipv6_address_cont/autoconfig (empty)

    YANG Description: This specifies if this auto-configuration 
for IP address allocation is enabled or not.
The presence of this leaf indicates that 
the auto-configuration is enabled.
    """
    return self.__autoconfig
      
  def _set_autoconfig(self, v, load=False):
    """
    Setter method for autoconfig, mapped from YANG variable /interface/management/ipv6/ipv6_address_cont/autoconfig (empty)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_autoconfig is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_autoconfig() directly.

    YANG Description: This specifies if this auto-configuration 
for IP address allocation is enabled or not.
The presence of this leaf indicates that 
the auto-configuration is enabled.
    """
    if hasattr(v, "_utype"):
      v = v._utype(v)
    try:
      t = YANGDynClass(v,base=YANGBool, is_leaf=True, yang_name="autoconfig", rest_name="autoconfig", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'cli-full-command': None, u'info': u'Auto-configuration enabling.', u'cli-show-no': None}}, namespace='urn:brocade.com:mgmt:brocade-interface', defining_module='brocade-interface', yang_type='empty', is_config=True)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """autoconfig must be of a type compatible with empty""",
          'defined-type': "empty",
          'generated-type': """YANGDynClass(base=YANGBool, is_leaf=True, yang_name="autoconfig", rest_name="autoconfig", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'cli-full-command': None, u'info': u'Auto-configuration enabling.', u'cli-show-no': None}}, namespace='urn:brocade.com:mgmt:brocade-interface', defining_module='brocade-interface', yang_type='empty', is_config=True)""",
        })

    self.__autoconfig = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_autoconfig(self):
    self.__autoconfig = YANGDynClass(base=YANGBool, is_leaf=True, yang_name="autoconfig", rest_name="autoconfig", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'cli-full-command': None, u'info': u'Auto-configuration enabling.', u'cli-show-no': None}}, namespace='urn:brocade.com:mgmt:brocade-interface', defining_module='brocade-interface', yang_type='empty', is_config=True)


  def _get_dhcpv6(self):
    """
    Getter method for dhcpv6, mapped from YANG variable /interface/management/ipv6/ipv6_address_cont/dhcpv6 (empty)

    YANG Description: This specifies if this ipv6 dhcp is enabled 
or not. The presence of this leaf indicates that 
the ipv6 dhcp is enabled.
    """
    return self.__dhcpv6
      
  def _set_dhcpv6(self, v, load=False):
    """
    Setter method for dhcpv6, mapped from YANG variable /interface/management/ipv6/ipv6_address_cont/dhcpv6 (empty)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_dhcpv6 is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_dhcpv6() directly.

    YANG Description: This specifies if this ipv6 dhcp is enabled 
or not. The presence of this leaf indicates that 
the ipv6 dhcp is enabled.
    """
    if hasattr(v, "_utype"):
      v = v._utype(v)
    try:
      t = YANGDynClass(v,base=YANGBool, is_leaf=True, yang_name="dhcpv6", rest_name="dhcp", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'cli-full-command': None, u'info': u'ipv6 DHCP enabling', u'alt-name': u'dhcp', u'cli-show-no': None}}, namespace='urn:brocade.com:mgmt:brocade-interface', defining_module='brocade-interface', yang_type='empty', is_config=True)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """dhcpv6 must be of a type compatible with empty""",
          'defined-type': "empty",
          'generated-type': """YANGDynClass(base=YANGBool, is_leaf=True, yang_name="dhcpv6", rest_name="dhcp", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'cli-full-command': None, u'info': u'ipv6 DHCP enabling', u'alt-name': u'dhcp', u'cli-show-no': None}}, namespace='urn:brocade.com:mgmt:brocade-interface', defining_module='brocade-interface', yang_type='empty', is_config=True)""",
        })

    self.__dhcpv6 = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_dhcpv6(self):
    self.__dhcpv6 = YANGDynClass(base=YANGBool, is_leaf=True, yang_name="dhcpv6", rest_name="dhcp", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'cli-full-command': None, u'info': u'ipv6 DHCP enabling', u'alt-name': u'dhcp', u'cli-show-no': None}}, namespace='urn:brocade.com:mgmt:brocade-interface', defining_module='brocade-interface', yang_type='empty', is_config=True)

  ipv6_global_cont = __builtin__.property(_get_ipv6_global_cont, _set_ipv6_global_cont)
  autoconfig = __builtin__.property(_get_autoconfig, _set_autoconfig)
  dhcpv6 = __builtin__.property(_get_dhcpv6, _set_dhcpv6)


  _pyangbind_elements = {'ipv6_global_cont': ipv6_global_cont, 'autoconfig': autoconfig, 'dhcpv6': dhcpv6, }


