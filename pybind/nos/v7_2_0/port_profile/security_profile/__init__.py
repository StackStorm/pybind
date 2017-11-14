
from operator import attrgetter
import pyangbind.lib.xpathhelper as xpathhelper
from pyangbind.lib.yangtypes import RestrictedPrecisionDecimalType, RestrictedClassType, TypedListType
from pyangbind.lib.yangtypes import YANGBool, YANGListType, YANGDynClass, ReferenceType
from pyangbind.lib.base import PybindBase
from decimal import Decimal
from bitarray import bitarray
import __builtin__
import mac
import ip
import ipv6
class security_profile(PybindBase):
  """
  This class was auto-generated by the PythonClass plugin for PYANG
  from YANG module brocade-port-profile - based on the path /port-profile/security-profile. Each member element of
  the container is represented as a class variable - with a specific
  YANG type.

  YANG Description: The Security profile.
  """
  __slots__ = ('_pybind_generated_by', '_path_helper', '_yang_name', '_rest_name', '_extmethods', '__mac','__ip','__ipv6',)

  _yang_name = 'security-profile'
  _rest_name = 'security-profile'

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
    self.__ip = YANGDynClass(base=ip.ip, is_container='container', presence=False, yang_name="ip", rest_name="ip", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'info': u'Configure IP parameters', u'cli-incomplete-no': None}}, namespace='urn:brocade.com:mgmt:brocade-port-profile', defining_module='brocade-port-profile', yang_type='container', is_config=True)
    self.__mac = YANGDynClass(base=mac.mac, is_container='container', presence=False, yang_name="mac", rest_name="mac", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'info': u'Configure MAC parameters', u'cli-incomplete-no': None}}, namespace='urn:brocade.com:mgmt:brocade-port-profile', defining_module='brocade-port-profile', yang_type='container', is_config=True)
    self.__ipv6 = YANGDynClass(base=ipv6.ipv6, is_container='container', presence=False, yang_name="ipv6", rest_name="ipv6", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'info': u'Configure IP parameters', u'cli-incomplete-no': None}}, namespace='urn:brocade.com:mgmt:brocade-port-profile', defining_module='brocade-port-profile', yang_type='container', is_config=True)

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
      return [u'port-profile', u'security-profile']

  def _rest_path(self):
    if hasattr(self, "_parent"):
      if self._rest_name:
        return self._parent._rest_path()+[self._rest_name]
      else:
        return self._parent._rest_path()
    else:
      return [u'port-profile', u'security-profile']

  def _get_mac(self):
    """
    Getter method for mac, mapped from YANG variable /port_profile/security_profile/mac (container)

    YANG Description: This provides the grouping for MAC configuration
elements.
    """
    return self.__mac
      
  def _set_mac(self, v, load=False):
    """
    Setter method for mac, mapped from YANG variable /port_profile/security_profile/mac (container)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_mac is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_mac() directly.

    YANG Description: This provides the grouping for MAC configuration
elements.
    """
    if hasattr(v, "_utype"):
      v = v._utype(v)
    try:
      t = YANGDynClass(v,base=mac.mac, is_container='container', presence=False, yang_name="mac", rest_name="mac", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'info': u'Configure MAC parameters', u'cli-incomplete-no': None}}, namespace='urn:brocade.com:mgmt:brocade-port-profile', defining_module='brocade-port-profile', yang_type='container', is_config=True)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """mac must be of a type compatible with container""",
          'defined-type': "container",
          'generated-type': """YANGDynClass(base=mac.mac, is_container='container', presence=False, yang_name="mac", rest_name="mac", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'info': u'Configure MAC parameters', u'cli-incomplete-no': None}}, namespace='urn:brocade.com:mgmt:brocade-port-profile', defining_module='brocade-port-profile', yang_type='container', is_config=True)""",
        })

    self.__mac = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_mac(self):
    self.__mac = YANGDynClass(base=mac.mac, is_container='container', presence=False, yang_name="mac", rest_name="mac", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'info': u'Configure MAC parameters', u'cli-incomplete-no': None}}, namespace='urn:brocade.com:mgmt:brocade-port-profile', defining_module='brocade-port-profile', yang_type='container', is_config=True)


  def _get_ip(self):
    """
    Getter method for ip, mapped from YANG variable /port_profile/security_profile/ip (container)

    YANG Description: This provides the grouping for IP configuration
elements.
    """
    return self.__ip
      
  def _set_ip(self, v, load=False):
    """
    Setter method for ip, mapped from YANG variable /port_profile/security_profile/ip (container)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_ip is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_ip() directly.

    YANG Description: This provides the grouping for IP configuration
elements.
    """
    if hasattr(v, "_utype"):
      v = v._utype(v)
    try:
      t = YANGDynClass(v,base=ip.ip, is_container='container', presence=False, yang_name="ip", rest_name="ip", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'info': u'Configure IP parameters', u'cli-incomplete-no': None}}, namespace='urn:brocade.com:mgmt:brocade-port-profile', defining_module='brocade-port-profile', yang_type='container', is_config=True)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """ip must be of a type compatible with container""",
          'defined-type': "container",
          'generated-type': """YANGDynClass(base=ip.ip, is_container='container', presence=False, yang_name="ip", rest_name="ip", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'info': u'Configure IP parameters', u'cli-incomplete-no': None}}, namespace='urn:brocade.com:mgmt:brocade-port-profile', defining_module='brocade-port-profile', yang_type='container', is_config=True)""",
        })

    self.__ip = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_ip(self):
    self.__ip = YANGDynClass(base=ip.ip, is_container='container', presence=False, yang_name="ip", rest_name="ip", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'info': u'Configure IP parameters', u'cli-incomplete-no': None}}, namespace='urn:brocade.com:mgmt:brocade-port-profile', defining_module='brocade-port-profile', yang_type='container', is_config=True)


  def _get_ipv6(self):
    """
    Getter method for ipv6, mapped from YANG variable /port_profile/security_profile/ipv6 (container)

    YANG Description: This provides the grouping for ipV6 configuration
elements.
    """
    return self.__ipv6
      
  def _set_ipv6(self, v, load=False):
    """
    Setter method for ipv6, mapped from YANG variable /port_profile/security_profile/ipv6 (container)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_ipv6 is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_ipv6() directly.

    YANG Description: This provides the grouping for ipV6 configuration
elements.
    """
    if hasattr(v, "_utype"):
      v = v._utype(v)
    try:
      t = YANGDynClass(v,base=ipv6.ipv6, is_container='container', presence=False, yang_name="ipv6", rest_name="ipv6", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'info': u'Configure IP parameters', u'cli-incomplete-no': None}}, namespace='urn:brocade.com:mgmt:brocade-port-profile', defining_module='brocade-port-profile', yang_type='container', is_config=True)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """ipv6 must be of a type compatible with container""",
          'defined-type': "container",
          'generated-type': """YANGDynClass(base=ipv6.ipv6, is_container='container', presence=False, yang_name="ipv6", rest_name="ipv6", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'info': u'Configure IP parameters', u'cli-incomplete-no': None}}, namespace='urn:brocade.com:mgmt:brocade-port-profile', defining_module='brocade-port-profile', yang_type='container', is_config=True)""",
        })

    self.__ipv6 = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_ipv6(self):
    self.__ipv6 = YANGDynClass(base=ipv6.ipv6, is_container='container', presence=False, yang_name="ipv6", rest_name="ipv6", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'info': u'Configure IP parameters', u'cli-incomplete-no': None}}, namespace='urn:brocade.com:mgmt:brocade-port-profile', defining_module='brocade-port-profile', yang_type='container', is_config=True)

  mac = __builtin__.property(_get_mac, _set_mac)
  ip = __builtin__.property(_get_ip, _set_ip)
  ipv6 = __builtin__.property(_get_ipv6, _set_ipv6)


  _pyangbind_elements = {'mac': mac, 'ip': ip, 'ipv6': ipv6, }


