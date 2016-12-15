
from operator import attrgetter
import pyangbind.lib.xpathhelper as xpathhelper
from pyangbind.lib.yangtypes import RestrictedPrecisionDecimalType, RestrictedClassType, TypedListType
from pyangbind.lib.yangtypes import YANGBool, YANGListType, YANGDynClass, ReferenceType
from pyangbind.lib.base import PybindBase
from decimal import Decimal
from bitarray import bitarray
import __builtin__
class metric(PybindBase):
  """
  This class was auto-generated by the PythonClass plugin for PYANG
  from YANG module brocade-rbridge - based on the path /rbridge-id/route-map/content/set/metric. Each member element of
  the container is represented as a class variable - with a specific
  YANG type.

  YANG Description: Route metric.
  """
  __slots__ = ('_pybind_generated_by', '_path_helper', '_yang_name', '_rest_name', '_extmethods', '__delta_rms','__metric_rms',)

  _yang_name = 'metric'
  _rest_name = 'metric'

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
    self.__delta_rms = YANGDynClass(base=RestrictedClassType(base_type=unicode,                                     restriction_type="dict_key",                                     restriction_arg={u'add': {'value': 1}, u'assign': {'value': 3}, u'none': {'value': 4}, u'sub': {'value': 2}},), is_leaf=True, yang_name="delta-rms", rest_name="", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'cli-drop-node-name': None}}, namespace='urn:brocade.com:mgmt:brocade-ip-policy', defining_module='brocade-ip-policy', yang_type='enumeration', is_config=True)
    self.__metric_rms = YANGDynClass(base=RestrictedClassType(base_type=RestrictedClassType(base_type=long, restriction_dict={'range': ['0..4294967295']}, int_size=32), restriction_dict={'range': [u'0..4294967295']}), is_leaf=True, yang_name="metric-rms", rest_name="", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'cli-drop-node-name': None}}, namespace='urn:brocade.com:mgmt:brocade-ip-policy', defining_module='brocade-ip-policy', yang_type='metric-t', is_config=True)

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
      return [u'rbridge-id', u'route-map', u'content', u'set', u'metric']

  def _rest_path(self):
    if hasattr(self, "_parent"):
      if self._rest_name:
        return self._parent._rest_path()+[self._rest_name]
      else:
        return self._parent._rest_path()
    else:
      return [u'rbridge-id', u'route-map', u'set', u'metric']

  def _get_delta_rms(self):
    """
    Getter method for delta_rms, mapped from YANG variable /rbridge_id/route_map/content/set/metric/delta_rms (enumeration)
    """
    return self.__delta_rms
      
  def _set_delta_rms(self, v, load=False):
    """
    Setter method for delta_rms, mapped from YANG variable /rbridge_id/route_map/content/set/metric/delta_rms (enumeration)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_delta_rms is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_delta_rms() directly.
    """
    if hasattr(v, "_utype"):
      v = v._utype(v)
    try:
      t = YANGDynClass(v,base=RestrictedClassType(base_type=unicode,                                     restriction_type="dict_key",                                     restriction_arg={u'add': {'value': 1}, u'assign': {'value': 3}, u'none': {'value': 4}, u'sub': {'value': 2}},), is_leaf=True, yang_name="delta-rms", rest_name="", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'cli-drop-node-name': None}}, namespace='urn:brocade.com:mgmt:brocade-ip-policy', defining_module='brocade-ip-policy', yang_type='enumeration', is_config=True)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """delta_rms must be of a type compatible with enumeration""",
          'defined-type': "brocade-ip-policy:enumeration",
          'generated-type': """YANGDynClass(base=RestrictedClassType(base_type=unicode,                                     restriction_type="dict_key",                                     restriction_arg={u'add': {'value': 1}, u'assign': {'value': 3}, u'none': {'value': 4}, u'sub': {'value': 2}},), is_leaf=True, yang_name="delta-rms", rest_name="", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'cli-drop-node-name': None}}, namespace='urn:brocade.com:mgmt:brocade-ip-policy', defining_module='brocade-ip-policy', yang_type='enumeration', is_config=True)""",
        })

    self.__delta_rms = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_delta_rms(self):
    self.__delta_rms = YANGDynClass(base=RestrictedClassType(base_type=unicode,                                     restriction_type="dict_key",                                     restriction_arg={u'add': {'value': 1}, u'assign': {'value': 3}, u'none': {'value': 4}, u'sub': {'value': 2}},), is_leaf=True, yang_name="delta-rms", rest_name="", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'cli-drop-node-name': None}}, namespace='urn:brocade.com:mgmt:brocade-ip-policy', defining_module='brocade-ip-policy', yang_type='enumeration', is_config=True)


  def _get_metric_rms(self):
    """
    Getter method for metric_rms, mapped from YANG variable /rbridge_id/route_map/content/set/metric/metric_rms (metric-t)
    """
    return self.__metric_rms
      
  def _set_metric_rms(self, v, load=False):
    """
    Setter method for metric_rms, mapped from YANG variable /rbridge_id/route_map/content/set/metric/metric_rms (metric-t)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_metric_rms is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_metric_rms() directly.
    """
    if hasattr(v, "_utype"):
      v = v._utype(v)
    try:
      t = YANGDynClass(v,base=RestrictedClassType(base_type=RestrictedClassType(base_type=long, restriction_dict={'range': ['0..4294967295']}, int_size=32), restriction_dict={'range': [u'0..4294967295']}), is_leaf=True, yang_name="metric-rms", rest_name="", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'cli-drop-node-name': None}}, namespace='urn:brocade.com:mgmt:brocade-ip-policy', defining_module='brocade-ip-policy', yang_type='metric-t', is_config=True)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """metric_rms must be of a type compatible with metric-t""",
          'defined-type': "brocade-ip-policy:metric-t",
          'generated-type': """YANGDynClass(base=RestrictedClassType(base_type=RestrictedClassType(base_type=long, restriction_dict={'range': ['0..4294967295']}, int_size=32), restriction_dict={'range': [u'0..4294967295']}), is_leaf=True, yang_name="metric-rms", rest_name="", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'cli-drop-node-name': None}}, namespace='urn:brocade.com:mgmt:brocade-ip-policy', defining_module='brocade-ip-policy', yang_type='metric-t', is_config=True)""",
        })

    self.__metric_rms = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_metric_rms(self):
    self.__metric_rms = YANGDynClass(base=RestrictedClassType(base_type=RestrictedClassType(base_type=long, restriction_dict={'range': ['0..4294967295']}, int_size=32), restriction_dict={'range': [u'0..4294967295']}), is_leaf=True, yang_name="metric-rms", rest_name="", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'cli-drop-node-name': None}}, namespace='urn:brocade.com:mgmt:brocade-ip-policy', defining_module='brocade-ip-policy', yang_type='metric-t', is_config=True)

  delta_rms = __builtin__.property(_get_delta_rms, _set_delta_rms)
  metric_rms = __builtin__.property(_get_metric_rms, _set_metric_rms)


  _pyangbind_elements = {'delta_rms': delta_rms, 'metric_rms': metric_rms, }


