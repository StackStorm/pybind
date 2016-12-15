
from operator import attrgetter
import pyangbind.lib.xpathhelper as xpathhelper
from pyangbind.lib.yangtypes import RestrictedPrecisionDecimalType, RestrictedClassType, TypedListType
from pyangbind.lib.yangtypes import YANGBool, YANGListType, YANGDynClass, ReferenceType
from pyangbind.lib.base import PybindBase
from decimal import Decimal
from bitarray import bitarray
import __builtin__
import static_mac
import static_ac_lif
class static(PybindBase):
  """
  This class was auto-generated by the PythonClass plugin for PYANG
  from YANG module brocade-mac-address-table - based on the path /mac-address-table/static. Each member element of
  the container is represented as a class variable - with a specific
  YANG type.
  """
  __slots__ = ('_pybind_generated_by', '_path_helper', '_yang_name', '_rest_name', '_extmethods', '__static_mac','__static_ac_lif',)

  _yang_name = 'static'
  _rest_name = 'static'

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
    self.__static_mac = YANGDynClass(base=YANGListType("mac_address forward interface_type interface_name vlan vlanid",static_mac.static_mac, yang_name="static-mac", rest_name="", parent=self, is_container='list', user_ordered=False, path_helper=self._path_helper, yang_keys='mac-address forward interface-type interface-name vlan vlanid', extensions={u'tailf-common': {u'info': u'Static address', u'cli-no-key-completion': None, u'cli-suppress-mode': None, u'cli-suppress-list-no': None, u'cli-drop-node-name': None, u'cli-sequence-commands': None, u'hidden': u'wyser-write-hook', u'callpoint': u'static-mac-callpoint'}}), is_container='list', yang_name="static-mac", rest_name="", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'info': u'Static address', u'cli-no-key-completion': None, u'cli-suppress-mode': None, u'cli-suppress-list-no': None, u'cli-drop-node-name': None, u'cli-sequence-commands': None, u'hidden': u'wyser-write-hook', u'callpoint': u'static-mac-callpoint'}}, namespace='urn:brocade.com:mgmt:brocade-mac-address-table', defining_module='brocade-mac-address-table', yang_type='list', is_config=True)
    self.__static_ac_lif = YANGDynClass(base=YANGListType("mac_address_lif forward_lif logical_interface interface_type_lif logical_interface_name",static_ac_lif.static_ac_lif, yang_name="static-ac-lif", rest_name="", parent=self, is_container='list', user_ordered=False, path_helper=self._path_helper, yang_keys='mac-address-lif forward-lif logical-interface interface-type-lif logical-interface-name', extensions={u'tailf-common': {u'info': u'Static address', u'cli-no-key-completion': None, u'cli-suppress-mode': None, u'cli-suppress-list-no': None, u'cli-drop-node-name': None, u'cli-sequence-commands': None, u'callpoint': u'static-mac-lif-callpoint'}}), is_container='list', yang_name="static-ac-lif", rest_name="", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'info': u'Static address', u'cli-no-key-completion': None, u'cli-suppress-mode': None, u'cli-suppress-list-no': None, u'cli-drop-node-name': None, u'cli-sequence-commands': None, u'callpoint': u'static-mac-lif-callpoint'}}, namespace='urn:brocade.com:mgmt:brocade-mac-address-table', defining_module='brocade-mac-address-table', yang_type='list', is_config=True)

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
      return [u'mac-address-table', u'static']

  def _rest_path(self):
    if hasattr(self, "_parent"):
      if self._rest_name:
        return self._parent._rest_path()+[self._rest_name]
      else:
        return self._parent._rest_path()
    else:
      return [u'mac-address-table', u'static']

  def _get_static_mac(self):
    """
    Getter method for static_mac, mapped from YANG variable /mac_address_table/static/static_mac (list)
    """
    return self.__static_mac
      
  def _set_static_mac(self, v, load=False):
    """
    Setter method for static_mac, mapped from YANG variable /mac_address_table/static/static_mac (list)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_static_mac is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_static_mac() directly.
    """
    if hasattr(v, "_utype"):
      v = v._utype(v)
    try:
      t = YANGDynClass(v,base=YANGListType("mac_address forward interface_type interface_name vlan vlanid",static_mac.static_mac, yang_name="static-mac", rest_name="", parent=self, is_container='list', user_ordered=False, path_helper=self._path_helper, yang_keys='mac-address forward interface-type interface-name vlan vlanid', extensions={u'tailf-common': {u'info': u'Static address', u'cli-no-key-completion': None, u'cli-suppress-mode': None, u'cli-suppress-list-no': None, u'cli-drop-node-name': None, u'cli-sequence-commands': None, u'hidden': u'wyser-write-hook', u'callpoint': u'static-mac-callpoint'}}), is_container='list', yang_name="static-mac", rest_name="", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'info': u'Static address', u'cli-no-key-completion': None, u'cli-suppress-mode': None, u'cli-suppress-list-no': None, u'cli-drop-node-name': None, u'cli-sequence-commands': None, u'hidden': u'wyser-write-hook', u'callpoint': u'static-mac-callpoint'}}, namespace='urn:brocade.com:mgmt:brocade-mac-address-table', defining_module='brocade-mac-address-table', yang_type='list', is_config=True)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """static_mac must be of a type compatible with list""",
          'defined-type': "list",
          'generated-type': """YANGDynClass(base=YANGListType("mac_address forward interface_type interface_name vlan vlanid",static_mac.static_mac, yang_name="static-mac", rest_name="", parent=self, is_container='list', user_ordered=False, path_helper=self._path_helper, yang_keys='mac-address forward interface-type interface-name vlan vlanid', extensions={u'tailf-common': {u'info': u'Static address', u'cli-no-key-completion': None, u'cli-suppress-mode': None, u'cli-suppress-list-no': None, u'cli-drop-node-name': None, u'cli-sequence-commands': None, u'hidden': u'wyser-write-hook', u'callpoint': u'static-mac-callpoint'}}), is_container='list', yang_name="static-mac", rest_name="", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'info': u'Static address', u'cli-no-key-completion': None, u'cli-suppress-mode': None, u'cli-suppress-list-no': None, u'cli-drop-node-name': None, u'cli-sequence-commands': None, u'hidden': u'wyser-write-hook', u'callpoint': u'static-mac-callpoint'}}, namespace='urn:brocade.com:mgmt:brocade-mac-address-table', defining_module='brocade-mac-address-table', yang_type='list', is_config=True)""",
        })

    self.__static_mac = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_static_mac(self):
    self.__static_mac = YANGDynClass(base=YANGListType("mac_address forward interface_type interface_name vlan vlanid",static_mac.static_mac, yang_name="static-mac", rest_name="", parent=self, is_container='list', user_ordered=False, path_helper=self._path_helper, yang_keys='mac-address forward interface-type interface-name vlan vlanid', extensions={u'tailf-common': {u'info': u'Static address', u'cli-no-key-completion': None, u'cli-suppress-mode': None, u'cli-suppress-list-no': None, u'cli-drop-node-name': None, u'cli-sequence-commands': None, u'hidden': u'wyser-write-hook', u'callpoint': u'static-mac-callpoint'}}), is_container='list', yang_name="static-mac", rest_name="", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'info': u'Static address', u'cli-no-key-completion': None, u'cli-suppress-mode': None, u'cli-suppress-list-no': None, u'cli-drop-node-name': None, u'cli-sequence-commands': None, u'hidden': u'wyser-write-hook', u'callpoint': u'static-mac-callpoint'}}, namespace='urn:brocade.com:mgmt:brocade-mac-address-table', defining_module='brocade-mac-address-table', yang_type='list', is_config=True)


  def _get_static_ac_lif(self):
    """
    Getter method for static_ac_lif, mapped from YANG variable /mac_address_table/static/static_ac_lif (list)
    """
    return self.__static_ac_lif
      
  def _set_static_ac_lif(self, v, load=False):
    """
    Setter method for static_ac_lif, mapped from YANG variable /mac_address_table/static/static_ac_lif (list)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_static_ac_lif is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_static_ac_lif() directly.
    """
    if hasattr(v, "_utype"):
      v = v._utype(v)
    try:
      t = YANGDynClass(v,base=YANGListType("mac_address_lif forward_lif logical_interface interface_type_lif logical_interface_name",static_ac_lif.static_ac_lif, yang_name="static-ac-lif", rest_name="", parent=self, is_container='list', user_ordered=False, path_helper=self._path_helper, yang_keys='mac-address-lif forward-lif logical-interface interface-type-lif logical-interface-name', extensions={u'tailf-common': {u'info': u'Static address', u'cli-no-key-completion': None, u'cli-suppress-mode': None, u'cli-suppress-list-no': None, u'cli-drop-node-name': None, u'cli-sequence-commands': None, u'callpoint': u'static-mac-lif-callpoint'}}), is_container='list', yang_name="static-ac-lif", rest_name="", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'info': u'Static address', u'cli-no-key-completion': None, u'cli-suppress-mode': None, u'cli-suppress-list-no': None, u'cli-drop-node-name': None, u'cli-sequence-commands': None, u'callpoint': u'static-mac-lif-callpoint'}}, namespace='urn:brocade.com:mgmt:brocade-mac-address-table', defining_module='brocade-mac-address-table', yang_type='list', is_config=True)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """static_ac_lif must be of a type compatible with list""",
          'defined-type': "list",
          'generated-type': """YANGDynClass(base=YANGListType("mac_address_lif forward_lif logical_interface interface_type_lif logical_interface_name",static_ac_lif.static_ac_lif, yang_name="static-ac-lif", rest_name="", parent=self, is_container='list', user_ordered=False, path_helper=self._path_helper, yang_keys='mac-address-lif forward-lif logical-interface interface-type-lif logical-interface-name', extensions={u'tailf-common': {u'info': u'Static address', u'cli-no-key-completion': None, u'cli-suppress-mode': None, u'cli-suppress-list-no': None, u'cli-drop-node-name': None, u'cli-sequence-commands': None, u'callpoint': u'static-mac-lif-callpoint'}}), is_container='list', yang_name="static-ac-lif", rest_name="", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'info': u'Static address', u'cli-no-key-completion': None, u'cli-suppress-mode': None, u'cli-suppress-list-no': None, u'cli-drop-node-name': None, u'cli-sequence-commands': None, u'callpoint': u'static-mac-lif-callpoint'}}, namespace='urn:brocade.com:mgmt:brocade-mac-address-table', defining_module='brocade-mac-address-table', yang_type='list', is_config=True)""",
        })

    self.__static_ac_lif = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_static_ac_lif(self):
    self.__static_ac_lif = YANGDynClass(base=YANGListType("mac_address_lif forward_lif logical_interface interface_type_lif logical_interface_name",static_ac_lif.static_ac_lif, yang_name="static-ac-lif", rest_name="", parent=self, is_container='list', user_ordered=False, path_helper=self._path_helper, yang_keys='mac-address-lif forward-lif logical-interface interface-type-lif logical-interface-name', extensions={u'tailf-common': {u'info': u'Static address', u'cli-no-key-completion': None, u'cli-suppress-mode': None, u'cli-suppress-list-no': None, u'cli-drop-node-name': None, u'cli-sequence-commands': None, u'callpoint': u'static-mac-lif-callpoint'}}), is_container='list', yang_name="static-ac-lif", rest_name="", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'info': u'Static address', u'cli-no-key-completion': None, u'cli-suppress-mode': None, u'cli-suppress-list-no': None, u'cli-drop-node-name': None, u'cli-sequence-commands': None, u'callpoint': u'static-mac-lif-callpoint'}}, namespace='urn:brocade.com:mgmt:brocade-mac-address-table', defining_module='brocade-mac-address-table', yang_type='list', is_config=True)

  static_mac = __builtin__.property(_get_static_mac, _set_static_mac)
  static_ac_lif = __builtin__.property(_get_static_ac_lif, _set_static_ac_lif)


  _pyangbind_elements = {'static_mac': static_mac, 'static_ac_lif': static_ac_lif, }


