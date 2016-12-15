
from operator import attrgetter
import pyangbind.lib.xpathhelper as xpathhelper
from pyangbind.lib.yangtypes import RestrictedPrecisionDecimalType, RestrictedClassType, TypedListType
from pyangbind.lib.yangtypes import YANGBool, YANGListType, YANGDynClass, ReferenceType
from pyangbind.lib.base import PybindBase
from decimal import Decimal
from bitarray import bitarray
import __builtin__
import ingress_policy
import egress_policy
class interface(PybindBase):
  """
  This class was auto-generated by the PythonClass plugin for PYANG
  from YANG module brocade-mac-access-list - based on the path /brocade_mac_access_list_rpc/get-mac-acl-for-intf/output/interface. Each member element of
  the container is represented as a class variable - with a specific
  YANG type.
  """
  __slots__ = ('_pybind_generated_by', '_path_helper', '_yang_name', '_rest_name', '_extmethods', '__interface_type','__interface_name','__ingress_policy','__egress_policy',)

  _yang_name = 'interface'
  _rest_name = 'interface'

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
    self.__ingress_policy = YANGDynClass(base=YANGListType(False,ingress_policy.ingress_policy, yang_name="ingress-policy", rest_name="ingress-policy", parent=self, is_container='list', user_ordered=False, path_helper=self._path_helper, yang_keys='False', extensions=None), is_container='list', yang_name="ingress-policy", rest_name="ingress-policy", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=False, extensions=None, namespace='urn:brocade.com:mgmt:brocade-mac-access-list', defining_module='brocade-mac-access-list', yang_type='list', is_config=True)
    self.__egress_policy = YANGDynClass(base=YANGListType(False,egress_policy.egress_policy, yang_name="egress-policy", rest_name="egress-policy", parent=self, is_container='list', user_ordered=False, path_helper=self._path_helper, yang_keys='False', extensions=None), is_container='list', yang_name="egress-policy", rest_name="egress-policy", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=False, extensions=None, namespace='urn:brocade.com:mgmt:brocade-mac-access-list', defining_module='brocade-mac-access-list', yang_type='list', is_config=True)
    self.__interface_type = YANGDynClass(base=RestrictedClassType(base_type=unicode,                                     restriction_type="dict_key",                                     restriction_arg={u'port-channel': {'value': 5}, u'loopback': {'value': 7}, u'fortygigabitethernet': {'value': 4}, u'unknown': {'value': 1}, u'gigabitethernet': {'value': 2}, u'tengigabitethernet': {'value': 3}, u'tunnel': {'value': 10}, u'hundredgigabitethernet': {'value': 9}, u'fibrechannel': {'value': 8}, u'l2vlan': {'value': 6}},), is_leaf=True, yang_name="interface-type", rest_name="interface-type", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=False, extensions={u'tailf-common': {u'info': u"The type of the interface. An 'unknown' type \nrepresents error scenario and should not be used."}}, is_keyval=True, namespace='urn:brocade.com:mgmt:brocade-mac-access-list', defining_module='brocade-mac-access-list', yang_type='enumeration', is_config=True)
    self.__interface_name = YANGDynClass(base=[RestrictedClassType(base_type=unicode, restriction_dict={'pattern': u'((([1-9]|[1-9][0-9]|1[0-9][0-9]|2[0-3][0-9])/)?(([0-9]|[1][0-6]))/([1-9]|[1-9][0-9]|[1-9][0-9][0-9])(:[1-4])?)', 'length': [u'3..16']}),RestrictedClassType(base_type=RestrictedClassType(base_type=long, restriction_dict={'range': ['0..4294967295']}, int_size=32), restriction_dict={'range': [u'1..6144']}),RestrictedClassType(base_type=RestrictedClassType(base_type=long, restriction_dict={'range': ['0..4294967295']}, int_size=32), restriction_dict={'range': [u'1..8191']}),], is_leaf=True, yang_name="interface-name", rest_name="interface-name", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=False, extensions={u'tailf-common': {u'info': u'The Interface value.'}}, is_keyval=True, namespace='urn:brocade.com:mgmt:brocade-mac-access-list', defining_module='brocade-mac-access-list', yang_type='union', is_config=True)

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
      return [u'brocade_mac_access_list_rpc', u'get-mac-acl-for-intf', u'output', u'interface']

  def _rest_path(self):
    if hasattr(self, "_parent"):
      if self._rest_name:
        return self._parent._rest_path()+[self._rest_name]
      else:
        return self._parent._rest_path()
    else:
      return [u'get-mac-acl-for-intf', u'output', u'interface']

  def _get_interface_type(self):
    """
    Getter method for interface_type, mapped from YANG variable /brocade_mac_access_list_rpc/get_mac_acl_for_intf/output/interface/interface_type (enumeration)

    YANG Description: The type of the interface. An 'unknown' type 
represents error scenario and should not be used.
    """
    return self.__interface_type
      
  def _set_interface_type(self, v, load=False):
    """
    Setter method for interface_type, mapped from YANG variable /brocade_mac_access_list_rpc/get_mac_acl_for_intf/output/interface/interface_type (enumeration)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_interface_type is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_interface_type() directly.

    YANG Description: The type of the interface. An 'unknown' type 
represents error scenario and should not be used.
    """
    parent = getattr(self, "_parent", None)
    if parent is not None and load is False:
      raise AttributeError("Cannot set keys directly when" +
                             " within an instantiated list")

    if hasattr(v, "_utype"):
      v = v._utype(v)
    try:
      t = YANGDynClass(v,base=RestrictedClassType(base_type=unicode,                                     restriction_type="dict_key",                                     restriction_arg={u'port-channel': {'value': 5}, u'loopback': {'value': 7}, u'fortygigabitethernet': {'value': 4}, u'unknown': {'value': 1}, u'gigabitethernet': {'value': 2}, u'tengigabitethernet': {'value': 3}, u'tunnel': {'value': 10}, u'hundredgigabitethernet': {'value': 9}, u'fibrechannel': {'value': 8}, u'l2vlan': {'value': 6}},), is_leaf=True, yang_name="interface-type", rest_name="interface-type", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=False, extensions={u'tailf-common': {u'info': u"The type of the interface. An 'unknown' type \nrepresents error scenario and should not be used."}}, is_keyval=True, namespace='urn:brocade.com:mgmt:brocade-mac-access-list', defining_module='brocade-mac-access-list', yang_type='enumeration', is_config=True)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """interface_type must be of a type compatible with enumeration""",
          'defined-type': "brocade-mac-access-list:enumeration",
          'generated-type': """YANGDynClass(base=RestrictedClassType(base_type=unicode,                                     restriction_type="dict_key",                                     restriction_arg={u'port-channel': {'value': 5}, u'loopback': {'value': 7}, u'fortygigabitethernet': {'value': 4}, u'unknown': {'value': 1}, u'gigabitethernet': {'value': 2}, u'tengigabitethernet': {'value': 3}, u'tunnel': {'value': 10}, u'hundredgigabitethernet': {'value': 9}, u'fibrechannel': {'value': 8}, u'l2vlan': {'value': 6}},), is_leaf=True, yang_name="interface-type", rest_name="interface-type", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=False, extensions={u'tailf-common': {u'info': u"The type of the interface. An 'unknown' type \nrepresents error scenario and should not be used."}}, is_keyval=True, namespace='urn:brocade.com:mgmt:brocade-mac-access-list', defining_module='brocade-mac-access-list', yang_type='enumeration', is_config=True)""",
        })

    self.__interface_type = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_interface_type(self):
    self.__interface_type = YANGDynClass(base=RestrictedClassType(base_type=unicode,                                     restriction_type="dict_key",                                     restriction_arg={u'port-channel': {'value': 5}, u'loopback': {'value': 7}, u'fortygigabitethernet': {'value': 4}, u'unknown': {'value': 1}, u'gigabitethernet': {'value': 2}, u'tengigabitethernet': {'value': 3}, u'tunnel': {'value': 10}, u'hundredgigabitethernet': {'value': 9}, u'fibrechannel': {'value': 8}, u'l2vlan': {'value': 6}},), is_leaf=True, yang_name="interface-type", rest_name="interface-type", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=False, extensions={u'tailf-common': {u'info': u"The type of the interface. An 'unknown' type \nrepresents error scenario and should not be used."}}, is_keyval=True, namespace='urn:brocade.com:mgmt:brocade-mac-access-list', defining_module='brocade-mac-access-list', yang_type='enumeration', is_config=True)


  def _get_interface_name(self):
    """
    Getter method for interface_name, mapped from YANG variable /brocade_mac_access_list_rpc/get_mac_acl_for_intf/output/interface/interface_name (union)

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
    Setter method for interface_name, mapped from YANG variable /brocade_mac_access_list_rpc/get_mac_acl_for_intf/output/interface/interface_name (union)
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
    parent = getattr(self, "_parent", None)
    if parent is not None and load is False:
      raise AttributeError("Cannot set keys directly when" +
                             " within an instantiated list")

    if hasattr(v, "_utype"):
      v = v._utype(v)
    try:
      t = YANGDynClass(v,base=[RestrictedClassType(base_type=unicode, restriction_dict={'pattern': u'((([1-9]|[1-9][0-9]|1[0-9][0-9]|2[0-3][0-9])/)?(([0-9]|[1][0-6]))/([1-9]|[1-9][0-9]|[1-9][0-9][0-9])(:[1-4])?)', 'length': [u'3..16']}),RestrictedClassType(base_type=RestrictedClassType(base_type=long, restriction_dict={'range': ['0..4294967295']}, int_size=32), restriction_dict={'range': [u'1..6144']}),RestrictedClassType(base_type=RestrictedClassType(base_type=long, restriction_dict={'range': ['0..4294967295']}, int_size=32), restriction_dict={'range': [u'1..8191']}),], is_leaf=True, yang_name="interface-name", rest_name="interface-name", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=False, extensions={u'tailf-common': {u'info': u'The Interface value.'}}, is_keyval=True, namespace='urn:brocade.com:mgmt:brocade-mac-access-list', defining_module='brocade-mac-access-list', yang_type='union', is_config=True)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """interface_name must be of a type compatible with union""",
          'defined-type': "brocade-mac-access-list:union",
          'generated-type': """YANGDynClass(base=[RestrictedClassType(base_type=unicode, restriction_dict={'pattern': u'((([1-9]|[1-9][0-9]|1[0-9][0-9]|2[0-3][0-9])/)?(([0-9]|[1][0-6]))/([1-9]|[1-9][0-9]|[1-9][0-9][0-9])(:[1-4])?)', 'length': [u'3..16']}),RestrictedClassType(base_type=RestrictedClassType(base_type=long, restriction_dict={'range': ['0..4294967295']}, int_size=32), restriction_dict={'range': [u'1..6144']}),RestrictedClassType(base_type=RestrictedClassType(base_type=long, restriction_dict={'range': ['0..4294967295']}, int_size=32), restriction_dict={'range': [u'1..8191']}),], is_leaf=True, yang_name="interface-name", rest_name="interface-name", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=False, extensions={u'tailf-common': {u'info': u'The Interface value.'}}, is_keyval=True, namespace='urn:brocade.com:mgmt:brocade-mac-access-list', defining_module='brocade-mac-access-list', yang_type='union', is_config=True)""",
        })

    self.__interface_name = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_interface_name(self):
    self.__interface_name = YANGDynClass(base=[RestrictedClassType(base_type=unicode, restriction_dict={'pattern': u'((([1-9]|[1-9][0-9]|1[0-9][0-9]|2[0-3][0-9])/)?(([0-9]|[1][0-6]))/([1-9]|[1-9][0-9]|[1-9][0-9][0-9])(:[1-4])?)', 'length': [u'3..16']}),RestrictedClassType(base_type=RestrictedClassType(base_type=long, restriction_dict={'range': ['0..4294967295']}, int_size=32), restriction_dict={'range': [u'1..6144']}),RestrictedClassType(base_type=RestrictedClassType(base_type=long, restriction_dict={'range': ['0..4294967295']}, int_size=32), restriction_dict={'range': [u'1..8191']}),], is_leaf=True, yang_name="interface-name", rest_name="interface-name", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=False, extensions={u'tailf-common': {u'info': u'The Interface value.'}}, is_keyval=True, namespace='urn:brocade.com:mgmt:brocade-mac-access-list', defining_module='brocade-mac-access-list', yang_type='union', is_config=True)


  def _get_ingress_policy(self):
    """
    Getter method for ingress_policy, mapped from YANG variable /brocade_mac_access_list_rpc/get_mac_acl_for_intf/output/interface/ingress_policy (list)

    YANG Description: Ingress policy details applied on this
interface.
    """
    return self.__ingress_policy
      
  def _set_ingress_policy(self, v, load=False):
    """
    Setter method for ingress_policy, mapped from YANG variable /brocade_mac_access_list_rpc/get_mac_acl_for_intf/output/interface/ingress_policy (list)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_ingress_policy is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_ingress_policy() directly.

    YANG Description: Ingress policy details applied on this
interface.
    """
    if hasattr(v, "_utype"):
      v = v._utype(v)
    try:
      t = YANGDynClass(v,base=YANGListType(False,ingress_policy.ingress_policy, yang_name="ingress-policy", rest_name="ingress-policy", parent=self, is_container='list', user_ordered=False, path_helper=self._path_helper, yang_keys='False', extensions=None), is_container='list', yang_name="ingress-policy", rest_name="ingress-policy", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=False, extensions=None, namespace='urn:brocade.com:mgmt:brocade-mac-access-list', defining_module='brocade-mac-access-list', yang_type='list', is_config=True)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """ingress_policy must be of a type compatible with list""",
          'defined-type': "list",
          'generated-type': """YANGDynClass(base=YANGListType(False,ingress_policy.ingress_policy, yang_name="ingress-policy", rest_name="ingress-policy", parent=self, is_container='list', user_ordered=False, path_helper=self._path_helper, yang_keys='False', extensions=None), is_container='list', yang_name="ingress-policy", rest_name="ingress-policy", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=False, extensions=None, namespace='urn:brocade.com:mgmt:brocade-mac-access-list', defining_module='brocade-mac-access-list', yang_type='list', is_config=True)""",
        })

    self.__ingress_policy = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_ingress_policy(self):
    self.__ingress_policy = YANGDynClass(base=YANGListType(False,ingress_policy.ingress_policy, yang_name="ingress-policy", rest_name="ingress-policy", parent=self, is_container='list', user_ordered=False, path_helper=self._path_helper, yang_keys='False', extensions=None), is_container='list', yang_name="ingress-policy", rest_name="ingress-policy", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=False, extensions=None, namespace='urn:brocade.com:mgmt:brocade-mac-access-list', defining_module='brocade-mac-access-list', yang_type='list', is_config=True)


  def _get_egress_policy(self):
    """
    Getter method for egress_policy, mapped from YANG variable /brocade_mac_access_list_rpc/get_mac_acl_for_intf/output/interface/egress_policy (list)

    YANG Description: Egress policy details applied on this
interface.
    """
    return self.__egress_policy
      
  def _set_egress_policy(self, v, load=False):
    """
    Setter method for egress_policy, mapped from YANG variable /brocade_mac_access_list_rpc/get_mac_acl_for_intf/output/interface/egress_policy (list)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_egress_policy is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_egress_policy() directly.

    YANG Description: Egress policy details applied on this
interface.
    """
    if hasattr(v, "_utype"):
      v = v._utype(v)
    try:
      t = YANGDynClass(v,base=YANGListType(False,egress_policy.egress_policy, yang_name="egress-policy", rest_name="egress-policy", parent=self, is_container='list', user_ordered=False, path_helper=self._path_helper, yang_keys='False', extensions=None), is_container='list', yang_name="egress-policy", rest_name="egress-policy", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=False, extensions=None, namespace='urn:brocade.com:mgmt:brocade-mac-access-list', defining_module='brocade-mac-access-list', yang_type='list', is_config=True)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """egress_policy must be of a type compatible with list""",
          'defined-type': "list",
          'generated-type': """YANGDynClass(base=YANGListType(False,egress_policy.egress_policy, yang_name="egress-policy", rest_name="egress-policy", parent=self, is_container='list', user_ordered=False, path_helper=self._path_helper, yang_keys='False', extensions=None), is_container='list', yang_name="egress-policy", rest_name="egress-policy", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=False, extensions=None, namespace='urn:brocade.com:mgmt:brocade-mac-access-list', defining_module='brocade-mac-access-list', yang_type='list', is_config=True)""",
        })

    self.__egress_policy = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_egress_policy(self):
    self.__egress_policy = YANGDynClass(base=YANGListType(False,egress_policy.egress_policy, yang_name="egress-policy", rest_name="egress-policy", parent=self, is_container='list', user_ordered=False, path_helper=self._path_helper, yang_keys='False', extensions=None), is_container='list', yang_name="egress-policy", rest_name="egress-policy", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=False, extensions=None, namespace='urn:brocade.com:mgmt:brocade-mac-access-list', defining_module='brocade-mac-access-list', yang_type='list', is_config=True)

  interface_type = __builtin__.property(_get_interface_type, _set_interface_type)
  interface_name = __builtin__.property(_get_interface_name, _set_interface_name)
  ingress_policy = __builtin__.property(_get_ingress_policy, _set_ingress_policy)
  egress_policy = __builtin__.property(_get_egress_policy, _set_egress_policy)


  _pyangbind_elements = {'interface_type': interface_type, 'interface_name': interface_name, 'ingress_policy': ingress_policy, 'egress_policy': egress_policy, }


