
from operator import attrgetter
import pyangbind.lib.xpathhelper as xpathhelper
from pyangbind.lib.yangtypes import RestrictedPrecisionDecimalType, RestrictedClassType, TypedListType
from pyangbind.lib.yangtypes import YANGBool, YANGListType, YANGDynClass, ReferenceType
from pyangbind.lib.base import PybindBase
from decimal import Decimal
from bitarray import bitarray
import __builtin__
import values
class dampening(PybindBase):
  """
  This class was auto-generated by the PythonClass plugin for PYANG
  from YANG module brocade-common-def - based on the path /routing-system/router/router-bgp/address-family/ipv6/ipv6-unicast/af-ipv6-vrf/dampening. Each member element of
  the container is represented as a class variable - with a specific
  YANG type.
  """
  __slots__ = ('_pybind_generated_by', '_path_helper', '_yang_name', '_rest_name', '_extmethods', '__dampening_flag','__values','__dampening_route_map',)

  _yang_name = 'dampening'
  _rest_name = 'dampening'

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
    self.__dampening_flag = YANGDynClass(base=YANGBool, is_leaf=True, yang_name="dampening-flag", rest_name="", parent=self, choice=(u'ch-dampening-source', u'ca-dampening-flag'), path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'cli-drop-node-name': None}}, namespace='urn:brocade.com:mgmt:brocade-bgp', defining_module='brocade-bgp', yang_type='empty', is_config=True)
    self.__dampening_route_map = YANGDynClass(base=RestrictedClassType(base_type=unicode, restriction_dict={'length': [u'1..63']}), is_leaf=True, yang_name="dampening-route-map", rest_name="route-map", parent=self, choice=(u'ch-dampening-source', u'ca-dampening-route-map'), path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'info': u'Route-map to specify criteria for dampening', u'alt-name': u'route-map'}}, namespace='urn:brocade.com:mgmt:brocade-bgp', defining_module='brocade-bgp', yang_type='rmap-type', is_config=True)
    self.__values = YANGDynClass(base=values.values, is_container='container', presence=False, yang_name="values", rest_name="", parent=self, choice=(u'ch-dampening-source', u'ca-dampening-specify-values'), path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'cli-compact-syntax': None, u'cli-drop-node-name': None, u'cli-sequence-commands': None}}, namespace='urn:brocade.com:mgmt:brocade-bgp', defining_module='brocade-bgp', yang_type='container', is_config=True)

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
      return [u'routing-system', u'router', u'router-bgp', u'address-family', u'ipv6', u'ipv6-unicast', u'af-ipv6-vrf', u'dampening']

  def _rest_path(self):
    if hasattr(self, "_parent"):
      if self._rest_name:
        return self._parent._rest_path()+[self._rest_name]
      else:
        return self._parent._rest_path()
    else:
      return [u'router', u'bgp', u'address-family', u'ipv6', u'unicast', u'vrf', u'dampening']

  def _get_dampening_flag(self):
    """
    Getter method for dampening_flag, mapped from YANG variable /routing_system/router/router_bgp/address_family/ipv6/ipv6_unicast/af_ipv6_vrf/dampening/dampening_flag (empty)

    YANG Description: This Flag is to indicate dampening feature  is enabled
    """
    return self.__dampening_flag
      
  def _set_dampening_flag(self, v, load=False):
    """
    Setter method for dampening_flag, mapped from YANG variable /routing_system/router/router_bgp/address_family/ipv6/ipv6_unicast/af_ipv6_vrf/dampening/dampening_flag (empty)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_dampening_flag is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_dampening_flag() directly.

    YANG Description: This Flag is to indicate dampening feature  is enabled
    """
    if hasattr(v, "_utype"):
      v = v._utype(v)
    try:
      t = YANGDynClass(v,base=YANGBool, is_leaf=True, yang_name="dampening-flag", rest_name="", parent=self, choice=(u'ch-dampening-source', u'ca-dampening-flag'), path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'cli-drop-node-name': None}}, namespace='urn:brocade.com:mgmt:brocade-bgp', defining_module='brocade-bgp', yang_type='empty', is_config=True)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """dampening_flag must be of a type compatible with empty""",
          'defined-type': "empty",
          'generated-type': """YANGDynClass(base=YANGBool, is_leaf=True, yang_name="dampening-flag", rest_name="", parent=self, choice=(u'ch-dampening-source', u'ca-dampening-flag'), path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'cli-drop-node-name': None}}, namespace='urn:brocade.com:mgmt:brocade-bgp', defining_module='brocade-bgp', yang_type='empty', is_config=True)""",
        })

    self.__dampening_flag = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_dampening_flag(self):
    self.__dampening_flag = YANGDynClass(base=YANGBool, is_leaf=True, yang_name="dampening-flag", rest_name="", parent=self, choice=(u'ch-dampening-source', u'ca-dampening-flag'), path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'cli-drop-node-name': None}}, namespace='urn:brocade.com:mgmt:brocade-bgp', defining_module='brocade-bgp', yang_type='empty', is_config=True)


  def _get_values(self):
    """
    Getter method for values, mapped from YANG variable /routing_system/router/router_bgp/address_family/ipv6/ipv6_unicast/af_ipv6_vrf/dampening/values (container)
    """
    return self.__values
      
  def _set_values(self, v, load=False):
    """
    Setter method for values, mapped from YANG variable /routing_system/router/router_bgp/address_family/ipv6/ipv6_unicast/af_ipv6_vrf/dampening/values (container)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_values is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_values() directly.
    """
    if hasattr(v, "_utype"):
      v = v._utype(v)
    try:
      t = YANGDynClass(v,base=values.values, is_container='container', presence=False, yang_name="values", rest_name="", parent=self, choice=(u'ch-dampening-source', u'ca-dampening-specify-values'), path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'cli-compact-syntax': None, u'cli-drop-node-name': None, u'cli-sequence-commands': None}}, namespace='urn:brocade.com:mgmt:brocade-bgp', defining_module='brocade-bgp', yang_type='container', is_config=True)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """values must be of a type compatible with container""",
          'defined-type': "container",
          'generated-type': """YANGDynClass(base=values.values, is_container='container', presence=False, yang_name="values", rest_name="", parent=self, choice=(u'ch-dampening-source', u'ca-dampening-specify-values'), path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'cli-compact-syntax': None, u'cli-drop-node-name': None, u'cli-sequence-commands': None}}, namespace='urn:brocade.com:mgmt:brocade-bgp', defining_module='brocade-bgp', yang_type='container', is_config=True)""",
        })

    self.__values = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_values(self):
    self.__values = YANGDynClass(base=values.values, is_container='container', presence=False, yang_name="values", rest_name="", parent=self, choice=(u'ch-dampening-source', u'ca-dampening-specify-values'), path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'cli-compact-syntax': None, u'cli-drop-node-name': None, u'cli-sequence-commands': None}}, namespace='urn:brocade.com:mgmt:brocade-bgp', defining_module='brocade-bgp', yang_type='container', is_config=True)


  def _get_dampening_route_map(self):
    """
    Getter method for dampening_route_map, mapped from YANG variable /routing_system/router/router_bgp/address_family/ipv6/ipv6_unicast/af_ipv6_vrf/dampening/dampening_route_map (rmap-type)
    """
    return self.__dampening_route_map
      
  def _set_dampening_route_map(self, v, load=False):
    """
    Setter method for dampening_route_map, mapped from YANG variable /routing_system/router/router_bgp/address_family/ipv6/ipv6_unicast/af_ipv6_vrf/dampening/dampening_route_map (rmap-type)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_dampening_route_map is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_dampening_route_map() directly.
    """
    if hasattr(v, "_utype"):
      v = v._utype(v)
    try:
      t = YANGDynClass(v,base=RestrictedClassType(base_type=unicode, restriction_dict={'length': [u'1..63']}), is_leaf=True, yang_name="dampening-route-map", rest_name="route-map", parent=self, choice=(u'ch-dampening-source', u'ca-dampening-route-map'), path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'info': u'Route-map to specify criteria for dampening', u'alt-name': u'route-map'}}, namespace='urn:brocade.com:mgmt:brocade-bgp', defining_module='brocade-bgp', yang_type='rmap-type', is_config=True)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """dampening_route_map must be of a type compatible with rmap-type""",
          'defined-type': "brocade-bgp:rmap-type",
          'generated-type': """YANGDynClass(base=RestrictedClassType(base_type=unicode, restriction_dict={'length': [u'1..63']}), is_leaf=True, yang_name="dampening-route-map", rest_name="route-map", parent=self, choice=(u'ch-dampening-source', u'ca-dampening-route-map'), path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'info': u'Route-map to specify criteria for dampening', u'alt-name': u'route-map'}}, namespace='urn:brocade.com:mgmt:brocade-bgp', defining_module='brocade-bgp', yang_type='rmap-type', is_config=True)""",
        })

    self.__dampening_route_map = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_dampening_route_map(self):
    self.__dampening_route_map = YANGDynClass(base=RestrictedClassType(base_type=unicode, restriction_dict={'length': [u'1..63']}), is_leaf=True, yang_name="dampening-route-map", rest_name="route-map", parent=self, choice=(u'ch-dampening-source', u'ca-dampening-route-map'), path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'info': u'Route-map to specify criteria for dampening', u'alt-name': u'route-map'}}, namespace='urn:brocade.com:mgmt:brocade-bgp', defining_module='brocade-bgp', yang_type='rmap-type', is_config=True)

  dampening_flag = __builtin__.property(_get_dampening_flag, _set_dampening_flag)
  values = __builtin__.property(_get_values, _set_values)
  dampening_route_map = __builtin__.property(_get_dampening_route_map, _set_dampening_route_map)

  __choices__ = {u'ch-dampening-source': {u'ca-dampening-flag': [u'dampening_flag'], u'ca-dampening-specify-values': [u'values'], u'ca-dampening-route-map': [u'dampening_route_map']}}
  _pyangbind_elements = {'dampening_flag': dampening_flag, 'values': values, 'dampening_route_map': dampening_route_map, }


