
from operator import attrgetter
import pyangbind.lib.xpathhelper as xpathhelper
from pyangbind.lib.yangtypes import RestrictedPrecisionDecimalType, RestrictedClassType, TypedListType
from pyangbind.lib.yangtypes import YANGBool, YANGListType, YANGDynClass, ReferenceType
from pyangbind.lib.base import PybindBase
from decimal import Decimal
from bitarray import bitarray
import __builtin__
class icmp(PybindBase):
  """
  This class was auto-generated by the PythonClass plugin for PYANG
  from YANG module brocade-interface - based on the path /interface/fortygigabitethernet/ip/icmp. Each member element of
  the container is represented as a class variable - with a specific
  YANG type.
  """
  __slots__ = ('_pybind_generated_by', '_path_helper', '_yang_name', '_rest_name', '_extmethods', '__echo_reply','__rate_limiting','__unreachable','__redirect','__address_mask',)

  _yang_name = 'icmp'
  _rest_name = 'icmp'

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
    self.__echo_reply = YANGDynClass(base=YANGBool, is_leaf=True, yang_name="echo-reply", rest_name="echo-reply", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'cli-full-command': None, u'cli-run-template': u'$(.?:no ip icmp echo-reply\n)', u'info': u'Enable echo-reply'}}, namespace='urn:brocade.com:mgmt:brocade-icmp', defining_module='brocade-icmp', yang_type='empty', is_config=True)
    self.__unreachable = YANGDynClass(base=YANGBool, is_leaf=True, yang_name="unreachable", rest_name="unreachable", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'cli-full-command': None, u'info': u'Enable destination unreachable messages'}}, namespace='urn:brocade.com:mgmt:brocade-icmp', defining_module='brocade-icmp', yang_type='empty', is_config=True)
    self.__redirect = YANGDynClass(base=YANGBool, is_leaf=True, yang_name="redirect", rest_name="redirect", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'cli-full-command': None, u'info': u'Enable redirect'}}, namespace='urn:brocade.com:mgmt:brocade-icmp', defining_module='brocade-icmp', yang_type='empty', is_config=True)
    self.__address_mask = YANGDynClass(base=YANGBool, is_leaf=True, yang_name="address-mask", rest_name="address-mask", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'cli-full-command': None, u'info': u'Enables ICMP address mask'}}, namespace='urn:brocade.com:mgmt:brocade-icmp', defining_module='brocade-icmp', yang_type='empty', is_config=True)
    self.__rate_limiting = YANGDynClass(base=RestrictedClassType(base_type=RestrictedClassType(base_type=long, restriction_dict={'range': ['0..4294967295']}, int_size=32), restriction_dict={'range': [u'0..4294967295']}), default=RestrictedClassType(base_type=long, restriction_dict={'range': ['0..4294967295']}, int_size=32)(1000), is_leaf=True, yang_name="rate-limiting", rest_name="rate-limiting", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'cli-full-command': None, u'info': u'Rate limit ICMP error messages'}}, namespace='urn:brocade.com:mgmt:brocade-icmp', defining_module='brocade-icmp', yang_type='uint32', is_config=True)

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
      return [u'interface', u'fortygigabitethernet', u'ip', u'icmp']

  def _rest_path(self):
    if hasattr(self, "_parent"):
      if self._rest_name:
        return self._parent._rest_path()+[self._rest_name]
      else:
        return self._parent._rest_path()
    else:
      return [u'interface', u'FortyGigabitEthernet', u'ip', u'icmp']

  def _get_echo_reply(self):
    """
    Getter method for echo_reply, mapped from YANG variable /interface/fortygigabitethernet/ip/icmp/echo_reply (empty)
    """
    return self.__echo_reply
      
  def _set_echo_reply(self, v, load=False):
    """
    Setter method for echo_reply, mapped from YANG variable /interface/fortygigabitethernet/ip/icmp/echo_reply (empty)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_echo_reply is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_echo_reply() directly.
    """
    if hasattr(v, "_utype"):
      v = v._utype(v)
    try:
      t = YANGDynClass(v,base=YANGBool, is_leaf=True, yang_name="echo-reply", rest_name="echo-reply", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'cli-full-command': None, u'cli-run-template': u'$(.?:no ip icmp echo-reply\n)', u'info': u'Enable echo-reply'}}, namespace='urn:brocade.com:mgmt:brocade-icmp', defining_module='brocade-icmp', yang_type='empty', is_config=True)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """echo_reply must be of a type compatible with empty""",
          'defined-type': "empty",
          'generated-type': """YANGDynClass(base=YANGBool, is_leaf=True, yang_name="echo-reply", rest_name="echo-reply", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'cli-full-command': None, u'cli-run-template': u'$(.?:no ip icmp echo-reply\n)', u'info': u'Enable echo-reply'}}, namespace='urn:brocade.com:mgmt:brocade-icmp', defining_module='brocade-icmp', yang_type='empty', is_config=True)""",
        })

    self.__echo_reply = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_echo_reply(self):
    self.__echo_reply = YANGDynClass(base=YANGBool, is_leaf=True, yang_name="echo-reply", rest_name="echo-reply", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'cli-full-command': None, u'cli-run-template': u'$(.?:no ip icmp echo-reply\n)', u'info': u'Enable echo-reply'}}, namespace='urn:brocade.com:mgmt:brocade-icmp', defining_module='brocade-icmp', yang_type='empty', is_config=True)


  def _get_rate_limiting(self):
    """
    Getter method for rate_limiting, mapped from YANG variable /interface/fortygigabitethernet/ip/icmp/rate_limiting (uint32)
    """
    return self.__rate_limiting
      
  def _set_rate_limiting(self, v, load=False):
    """
    Setter method for rate_limiting, mapped from YANG variable /interface/fortygigabitethernet/ip/icmp/rate_limiting (uint32)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_rate_limiting is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_rate_limiting() directly.
    """
    if hasattr(v, "_utype"):
      v = v._utype(v)
    try:
      t = YANGDynClass(v,base=RestrictedClassType(base_type=RestrictedClassType(base_type=long, restriction_dict={'range': ['0..4294967295']}, int_size=32), restriction_dict={'range': [u'0..4294967295']}), default=RestrictedClassType(base_type=long, restriction_dict={'range': ['0..4294967295']}, int_size=32)(1000), is_leaf=True, yang_name="rate-limiting", rest_name="rate-limiting", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'cli-full-command': None, u'info': u'Rate limit ICMP error messages'}}, namespace='urn:brocade.com:mgmt:brocade-icmp', defining_module='brocade-icmp', yang_type='uint32', is_config=True)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """rate_limiting must be of a type compatible with uint32""",
          'defined-type': "uint32",
          'generated-type': """YANGDynClass(base=RestrictedClassType(base_type=RestrictedClassType(base_type=long, restriction_dict={'range': ['0..4294967295']}, int_size=32), restriction_dict={'range': [u'0..4294967295']}), default=RestrictedClassType(base_type=long, restriction_dict={'range': ['0..4294967295']}, int_size=32)(1000), is_leaf=True, yang_name="rate-limiting", rest_name="rate-limiting", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'cli-full-command': None, u'info': u'Rate limit ICMP error messages'}}, namespace='urn:brocade.com:mgmt:brocade-icmp', defining_module='brocade-icmp', yang_type='uint32', is_config=True)""",
        })

    self.__rate_limiting = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_rate_limiting(self):
    self.__rate_limiting = YANGDynClass(base=RestrictedClassType(base_type=RestrictedClassType(base_type=long, restriction_dict={'range': ['0..4294967295']}, int_size=32), restriction_dict={'range': [u'0..4294967295']}), default=RestrictedClassType(base_type=long, restriction_dict={'range': ['0..4294967295']}, int_size=32)(1000), is_leaf=True, yang_name="rate-limiting", rest_name="rate-limiting", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'cli-full-command': None, u'info': u'Rate limit ICMP error messages'}}, namespace='urn:brocade.com:mgmt:brocade-icmp', defining_module='brocade-icmp', yang_type='uint32', is_config=True)


  def _get_unreachable(self):
    """
    Getter method for unreachable, mapped from YANG variable /interface/fortygigabitethernet/ip/icmp/unreachable (empty)
    """
    return self.__unreachable
      
  def _set_unreachable(self, v, load=False):
    """
    Setter method for unreachable, mapped from YANG variable /interface/fortygigabitethernet/ip/icmp/unreachable (empty)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_unreachable is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_unreachable() directly.
    """
    if hasattr(v, "_utype"):
      v = v._utype(v)
    try:
      t = YANGDynClass(v,base=YANGBool, is_leaf=True, yang_name="unreachable", rest_name="unreachable", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'cli-full-command': None, u'info': u'Enable destination unreachable messages'}}, namespace='urn:brocade.com:mgmt:brocade-icmp', defining_module='brocade-icmp', yang_type='empty', is_config=True)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """unreachable must be of a type compatible with empty""",
          'defined-type': "empty",
          'generated-type': """YANGDynClass(base=YANGBool, is_leaf=True, yang_name="unreachable", rest_name="unreachable", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'cli-full-command': None, u'info': u'Enable destination unreachable messages'}}, namespace='urn:brocade.com:mgmt:brocade-icmp', defining_module='brocade-icmp', yang_type='empty', is_config=True)""",
        })

    self.__unreachable = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_unreachable(self):
    self.__unreachable = YANGDynClass(base=YANGBool, is_leaf=True, yang_name="unreachable", rest_name="unreachable", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'cli-full-command': None, u'info': u'Enable destination unreachable messages'}}, namespace='urn:brocade.com:mgmt:brocade-icmp', defining_module='brocade-icmp', yang_type='empty', is_config=True)


  def _get_redirect(self):
    """
    Getter method for redirect, mapped from YANG variable /interface/fortygigabitethernet/ip/icmp/redirect (empty)
    """
    return self.__redirect
      
  def _set_redirect(self, v, load=False):
    """
    Setter method for redirect, mapped from YANG variable /interface/fortygigabitethernet/ip/icmp/redirect (empty)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_redirect is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_redirect() directly.
    """
    if hasattr(v, "_utype"):
      v = v._utype(v)
    try:
      t = YANGDynClass(v,base=YANGBool, is_leaf=True, yang_name="redirect", rest_name="redirect", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'cli-full-command': None, u'info': u'Enable redirect'}}, namespace='urn:brocade.com:mgmt:brocade-icmp', defining_module='brocade-icmp', yang_type='empty', is_config=True)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """redirect must be of a type compatible with empty""",
          'defined-type': "empty",
          'generated-type': """YANGDynClass(base=YANGBool, is_leaf=True, yang_name="redirect", rest_name="redirect", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'cli-full-command': None, u'info': u'Enable redirect'}}, namespace='urn:brocade.com:mgmt:brocade-icmp', defining_module='brocade-icmp', yang_type='empty', is_config=True)""",
        })

    self.__redirect = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_redirect(self):
    self.__redirect = YANGDynClass(base=YANGBool, is_leaf=True, yang_name="redirect", rest_name="redirect", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'cli-full-command': None, u'info': u'Enable redirect'}}, namespace='urn:brocade.com:mgmt:brocade-icmp', defining_module='brocade-icmp', yang_type='empty', is_config=True)


  def _get_address_mask(self):
    """
    Getter method for address_mask, mapped from YANG variable /interface/fortygigabitethernet/ip/icmp/address_mask (empty)
    """
    return self.__address_mask
      
  def _set_address_mask(self, v, load=False):
    """
    Setter method for address_mask, mapped from YANG variable /interface/fortygigabitethernet/ip/icmp/address_mask (empty)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_address_mask is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_address_mask() directly.
    """
    if hasattr(v, "_utype"):
      v = v._utype(v)
    try:
      t = YANGDynClass(v,base=YANGBool, is_leaf=True, yang_name="address-mask", rest_name="address-mask", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'cli-full-command': None, u'info': u'Enables ICMP address mask'}}, namespace='urn:brocade.com:mgmt:brocade-icmp', defining_module='brocade-icmp', yang_type='empty', is_config=True)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """address_mask must be of a type compatible with empty""",
          'defined-type': "empty",
          'generated-type': """YANGDynClass(base=YANGBool, is_leaf=True, yang_name="address-mask", rest_name="address-mask", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'cli-full-command': None, u'info': u'Enables ICMP address mask'}}, namespace='urn:brocade.com:mgmt:brocade-icmp', defining_module='brocade-icmp', yang_type='empty', is_config=True)""",
        })

    self.__address_mask = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_address_mask(self):
    self.__address_mask = YANGDynClass(base=YANGBool, is_leaf=True, yang_name="address-mask", rest_name="address-mask", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'cli-full-command': None, u'info': u'Enables ICMP address mask'}}, namespace='urn:brocade.com:mgmt:brocade-icmp', defining_module='brocade-icmp', yang_type='empty', is_config=True)

  echo_reply = __builtin__.property(_get_echo_reply, _set_echo_reply)
  rate_limiting = __builtin__.property(_get_rate_limiting, _set_rate_limiting)
  unreachable = __builtin__.property(_get_unreachable, _set_unreachable)
  redirect = __builtin__.property(_get_redirect, _set_redirect)
  address_mask = __builtin__.property(_get_address_mask, _set_address_mask)


  _pyangbind_elements = {'echo_reply': echo_reply, 'rate_limiting': rate_limiting, 'unreachable': unreachable, 'redirect': redirect, 'address_mask': address_mask, }


