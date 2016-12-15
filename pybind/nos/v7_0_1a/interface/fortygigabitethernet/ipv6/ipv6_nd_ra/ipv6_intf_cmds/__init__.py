
from operator import attrgetter
import pyangbind.lib.xpathhelper as xpathhelper
from pyangbind.lib.yangtypes import RestrictedPrecisionDecimalType, RestrictedClassType, TypedListType
from pyangbind.lib.yangtypes import YANGBool, YANGListType, YANGDynClass, ReferenceType
from pyangbind.lib.base import PybindBase
from decimal import Decimal
from bitarray import bitarray
import __builtin__
import nd
import neighbor
class ipv6_intf_cmds(PybindBase):
  """
  This class was auto-generated by the PythonClass plugin for PYANG
  from YANG module brocade-interface - based on the path /interface/fortygigabitethernet/ipv6/ipv6-nd-ra/ipv6-intf-cmds. Each member element of
  the container is represented as a class variable - with a specific
  YANG type.
  """
  __slots__ = ('_pybind_generated_by', '_path_helper', '_yang_name', '_rest_name', '_extmethods', '__vrrp_suppress_interface_ra','__nd','__neighbor',)

  _yang_name = 'ipv6-intf-cmds'
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
    self.__nd = YANGDynClass(base=nd.nd, is_container='container', yang_name="nd", rest_name="nd", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'info': u'Neighbor Discovery commands', u'cli-incomplete-no': None, u'sort-priority': u'116'}}, namespace='urn:brocade.com:mgmt:brocade-ipv6-nd-ra', defining_module='brocade-ipv6-nd-ra', yang_type='container', is_config=True)
    self.__neighbor = YANGDynClass(base=YANGListType("ipv6_address",neighbor.neighbor, yang_name="neighbor", rest_name="neighbor", parent=self, is_container='list', user_ordered=False, path_helper=self._path_helper, yang_keys='ipv6-address', extensions={u'tailf-common': {u'info': u'Neighbor Discovery commands', u'cli-no-key-completion': None, u'cli-suppress-mode': None, u'cli-suppress-list-no': None, u'cli-suppress-key-abbreviation': None, u'cli-incomplete-command': None, u'callpoint': u'IpV6NdRaNeighborPhyIntf'}}), is_container='list', yang_name="neighbor", rest_name="neighbor", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'info': u'Neighbor Discovery commands', u'cli-no-key-completion': None, u'cli-suppress-mode': None, u'cli-suppress-list-no': None, u'cli-suppress-key-abbreviation': None, u'cli-incomplete-command': None, u'callpoint': u'IpV6NdRaNeighborPhyIntf'}}, namespace='urn:brocade.com:mgmt:brocade-ipv6-nd-ra', defining_module='brocade-ipv6-nd-ra', yang_type='list', is_config=True)
    self.__vrrp_suppress_interface_ra = YANGDynClass(base=YANGBool, is_leaf=True, yang_name="vrrp-suppress-interface-ra", rest_name="vrrp-suppress-interface-ra", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'cli-full-command': None, u'info': u'Suppress interface RA for vrrpv3'}}, namespace='urn:brocade.com:mgmt:brocade-ipv6-nd-ra', defining_module='brocade-ipv6-nd-ra', yang_type='empty', is_config=True)

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
      return [u'interface', u'fortygigabitethernet', u'ipv6', u'ipv6-nd-ra', u'ipv6-intf-cmds']

  def _rest_path(self):
    if hasattr(self, "_parent"):
      if self._rest_name:
        return self._parent._rest_path()+[self._rest_name]
      else:
        return self._parent._rest_path()
    else:
      return [u'interface', u'FortyGigabitEthernet', u'ipv6']

  def _get_vrrp_suppress_interface_ra(self):
    """
    Getter method for vrrp_suppress_interface_ra, mapped from YANG variable /interface/fortygigabitethernet/ipv6/ipv6_nd_ra/ipv6_intf_cmds/vrrp_suppress_interface_ra (empty)
    """
    return self.__vrrp_suppress_interface_ra
      
  def _set_vrrp_suppress_interface_ra(self, v, load=False):
    """
    Setter method for vrrp_suppress_interface_ra, mapped from YANG variable /interface/fortygigabitethernet/ipv6/ipv6_nd_ra/ipv6_intf_cmds/vrrp_suppress_interface_ra (empty)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_vrrp_suppress_interface_ra is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_vrrp_suppress_interface_ra() directly.
    """
    if hasattr(v, "_utype"):
      v = v._utype(v)
    try:
      t = YANGDynClass(v,base=YANGBool, is_leaf=True, yang_name="vrrp-suppress-interface-ra", rest_name="vrrp-suppress-interface-ra", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'cli-full-command': None, u'info': u'Suppress interface RA for vrrpv3'}}, namespace='urn:brocade.com:mgmt:brocade-ipv6-nd-ra', defining_module='brocade-ipv6-nd-ra', yang_type='empty', is_config=True)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """vrrp_suppress_interface_ra must be of a type compatible with empty""",
          'defined-type': "empty",
          'generated-type': """YANGDynClass(base=YANGBool, is_leaf=True, yang_name="vrrp-suppress-interface-ra", rest_name="vrrp-suppress-interface-ra", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'cli-full-command': None, u'info': u'Suppress interface RA for vrrpv3'}}, namespace='urn:brocade.com:mgmt:brocade-ipv6-nd-ra', defining_module='brocade-ipv6-nd-ra', yang_type='empty', is_config=True)""",
        })

    self.__vrrp_suppress_interface_ra = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_vrrp_suppress_interface_ra(self):
    self.__vrrp_suppress_interface_ra = YANGDynClass(base=YANGBool, is_leaf=True, yang_name="vrrp-suppress-interface-ra", rest_name="vrrp-suppress-interface-ra", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'cli-full-command': None, u'info': u'Suppress interface RA for vrrpv3'}}, namespace='urn:brocade.com:mgmt:brocade-ipv6-nd-ra', defining_module='brocade-ipv6-nd-ra', yang_type='empty', is_config=True)


  def _get_nd(self):
    """
    Getter method for nd, mapped from YANG variable /interface/fortygigabitethernet/ipv6/ipv6_nd_ra/ipv6_intf_cmds/nd (container)
    """
    return self.__nd
      
  def _set_nd(self, v, load=False):
    """
    Setter method for nd, mapped from YANG variable /interface/fortygigabitethernet/ipv6/ipv6_nd_ra/ipv6_intf_cmds/nd (container)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_nd is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_nd() directly.
    """
    if hasattr(v, "_utype"):
      v = v._utype(v)
    try:
      t = YANGDynClass(v,base=nd.nd, is_container='container', yang_name="nd", rest_name="nd", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'info': u'Neighbor Discovery commands', u'cli-incomplete-no': None, u'sort-priority': u'116'}}, namespace='urn:brocade.com:mgmt:brocade-ipv6-nd-ra', defining_module='brocade-ipv6-nd-ra', yang_type='container', is_config=True)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """nd must be of a type compatible with container""",
          'defined-type': "container",
          'generated-type': """YANGDynClass(base=nd.nd, is_container='container', yang_name="nd", rest_name="nd", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'info': u'Neighbor Discovery commands', u'cli-incomplete-no': None, u'sort-priority': u'116'}}, namespace='urn:brocade.com:mgmt:brocade-ipv6-nd-ra', defining_module='brocade-ipv6-nd-ra', yang_type='container', is_config=True)""",
        })

    self.__nd = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_nd(self):
    self.__nd = YANGDynClass(base=nd.nd, is_container='container', yang_name="nd", rest_name="nd", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'info': u'Neighbor Discovery commands', u'cli-incomplete-no': None, u'sort-priority': u'116'}}, namespace='urn:brocade.com:mgmt:brocade-ipv6-nd-ra', defining_module='brocade-ipv6-nd-ra', yang_type='container', is_config=True)


  def _get_neighbor(self):
    """
    Getter method for neighbor, mapped from YANG variable /interface/fortygigabitethernet/ipv6/ipv6_nd_ra/ipv6_intf_cmds/neighbor (list)
    """
    return self.__neighbor
      
  def _set_neighbor(self, v, load=False):
    """
    Setter method for neighbor, mapped from YANG variable /interface/fortygigabitethernet/ipv6/ipv6_nd_ra/ipv6_intf_cmds/neighbor (list)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_neighbor is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_neighbor() directly.
    """
    if hasattr(v, "_utype"):
      v = v._utype(v)
    try:
      t = YANGDynClass(v,base=YANGListType("ipv6_address",neighbor.neighbor, yang_name="neighbor", rest_name="neighbor", parent=self, is_container='list', user_ordered=False, path_helper=self._path_helper, yang_keys='ipv6-address', extensions={u'tailf-common': {u'info': u'Neighbor Discovery commands', u'cli-no-key-completion': None, u'cli-suppress-mode': None, u'cli-suppress-list-no': None, u'cli-suppress-key-abbreviation': None, u'cli-incomplete-command': None, u'callpoint': u'IpV6NdRaNeighborPhyIntf'}}), is_container='list', yang_name="neighbor", rest_name="neighbor", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'info': u'Neighbor Discovery commands', u'cli-no-key-completion': None, u'cli-suppress-mode': None, u'cli-suppress-list-no': None, u'cli-suppress-key-abbreviation': None, u'cli-incomplete-command': None, u'callpoint': u'IpV6NdRaNeighborPhyIntf'}}, namespace='urn:brocade.com:mgmt:brocade-ipv6-nd-ra', defining_module='brocade-ipv6-nd-ra', yang_type='list', is_config=True)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """neighbor must be of a type compatible with list""",
          'defined-type': "list",
          'generated-type': """YANGDynClass(base=YANGListType("ipv6_address",neighbor.neighbor, yang_name="neighbor", rest_name="neighbor", parent=self, is_container='list', user_ordered=False, path_helper=self._path_helper, yang_keys='ipv6-address', extensions={u'tailf-common': {u'info': u'Neighbor Discovery commands', u'cli-no-key-completion': None, u'cli-suppress-mode': None, u'cli-suppress-list-no': None, u'cli-suppress-key-abbreviation': None, u'cli-incomplete-command': None, u'callpoint': u'IpV6NdRaNeighborPhyIntf'}}), is_container='list', yang_name="neighbor", rest_name="neighbor", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'info': u'Neighbor Discovery commands', u'cli-no-key-completion': None, u'cli-suppress-mode': None, u'cli-suppress-list-no': None, u'cli-suppress-key-abbreviation': None, u'cli-incomplete-command': None, u'callpoint': u'IpV6NdRaNeighborPhyIntf'}}, namespace='urn:brocade.com:mgmt:brocade-ipv6-nd-ra', defining_module='brocade-ipv6-nd-ra', yang_type='list', is_config=True)""",
        })

    self.__neighbor = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_neighbor(self):
    self.__neighbor = YANGDynClass(base=YANGListType("ipv6_address",neighbor.neighbor, yang_name="neighbor", rest_name="neighbor", parent=self, is_container='list', user_ordered=False, path_helper=self._path_helper, yang_keys='ipv6-address', extensions={u'tailf-common': {u'info': u'Neighbor Discovery commands', u'cli-no-key-completion': None, u'cli-suppress-mode': None, u'cli-suppress-list-no': None, u'cli-suppress-key-abbreviation': None, u'cli-incomplete-command': None, u'callpoint': u'IpV6NdRaNeighborPhyIntf'}}), is_container='list', yang_name="neighbor", rest_name="neighbor", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'info': u'Neighbor Discovery commands', u'cli-no-key-completion': None, u'cli-suppress-mode': None, u'cli-suppress-list-no': None, u'cli-suppress-key-abbreviation': None, u'cli-incomplete-command': None, u'callpoint': u'IpV6NdRaNeighborPhyIntf'}}, namespace='urn:brocade.com:mgmt:brocade-ipv6-nd-ra', defining_module='brocade-ipv6-nd-ra', yang_type='list', is_config=True)

  vrrp_suppress_interface_ra = __builtin__.property(_get_vrrp_suppress_interface_ra, _set_vrrp_suppress_interface_ra)
  nd = __builtin__.property(_get_nd, _set_nd)
  neighbor = __builtin__.property(_get_neighbor, _set_neighbor)


  _pyangbind_elements = {'vrrp_suppress_interface_ra': vrrp_suppress_interface_ra, 'nd': nd, 'neighbor': neighbor, }


