
from operator import attrgetter
import pyangbind.lib.xpathhelper as xpathhelper
from pyangbind.lib.yangtypes import RestrictedPrecisionDecimalType, RestrictedClassType, TypedListType
from pyangbind.lib.yangtypes import YANGBool, YANGListType, YANGDynClass, ReferenceType
from pyangbind.lib.base import PybindBase
from decimal import Decimal
from bitarray import bitarray
import __builtin__
import link_local_config
import ipv6_address
class address(PybindBase):
  """
  This class was auto-generated by the PythonClass plugin for PYANG
  from YANG module brocade-interface - based on the path /interface/gigabitethernet/ipv6/ipv6-config/address. Each member element of
  the container is represented as a class variable - with a specific
  YANG type.
  """
  __slots__ = ('_pybind_generated_by', '_path_helper', '_yang_name', '_rest_name', '_extmethods', '__use_link_local_only','__link_local_config','__ipv6_address',)

  _yang_name = 'address'
  _rest_name = 'address'

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
    self.__use_link_local_only = YANGDynClass(base=YANGBool, is_leaf=True, yang_name="use-link-local-only", rest_name="use-link-local-only", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'cli-full-command': None, u'info': u'Configure automatically computed link-local address', u'callpoint': u'phy-intf-ipv6-cfg-cp'}}, namespace='urn:brocade.com:mgmt:brocade-ipv6-config', defining_module='brocade-ipv6-config', yang_type='empty', is_config=True)
    self.__link_local_config = YANGDynClass(base=link_local_config.link_local_config, is_container='container', presence=False, yang_name="link-local-config", rest_name="", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'cli-compact-syntax': None, u'cli-drop-node-name': None, u'cli-sequence-commands': None, u'callpoint': u'phy-intf-ipv6-cfg-cp'}}, namespace='urn:brocade.com:mgmt:brocade-ipv6-config', defining_module='brocade-ipv6-config', yang_type='container', is_config=True)
    self.__ipv6_address = YANGDynClass(base=YANGListType("address",ipv6_address.ipv6_address, yang_name="ipv6-address", rest_name="", parent=self, is_container='list', user_ordered=True, path_helper=self._path_helper, yang_keys='address', extensions={u'tailf-common': {u'info': u'Set the IP address of an interface', u'cli-no-key-completion': None, u'cli-suppress-mode': None, u'cli-compact-syntax': None, u'cli-drop-node-name': None, u'cli-no-match-completion': None, u'callpoint': u'phy-intf-ipv6-addr-cp'}}), is_container='list', yang_name="ipv6-address", rest_name="", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'info': u'Set the IP address of an interface', u'cli-no-key-completion': None, u'cli-suppress-mode': None, u'cli-compact-syntax': None, u'cli-drop-node-name': None, u'cli-no-match-completion': None, u'callpoint': u'phy-intf-ipv6-addr-cp'}}, namespace='urn:brocade.com:mgmt:brocade-ipv6-config', defining_module='brocade-ipv6-config', yang_type='list', is_config=True)

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
      return [u'interface', u'gigabitethernet', u'ipv6', u'ipv6-config', u'address']

  def _rest_path(self):
    if hasattr(self, "_parent"):
      if self._rest_name:
        return self._parent._rest_path()+[self._rest_name]
      else:
        return self._parent._rest_path()
    else:
      return [u'interface', u'GigabitEthernet', u'ipv6', u'address']

  def _get_use_link_local_only(self):
    """
    Getter method for use_link_local_only, mapped from YANG variable /interface/gigabitethernet/ipv6/ipv6_config/address/use_link_local_only (empty)
    """
    return self.__use_link_local_only
      
  def _set_use_link_local_only(self, v, load=False):
    """
    Setter method for use_link_local_only, mapped from YANG variable /interface/gigabitethernet/ipv6/ipv6_config/address/use_link_local_only (empty)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_use_link_local_only is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_use_link_local_only() directly.
    """
    if hasattr(v, "_utype"):
      v = v._utype(v)
    try:
      t = YANGDynClass(v,base=YANGBool, is_leaf=True, yang_name="use-link-local-only", rest_name="use-link-local-only", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'cli-full-command': None, u'info': u'Configure automatically computed link-local address', u'callpoint': u'phy-intf-ipv6-cfg-cp'}}, namespace='urn:brocade.com:mgmt:brocade-ipv6-config', defining_module='brocade-ipv6-config', yang_type='empty', is_config=True)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """use_link_local_only must be of a type compatible with empty""",
          'defined-type': "empty",
          'generated-type': """YANGDynClass(base=YANGBool, is_leaf=True, yang_name="use-link-local-only", rest_name="use-link-local-only", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'cli-full-command': None, u'info': u'Configure automatically computed link-local address', u'callpoint': u'phy-intf-ipv6-cfg-cp'}}, namespace='urn:brocade.com:mgmt:brocade-ipv6-config', defining_module='brocade-ipv6-config', yang_type='empty', is_config=True)""",
        })

    self.__use_link_local_only = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_use_link_local_only(self):
    self.__use_link_local_only = YANGDynClass(base=YANGBool, is_leaf=True, yang_name="use-link-local-only", rest_name="use-link-local-only", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'cli-full-command': None, u'info': u'Configure automatically computed link-local address', u'callpoint': u'phy-intf-ipv6-cfg-cp'}}, namespace='urn:brocade.com:mgmt:brocade-ipv6-config', defining_module='brocade-ipv6-config', yang_type='empty', is_config=True)


  def _get_link_local_config(self):
    """
    Getter method for link_local_config, mapped from YANG variable /interface/gigabitethernet/ipv6/ipv6_config/address/link_local_config (container)
    """
    return self.__link_local_config
      
  def _set_link_local_config(self, v, load=False):
    """
    Setter method for link_local_config, mapped from YANG variable /interface/gigabitethernet/ipv6/ipv6_config/address/link_local_config (container)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_link_local_config is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_link_local_config() directly.
    """
    if hasattr(v, "_utype"):
      v = v._utype(v)
    try:
      t = YANGDynClass(v,base=link_local_config.link_local_config, is_container='container', presence=False, yang_name="link-local-config", rest_name="", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'cli-compact-syntax': None, u'cli-drop-node-name': None, u'cli-sequence-commands': None, u'callpoint': u'phy-intf-ipv6-cfg-cp'}}, namespace='urn:brocade.com:mgmt:brocade-ipv6-config', defining_module='brocade-ipv6-config', yang_type='container', is_config=True)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """link_local_config must be of a type compatible with container""",
          'defined-type': "container",
          'generated-type': """YANGDynClass(base=link_local_config.link_local_config, is_container='container', presence=False, yang_name="link-local-config", rest_name="", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'cli-compact-syntax': None, u'cli-drop-node-name': None, u'cli-sequence-commands': None, u'callpoint': u'phy-intf-ipv6-cfg-cp'}}, namespace='urn:brocade.com:mgmt:brocade-ipv6-config', defining_module='brocade-ipv6-config', yang_type='container', is_config=True)""",
        })

    self.__link_local_config = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_link_local_config(self):
    self.__link_local_config = YANGDynClass(base=link_local_config.link_local_config, is_container='container', presence=False, yang_name="link-local-config", rest_name="", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'cli-compact-syntax': None, u'cli-drop-node-name': None, u'cli-sequence-commands': None, u'callpoint': u'phy-intf-ipv6-cfg-cp'}}, namespace='urn:brocade.com:mgmt:brocade-ipv6-config', defining_module='brocade-ipv6-config', yang_type='container', is_config=True)


  def _get_ipv6_address(self):
    """
    Getter method for ipv6_address, mapped from YANG variable /interface/gigabitethernet/ipv6/ipv6_config/address/ipv6_address (list)
    """
    return self.__ipv6_address
      
  def _set_ipv6_address(self, v, load=False):
    """
    Setter method for ipv6_address, mapped from YANG variable /interface/gigabitethernet/ipv6/ipv6_config/address/ipv6_address (list)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_ipv6_address is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_ipv6_address() directly.
    """
    if hasattr(v, "_utype"):
      v = v._utype(v)
    try:
      t = YANGDynClass(v,base=YANGListType("address",ipv6_address.ipv6_address, yang_name="ipv6-address", rest_name="", parent=self, is_container='list', user_ordered=True, path_helper=self._path_helper, yang_keys='address', extensions={u'tailf-common': {u'info': u'Set the IP address of an interface', u'cli-no-key-completion': None, u'cli-suppress-mode': None, u'cli-compact-syntax': None, u'cli-drop-node-name': None, u'cli-no-match-completion': None, u'callpoint': u'phy-intf-ipv6-addr-cp'}}), is_container='list', yang_name="ipv6-address", rest_name="", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'info': u'Set the IP address of an interface', u'cli-no-key-completion': None, u'cli-suppress-mode': None, u'cli-compact-syntax': None, u'cli-drop-node-name': None, u'cli-no-match-completion': None, u'callpoint': u'phy-intf-ipv6-addr-cp'}}, namespace='urn:brocade.com:mgmt:brocade-ipv6-config', defining_module='brocade-ipv6-config', yang_type='list', is_config=True)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """ipv6_address must be of a type compatible with list""",
          'defined-type': "list",
          'generated-type': """YANGDynClass(base=YANGListType("address",ipv6_address.ipv6_address, yang_name="ipv6-address", rest_name="", parent=self, is_container='list', user_ordered=True, path_helper=self._path_helper, yang_keys='address', extensions={u'tailf-common': {u'info': u'Set the IP address of an interface', u'cli-no-key-completion': None, u'cli-suppress-mode': None, u'cli-compact-syntax': None, u'cli-drop-node-name': None, u'cli-no-match-completion': None, u'callpoint': u'phy-intf-ipv6-addr-cp'}}), is_container='list', yang_name="ipv6-address", rest_name="", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'info': u'Set the IP address of an interface', u'cli-no-key-completion': None, u'cli-suppress-mode': None, u'cli-compact-syntax': None, u'cli-drop-node-name': None, u'cli-no-match-completion': None, u'callpoint': u'phy-intf-ipv6-addr-cp'}}, namespace='urn:brocade.com:mgmt:brocade-ipv6-config', defining_module='brocade-ipv6-config', yang_type='list', is_config=True)""",
        })

    self.__ipv6_address = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_ipv6_address(self):
    self.__ipv6_address = YANGDynClass(base=YANGListType("address",ipv6_address.ipv6_address, yang_name="ipv6-address", rest_name="", parent=self, is_container='list', user_ordered=True, path_helper=self._path_helper, yang_keys='address', extensions={u'tailf-common': {u'info': u'Set the IP address of an interface', u'cli-no-key-completion': None, u'cli-suppress-mode': None, u'cli-compact-syntax': None, u'cli-drop-node-name': None, u'cli-no-match-completion': None, u'callpoint': u'phy-intf-ipv6-addr-cp'}}), is_container='list', yang_name="ipv6-address", rest_name="", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'info': u'Set the IP address of an interface', u'cli-no-key-completion': None, u'cli-suppress-mode': None, u'cli-compact-syntax': None, u'cli-drop-node-name': None, u'cli-no-match-completion': None, u'callpoint': u'phy-intf-ipv6-addr-cp'}}, namespace='urn:brocade.com:mgmt:brocade-ipv6-config', defining_module='brocade-ipv6-config', yang_type='list', is_config=True)

  use_link_local_only = __builtin__.property(_get_use_link_local_only, _set_use_link_local_only)
  link_local_config = __builtin__.property(_get_link_local_config, _set_link_local_config)
  ipv6_address = __builtin__.property(_get_ipv6_address, _set_ipv6_address)


  _pyangbind_elements = {'use_link_local_only': use_link_local_only, 'link_local_config': link_local_config, 'ipv6_address': ipv6_address, }


