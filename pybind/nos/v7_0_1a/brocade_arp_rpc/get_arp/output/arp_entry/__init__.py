
from operator import attrgetter
import pyangbind.lib.xpathhelper as xpathhelper
from pyangbind.lib.yangtypes import RestrictedPrecisionDecimalType, RestrictedClassType, TypedListType
from pyangbind.lib.yangtypes import YANGBool, YANGListType, YANGDynClass, ReferenceType
from pyangbind.lib.base import PybindBase
from decimal import Decimal
from bitarray import bitarray
import __builtin__
class arp_entry(PybindBase):
  """
  This class was auto-generated by the PythonClass plugin for PYANG
  from YANG module brocade-arp - based on the path /brocade_arp_rpc/get-arp/output/arp-entry. Each member element of
  the container is represented as a class variable - with a specific
  YANG type.
  """
  __slots__ = ('_pybind_generated_by', '_path_helper', '_yang_name', '_rest_name', '_extmethods', '__ip_address','__mac_address','__interface_type','__interface_name','__is_resolved','__age','__entry_type',)

  _yang_name = 'arp-entry'
  _rest_name = 'arp-entry'

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
    self.__entry_type = YANGDynClass(base=RestrictedClassType(base_type=unicode,                                     restriction_type="dict_key",                                     restriction_arg={u'dynamic': {'value': 2}, u'static': {'value': 1}, u'unknown': {'value': 3}},), is_leaf=True, yang_name="entry-type", rest_name="entry-type", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=False, namespace='urn:brocade.com:mgmt:brocade-arp', defining_module='brocade-arp', yang_type='enumeration', is_config=True)
    self.__interface_type = YANGDynClass(base=RestrictedClassType(base_type=unicode,                                     restriction_type="dict_key",                                     restriction_arg={u'port-channel': {'value': 5}, u'loopback': {'value': 7}, u'fortygigabitethernet': {'value': 4}, u'unknown': {'value': 1}, u'gigabitethernet': {'value': 2}, u'tengigabitethernet': {'value': 3}, u'tunnel': {'value': 10}, u'hundredgigabitethernet': {'value': 9}, u'fibrechannel': {'value': 8}, u'l2vlan': {'value': 6}},), is_leaf=True, yang_name="interface-type", rest_name="interface-type", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=False, extensions={u'tailf-common': {u'info': u"The type of the interface. An 'unknown' type \nrepresents error scenario and should not be used."}}, namespace='urn:brocade.com:mgmt:brocade-arp', defining_module='brocade-arp', yang_type='enumeration', is_config=True)
    self.__is_resolved = YANGDynClass(base=YANGBool, is_leaf=True, yang_name="is-resolved", rest_name="is-resolved", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=False, namespace='urn:brocade.com:mgmt:brocade-arp', defining_module='brocade-arp', yang_type='boolean', is_config=True)
    self.__mac_address = YANGDynClass(base=unicode, is_leaf=True, yang_name="mac-address", rest_name="mac-address", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=False, namespace='urn:brocade.com:mgmt:brocade-arp', defining_module='brocade-arp', yang_type='mac-access-list:mac-address-type', is_config=True)
    self.__interface_name = YANGDynClass(base=[RestrictedClassType(base_type=unicode, restriction_dict={'pattern': u'((([1-9]|[1-9][0-9]|1[0-9][0-9]|2[0-3][0-9])/)?(([0-9]|[1][0-6]))/([1-9]|[1-9][0-9]|[1-9][0-9][0-9])(:[1-4])?)', 'length': [u'3..16']}),RestrictedClassType(base_type=RestrictedClassType(base_type=long, restriction_dict={'range': ['0..4294967295']}, int_size=32), restriction_dict={'range': [u'1..6144']}),RestrictedClassType(base_type=RestrictedClassType(base_type=long, restriction_dict={'range': ['0..4294967295']}, int_size=32), restriction_dict={'range': [u'1..8191']}),], is_leaf=True, yang_name="interface-name", rest_name="interface-name", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=False, extensions={u'tailf-common': {u'info': u'The Interface value.'}}, namespace='urn:brocade.com:mgmt:brocade-arp', defining_module='brocade-arp', yang_type='union', is_config=True)
    self.__ip_address = YANGDynClass(base=RestrictedClassType(base_type=unicode, restriction_dict={'pattern': u'(([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])\\.){3}([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])(%[\\p{N}\\p{L}]+)?'}), is_leaf=True, yang_name="ip-address", rest_name="ip-address", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=False, is_keyval=True, namespace='urn:brocade.com:mgmt:brocade-arp', defining_module='brocade-arp', yang_type='inet:ipv4-address', is_config=True)
    self.__age = YANGDynClass(base=unicode, is_leaf=True, yang_name="age", rest_name="age", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=False, namespace='urn:brocade.com:mgmt:brocade-arp', defining_module='brocade-arp', yang_type='string', is_config=True)

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
      return [u'brocade_arp_rpc', u'get-arp', u'output', u'arp-entry']

  def _rest_path(self):
    if hasattr(self, "_parent"):
      if self._rest_name:
        return self._parent._rest_path()+[self._rest_name]
      else:
        return self._parent._rest_path()
    else:
      return [u'get-arp', u'output', u'arp-entry']

  def _get_ip_address(self):
    """
    Getter method for ip_address, mapped from YANG variable /brocade_arp_rpc/get_arp/output/arp_entry/ip_address (inet:ipv4-address)

    YANG Description: IP address of the ARP entry
    """
    return self.__ip_address
      
  def _set_ip_address(self, v, load=False):
    """
    Setter method for ip_address, mapped from YANG variable /brocade_arp_rpc/get_arp/output/arp_entry/ip_address (inet:ipv4-address)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_ip_address is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_ip_address() directly.

    YANG Description: IP address of the ARP entry
    """
    parent = getattr(self, "_parent", None)
    if parent is not None and load is False:
      raise AttributeError("Cannot set keys directly when" +
                             " within an instantiated list")

    if hasattr(v, "_utype"):
      v = v._utype(v)
    try:
      t = YANGDynClass(v,base=RestrictedClassType(base_type=unicode, restriction_dict={'pattern': u'(([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])\\.){3}([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])(%[\\p{N}\\p{L}]+)?'}), is_leaf=True, yang_name="ip-address", rest_name="ip-address", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=False, is_keyval=True, namespace='urn:brocade.com:mgmt:brocade-arp', defining_module='brocade-arp', yang_type='inet:ipv4-address', is_config=True)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """ip_address must be of a type compatible with inet:ipv4-address""",
          'defined-type': "inet:ipv4-address",
          'generated-type': """YANGDynClass(base=RestrictedClassType(base_type=unicode, restriction_dict={'pattern': u'(([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])\\.){3}([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])(%[\\p{N}\\p{L}]+)?'}), is_leaf=True, yang_name="ip-address", rest_name="ip-address", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=False, is_keyval=True, namespace='urn:brocade.com:mgmt:brocade-arp', defining_module='brocade-arp', yang_type='inet:ipv4-address', is_config=True)""",
        })

    self.__ip_address = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_ip_address(self):
    self.__ip_address = YANGDynClass(base=RestrictedClassType(base_type=unicode, restriction_dict={'pattern': u'(([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])\\.){3}([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])(%[\\p{N}\\p{L}]+)?'}), is_leaf=True, yang_name="ip-address", rest_name="ip-address", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=False, is_keyval=True, namespace='urn:brocade.com:mgmt:brocade-arp', defining_module='brocade-arp', yang_type='inet:ipv4-address', is_config=True)


  def _get_mac_address(self):
    """
    Getter method for mac_address, mapped from YANG variable /brocade_arp_rpc/get_arp/output/arp_entry/mac_address (mac-access-list:mac-address-type)

    YANG Description: Mac address of the ARP entry
    """
    return self.__mac_address
      
  def _set_mac_address(self, v, load=False):
    """
    Setter method for mac_address, mapped from YANG variable /brocade_arp_rpc/get_arp/output/arp_entry/mac_address (mac-access-list:mac-address-type)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_mac_address is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_mac_address() directly.

    YANG Description: Mac address of the ARP entry
    """
    if hasattr(v, "_utype"):
      v = v._utype(v)
    try:
      t = YANGDynClass(v,base=unicode, is_leaf=True, yang_name="mac-address", rest_name="mac-address", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=False, namespace='urn:brocade.com:mgmt:brocade-arp', defining_module='brocade-arp', yang_type='mac-access-list:mac-address-type', is_config=True)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """mac_address must be of a type compatible with mac-access-list:mac-address-type""",
          'defined-type': "mac-access-list:mac-address-type",
          'generated-type': """YANGDynClass(base=unicode, is_leaf=True, yang_name="mac-address", rest_name="mac-address", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=False, namespace='urn:brocade.com:mgmt:brocade-arp', defining_module='brocade-arp', yang_type='mac-access-list:mac-address-type', is_config=True)""",
        })

    self.__mac_address = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_mac_address(self):
    self.__mac_address = YANGDynClass(base=unicode, is_leaf=True, yang_name="mac-address", rest_name="mac-address", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=False, namespace='urn:brocade.com:mgmt:brocade-arp', defining_module='brocade-arp', yang_type='mac-access-list:mac-address-type', is_config=True)


  def _get_interface_type(self):
    """
    Getter method for interface_type, mapped from YANG variable /brocade_arp_rpc/get_arp/output/arp_entry/interface_type (enumeration)

    YANG Description: The type of the interface. An 'unknown' type 
represents error scenario and should not be used.
    """
    return self.__interface_type
      
  def _set_interface_type(self, v, load=False):
    """
    Setter method for interface_type, mapped from YANG variable /brocade_arp_rpc/get_arp/output/arp_entry/interface_type (enumeration)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_interface_type is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_interface_type() directly.

    YANG Description: The type of the interface. An 'unknown' type 
represents error scenario and should not be used.
    """
    if hasattr(v, "_utype"):
      v = v._utype(v)
    try:
      t = YANGDynClass(v,base=RestrictedClassType(base_type=unicode,                                     restriction_type="dict_key",                                     restriction_arg={u'port-channel': {'value': 5}, u'loopback': {'value': 7}, u'fortygigabitethernet': {'value': 4}, u'unknown': {'value': 1}, u'gigabitethernet': {'value': 2}, u'tengigabitethernet': {'value': 3}, u'tunnel': {'value': 10}, u'hundredgigabitethernet': {'value': 9}, u'fibrechannel': {'value': 8}, u'l2vlan': {'value': 6}},), is_leaf=True, yang_name="interface-type", rest_name="interface-type", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=False, extensions={u'tailf-common': {u'info': u"The type of the interface. An 'unknown' type \nrepresents error scenario and should not be used."}}, namespace='urn:brocade.com:mgmt:brocade-arp', defining_module='brocade-arp', yang_type='enumeration', is_config=True)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """interface_type must be of a type compatible with enumeration""",
          'defined-type': "brocade-arp:enumeration",
          'generated-type': """YANGDynClass(base=RestrictedClassType(base_type=unicode,                                     restriction_type="dict_key",                                     restriction_arg={u'port-channel': {'value': 5}, u'loopback': {'value': 7}, u'fortygigabitethernet': {'value': 4}, u'unknown': {'value': 1}, u'gigabitethernet': {'value': 2}, u'tengigabitethernet': {'value': 3}, u'tunnel': {'value': 10}, u'hundredgigabitethernet': {'value': 9}, u'fibrechannel': {'value': 8}, u'l2vlan': {'value': 6}},), is_leaf=True, yang_name="interface-type", rest_name="interface-type", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=False, extensions={u'tailf-common': {u'info': u"The type of the interface. An 'unknown' type \nrepresents error scenario and should not be used."}}, namespace='urn:brocade.com:mgmt:brocade-arp', defining_module='brocade-arp', yang_type='enumeration', is_config=True)""",
        })

    self.__interface_type = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_interface_type(self):
    self.__interface_type = YANGDynClass(base=RestrictedClassType(base_type=unicode,                                     restriction_type="dict_key",                                     restriction_arg={u'port-channel': {'value': 5}, u'loopback': {'value': 7}, u'fortygigabitethernet': {'value': 4}, u'unknown': {'value': 1}, u'gigabitethernet': {'value': 2}, u'tengigabitethernet': {'value': 3}, u'tunnel': {'value': 10}, u'hundredgigabitethernet': {'value': 9}, u'fibrechannel': {'value': 8}, u'l2vlan': {'value': 6}},), is_leaf=True, yang_name="interface-type", rest_name="interface-type", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=False, extensions={u'tailf-common': {u'info': u"The type of the interface. An 'unknown' type \nrepresents error scenario and should not be used."}}, namespace='urn:brocade.com:mgmt:brocade-arp', defining_module='brocade-arp', yang_type='enumeration', is_config=True)


  def _get_interface_name(self):
    """
    Getter method for interface_name, mapped from YANG variable /brocade_arp_rpc/get_arp/output/arp_entry/interface_name (union)

    YANG Description: The Interface value. The interface value is always 
interpreted within the context of the value of 
'interface-type' leaf:

interface-type         interface-name
-----------------      --------------------
gigabitethernet        [rbridge-id]/slot/port
tengigabitethernet     [rbridge-id]/slot/port
fortygigabitethernet   [rbridge-id]/slot/port
hundredgigabitethernet [rbridge-id]/slot/port
port-channel           Port channel ID
l2vlan                 Vlan ID
unknown                Zero-length string.

The value of an 'interface-name' must always be 
consistent with the value of the associated 
'interface-type'.  Attempts to set an interface-name
to a value inconsistent with the associated 
'interface-type' must fail with an error.
    """
    return self.__interface_name
      
  def _set_interface_name(self, v, load=False):
    """
    Setter method for interface_name, mapped from YANG variable /brocade_arp_rpc/get_arp/output/arp_entry/interface_name (union)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_interface_name is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_interface_name() directly.

    YANG Description: The Interface value. The interface value is always 
interpreted within the context of the value of 
'interface-type' leaf:

interface-type         interface-name
-----------------      --------------------
gigabitethernet        [rbridge-id]/slot/port
tengigabitethernet     [rbridge-id]/slot/port
fortygigabitethernet   [rbridge-id]/slot/port
hundredgigabitethernet [rbridge-id]/slot/port
port-channel           Port channel ID
l2vlan                 Vlan ID
unknown                Zero-length string.

The value of an 'interface-name' must always be 
consistent with the value of the associated 
'interface-type'.  Attempts to set an interface-name
to a value inconsistent with the associated 
'interface-type' must fail with an error.
    """
    if hasattr(v, "_utype"):
      v = v._utype(v)
    try:
      t = YANGDynClass(v,base=[RestrictedClassType(base_type=unicode, restriction_dict={'pattern': u'((([1-9]|[1-9][0-9]|1[0-9][0-9]|2[0-3][0-9])/)?(([0-9]|[1][0-6]))/([1-9]|[1-9][0-9]|[1-9][0-9][0-9])(:[1-4])?)', 'length': [u'3..16']}),RestrictedClassType(base_type=RestrictedClassType(base_type=long, restriction_dict={'range': ['0..4294967295']}, int_size=32), restriction_dict={'range': [u'1..6144']}),RestrictedClassType(base_type=RestrictedClassType(base_type=long, restriction_dict={'range': ['0..4294967295']}, int_size=32), restriction_dict={'range': [u'1..8191']}),], is_leaf=True, yang_name="interface-name", rest_name="interface-name", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=False, extensions={u'tailf-common': {u'info': u'The Interface value.'}}, namespace='urn:brocade.com:mgmt:brocade-arp', defining_module='brocade-arp', yang_type='union', is_config=True)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """interface_name must be of a type compatible with union""",
          'defined-type': "brocade-arp:union",
          'generated-type': """YANGDynClass(base=[RestrictedClassType(base_type=unicode, restriction_dict={'pattern': u'((([1-9]|[1-9][0-9]|1[0-9][0-9]|2[0-3][0-9])/)?(([0-9]|[1][0-6]))/([1-9]|[1-9][0-9]|[1-9][0-9][0-9])(:[1-4])?)', 'length': [u'3..16']}),RestrictedClassType(base_type=RestrictedClassType(base_type=long, restriction_dict={'range': ['0..4294967295']}, int_size=32), restriction_dict={'range': [u'1..6144']}),RestrictedClassType(base_type=RestrictedClassType(base_type=long, restriction_dict={'range': ['0..4294967295']}, int_size=32), restriction_dict={'range': [u'1..8191']}),], is_leaf=True, yang_name="interface-name", rest_name="interface-name", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=False, extensions={u'tailf-common': {u'info': u'The Interface value.'}}, namespace='urn:brocade.com:mgmt:brocade-arp', defining_module='brocade-arp', yang_type='union', is_config=True)""",
        })

    self.__interface_name = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_interface_name(self):
    self.__interface_name = YANGDynClass(base=[RestrictedClassType(base_type=unicode, restriction_dict={'pattern': u'((([1-9]|[1-9][0-9]|1[0-9][0-9]|2[0-3][0-9])/)?(([0-9]|[1][0-6]))/([1-9]|[1-9][0-9]|[1-9][0-9][0-9])(:[1-4])?)', 'length': [u'3..16']}),RestrictedClassType(base_type=RestrictedClassType(base_type=long, restriction_dict={'range': ['0..4294967295']}, int_size=32), restriction_dict={'range': [u'1..6144']}),RestrictedClassType(base_type=RestrictedClassType(base_type=long, restriction_dict={'range': ['0..4294967295']}, int_size=32), restriction_dict={'range': [u'1..8191']}),], is_leaf=True, yang_name="interface-name", rest_name="interface-name", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=False, extensions={u'tailf-common': {u'info': u'The Interface value.'}}, namespace='urn:brocade.com:mgmt:brocade-arp', defining_module='brocade-arp', yang_type='union', is_config=True)


  def _get_is_resolved(self):
    """
    Getter method for is_resolved, mapped from YANG variable /brocade_arp_rpc/get_arp/output/arp_entry/is_resolved (boolean)

    YANG Description: This indicates whether the arp entry is
resolved or not
    """
    return self.__is_resolved
      
  def _set_is_resolved(self, v, load=False):
    """
    Setter method for is_resolved, mapped from YANG variable /brocade_arp_rpc/get_arp/output/arp_entry/is_resolved (boolean)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_is_resolved is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_is_resolved() directly.

    YANG Description: This indicates whether the arp entry is
resolved or not
    """
    if hasattr(v, "_utype"):
      v = v._utype(v)
    try:
      t = YANGDynClass(v,base=YANGBool, is_leaf=True, yang_name="is-resolved", rest_name="is-resolved", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=False, namespace='urn:brocade.com:mgmt:brocade-arp', defining_module='brocade-arp', yang_type='boolean', is_config=True)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """is_resolved must be of a type compatible with boolean""",
          'defined-type': "boolean",
          'generated-type': """YANGDynClass(base=YANGBool, is_leaf=True, yang_name="is-resolved", rest_name="is-resolved", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=False, namespace='urn:brocade.com:mgmt:brocade-arp', defining_module='brocade-arp', yang_type='boolean', is_config=True)""",
        })

    self.__is_resolved = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_is_resolved(self):
    self.__is_resolved = YANGDynClass(base=YANGBool, is_leaf=True, yang_name="is-resolved", rest_name="is-resolved", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=False, namespace='urn:brocade.com:mgmt:brocade-arp', defining_module='brocade-arp', yang_type='boolean', is_config=True)


  def _get_age(self):
    """
    Getter method for age, mapped from YANG variable /brocade_arp_rpc/get_arp/output/arp_entry/age (string)

    YANG Description: This indicates the age of the arp entry
    """
    return self.__age
      
  def _set_age(self, v, load=False):
    """
    Setter method for age, mapped from YANG variable /brocade_arp_rpc/get_arp/output/arp_entry/age (string)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_age is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_age() directly.

    YANG Description: This indicates the age of the arp entry
    """
    if hasattr(v, "_utype"):
      v = v._utype(v)
    try:
      t = YANGDynClass(v,base=unicode, is_leaf=True, yang_name="age", rest_name="age", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=False, namespace='urn:brocade.com:mgmt:brocade-arp', defining_module='brocade-arp', yang_type='string', is_config=True)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """age must be of a type compatible with string""",
          'defined-type': "string",
          'generated-type': """YANGDynClass(base=unicode, is_leaf=True, yang_name="age", rest_name="age", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=False, namespace='urn:brocade.com:mgmt:brocade-arp', defining_module='brocade-arp', yang_type='string', is_config=True)""",
        })

    self.__age = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_age(self):
    self.__age = YANGDynClass(base=unicode, is_leaf=True, yang_name="age", rest_name="age", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=False, namespace='urn:brocade.com:mgmt:brocade-arp', defining_module='brocade-arp', yang_type='string', is_config=True)


  def _get_entry_type(self):
    """
    Getter method for entry_type, mapped from YANG variable /brocade_arp_rpc/get_arp/output/arp_entry/entry_type (enumeration)

    YANG Description: This indicates the type of the arp entry
    """
    return self.__entry_type
      
  def _set_entry_type(self, v, load=False):
    """
    Setter method for entry_type, mapped from YANG variable /brocade_arp_rpc/get_arp/output/arp_entry/entry_type (enumeration)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_entry_type is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_entry_type() directly.

    YANG Description: This indicates the type of the arp entry
    """
    if hasattr(v, "_utype"):
      v = v._utype(v)
    try:
      t = YANGDynClass(v,base=RestrictedClassType(base_type=unicode,                                     restriction_type="dict_key",                                     restriction_arg={u'dynamic': {'value': 2}, u'static': {'value': 1}, u'unknown': {'value': 3}},), is_leaf=True, yang_name="entry-type", rest_name="entry-type", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=False, namespace='urn:brocade.com:mgmt:brocade-arp', defining_module='brocade-arp', yang_type='enumeration', is_config=True)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """entry_type must be of a type compatible with enumeration""",
          'defined-type': "brocade-arp:enumeration",
          'generated-type': """YANGDynClass(base=RestrictedClassType(base_type=unicode,                                     restriction_type="dict_key",                                     restriction_arg={u'dynamic': {'value': 2}, u'static': {'value': 1}, u'unknown': {'value': 3}},), is_leaf=True, yang_name="entry-type", rest_name="entry-type", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=False, namespace='urn:brocade.com:mgmt:brocade-arp', defining_module='brocade-arp', yang_type='enumeration', is_config=True)""",
        })

    self.__entry_type = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_entry_type(self):
    self.__entry_type = YANGDynClass(base=RestrictedClassType(base_type=unicode,                                     restriction_type="dict_key",                                     restriction_arg={u'dynamic': {'value': 2}, u'static': {'value': 1}, u'unknown': {'value': 3}},), is_leaf=True, yang_name="entry-type", rest_name="entry-type", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=False, namespace='urn:brocade.com:mgmt:brocade-arp', defining_module='brocade-arp', yang_type='enumeration', is_config=True)

  ip_address = __builtin__.property(_get_ip_address, _set_ip_address)
  mac_address = __builtin__.property(_get_mac_address, _set_mac_address)
  interface_type = __builtin__.property(_get_interface_type, _set_interface_type)
  interface_name = __builtin__.property(_get_interface_name, _set_interface_name)
  is_resolved = __builtin__.property(_get_is_resolved, _set_is_resolved)
  age = __builtin__.property(_get_age, _set_age)
  entry_type = __builtin__.property(_get_entry_type, _set_entry_type)


  _pyangbind_elements = {'ip_address': ip_address, 'mac_address': mac_address, 'interface_type': interface_type, 'interface_name': interface_name, 'is_resolved': is_resolved, 'age': age, 'entry_type': entry_type, }


