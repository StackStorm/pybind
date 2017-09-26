
from operator import attrgetter
import pyangbind.lib.xpathhelper as xpathhelper
from pyangbind.lib.yangtypes import RestrictedPrecisionDecimalType, RestrictedClassType, TypedListType
from pyangbind.lib.yangtypes import YANGBool, YANGListType, YANGDynClass, ReferenceType
from pyangbind.lib.base import PybindBase
from decimal import Decimal
from bitarray import bitarray
import __builtin__
class extended_community(PybindBase):
  """
  This class was auto-generated by the PythonClass plugin for PYANG
  from YANG module brocade-common-def - based on the path /routing-system/router/router-bgp/address-family/vpnv6/vpnv6-unicast/af-vpn-neighbor-peergroup-holder/af-vpn-neighbor-peergroup/af-neighbor-capability/orf/extended-community. Each member element of
  the container is represented as a class variable - with a specific
  YANG type.
  """
  __slots__ = ('_pybind_generated_by', '_path_helper', '_yang_name', '_rest_name', '_extmethods', '__ext_community_receive','__ext_community_send_vrf',)

  _yang_name = 'extended-community'
  _rest_name = 'extended-community'

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
    self.__ext_community_receive = YANGDynClass(base=YANGBool, is_leaf=True, yang_name="ext-community-receive", rest_name="receive", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'cli-full-command': None, u'cli-run-template': u'$(.?:)', u'alt-name': u'receive', u'info': u'Capability to RECEIVE the ORF from this neighbor'}}, namespace='urn:brocade.com:mgmt:brocade-bgp', defining_module='brocade-bgp', yang_type='empty', is_config=True)
    self.__ext_community_send_vrf = YANGDynClass(base=YANGBool, is_leaf=True, yang_name="ext-community-send-vrf", rest_name="send-vrf-filter", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'cli-full-command': None, u'cli-run-template': u'$(.?:)', u'alt-name': u'send-vrf-filter', u'info': u'Capability to SEND the ORF (local VRF route targets) to this neighbor'}}, namespace='urn:brocade.com:mgmt:brocade-bgp', defining_module='brocade-bgp', yang_type='empty', is_config=True)

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
      return [u'routing-system', u'router', u'router-bgp', u'address-family', u'vpnv6', u'vpnv6-unicast', u'af-vpn-neighbor-peergroup-holder', u'af-vpn-neighbor-peergroup', u'af-neighbor-capability', u'orf', u'extended-community']

  def _rest_path(self):
    if hasattr(self, "_parent"):
      if self._rest_name:
        return self._parent._rest_path()+[self._rest_name]
      else:
        return self._parent._rest_path()
    else:
      return [u'router', u'bgp', u'address-family', u'vpnv6', u'unicast', u'neighbor', u'capability', u'orf', u'extended-community']

  def _get_ext_community_receive(self):
    """
    Getter method for ext_community_receive, mapped from YANG variable /routing_system/router/router_bgp/address_family/vpnv6/vpnv6_unicast/af_vpn_neighbor_peergroup_holder/af_vpn_neighbor_peergroup/af_neighbor_capability/orf/extended_community/ext_community_receive (empty)

    YANG Description: Capability to RECEIVE the ORF from this neighbor
    """
    return self.__ext_community_receive
      
  def _set_ext_community_receive(self, v, load=False):
    """
    Setter method for ext_community_receive, mapped from YANG variable /routing_system/router/router_bgp/address_family/vpnv6/vpnv6_unicast/af_vpn_neighbor_peergroup_holder/af_vpn_neighbor_peergroup/af_neighbor_capability/orf/extended_community/ext_community_receive (empty)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_ext_community_receive is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_ext_community_receive() directly.

    YANG Description: Capability to RECEIVE the ORF from this neighbor
    """
    if hasattr(v, "_utype"):
      v = v._utype(v)
    try:
      t = YANGDynClass(v,base=YANGBool, is_leaf=True, yang_name="ext-community-receive", rest_name="receive", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'cli-full-command': None, u'cli-run-template': u'$(.?:)', u'alt-name': u'receive', u'info': u'Capability to RECEIVE the ORF from this neighbor'}}, namespace='urn:brocade.com:mgmt:brocade-bgp', defining_module='brocade-bgp', yang_type='empty', is_config=True)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """ext_community_receive must be of a type compatible with empty""",
          'defined-type': "empty",
          'generated-type': """YANGDynClass(base=YANGBool, is_leaf=True, yang_name="ext-community-receive", rest_name="receive", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'cli-full-command': None, u'cli-run-template': u'$(.?:)', u'alt-name': u'receive', u'info': u'Capability to RECEIVE the ORF from this neighbor'}}, namespace='urn:brocade.com:mgmt:brocade-bgp', defining_module='brocade-bgp', yang_type='empty', is_config=True)""",
        })

    self.__ext_community_receive = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_ext_community_receive(self):
    self.__ext_community_receive = YANGDynClass(base=YANGBool, is_leaf=True, yang_name="ext-community-receive", rest_name="receive", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'cli-full-command': None, u'cli-run-template': u'$(.?:)', u'alt-name': u'receive', u'info': u'Capability to RECEIVE the ORF from this neighbor'}}, namespace='urn:brocade.com:mgmt:brocade-bgp', defining_module='brocade-bgp', yang_type='empty', is_config=True)


  def _get_ext_community_send_vrf(self):
    """
    Getter method for ext_community_send_vrf, mapped from YANG variable /routing_system/router/router_bgp/address_family/vpnv6/vpnv6_unicast/af_vpn_neighbor_peergroup_holder/af_vpn_neighbor_peergroup/af_neighbor_capability/orf/extended_community/ext_community_send_vrf (empty)

    YANG Description: Capability to SEND the ORF (local VRF route targets) to this neighbor
    """
    return self.__ext_community_send_vrf
      
  def _set_ext_community_send_vrf(self, v, load=False):
    """
    Setter method for ext_community_send_vrf, mapped from YANG variable /routing_system/router/router_bgp/address_family/vpnv6/vpnv6_unicast/af_vpn_neighbor_peergroup_holder/af_vpn_neighbor_peergroup/af_neighbor_capability/orf/extended_community/ext_community_send_vrf (empty)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_ext_community_send_vrf is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_ext_community_send_vrf() directly.

    YANG Description: Capability to SEND the ORF (local VRF route targets) to this neighbor
    """
    if hasattr(v, "_utype"):
      v = v._utype(v)
    try:
      t = YANGDynClass(v,base=YANGBool, is_leaf=True, yang_name="ext-community-send-vrf", rest_name="send-vrf-filter", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'cli-full-command': None, u'cli-run-template': u'$(.?:)', u'alt-name': u'send-vrf-filter', u'info': u'Capability to SEND the ORF (local VRF route targets) to this neighbor'}}, namespace='urn:brocade.com:mgmt:brocade-bgp', defining_module='brocade-bgp', yang_type='empty', is_config=True)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """ext_community_send_vrf must be of a type compatible with empty""",
          'defined-type': "empty",
          'generated-type': """YANGDynClass(base=YANGBool, is_leaf=True, yang_name="ext-community-send-vrf", rest_name="send-vrf-filter", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'cli-full-command': None, u'cli-run-template': u'$(.?:)', u'alt-name': u'send-vrf-filter', u'info': u'Capability to SEND the ORF (local VRF route targets) to this neighbor'}}, namespace='urn:brocade.com:mgmt:brocade-bgp', defining_module='brocade-bgp', yang_type='empty', is_config=True)""",
        })

    self.__ext_community_send_vrf = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_ext_community_send_vrf(self):
    self.__ext_community_send_vrf = YANGDynClass(base=YANGBool, is_leaf=True, yang_name="ext-community-send-vrf", rest_name="send-vrf-filter", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'cli-full-command': None, u'cli-run-template': u'$(.?:)', u'alt-name': u'send-vrf-filter', u'info': u'Capability to SEND the ORF (local VRF route targets) to this neighbor'}}, namespace='urn:brocade.com:mgmt:brocade-bgp', defining_module='brocade-bgp', yang_type='empty', is_config=True)

  ext_community_receive = __builtin__.property(_get_ext_community_receive, _set_ext_community_receive)
  ext_community_send_vrf = __builtin__.property(_get_ext_community_send_vrf, _set_ext_community_send_vrf)


  _pyangbind_elements = {'ext_community_receive': ext_community_receive, 'ext_community_send_vrf': ext_community_send_vrf, }


