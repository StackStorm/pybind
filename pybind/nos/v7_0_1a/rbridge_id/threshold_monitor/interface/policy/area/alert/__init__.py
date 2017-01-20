
from operator import attrgetter
import pyangbind.lib.xpathhelper as xpathhelper
from pyangbind.lib.yangtypes import RestrictedPrecisionDecimalType, RestrictedClassType, TypedListType
from pyangbind.lib.yangtypes import YANGBool, YANGListType, YANGDynClass, ReferenceType
from pyangbind.lib.base import PybindBase
from decimal import Decimal
from bitarray import bitarray
import __builtin__
import above
import below
class alert(PybindBase):
  """
  This class was auto-generated by the PythonClass plugin for PYANG
  from YANG module brocade-rbridge - based on the path /rbridge-id/threshold-monitor/interface/policy/area/alert. Each member element of
  the container is represented as a class variable - with a specific
  YANG type.
  """
  __slots__ = ('_pybind_generated_by', '_path_helper', '_yang_name', '_rest_name', '_extmethods', '__above','__below',)

  _yang_name = 'alert'
  _rest_name = 'alert'

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
    self.__below = YANGDynClass(base=below.below, is_container='container', presence=False, yang_name="below", rest_name="below", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'info': u'Below trigger', u'cli-incomplete-no': None}}, namespace='urn:brocade.com:mgmt:brocade-threshold-monitor', defining_module='brocade-threshold-monitor', yang_type='container', is_config=True)
    self.__above = YANGDynClass(base=above.above, is_container='container', presence=False, yang_name="above", rest_name="above", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'info': u'Above trigger', u'cli-incomplete-no': None}}, namespace='urn:brocade.com:mgmt:brocade-threshold-monitor', defining_module='brocade-threshold-monitor', yang_type='container', is_config=True)

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
      return [u'rbridge-id', u'threshold-monitor', u'interface', u'policy', u'area', u'alert']

  def _rest_path(self):
    if hasattr(self, "_parent"):
      if self._rest_name:
        return self._parent._rest_path()+[self._rest_name]
      else:
        return self._parent._rest_path()
    else:
      return [u'rbridge-id', u'threshold-monitor', u'interface', u'policy', u'alert']

  def _get_above(self):
    """
    Getter method for above, mapped from YANG variable /rbridge_id/threshold_monitor/interface/policy/area/alert/above (container)
    """
    return self.__above
      
  def _set_above(self, v, load=False):
    """
    Setter method for above, mapped from YANG variable /rbridge_id/threshold_monitor/interface/policy/area/alert/above (container)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_above is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_above() directly.
    """
    if hasattr(v, "_utype"):
      v = v._utype(v)
    try:
      t = YANGDynClass(v,base=above.above, is_container='container', presence=False, yang_name="above", rest_name="above", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'info': u'Above trigger', u'cli-incomplete-no': None}}, namespace='urn:brocade.com:mgmt:brocade-threshold-monitor', defining_module='brocade-threshold-monitor', yang_type='container', is_config=True)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """above must be of a type compatible with container""",
          'defined-type': "container",
          'generated-type': """YANGDynClass(base=above.above, is_container='container', presence=False, yang_name="above", rest_name="above", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'info': u'Above trigger', u'cli-incomplete-no': None}}, namespace='urn:brocade.com:mgmt:brocade-threshold-monitor', defining_module='brocade-threshold-monitor', yang_type='container', is_config=True)""",
        })

    self.__above = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_above(self):
    self.__above = YANGDynClass(base=above.above, is_container='container', presence=False, yang_name="above", rest_name="above", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'info': u'Above trigger', u'cli-incomplete-no': None}}, namespace='urn:brocade.com:mgmt:brocade-threshold-monitor', defining_module='brocade-threshold-monitor', yang_type='container', is_config=True)


  def _get_below(self):
    """
    Getter method for below, mapped from YANG variable /rbridge_id/threshold_monitor/interface/policy/area/alert/below (container)
    """
    return self.__below
      
  def _set_below(self, v, load=False):
    """
    Setter method for below, mapped from YANG variable /rbridge_id/threshold_monitor/interface/policy/area/alert/below (container)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_below is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_below() directly.
    """
    if hasattr(v, "_utype"):
      v = v._utype(v)
    try:
      t = YANGDynClass(v,base=below.below, is_container='container', presence=False, yang_name="below", rest_name="below", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'info': u'Below trigger', u'cli-incomplete-no': None}}, namespace='urn:brocade.com:mgmt:brocade-threshold-monitor', defining_module='brocade-threshold-monitor', yang_type='container', is_config=True)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """below must be of a type compatible with container""",
          'defined-type': "container",
          'generated-type': """YANGDynClass(base=below.below, is_container='container', presence=False, yang_name="below", rest_name="below", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'info': u'Below trigger', u'cli-incomplete-no': None}}, namespace='urn:brocade.com:mgmt:brocade-threshold-monitor', defining_module='brocade-threshold-monitor', yang_type='container', is_config=True)""",
        })

    self.__below = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_below(self):
    self.__below = YANGDynClass(base=below.below, is_container='container', presence=False, yang_name="below", rest_name="below", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'info': u'Below trigger', u'cli-incomplete-no': None}}, namespace='urn:brocade.com:mgmt:brocade-threshold-monitor', defining_module='brocade-threshold-monitor', yang_type='container', is_config=True)

  above = __builtin__.property(_get_above, _set_above)
  below = __builtin__.property(_get_below, _set_below)


  _pyangbind_elements = {'above': above, 'below': below, }


