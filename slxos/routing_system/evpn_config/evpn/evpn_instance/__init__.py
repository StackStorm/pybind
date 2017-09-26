
from operator import attrgetter
import pyangbind.lib.xpathhelper as xpathhelper
from pyangbind.lib.yangtypes import RestrictedPrecisionDecimalType, RestrictedClassType, TypedListType
from pyangbind.lib.yangtypes import YANGBool, YANGListType, YANGDynClass, ReferenceType
from pyangbind.lib.base import PybindBase
from decimal import Decimal
from bitarray import bitarray
import __builtin__
import route_target
import route_distinguisher
import duplicate_mac_timer
import bridge_domain
import vlan
class evpn_instance(PybindBase):
  """
  This class was auto-generated by the PythonClass plugin for PYANG
  from YANG module brocade-common-def - based on the path /routing-system/evpn-config/evpn/evpn-instance. Each member element of
  the container is represented as a class variable - with a specific
  YANG type.

  YANG Description: EVPN instance config
  """
  __slots__ = ('_pybind_generated_by', '_path_helper', '_yang_name', '_rest_name', '_extmethods', '__instance_name','__route_target','__route_distinguisher','__df_delay_timer','__duplicate_mac_timer','__bridge_domain','__vlan',)

  _yang_name = 'evpn-instance'
  _rest_name = 'evpn-instance'

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
    self.__route_target = YANGDynClass(base=route_target.route_target, is_container='container', presence=False, yang_name="route-target", rest_name="route-target", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'info': u'Configure Target VPN Extended Communities', u'cli-incomplete-no': None, u'cli-incomplete-command': None}}, namespace='urn:brocade.com:mgmt:brocade-bgp', defining_module='brocade-bgp', yang_type='container', is_config=True)
    self.__df_delay_timer = YANGDynClass(base=RestrictedClassType(base_type=RestrictedClassType(base_type=long, restriction_dict={'range': ['0..4294967295']}, int_size=32), restriction_dict={'range': [u'3..10']}), is_leaf=True, yang_name="df-delay-timer", rest_name="df-delay-timer", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'info': u'DF delay timer', u'hidden': u'full'}}, namespace='urn:brocade.com:mgmt:brocade-bgp', defining_module='brocade-bgp', yang_type='delay-timer', is_config=True)
    self.__vlan = YANGDynClass(base=vlan.vlan, is_container='container', presence=False, yang_name="vlan", rest_name="vlan", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'info': u'VLAN configuration', u'cli-incomplete-no': None, u'cli-incomplete-command': None}}, namespace='urn:brocade.com:mgmt:brocade-bgp', defining_module='brocade-bgp', yang_type='container', is_config=True)
    self.__instance_name = YANGDynClass(base=RestrictedClassType(base_type=unicode, restriction_dict={'pattern': u'[a-zA-Z]{1}([-a-zA-Z0-9_]{0,63})'}), is_leaf=True, yang_name="instance-name", rest_name="instance-name", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'key-default': u'default'}}, is_keyval=True, namespace='urn:brocade.com:mgmt:brocade-bgp', defining_module='brocade-bgp', yang_type='evpn-type', is_config=True)
    self.__route_distinguisher = YANGDynClass(base=route_distinguisher.route_distinguisher, is_container='container', presence=False, yang_name="route-distinguisher", rest_name="rd", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'info': u'Configure Route distinguisher', u'cli-compact-syntax': None, u'alt-name': u'rd', u'cli-incomplete-no': None, u'cli-incomplete-command': None}}, namespace='urn:brocade.com:mgmt:brocade-bgp', defining_module='brocade-bgp', yang_type='container', is_config=True)
    self.__bridge_domain = YANGDynClass(base=bridge_domain.bridge_domain, is_container='container', presence=False, yang_name="bridge-domain", rest_name="bridge-domain", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'info': u'Bridge Domain configuration', u'cli-incomplete-no': None, u'cli-incomplete-command': None}}, namespace='urn:brocade.com:mgmt:brocade-bgp', defining_module='brocade-bgp', yang_type='container', is_config=True)
    self.__duplicate_mac_timer = YANGDynClass(base=duplicate_mac_timer.duplicate_mac_timer, is_container='container', presence=False, yang_name="duplicate-mac-timer", rest_name="duplicate-mac-timer", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'cli-compact-syntax': None, u'info': u'Duplicate mac timer', u'cli-sequence-commands': None, u'cli-incomplete-no': None, u'cli-incomplete-command': None}}, namespace='urn:brocade.com:mgmt:brocade-bgp', defining_module='brocade-bgp', yang_type='container', is_config=True)

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
      return [u'routing-system', u'evpn-config', u'evpn', u'evpn-instance']

  def _rest_path(self):
    if hasattr(self, "_parent"):
      if self._rest_name:
        return self._parent._rest_path()+[self._rest_name]
      else:
        return self._parent._rest_path()
    else:
      return [u'evpn', u'evpn-instance']

  def _get_instance_name(self):
    """
    Getter method for instance_name, mapped from YANG variable /routing_system/evpn_config/evpn/evpn_instance/instance_name (evpn-type)
    """
    return self.__instance_name
      
  def _set_instance_name(self, v, load=False):
    """
    Setter method for instance_name, mapped from YANG variable /routing_system/evpn_config/evpn/evpn_instance/instance_name (evpn-type)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_instance_name is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_instance_name() directly.
    """
    parent = getattr(self, "_parent", None)
    if parent is not None and load is False:
      raise AttributeError("Cannot set keys directly when" +
                             " within an instantiated list")

    if hasattr(v, "_utype"):
      v = v._utype(v)
    try:
      t = YANGDynClass(v,base=RestrictedClassType(base_type=unicode, restriction_dict={'pattern': u'[a-zA-Z]{1}([-a-zA-Z0-9_]{0,63})'}), is_leaf=True, yang_name="instance-name", rest_name="instance-name", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'key-default': u'default'}}, is_keyval=True, namespace='urn:brocade.com:mgmt:brocade-bgp', defining_module='brocade-bgp', yang_type='evpn-type', is_config=True)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """instance_name must be of a type compatible with evpn-type""",
          'defined-type': "brocade-bgp:evpn-type",
          'generated-type': """YANGDynClass(base=RestrictedClassType(base_type=unicode, restriction_dict={'pattern': u'[a-zA-Z]{1}([-a-zA-Z0-9_]{0,63})'}), is_leaf=True, yang_name="instance-name", rest_name="instance-name", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'key-default': u'default'}}, is_keyval=True, namespace='urn:brocade.com:mgmt:brocade-bgp', defining_module='brocade-bgp', yang_type='evpn-type', is_config=True)""",
        })

    self.__instance_name = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_instance_name(self):
    self.__instance_name = YANGDynClass(base=RestrictedClassType(base_type=unicode, restriction_dict={'pattern': u'[a-zA-Z]{1}([-a-zA-Z0-9_]{0,63})'}), is_leaf=True, yang_name="instance-name", rest_name="instance-name", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'key-default': u'default'}}, is_keyval=True, namespace='urn:brocade.com:mgmt:brocade-bgp', defining_module='brocade-bgp', yang_type='evpn-type', is_config=True)


  def _get_route_target(self):
    """
    Getter method for route_target, mapped from YANG variable /routing_system/evpn_config/evpn/evpn_instance/route_target (container)
    """
    return self.__route_target
      
  def _set_route_target(self, v, load=False):
    """
    Setter method for route_target, mapped from YANG variable /routing_system/evpn_config/evpn/evpn_instance/route_target (container)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_route_target is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_route_target() directly.
    """
    if hasattr(v, "_utype"):
      v = v._utype(v)
    try:
      t = YANGDynClass(v,base=route_target.route_target, is_container='container', presence=False, yang_name="route-target", rest_name="route-target", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'info': u'Configure Target VPN Extended Communities', u'cli-incomplete-no': None, u'cli-incomplete-command': None}}, namespace='urn:brocade.com:mgmt:brocade-bgp', defining_module='brocade-bgp', yang_type='container', is_config=True)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """route_target must be of a type compatible with container""",
          'defined-type': "container",
          'generated-type': """YANGDynClass(base=route_target.route_target, is_container='container', presence=False, yang_name="route-target", rest_name="route-target", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'info': u'Configure Target VPN Extended Communities', u'cli-incomplete-no': None, u'cli-incomplete-command': None}}, namespace='urn:brocade.com:mgmt:brocade-bgp', defining_module='brocade-bgp', yang_type='container', is_config=True)""",
        })

    self.__route_target = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_route_target(self):
    self.__route_target = YANGDynClass(base=route_target.route_target, is_container='container', presence=False, yang_name="route-target", rest_name="route-target", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'info': u'Configure Target VPN Extended Communities', u'cli-incomplete-no': None, u'cli-incomplete-command': None}}, namespace='urn:brocade.com:mgmt:brocade-bgp', defining_module='brocade-bgp', yang_type='container', is_config=True)


  def _get_route_distinguisher(self):
    """
    Getter method for route_distinguisher, mapped from YANG variable /routing_system/evpn_config/evpn/evpn_instance/route_distinguisher (container)
    """
    return self.__route_distinguisher
      
  def _set_route_distinguisher(self, v, load=False):
    """
    Setter method for route_distinguisher, mapped from YANG variable /routing_system/evpn_config/evpn/evpn_instance/route_distinguisher (container)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_route_distinguisher is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_route_distinguisher() directly.
    """
    if hasattr(v, "_utype"):
      v = v._utype(v)
    try:
      t = YANGDynClass(v,base=route_distinguisher.route_distinguisher, is_container='container', presence=False, yang_name="route-distinguisher", rest_name="rd", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'info': u'Configure Route distinguisher', u'cli-compact-syntax': None, u'alt-name': u'rd', u'cli-incomplete-no': None, u'cli-incomplete-command': None}}, namespace='urn:brocade.com:mgmt:brocade-bgp', defining_module='brocade-bgp', yang_type='container', is_config=True)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """route_distinguisher must be of a type compatible with container""",
          'defined-type': "container",
          'generated-type': """YANGDynClass(base=route_distinguisher.route_distinguisher, is_container='container', presence=False, yang_name="route-distinguisher", rest_name="rd", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'info': u'Configure Route distinguisher', u'cli-compact-syntax': None, u'alt-name': u'rd', u'cli-incomplete-no': None, u'cli-incomplete-command': None}}, namespace='urn:brocade.com:mgmt:brocade-bgp', defining_module='brocade-bgp', yang_type='container', is_config=True)""",
        })

    self.__route_distinguisher = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_route_distinguisher(self):
    self.__route_distinguisher = YANGDynClass(base=route_distinguisher.route_distinguisher, is_container='container', presence=False, yang_name="route-distinguisher", rest_name="rd", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'info': u'Configure Route distinguisher', u'cli-compact-syntax': None, u'alt-name': u'rd', u'cli-incomplete-no': None, u'cli-incomplete-command': None}}, namespace='urn:brocade.com:mgmt:brocade-bgp', defining_module='brocade-bgp', yang_type='container', is_config=True)


  def _get_df_delay_timer(self):
    """
    Getter method for df_delay_timer, mapped from YANG variable /routing_system/evpn_config/evpn/evpn_instance/df_delay_timer (delay-timer)

    YANG Description: DF delay timer
    """
    return self.__df_delay_timer
      
  def _set_df_delay_timer(self, v, load=False):
    """
    Setter method for df_delay_timer, mapped from YANG variable /routing_system/evpn_config/evpn/evpn_instance/df_delay_timer (delay-timer)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_df_delay_timer is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_df_delay_timer() directly.

    YANG Description: DF delay timer
    """
    if hasattr(v, "_utype"):
      v = v._utype(v)
    try:
      t = YANGDynClass(v,base=RestrictedClassType(base_type=RestrictedClassType(base_type=long, restriction_dict={'range': ['0..4294967295']}, int_size=32), restriction_dict={'range': [u'3..10']}), is_leaf=True, yang_name="df-delay-timer", rest_name="df-delay-timer", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'info': u'DF delay timer', u'hidden': u'full'}}, namespace='urn:brocade.com:mgmt:brocade-bgp', defining_module='brocade-bgp', yang_type='delay-timer', is_config=True)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """df_delay_timer must be of a type compatible with delay-timer""",
          'defined-type': "brocade-bgp:delay-timer",
          'generated-type': """YANGDynClass(base=RestrictedClassType(base_type=RestrictedClassType(base_type=long, restriction_dict={'range': ['0..4294967295']}, int_size=32), restriction_dict={'range': [u'3..10']}), is_leaf=True, yang_name="df-delay-timer", rest_name="df-delay-timer", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'info': u'DF delay timer', u'hidden': u'full'}}, namespace='urn:brocade.com:mgmt:brocade-bgp', defining_module='brocade-bgp', yang_type='delay-timer', is_config=True)""",
        })

    self.__df_delay_timer = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_df_delay_timer(self):
    self.__df_delay_timer = YANGDynClass(base=RestrictedClassType(base_type=RestrictedClassType(base_type=long, restriction_dict={'range': ['0..4294967295']}, int_size=32), restriction_dict={'range': [u'3..10']}), is_leaf=True, yang_name="df-delay-timer", rest_name="df-delay-timer", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'info': u'DF delay timer', u'hidden': u'full'}}, namespace='urn:brocade.com:mgmt:brocade-bgp', defining_module='brocade-bgp', yang_type='delay-timer', is_config=True)


  def _get_duplicate_mac_timer(self):
    """
    Getter method for duplicate_mac_timer, mapped from YANG variable /routing_system/evpn_config/evpn/evpn_instance/duplicate_mac_timer (container)

    YANG Description: Duplicate mac timer
    """
    return self.__duplicate_mac_timer
      
  def _set_duplicate_mac_timer(self, v, load=False):
    """
    Setter method for duplicate_mac_timer, mapped from YANG variable /routing_system/evpn_config/evpn/evpn_instance/duplicate_mac_timer (container)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_duplicate_mac_timer is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_duplicate_mac_timer() directly.

    YANG Description: Duplicate mac timer
    """
    if hasattr(v, "_utype"):
      v = v._utype(v)
    try:
      t = YANGDynClass(v,base=duplicate_mac_timer.duplicate_mac_timer, is_container='container', presence=False, yang_name="duplicate-mac-timer", rest_name="duplicate-mac-timer", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'cli-compact-syntax': None, u'info': u'Duplicate mac timer', u'cli-sequence-commands': None, u'cli-incomplete-no': None, u'cli-incomplete-command': None}}, namespace='urn:brocade.com:mgmt:brocade-bgp', defining_module='brocade-bgp', yang_type='container', is_config=True)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """duplicate_mac_timer must be of a type compatible with container""",
          'defined-type': "container",
          'generated-type': """YANGDynClass(base=duplicate_mac_timer.duplicate_mac_timer, is_container='container', presence=False, yang_name="duplicate-mac-timer", rest_name="duplicate-mac-timer", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'cli-compact-syntax': None, u'info': u'Duplicate mac timer', u'cli-sequence-commands': None, u'cli-incomplete-no': None, u'cli-incomplete-command': None}}, namespace='urn:brocade.com:mgmt:brocade-bgp', defining_module='brocade-bgp', yang_type='container', is_config=True)""",
        })

    self.__duplicate_mac_timer = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_duplicate_mac_timer(self):
    self.__duplicate_mac_timer = YANGDynClass(base=duplicate_mac_timer.duplicate_mac_timer, is_container='container', presence=False, yang_name="duplicate-mac-timer", rest_name="duplicate-mac-timer", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'cli-compact-syntax': None, u'info': u'Duplicate mac timer', u'cli-sequence-commands': None, u'cli-incomplete-no': None, u'cli-incomplete-command': None}}, namespace='urn:brocade.com:mgmt:brocade-bgp', defining_module='brocade-bgp', yang_type='container', is_config=True)


  def _get_bridge_domain(self):
    """
    Getter method for bridge_domain, mapped from YANG variable /routing_system/evpn_config/evpn/evpn_instance/bridge_domain (container)
    """
    return self.__bridge_domain
      
  def _set_bridge_domain(self, v, load=False):
    """
    Setter method for bridge_domain, mapped from YANG variable /routing_system/evpn_config/evpn/evpn_instance/bridge_domain (container)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_bridge_domain is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_bridge_domain() directly.
    """
    if hasattr(v, "_utype"):
      v = v._utype(v)
    try:
      t = YANGDynClass(v,base=bridge_domain.bridge_domain, is_container='container', presence=False, yang_name="bridge-domain", rest_name="bridge-domain", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'info': u'Bridge Domain configuration', u'cli-incomplete-no': None, u'cli-incomplete-command': None}}, namespace='urn:brocade.com:mgmt:brocade-bgp', defining_module='brocade-bgp', yang_type='container', is_config=True)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """bridge_domain must be of a type compatible with container""",
          'defined-type': "container",
          'generated-type': """YANGDynClass(base=bridge_domain.bridge_domain, is_container='container', presence=False, yang_name="bridge-domain", rest_name="bridge-domain", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'info': u'Bridge Domain configuration', u'cli-incomplete-no': None, u'cli-incomplete-command': None}}, namespace='urn:brocade.com:mgmt:brocade-bgp', defining_module='brocade-bgp', yang_type='container', is_config=True)""",
        })

    self.__bridge_domain = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_bridge_domain(self):
    self.__bridge_domain = YANGDynClass(base=bridge_domain.bridge_domain, is_container='container', presence=False, yang_name="bridge-domain", rest_name="bridge-domain", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'info': u'Bridge Domain configuration', u'cli-incomplete-no': None, u'cli-incomplete-command': None}}, namespace='urn:brocade.com:mgmt:brocade-bgp', defining_module='brocade-bgp', yang_type='container', is_config=True)


  def _get_vlan(self):
    """
    Getter method for vlan, mapped from YANG variable /routing_system/evpn_config/evpn/evpn_instance/vlan (container)
    """
    return self.__vlan
      
  def _set_vlan(self, v, load=False):
    """
    Setter method for vlan, mapped from YANG variable /routing_system/evpn_config/evpn/evpn_instance/vlan (container)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_vlan is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_vlan() directly.
    """
    if hasattr(v, "_utype"):
      v = v._utype(v)
    try:
      t = YANGDynClass(v,base=vlan.vlan, is_container='container', presence=False, yang_name="vlan", rest_name="vlan", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'info': u'VLAN configuration', u'cli-incomplete-no': None, u'cli-incomplete-command': None}}, namespace='urn:brocade.com:mgmt:brocade-bgp', defining_module='brocade-bgp', yang_type='container', is_config=True)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """vlan must be of a type compatible with container""",
          'defined-type': "container",
          'generated-type': """YANGDynClass(base=vlan.vlan, is_container='container', presence=False, yang_name="vlan", rest_name="vlan", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'info': u'VLAN configuration', u'cli-incomplete-no': None, u'cli-incomplete-command': None}}, namespace='urn:brocade.com:mgmt:brocade-bgp', defining_module='brocade-bgp', yang_type='container', is_config=True)""",
        })

    self.__vlan = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_vlan(self):
    self.__vlan = YANGDynClass(base=vlan.vlan, is_container='container', presence=False, yang_name="vlan", rest_name="vlan", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'info': u'VLAN configuration', u'cli-incomplete-no': None, u'cli-incomplete-command': None}}, namespace='urn:brocade.com:mgmt:brocade-bgp', defining_module='brocade-bgp', yang_type='container', is_config=True)

  instance_name = __builtin__.property(_get_instance_name, _set_instance_name)
  route_target = __builtin__.property(_get_route_target, _set_route_target)
  route_distinguisher = __builtin__.property(_get_route_distinguisher, _set_route_distinguisher)
  df_delay_timer = __builtin__.property(_get_df_delay_timer, _set_df_delay_timer)
  duplicate_mac_timer = __builtin__.property(_get_duplicate_mac_timer, _set_duplicate_mac_timer)
  bridge_domain = __builtin__.property(_get_bridge_domain, _set_bridge_domain)
  vlan = __builtin__.property(_get_vlan, _set_vlan)


  _pyangbind_elements = {'instance_name': instance_name, 'route_target': route_target, 'route_distinguisher': route_distinguisher, 'df_delay_timer': df_delay_timer, 'duplicate_mac_timer': duplicate_mac_timer, 'bridge_domain': bridge_domain, 'vlan': vlan, }


