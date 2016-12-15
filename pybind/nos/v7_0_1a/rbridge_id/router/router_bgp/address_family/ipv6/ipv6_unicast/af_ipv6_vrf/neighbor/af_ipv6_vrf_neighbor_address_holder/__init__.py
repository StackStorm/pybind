
from operator import attrgetter
import pyangbind.lib.xpathhelper as xpathhelper
from pyangbind.lib.yangtypes import RestrictedPrecisionDecimalType, RestrictedClassType, TypedListType
from pyangbind.lib.yangtypes import YANGBool, YANGListType, YANGDynClass, ReferenceType
from pyangbind.lib.base import PybindBase
from decimal import Decimal
from bitarray import bitarray
import __builtin__
import af_ipv6_neighbor_addr
class af_ipv6_vrf_neighbor_address_holder(PybindBase):
  """
  This class was auto-generated by the PythonClass plugin for PYANG
  from YANG module brocade-rbridge - based on the path /rbridge-id/router/router-bgp/address-family/ipv6/ipv6-unicast/af-ipv6-vrf/neighbor/af-ipv6-vrf-neighbor-address-holder. Each member element of
  the container is represented as a class variable - with a specific
  YANG type.
  """
  __slots__ = ('_pybind_generated_by', '_path_helper', '_yang_name', '_rest_name', '_extmethods', '__af_ipv6_neighbor_addr',)

  _yang_name = 'af-ipv6-vrf-neighbor-address-holder'
  _rest_name = ''

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
    self.__af_ipv6_neighbor_addr = YANGDynClass(base=YANGListType("af_ipv6_neighbor_address",af_ipv6_neighbor_addr.af_ipv6_neighbor_addr, yang_name="af-ipv6-neighbor-addr", rest_name="", parent=self, is_container='list', user_ordered=False, path_helper=self._path_helper, yang_keys='af-ipv6-neighbor-address', extensions={u'tailf-common': {u'cli-no-key-completion': None, u'cli-suppress-mode': None, u'cli-incomplete-no': None, u'cli-suppress-list-no': None, u'cli-drop-node-name': None, u'cli-suppress-key-abbreviation': None, u'cli-incomplete-command': None, u'callpoint': u'AfIpv6VrfNeighborAddr'}}), is_container='list', yang_name="af-ipv6-neighbor-addr", rest_name="", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'cli-no-key-completion': None, u'cli-suppress-mode': None, u'cli-incomplete-no': None, u'cli-suppress-list-no': None, u'cli-drop-node-name': None, u'cli-suppress-key-abbreviation': None, u'cli-incomplete-command': None, u'callpoint': u'AfIpv6VrfNeighborAddr'}}, namespace='urn:brocade.com:mgmt:brocade-bgp', defining_module='brocade-bgp', yang_type='list', is_config=True)

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
      return [u'rbridge-id', u'router', u'router-bgp', u'address-family', u'ipv6', u'ipv6-unicast', u'af-ipv6-vrf', u'neighbor', u'af-ipv6-vrf-neighbor-address-holder']

  def _rest_path(self):
    if hasattr(self, "_parent"):
      if self._rest_name:
        return self._parent._rest_path()+[self._rest_name]
      else:
        return self._parent._rest_path()
    else:
      return [u'rbridge-id', u'router', u'bgp', u'address-family', u'ipv6', u'unicast', u'vrf', u'neighbor']

  def _get_af_ipv6_neighbor_addr(self):
    """
    Getter method for af_ipv6_neighbor_addr, mapped from YANG variable /rbridge_id/router/router_bgp/address_family/ipv6/ipv6_unicast/af_ipv6_vrf/neighbor/af_ipv6_vrf_neighbor_address_holder/af_ipv6_neighbor_addr (list)
    """
    return self.__af_ipv6_neighbor_addr
      
  def _set_af_ipv6_neighbor_addr(self, v, load=False):
    """
    Setter method for af_ipv6_neighbor_addr, mapped from YANG variable /rbridge_id/router/router_bgp/address_family/ipv6/ipv6_unicast/af_ipv6_vrf/neighbor/af_ipv6_vrf_neighbor_address_holder/af_ipv6_neighbor_addr (list)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_af_ipv6_neighbor_addr is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_af_ipv6_neighbor_addr() directly.
    """
    if hasattr(v, "_utype"):
      v = v._utype(v)
    try:
      t = YANGDynClass(v,base=YANGListType("af_ipv6_neighbor_address",af_ipv6_neighbor_addr.af_ipv6_neighbor_addr, yang_name="af-ipv6-neighbor-addr", rest_name="", parent=self, is_container='list', user_ordered=False, path_helper=self._path_helper, yang_keys='af-ipv6-neighbor-address', extensions={u'tailf-common': {u'cli-no-key-completion': None, u'cli-suppress-mode': None, u'cli-incomplete-no': None, u'cli-suppress-list-no': None, u'cli-drop-node-name': None, u'cli-suppress-key-abbreviation': None, u'cli-incomplete-command': None, u'callpoint': u'AfIpv6VrfNeighborAddr'}}), is_container='list', yang_name="af-ipv6-neighbor-addr", rest_name="", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'cli-no-key-completion': None, u'cli-suppress-mode': None, u'cli-incomplete-no': None, u'cli-suppress-list-no': None, u'cli-drop-node-name': None, u'cli-suppress-key-abbreviation': None, u'cli-incomplete-command': None, u'callpoint': u'AfIpv6VrfNeighborAddr'}}, namespace='urn:brocade.com:mgmt:brocade-bgp', defining_module='brocade-bgp', yang_type='list', is_config=True)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """af_ipv6_neighbor_addr must be of a type compatible with list""",
          'defined-type': "list",
          'generated-type': """YANGDynClass(base=YANGListType("af_ipv6_neighbor_address",af_ipv6_neighbor_addr.af_ipv6_neighbor_addr, yang_name="af-ipv6-neighbor-addr", rest_name="", parent=self, is_container='list', user_ordered=False, path_helper=self._path_helper, yang_keys='af-ipv6-neighbor-address', extensions={u'tailf-common': {u'cli-no-key-completion': None, u'cli-suppress-mode': None, u'cli-incomplete-no': None, u'cli-suppress-list-no': None, u'cli-drop-node-name': None, u'cli-suppress-key-abbreviation': None, u'cli-incomplete-command': None, u'callpoint': u'AfIpv6VrfNeighborAddr'}}), is_container='list', yang_name="af-ipv6-neighbor-addr", rest_name="", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'cli-no-key-completion': None, u'cli-suppress-mode': None, u'cli-incomplete-no': None, u'cli-suppress-list-no': None, u'cli-drop-node-name': None, u'cli-suppress-key-abbreviation': None, u'cli-incomplete-command': None, u'callpoint': u'AfIpv6VrfNeighborAddr'}}, namespace='urn:brocade.com:mgmt:brocade-bgp', defining_module='brocade-bgp', yang_type='list', is_config=True)""",
        })

    self.__af_ipv6_neighbor_addr = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_af_ipv6_neighbor_addr(self):
    self.__af_ipv6_neighbor_addr = YANGDynClass(base=YANGListType("af_ipv6_neighbor_address",af_ipv6_neighbor_addr.af_ipv6_neighbor_addr, yang_name="af-ipv6-neighbor-addr", rest_name="", parent=self, is_container='list', user_ordered=False, path_helper=self._path_helper, yang_keys='af-ipv6-neighbor-address', extensions={u'tailf-common': {u'cli-no-key-completion': None, u'cli-suppress-mode': None, u'cli-incomplete-no': None, u'cli-suppress-list-no': None, u'cli-drop-node-name': None, u'cli-suppress-key-abbreviation': None, u'cli-incomplete-command': None, u'callpoint': u'AfIpv6VrfNeighborAddr'}}), is_container='list', yang_name="af-ipv6-neighbor-addr", rest_name="", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'cli-no-key-completion': None, u'cli-suppress-mode': None, u'cli-incomplete-no': None, u'cli-suppress-list-no': None, u'cli-drop-node-name': None, u'cli-suppress-key-abbreviation': None, u'cli-incomplete-command': None, u'callpoint': u'AfIpv6VrfNeighborAddr'}}, namespace='urn:brocade.com:mgmt:brocade-bgp', defining_module='brocade-bgp', yang_type='list', is_config=True)

  af_ipv6_neighbor_addr = __builtin__.property(_get_af_ipv6_neighbor_addr, _set_af_ipv6_neighbor_addr)


  _pyangbind_elements = {'af_ipv6_neighbor_addr': af_ipv6_neighbor_addr, }


