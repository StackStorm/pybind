
from operator import attrgetter
import pyangbind.lib.xpathhelper as xpathhelper
from pyangbind.lib.yangtypes import RestrictedPrecisionDecimalType, RestrictedClassType, TypedListType
from pyangbind.lib.yangtypes import YANGBool, YANGListType, YANGDynClass, ReferenceType
from pyangbind.lib.base import PybindBase
from decimal import Decimal
from bitarray import bitarray
import __builtin__
class isns_device_list(PybindBase):
  """
  This class was auto-generated by the PythonClass plugin for PYANG
  from YANG module brocade-isns-ext - based on the path /brocade_isns_ext_rpc/isns-get-device-brief/output/isns-entity-list/isns-device-list. Each member element of
  the container is represented as a class variable - with a specific
  YANG type.

  YANG Description: This is a list of logged-in iSNS devices.
Each row represents a logged-in iSNS device
operational details such as iqn,,
ip addressand device type.
The device iqn is used as the key for this
list as it will be unique for each entry.
  """
  __slots__ = ('_pybind_generated_by', '_path_helper', '_yang_name', '_rest_name', '_extmethods', '__isns_device_ipaddress','__isns_device_iqn','__isns_device_type',)

  _yang_name = 'isns-device-list'
  _rest_name = 'isns-device-list'

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
    self.__isns_device_type = YANGDynClass(base=RestrictedClassType(base_type=unicode,                                     restriction_type="dict_key",                                     restriction_arg={u'device-control': {'value': 4}, u'device-target': {'value': 1}, u'device-initiator': {'value': 2}},), is_leaf=True, yang_name="isns-device-type", rest_name="isns-device-type", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=False, namespace='urn:brocade.com:mgmt:brocade-isns-ext', defining_module='brocade-isns-ext', yang_type='enumeration', is_config=True)
    self.__isns_device_ipaddress = YANGDynClass(base=RestrictedClassType(base_type=unicode, restriction_dict={'pattern': u'(([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])\\.){3}([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])(%[\\p{N}\\p{L}]+)?'}), is_leaf=True, yang_name="isns-device-ipaddress", rest_name="isns-device-ipaddress", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=False, namespace='urn:brocade.com:mgmt:brocade-isns-ext', defining_module='brocade-isns-ext', yang_type='inet:ipv4-address', is_config=True)
    self.__isns_device_iqn = YANGDynClass(base=RestrictedClassType(base_type=unicode, restriction_dict={'pattern': u'[-.:0-9a-zA-Z]{1,223}', 'length': [u'1..223']}), is_leaf=True, yang_name="isns-device-iqn", rest_name="isns-device-iqn", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=False, is_keyval=True, namespace='urn:brocade.com:mgmt:brocade-isns-ext', defining_module='brocade-isns-ext', yang_type='isns:isns-device-name-type', is_config=True)

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
      return [u'brocade_isns_ext_rpc', u'isns-get-device-brief', u'output', u'isns-entity-list', u'isns-device-list']

  def _rest_path(self):
    if hasattr(self, "_parent"):
      if self._rest_name:
        return self._parent._rest_path()+[self._rest_name]
      else:
        return self._parent._rest_path()
    else:
      return [u'isns-get-device-brief', u'output', u'isns-entity-list', u'isns-device-list']

  def _get_isns_device_ipaddress(self):
    """
    Getter method for isns_device_ipaddress, mapped from YANG variable /brocade_isns_ext_rpc/isns_get_device_brief/output/isns_entity_list/isns_device_list/isns_device_ipaddress (inet:ipv4-address)

    YANG Description: This leaf indicates the devices ip-address.
    """
    return self.__isns_device_ipaddress
      
  def _set_isns_device_ipaddress(self, v, load=False):
    """
    Setter method for isns_device_ipaddress, mapped from YANG variable /brocade_isns_ext_rpc/isns_get_device_brief/output/isns_entity_list/isns_device_list/isns_device_ipaddress (inet:ipv4-address)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_isns_device_ipaddress is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_isns_device_ipaddress() directly.

    YANG Description: This leaf indicates the devices ip-address.
    """
    if hasattr(v, "_utype"):
      v = v._utype(v)
    try:
      t = YANGDynClass(v,base=RestrictedClassType(base_type=unicode, restriction_dict={'pattern': u'(([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])\\.){3}([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])(%[\\p{N}\\p{L}]+)?'}), is_leaf=True, yang_name="isns-device-ipaddress", rest_name="isns-device-ipaddress", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=False, namespace='urn:brocade.com:mgmt:brocade-isns-ext', defining_module='brocade-isns-ext', yang_type='inet:ipv4-address', is_config=True)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """isns_device_ipaddress must be of a type compatible with inet:ipv4-address""",
          'defined-type': "inet:ipv4-address",
          'generated-type': """YANGDynClass(base=RestrictedClassType(base_type=unicode, restriction_dict={'pattern': u'(([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])\\.){3}([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])(%[\\p{N}\\p{L}]+)?'}), is_leaf=True, yang_name="isns-device-ipaddress", rest_name="isns-device-ipaddress", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=False, namespace='urn:brocade.com:mgmt:brocade-isns-ext', defining_module='brocade-isns-ext', yang_type='inet:ipv4-address', is_config=True)""",
        })

    self.__isns_device_ipaddress = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_isns_device_ipaddress(self):
    self.__isns_device_ipaddress = YANGDynClass(base=RestrictedClassType(base_type=unicode, restriction_dict={'pattern': u'(([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])\\.){3}([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])(%[\\p{N}\\p{L}]+)?'}), is_leaf=True, yang_name="isns-device-ipaddress", rest_name="isns-device-ipaddress", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=False, namespace='urn:brocade.com:mgmt:brocade-isns-ext', defining_module='brocade-isns-ext', yang_type='inet:ipv4-address', is_config=True)


  def _get_isns_device_iqn(self):
    """
    Getter method for isns_device_iqn, mapped from YANG variable /brocade_isns_ext_rpc/isns_get_device_brief/output/isns_entity_list/isns_device_list/isns_device_iqn (isns:isns-device-name-type)

    YANG Description: This leaf indicates the isns device name.
    """
    return self.__isns_device_iqn
      
  def _set_isns_device_iqn(self, v, load=False):
    """
    Setter method for isns_device_iqn, mapped from YANG variable /brocade_isns_ext_rpc/isns_get_device_brief/output/isns_entity_list/isns_device_list/isns_device_iqn (isns:isns-device-name-type)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_isns_device_iqn is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_isns_device_iqn() directly.

    YANG Description: This leaf indicates the isns device name.
    """
    parent = getattr(self, "_parent", None)
    if parent is not None and load is False:
      raise AttributeError("Cannot set keys directly when" +
                             " within an instantiated list")

    if hasattr(v, "_utype"):
      v = v._utype(v)
    try:
      t = YANGDynClass(v,base=RestrictedClassType(base_type=unicode, restriction_dict={'pattern': u'[-.:0-9a-zA-Z]{1,223}', 'length': [u'1..223']}), is_leaf=True, yang_name="isns-device-iqn", rest_name="isns-device-iqn", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=False, is_keyval=True, namespace='urn:brocade.com:mgmt:brocade-isns-ext', defining_module='brocade-isns-ext', yang_type='isns:isns-device-name-type', is_config=True)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """isns_device_iqn must be of a type compatible with isns:isns-device-name-type""",
          'defined-type': "isns:isns-device-name-type",
          'generated-type': """YANGDynClass(base=RestrictedClassType(base_type=unicode, restriction_dict={'pattern': u'[-.:0-9a-zA-Z]{1,223}', 'length': [u'1..223']}), is_leaf=True, yang_name="isns-device-iqn", rest_name="isns-device-iqn", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=False, is_keyval=True, namespace='urn:brocade.com:mgmt:brocade-isns-ext', defining_module='brocade-isns-ext', yang_type='isns:isns-device-name-type', is_config=True)""",
        })

    self.__isns_device_iqn = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_isns_device_iqn(self):
    self.__isns_device_iqn = YANGDynClass(base=RestrictedClassType(base_type=unicode, restriction_dict={'pattern': u'[-.:0-9a-zA-Z]{1,223}', 'length': [u'1..223']}), is_leaf=True, yang_name="isns-device-iqn", rest_name="isns-device-iqn", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=False, is_keyval=True, namespace='urn:brocade.com:mgmt:brocade-isns-ext', defining_module='brocade-isns-ext', yang_type='isns:isns-device-name-type', is_config=True)


  def _get_isns_device_type(self):
    """
    Getter method for isns_device_type, mapped from YANG variable /brocade_isns_ext_rpc/isns_get_device_brief/output/isns_entity_list/isns_device_list/isns_device_type (enumeration)

    YANG Description: This leaf indicates the type of device
connected to the FCF.
    """
    return self.__isns_device_type
      
  def _set_isns_device_type(self, v, load=False):
    """
    Setter method for isns_device_type, mapped from YANG variable /brocade_isns_ext_rpc/isns_get_device_brief/output/isns_entity_list/isns_device_list/isns_device_type (enumeration)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_isns_device_type is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_isns_device_type() directly.

    YANG Description: This leaf indicates the type of device
connected to the FCF.
    """
    if hasattr(v, "_utype"):
      v = v._utype(v)
    try:
      t = YANGDynClass(v,base=RestrictedClassType(base_type=unicode,                                     restriction_type="dict_key",                                     restriction_arg={u'device-control': {'value': 4}, u'device-target': {'value': 1}, u'device-initiator': {'value': 2}},), is_leaf=True, yang_name="isns-device-type", rest_name="isns-device-type", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=False, namespace='urn:brocade.com:mgmt:brocade-isns-ext', defining_module='brocade-isns-ext', yang_type='enumeration', is_config=True)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """isns_device_type must be of a type compatible with enumeration""",
          'defined-type': "brocade-isns-ext:enumeration",
          'generated-type': """YANGDynClass(base=RestrictedClassType(base_type=unicode,                                     restriction_type="dict_key",                                     restriction_arg={u'device-control': {'value': 4}, u'device-target': {'value': 1}, u'device-initiator': {'value': 2}},), is_leaf=True, yang_name="isns-device-type", rest_name="isns-device-type", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=False, namespace='urn:brocade.com:mgmt:brocade-isns-ext', defining_module='brocade-isns-ext', yang_type='enumeration', is_config=True)""",
        })

    self.__isns_device_type = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_isns_device_type(self):
    self.__isns_device_type = YANGDynClass(base=RestrictedClassType(base_type=unicode,                                     restriction_type="dict_key",                                     restriction_arg={u'device-control': {'value': 4}, u'device-target': {'value': 1}, u'device-initiator': {'value': 2}},), is_leaf=True, yang_name="isns-device-type", rest_name="isns-device-type", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=False, namespace='urn:brocade.com:mgmt:brocade-isns-ext', defining_module='brocade-isns-ext', yang_type='enumeration', is_config=True)

  isns_device_ipaddress = __builtin__.property(_get_isns_device_ipaddress, _set_isns_device_ipaddress)
  isns_device_iqn = __builtin__.property(_get_isns_device_iqn, _set_isns_device_iqn)
  isns_device_type = __builtin__.property(_get_isns_device_type, _set_isns_device_type)


  _pyangbind_elements = {'isns_device_ipaddress': isns_device_ipaddress, 'isns_device_iqn': isns_device_iqn, 'isns_device_type': isns_device_type, }

