
from operator import attrgetter
import pyangbind.lib.xpathhelper as xpathhelper
from pyangbind.lib.yangtypes import RestrictedPrecisionDecimalType, RestrictedClassType, TypedListType
from pyangbind.lib.yangtypes import YANGBool, YANGListType, YANGDynClass, ReferenceType
from pyangbind.lib.base import PybindBase
from decimal import Decimal
from bitarray import bitarray
import __builtin__
class connected(PybindBase):
  """
  This class was auto-generated by the PythonClass plugin for PYANG
  from YANG module brocade-common-def - based on the path /routing-system/router/isis/router-isis-cmds-holder/address-family/ipv4/af-ipv4-unicast/af-ipv4-attributes/af-common-attributes/redistribute/connected. Each member element of
  the container is represented as a class variable - with a specific
  YANG type.
  """
  __slots__ = ('_pybind_generated_by', '_path_helper', '_yang_name', '_rest_name', '_extmethods', '__connected_metric','__connected_route_map','__connected_level1','__connected_level2','__connected_level12','__connected_metric_type',)

  _yang_name = 'connected'
  _rest_name = 'connected'

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
    self.__connected_metric = YANGDynClass(base=RestrictedClassType(base_type=RestrictedClassType(base_type=long, restriction_dict={'range': ['0..4294967295']}, int_size=32), restriction_dict={'range': [u'1..4261412863']}), is_leaf=True, yang_name="connected-metric", rest_name="metric", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'info': u'Metric for redistributed routes', u'cli-full-command': None, u'alt-name': u'metric'}}, namespace='urn:brocade.com:mgmt:brocade-isis', defining_module='brocade-isis', yang_type='conn-metric', is_config=True)
    self.__connected_level2 = YANGDynClass(base=YANGBool, is_leaf=True, yang_name="connected-level2", rest_name="level-2", parent=self, choice=(u'ch-connected-levels', u'ca-connected-level2'), path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'cli-full-command': None, u'info': u'IS-IS Level-2 routes only', u'alt-name': u'level-2', u'cli-full-no': None}}, namespace='urn:brocade.com:mgmt:brocade-isis', defining_module='brocade-isis', yang_type='empty', is_config=True)
    self.__connected_level1 = YANGDynClass(base=YANGBool, is_leaf=True, yang_name="connected-level1", rest_name="level-1", parent=self, choice=(u'ch-connected-levels', u'ca-connected-level1'), path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'cli-full-command': None, u'info': u'IS-IS Level-1 routes only', u'alt-name': u'level-1', u'cli-full-no': None}}, namespace='urn:brocade.com:mgmt:brocade-isis', defining_module='brocade-isis', yang_type='empty', is_config=True)
    self.__connected_level12 = YANGDynClass(base=YANGBool, is_leaf=True, yang_name="connected-level12", rest_name="level-1-2", parent=self, choice=(u'ch-connected-levels', u'ca-connected-level12'), path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'cli-full-command': None, u'info': u'IS-IS Level-1-2 routes', u'alt-name': u'level-1-2', u'cli-full-no': None}}, namespace='urn:brocade.com:mgmt:brocade-isis', defining_module='brocade-isis', yang_type='empty', is_config=True)
    self.__connected_route_map = YANGDynClass(base=RestrictedClassType(base_type=unicode, restriction_dict={'length': [u'1..63']}), is_leaf=True, yang_name="connected-route-map", rest_name="route-map", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'info': u'Route map reference', u'cli-full-command': None, u'alt-name': u'route-map'}}, namespace='urn:brocade.com:mgmt:brocade-isis', defining_module='brocade-isis', yang_type='rmap-type', is_config=True)
    self.__connected_metric_type = YANGDynClass(base=RestrictedClassType(base_type=unicode,                                     restriction_type="dict_key",                                     restriction_arg={u'internal': {'value': 1}, u'external': {'value': 2}},), default=unicode("internal"), is_leaf=True, yang_name="connected-metric-type", rest_name="metric-type", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'info': u'IS-IS metric type for redistributed routes', u'alt-name': u'metric-type'}}, namespace='urn:brocade.com:mgmt:brocade-isis', defining_module='brocade-isis', yang_type='is-metric-type-t', is_config=True)

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
      return [u'routing-system', u'router', u'isis', u'router-isis-cmds-holder', u'address-family', u'ipv4', u'af-ipv4-unicast', u'af-ipv4-attributes', u'af-common-attributes', u'redistribute', u'connected']

  def _rest_path(self):
    if hasattr(self, "_parent"):
      if self._rest_name:
        return self._parent._rest_path()+[self._rest_name]
      else:
        return self._parent._rest_path()
    else:
      return [u'router', u'isis', u'address-family', u'ipv4', u'unicast', u'redistribute', u'connected']

  def _get_connected_metric(self):
    """
    Getter method for connected_metric, mapped from YANG variable /routing_system/router/isis/router_isis_cmds_holder/address_family/ipv4/af_ipv4_unicast/af_ipv4_attributes/af_common_attributes/redistribute/connected/connected_metric (conn-metric)
    """
    return self.__connected_metric
      
  def _set_connected_metric(self, v, load=False):
    """
    Setter method for connected_metric, mapped from YANG variable /routing_system/router/isis/router_isis_cmds_holder/address_family/ipv4/af_ipv4_unicast/af_ipv4_attributes/af_common_attributes/redistribute/connected/connected_metric (conn-metric)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_connected_metric is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_connected_metric() directly.
    """
    if hasattr(v, "_utype"):
      v = v._utype(v)
    try:
      t = YANGDynClass(v,base=RestrictedClassType(base_type=RestrictedClassType(base_type=long, restriction_dict={'range': ['0..4294967295']}, int_size=32), restriction_dict={'range': [u'1..4261412863']}), is_leaf=True, yang_name="connected-metric", rest_name="metric", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'info': u'Metric for redistributed routes', u'cli-full-command': None, u'alt-name': u'metric'}}, namespace='urn:brocade.com:mgmt:brocade-isis', defining_module='brocade-isis', yang_type='conn-metric', is_config=True)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """connected_metric must be of a type compatible with conn-metric""",
          'defined-type': "brocade-isis:conn-metric",
          'generated-type': """YANGDynClass(base=RestrictedClassType(base_type=RestrictedClassType(base_type=long, restriction_dict={'range': ['0..4294967295']}, int_size=32), restriction_dict={'range': [u'1..4261412863']}), is_leaf=True, yang_name="connected-metric", rest_name="metric", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'info': u'Metric for redistributed routes', u'cli-full-command': None, u'alt-name': u'metric'}}, namespace='urn:brocade.com:mgmt:brocade-isis', defining_module='brocade-isis', yang_type='conn-metric', is_config=True)""",
        })

    self.__connected_metric = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_connected_metric(self):
    self.__connected_metric = YANGDynClass(base=RestrictedClassType(base_type=RestrictedClassType(base_type=long, restriction_dict={'range': ['0..4294967295']}, int_size=32), restriction_dict={'range': [u'1..4261412863']}), is_leaf=True, yang_name="connected-metric", rest_name="metric", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'info': u'Metric for redistributed routes', u'cli-full-command': None, u'alt-name': u'metric'}}, namespace='urn:brocade.com:mgmt:brocade-isis', defining_module='brocade-isis', yang_type='conn-metric', is_config=True)


  def _get_connected_route_map(self):
    """
    Getter method for connected_route_map, mapped from YANG variable /routing_system/router/isis/router_isis_cmds_holder/address_family/ipv4/af_ipv4_unicast/af_ipv4_attributes/af_common_attributes/redistribute/connected/connected_route_map (rmap-type)
    """
    return self.__connected_route_map
      
  def _set_connected_route_map(self, v, load=False):
    """
    Setter method for connected_route_map, mapped from YANG variable /routing_system/router/isis/router_isis_cmds_holder/address_family/ipv4/af_ipv4_unicast/af_ipv4_attributes/af_common_attributes/redistribute/connected/connected_route_map (rmap-type)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_connected_route_map is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_connected_route_map() directly.
    """
    if hasattr(v, "_utype"):
      v = v._utype(v)
    try:
      t = YANGDynClass(v,base=RestrictedClassType(base_type=unicode, restriction_dict={'length': [u'1..63']}), is_leaf=True, yang_name="connected-route-map", rest_name="route-map", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'info': u'Route map reference', u'cli-full-command': None, u'alt-name': u'route-map'}}, namespace='urn:brocade.com:mgmt:brocade-isis', defining_module='brocade-isis', yang_type='rmap-type', is_config=True)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """connected_route_map must be of a type compatible with rmap-type""",
          'defined-type': "brocade-isis:rmap-type",
          'generated-type': """YANGDynClass(base=RestrictedClassType(base_type=unicode, restriction_dict={'length': [u'1..63']}), is_leaf=True, yang_name="connected-route-map", rest_name="route-map", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'info': u'Route map reference', u'cli-full-command': None, u'alt-name': u'route-map'}}, namespace='urn:brocade.com:mgmt:brocade-isis', defining_module='brocade-isis', yang_type='rmap-type', is_config=True)""",
        })

    self.__connected_route_map = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_connected_route_map(self):
    self.__connected_route_map = YANGDynClass(base=RestrictedClassType(base_type=unicode, restriction_dict={'length': [u'1..63']}), is_leaf=True, yang_name="connected-route-map", rest_name="route-map", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'info': u'Route map reference', u'cli-full-command': None, u'alt-name': u'route-map'}}, namespace='urn:brocade.com:mgmt:brocade-isis', defining_module='brocade-isis', yang_type='rmap-type', is_config=True)


  def _get_connected_level1(self):
    """
    Getter method for connected_level1, mapped from YANG variable /routing_system/router/isis/router_isis_cmds_holder/address_family/ipv4/af_ipv4_unicast/af_ipv4_attributes/af_common_attributes/redistribute/connected/connected_level1 (empty)
    """
    return self.__connected_level1
      
  def _set_connected_level1(self, v, load=False):
    """
    Setter method for connected_level1, mapped from YANG variable /routing_system/router/isis/router_isis_cmds_holder/address_family/ipv4/af_ipv4_unicast/af_ipv4_attributes/af_common_attributes/redistribute/connected/connected_level1 (empty)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_connected_level1 is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_connected_level1() directly.
    """
    if hasattr(v, "_utype"):
      v = v._utype(v)
    try:
      t = YANGDynClass(v,base=YANGBool, is_leaf=True, yang_name="connected-level1", rest_name="level-1", parent=self, choice=(u'ch-connected-levels', u'ca-connected-level1'), path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'cli-full-command': None, u'info': u'IS-IS Level-1 routes only', u'alt-name': u'level-1', u'cli-full-no': None}}, namespace='urn:brocade.com:mgmt:brocade-isis', defining_module='brocade-isis', yang_type='empty', is_config=True)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """connected_level1 must be of a type compatible with empty""",
          'defined-type': "empty",
          'generated-type': """YANGDynClass(base=YANGBool, is_leaf=True, yang_name="connected-level1", rest_name="level-1", parent=self, choice=(u'ch-connected-levels', u'ca-connected-level1'), path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'cli-full-command': None, u'info': u'IS-IS Level-1 routes only', u'alt-name': u'level-1', u'cli-full-no': None}}, namespace='urn:brocade.com:mgmt:brocade-isis', defining_module='brocade-isis', yang_type='empty', is_config=True)""",
        })

    self.__connected_level1 = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_connected_level1(self):
    self.__connected_level1 = YANGDynClass(base=YANGBool, is_leaf=True, yang_name="connected-level1", rest_name="level-1", parent=self, choice=(u'ch-connected-levels', u'ca-connected-level1'), path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'cli-full-command': None, u'info': u'IS-IS Level-1 routes only', u'alt-name': u'level-1', u'cli-full-no': None}}, namespace='urn:brocade.com:mgmt:brocade-isis', defining_module='brocade-isis', yang_type='empty', is_config=True)


  def _get_connected_level2(self):
    """
    Getter method for connected_level2, mapped from YANG variable /routing_system/router/isis/router_isis_cmds_holder/address_family/ipv4/af_ipv4_unicast/af_ipv4_attributes/af_common_attributes/redistribute/connected/connected_level2 (empty)
    """
    return self.__connected_level2
      
  def _set_connected_level2(self, v, load=False):
    """
    Setter method for connected_level2, mapped from YANG variable /routing_system/router/isis/router_isis_cmds_holder/address_family/ipv4/af_ipv4_unicast/af_ipv4_attributes/af_common_attributes/redistribute/connected/connected_level2 (empty)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_connected_level2 is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_connected_level2() directly.
    """
    if hasattr(v, "_utype"):
      v = v._utype(v)
    try:
      t = YANGDynClass(v,base=YANGBool, is_leaf=True, yang_name="connected-level2", rest_name="level-2", parent=self, choice=(u'ch-connected-levels', u'ca-connected-level2'), path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'cli-full-command': None, u'info': u'IS-IS Level-2 routes only', u'alt-name': u'level-2', u'cli-full-no': None}}, namespace='urn:brocade.com:mgmt:brocade-isis', defining_module='brocade-isis', yang_type='empty', is_config=True)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """connected_level2 must be of a type compatible with empty""",
          'defined-type': "empty",
          'generated-type': """YANGDynClass(base=YANGBool, is_leaf=True, yang_name="connected-level2", rest_name="level-2", parent=self, choice=(u'ch-connected-levels', u'ca-connected-level2'), path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'cli-full-command': None, u'info': u'IS-IS Level-2 routes only', u'alt-name': u'level-2', u'cli-full-no': None}}, namespace='urn:brocade.com:mgmt:brocade-isis', defining_module='brocade-isis', yang_type='empty', is_config=True)""",
        })

    self.__connected_level2 = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_connected_level2(self):
    self.__connected_level2 = YANGDynClass(base=YANGBool, is_leaf=True, yang_name="connected-level2", rest_name="level-2", parent=self, choice=(u'ch-connected-levels', u'ca-connected-level2'), path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'cli-full-command': None, u'info': u'IS-IS Level-2 routes only', u'alt-name': u'level-2', u'cli-full-no': None}}, namespace='urn:brocade.com:mgmt:brocade-isis', defining_module='brocade-isis', yang_type='empty', is_config=True)


  def _get_connected_level12(self):
    """
    Getter method for connected_level12, mapped from YANG variable /routing_system/router/isis/router_isis_cmds_holder/address_family/ipv4/af_ipv4_unicast/af_ipv4_attributes/af_common_attributes/redistribute/connected/connected_level12 (empty)
    """
    return self.__connected_level12
      
  def _set_connected_level12(self, v, load=False):
    """
    Setter method for connected_level12, mapped from YANG variable /routing_system/router/isis/router_isis_cmds_holder/address_family/ipv4/af_ipv4_unicast/af_ipv4_attributes/af_common_attributes/redistribute/connected/connected_level12 (empty)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_connected_level12 is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_connected_level12() directly.
    """
    if hasattr(v, "_utype"):
      v = v._utype(v)
    try:
      t = YANGDynClass(v,base=YANGBool, is_leaf=True, yang_name="connected-level12", rest_name="level-1-2", parent=self, choice=(u'ch-connected-levels', u'ca-connected-level12'), path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'cli-full-command': None, u'info': u'IS-IS Level-1-2 routes', u'alt-name': u'level-1-2', u'cli-full-no': None}}, namespace='urn:brocade.com:mgmt:brocade-isis', defining_module='brocade-isis', yang_type='empty', is_config=True)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """connected_level12 must be of a type compatible with empty""",
          'defined-type': "empty",
          'generated-type': """YANGDynClass(base=YANGBool, is_leaf=True, yang_name="connected-level12", rest_name="level-1-2", parent=self, choice=(u'ch-connected-levels', u'ca-connected-level12'), path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'cli-full-command': None, u'info': u'IS-IS Level-1-2 routes', u'alt-name': u'level-1-2', u'cli-full-no': None}}, namespace='urn:brocade.com:mgmt:brocade-isis', defining_module='brocade-isis', yang_type='empty', is_config=True)""",
        })

    self.__connected_level12 = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_connected_level12(self):
    self.__connected_level12 = YANGDynClass(base=YANGBool, is_leaf=True, yang_name="connected-level12", rest_name="level-1-2", parent=self, choice=(u'ch-connected-levels', u'ca-connected-level12'), path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'cli-full-command': None, u'info': u'IS-IS Level-1-2 routes', u'alt-name': u'level-1-2', u'cli-full-no': None}}, namespace='urn:brocade.com:mgmt:brocade-isis', defining_module='brocade-isis', yang_type='empty', is_config=True)


  def _get_connected_metric_type(self):
    """
    Getter method for connected_metric_type, mapped from YANG variable /routing_system/router/isis/router_isis_cmds_holder/address_family/ipv4/af_ipv4_unicast/af_ipv4_attributes/af_common_attributes/redistribute/connected/connected_metric_type (is-metric-type-t)
    """
    return self.__connected_metric_type
      
  def _set_connected_metric_type(self, v, load=False):
    """
    Setter method for connected_metric_type, mapped from YANG variable /routing_system/router/isis/router_isis_cmds_holder/address_family/ipv4/af_ipv4_unicast/af_ipv4_attributes/af_common_attributes/redistribute/connected/connected_metric_type (is-metric-type-t)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_connected_metric_type is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_connected_metric_type() directly.
    """
    if hasattr(v, "_utype"):
      v = v._utype(v)
    try:
      t = YANGDynClass(v,base=RestrictedClassType(base_type=unicode,                                     restriction_type="dict_key",                                     restriction_arg={u'internal': {'value': 1}, u'external': {'value': 2}},), default=unicode("internal"), is_leaf=True, yang_name="connected-metric-type", rest_name="metric-type", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'info': u'IS-IS metric type for redistributed routes', u'alt-name': u'metric-type'}}, namespace='urn:brocade.com:mgmt:brocade-isis', defining_module='brocade-isis', yang_type='is-metric-type-t', is_config=True)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """connected_metric_type must be of a type compatible with is-metric-type-t""",
          'defined-type': "brocade-isis:is-metric-type-t",
          'generated-type': """YANGDynClass(base=RestrictedClassType(base_type=unicode,                                     restriction_type="dict_key",                                     restriction_arg={u'internal': {'value': 1}, u'external': {'value': 2}},), default=unicode("internal"), is_leaf=True, yang_name="connected-metric-type", rest_name="metric-type", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'info': u'IS-IS metric type for redistributed routes', u'alt-name': u'metric-type'}}, namespace='urn:brocade.com:mgmt:brocade-isis', defining_module='brocade-isis', yang_type='is-metric-type-t', is_config=True)""",
        })

    self.__connected_metric_type = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_connected_metric_type(self):
    self.__connected_metric_type = YANGDynClass(base=RestrictedClassType(base_type=unicode,                                     restriction_type="dict_key",                                     restriction_arg={u'internal': {'value': 1}, u'external': {'value': 2}},), default=unicode("internal"), is_leaf=True, yang_name="connected-metric-type", rest_name="metric-type", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'info': u'IS-IS metric type for redistributed routes', u'alt-name': u'metric-type'}}, namespace='urn:brocade.com:mgmt:brocade-isis', defining_module='brocade-isis', yang_type='is-metric-type-t', is_config=True)

  connected_metric = __builtin__.property(_get_connected_metric, _set_connected_metric)
  connected_route_map = __builtin__.property(_get_connected_route_map, _set_connected_route_map)
  connected_level1 = __builtin__.property(_get_connected_level1, _set_connected_level1)
  connected_level2 = __builtin__.property(_get_connected_level2, _set_connected_level2)
  connected_level12 = __builtin__.property(_get_connected_level12, _set_connected_level12)
  connected_metric_type = __builtin__.property(_get_connected_metric_type, _set_connected_metric_type)

  __choices__ = {u'ch-connected-levels': {u'ca-connected-level12': [u'connected_level12'], u'ca-connected-level2': [u'connected_level2'], u'ca-connected-level1': [u'connected_level1']}}
  _pyangbind_elements = {'connected_metric': connected_metric, 'connected_route_map': connected_route_map, 'connected_level1': connected_level1, 'connected_level2': connected_level2, 'connected_level12': connected_level12, 'connected_metric_type': connected_metric_type, }


