
from operator import attrgetter
import pyangbind.lib.xpathhelper as xpathhelper
from pyangbind.lib.yangtypes import RestrictedPrecisionDecimalType, RestrictedClassType, TypedListType
from pyangbind.lib.yangtypes import YANGBool, YANGListType, YANGDynClass, ReferenceType
from pyangbind.lib.base import PybindBase
from decimal import Decimal
from bitarray import bitarray
import __builtin__
import match
class ospf(PybindBase):
  """
  This class was auto-generated by the PythonClass plugin for PYANG
  from YANG module brocade-common-def - based on the path /routing-system/router/router-bgp/address-family/ipv6/ipv6-unicast/af-ipv6-vrf/af-ipv6-uc-and-vrf-cmds-call-point-holder/redistribute/ospf. Each member element of
  the container is represented as a class variable - with a specific
  YANG type.
  """
  __slots__ = ('_pybind_generated_by', '_path_helper', '_yang_name', '_rest_name', '_extmethods', '__redistribute_ospf','__match','__ospf_metric','__ospf_route_map',)

  _yang_name = 'ospf'
  _rest_name = 'ospf'

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
    self.__ospf_metric = YANGDynClass(base=RestrictedClassType(base_type=RestrictedClassType(base_type=long, restriction_dict={'range': ['0..4294967295']}, int_size=32), restriction_dict={'range': [u'1..4294967295']}), is_leaf=True, yang_name="ospf-metric", rest_name="metric", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'info': u'Metric for redistributed routes', u'cli-full-command': None, u'alt-name': u'metric'}}, namespace='urn:brocade.com:mgmt:brocade-bgp', defining_module='brocade-bgp', yang_type='conn-metric', is_config=True)
    self.__redistribute_ospf = YANGDynClass(base=YANGBool, is_leaf=True, yang_name="redistribute-ospf", rest_name="", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'cli-run-template': u'$(.?$(../ospf-metric?\\r:$(../ospf-route-map?\\r:$(../match/ospf-external1?\\r:$(../match/ospf-external2?\\r:redistribute ospf\n)))):\\r)', u'cli-drop-node-name': None}}, namespace='urn:brocade.com:mgmt:brocade-bgp', defining_module='brocade-bgp', yang_type='empty', is_config=True)
    self.__match = YANGDynClass(base=match.match, is_container='container', yang_name="match", rest_name="match", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'info': u'Redistribution of OSPF routes', u'cli-incomplete-no': None, u'cli-incomplete-command': None}}, namespace='urn:brocade.com:mgmt:brocade-bgp', defining_module='brocade-bgp', yang_type='container', is_config=True)
    self.__ospf_route_map = YANGDynClass(base=RestrictedClassType(base_type=unicode, restriction_dict={'length': [u'1..63']}), is_leaf=True, yang_name="ospf-route-map", rest_name="route-map", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'info': u'Route map reference', u'cli-full-command': None, u'alt-name': u'route-map'}}, namespace='urn:brocade.com:mgmt:brocade-bgp', defining_module='brocade-bgp', yang_type='rmap-type', is_config=True)

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
      return [u'routing-system', u'router', u'router-bgp', u'address-family', u'ipv6', u'ipv6-unicast', u'af-ipv6-vrf', u'af-ipv6-uc-and-vrf-cmds-call-point-holder', u'redistribute', u'ospf']

  def _rest_path(self):
    if hasattr(self, "_parent"):
      if self._rest_name:
        return self._parent._rest_path()+[self._rest_name]
      else:
        return self._parent._rest_path()
    else:
      return [u'router', u'bgp', u'address-family', u'ipv6', u'unicast', u'vrf', u'redistribute', u'ospf']

  def _get_redistribute_ospf(self):
    """
    Getter method for redistribute_ospf, mapped from YANG variable /routing_system/router/router_bgp/address_family/ipv6/ipv6_unicast/af_ipv6_vrf/af_ipv6_uc_and_vrf_cmds_call_point_holder/redistribute/ospf/redistribute_ospf (empty)
    """
    return self.__redistribute_ospf
      
  def _set_redistribute_ospf(self, v, load=False):
    """
    Setter method for redistribute_ospf, mapped from YANG variable /routing_system/router/router_bgp/address_family/ipv6/ipv6_unicast/af_ipv6_vrf/af_ipv6_uc_and_vrf_cmds_call_point_holder/redistribute/ospf/redistribute_ospf (empty)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_redistribute_ospf is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_redistribute_ospf() directly.
    """
    if hasattr(v, "_utype"):
      v = v._utype(v)
    try:
      t = YANGDynClass(v,base=YANGBool, is_leaf=True, yang_name="redistribute-ospf", rest_name="", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'cli-run-template': u'$(.?$(../ospf-metric?\\r:$(../ospf-route-map?\\r:$(../match/ospf-external1?\\r:$(../match/ospf-external2?\\r:redistribute ospf\n)))):\\r)', u'cli-drop-node-name': None}}, namespace='urn:brocade.com:mgmt:brocade-bgp', defining_module='brocade-bgp', yang_type='empty', is_config=True)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """redistribute_ospf must be of a type compatible with empty""",
          'defined-type': "empty",
          'generated-type': """YANGDynClass(base=YANGBool, is_leaf=True, yang_name="redistribute-ospf", rest_name="", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'cli-run-template': u'$(.?$(../ospf-metric?\\r:$(../ospf-route-map?\\r:$(../match/ospf-external1?\\r:$(../match/ospf-external2?\\r:redistribute ospf\n)))):\\r)', u'cli-drop-node-name': None}}, namespace='urn:brocade.com:mgmt:brocade-bgp', defining_module='brocade-bgp', yang_type='empty', is_config=True)""",
        })

    self.__redistribute_ospf = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_redistribute_ospf(self):
    self.__redistribute_ospf = YANGDynClass(base=YANGBool, is_leaf=True, yang_name="redistribute-ospf", rest_name="", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'cli-run-template': u'$(.?$(../ospf-metric?\\r:$(../ospf-route-map?\\r:$(../match/ospf-external1?\\r:$(../match/ospf-external2?\\r:redistribute ospf\n)))):\\r)', u'cli-drop-node-name': None}}, namespace='urn:brocade.com:mgmt:brocade-bgp', defining_module='brocade-bgp', yang_type='empty', is_config=True)


  def _get_match(self):
    """
    Getter method for match, mapped from YANG variable /routing_system/router/router_bgp/address_family/ipv6/ipv6_unicast/af_ipv6_vrf/af_ipv6_uc_and_vrf_cmds_call_point_holder/redistribute/ospf/match (container)
    """
    return self.__match
      
  def _set_match(self, v, load=False):
    """
    Setter method for match, mapped from YANG variable /routing_system/router/router_bgp/address_family/ipv6/ipv6_unicast/af_ipv6_vrf/af_ipv6_uc_and_vrf_cmds_call_point_holder/redistribute/ospf/match (container)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_match is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_match() directly.
    """
    if hasattr(v, "_utype"):
      v = v._utype(v)
    try:
      t = YANGDynClass(v,base=match.match, is_container='container', yang_name="match", rest_name="match", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'info': u'Redistribution of OSPF routes', u'cli-incomplete-no': None, u'cli-incomplete-command': None}}, namespace='urn:brocade.com:mgmt:brocade-bgp', defining_module='brocade-bgp', yang_type='container', is_config=True)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """match must be of a type compatible with container""",
          'defined-type': "container",
          'generated-type': """YANGDynClass(base=match.match, is_container='container', yang_name="match", rest_name="match", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'info': u'Redistribution of OSPF routes', u'cli-incomplete-no': None, u'cli-incomplete-command': None}}, namespace='urn:brocade.com:mgmt:brocade-bgp', defining_module='brocade-bgp', yang_type='container', is_config=True)""",
        })

    self.__match = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_match(self):
    self.__match = YANGDynClass(base=match.match, is_container='container', yang_name="match", rest_name="match", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'info': u'Redistribution of OSPF routes', u'cli-incomplete-no': None, u'cli-incomplete-command': None}}, namespace='urn:brocade.com:mgmt:brocade-bgp', defining_module='brocade-bgp', yang_type='container', is_config=True)


  def _get_ospf_metric(self):
    """
    Getter method for ospf_metric, mapped from YANG variable /routing_system/router/router_bgp/address_family/ipv6/ipv6_unicast/af_ipv6_vrf/af_ipv6_uc_and_vrf_cmds_call_point_holder/redistribute/ospf/ospf_metric (conn-metric)
    """
    return self.__ospf_metric
      
  def _set_ospf_metric(self, v, load=False):
    """
    Setter method for ospf_metric, mapped from YANG variable /routing_system/router/router_bgp/address_family/ipv6/ipv6_unicast/af_ipv6_vrf/af_ipv6_uc_and_vrf_cmds_call_point_holder/redistribute/ospf/ospf_metric (conn-metric)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_ospf_metric is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_ospf_metric() directly.
    """
    if hasattr(v, "_utype"):
      v = v._utype(v)
    try:
      t = YANGDynClass(v,base=RestrictedClassType(base_type=RestrictedClassType(base_type=long, restriction_dict={'range': ['0..4294967295']}, int_size=32), restriction_dict={'range': [u'1..4294967295']}), is_leaf=True, yang_name="ospf-metric", rest_name="metric", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'info': u'Metric for redistributed routes', u'cli-full-command': None, u'alt-name': u'metric'}}, namespace='urn:brocade.com:mgmt:brocade-bgp', defining_module='brocade-bgp', yang_type='conn-metric', is_config=True)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """ospf_metric must be of a type compatible with conn-metric""",
          'defined-type': "brocade-bgp:conn-metric",
          'generated-type': """YANGDynClass(base=RestrictedClassType(base_type=RestrictedClassType(base_type=long, restriction_dict={'range': ['0..4294967295']}, int_size=32), restriction_dict={'range': [u'1..4294967295']}), is_leaf=True, yang_name="ospf-metric", rest_name="metric", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'info': u'Metric for redistributed routes', u'cli-full-command': None, u'alt-name': u'metric'}}, namespace='urn:brocade.com:mgmt:brocade-bgp', defining_module='brocade-bgp', yang_type='conn-metric', is_config=True)""",
        })

    self.__ospf_metric = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_ospf_metric(self):
    self.__ospf_metric = YANGDynClass(base=RestrictedClassType(base_type=RestrictedClassType(base_type=long, restriction_dict={'range': ['0..4294967295']}, int_size=32), restriction_dict={'range': [u'1..4294967295']}), is_leaf=True, yang_name="ospf-metric", rest_name="metric", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'info': u'Metric for redistributed routes', u'cli-full-command': None, u'alt-name': u'metric'}}, namespace='urn:brocade.com:mgmt:brocade-bgp', defining_module='brocade-bgp', yang_type='conn-metric', is_config=True)


  def _get_ospf_route_map(self):
    """
    Getter method for ospf_route_map, mapped from YANG variable /routing_system/router/router_bgp/address_family/ipv6/ipv6_unicast/af_ipv6_vrf/af_ipv6_uc_and_vrf_cmds_call_point_holder/redistribute/ospf/ospf_route_map (rmap-type)
    """
    return self.__ospf_route_map
      
  def _set_ospf_route_map(self, v, load=False):
    """
    Setter method for ospf_route_map, mapped from YANG variable /routing_system/router/router_bgp/address_family/ipv6/ipv6_unicast/af_ipv6_vrf/af_ipv6_uc_and_vrf_cmds_call_point_holder/redistribute/ospf/ospf_route_map (rmap-type)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_ospf_route_map is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_ospf_route_map() directly.
    """
    if hasattr(v, "_utype"):
      v = v._utype(v)
    try:
      t = YANGDynClass(v,base=RestrictedClassType(base_type=unicode, restriction_dict={'length': [u'1..63']}), is_leaf=True, yang_name="ospf-route-map", rest_name="route-map", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'info': u'Route map reference', u'cli-full-command': None, u'alt-name': u'route-map'}}, namespace='urn:brocade.com:mgmt:brocade-bgp', defining_module='brocade-bgp', yang_type='rmap-type', is_config=True)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """ospf_route_map must be of a type compatible with rmap-type""",
          'defined-type': "brocade-bgp:rmap-type",
          'generated-type': """YANGDynClass(base=RestrictedClassType(base_type=unicode, restriction_dict={'length': [u'1..63']}), is_leaf=True, yang_name="ospf-route-map", rest_name="route-map", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'info': u'Route map reference', u'cli-full-command': None, u'alt-name': u'route-map'}}, namespace='urn:brocade.com:mgmt:brocade-bgp', defining_module='brocade-bgp', yang_type='rmap-type', is_config=True)""",
        })

    self.__ospf_route_map = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_ospf_route_map(self):
    self.__ospf_route_map = YANGDynClass(base=RestrictedClassType(base_type=unicode, restriction_dict={'length': [u'1..63']}), is_leaf=True, yang_name="ospf-route-map", rest_name="route-map", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'info': u'Route map reference', u'cli-full-command': None, u'alt-name': u'route-map'}}, namespace='urn:brocade.com:mgmt:brocade-bgp', defining_module='brocade-bgp', yang_type='rmap-type', is_config=True)

  redistribute_ospf = __builtin__.property(_get_redistribute_ospf, _set_redistribute_ospf)
  match = __builtin__.property(_get_match, _set_match)
  ospf_metric = __builtin__.property(_get_ospf_metric, _set_ospf_metric)
  ospf_route_map = __builtin__.property(_get_ospf_route_map, _set_ospf_route_map)


  _pyangbind_elements = {'redistribute_ospf': redistribute_ospf, 'match': match, 'ospf_metric': ospf_metric, 'ospf_route_map': ospf_route_map, }


