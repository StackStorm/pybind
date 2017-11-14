
from operator import attrgetter
import pyangbind.lib.xpathhelper as xpathhelper
from pyangbind.lib.yangtypes import RestrictedPrecisionDecimalType, RestrictedClassType, TypedListType
from pyangbind.lib.yangtypes import YANGBool, YANGListType, YANGDynClass, ReferenceType
from pyangbind.lib.base import PybindBase
from decimal import Decimal
from bitarray import bitarray
import __builtin__
import ipv6route
import prefix_list
import ipv6_global_cmds
import route
import import_
import proto_vrrpv3
class ipv6(PybindBase):
  """
  This class was auto-generated by the PythonClass plugin for PYANG
  from YANG module brocade-common-def - based on the path /ipv6. Each member element of
  the container is represented as a class variable - with a specific
  YANG type.
  """
  __slots__ = ('_pybind_generated_by', '_path_helper', '_yang_name', '_rest_name', '_extmethods', '__ipv6route','__prefix_list','__ipv6_global_cmds','__route','__import_','__proto_vrrpv3',)

  _yang_name = 'ipv6'
  _rest_name = 'ipv6'

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
    self.__import_ = YANGDynClass(base=import_.import_, is_container='container', presence=False, yang_name="import", rest_name="import", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'info': u'Import IPV6 routes'}}, namespace='urn:brocade.com:mgmt:brocade-ipv6-rtm', defining_module='brocade-ipv6-rtm', yang_type='container', is_config=True)
    self.__route = YANGDynClass(base=route.route, is_container='container', presence=False, yang_name="route", rest_name="route", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'info': u'Configure IPv6 unicast static route', u'cli-incomplete-no': None}}, namespace='urn:brocade.com:mgmt:brocade-ipv6-rtm', defining_module='brocade-ipv6-rtm', yang_type='container', is_config=True)
    self.__ipv6_global_cmds = YANGDynClass(base=ipv6_global_cmds.ipv6_global_cmds, is_container='container', presence=False, yang_name="ipv6-global-cmds", rest_name="", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'cli-drop-node-name': None}}, namespace='urn:brocade.com:mgmt:brocade-ipv6-nd-ra', defining_module='brocade-ipv6-nd-ra', yang_type='container', is_config=True)
    self.__proto_vrrpv3 = YANGDynClass(base=proto_vrrpv3.proto_vrrpv3, is_container='container', presence=False, yang_name="proto-vrrpv3", rest_name="protocol", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'callpoint': u'vrrpv3GlobalConf', u'alt-name': u'protocol', u'cli-incomplete-no': None}}, namespace='urn:brocade.com:mgmt:brocade-vrrpv3', defining_module='brocade-vrrpv3', yang_type='container', is_config=True)
    self.__ipv6route = YANGDynClass(base=ipv6route.ipv6route, is_container='container', presence=False, yang_name="ipv6route", rest_name="", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'cli-drop-node-name': None, u'hidden': u'full'}}, namespace='urn:brocade.com:mgmt:brocade-ip-forward', defining_module='brocade-ip-forward', yang_type='container', is_config=True)
    self.__prefix_list = YANGDynClass(base=YANGListType("name seq_keyword instance",prefix_list.prefix_list, yang_name="prefix-list", rest_name="prefix-list", parent=self, is_container='list', user_ordered=False, path_helper=self._path_helper, yang_keys='name seq-keyword instance', extensions={u'tailf-common': {u'info': u'IPv6 address prefix list.', u'cli-no-key-completion': None, u'cli-suppress-mode': None, u'sort-priority': u'68', u'cli-suppress-list-no': None, u'cli-compact-syntax': None, u'cli-sequence-commands': None, u'cli-suppress-key-abbreviation': None, u'cli-incomplete-command': None, u'callpoint': u'ipv6prefix-cp'}}), is_container='list', yang_name="prefix-list", rest_name="prefix-list", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'info': u'IPv6 address prefix list.', u'cli-no-key-completion': None, u'cli-suppress-mode': None, u'sort-priority': u'68', u'cli-suppress-list-no': None, u'cli-compact-syntax': None, u'cli-sequence-commands': None, u'cli-suppress-key-abbreviation': None, u'cli-incomplete-command': None, u'callpoint': u'ipv6prefix-cp'}}, namespace='urn:brocade.com:mgmt:brocade-ip-policy', defining_module='brocade-ip-policy', yang_type='list', is_config=True)

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
      return [u'ipv6']

  def _rest_path(self):
    if hasattr(self, "_parent"):
      if self._rest_name:
        return self._parent._rest_path()+[self._rest_name]
      else:
        return self._parent._rest_path()
    else:
      return [u'ipv6']

  def _get_ipv6route(self):
    """
    Getter method for ipv6route, mapped from YANG variable /ipv6/ipv6route (container)
    """
    return self.__ipv6route
      
  def _set_ipv6route(self, v, load=False):
    """
    Setter method for ipv6route, mapped from YANG variable /ipv6/ipv6route (container)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_ipv6route is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_ipv6route() directly.
    """
    if hasattr(v, "_utype"):
      v = v._utype(v)
    try:
      t = YANGDynClass(v,base=ipv6route.ipv6route, is_container='container', presence=False, yang_name="ipv6route", rest_name="", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'cli-drop-node-name': None, u'hidden': u'full'}}, namespace='urn:brocade.com:mgmt:brocade-ip-forward', defining_module='brocade-ip-forward', yang_type='container', is_config=True)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """ipv6route must be of a type compatible with container""",
          'defined-type': "container",
          'generated-type': """YANGDynClass(base=ipv6route.ipv6route, is_container='container', presence=False, yang_name="ipv6route", rest_name="", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'cli-drop-node-name': None, u'hidden': u'full'}}, namespace='urn:brocade.com:mgmt:brocade-ip-forward', defining_module='brocade-ip-forward', yang_type='container', is_config=True)""",
        })

    self.__ipv6route = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_ipv6route(self):
    self.__ipv6route = YANGDynClass(base=ipv6route.ipv6route, is_container='container', presence=False, yang_name="ipv6route", rest_name="", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'cli-drop-node-name': None, u'hidden': u'full'}}, namespace='urn:brocade.com:mgmt:brocade-ip-forward', defining_module='brocade-ip-forward', yang_type='container', is_config=True)


  def _get_prefix_list(self):
    """
    Getter method for prefix_list, mapped from YANG variable /ipv6/prefix_list (list)

    YANG Description: IPv6 address prefix list.
    """
    return self.__prefix_list
      
  def _set_prefix_list(self, v, load=False):
    """
    Setter method for prefix_list, mapped from YANG variable /ipv6/prefix_list (list)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_prefix_list is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_prefix_list() directly.

    YANG Description: IPv6 address prefix list.
    """
    if hasattr(v, "_utype"):
      v = v._utype(v)
    try:
      t = YANGDynClass(v,base=YANGListType("name seq_keyword instance",prefix_list.prefix_list, yang_name="prefix-list", rest_name="prefix-list", parent=self, is_container='list', user_ordered=False, path_helper=self._path_helper, yang_keys='name seq-keyword instance', extensions={u'tailf-common': {u'info': u'IPv6 address prefix list.', u'cli-no-key-completion': None, u'cli-suppress-mode': None, u'sort-priority': u'68', u'cli-suppress-list-no': None, u'cli-compact-syntax': None, u'cli-sequence-commands': None, u'cli-suppress-key-abbreviation': None, u'cli-incomplete-command': None, u'callpoint': u'ipv6prefix-cp'}}), is_container='list', yang_name="prefix-list", rest_name="prefix-list", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'info': u'IPv6 address prefix list.', u'cli-no-key-completion': None, u'cli-suppress-mode': None, u'sort-priority': u'68', u'cli-suppress-list-no': None, u'cli-compact-syntax': None, u'cli-sequence-commands': None, u'cli-suppress-key-abbreviation': None, u'cli-incomplete-command': None, u'callpoint': u'ipv6prefix-cp'}}, namespace='urn:brocade.com:mgmt:brocade-ip-policy', defining_module='brocade-ip-policy', yang_type='list', is_config=True)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """prefix_list must be of a type compatible with list""",
          'defined-type': "list",
          'generated-type': """YANGDynClass(base=YANGListType("name seq_keyword instance",prefix_list.prefix_list, yang_name="prefix-list", rest_name="prefix-list", parent=self, is_container='list', user_ordered=False, path_helper=self._path_helper, yang_keys='name seq-keyword instance', extensions={u'tailf-common': {u'info': u'IPv6 address prefix list.', u'cli-no-key-completion': None, u'cli-suppress-mode': None, u'sort-priority': u'68', u'cli-suppress-list-no': None, u'cli-compact-syntax': None, u'cli-sequence-commands': None, u'cli-suppress-key-abbreviation': None, u'cli-incomplete-command': None, u'callpoint': u'ipv6prefix-cp'}}), is_container='list', yang_name="prefix-list", rest_name="prefix-list", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'info': u'IPv6 address prefix list.', u'cli-no-key-completion': None, u'cli-suppress-mode': None, u'sort-priority': u'68', u'cli-suppress-list-no': None, u'cli-compact-syntax': None, u'cli-sequence-commands': None, u'cli-suppress-key-abbreviation': None, u'cli-incomplete-command': None, u'callpoint': u'ipv6prefix-cp'}}, namespace='urn:brocade.com:mgmt:brocade-ip-policy', defining_module='brocade-ip-policy', yang_type='list', is_config=True)""",
        })

    self.__prefix_list = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_prefix_list(self):
    self.__prefix_list = YANGDynClass(base=YANGListType("name seq_keyword instance",prefix_list.prefix_list, yang_name="prefix-list", rest_name="prefix-list", parent=self, is_container='list', user_ordered=False, path_helper=self._path_helper, yang_keys='name seq-keyword instance', extensions={u'tailf-common': {u'info': u'IPv6 address prefix list.', u'cli-no-key-completion': None, u'cli-suppress-mode': None, u'sort-priority': u'68', u'cli-suppress-list-no': None, u'cli-compact-syntax': None, u'cli-sequence-commands': None, u'cli-suppress-key-abbreviation': None, u'cli-incomplete-command': None, u'callpoint': u'ipv6prefix-cp'}}), is_container='list', yang_name="prefix-list", rest_name="prefix-list", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'info': u'IPv6 address prefix list.', u'cli-no-key-completion': None, u'cli-suppress-mode': None, u'sort-priority': u'68', u'cli-suppress-list-no': None, u'cli-compact-syntax': None, u'cli-sequence-commands': None, u'cli-suppress-key-abbreviation': None, u'cli-incomplete-command': None, u'callpoint': u'ipv6prefix-cp'}}, namespace='urn:brocade.com:mgmt:brocade-ip-policy', defining_module='brocade-ip-policy', yang_type='list', is_config=True)


  def _get_ipv6_global_cmds(self):
    """
    Getter method for ipv6_global_cmds, mapped from YANG variable /ipv6/ipv6_global_cmds (container)
    """
    return self.__ipv6_global_cmds
      
  def _set_ipv6_global_cmds(self, v, load=False):
    """
    Setter method for ipv6_global_cmds, mapped from YANG variable /ipv6/ipv6_global_cmds (container)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_ipv6_global_cmds is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_ipv6_global_cmds() directly.
    """
    if hasattr(v, "_utype"):
      v = v._utype(v)
    try:
      t = YANGDynClass(v,base=ipv6_global_cmds.ipv6_global_cmds, is_container='container', presence=False, yang_name="ipv6-global-cmds", rest_name="", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'cli-drop-node-name': None}}, namespace='urn:brocade.com:mgmt:brocade-ipv6-nd-ra', defining_module='brocade-ipv6-nd-ra', yang_type='container', is_config=True)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """ipv6_global_cmds must be of a type compatible with container""",
          'defined-type': "container",
          'generated-type': """YANGDynClass(base=ipv6_global_cmds.ipv6_global_cmds, is_container='container', presence=False, yang_name="ipv6-global-cmds", rest_name="", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'cli-drop-node-name': None}}, namespace='urn:brocade.com:mgmt:brocade-ipv6-nd-ra', defining_module='brocade-ipv6-nd-ra', yang_type='container', is_config=True)""",
        })

    self.__ipv6_global_cmds = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_ipv6_global_cmds(self):
    self.__ipv6_global_cmds = YANGDynClass(base=ipv6_global_cmds.ipv6_global_cmds, is_container='container', presence=False, yang_name="ipv6-global-cmds", rest_name="", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'cli-drop-node-name': None}}, namespace='urn:brocade.com:mgmt:brocade-ipv6-nd-ra', defining_module='brocade-ipv6-nd-ra', yang_type='container', is_config=True)


  def _get_route(self):
    """
    Getter method for route, mapped from YANG variable /ipv6/route (container)
    """
    return self.__route
      
  def _set_route(self, v, load=False):
    """
    Setter method for route, mapped from YANG variable /ipv6/route (container)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_route is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_route() directly.
    """
    if hasattr(v, "_utype"):
      v = v._utype(v)
    try:
      t = YANGDynClass(v,base=route.route, is_container='container', presence=False, yang_name="route", rest_name="route", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'info': u'Configure IPv6 unicast static route', u'cli-incomplete-no': None}}, namespace='urn:brocade.com:mgmt:brocade-ipv6-rtm', defining_module='brocade-ipv6-rtm', yang_type='container', is_config=True)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """route must be of a type compatible with container""",
          'defined-type': "container",
          'generated-type': """YANGDynClass(base=route.route, is_container='container', presence=False, yang_name="route", rest_name="route", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'info': u'Configure IPv6 unicast static route', u'cli-incomplete-no': None}}, namespace='urn:brocade.com:mgmt:brocade-ipv6-rtm', defining_module='brocade-ipv6-rtm', yang_type='container', is_config=True)""",
        })

    self.__route = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_route(self):
    self.__route = YANGDynClass(base=route.route, is_container='container', presence=False, yang_name="route", rest_name="route", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'info': u'Configure IPv6 unicast static route', u'cli-incomplete-no': None}}, namespace='urn:brocade.com:mgmt:brocade-ipv6-rtm', defining_module='brocade-ipv6-rtm', yang_type='container', is_config=True)


  def _get_import_(self):
    """
    Getter method for import_, mapped from YANG variable /ipv6/import (container)
    """
    return self.__import_
      
  def _set_import_(self, v, load=False):
    """
    Setter method for import_, mapped from YANG variable /ipv6/import (container)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_import_ is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_import_() directly.
    """
    if hasattr(v, "_utype"):
      v = v._utype(v)
    try:
      t = YANGDynClass(v,base=import_.import_, is_container='container', presence=False, yang_name="import", rest_name="import", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'info': u'Import IPV6 routes'}}, namespace='urn:brocade.com:mgmt:brocade-ipv6-rtm', defining_module='brocade-ipv6-rtm', yang_type='container', is_config=True)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """import_ must be of a type compatible with container""",
          'defined-type': "container",
          'generated-type': """YANGDynClass(base=import_.import_, is_container='container', presence=False, yang_name="import", rest_name="import", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'info': u'Import IPV6 routes'}}, namespace='urn:brocade.com:mgmt:brocade-ipv6-rtm', defining_module='brocade-ipv6-rtm', yang_type='container', is_config=True)""",
        })

    self.__import_ = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_import_(self):
    self.__import_ = YANGDynClass(base=import_.import_, is_container='container', presence=False, yang_name="import", rest_name="import", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'info': u'Import IPV6 routes'}}, namespace='urn:brocade.com:mgmt:brocade-ipv6-rtm', defining_module='brocade-ipv6-rtm', yang_type='container', is_config=True)


  def _get_proto_vrrpv3(self):
    """
    Getter method for proto_vrrpv3, mapped from YANG variable /ipv6/proto_vrrpv3 (container)
    """
    return self.__proto_vrrpv3
      
  def _set_proto_vrrpv3(self, v, load=False):
    """
    Setter method for proto_vrrpv3, mapped from YANG variable /ipv6/proto_vrrpv3 (container)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_proto_vrrpv3 is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_proto_vrrpv3() directly.
    """
    if hasattr(v, "_utype"):
      v = v._utype(v)
    try:
      t = YANGDynClass(v,base=proto_vrrpv3.proto_vrrpv3, is_container='container', presence=False, yang_name="proto-vrrpv3", rest_name="protocol", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'callpoint': u'vrrpv3GlobalConf', u'alt-name': u'protocol', u'cli-incomplete-no': None}}, namespace='urn:brocade.com:mgmt:brocade-vrrpv3', defining_module='brocade-vrrpv3', yang_type='container', is_config=True)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """proto_vrrpv3 must be of a type compatible with container""",
          'defined-type': "container",
          'generated-type': """YANGDynClass(base=proto_vrrpv3.proto_vrrpv3, is_container='container', presence=False, yang_name="proto-vrrpv3", rest_name="protocol", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'callpoint': u'vrrpv3GlobalConf', u'alt-name': u'protocol', u'cli-incomplete-no': None}}, namespace='urn:brocade.com:mgmt:brocade-vrrpv3', defining_module='brocade-vrrpv3', yang_type='container', is_config=True)""",
        })

    self.__proto_vrrpv3 = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_proto_vrrpv3(self):
    self.__proto_vrrpv3 = YANGDynClass(base=proto_vrrpv3.proto_vrrpv3, is_container='container', presence=False, yang_name="proto-vrrpv3", rest_name="protocol", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'callpoint': u'vrrpv3GlobalConf', u'alt-name': u'protocol', u'cli-incomplete-no': None}}, namespace='urn:brocade.com:mgmt:brocade-vrrpv3', defining_module='brocade-vrrpv3', yang_type='container', is_config=True)

  ipv6route = __builtin__.property(_get_ipv6route, _set_ipv6route)
  prefix_list = __builtin__.property(_get_prefix_list, _set_prefix_list)
  ipv6_global_cmds = __builtin__.property(_get_ipv6_global_cmds, _set_ipv6_global_cmds)
  route = __builtin__.property(_get_route, _set_route)
  import_ = __builtin__.property(_get_import_, _set_import_)
  proto_vrrpv3 = __builtin__.property(_get_proto_vrrpv3, _set_proto_vrrpv3)


  _pyangbind_elements = {'ipv6route': ipv6route, 'prefix_list': prefix_list, 'ipv6_global_cmds': ipv6_global_cmds, 'route': route, 'import_': import_, 'proto_vrrpv3': proto_vrrpv3, }


