
from operator import attrgetter
import pyangbind.lib.xpathhelper as xpathhelper
from pyangbind.lib.yangtypes import RestrictedPrecisionDecimalType, RestrictedClassType, TypedListType
from pyangbind.lib.yangtypes import YANGBool, YANGListType, YANGDynClass, ReferenceType
from pyangbind.lib.base import PybindBase
from decimal import Decimal
from bitarray import bitarray
import __builtin__
import forwarding_interface
import last_mac_address_details
class input(PybindBase):
  """
  This class was auto-generated by the PythonClass plugin for PYANG
  from YANG module brocade-mac-address-table - based on the path /brocade_mac_address_table_rpc/get-mac-address-table/input. Each member element of
  the container is represented as a class variable - with a specific
  YANG type.
  """
  __slots__ = ('_pybind_generated_by', '_path_helper', '_yang_name', '_rest_name', '_extmethods', '__mac_address','__forwarding_interface','__mac_type','__last_mac_address_details','__forwarding_interface_type','__forwarding_interface_name','__mac_address_type',)

  _yang_name = 'input'
  _rest_name = 'input'

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
    self.__forwarding_interface_name = YANGDynClass(base=[RestrictedClassType(base_type=unicode, restriction_dict={'pattern': u'((([0-9]|[1][0-6]))/([1-9]|[1-9][0-9]|[1-9][0-9][0-9])(:[1-4])?)', 'length': [u'3..16']}),RestrictedClassType(base_type=RestrictedClassType(base_type=long, restriction_dict={'range': ['0..4294967295']}, int_size=32), restriction_dict={'range': [u'1..1024']}),RestrictedClassType(base_type=RestrictedClassType(base_type=long, restriction_dict={'range': ['0..4294967295']}, int_size=32), restriction_dict={'range': [u'1..100000']}),], is_leaf=True, yang_name="forwarding-interface-name", rest_name="forwarding-interface-name", parent=self, choice=(u'request-type', u'get-next-request'), path_helper=self._path_helper, extmethods=self._extmethods, register_paths=False, extensions={u'tailf-common': {u'info': u'The Interface name.'}}, namespace='urn:brocade.com:mgmt:brocade-mac-address-table', defining_module='brocade-mac-address-table', yang_type='union', is_config=True)
    self.__last_mac_address_details = YANGDynClass(base=last_mac_address_details.last_mac_address_details, is_container='container', presence=False, yang_name="last-mac-address-details", rest_name="last-mac-address-details", parent=self, choice=(u'request-type', u'get-next-request'), path_helper=self._path_helper, extmethods=self._extmethods, register_paths=False, extensions=None, namespace='urn:brocade.com:mgmt:brocade-mac-address-table', defining_module='brocade-mac-address-table', yang_type='container', is_config=True)
    self.__mac_address = YANGDynClass(base=RestrictedClassType(base_type=unicode, restriction_dict={'pattern': u'[0-9a-fA-F]{2}(:[0-9a-fA-F]{2}){5}'}), is_leaf=True, yang_name="mac-address", rest_name="mac-address", parent=self, choice=(u'request-type', u'get-request'), path_helper=self._path_helper, extmethods=self._extmethods, register_paths=False, namespace='urn:brocade.com:mgmt:brocade-mac-address-table', defining_module='brocade-mac-address-table', yang_type='yang:mac-address', is_config=True)
    self.__mac_type = YANGDynClass(base=RestrictedClassType(base_type=unicode,                                     restriction_type="dict_key",                                     restriction_arg={u'dynamic': {'value': 2}, u'static': {'value': 1}},), is_leaf=True, yang_name="mac-type", rest_name="mac-type", parent=self, choice=(u'request-type', u'get-interface-based-request'), path_helper=self._path_helper, extmethods=self._extmethods, register_paths=False, namespace='urn:brocade.com:mgmt:brocade-mac-address-table', defining_module='brocade-mac-address-table', yang_type='enumeration', is_config=True)
    self.__mac_address_type = YANGDynClass(base=RestrictedClassType(base_type=unicode,                                     restriction_type="dict_key",                                     restriction_arg={u'dynamic': {'value': 2}, u'static': {'value': 1}},), is_leaf=True, yang_name="mac-address-type", rest_name="mac-address-type", parent=self, choice=(u'request-type', u'get-next-request'), path_helper=self._path_helper, extmethods=self._extmethods, register_paths=False, namespace='urn:brocade.com:mgmt:brocade-mac-address-table', defining_module='brocade-mac-address-table', yang_type='enumeration', is_config=True)
    self.__forwarding_interface = YANGDynClass(base=forwarding_interface.forwarding_interface, is_container='container', presence=False, yang_name="forwarding-interface", rest_name="forwarding-interface", parent=self, choice=(u'request-type', u'get-interface-based-request'), path_helper=self._path_helper, extmethods=self._extmethods, register_paths=False, extensions=None, namespace='urn:brocade.com:mgmt:brocade-mac-address-table', defining_module='brocade-mac-address-table', yang_type='container', is_config=True)
    self.__forwarding_interface_type = YANGDynClass(base=RestrictedClassType(base_type=unicode,                                     restriction_type="dict_key",                                     restriction_arg={u'tunnel': {'value': 12}, u'unknown': {'value': 1}, u'port-channel': {'value': 5}, u'ethernet': {'value': 10}},), is_leaf=True, yang_name="forwarding-interface-type", rest_name="forwarding-interface-type", parent=self, choice=(u'request-type', u'get-next-request'), path_helper=self._path_helper, extmethods=self._extmethods, register_paths=False, extensions={u'tailf-common': {u'info': u"The type of the interface. An 'unknown' type \nrepresents error scenario and should not be used."}}, namespace='urn:brocade.com:mgmt:brocade-mac-address-table', defining_module='brocade-mac-address-table', yang_type='enumeration', is_config=True)

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
      return [u'brocade_mac_address_table_rpc', u'get-mac-address-table', u'input']

  def _rest_path(self):
    if hasattr(self, "_parent"):
      if self._rest_name:
        return self._parent._rest_path()+[self._rest_name]
      else:
        return self._parent._rest_path()
    else:
      return [u'get-mac-address-table', u'input']

  def _get_mac_address(self):
    """
    Getter method for mac_address, mapped from YANG variable /brocade_mac_address_table_rpc/get_mac_address_table/input/mac_address (yang:mac-address)

    YANG Description: The Mac Address for which the
corresponding mac entry will be
fetched. The i/p should be in 
xx:xx:xx:xx:xx:xx format.
    """
    return self.__mac_address
      
  def _set_mac_address(self, v, load=False):
    """
    Setter method for mac_address, mapped from YANG variable /brocade_mac_address_table_rpc/get_mac_address_table/input/mac_address (yang:mac-address)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_mac_address is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_mac_address() directly.

    YANG Description: The Mac Address for which the
corresponding mac entry will be
fetched. The i/p should be in 
xx:xx:xx:xx:xx:xx format.
    """
    if hasattr(v, "_utype"):
      v = v._utype(v)
    try:
      t = YANGDynClass(v,base=RestrictedClassType(base_type=unicode, restriction_dict={'pattern': u'[0-9a-fA-F]{2}(:[0-9a-fA-F]{2}){5}'}), is_leaf=True, yang_name="mac-address", rest_name="mac-address", parent=self, choice=(u'request-type', u'get-request'), path_helper=self._path_helper, extmethods=self._extmethods, register_paths=False, namespace='urn:brocade.com:mgmt:brocade-mac-address-table', defining_module='brocade-mac-address-table', yang_type='yang:mac-address', is_config=True)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """mac_address must be of a type compatible with yang:mac-address""",
          'defined-type': "yang:mac-address",
          'generated-type': """YANGDynClass(base=RestrictedClassType(base_type=unicode, restriction_dict={'pattern': u'[0-9a-fA-F]{2}(:[0-9a-fA-F]{2}){5}'}), is_leaf=True, yang_name="mac-address", rest_name="mac-address", parent=self, choice=(u'request-type', u'get-request'), path_helper=self._path_helper, extmethods=self._extmethods, register_paths=False, namespace='urn:brocade.com:mgmt:brocade-mac-address-table', defining_module='brocade-mac-address-table', yang_type='yang:mac-address', is_config=True)""",
        })

    self.__mac_address = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_mac_address(self):
    self.__mac_address = YANGDynClass(base=RestrictedClassType(base_type=unicode, restriction_dict={'pattern': u'[0-9a-fA-F]{2}(:[0-9a-fA-F]{2}){5}'}), is_leaf=True, yang_name="mac-address", rest_name="mac-address", parent=self, choice=(u'request-type', u'get-request'), path_helper=self._path_helper, extmethods=self._extmethods, register_paths=False, namespace='urn:brocade.com:mgmt:brocade-mac-address-table', defining_module='brocade-mac-address-table', yang_type='yang:mac-address', is_config=True)


  def _get_forwarding_interface(self):
    """
    Getter method for forwarding_interface, mapped from YANG variable /brocade_mac_address_table_rpc/get_mac_address_table/input/forwarding_interface (container)

    YANG Description: The interface for which corresponding
MAC entries will be fetched.
    """
    return self.__forwarding_interface
      
  def _set_forwarding_interface(self, v, load=False):
    """
    Setter method for forwarding_interface, mapped from YANG variable /brocade_mac_address_table_rpc/get_mac_address_table/input/forwarding_interface (container)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_forwarding_interface is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_forwarding_interface() directly.

    YANG Description: The interface for which corresponding
MAC entries will be fetched.
    """
    if hasattr(v, "_utype"):
      v = v._utype(v)
    try:
      t = YANGDynClass(v,base=forwarding_interface.forwarding_interface, is_container='container', presence=False, yang_name="forwarding-interface", rest_name="forwarding-interface", parent=self, choice=(u'request-type', u'get-interface-based-request'), path_helper=self._path_helper, extmethods=self._extmethods, register_paths=False, extensions=None, namespace='urn:brocade.com:mgmt:brocade-mac-address-table', defining_module='brocade-mac-address-table', yang_type='container', is_config=True)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """forwarding_interface must be of a type compatible with container""",
          'defined-type': "container",
          'generated-type': """YANGDynClass(base=forwarding_interface.forwarding_interface, is_container='container', presence=False, yang_name="forwarding-interface", rest_name="forwarding-interface", parent=self, choice=(u'request-type', u'get-interface-based-request'), path_helper=self._path_helper, extmethods=self._extmethods, register_paths=False, extensions=None, namespace='urn:brocade.com:mgmt:brocade-mac-address-table', defining_module='brocade-mac-address-table', yang_type='container', is_config=True)""",
        })

    self.__forwarding_interface = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_forwarding_interface(self):
    self.__forwarding_interface = YANGDynClass(base=forwarding_interface.forwarding_interface, is_container='container', presence=False, yang_name="forwarding-interface", rest_name="forwarding-interface", parent=self, choice=(u'request-type', u'get-interface-based-request'), path_helper=self._path_helper, extmethods=self._extmethods, register_paths=False, extensions=None, namespace='urn:brocade.com:mgmt:brocade-mac-address-table', defining_module='brocade-mac-address-table', yang_type='container', is_config=True)


  def _get_mac_type(self):
    """
    Getter method for mac_type, mapped from YANG variable /brocade_mac_address_table_rpc/get_mac_address_table/input/mac_type (enumeration)

    YANG Description: Type of MAC addresses to be fetched.
    """
    return self.__mac_type
      
  def _set_mac_type(self, v, load=False):
    """
    Setter method for mac_type, mapped from YANG variable /brocade_mac_address_table_rpc/get_mac_address_table/input/mac_type (enumeration)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_mac_type is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_mac_type() directly.

    YANG Description: Type of MAC addresses to be fetched.
    """
    if hasattr(v, "_utype"):
      v = v._utype(v)
    try:
      t = YANGDynClass(v,base=RestrictedClassType(base_type=unicode,                                     restriction_type="dict_key",                                     restriction_arg={u'dynamic': {'value': 2}, u'static': {'value': 1}},), is_leaf=True, yang_name="mac-type", rest_name="mac-type", parent=self, choice=(u'request-type', u'get-interface-based-request'), path_helper=self._path_helper, extmethods=self._extmethods, register_paths=False, namespace='urn:brocade.com:mgmt:brocade-mac-address-table', defining_module='brocade-mac-address-table', yang_type='enumeration', is_config=True)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """mac_type must be of a type compatible with enumeration""",
          'defined-type': "brocade-mac-address-table:enumeration",
          'generated-type': """YANGDynClass(base=RestrictedClassType(base_type=unicode,                                     restriction_type="dict_key",                                     restriction_arg={u'dynamic': {'value': 2}, u'static': {'value': 1}},), is_leaf=True, yang_name="mac-type", rest_name="mac-type", parent=self, choice=(u'request-type', u'get-interface-based-request'), path_helper=self._path_helper, extmethods=self._extmethods, register_paths=False, namespace='urn:brocade.com:mgmt:brocade-mac-address-table', defining_module='brocade-mac-address-table', yang_type='enumeration', is_config=True)""",
        })

    self.__mac_type = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_mac_type(self):
    self.__mac_type = YANGDynClass(base=RestrictedClassType(base_type=unicode,                                     restriction_type="dict_key",                                     restriction_arg={u'dynamic': {'value': 2}, u'static': {'value': 1}},), is_leaf=True, yang_name="mac-type", rest_name="mac-type", parent=self, choice=(u'request-type', u'get-interface-based-request'), path_helper=self._path_helper, extmethods=self._extmethods, register_paths=False, namespace='urn:brocade.com:mgmt:brocade-mac-address-table', defining_module='brocade-mac-address-table', yang_type='enumeration', is_config=True)


  def _get_last_mac_address_details(self):
    """
    Getter method for last_mac_address_details, mapped from YANG variable /brocade_mac_address_table_rpc/get_mac_address_table/input/last_mac_address_details (container)
    """
    return self.__last_mac_address_details
      
  def _set_last_mac_address_details(self, v, load=False):
    """
    Setter method for last_mac_address_details, mapped from YANG variable /brocade_mac_address_table_rpc/get_mac_address_table/input/last_mac_address_details (container)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_last_mac_address_details is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_last_mac_address_details() directly.
    """
    if hasattr(v, "_utype"):
      v = v._utype(v)
    try:
      t = YANGDynClass(v,base=last_mac_address_details.last_mac_address_details, is_container='container', presence=False, yang_name="last-mac-address-details", rest_name="last-mac-address-details", parent=self, choice=(u'request-type', u'get-next-request'), path_helper=self._path_helper, extmethods=self._extmethods, register_paths=False, extensions=None, namespace='urn:brocade.com:mgmt:brocade-mac-address-table', defining_module='brocade-mac-address-table', yang_type='container', is_config=True)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """last_mac_address_details must be of a type compatible with container""",
          'defined-type': "container",
          'generated-type': """YANGDynClass(base=last_mac_address_details.last_mac_address_details, is_container='container', presence=False, yang_name="last-mac-address-details", rest_name="last-mac-address-details", parent=self, choice=(u'request-type', u'get-next-request'), path_helper=self._path_helper, extmethods=self._extmethods, register_paths=False, extensions=None, namespace='urn:brocade.com:mgmt:brocade-mac-address-table', defining_module='brocade-mac-address-table', yang_type='container', is_config=True)""",
        })

    self.__last_mac_address_details = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_last_mac_address_details(self):
    self.__last_mac_address_details = YANGDynClass(base=last_mac_address_details.last_mac_address_details, is_container='container', presence=False, yang_name="last-mac-address-details", rest_name="last-mac-address-details", parent=self, choice=(u'request-type', u'get-next-request'), path_helper=self._path_helper, extmethods=self._extmethods, register_paths=False, extensions=None, namespace='urn:brocade.com:mgmt:brocade-mac-address-table', defining_module='brocade-mac-address-table', yang_type='container', is_config=True)


  def _get_forwarding_interface_type(self):
    """
    Getter method for forwarding_interface_type, mapped from YANG variable /brocade_mac_address_table_rpc/get_mac_address_table/input/forwarding_interface_type (enumeration)

    YANG Description: The type of the interface. An 'unknown' type 
represents error scenario and should not be used.
    """
    return self.__forwarding_interface_type
      
  def _set_forwarding_interface_type(self, v, load=False):
    """
    Setter method for forwarding_interface_type, mapped from YANG variable /brocade_mac_address_table_rpc/get_mac_address_table/input/forwarding_interface_type (enumeration)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_forwarding_interface_type is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_forwarding_interface_type() directly.

    YANG Description: The type of the interface. An 'unknown' type 
represents error scenario and should not be used.
    """
    if hasattr(v, "_utype"):
      v = v._utype(v)
    try:
      t = YANGDynClass(v,base=RestrictedClassType(base_type=unicode,                                     restriction_type="dict_key",                                     restriction_arg={u'tunnel': {'value': 12}, u'unknown': {'value': 1}, u'port-channel': {'value': 5}, u'ethernet': {'value': 10}},), is_leaf=True, yang_name="forwarding-interface-type", rest_name="forwarding-interface-type", parent=self, choice=(u'request-type', u'get-next-request'), path_helper=self._path_helper, extmethods=self._extmethods, register_paths=False, extensions={u'tailf-common': {u'info': u"The type of the interface. An 'unknown' type \nrepresents error scenario and should not be used."}}, namespace='urn:brocade.com:mgmt:brocade-mac-address-table', defining_module='brocade-mac-address-table', yang_type='enumeration', is_config=True)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """forwarding_interface_type must be of a type compatible with enumeration""",
          'defined-type': "brocade-mac-address-table:enumeration",
          'generated-type': """YANGDynClass(base=RestrictedClassType(base_type=unicode,                                     restriction_type="dict_key",                                     restriction_arg={u'tunnel': {'value': 12}, u'unknown': {'value': 1}, u'port-channel': {'value': 5}, u'ethernet': {'value': 10}},), is_leaf=True, yang_name="forwarding-interface-type", rest_name="forwarding-interface-type", parent=self, choice=(u'request-type', u'get-next-request'), path_helper=self._path_helper, extmethods=self._extmethods, register_paths=False, extensions={u'tailf-common': {u'info': u"The type of the interface. An 'unknown' type \nrepresents error scenario and should not be used."}}, namespace='urn:brocade.com:mgmt:brocade-mac-address-table', defining_module='brocade-mac-address-table', yang_type='enumeration', is_config=True)""",
        })

    self.__forwarding_interface_type = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_forwarding_interface_type(self):
    self.__forwarding_interface_type = YANGDynClass(base=RestrictedClassType(base_type=unicode,                                     restriction_type="dict_key",                                     restriction_arg={u'tunnel': {'value': 12}, u'unknown': {'value': 1}, u'port-channel': {'value': 5}, u'ethernet': {'value': 10}},), is_leaf=True, yang_name="forwarding-interface-type", rest_name="forwarding-interface-type", parent=self, choice=(u'request-type', u'get-next-request'), path_helper=self._path_helper, extmethods=self._extmethods, register_paths=False, extensions={u'tailf-common': {u'info': u"The type of the interface. An 'unknown' type \nrepresents error scenario and should not be used."}}, namespace='urn:brocade.com:mgmt:brocade-mac-address-table', defining_module='brocade-mac-address-table', yang_type='enumeration', is_config=True)


  def _get_forwarding_interface_name(self):
    """
    Getter method for forwarding_interface_name, mapped from YANG variable /brocade_mac_address_table_rpc/get_mac_address_table/input/forwarding_interface_name (union)

    YANG Description: The Interface name. The interface name is always 
interpreted within the context of the value of 
'interface-type' leaf:

interface-type         interface-name
-----------------      --------------------
ethernet               [slot/port]
port-channel           Port channel ID
unknown                Zero-length string.

The value of an 'forwarding-interface-name' must always be 
consistent with the value of the associated 
'forwarding-interface-type'.  Attempts to set an interface-name
to a value inconsistent with the associated 
'forwarding-interface-type' must fail with an error.
    """
    return self.__forwarding_interface_name
      
  def _set_forwarding_interface_name(self, v, load=False):
    """
    Setter method for forwarding_interface_name, mapped from YANG variable /brocade_mac_address_table_rpc/get_mac_address_table/input/forwarding_interface_name (union)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_forwarding_interface_name is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_forwarding_interface_name() directly.

    YANG Description: The Interface name. The interface name is always 
interpreted within the context of the value of 
'interface-type' leaf:

interface-type         interface-name
-----------------      --------------------
ethernet               [slot/port]
port-channel           Port channel ID
unknown                Zero-length string.

The value of an 'forwarding-interface-name' must always be 
consistent with the value of the associated 
'forwarding-interface-type'.  Attempts to set an interface-name
to a value inconsistent with the associated 
'forwarding-interface-type' must fail with an error.
    """
    if hasattr(v, "_utype"):
      v = v._utype(v)
    try:
      t = YANGDynClass(v,base=[RestrictedClassType(base_type=unicode, restriction_dict={'pattern': u'((([0-9]|[1][0-6]))/([1-9]|[1-9][0-9]|[1-9][0-9][0-9])(:[1-4])?)', 'length': [u'3..16']}),RestrictedClassType(base_type=RestrictedClassType(base_type=long, restriction_dict={'range': ['0..4294967295']}, int_size=32), restriction_dict={'range': [u'1..1024']}),RestrictedClassType(base_type=RestrictedClassType(base_type=long, restriction_dict={'range': ['0..4294967295']}, int_size=32), restriction_dict={'range': [u'1..100000']}),], is_leaf=True, yang_name="forwarding-interface-name", rest_name="forwarding-interface-name", parent=self, choice=(u'request-type', u'get-next-request'), path_helper=self._path_helper, extmethods=self._extmethods, register_paths=False, extensions={u'tailf-common': {u'info': u'The Interface name.'}}, namespace='urn:brocade.com:mgmt:brocade-mac-address-table', defining_module='brocade-mac-address-table', yang_type='union', is_config=True)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """forwarding_interface_name must be of a type compatible with union""",
          'defined-type': "brocade-mac-address-table:union",
          'generated-type': """YANGDynClass(base=[RestrictedClassType(base_type=unicode, restriction_dict={'pattern': u'((([0-9]|[1][0-6]))/([1-9]|[1-9][0-9]|[1-9][0-9][0-9])(:[1-4])?)', 'length': [u'3..16']}),RestrictedClassType(base_type=RestrictedClassType(base_type=long, restriction_dict={'range': ['0..4294967295']}, int_size=32), restriction_dict={'range': [u'1..1024']}),RestrictedClassType(base_type=RestrictedClassType(base_type=long, restriction_dict={'range': ['0..4294967295']}, int_size=32), restriction_dict={'range': [u'1..100000']}),], is_leaf=True, yang_name="forwarding-interface-name", rest_name="forwarding-interface-name", parent=self, choice=(u'request-type', u'get-next-request'), path_helper=self._path_helper, extmethods=self._extmethods, register_paths=False, extensions={u'tailf-common': {u'info': u'The Interface name.'}}, namespace='urn:brocade.com:mgmt:brocade-mac-address-table', defining_module='brocade-mac-address-table', yang_type='union', is_config=True)""",
        })

    self.__forwarding_interface_name = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_forwarding_interface_name(self):
    self.__forwarding_interface_name = YANGDynClass(base=[RestrictedClassType(base_type=unicode, restriction_dict={'pattern': u'((([0-9]|[1][0-6]))/([1-9]|[1-9][0-9]|[1-9][0-9][0-9])(:[1-4])?)', 'length': [u'3..16']}),RestrictedClassType(base_type=RestrictedClassType(base_type=long, restriction_dict={'range': ['0..4294967295']}, int_size=32), restriction_dict={'range': [u'1..1024']}),RestrictedClassType(base_type=RestrictedClassType(base_type=long, restriction_dict={'range': ['0..4294967295']}, int_size=32), restriction_dict={'range': [u'1..100000']}),], is_leaf=True, yang_name="forwarding-interface-name", rest_name="forwarding-interface-name", parent=self, choice=(u'request-type', u'get-next-request'), path_helper=self._path_helper, extmethods=self._extmethods, register_paths=False, extensions={u'tailf-common': {u'info': u'The Interface name.'}}, namespace='urn:brocade.com:mgmt:brocade-mac-address-table', defining_module='brocade-mac-address-table', yang_type='union', is_config=True)


  def _get_mac_address_type(self):
    """
    Getter method for mac_address_type, mapped from YANG variable /brocade_mac_address_table_rpc/get_mac_address_table/input/mac_address_type (enumeration)

    YANG Description: Type of MAC addresses to be fetched.
    """
    return self.__mac_address_type
      
  def _set_mac_address_type(self, v, load=False):
    """
    Setter method for mac_address_type, mapped from YANG variable /brocade_mac_address_table_rpc/get_mac_address_table/input/mac_address_type (enumeration)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_mac_address_type is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_mac_address_type() directly.

    YANG Description: Type of MAC addresses to be fetched.
    """
    if hasattr(v, "_utype"):
      v = v._utype(v)
    try:
      t = YANGDynClass(v,base=RestrictedClassType(base_type=unicode,                                     restriction_type="dict_key",                                     restriction_arg={u'dynamic': {'value': 2}, u'static': {'value': 1}},), is_leaf=True, yang_name="mac-address-type", rest_name="mac-address-type", parent=self, choice=(u'request-type', u'get-next-request'), path_helper=self._path_helper, extmethods=self._extmethods, register_paths=False, namespace='urn:brocade.com:mgmt:brocade-mac-address-table', defining_module='brocade-mac-address-table', yang_type='enumeration', is_config=True)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """mac_address_type must be of a type compatible with enumeration""",
          'defined-type': "brocade-mac-address-table:enumeration",
          'generated-type': """YANGDynClass(base=RestrictedClassType(base_type=unicode,                                     restriction_type="dict_key",                                     restriction_arg={u'dynamic': {'value': 2}, u'static': {'value': 1}},), is_leaf=True, yang_name="mac-address-type", rest_name="mac-address-type", parent=self, choice=(u'request-type', u'get-next-request'), path_helper=self._path_helper, extmethods=self._extmethods, register_paths=False, namespace='urn:brocade.com:mgmt:brocade-mac-address-table', defining_module='brocade-mac-address-table', yang_type='enumeration', is_config=True)""",
        })

    self.__mac_address_type = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_mac_address_type(self):
    self.__mac_address_type = YANGDynClass(base=RestrictedClassType(base_type=unicode,                                     restriction_type="dict_key",                                     restriction_arg={u'dynamic': {'value': 2}, u'static': {'value': 1}},), is_leaf=True, yang_name="mac-address-type", rest_name="mac-address-type", parent=self, choice=(u'request-type', u'get-next-request'), path_helper=self._path_helper, extmethods=self._extmethods, register_paths=False, namespace='urn:brocade.com:mgmt:brocade-mac-address-table', defining_module='brocade-mac-address-table', yang_type='enumeration', is_config=True)

  mac_address = __builtin__.property(_get_mac_address, _set_mac_address)
  forwarding_interface = __builtin__.property(_get_forwarding_interface, _set_forwarding_interface)
  mac_type = __builtin__.property(_get_mac_type, _set_mac_type)
  last_mac_address_details = __builtin__.property(_get_last_mac_address_details, _set_last_mac_address_details)
  forwarding_interface_type = __builtin__.property(_get_forwarding_interface_type, _set_forwarding_interface_type)
  forwarding_interface_name = __builtin__.property(_get_forwarding_interface_name, _set_forwarding_interface_name)
  mac_address_type = __builtin__.property(_get_mac_address_type, _set_mac_address_type)

  __choices__ = {u'request-type': {u'get-interface-based-request': [u'forwarding_interface', u'mac_type'], u'get-next-request': [u'last_mac_address_details', u'forwarding_interface_type', u'forwarding_interface_name', u'mac_address_type'], u'get-request': [u'mac_address']}}
  _pyangbind_elements = {'mac_address': mac_address, 'forwarding_interface': forwarding_interface, 'mac_type': mac_type, 'last_mac_address_details': last_mac_address_details, 'forwarding_interface_type': forwarding_interface_type, 'forwarding_interface_name': forwarding_interface_name, 'mac_address_type': mac_address_type, }


