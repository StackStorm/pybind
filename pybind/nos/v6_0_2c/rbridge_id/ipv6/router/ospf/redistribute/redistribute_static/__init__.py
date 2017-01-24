
from operator import attrgetter
import pyangbind.lib.xpathhelper as xpathhelper
from pyangbind.lib.yangtypes import RestrictedPrecisionDecimalType, RestrictedClassType, TypedListType
from pyangbind.lib.yangtypes import YANGBool, YANGListType, YANGDynClass, ReferenceType
from pyangbind.lib.base import PybindBase
from decimal import Decimal
from bitarray import bitarray
import __builtin__
class redistribute_static(PybindBase):
  """
  This class was auto-generated by the PythonClass plugin for PYANG
  from YANG module brocade-rbridge - based on the path /rbridge-id/ipv6/router/ospf/redistribute/redistribute-static. Each member element of
  the container is represented as a class variable - with a specific
  YANG type.

  YANG Description: Static routes
  """
  __slots__ = ('_pybind_generated_by', '_path_helper', '_yang_name', '_rest_name', '_extmethods', '__static_route_map','__redistribute_static_metric','__redistribute_static_metric_type',)

  _yang_name = 'redistribute-static'
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
    self.__redistribute_static_metric_type = YANGDynClass(base=RestrictedClassType(base_type=unicode,                                     restriction_type="dict_key",                                     restriction_arg={u'type1': {'value': 1}, u'type2': {'value': 2}},), is_leaf=True, yang_name="redistribute-static-metric-type", rest_name="metric-type", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'cli-full-command': None, u'info': u'Type of the metric', u'alt-name': u'metric-type'}}, namespace='urn:brocade.com:mgmt:brocade-ospfv3', defining_module='brocade-ospfv3', yang_type='ospf:metric-type', is_config=True)
    self.__static_route_map = YANGDynClass(base=RestrictedClassType(base_type=unicode, restriction_dict={'pattern': u'[a-zA-Z]{1}([-a-zA-Z0-9\\.\\\\\\\\@#\\+\\*\\(\\)=\\{~\\}%<>=$_\\[\\]\\|]{0,62})'}), is_leaf=True, yang_name="static-route-map", rest_name="route-map", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'info': u'Route map reference', u'alt-name': u'route-map'}}, namespace='urn:brocade.com:mgmt:brocade-ospfv3', defining_module='brocade-ospfv3', yang_type='common-def:name-string63', is_config=True)
    self.__redistribute_static_metric = YANGDynClass(base=RestrictedClassType(base_type=RestrictedClassType(base_type=long, restriction_dict={'range': ['0..4294967295']}, int_size=32), restriction_dict={'range': [u'0..65535']}), is_leaf=True, yang_name="redistribute-static-metric", rest_name="metric", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'cli-full-command': None, u'info': u'Route metric', u'alt-name': u'metric'}}, namespace='urn:brocade.com:mgmt:brocade-ospfv3', defining_module='brocade-ospfv3', yang_type='uint32', is_config=True)

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
      return [u'rbridge-id', u'ipv6', u'router', u'ospf', u'redistribute', u'redistribute-static']

  def _rest_path(self):
    if hasattr(self, "_parent"):
      if self._rest_name:
        return self._parent._rest_path()+[self._rest_name]
      else:
        return self._parent._rest_path()
    else:
      return [u'rbridge-id', u'ipv6', u'router', u'ospf', u'redistribute', u'static']

  def _get_static_route_map(self):
    """
    Getter method for static_route_map, mapped from YANG variable /rbridge_id/ipv6/router/ospf/redistribute/redistribute_static/static_route_map (common-def:name-string63)

    YANG Description: Route map reference
    """
    return self.__static_route_map
      
  def _set_static_route_map(self, v, load=False):
    """
    Setter method for static_route_map, mapped from YANG variable /rbridge_id/ipv6/router/ospf/redistribute/redistribute_static/static_route_map (common-def:name-string63)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_static_route_map is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_static_route_map() directly.

    YANG Description: Route map reference
    """
    if hasattr(v, "_utype"):
      v = v._utype(v)
    try:
      t = YANGDynClass(v,base=RestrictedClassType(base_type=unicode, restriction_dict={'pattern': u'[a-zA-Z]{1}([-a-zA-Z0-9\\.\\\\\\\\@#\\+\\*\\(\\)=\\{~\\}%<>=$_\\[\\]\\|]{0,62})'}), is_leaf=True, yang_name="static-route-map", rest_name="route-map", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'info': u'Route map reference', u'alt-name': u'route-map'}}, namespace='urn:brocade.com:mgmt:brocade-ospfv3', defining_module='brocade-ospfv3', yang_type='common-def:name-string63', is_config=True)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """static_route_map must be of a type compatible with common-def:name-string63""",
          'defined-type': "common-def:name-string63",
          'generated-type': """YANGDynClass(base=RestrictedClassType(base_type=unicode, restriction_dict={'pattern': u'[a-zA-Z]{1}([-a-zA-Z0-9\\.\\\\\\\\@#\\+\\*\\(\\)=\\{~\\}%<>=$_\\[\\]\\|]{0,62})'}), is_leaf=True, yang_name="static-route-map", rest_name="route-map", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'info': u'Route map reference', u'alt-name': u'route-map'}}, namespace='urn:brocade.com:mgmt:brocade-ospfv3', defining_module='brocade-ospfv3', yang_type='common-def:name-string63', is_config=True)""",
        })

    self.__static_route_map = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_static_route_map(self):
    self.__static_route_map = YANGDynClass(base=RestrictedClassType(base_type=unicode, restriction_dict={'pattern': u'[a-zA-Z]{1}([-a-zA-Z0-9\\.\\\\\\\\@#\\+\\*\\(\\)=\\{~\\}%<>=$_\\[\\]\\|]{0,62})'}), is_leaf=True, yang_name="static-route-map", rest_name="route-map", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'info': u'Route map reference', u'alt-name': u'route-map'}}, namespace='urn:brocade.com:mgmt:brocade-ospfv3', defining_module='brocade-ospfv3', yang_type='common-def:name-string63', is_config=True)


  def _get_redistribute_static_metric(self):
    """
    Getter method for redistribute_static_metric, mapped from YANG variable /rbridge_id/ipv6/router/ospf/redistribute/redistribute_static/redistribute_static_metric (uint32)

    YANG Description: Specifies the metric used for the redistributed route. If not specified and the value for thedefault-metric command is set to 0, its default metric, then routes redistributed from the variousrouting protocols will have the metric value of the protocol from which they are redistributed.
    """
    return self.__redistribute_static_metric
      
  def _set_redistribute_static_metric(self, v, load=False):
    """
    Setter method for redistribute_static_metric, mapped from YANG variable /rbridge_id/ipv6/router/ospf/redistribute/redistribute_static/redistribute_static_metric (uint32)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_redistribute_static_metric is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_redistribute_static_metric() directly.

    YANG Description: Specifies the metric used for the redistributed route. If not specified and the value for thedefault-metric command is set to 0, its default metric, then routes redistributed from the variousrouting protocols will have the metric value of the protocol from which they are redistributed.
    """
    if hasattr(v, "_utype"):
      v = v._utype(v)
    try:
      t = YANGDynClass(v,base=RestrictedClassType(base_type=RestrictedClassType(base_type=long, restriction_dict={'range': ['0..4294967295']}, int_size=32), restriction_dict={'range': [u'0..65535']}), is_leaf=True, yang_name="redistribute-static-metric", rest_name="metric", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'cli-full-command': None, u'info': u'Route metric', u'alt-name': u'metric'}}, namespace='urn:brocade.com:mgmt:brocade-ospfv3', defining_module='brocade-ospfv3', yang_type='uint32', is_config=True)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """redistribute_static_metric must be of a type compatible with uint32""",
          'defined-type': "uint32",
          'generated-type': """YANGDynClass(base=RestrictedClassType(base_type=RestrictedClassType(base_type=long, restriction_dict={'range': ['0..4294967295']}, int_size=32), restriction_dict={'range': [u'0..65535']}), is_leaf=True, yang_name="redistribute-static-metric", rest_name="metric", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'cli-full-command': None, u'info': u'Route metric', u'alt-name': u'metric'}}, namespace='urn:brocade.com:mgmt:brocade-ospfv3', defining_module='brocade-ospfv3', yang_type='uint32', is_config=True)""",
        })

    self.__redistribute_static_metric = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_redistribute_static_metric(self):
    self.__redistribute_static_metric = YANGDynClass(base=RestrictedClassType(base_type=RestrictedClassType(base_type=long, restriction_dict={'range': ['0..4294967295']}, int_size=32), restriction_dict={'range': [u'0..65535']}), is_leaf=True, yang_name="redistribute-static-metric", rest_name="metric", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'cli-full-command': None, u'info': u'Route metric', u'alt-name': u'metric'}}, namespace='urn:brocade.com:mgmt:brocade-ospfv3', defining_module='brocade-ospfv3', yang_type='uint32', is_config=True)


  def _get_redistribute_static_metric_type(self):
    """
    Getter method for redistribute_static_metric_type, mapped from YANG variable /rbridge_id/ipv6/router/ospf/redistribute/redistribute_static/redistribute_static_metric_type (ospf:metric-type)

    YANG Description: Specifies an OSPF metric type (type 1 or type 2) for the redistributed route.If not specified, the device uses the value specified by the metric-type command.
    """
    return self.__redistribute_static_metric_type
      
  def _set_redistribute_static_metric_type(self, v, load=False):
    """
    Setter method for redistribute_static_metric_type, mapped from YANG variable /rbridge_id/ipv6/router/ospf/redistribute/redistribute_static/redistribute_static_metric_type (ospf:metric-type)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_redistribute_static_metric_type is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_redistribute_static_metric_type() directly.

    YANG Description: Specifies an OSPF metric type (type 1 or type 2) for the redistributed route.If not specified, the device uses the value specified by the metric-type command.
    """
    if hasattr(v, "_utype"):
      v = v._utype(v)
    try:
      t = YANGDynClass(v,base=RestrictedClassType(base_type=unicode,                                     restriction_type="dict_key",                                     restriction_arg={u'type1': {'value': 1}, u'type2': {'value': 2}},), is_leaf=True, yang_name="redistribute-static-metric-type", rest_name="metric-type", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'cli-full-command': None, u'info': u'Type of the metric', u'alt-name': u'metric-type'}}, namespace='urn:brocade.com:mgmt:brocade-ospfv3', defining_module='brocade-ospfv3', yang_type='ospf:metric-type', is_config=True)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """redistribute_static_metric_type must be of a type compatible with ospf:metric-type""",
          'defined-type': "ospf:metric-type",
          'generated-type': """YANGDynClass(base=RestrictedClassType(base_type=unicode,                                     restriction_type="dict_key",                                     restriction_arg={u'type1': {'value': 1}, u'type2': {'value': 2}},), is_leaf=True, yang_name="redistribute-static-metric-type", rest_name="metric-type", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'cli-full-command': None, u'info': u'Type of the metric', u'alt-name': u'metric-type'}}, namespace='urn:brocade.com:mgmt:brocade-ospfv3', defining_module='brocade-ospfv3', yang_type='ospf:metric-type', is_config=True)""",
        })

    self.__redistribute_static_metric_type = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_redistribute_static_metric_type(self):
    self.__redistribute_static_metric_type = YANGDynClass(base=RestrictedClassType(base_type=unicode,                                     restriction_type="dict_key",                                     restriction_arg={u'type1': {'value': 1}, u'type2': {'value': 2}},), is_leaf=True, yang_name="redistribute-static-metric-type", rest_name="metric-type", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'cli-full-command': None, u'info': u'Type of the metric', u'alt-name': u'metric-type'}}, namespace='urn:brocade.com:mgmt:brocade-ospfv3', defining_module='brocade-ospfv3', yang_type='ospf:metric-type', is_config=True)

  static_route_map = __builtin__.property(_get_static_route_map, _set_static_route_map)
  redistribute_static_metric = __builtin__.property(_get_redistribute_static_metric, _set_redistribute_static_metric)
  redistribute_static_metric_type = __builtin__.property(_get_redistribute_static_metric_type, _set_redistribute_static_metric_type)


  _pyangbind_elements = {'static_route_map': static_route_map, 'redistribute_static_metric': redistribute_static_metric, 'redistribute_static_metric_type': redistribute_static_metric_type, }

