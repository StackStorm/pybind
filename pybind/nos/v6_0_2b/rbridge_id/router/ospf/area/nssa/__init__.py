
from operator import attrgetter
import pyangbind.lib.xpathhelper as xpathhelper
from pyangbind.lib.yangtypes import RestrictedPrecisionDecimalType, RestrictedClassType, TypedListType
from pyangbind.lib.yangtypes import YANGBool, YANGListType, YANGDynClass, ReferenceType
from pyangbind.lib.base import PybindBase
from decimal import Decimal
from bitarray import bitarray
import __builtin__
import metric
class nssa(PybindBase):
  """
  This class was auto-generated by the PythonClass plugin for PYANG
  from YANG module brocade-rbridge - based on the path /rbridge-id/router/ospf/area/nssa. Each member element of
  the container is represented as a class variable - with a specific
  YANG type.
  """
  __slots__ = ('_pybind_generated_by', '_path_helper', '_yang_name', '_rest_name', '_extmethods', '__metric','__default_information_originate',)

  _yang_name = 'nssa'
  _rest_name = 'nssa'

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
    self.__metric = YANGDynClass(base=metric.metric, is_container='container', presence=False, yang_name="metric", rest_name="", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'cli-compact-syntax': None, u'cli-drop-node-name': None, u'cli-sequence-commands': None}}, namespace='urn:brocade.com:mgmt:brocade-ospf', defining_module='brocade-ospf', yang_type='container', is_config=True)
    self.__default_information_originate = YANGDynClass(base=YANGBool, is_leaf=True, yang_name="default-information-originate", rest_name="default-information-originate", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'cli-full-command': None, u'info': u'Originate default-information'}}, namespace='urn:brocade.com:mgmt:brocade-ospf', defining_module='brocade-ospf', yang_type='empty', is_config=True)

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
      return [u'rbridge-id', u'router', u'ospf', u'area', u'nssa']

  def _rest_path(self):
    if hasattr(self, "_parent"):
      if self._rest_name:
        return self._parent._rest_path()+[self._rest_name]
      else:
        return self._parent._rest_path()
    else:
      return [u'rbridge-id', u'router', u'ospf', u'area', u'nssa']

  def _get_metric(self):
    """
    Getter method for metric, mapped from YANG variable /rbridge_id/router/ospf/area/nssa/metric (container)
    """
    return self.__metric
      
  def _set_metric(self, v, load=False):
    """
    Setter method for metric, mapped from YANG variable /rbridge_id/router/ospf/area/nssa/metric (container)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_metric is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_metric() directly.
    """
    if hasattr(v, "_utype"):
      v = v._utype(v)
    try:
      t = YANGDynClass(v,base=metric.metric, is_container='container', presence=False, yang_name="metric", rest_name="", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'cli-compact-syntax': None, u'cli-drop-node-name': None, u'cli-sequence-commands': None}}, namespace='urn:brocade.com:mgmt:brocade-ospf', defining_module='brocade-ospf', yang_type='container', is_config=True)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """metric must be of a type compatible with container""",
          'defined-type': "container",
          'generated-type': """YANGDynClass(base=metric.metric, is_container='container', presence=False, yang_name="metric", rest_name="", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'cli-compact-syntax': None, u'cli-drop-node-name': None, u'cli-sequence-commands': None}}, namespace='urn:brocade.com:mgmt:brocade-ospf', defining_module='brocade-ospf', yang_type='container', is_config=True)""",
        })

    self.__metric = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_metric(self):
    self.__metric = YANGDynClass(base=metric.metric, is_container='container', presence=False, yang_name="metric", rest_name="", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'cli-compact-syntax': None, u'cli-drop-node-name': None, u'cli-sequence-commands': None}}, namespace='urn:brocade.com:mgmt:brocade-ospf', defining_module='brocade-ospf', yang_type='container', is_config=True)


  def _get_default_information_originate(self):
    """
    Getter method for default_information_originate, mapped from YANG variable /rbridge_id/router/ospf/area/nssa/default_information_originate (empty)
    """
    return self.__default_information_originate
      
  def _set_default_information_originate(self, v, load=False):
    """
    Setter method for default_information_originate, mapped from YANG variable /rbridge_id/router/ospf/area/nssa/default_information_originate (empty)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_default_information_originate is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_default_information_originate() directly.
    """
    if hasattr(v, "_utype"):
      v = v._utype(v)
    try:
      t = YANGDynClass(v,base=YANGBool, is_leaf=True, yang_name="default-information-originate", rest_name="default-information-originate", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'cli-full-command': None, u'info': u'Originate default-information'}}, namespace='urn:brocade.com:mgmt:brocade-ospf', defining_module='brocade-ospf', yang_type='empty', is_config=True)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """default_information_originate must be of a type compatible with empty""",
          'defined-type': "empty",
          'generated-type': """YANGDynClass(base=YANGBool, is_leaf=True, yang_name="default-information-originate", rest_name="default-information-originate", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'cli-full-command': None, u'info': u'Originate default-information'}}, namespace='urn:brocade.com:mgmt:brocade-ospf', defining_module='brocade-ospf', yang_type='empty', is_config=True)""",
        })

    self.__default_information_originate = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_default_information_originate(self):
    self.__default_information_originate = YANGDynClass(base=YANGBool, is_leaf=True, yang_name="default-information-originate", rest_name="default-information-originate", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'cli-full-command': None, u'info': u'Originate default-information'}}, namespace='urn:brocade.com:mgmt:brocade-ospf', defining_module='brocade-ospf', yang_type='empty', is_config=True)

  metric = __builtin__.property(_get_metric, _set_metric)
  default_information_originate = __builtin__.property(_get_default_information_originate, _set_default_information_originate)


  _pyangbind_elements = {'metric': metric, 'default_information_originate': default_information_originate, }


