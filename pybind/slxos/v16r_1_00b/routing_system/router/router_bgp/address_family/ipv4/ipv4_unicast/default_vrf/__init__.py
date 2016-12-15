
from operator import attrgetter
import pyangbind.lib.xpathhelper as xpathhelper
from pyangbind.lib.yangtypes import RestrictedPrecisionDecimalType, RestrictedClassType, TypedListType
from pyangbind.lib.yangtypes import YANGBool, YANGListType, YANGDynClass, ReferenceType
from pyangbind.lib.base import PybindBase
from decimal import Decimal
from bitarray import bitarray
import __builtin__
import af_ipv4_uc_and_vrf_cmds_call_point_holder
import static_network
import aggregate_address
import network
import neighbor
import af_common_cmds_holder
import next_hop_mpls
class default_vrf(PybindBase):
  """
  This class was auto-generated by the PythonClass plugin for PYANG
  from YANG module brocade-common-def - based on the path /routing-system/router/router-bgp/address-family/ipv4/ipv4-unicast/default-vrf. Each member element of
  the container is represented as a class variable - with a specific
  YANG type.
  """
  __slots__ = ('_pybind_generated_by', '_path_helper', '_yang_name', '_rest_name', '_extmethods', '__default_vrf_selected','__af_ipv4_uc_and_vrf_cmds_call_point_holder','__static_network','__aggregate_address','__network','__neighbor','__af_common_cmds_holder','__next_hop_recursion','__next_hop_mpls',)

  _yang_name = 'default-vrf'
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
    self.__network = YANGDynClass(base=YANGListType("network_ipv4_address",network.network, yang_name="network", rest_name="network", parent=self, is_container='list', user_ordered=False, path_helper=self._path_helper, yang_keys='network-ipv4-address', extensions={u'tailf-common': {u'info': u'Specify a network to announce via BGP', u'cli-no-key-completion': None, u'cli-suppress-mode': None, u'cli-suppress-list-no': None, u'cli-suppress-key-abbreviation': None, u'callpoint': u'AfIpv4Network'}}), is_container='list', yang_name="network", rest_name="network", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'info': u'Specify a network to announce via BGP', u'cli-no-key-completion': None, u'cli-suppress-mode': None, u'cli-suppress-list-no': None, u'cli-suppress-key-abbreviation': None, u'callpoint': u'AfIpv4Network'}}, namespace='urn:brocade.com:mgmt:brocade-bgp', defining_module='brocade-bgp', yang_type='list', is_config=True)
    self.__aggregate_address = YANGDynClass(base=YANGListType("aggregate_ip_prefix",aggregate_address.aggregate_address, yang_name="aggregate-address", rest_name="aggregate-address", parent=self, is_container='list', user_ordered=False, path_helper=self._path_helper, yang_keys='aggregate-ip-prefix', extensions={u'tailf-common': {u'info': u'Configure BGP aggregate entries', u'cli-no-key-completion': None, u'cli-suppress-mode': None, u'cli-suppress-list-no': None, u'cli-suppress-key-abbreviation': None, u'callpoint': u'AggregateIpv4Address'}}), is_container='list', yang_name="aggregate-address", rest_name="aggregate-address", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'info': u'Configure BGP aggregate entries', u'cli-no-key-completion': None, u'cli-suppress-mode': None, u'cli-suppress-list-no': None, u'cli-suppress-key-abbreviation': None, u'callpoint': u'AggregateIpv4Address'}}, namespace='urn:brocade.com:mgmt:brocade-bgp', defining_module='brocade-bgp', yang_type='list', is_config=True)
    self.__default_vrf_selected = YANGDynClass(base=YANGBool, is_leaf=True, yang_name="default-vrf-selected", rest_name="", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'cli-drop-node-name': None, u'cli-full-no': None}}, namespace='urn:brocade.com:mgmt:brocade-bgp', defining_module='brocade-bgp', yang_type='empty', is_config=True)
    self.__af_ipv4_uc_and_vrf_cmds_call_point_holder = YANGDynClass(base=af_ipv4_uc_and_vrf_cmds_call_point_holder.af_ipv4_uc_and_vrf_cmds_call_point_holder, is_container='container', yang_name="af-ipv4-uc-and-vrf-cmds-call-point-holder", rest_name="", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'cli-drop-node-name': None, u'callpoint': u'AfIpv4Ucast'}}, namespace='urn:brocade.com:mgmt:brocade-bgp', defining_module='brocade-bgp', yang_type='container', is_config=True)
    self.__neighbor = YANGDynClass(base=neighbor.neighbor, is_container='container', yang_name="neighbor", rest_name="neighbor", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'info': u'Specify a neighbor router', u'cli-incomplete-no': None}}, namespace='urn:brocade.com:mgmt:brocade-bgp', defining_module='brocade-bgp', yang_type='container', is_config=True)
    self.__next_hop_mpls = YANGDynClass(base=next_hop_mpls.next_hop_mpls, is_container='container', yang_name="next-hop-mpls", rest_name="next-hop-mpls", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'info': u'Changes for IPoMPLS route download, pkt path.'}}, namespace='urn:brocade.com:mgmt:brocade-bgp', defining_module='brocade-bgp', yang_type='container', is_config=True)
    self.__next_hop_recursion = YANGDynClass(base=YANGBool, is_leaf=True, yang_name="next-hop-recursion", rest_name="next-hop-recursion", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'info': u'Perform next-hop recursive lookup for BGP route', u'callpoint': u'AfIpv4Ucast'}}, namespace='urn:brocade.com:mgmt:brocade-bgp', defining_module='brocade-bgp', yang_type='empty', is_config=True)
    self.__af_common_cmds_holder = YANGDynClass(base=af_common_cmds_holder.af_common_cmds_holder, is_container='container', yang_name="af-common-cmds-holder", rest_name="", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'cli-drop-node-name': None, u'callpoint': u'AfIpv4Ucast'}}, namespace='urn:brocade.com:mgmt:brocade-bgp', defining_module='brocade-bgp', yang_type='container', is_config=True)
    self.__static_network = YANGDynClass(base=YANGListType("static_network_address",static_network.static_network, yang_name="static-network", rest_name="static-network", parent=self, is_container='list', user_ordered=False, path_helper=self._path_helper, yang_keys='static-network-address', extensions={u'tailf-common': {u'info': u'Special network that do not depends on IGP and always treat as best route in BGP', u'cli-no-key-completion': None, u'cli-suppress-mode': None, u'cli-suppress-list-no': None, u'cli-suppress-key-abbreviation': None, u'callpoint': u'AfStaticNetwork'}}), is_container='list', yang_name="static-network", rest_name="static-network", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'info': u'Special network that do not depends on IGP and always treat as best route in BGP', u'cli-no-key-completion': None, u'cli-suppress-mode': None, u'cli-suppress-list-no': None, u'cli-suppress-key-abbreviation': None, u'callpoint': u'AfStaticNetwork'}}, namespace='urn:brocade.com:mgmt:brocade-bgp', defining_module='brocade-bgp', yang_type='list', is_config=True)

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
      return [u'routing-system', u'router', u'router-bgp', u'address-family', u'ipv4', u'ipv4-unicast', u'default-vrf']

  def _rest_path(self):
    if hasattr(self, "_parent"):
      if self._rest_name:
        return self._parent._rest_path()+[self._rest_name]
      else:
        return self._parent._rest_path()
    else:
      return [u'router', u'bgp', u'address-family', u'ipv4', u'unicast']

  def _get_default_vrf_selected(self):
    """
    Getter method for default_vrf_selected, mapped from YANG variable /routing_system/router/router_bgp/address_family/ipv4/ipv4_unicast/default_vrf/default_vrf_selected (empty)
    """
    return self.__default_vrf_selected
      
  def _set_default_vrf_selected(self, v, load=False):
    """
    Setter method for default_vrf_selected, mapped from YANG variable /routing_system/router/router_bgp/address_family/ipv4/ipv4_unicast/default_vrf/default_vrf_selected (empty)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_default_vrf_selected is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_default_vrf_selected() directly.
    """
    if hasattr(v, "_utype"):
      v = v._utype(v)
    try:
      t = YANGDynClass(v,base=YANGBool, is_leaf=True, yang_name="default-vrf-selected", rest_name="", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'cli-drop-node-name': None, u'cli-full-no': None}}, namespace='urn:brocade.com:mgmt:brocade-bgp', defining_module='brocade-bgp', yang_type='empty', is_config=True)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """default_vrf_selected must be of a type compatible with empty""",
          'defined-type': "empty",
          'generated-type': """YANGDynClass(base=YANGBool, is_leaf=True, yang_name="default-vrf-selected", rest_name="", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'cli-drop-node-name': None, u'cli-full-no': None}}, namespace='urn:brocade.com:mgmt:brocade-bgp', defining_module='brocade-bgp', yang_type='empty', is_config=True)""",
        })

    self.__default_vrf_selected = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_default_vrf_selected(self):
    self.__default_vrf_selected = YANGDynClass(base=YANGBool, is_leaf=True, yang_name="default-vrf-selected", rest_name="", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'cli-drop-node-name': None, u'cli-full-no': None}}, namespace='urn:brocade.com:mgmt:brocade-bgp', defining_module='brocade-bgp', yang_type='empty', is_config=True)


  def _get_af_ipv4_uc_and_vrf_cmds_call_point_holder(self):
    """
    Getter method for af_ipv4_uc_and_vrf_cmds_call_point_holder, mapped from YANG variable /routing_system/router/router_bgp/address_family/ipv4/ipv4_unicast/default_vrf/af_ipv4_uc_and_vrf_cmds_call_point_holder (container)
    """
    return self.__af_ipv4_uc_and_vrf_cmds_call_point_holder
      
  def _set_af_ipv4_uc_and_vrf_cmds_call_point_holder(self, v, load=False):
    """
    Setter method for af_ipv4_uc_and_vrf_cmds_call_point_holder, mapped from YANG variable /routing_system/router/router_bgp/address_family/ipv4/ipv4_unicast/default_vrf/af_ipv4_uc_and_vrf_cmds_call_point_holder (container)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_af_ipv4_uc_and_vrf_cmds_call_point_holder is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_af_ipv4_uc_and_vrf_cmds_call_point_holder() directly.
    """
    if hasattr(v, "_utype"):
      v = v._utype(v)
    try:
      t = YANGDynClass(v,base=af_ipv4_uc_and_vrf_cmds_call_point_holder.af_ipv4_uc_and_vrf_cmds_call_point_holder, is_container='container', yang_name="af-ipv4-uc-and-vrf-cmds-call-point-holder", rest_name="", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'cli-drop-node-name': None, u'callpoint': u'AfIpv4Ucast'}}, namespace='urn:brocade.com:mgmt:brocade-bgp', defining_module='brocade-bgp', yang_type='container', is_config=True)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """af_ipv4_uc_and_vrf_cmds_call_point_holder must be of a type compatible with container""",
          'defined-type': "container",
          'generated-type': """YANGDynClass(base=af_ipv4_uc_and_vrf_cmds_call_point_holder.af_ipv4_uc_and_vrf_cmds_call_point_holder, is_container='container', yang_name="af-ipv4-uc-and-vrf-cmds-call-point-holder", rest_name="", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'cli-drop-node-name': None, u'callpoint': u'AfIpv4Ucast'}}, namespace='urn:brocade.com:mgmt:brocade-bgp', defining_module='brocade-bgp', yang_type='container', is_config=True)""",
        })

    self.__af_ipv4_uc_and_vrf_cmds_call_point_holder = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_af_ipv4_uc_and_vrf_cmds_call_point_holder(self):
    self.__af_ipv4_uc_and_vrf_cmds_call_point_holder = YANGDynClass(base=af_ipv4_uc_and_vrf_cmds_call_point_holder.af_ipv4_uc_and_vrf_cmds_call_point_holder, is_container='container', yang_name="af-ipv4-uc-and-vrf-cmds-call-point-holder", rest_name="", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'cli-drop-node-name': None, u'callpoint': u'AfIpv4Ucast'}}, namespace='urn:brocade.com:mgmt:brocade-bgp', defining_module='brocade-bgp', yang_type='container', is_config=True)


  def _get_static_network(self):
    """
    Getter method for static_network, mapped from YANG variable /routing_system/router/router_bgp/address_family/ipv4/ipv4_unicast/default_vrf/static_network (list)
    """
    return self.__static_network
      
  def _set_static_network(self, v, load=False):
    """
    Setter method for static_network, mapped from YANG variable /routing_system/router/router_bgp/address_family/ipv4/ipv4_unicast/default_vrf/static_network (list)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_static_network is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_static_network() directly.
    """
    if hasattr(v, "_utype"):
      v = v._utype(v)
    try:
      t = YANGDynClass(v,base=YANGListType("static_network_address",static_network.static_network, yang_name="static-network", rest_name="static-network", parent=self, is_container='list', user_ordered=False, path_helper=self._path_helper, yang_keys='static-network-address', extensions={u'tailf-common': {u'info': u'Special network that do not depends on IGP and always treat as best route in BGP', u'cli-no-key-completion': None, u'cli-suppress-mode': None, u'cli-suppress-list-no': None, u'cli-suppress-key-abbreviation': None, u'callpoint': u'AfStaticNetwork'}}), is_container='list', yang_name="static-network", rest_name="static-network", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'info': u'Special network that do not depends on IGP and always treat as best route in BGP', u'cli-no-key-completion': None, u'cli-suppress-mode': None, u'cli-suppress-list-no': None, u'cli-suppress-key-abbreviation': None, u'callpoint': u'AfStaticNetwork'}}, namespace='urn:brocade.com:mgmt:brocade-bgp', defining_module='brocade-bgp', yang_type='list', is_config=True)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """static_network must be of a type compatible with list""",
          'defined-type': "list",
          'generated-type': """YANGDynClass(base=YANGListType("static_network_address",static_network.static_network, yang_name="static-network", rest_name="static-network", parent=self, is_container='list', user_ordered=False, path_helper=self._path_helper, yang_keys='static-network-address', extensions={u'tailf-common': {u'info': u'Special network that do not depends on IGP and always treat as best route in BGP', u'cli-no-key-completion': None, u'cli-suppress-mode': None, u'cli-suppress-list-no': None, u'cli-suppress-key-abbreviation': None, u'callpoint': u'AfStaticNetwork'}}), is_container='list', yang_name="static-network", rest_name="static-network", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'info': u'Special network that do not depends on IGP and always treat as best route in BGP', u'cli-no-key-completion': None, u'cli-suppress-mode': None, u'cli-suppress-list-no': None, u'cli-suppress-key-abbreviation': None, u'callpoint': u'AfStaticNetwork'}}, namespace='urn:brocade.com:mgmt:brocade-bgp', defining_module='brocade-bgp', yang_type='list', is_config=True)""",
        })

    self.__static_network = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_static_network(self):
    self.__static_network = YANGDynClass(base=YANGListType("static_network_address",static_network.static_network, yang_name="static-network", rest_name="static-network", parent=self, is_container='list', user_ordered=False, path_helper=self._path_helper, yang_keys='static-network-address', extensions={u'tailf-common': {u'info': u'Special network that do not depends on IGP and always treat as best route in BGP', u'cli-no-key-completion': None, u'cli-suppress-mode': None, u'cli-suppress-list-no': None, u'cli-suppress-key-abbreviation': None, u'callpoint': u'AfStaticNetwork'}}), is_container='list', yang_name="static-network", rest_name="static-network", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'info': u'Special network that do not depends on IGP and always treat as best route in BGP', u'cli-no-key-completion': None, u'cli-suppress-mode': None, u'cli-suppress-list-no': None, u'cli-suppress-key-abbreviation': None, u'callpoint': u'AfStaticNetwork'}}, namespace='urn:brocade.com:mgmt:brocade-bgp', defining_module='brocade-bgp', yang_type='list', is_config=True)


  def _get_aggregate_address(self):
    """
    Getter method for aggregate_address, mapped from YANG variable /routing_system/router/router_bgp/address_family/ipv4/ipv4_unicast/default_vrf/aggregate_address (list)
    """
    return self.__aggregate_address
      
  def _set_aggregate_address(self, v, load=False):
    """
    Setter method for aggregate_address, mapped from YANG variable /routing_system/router/router_bgp/address_family/ipv4/ipv4_unicast/default_vrf/aggregate_address (list)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_aggregate_address is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_aggregate_address() directly.
    """
    if hasattr(v, "_utype"):
      v = v._utype(v)
    try:
      t = YANGDynClass(v,base=YANGListType("aggregate_ip_prefix",aggregate_address.aggregate_address, yang_name="aggregate-address", rest_name="aggregate-address", parent=self, is_container='list', user_ordered=False, path_helper=self._path_helper, yang_keys='aggregate-ip-prefix', extensions={u'tailf-common': {u'info': u'Configure BGP aggregate entries', u'cli-no-key-completion': None, u'cli-suppress-mode': None, u'cli-suppress-list-no': None, u'cli-suppress-key-abbreviation': None, u'callpoint': u'AggregateIpv4Address'}}), is_container='list', yang_name="aggregate-address", rest_name="aggregate-address", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'info': u'Configure BGP aggregate entries', u'cli-no-key-completion': None, u'cli-suppress-mode': None, u'cli-suppress-list-no': None, u'cli-suppress-key-abbreviation': None, u'callpoint': u'AggregateIpv4Address'}}, namespace='urn:brocade.com:mgmt:brocade-bgp', defining_module='brocade-bgp', yang_type='list', is_config=True)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """aggregate_address must be of a type compatible with list""",
          'defined-type': "list",
          'generated-type': """YANGDynClass(base=YANGListType("aggregate_ip_prefix",aggregate_address.aggregate_address, yang_name="aggregate-address", rest_name="aggregate-address", parent=self, is_container='list', user_ordered=False, path_helper=self._path_helper, yang_keys='aggregate-ip-prefix', extensions={u'tailf-common': {u'info': u'Configure BGP aggregate entries', u'cli-no-key-completion': None, u'cli-suppress-mode': None, u'cli-suppress-list-no': None, u'cli-suppress-key-abbreviation': None, u'callpoint': u'AggregateIpv4Address'}}), is_container='list', yang_name="aggregate-address", rest_name="aggregate-address", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'info': u'Configure BGP aggregate entries', u'cli-no-key-completion': None, u'cli-suppress-mode': None, u'cli-suppress-list-no': None, u'cli-suppress-key-abbreviation': None, u'callpoint': u'AggregateIpv4Address'}}, namespace='urn:brocade.com:mgmt:brocade-bgp', defining_module='brocade-bgp', yang_type='list', is_config=True)""",
        })

    self.__aggregate_address = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_aggregate_address(self):
    self.__aggregate_address = YANGDynClass(base=YANGListType("aggregate_ip_prefix",aggregate_address.aggregate_address, yang_name="aggregate-address", rest_name="aggregate-address", parent=self, is_container='list', user_ordered=False, path_helper=self._path_helper, yang_keys='aggregate-ip-prefix', extensions={u'tailf-common': {u'info': u'Configure BGP aggregate entries', u'cli-no-key-completion': None, u'cli-suppress-mode': None, u'cli-suppress-list-no': None, u'cli-suppress-key-abbreviation': None, u'callpoint': u'AggregateIpv4Address'}}), is_container='list', yang_name="aggregate-address", rest_name="aggregate-address", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'info': u'Configure BGP aggregate entries', u'cli-no-key-completion': None, u'cli-suppress-mode': None, u'cli-suppress-list-no': None, u'cli-suppress-key-abbreviation': None, u'callpoint': u'AggregateIpv4Address'}}, namespace='urn:brocade.com:mgmt:brocade-bgp', defining_module='brocade-bgp', yang_type='list', is_config=True)


  def _get_network(self):
    """
    Getter method for network, mapped from YANG variable /routing_system/router/router_bgp/address_family/ipv4/ipv4_unicast/default_vrf/network (list)
    """
    return self.__network
      
  def _set_network(self, v, load=False):
    """
    Setter method for network, mapped from YANG variable /routing_system/router/router_bgp/address_family/ipv4/ipv4_unicast/default_vrf/network (list)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_network is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_network() directly.
    """
    if hasattr(v, "_utype"):
      v = v._utype(v)
    try:
      t = YANGDynClass(v,base=YANGListType("network_ipv4_address",network.network, yang_name="network", rest_name="network", parent=self, is_container='list', user_ordered=False, path_helper=self._path_helper, yang_keys='network-ipv4-address', extensions={u'tailf-common': {u'info': u'Specify a network to announce via BGP', u'cli-no-key-completion': None, u'cli-suppress-mode': None, u'cli-suppress-list-no': None, u'cli-suppress-key-abbreviation': None, u'callpoint': u'AfIpv4Network'}}), is_container='list', yang_name="network", rest_name="network", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'info': u'Specify a network to announce via BGP', u'cli-no-key-completion': None, u'cli-suppress-mode': None, u'cli-suppress-list-no': None, u'cli-suppress-key-abbreviation': None, u'callpoint': u'AfIpv4Network'}}, namespace='urn:brocade.com:mgmt:brocade-bgp', defining_module='brocade-bgp', yang_type='list', is_config=True)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """network must be of a type compatible with list""",
          'defined-type': "list",
          'generated-type': """YANGDynClass(base=YANGListType("network_ipv4_address",network.network, yang_name="network", rest_name="network", parent=self, is_container='list', user_ordered=False, path_helper=self._path_helper, yang_keys='network-ipv4-address', extensions={u'tailf-common': {u'info': u'Specify a network to announce via BGP', u'cli-no-key-completion': None, u'cli-suppress-mode': None, u'cli-suppress-list-no': None, u'cli-suppress-key-abbreviation': None, u'callpoint': u'AfIpv4Network'}}), is_container='list', yang_name="network", rest_name="network", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'info': u'Specify a network to announce via BGP', u'cli-no-key-completion': None, u'cli-suppress-mode': None, u'cli-suppress-list-no': None, u'cli-suppress-key-abbreviation': None, u'callpoint': u'AfIpv4Network'}}, namespace='urn:brocade.com:mgmt:brocade-bgp', defining_module='brocade-bgp', yang_type='list', is_config=True)""",
        })

    self.__network = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_network(self):
    self.__network = YANGDynClass(base=YANGListType("network_ipv4_address",network.network, yang_name="network", rest_name="network", parent=self, is_container='list', user_ordered=False, path_helper=self._path_helper, yang_keys='network-ipv4-address', extensions={u'tailf-common': {u'info': u'Specify a network to announce via BGP', u'cli-no-key-completion': None, u'cli-suppress-mode': None, u'cli-suppress-list-no': None, u'cli-suppress-key-abbreviation': None, u'callpoint': u'AfIpv4Network'}}), is_container='list', yang_name="network", rest_name="network", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'info': u'Specify a network to announce via BGP', u'cli-no-key-completion': None, u'cli-suppress-mode': None, u'cli-suppress-list-no': None, u'cli-suppress-key-abbreviation': None, u'callpoint': u'AfIpv4Network'}}, namespace='urn:brocade.com:mgmt:brocade-bgp', defining_module='brocade-bgp', yang_type='list', is_config=True)


  def _get_neighbor(self):
    """
    Getter method for neighbor, mapped from YANG variable /routing_system/router/router_bgp/address_family/ipv4/ipv4_unicast/default_vrf/neighbor (container)
    """
    return self.__neighbor
      
  def _set_neighbor(self, v, load=False):
    """
    Setter method for neighbor, mapped from YANG variable /routing_system/router/router_bgp/address_family/ipv4/ipv4_unicast/default_vrf/neighbor (container)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_neighbor is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_neighbor() directly.
    """
    if hasattr(v, "_utype"):
      v = v._utype(v)
    try:
      t = YANGDynClass(v,base=neighbor.neighbor, is_container='container', yang_name="neighbor", rest_name="neighbor", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'info': u'Specify a neighbor router', u'cli-incomplete-no': None}}, namespace='urn:brocade.com:mgmt:brocade-bgp', defining_module='brocade-bgp', yang_type='container', is_config=True)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """neighbor must be of a type compatible with container""",
          'defined-type': "container",
          'generated-type': """YANGDynClass(base=neighbor.neighbor, is_container='container', yang_name="neighbor", rest_name="neighbor", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'info': u'Specify a neighbor router', u'cli-incomplete-no': None}}, namespace='urn:brocade.com:mgmt:brocade-bgp', defining_module='brocade-bgp', yang_type='container', is_config=True)""",
        })

    self.__neighbor = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_neighbor(self):
    self.__neighbor = YANGDynClass(base=neighbor.neighbor, is_container='container', yang_name="neighbor", rest_name="neighbor", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'info': u'Specify a neighbor router', u'cli-incomplete-no': None}}, namespace='urn:brocade.com:mgmt:brocade-bgp', defining_module='brocade-bgp', yang_type='container', is_config=True)


  def _get_af_common_cmds_holder(self):
    """
    Getter method for af_common_cmds_holder, mapped from YANG variable /routing_system/router/router_bgp/address_family/ipv4/ipv4_unicast/default_vrf/af_common_cmds_holder (container)
    """
    return self.__af_common_cmds_holder
      
  def _set_af_common_cmds_holder(self, v, load=False):
    """
    Setter method for af_common_cmds_holder, mapped from YANG variable /routing_system/router/router_bgp/address_family/ipv4/ipv4_unicast/default_vrf/af_common_cmds_holder (container)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_af_common_cmds_holder is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_af_common_cmds_holder() directly.
    """
    if hasattr(v, "_utype"):
      v = v._utype(v)
    try:
      t = YANGDynClass(v,base=af_common_cmds_holder.af_common_cmds_holder, is_container='container', yang_name="af-common-cmds-holder", rest_name="", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'cli-drop-node-name': None, u'callpoint': u'AfIpv4Ucast'}}, namespace='urn:brocade.com:mgmt:brocade-bgp', defining_module='brocade-bgp', yang_type='container', is_config=True)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """af_common_cmds_holder must be of a type compatible with container""",
          'defined-type': "container",
          'generated-type': """YANGDynClass(base=af_common_cmds_holder.af_common_cmds_holder, is_container='container', yang_name="af-common-cmds-holder", rest_name="", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'cli-drop-node-name': None, u'callpoint': u'AfIpv4Ucast'}}, namespace='urn:brocade.com:mgmt:brocade-bgp', defining_module='brocade-bgp', yang_type='container', is_config=True)""",
        })

    self.__af_common_cmds_holder = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_af_common_cmds_holder(self):
    self.__af_common_cmds_holder = YANGDynClass(base=af_common_cmds_holder.af_common_cmds_holder, is_container='container', yang_name="af-common-cmds-holder", rest_name="", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'cli-drop-node-name': None, u'callpoint': u'AfIpv4Ucast'}}, namespace='urn:brocade.com:mgmt:brocade-bgp', defining_module='brocade-bgp', yang_type='container', is_config=True)


  def _get_next_hop_recursion(self):
    """
    Getter method for next_hop_recursion, mapped from YANG variable /routing_system/router/router_bgp/address_family/ipv4/ipv4_unicast/default_vrf/next_hop_recursion (empty)
    """
    return self.__next_hop_recursion
      
  def _set_next_hop_recursion(self, v, load=False):
    """
    Setter method for next_hop_recursion, mapped from YANG variable /routing_system/router/router_bgp/address_family/ipv4/ipv4_unicast/default_vrf/next_hop_recursion (empty)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_next_hop_recursion is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_next_hop_recursion() directly.
    """
    if hasattr(v, "_utype"):
      v = v._utype(v)
    try:
      t = YANGDynClass(v,base=YANGBool, is_leaf=True, yang_name="next-hop-recursion", rest_name="next-hop-recursion", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'info': u'Perform next-hop recursive lookup for BGP route', u'callpoint': u'AfIpv4Ucast'}}, namespace='urn:brocade.com:mgmt:brocade-bgp', defining_module='brocade-bgp', yang_type='empty', is_config=True)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """next_hop_recursion must be of a type compatible with empty""",
          'defined-type': "empty",
          'generated-type': """YANGDynClass(base=YANGBool, is_leaf=True, yang_name="next-hop-recursion", rest_name="next-hop-recursion", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'info': u'Perform next-hop recursive lookup for BGP route', u'callpoint': u'AfIpv4Ucast'}}, namespace='urn:brocade.com:mgmt:brocade-bgp', defining_module='brocade-bgp', yang_type='empty', is_config=True)""",
        })

    self.__next_hop_recursion = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_next_hop_recursion(self):
    self.__next_hop_recursion = YANGDynClass(base=YANGBool, is_leaf=True, yang_name="next-hop-recursion", rest_name="next-hop-recursion", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'info': u'Perform next-hop recursive lookup for BGP route', u'callpoint': u'AfIpv4Ucast'}}, namespace='urn:brocade.com:mgmt:brocade-bgp', defining_module='brocade-bgp', yang_type='empty', is_config=True)


  def _get_next_hop_mpls(self):
    """
    Getter method for next_hop_mpls, mapped from YANG variable /routing_system/router/router_bgp/address_family/ipv4/ipv4_unicast/default_vrf/next_hop_mpls (container)
    """
    return self.__next_hop_mpls
      
  def _set_next_hop_mpls(self, v, load=False):
    """
    Setter method for next_hop_mpls, mapped from YANG variable /routing_system/router/router_bgp/address_family/ipv4/ipv4_unicast/default_vrf/next_hop_mpls (container)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_next_hop_mpls is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_next_hop_mpls() directly.
    """
    if hasattr(v, "_utype"):
      v = v._utype(v)
    try:
      t = YANGDynClass(v,base=next_hop_mpls.next_hop_mpls, is_container='container', yang_name="next-hop-mpls", rest_name="next-hop-mpls", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'info': u'Changes for IPoMPLS route download, pkt path.'}}, namespace='urn:brocade.com:mgmt:brocade-bgp', defining_module='brocade-bgp', yang_type='container', is_config=True)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """next_hop_mpls must be of a type compatible with container""",
          'defined-type': "container",
          'generated-type': """YANGDynClass(base=next_hop_mpls.next_hop_mpls, is_container='container', yang_name="next-hop-mpls", rest_name="next-hop-mpls", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'info': u'Changes for IPoMPLS route download, pkt path.'}}, namespace='urn:brocade.com:mgmt:brocade-bgp', defining_module='brocade-bgp', yang_type='container', is_config=True)""",
        })

    self.__next_hop_mpls = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_next_hop_mpls(self):
    self.__next_hop_mpls = YANGDynClass(base=next_hop_mpls.next_hop_mpls, is_container='container', yang_name="next-hop-mpls", rest_name="next-hop-mpls", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'info': u'Changes for IPoMPLS route download, pkt path.'}}, namespace='urn:brocade.com:mgmt:brocade-bgp', defining_module='brocade-bgp', yang_type='container', is_config=True)

  default_vrf_selected = __builtin__.property(_get_default_vrf_selected, _set_default_vrf_selected)
  af_ipv4_uc_and_vrf_cmds_call_point_holder = __builtin__.property(_get_af_ipv4_uc_and_vrf_cmds_call_point_holder, _set_af_ipv4_uc_and_vrf_cmds_call_point_holder)
  static_network = __builtin__.property(_get_static_network, _set_static_network)
  aggregate_address = __builtin__.property(_get_aggregate_address, _set_aggregate_address)
  network = __builtin__.property(_get_network, _set_network)
  neighbor = __builtin__.property(_get_neighbor, _set_neighbor)
  af_common_cmds_holder = __builtin__.property(_get_af_common_cmds_holder, _set_af_common_cmds_holder)
  next_hop_recursion = __builtin__.property(_get_next_hop_recursion, _set_next_hop_recursion)
  next_hop_mpls = __builtin__.property(_get_next_hop_mpls, _set_next_hop_mpls)


  _pyangbind_elements = {'default_vrf_selected': default_vrf_selected, 'af_ipv4_uc_and_vrf_cmds_call_point_holder': af_ipv4_uc_and_vrf_cmds_call_point_holder, 'static_network': static_network, 'aggregate_address': aggregate_address, 'network': network, 'neighbor': neighbor, 'af_common_cmds_holder': af_common_cmds_holder, 'next_hop_recursion': next_hop_recursion, 'next_hop_mpls': next_hop_mpls, }


