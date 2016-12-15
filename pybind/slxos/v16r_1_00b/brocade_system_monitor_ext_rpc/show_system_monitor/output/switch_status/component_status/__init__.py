
from operator import attrgetter
import pyangbind.lib.xpathhelper as xpathhelper
from pyangbind.lib.yangtypes import RestrictedPrecisionDecimalType, RestrictedClassType, TypedListType
from pyangbind.lib.yangtypes import YANGBool, YANGListType, YANGDynClass, ReferenceType
from pyangbind.lib.base import PybindBase
from decimal import Decimal
from bitarray import bitarray
import __builtin__
class component_status(PybindBase):
  """
  This class was auto-generated by the PythonClass plugin for PYANG
  from YANG module brocade-system-monitor-ext - based on the path /brocade_system_monitor_ext_rpc/show-system-monitor/output/switch-status/component-status. Each member element of
  the container is represented as a class variable - with a specific
  YANG type.
  """
  __slots__ = ('_pybind_generated_by', '_path_helper', '_yang_name', '_rest_name', '_extmethods', '__component_name','__component_state',)

  _yang_name = 'component-status'
  _rest_name = 'component-status'

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
    self.__component_state = YANGDynClass(base=RestrictedClassType(base_type=unicode,                                     restriction_type="dict_key",                                     restriction_arg={u'state-healthy': {}, u'state-unknown': {}, u'state-unmonitored': {}, u'state-down': {}, u'state-marginal': {}},), is_leaf=True, yang_name="component-state", rest_name="component-state", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=False, namespace='urn:brocade.com:mgmt:brocade-system-monitor-ext', defining_module='brocade-system-monitor-ext', yang_type='system-monitor-health-state-enum', is_config=True)
    self.__component_name = YANGDynClass(base=unicode, is_leaf=True, yang_name="component-name", rest_name="component-name", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=False, namespace='urn:brocade.com:mgmt:brocade-system-monitor-ext', defining_module='brocade-system-monitor-ext', yang_type='string', is_config=True)

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
      return [u'brocade_system_monitor_ext_rpc', u'show-system-monitor', u'output', u'switch-status', u'component-status']

  def _rest_path(self):
    if hasattr(self, "_parent"):
      if self._rest_name:
        return self._parent._rest_path()+[self._rest_name]
      else:
        return self._parent._rest_path()
    else:
      return [u'show-system-monitor', u'output', u'switch-status', u'component-status']

  def _get_component_name(self):
    """
    Getter method for component_name, mapped from YANG variable /brocade_system_monitor_ext_rpc/show_system_monitor/output/switch_status/component_status/component_name (string)

    YANG Description: component name
    """
    return self.__component_name
      
  def _set_component_name(self, v, load=False):
    """
    Setter method for component_name, mapped from YANG variable /brocade_system_monitor_ext_rpc/show_system_monitor/output/switch_status/component_status/component_name (string)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_component_name is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_component_name() directly.

    YANG Description: component name
    """
    if hasattr(v, "_utype"):
      v = v._utype(v)
    try:
      t = YANGDynClass(v,base=unicode, is_leaf=True, yang_name="component-name", rest_name="component-name", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=False, namespace='urn:brocade.com:mgmt:brocade-system-monitor-ext', defining_module='brocade-system-monitor-ext', yang_type='string', is_config=True)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """component_name must be of a type compatible with string""",
          'defined-type': "string",
          'generated-type': """YANGDynClass(base=unicode, is_leaf=True, yang_name="component-name", rest_name="component-name", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=False, namespace='urn:brocade.com:mgmt:brocade-system-monitor-ext', defining_module='brocade-system-monitor-ext', yang_type='string', is_config=True)""",
        })

    self.__component_name = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_component_name(self):
    self.__component_name = YANGDynClass(base=unicode, is_leaf=True, yang_name="component-name", rest_name="component-name", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=False, namespace='urn:brocade.com:mgmt:brocade-system-monitor-ext', defining_module='brocade-system-monitor-ext', yang_type='string', is_config=True)


  def _get_component_state(self):
    """
    Getter method for component_state, mapped from YANG variable /brocade_system_monitor_ext_rpc/show_system_monitor/output/switch_status/component_status/component_state (system-monitor-health-state-enum)

    YANG Description: component status based on thresholds
    """
    return self.__component_state
      
  def _set_component_state(self, v, load=False):
    """
    Setter method for component_state, mapped from YANG variable /brocade_system_monitor_ext_rpc/show_system_monitor/output/switch_status/component_status/component_state (system-monitor-health-state-enum)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_component_state is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_component_state() directly.

    YANG Description: component status based on thresholds
    """
    if hasattr(v, "_utype"):
      v = v._utype(v)
    try:
      t = YANGDynClass(v,base=RestrictedClassType(base_type=unicode,                                     restriction_type="dict_key",                                     restriction_arg={u'state-healthy': {}, u'state-unknown': {}, u'state-unmonitored': {}, u'state-down': {}, u'state-marginal': {}},), is_leaf=True, yang_name="component-state", rest_name="component-state", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=False, namespace='urn:brocade.com:mgmt:brocade-system-monitor-ext', defining_module='brocade-system-monitor-ext', yang_type='system-monitor-health-state-enum', is_config=True)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """component_state must be of a type compatible with system-monitor-health-state-enum""",
          'defined-type': "brocade-system-monitor-ext:system-monitor-health-state-enum",
          'generated-type': """YANGDynClass(base=RestrictedClassType(base_type=unicode,                                     restriction_type="dict_key",                                     restriction_arg={u'state-healthy': {}, u'state-unknown': {}, u'state-unmonitored': {}, u'state-down': {}, u'state-marginal': {}},), is_leaf=True, yang_name="component-state", rest_name="component-state", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=False, namespace='urn:brocade.com:mgmt:brocade-system-monitor-ext', defining_module='brocade-system-monitor-ext', yang_type='system-monitor-health-state-enum', is_config=True)""",
        })

    self.__component_state = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_component_state(self):
    self.__component_state = YANGDynClass(base=RestrictedClassType(base_type=unicode,                                     restriction_type="dict_key",                                     restriction_arg={u'state-healthy': {}, u'state-unknown': {}, u'state-unmonitored': {}, u'state-down': {}, u'state-marginal': {}},), is_leaf=True, yang_name="component-state", rest_name="component-state", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=False, namespace='urn:brocade.com:mgmt:brocade-system-monitor-ext', defining_module='brocade-system-monitor-ext', yang_type='system-monitor-health-state-enum', is_config=True)

  component_name = __builtin__.property(_get_component_name, _set_component_name)
  component_state = __builtin__.property(_get_component_state, _set_component_state)


  _pyangbind_elements = {'component_name': component_name, 'component_state': component_state, }


