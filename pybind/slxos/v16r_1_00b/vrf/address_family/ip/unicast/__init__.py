
from operator import attrgetter
import pyangbind.lib.xpathhelper as xpathhelper
from pyangbind.lib.yangtypes import RestrictedPrecisionDecimalType, RestrictedClassType, TypedListType
from pyangbind.lib.yangtypes import YANGBool, YANGListType, YANGDynClass, ReferenceType
from pyangbind.lib.base import PybindBase
from decimal import Decimal
from bitarray import bitarray
import __builtin__
import arp_entry
import ip
class unicast(PybindBase):
  """
  This class was auto-generated by the PythonClass plugin for PYANG
  from YANG module brocade-vrf - based on the path /vrf/address-family/ip/unicast. Each member element of
  the container is represented as a class variable - with a specific
  YANG type.
  """
  __slots__ = ('_pybind_generated_by', '_path_helper', '_yang_name', '_rest_name', '_extmethods', '__max_route','__arp_entry','__ip',)

  _yang_name = 'unicast'
  _rest_name = 'unicast'

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
    self.__ip = YANGDynClass(base=ip.ip, is_container='container', presence=False, yang_name="ip", rest_name="ip", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'info': u'The Internet Protocol (IP).', u'cli-incomplete-command': None}}, namespace='urn:brocade.com:mgmt:brocade-rtm', defining_module='brocade-rtm', yang_type='container', is_config=True)
    self.__max_route = YANGDynClass(base=RestrictedClassType(base_type=RestrictedClassType(base_type=long, restriction_dict={'range': ['0..4294967295']}, int_size=32), restriction_dict={'range': [u'1..4294967295']}), is_leaf=True, yang_name="max-route", rest_name="max-route", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'info': u'Maximum number of routes allowed in this routing table'}}, namespace='urn:brocade.com:mgmt:brocade-vrf', defining_module='brocade-vrf', yang_type='uint32', is_config=True)
    self.__arp_entry = YANGDynClass(base=YANGListType("arp_ip_address",arp_entry.arp_entry, yang_name="arp-entry", rest_name="arp", parent=self, is_container='list', user_ordered=False, path_helper=self._path_helper, yang_keys='arp-ip-address', extensions={u'tailf-common': {u'info': u'Address Resolution Protocol (ARP)', u'cli-no-key-completion': None, u'cli-suppress-mode': None, u'cli-suppress-list-no': None, u'alt-name': u'arp', u'cli-compact-syntax': None, u'cli-sequence-commands': None, u'cli-incomplete-command': None, u'callpoint': u'ArpStaticConfigCallpoint'}}), is_container='list', yang_name="arp-entry", rest_name="arp", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'info': u'Address Resolution Protocol (ARP)', u'cli-no-key-completion': None, u'cli-suppress-mode': None, u'cli-suppress-list-no': None, u'alt-name': u'arp', u'cli-compact-syntax': None, u'cli-sequence-commands': None, u'cli-incomplete-command': None, u'callpoint': u'ArpStaticConfigCallpoint'}}, namespace='urn:brocade.com:mgmt:brocade-arp', defining_module='brocade-arp', yang_type='list', is_config=True)

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
      return [u'vrf', u'address-family', u'ip', u'unicast']

  def _rest_path(self):
    if hasattr(self, "_parent"):
      if self._rest_name:
        return self._parent._rest_path()+[self._rest_name]
      else:
        return self._parent._rest_path()
    else:
      return [u'vrf', u'address-family', u'ipv4', u'unicast']

  def _get_max_route(self):
    """
    Getter method for max_route, mapped from YANG variable /vrf/address_family/ip/unicast/max_route (uint32)

    YANG Description: Maximum number of routes allowed in this routing table
    """
    return self.__max_route
      
  def _set_max_route(self, v, load=False):
    """
    Setter method for max_route, mapped from YANG variable /vrf/address_family/ip/unicast/max_route (uint32)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_max_route is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_max_route() directly.

    YANG Description: Maximum number of routes allowed in this routing table
    """
    if hasattr(v, "_utype"):
      v = v._utype(v)
    try:
      t = YANGDynClass(v,base=RestrictedClassType(base_type=RestrictedClassType(base_type=long, restriction_dict={'range': ['0..4294967295']}, int_size=32), restriction_dict={'range': [u'1..4294967295']}), is_leaf=True, yang_name="max-route", rest_name="max-route", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'info': u'Maximum number of routes allowed in this routing table'}}, namespace='urn:brocade.com:mgmt:brocade-vrf', defining_module='brocade-vrf', yang_type='uint32', is_config=True)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """max_route must be of a type compatible with uint32""",
          'defined-type': "uint32",
          'generated-type': """YANGDynClass(base=RestrictedClassType(base_type=RestrictedClassType(base_type=long, restriction_dict={'range': ['0..4294967295']}, int_size=32), restriction_dict={'range': [u'1..4294967295']}), is_leaf=True, yang_name="max-route", rest_name="max-route", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'info': u'Maximum number of routes allowed in this routing table'}}, namespace='urn:brocade.com:mgmt:brocade-vrf', defining_module='brocade-vrf', yang_type='uint32', is_config=True)""",
        })

    self.__max_route = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_max_route(self):
    self.__max_route = YANGDynClass(base=RestrictedClassType(base_type=RestrictedClassType(base_type=long, restriction_dict={'range': ['0..4294967295']}, int_size=32), restriction_dict={'range': [u'1..4294967295']}), is_leaf=True, yang_name="max-route", rest_name="max-route", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'info': u'Maximum number of routes allowed in this routing table'}}, namespace='urn:brocade.com:mgmt:brocade-vrf', defining_module='brocade-vrf', yang_type='uint32', is_config=True)


  def _get_arp_entry(self):
    """
    Getter method for arp_entry, mapped from YANG variable /vrf/address_family/ip/unicast/arp_entry (list)
    """
    return self.__arp_entry
      
  def _set_arp_entry(self, v, load=False):
    """
    Setter method for arp_entry, mapped from YANG variable /vrf/address_family/ip/unicast/arp_entry (list)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_arp_entry is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_arp_entry() directly.
    """
    if hasattr(v, "_utype"):
      v = v._utype(v)
    try:
      t = YANGDynClass(v,base=YANGListType("arp_ip_address",arp_entry.arp_entry, yang_name="arp-entry", rest_name="arp", parent=self, is_container='list', user_ordered=False, path_helper=self._path_helper, yang_keys='arp-ip-address', extensions={u'tailf-common': {u'info': u'Address Resolution Protocol (ARP)', u'cli-no-key-completion': None, u'cli-suppress-mode': None, u'cli-suppress-list-no': None, u'alt-name': u'arp', u'cli-compact-syntax': None, u'cli-sequence-commands': None, u'cli-incomplete-command': None, u'callpoint': u'ArpStaticConfigCallpoint'}}), is_container='list', yang_name="arp-entry", rest_name="arp", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'info': u'Address Resolution Protocol (ARP)', u'cli-no-key-completion': None, u'cli-suppress-mode': None, u'cli-suppress-list-no': None, u'alt-name': u'arp', u'cli-compact-syntax': None, u'cli-sequence-commands': None, u'cli-incomplete-command': None, u'callpoint': u'ArpStaticConfigCallpoint'}}, namespace='urn:brocade.com:mgmt:brocade-arp', defining_module='brocade-arp', yang_type='list', is_config=True)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """arp_entry must be of a type compatible with list""",
          'defined-type': "list",
          'generated-type': """YANGDynClass(base=YANGListType("arp_ip_address",arp_entry.arp_entry, yang_name="arp-entry", rest_name="arp", parent=self, is_container='list', user_ordered=False, path_helper=self._path_helper, yang_keys='arp-ip-address', extensions={u'tailf-common': {u'info': u'Address Resolution Protocol (ARP)', u'cli-no-key-completion': None, u'cli-suppress-mode': None, u'cli-suppress-list-no': None, u'alt-name': u'arp', u'cli-compact-syntax': None, u'cli-sequence-commands': None, u'cli-incomplete-command': None, u'callpoint': u'ArpStaticConfigCallpoint'}}), is_container='list', yang_name="arp-entry", rest_name="arp", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'info': u'Address Resolution Protocol (ARP)', u'cli-no-key-completion': None, u'cli-suppress-mode': None, u'cli-suppress-list-no': None, u'alt-name': u'arp', u'cli-compact-syntax': None, u'cli-sequence-commands': None, u'cli-incomplete-command': None, u'callpoint': u'ArpStaticConfigCallpoint'}}, namespace='urn:brocade.com:mgmt:brocade-arp', defining_module='brocade-arp', yang_type='list', is_config=True)""",
        })

    self.__arp_entry = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_arp_entry(self):
    self.__arp_entry = YANGDynClass(base=YANGListType("arp_ip_address",arp_entry.arp_entry, yang_name="arp-entry", rest_name="arp", parent=self, is_container='list', user_ordered=False, path_helper=self._path_helper, yang_keys='arp-ip-address', extensions={u'tailf-common': {u'info': u'Address Resolution Protocol (ARP)', u'cli-no-key-completion': None, u'cli-suppress-mode': None, u'cli-suppress-list-no': None, u'alt-name': u'arp', u'cli-compact-syntax': None, u'cli-sequence-commands': None, u'cli-incomplete-command': None, u'callpoint': u'ArpStaticConfigCallpoint'}}), is_container='list', yang_name="arp-entry", rest_name="arp", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'info': u'Address Resolution Protocol (ARP)', u'cli-no-key-completion': None, u'cli-suppress-mode': None, u'cli-suppress-list-no': None, u'alt-name': u'arp', u'cli-compact-syntax': None, u'cli-sequence-commands': None, u'cli-incomplete-command': None, u'callpoint': u'ArpStaticConfigCallpoint'}}, namespace='urn:brocade.com:mgmt:brocade-arp', defining_module='brocade-arp', yang_type='list', is_config=True)


  def _get_ip(self):
    """
    Getter method for ip, mapped from YANG variable /vrf/address_family/ip/unicast/ip (container)

    YANG Description: rtm commands
    """
    return self.__ip
      
  def _set_ip(self, v, load=False):
    """
    Setter method for ip, mapped from YANG variable /vrf/address_family/ip/unicast/ip (container)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_ip is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_ip() directly.

    YANG Description: rtm commands
    """
    if hasattr(v, "_utype"):
      v = v._utype(v)
    try:
      t = YANGDynClass(v,base=ip.ip, is_container='container', presence=False, yang_name="ip", rest_name="ip", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'info': u'The Internet Protocol (IP).', u'cli-incomplete-command': None}}, namespace='urn:brocade.com:mgmt:brocade-rtm', defining_module='brocade-rtm', yang_type='container', is_config=True)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """ip must be of a type compatible with container""",
          'defined-type': "container",
          'generated-type': """YANGDynClass(base=ip.ip, is_container='container', presence=False, yang_name="ip", rest_name="ip", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'info': u'The Internet Protocol (IP).', u'cli-incomplete-command': None}}, namespace='urn:brocade.com:mgmt:brocade-rtm', defining_module='brocade-rtm', yang_type='container', is_config=True)""",
        })

    self.__ip = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_ip(self):
    self.__ip = YANGDynClass(base=ip.ip, is_container='container', presence=False, yang_name="ip", rest_name="ip", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'info': u'The Internet Protocol (IP).', u'cli-incomplete-command': None}}, namespace='urn:brocade.com:mgmt:brocade-rtm', defining_module='brocade-rtm', yang_type='container', is_config=True)

  max_route = __builtin__.property(_get_max_route, _set_max_route)
  arp_entry = __builtin__.property(_get_arp_entry, _set_arp_entry)
  ip = __builtin__.property(_get_ip, _set_ip)


  _pyangbind_elements = {'max_route': max_route, 'arp_entry': arp_entry, 'ip': ip, }


