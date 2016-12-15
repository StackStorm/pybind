
from operator import attrgetter
import pyangbind.lib.xpathhelper as xpathhelper
from pyangbind.lib.yangtypes import RestrictedPrecisionDecimalType, RestrictedClassType, TypedListType
from pyangbind.lib.yangtypes import YANGBool, YANGListType, YANGDynClass, ReferenceType
from pyangbind.lib.base import PybindBase
from decimal import Decimal
from bitarray import bitarray
import __builtin__
class af_evpn_neighbor(PybindBase):
  """
  This class was auto-generated by the PythonClass plugin for PYANG
  from YANG module brocade-common-def - based on the path /routing-system/router/router-bgp/address-family/evpn/af-evpn-neighbor-address-holder/af-evpn-neighbor. Each member element of
  the container is represented as a class variable - with a specific
  YANG type.
  """
  __slots__ = ('_pybind_generated_by', '_path_helper', '_yang_name', '_rest_name', '_extmethods', '__af_evpn_neighbor_address','__evpn_nbr_activate',)

  _yang_name = 'af-evpn-neighbor'
  _rest_name = 'neighbor'

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
    self.__af_evpn_neighbor_address = YANGDynClass(base=RestrictedClassType(base_type=unicode, restriction_dict={'pattern': u'(([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])\\.){3}([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])(%[\\p{N}\\p{L}]+)?'}), is_leaf=True, yang_name="af-evpn-neighbor-address", rest_name="", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'info': u'A.B.C.D;;Neighbor Address', u'cli-drop-node-name': None}}, is_keyval=True, namespace='urn:brocade.com:mgmt:brocade-bgp', defining_module='brocade-bgp', yang_type='inet:ipv4-address', is_config=True)
    self.__evpn_nbr_activate = YANGDynClass(base=YANGBool, is_leaf=True, yang_name="evpn-nbr-activate", rest_name="activate", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'info': u'Allow exchange of route in the current family mode', u'cli-full-command': None, u'alt-name': u'activate'}}, namespace='urn:brocade.com:mgmt:brocade-bgp', defining_module='brocade-bgp', yang_type='empty', is_config=True)

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
      return [u'routing-system', u'router', u'router-bgp', u'address-family', u'evpn', u'af-evpn-neighbor-address-holder', u'af-evpn-neighbor']

  def _rest_path(self):
    if hasattr(self, "_parent"):
      if self._rest_name:
        return self._parent._rest_path()+[self._rest_name]
      else:
        return self._parent._rest_path()
    else:
      return [u'router', u'bgp', u'address-family', u'evpn', u'neighbor']

  def _get_af_evpn_neighbor_address(self):
    """
    Getter method for af_evpn_neighbor_address, mapped from YANG variable /routing_system/router/router_bgp/address_family/evpn/af_evpn_neighbor_address_holder/af_evpn_neighbor/af_evpn_neighbor_address (inet:ipv4-address)
    """
    return self.__af_evpn_neighbor_address
      
  def _set_af_evpn_neighbor_address(self, v, load=False):
    """
    Setter method for af_evpn_neighbor_address, mapped from YANG variable /routing_system/router/router_bgp/address_family/evpn/af_evpn_neighbor_address_holder/af_evpn_neighbor/af_evpn_neighbor_address (inet:ipv4-address)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_af_evpn_neighbor_address is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_af_evpn_neighbor_address() directly.
    """
    parent = getattr(self, "_parent", None)
    if parent is not None and load is False:
      raise AttributeError("Cannot set keys directly when" +
                             " within an instantiated list")

    if hasattr(v, "_utype"):
      v = v._utype(v)
    try:
      t = YANGDynClass(v,base=RestrictedClassType(base_type=unicode, restriction_dict={'pattern': u'(([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])\\.){3}([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])(%[\\p{N}\\p{L}]+)?'}), is_leaf=True, yang_name="af-evpn-neighbor-address", rest_name="", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'info': u'A.B.C.D;;Neighbor Address', u'cli-drop-node-name': None}}, is_keyval=True, namespace='urn:brocade.com:mgmt:brocade-bgp', defining_module='brocade-bgp', yang_type='inet:ipv4-address', is_config=True)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """af_evpn_neighbor_address must be of a type compatible with inet:ipv4-address""",
          'defined-type': "inet:ipv4-address",
          'generated-type': """YANGDynClass(base=RestrictedClassType(base_type=unicode, restriction_dict={'pattern': u'(([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])\\.){3}([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])(%[\\p{N}\\p{L}]+)?'}), is_leaf=True, yang_name="af-evpn-neighbor-address", rest_name="", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'info': u'A.B.C.D;;Neighbor Address', u'cli-drop-node-name': None}}, is_keyval=True, namespace='urn:brocade.com:mgmt:brocade-bgp', defining_module='brocade-bgp', yang_type='inet:ipv4-address', is_config=True)""",
        })

    self.__af_evpn_neighbor_address = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_af_evpn_neighbor_address(self):
    self.__af_evpn_neighbor_address = YANGDynClass(base=RestrictedClassType(base_type=unicode, restriction_dict={'pattern': u'(([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])\\.){3}([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])(%[\\p{N}\\p{L}]+)?'}), is_leaf=True, yang_name="af-evpn-neighbor-address", rest_name="", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'info': u'A.B.C.D;;Neighbor Address', u'cli-drop-node-name': None}}, is_keyval=True, namespace='urn:brocade.com:mgmt:brocade-bgp', defining_module='brocade-bgp', yang_type='inet:ipv4-address', is_config=True)


  def _get_evpn_nbr_activate(self):
    """
    Getter method for evpn_nbr_activate, mapped from YANG variable /routing_system/router/router_bgp/address_family/evpn/af_evpn_neighbor_address_holder/af_evpn_neighbor/evpn_nbr_activate (empty)
    """
    return self.__evpn_nbr_activate
      
  def _set_evpn_nbr_activate(self, v, load=False):
    """
    Setter method for evpn_nbr_activate, mapped from YANG variable /routing_system/router/router_bgp/address_family/evpn/af_evpn_neighbor_address_holder/af_evpn_neighbor/evpn_nbr_activate (empty)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_evpn_nbr_activate is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_evpn_nbr_activate() directly.
    """
    if hasattr(v, "_utype"):
      v = v._utype(v)
    try:
      t = YANGDynClass(v,base=YANGBool, is_leaf=True, yang_name="evpn-nbr-activate", rest_name="activate", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'info': u'Allow exchange of route in the current family mode', u'cli-full-command': None, u'alt-name': u'activate'}}, namespace='urn:brocade.com:mgmt:brocade-bgp', defining_module='brocade-bgp', yang_type='empty', is_config=True)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """evpn_nbr_activate must be of a type compatible with empty""",
          'defined-type': "empty",
          'generated-type': """YANGDynClass(base=YANGBool, is_leaf=True, yang_name="evpn-nbr-activate", rest_name="activate", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'info': u'Allow exchange of route in the current family mode', u'cli-full-command': None, u'alt-name': u'activate'}}, namespace='urn:brocade.com:mgmt:brocade-bgp', defining_module='brocade-bgp', yang_type='empty', is_config=True)""",
        })

    self.__evpn_nbr_activate = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_evpn_nbr_activate(self):
    self.__evpn_nbr_activate = YANGDynClass(base=YANGBool, is_leaf=True, yang_name="evpn-nbr-activate", rest_name="activate", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'info': u'Allow exchange of route in the current family mode', u'cli-full-command': None, u'alt-name': u'activate'}}, namespace='urn:brocade.com:mgmt:brocade-bgp', defining_module='brocade-bgp', yang_type='empty', is_config=True)

  af_evpn_neighbor_address = __builtin__.property(_get_af_evpn_neighbor_address, _set_af_evpn_neighbor_address)
  evpn_nbr_activate = __builtin__.property(_get_evpn_nbr_activate, _set_evpn_nbr_activate)


  _pyangbind_elements = {'af_evpn_neighbor_address': af_evpn_neighbor_address, 'evpn_nbr_activate': evpn_nbr_activate, }


