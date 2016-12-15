
from operator import attrgetter
import pyangbind.lib.xpathhelper as xpathhelper
from pyangbind.lib.yangtypes import RestrictedPrecisionDecimalType, RestrictedClassType, TypedListType
from pyangbind.lib.yangtypes import YANGBool, YANGListType, YANGDynClass, ReferenceType
from pyangbind.lib.base import PybindBase
from decimal import Decimal
from bitarray import bitarray
import __builtin__
import oper_address
class chassis(PybindBase):
  """
  This class was auto-generated by the PythonClass plugin for PYANG
  from YANG module brocade-chassis - based on the path /hide-virtual-ip-holder/chassis. Each member element of
  the container is represented as a class variable - with a specific
  YANG type.
  """
  __slots__ = ('_pybind_generated_by', '_path_helper', '_yang_name', '_rest_name', '_extmethods', '__virtual_ip','__virtual_ipv6','__oper_address',)

  _yang_name = 'chassis'
  _rest_name = 'chassis'

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
    self.__oper_address = YANGDynClass(base=oper_address.oper_address, is_container='container', yang_name="oper-address", rest_name="virtual-ip", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'alt-name': u'virtual-ip'}}, namespace='urn:brocade.com:mgmt:brocade-chassis', defining_module='brocade-chassis', yang_type='container', is_config=True)
    self.__virtual_ipv6 = YANGDynClass(base=RestrictedClassType(base_type=unicode, restriction_dict={'pattern': u'((:|[0-9a-fA-F]{0,4}):)([0-9a-fA-F]{0,4}:){0,5}((([0-9a-fA-F]{0,4}:)?(:|[0-9a-fA-F]{0,4}))|(((25[0-5]|2[0-4][0-9]|[01]?[0-9]?[0-9])\\.){3}(25[0-5]|2[0-4][0-9]|[01]?[0-9]?[0-9])))(/(([0-9])|([0-9]{2})|(1[0-1][0-9])|(12[0-8])))'}), is_leaf=True, yang_name="virtual-ipv6", rest_name="virtual-ipv6", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'info': u'Chassis Virtual IPv6 address'}}, namespace='urn:brocade.com:mgmt:brocade-chassis', defining_module='brocade-chassis', yang_type='common-def:ipv6-address-prefix', is_config=True)
    self.__virtual_ip = YANGDynClass(base=RestrictedClassType(base_type=unicode, restriction_dict={'pattern': u'(([1-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])\\.)(([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])\\.){2}([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])/(([1-9])|([1-2][0-9])|(3[0-1]))'}), is_leaf=True, yang_name="virtual-ip", rest_name="virtual-ip", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'info': u'Chassis Virtual IPv4 address'}}, namespace='urn:brocade.com:mgmt:brocade-chassis', defining_module='brocade-chassis', yang_type='common-def:ipv4-prefix-mask', is_config=True)

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
      return [u'hide-virtual-ip-holder', u'chassis']

  def _rest_path(self):
    if hasattr(self, "_parent"):
      if self._rest_name:
        return self._parent._rest_path()+[self._rest_name]
      else:
        return self._parent._rest_path()
    else:
      return [u'chassis']

  def _get_virtual_ip(self):
    """
    Getter method for virtual_ip, mapped from YANG variable /hide_virtual_ip_holder/chassis/virtual_ip (common-def:ipv4-prefix-mask)
    """
    return self.__virtual_ip
      
  def _set_virtual_ip(self, v, load=False):
    """
    Setter method for virtual_ip, mapped from YANG variable /hide_virtual_ip_holder/chassis/virtual_ip (common-def:ipv4-prefix-mask)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_virtual_ip is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_virtual_ip() directly.
    """
    if hasattr(v, "_utype"):
      v = v._utype(v)
    try:
      t = YANGDynClass(v,base=RestrictedClassType(base_type=unicode, restriction_dict={'pattern': u'(([1-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])\\.)(([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])\\.){2}([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])/(([1-9])|([1-2][0-9])|(3[0-1]))'}), is_leaf=True, yang_name="virtual-ip", rest_name="virtual-ip", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'info': u'Chassis Virtual IPv4 address'}}, namespace='urn:brocade.com:mgmt:brocade-chassis', defining_module='brocade-chassis', yang_type='common-def:ipv4-prefix-mask', is_config=True)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """virtual_ip must be of a type compatible with common-def:ipv4-prefix-mask""",
          'defined-type': "common-def:ipv4-prefix-mask",
          'generated-type': """YANGDynClass(base=RestrictedClassType(base_type=unicode, restriction_dict={'pattern': u'(([1-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])\\.)(([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])\\.){2}([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])/(([1-9])|([1-2][0-9])|(3[0-1]))'}), is_leaf=True, yang_name="virtual-ip", rest_name="virtual-ip", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'info': u'Chassis Virtual IPv4 address'}}, namespace='urn:brocade.com:mgmt:brocade-chassis', defining_module='brocade-chassis', yang_type='common-def:ipv4-prefix-mask', is_config=True)""",
        })

    self.__virtual_ip = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_virtual_ip(self):
    self.__virtual_ip = YANGDynClass(base=RestrictedClassType(base_type=unicode, restriction_dict={'pattern': u'(([1-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])\\.)(([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])\\.){2}([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])/(([1-9])|([1-2][0-9])|(3[0-1]))'}), is_leaf=True, yang_name="virtual-ip", rest_name="virtual-ip", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'info': u'Chassis Virtual IPv4 address'}}, namespace='urn:brocade.com:mgmt:brocade-chassis', defining_module='brocade-chassis', yang_type='common-def:ipv4-prefix-mask', is_config=True)


  def _get_virtual_ipv6(self):
    """
    Getter method for virtual_ipv6, mapped from YANG variable /hide_virtual_ip_holder/chassis/virtual_ipv6 (common-def:ipv6-address-prefix)
    """
    return self.__virtual_ipv6
      
  def _set_virtual_ipv6(self, v, load=False):
    """
    Setter method for virtual_ipv6, mapped from YANG variable /hide_virtual_ip_holder/chassis/virtual_ipv6 (common-def:ipv6-address-prefix)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_virtual_ipv6 is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_virtual_ipv6() directly.
    """
    if hasattr(v, "_utype"):
      v = v._utype(v)
    try:
      t = YANGDynClass(v,base=RestrictedClassType(base_type=unicode, restriction_dict={'pattern': u'((:|[0-9a-fA-F]{0,4}):)([0-9a-fA-F]{0,4}:){0,5}((([0-9a-fA-F]{0,4}:)?(:|[0-9a-fA-F]{0,4}))|(((25[0-5]|2[0-4][0-9]|[01]?[0-9]?[0-9])\\.){3}(25[0-5]|2[0-4][0-9]|[01]?[0-9]?[0-9])))(/(([0-9])|([0-9]{2})|(1[0-1][0-9])|(12[0-8])))'}), is_leaf=True, yang_name="virtual-ipv6", rest_name="virtual-ipv6", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'info': u'Chassis Virtual IPv6 address'}}, namespace='urn:brocade.com:mgmt:brocade-chassis', defining_module='brocade-chassis', yang_type='common-def:ipv6-address-prefix', is_config=True)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """virtual_ipv6 must be of a type compatible with common-def:ipv6-address-prefix""",
          'defined-type': "common-def:ipv6-address-prefix",
          'generated-type': """YANGDynClass(base=RestrictedClassType(base_type=unicode, restriction_dict={'pattern': u'((:|[0-9a-fA-F]{0,4}):)([0-9a-fA-F]{0,4}:){0,5}((([0-9a-fA-F]{0,4}:)?(:|[0-9a-fA-F]{0,4}))|(((25[0-5]|2[0-4][0-9]|[01]?[0-9]?[0-9])\\.){3}(25[0-5]|2[0-4][0-9]|[01]?[0-9]?[0-9])))(/(([0-9])|([0-9]{2})|(1[0-1][0-9])|(12[0-8])))'}), is_leaf=True, yang_name="virtual-ipv6", rest_name="virtual-ipv6", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'info': u'Chassis Virtual IPv6 address'}}, namespace='urn:brocade.com:mgmt:brocade-chassis', defining_module='brocade-chassis', yang_type='common-def:ipv6-address-prefix', is_config=True)""",
        })

    self.__virtual_ipv6 = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_virtual_ipv6(self):
    self.__virtual_ipv6 = YANGDynClass(base=RestrictedClassType(base_type=unicode, restriction_dict={'pattern': u'((:|[0-9a-fA-F]{0,4}):)([0-9a-fA-F]{0,4}:){0,5}((([0-9a-fA-F]{0,4}:)?(:|[0-9a-fA-F]{0,4}))|(((25[0-5]|2[0-4][0-9]|[01]?[0-9]?[0-9])\\.){3}(25[0-5]|2[0-4][0-9]|[01]?[0-9]?[0-9])))(/(([0-9])|([0-9]{2})|(1[0-1][0-9])|(12[0-8])))'}), is_leaf=True, yang_name="virtual-ipv6", rest_name="virtual-ipv6", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'info': u'Chassis Virtual IPv6 address'}}, namespace='urn:brocade.com:mgmt:brocade-chassis', defining_module='brocade-chassis', yang_type='common-def:ipv6-address-prefix', is_config=True)


  def _get_oper_address(self):
    """
    Getter method for oper_address, mapped from YANG variable /hide_virtual_ip_holder/chassis/oper_address (container)
    """
    return self.__oper_address
      
  def _set_oper_address(self, v, load=False):
    """
    Setter method for oper_address, mapped from YANG variable /hide_virtual_ip_holder/chassis/oper_address (container)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_oper_address is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_oper_address() directly.
    """
    if hasattr(v, "_utype"):
      v = v._utype(v)
    try:
      t = YANGDynClass(v,base=oper_address.oper_address, is_container='container', yang_name="oper-address", rest_name="virtual-ip", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'alt-name': u'virtual-ip'}}, namespace='urn:brocade.com:mgmt:brocade-chassis', defining_module='brocade-chassis', yang_type='container', is_config=True)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """oper_address must be of a type compatible with container""",
          'defined-type': "container",
          'generated-type': """YANGDynClass(base=oper_address.oper_address, is_container='container', yang_name="oper-address", rest_name="virtual-ip", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'alt-name': u'virtual-ip'}}, namespace='urn:brocade.com:mgmt:brocade-chassis', defining_module='brocade-chassis', yang_type='container', is_config=True)""",
        })

    self.__oper_address = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_oper_address(self):
    self.__oper_address = YANGDynClass(base=oper_address.oper_address, is_container='container', yang_name="oper-address", rest_name="virtual-ip", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'alt-name': u'virtual-ip'}}, namespace='urn:brocade.com:mgmt:brocade-chassis', defining_module='brocade-chassis', yang_type='container', is_config=True)

  virtual_ip = __builtin__.property(_get_virtual_ip, _set_virtual_ip)
  virtual_ipv6 = __builtin__.property(_get_virtual_ipv6, _set_virtual_ipv6)
  oper_address = __builtin__.property(_get_oper_address, _set_oper_address)


  _pyangbind_elements = {'virtual_ip': virtual_ip, 'virtual_ipv6': virtual_ipv6, 'oper_address': oper_address, }


