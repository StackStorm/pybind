
from operator import attrgetter
import pyangbind.lib.xpathhelper as xpathhelper
from pyangbind.lib.yangtypes import RestrictedPrecisionDecimalType, RestrictedClassType, TypedListType
from pyangbind.lib.yangtypes import YANGBool, YANGListType, YANGDynClass, ReferenceType
from pyangbind.lib.base import PybindBase
from decimal import Decimal
from bitarray import bitarray
import __builtin__
import threshold
import alert
class area(PybindBase):
  """
  This class was auto-generated by the PythonClass plugin for PYANG
  from YANG module brocade-threshold-monitor - based on the path /threshold-monitor-hidden/threshold-monitor/sfp/policy/area. Each member element of
  the container is represented as a class variable - with a specific
  YANG type.
  """
  __slots__ = ('_pybind_generated_by', '_path_helper', '_yang_name', '_rest_name', '_extmethods', '__type','__area_value','__threshold','__alert',)

  _yang_name = 'area'
  _rest_name = 'area'

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
    self.__threshold = YANGDynClass(base=threshold.threshold, is_container='container', presence=False, yang_name="threshold", rest_name="threshold", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'info': u'Threshold configuration', u'cli-compact-syntax': None, u'cli-suppress-show-conf-path': None, u'cli-incomplete-no': None}}, namespace='urn:brocade.com:mgmt:brocade-threshold-monitor', defining_module='brocade-threshold-monitor', yang_type='container', is_config=True)
    self.__area_value = YANGDynClass(base=RestrictedClassType(base_type=unicode,                                     restriction_type="dict_key",                                     restriction_arg={u'Current': {'value': 3}, u'RXP': {'value': 1}, u'Voltage': {'value': 4}, u'Temperature': {'value': 0}, u'TXP': {'value': 2}},), is_leaf=True, yang_name="area_value", rest_name="area", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'alt-name': u'area', u'cli-expose-key-name': None, u'cli-incomplete-command': None}}, is_keyval=True, namespace='urn:brocade.com:mgmt:brocade-threshold-monitor', defining_module='brocade-threshold-monitor', yang_type='enumeration', is_config=True)
    self.__type = YANGDynClass(base=RestrictedClassType(base_type=unicode,                                     restriction_type="dict_key",                                     restriction_arg={u'1GCOP': {'value': 2}, u'10GLR': {'value': 5}, u'1GLR': {'value': 1}, u'100GLRLT': {'value': 16}, u'10GSR': {'value': 4}, u'100GCWDM': {'value': 14}, u'100GAOC': {'value': 23}, u'1GCWDM': {'value': 18}, u'10GZR': {'value': 17}, u'40GESR': {'value': 9}, u'40GER': {'value': 20}, u'100GCLR': {'value': 15}, u'100GESR': {'value': 22}, u'40GLM': {'value': 21}, u'40GSRINT': {'value': 8}, u'40GLR': {'value': 10}, u'40GSR': {'value': 7}, u'1GSR': {'value': 0}, u'10GDWDMT': {'value': 19}, u'100GPSM': {'value': 13}, u'100GLR': {'value': 12}, u'100GSR': {'value': 11}, u'10GER': {'value': 6}, u'10GUSR': {'value': 3}},), is_leaf=True, yang_name="type", rest_name="type", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'info': u'SFP types that can be configured', u'cli-expose-key-name': None}}, is_keyval=True, namespace='urn:brocade.com:mgmt:brocade-threshold-monitor', defining_module='brocade-threshold-monitor', yang_type='enumeration', is_config=True)
    self.__alert = YANGDynClass(base=alert.alert, is_container='container', presence=False, yang_name="alert", rest_name="alert", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'info': u'Alert configuration', u'cli-suppress-show-conf-path': None, u'cli-incomplete-no': None}}, namespace='urn:brocade.com:mgmt:brocade-threshold-monitor', defining_module='brocade-threshold-monitor', yang_type='container', is_config=True)

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
      return [u'threshold-monitor-hidden', u'threshold-monitor', u'sfp', u'policy', u'area']

  def _rest_path(self):
    if hasattr(self, "_parent"):
      if self._rest_name:
        return self._parent._rest_path()+[self._rest_name]
      else:
        return self._parent._rest_path()
    else:
      return [u'threshold-monitor', u'sfp', u'policy', u'area']

  def _get_type(self):
    """
    Getter method for type, mapped from YANG variable /threshold_monitor_hidden/threshold_monitor/sfp/policy/area/type (enumeration)
    """
    return self.__type
      
  def _set_type(self, v, load=False):
    """
    Setter method for type, mapped from YANG variable /threshold_monitor_hidden/threshold_monitor/sfp/policy/area/type (enumeration)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_type is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_type() directly.
    """
    parent = getattr(self, "_parent", None)
    if parent is not None and load is False:
      raise AttributeError("Cannot set keys directly when" +
                             " within an instantiated list")

    if hasattr(v, "_utype"):
      v = v._utype(v)
    try:
      t = YANGDynClass(v,base=RestrictedClassType(base_type=unicode,                                     restriction_type="dict_key",                                     restriction_arg={u'1GCOP': {'value': 2}, u'10GLR': {'value': 5}, u'1GLR': {'value': 1}, u'100GLRLT': {'value': 16}, u'10GSR': {'value': 4}, u'100GCWDM': {'value': 14}, u'100GAOC': {'value': 23}, u'1GCWDM': {'value': 18}, u'10GZR': {'value': 17}, u'40GESR': {'value': 9}, u'40GER': {'value': 20}, u'100GCLR': {'value': 15}, u'100GESR': {'value': 22}, u'40GLM': {'value': 21}, u'40GSRINT': {'value': 8}, u'40GLR': {'value': 10}, u'40GSR': {'value': 7}, u'1GSR': {'value': 0}, u'10GDWDMT': {'value': 19}, u'100GPSM': {'value': 13}, u'100GLR': {'value': 12}, u'100GSR': {'value': 11}, u'10GER': {'value': 6}, u'10GUSR': {'value': 3}},), is_leaf=True, yang_name="type", rest_name="type", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'info': u'SFP types that can be configured', u'cli-expose-key-name': None}}, is_keyval=True, namespace='urn:brocade.com:mgmt:brocade-threshold-monitor', defining_module='brocade-threshold-monitor', yang_type='enumeration', is_config=True)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """type must be of a type compatible with enumeration""",
          'defined-type': "brocade-threshold-monitor:enumeration",
          'generated-type': """YANGDynClass(base=RestrictedClassType(base_type=unicode,                                     restriction_type="dict_key",                                     restriction_arg={u'1GCOP': {'value': 2}, u'10GLR': {'value': 5}, u'1GLR': {'value': 1}, u'100GLRLT': {'value': 16}, u'10GSR': {'value': 4}, u'100GCWDM': {'value': 14}, u'100GAOC': {'value': 23}, u'1GCWDM': {'value': 18}, u'10GZR': {'value': 17}, u'40GESR': {'value': 9}, u'40GER': {'value': 20}, u'100GCLR': {'value': 15}, u'100GESR': {'value': 22}, u'40GLM': {'value': 21}, u'40GSRINT': {'value': 8}, u'40GLR': {'value': 10}, u'40GSR': {'value': 7}, u'1GSR': {'value': 0}, u'10GDWDMT': {'value': 19}, u'100GPSM': {'value': 13}, u'100GLR': {'value': 12}, u'100GSR': {'value': 11}, u'10GER': {'value': 6}, u'10GUSR': {'value': 3}},), is_leaf=True, yang_name="type", rest_name="type", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'info': u'SFP types that can be configured', u'cli-expose-key-name': None}}, is_keyval=True, namespace='urn:brocade.com:mgmt:brocade-threshold-monitor', defining_module='brocade-threshold-monitor', yang_type='enumeration', is_config=True)""",
        })

    self.__type = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_type(self):
    self.__type = YANGDynClass(base=RestrictedClassType(base_type=unicode,                                     restriction_type="dict_key",                                     restriction_arg={u'1GCOP': {'value': 2}, u'10GLR': {'value': 5}, u'1GLR': {'value': 1}, u'100GLRLT': {'value': 16}, u'10GSR': {'value': 4}, u'100GCWDM': {'value': 14}, u'100GAOC': {'value': 23}, u'1GCWDM': {'value': 18}, u'10GZR': {'value': 17}, u'40GESR': {'value': 9}, u'40GER': {'value': 20}, u'100GCLR': {'value': 15}, u'100GESR': {'value': 22}, u'40GLM': {'value': 21}, u'40GSRINT': {'value': 8}, u'40GLR': {'value': 10}, u'40GSR': {'value': 7}, u'1GSR': {'value': 0}, u'10GDWDMT': {'value': 19}, u'100GPSM': {'value': 13}, u'100GLR': {'value': 12}, u'100GSR': {'value': 11}, u'10GER': {'value': 6}, u'10GUSR': {'value': 3}},), is_leaf=True, yang_name="type", rest_name="type", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'info': u'SFP types that can be configured', u'cli-expose-key-name': None}}, is_keyval=True, namespace='urn:brocade.com:mgmt:brocade-threshold-monitor', defining_module='brocade-threshold-monitor', yang_type='enumeration', is_config=True)


  def _get_area_value(self):
    """
    Getter method for area_value, mapped from YANG variable /threshold_monitor_hidden/threshold_monitor/sfp/policy/area/area_value (enumeration)
    """
    return self.__area_value
      
  def _set_area_value(self, v, load=False):
    """
    Setter method for area_value, mapped from YANG variable /threshold_monitor_hidden/threshold_monitor/sfp/policy/area/area_value (enumeration)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_area_value is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_area_value() directly.
    """
    parent = getattr(self, "_parent", None)
    if parent is not None and load is False:
      raise AttributeError("Cannot set keys directly when" +
                             " within an instantiated list")

    if hasattr(v, "_utype"):
      v = v._utype(v)
    try:
      t = YANGDynClass(v,base=RestrictedClassType(base_type=unicode,                                     restriction_type="dict_key",                                     restriction_arg={u'Current': {'value': 3}, u'RXP': {'value': 1}, u'Voltage': {'value': 4}, u'Temperature': {'value': 0}, u'TXP': {'value': 2}},), is_leaf=True, yang_name="area_value", rest_name="area", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'alt-name': u'area', u'cli-expose-key-name': None, u'cli-incomplete-command': None}}, is_keyval=True, namespace='urn:brocade.com:mgmt:brocade-threshold-monitor', defining_module='brocade-threshold-monitor', yang_type='enumeration', is_config=True)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """area_value must be of a type compatible with enumeration""",
          'defined-type': "brocade-threshold-monitor:enumeration",
          'generated-type': """YANGDynClass(base=RestrictedClassType(base_type=unicode,                                     restriction_type="dict_key",                                     restriction_arg={u'Current': {'value': 3}, u'RXP': {'value': 1}, u'Voltage': {'value': 4}, u'Temperature': {'value': 0}, u'TXP': {'value': 2}},), is_leaf=True, yang_name="area_value", rest_name="area", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'alt-name': u'area', u'cli-expose-key-name': None, u'cli-incomplete-command': None}}, is_keyval=True, namespace='urn:brocade.com:mgmt:brocade-threshold-monitor', defining_module='brocade-threshold-monitor', yang_type='enumeration', is_config=True)""",
        })

    self.__area_value = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_area_value(self):
    self.__area_value = YANGDynClass(base=RestrictedClassType(base_type=unicode,                                     restriction_type="dict_key",                                     restriction_arg={u'Current': {'value': 3}, u'RXP': {'value': 1}, u'Voltage': {'value': 4}, u'Temperature': {'value': 0}, u'TXP': {'value': 2}},), is_leaf=True, yang_name="area_value", rest_name="area", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'alt-name': u'area', u'cli-expose-key-name': None, u'cli-incomplete-command': None}}, is_keyval=True, namespace='urn:brocade.com:mgmt:brocade-threshold-monitor', defining_module='brocade-threshold-monitor', yang_type='enumeration', is_config=True)


  def _get_threshold(self):
    """
    Getter method for threshold, mapped from YANG variable /threshold_monitor_hidden/threshold_monitor/sfp/policy/area/threshold (container)
    """
    return self.__threshold
      
  def _set_threshold(self, v, load=False):
    """
    Setter method for threshold, mapped from YANG variable /threshold_monitor_hidden/threshold_monitor/sfp/policy/area/threshold (container)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_threshold is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_threshold() directly.
    """
    if hasattr(v, "_utype"):
      v = v._utype(v)
    try:
      t = YANGDynClass(v,base=threshold.threshold, is_container='container', presence=False, yang_name="threshold", rest_name="threshold", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'info': u'Threshold configuration', u'cli-compact-syntax': None, u'cli-suppress-show-conf-path': None, u'cli-incomplete-no': None}}, namespace='urn:brocade.com:mgmt:brocade-threshold-monitor', defining_module='brocade-threshold-monitor', yang_type='container', is_config=True)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """threshold must be of a type compatible with container""",
          'defined-type': "container",
          'generated-type': """YANGDynClass(base=threshold.threshold, is_container='container', presence=False, yang_name="threshold", rest_name="threshold", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'info': u'Threshold configuration', u'cli-compact-syntax': None, u'cli-suppress-show-conf-path': None, u'cli-incomplete-no': None}}, namespace='urn:brocade.com:mgmt:brocade-threshold-monitor', defining_module='brocade-threshold-monitor', yang_type='container', is_config=True)""",
        })

    self.__threshold = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_threshold(self):
    self.__threshold = YANGDynClass(base=threshold.threshold, is_container='container', presence=False, yang_name="threshold", rest_name="threshold", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'info': u'Threshold configuration', u'cli-compact-syntax': None, u'cli-suppress-show-conf-path': None, u'cli-incomplete-no': None}}, namespace='urn:brocade.com:mgmt:brocade-threshold-monitor', defining_module='brocade-threshold-monitor', yang_type='container', is_config=True)


  def _get_alert(self):
    """
    Getter method for alert, mapped from YANG variable /threshold_monitor_hidden/threshold_monitor/sfp/policy/area/alert (container)
    """
    return self.__alert
      
  def _set_alert(self, v, load=False):
    """
    Setter method for alert, mapped from YANG variable /threshold_monitor_hidden/threshold_monitor/sfp/policy/area/alert (container)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_alert is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_alert() directly.
    """
    if hasattr(v, "_utype"):
      v = v._utype(v)
    try:
      t = YANGDynClass(v,base=alert.alert, is_container='container', presence=False, yang_name="alert", rest_name="alert", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'info': u'Alert configuration', u'cli-suppress-show-conf-path': None, u'cli-incomplete-no': None}}, namespace='urn:brocade.com:mgmt:brocade-threshold-monitor', defining_module='brocade-threshold-monitor', yang_type='container', is_config=True)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """alert must be of a type compatible with container""",
          'defined-type': "container",
          'generated-type': """YANGDynClass(base=alert.alert, is_container='container', presence=False, yang_name="alert", rest_name="alert", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'info': u'Alert configuration', u'cli-suppress-show-conf-path': None, u'cli-incomplete-no': None}}, namespace='urn:brocade.com:mgmt:brocade-threshold-monitor', defining_module='brocade-threshold-monitor', yang_type='container', is_config=True)""",
        })

    self.__alert = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_alert(self):
    self.__alert = YANGDynClass(base=alert.alert, is_container='container', presence=False, yang_name="alert", rest_name="alert", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'info': u'Alert configuration', u'cli-suppress-show-conf-path': None, u'cli-incomplete-no': None}}, namespace='urn:brocade.com:mgmt:brocade-threshold-monitor', defining_module='brocade-threshold-monitor', yang_type='container', is_config=True)

  type = __builtin__.property(_get_type, _set_type)
  area_value = __builtin__.property(_get_area_value, _set_area_value)
  threshold = __builtin__.property(_get_threshold, _set_threshold)
  alert = __builtin__.property(_get_alert, _set_alert)


  _pyangbind_elements = {'type': type, 'area_value': area_value, 'threshold': threshold, 'alert': alert, }


