
from operator import attrgetter
import pyangbind.lib.xpathhelper as xpathhelper
from pyangbind.lib.yangtypes import RestrictedPrecisionDecimalType, RestrictedClassType, TypedListType
from pyangbind.lib.yangtypes import YANGBool, YANGListType, YANGDynClass, ReferenceType
from pyangbind.lib.base import PybindBase
from decimal import Decimal
from bitarray import bitarray
import __builtin__
import alert
class sfp(PybindBase):
  """
  This class was auto-generated by the PythonClass plugin for PYANG
  from YANG module brocade-rbridge - based on the path /rbridge-id/system-monitor/sfp. Each member element of
  the container is represented as a class variable - with a specific
  YANG type.
  """
  __slots__ = ('_pybind_generated_by', '_path_helper', '_yang_name', '_rest_name', '_extmethods', '__alert',)

  _yang_name = 'sfp'
  _rest_name = 'sfp'

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
    self.__alert = YANGDynClass(base=alert.alert, is_container='container', presence=False, yang_name="alert", rest_name="alert", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'info': u'Configure alerts for component:SFP', u'cli-compact-syntax': None, u'callpoint': u'smsetSfpAlert', u'cli-incomplete-no': None}}, namespace='urn:brocade.com:mgmt:brocade-system-monitor', defining_module='brocade-system-monitor', yang_type='container', is_config=True)

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
      return [u'rbridge-id', u'system-monitor', u'sfp']

  def _rest_path(self):
    if hasattr(self, "_parent"):
      if self._rest_name:
        return self._parent._rest_path()+[self._rest_name]
      else:
        return self._parent._rest_path()
    else:
      return [u'rbridge-id', u'system-monitor', u'sfp']

  def _get_alert(self):
    """
    Getter method for alert, mapped from YANG variable /rbridge_id/system_monitor/sfp/alert (container)
    """
    return self.__alert
      
  def _set_alert(self, v, load=False):
    """
    Setter method for alert, mapped from YANG variable /rbridge_id/system_monitor/sfp/alert (container)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_alert is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_alert() directly.
    """
    if hasattr(v, "_utype"):
      v = v._utype(v)
    try:
      t = YANGDynClass(v,base=alert.alert, is_container='container', presence=False, yang_name="alert", rest_name="alert", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'info': u'Configure alerts for component:SFP', u'cli-compact-syntax': None, u'callpoint': u'smsetSfpAlert', u'cli-incomplete-no': None}}, namespace='urn:brocade.com:mgmt:brocade-system-monitor', defining_module='brocade-system-monitor', yang_type='container', is_config=True)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """alert must be of a type compatible with container""",
          'defined-type': "container",
          'generated-type': """YANGDynClass(base=alert.alert, is_container='container', presence=False, yang_name="alert", rest_name="alert", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'info': u'Configure alerts for component:SFP', u'cli-compact-syntax': None, u'callpoint': u'smsetSfpAlert', u'cli-incomplete-no': None}}, namespace='urn:brocade.com:mgmt:brocade-system-monitor', defining_module='brocade-system-monitor', yang_type='container', is_config=True)""",
        })

    self.__alert = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_alert(self):
    self.__alert = YANGDynClass(base=alert.alert, is_container='container', presence=False, yang_name="alert", rest_name="alert", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'info': u'Configure alerts for component:SFP', u'cli-compact-syntax': None, u'callpoint': u'smsetSfpAlert', u'cli-incomplete-no': None}}, namespace='urn:brocade.com:mgmt:brocade-system-monitor', defining_module='brocade-system-monitor', yang_type='container', is_config=True)

  alert = __builtin__.property(_get_alert, _set_alert)


  _pyangbind_elements = {'alert': alert, }


