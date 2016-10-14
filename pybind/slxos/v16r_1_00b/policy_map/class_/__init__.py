
from operator import attrgetter
import pyangbind.lib.xpathhelper as xpathhelper
from pyangbind.lib.yangtypes import RestrictedPrecisionDecimalType, RestrictedClassType, TypedListType
from pyangbind.lib.yangtypes import YANGBool, YANGListType, YANGDynClass, ReferenceType
from pyangbind.lib.base import PybindBase
from decimal import Decimal
from bitarray import bitarray
import __builtin__
import police
import set_
import span
import map_
import shape
import scheduler
import priority_mapping_table
class class_(PybindBase):
  """
  This class was auto-generated by the PythonClass plugin for PYANG
  from YANG module brocade-qos-mqc - based on the path /policy-map/class. Each member element of
  the container is represented as a class variable - with a specific
  YANG type.
  """
  __slots__ = ('_pybind_generated_by', '_path_helper', '_yang_name', '_extmethods', '__cl_name','__police','__set_','__span','__map_','__sflow_profile','__shape','__scheduler','__priority_mapping_table',)

  _yang_name = 'class'

  _pybind_generated_by = 'container'

  def __init__(self, *args, **kwargs):

    helper = kwargs.pop("path_helper", None)
    if helper is False:
      self._path_helper = False
    elif helper is not None and isinstance(helper, xpathhelper.YANGPathHelper):
      self._path_helper = helper
    elif hasattr(self, "_parent"):
      helper = getattr(self._parent, "_path_helper", False)
      self._path_helper = helper
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
    self.__span = YANGDynClass(base=span.span, is_container='container', yang_name="span", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'info': u'span sesion <id>'}}, namespace='urn:brocade.com:mgmt:brocade-qos-mqc', defining_module='brocade-qos-mqc', yang_type='container', is_config=True)
    self.__scheduler = YANGDynClass(base=scheduler.scheduler, is_container='container', yang_name="scheduler", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'info': u'Configure Traffic Class Scheduler', u'cli-full-no': None}}, namespace='urn:brocade.com:mgmt:brocade-qos-mqc', defining_module='brocade-qos-mqc', yang_type='container', is_config=True)
    self.__sflow_profile = YANGDynClass(base=RestrictedClassType(base_type=unicode, restriction_dict={'pattern': u'[a-zA-Z]{1}([-a-zA-Z0-9_]{0,63})'}), is_leaf=True, yang_name="sflow-profile", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'cli-full-command': None, u'info': u'Apply sflow profile'}}, namespace='urn:brocade.com:mgmt:brocade-qos-mqc', defining_module='brocade-qos-mqc', yang_type='sflow:profile-name-type', is_config=True)
    self.__priority_mapping_table = YANGDynClass(base=priority_mapping_table.priority_mapping_table, is_container='container', yang_name="priority-mapping-table", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'info': u'Configure cee priority mapping table', u'cli-incomplete-command': None}}, namespace='urn:brocade.com:mgmt:brocade-qos-mqc', defining_module='brocade-qos-mqc', yang_type='container', is_config=True)
    self.__shape = YANGDynClass(base=shape.shape, is_container='container', yang_name="shape", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'info': u'Configure Shaping rate', u'cli-full-no': None}}, namespace='urn:brocade.com:mgmt:brocade-qos-mqc', defining_module='brocade-qos-mqc', yang_type='container', is_config=True)
    self.__cl_name = YANGDynClass(base=RestrictedClassType(base_type=unicode, restriction_dict={'pattern': u'[a-zA-Z]{1}([-a-zA-Z0-9_]{0,63})'}), is_leaf=True, yang_name="cl-name", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'info': u'Policy Map Class Name (Max Size -64)'}}, is_keyval=True, namespace='urn:brocade.com:mgmt:brocade-qos-mqc', defining_module='brocade-qos-mqc', yang_type='map-name-type', is_config=True)
    self.__police = YANGDynClass(base=police.police, is_container='container', yang_name="police", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'cli-compact-syntax': None, u'info': u'Policy Map Class Police Instance', u'cli-sequence-commands': None, u'cli-incomplete-command': None}}, namespace='urn:brocade.com:mgmt:brocade-qos-mqc', defining_module='brocade-qos-mqc', yang_type='container', is_config=True)
    self.__set_ = YANGDynClass(base=set_.set_, is_container='container', yang_name="set", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'info': u'set cos,traffic-class or dscp value', u'cli-compact-syntax': None, u'cli-incomplete-no': None}}, namespace='urn:brocade.com:mgmt:brocade-qos-mqc', defining_module='brocade-qos-mqc', yang_type='container', is_config=True)
    self.__map_ = YANGDynClass(base=map_.map_, is_container='container', yang_name="map", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'info': u'Configure QoS Map', u'cli-incomplete-no': None}}, namespace='urn:brocade.com:mgmt:brocade-qos-mqc', defining_module='brocade-qos-mqc', yang_type='container', is_config=True)

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
      return [u'policy-map', u'class']

  def _rest_path(self):
    if hasattr(self, "_supplied_register_path"):
      return [self._supplied_register_path]
    if hasattr(self, "_parent"):
      return self._parent._rest_path()+[self._yang_name]
    else:
      return [u'policy-map', u'class']

  def _get_cl_name(self):
    """
    Getter method for cl_name, mapped from YANG variable /policy_map/class/cl_name (map-name-type)
    """
    return self.__cl_name
      
  def _set_cl_name(self, v, load=False):
    """
    Setter method for cl_name, mapped from YANG variable /policy_map/class/cl_name (map-name-type)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_cl_name is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_cl_name() directly.
    """
    parent = getattr(self, "_parent", None)
    if parent is not None and load is False:
      raise AttributeError("Cannot set keys directly when" +
                             " within an instantiated list")

    try:
      t = YANGDynClass(v,base=RestrictedClassType(base_type=unicode, restriction_dict={'pattern': u'[a-zA-Z]{1}([-a-zA-Z0-9_]{0,63})'}), is_leaf=True, yang_name="cl-name", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'info': u'Policy Map Class Name (Max Size -64)'}}, is_keyval=True, namespace='urn:brocade.com:mgmt:brocade-qos-mqc', defining_module='brocade-qos-mqc', yang_type='map-name-type', is_config=True)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """cl_name must be of a type compatible with map-name-type""",
          'defined-type': "brocade-qos-mqc:map-name-type",
          'generated-type': """YANGDynClass(base=RestrictedClassType(base_type=unicode, restriction_dict={'pattern': u'[a-zA-Z]{1}([-a-zA-Z0-9_]{0,63})'}), is_leaf=True, yang_name="cl-name", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'info': u'Policy Map Class Name (Max Size -64)'}}, is_keyval=True, namespace='urn:brocade.com:mgmt:brocade-qos-mqc', defining_module='brocade-qos-mqc', yang_type='map-name-type', is_config=True)""",
        })

    self.__cl_name = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_cl_name(self):
    self.__cl_name = YANGDynClass(base=RestrictedClassType(base_type=unicode, restriction_dict={'pattern': u'[a-zA-Z]{1}([-a-zA-Z0-9_]{0,63})'}), is_leaf=True, yang_name="cl-name", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'info': u'Policy Map Class Name (Max Size -64)'}}, is_keyval=True, namespace='urn:brocade.com:mgmt:brocade-qos-mqc', defining_module='brocade-qos-mqc', yang_type='map-name-type', is_config=True)


  def _get_police(self):
    """
    Getter method for police, mapped from YANG variable /policy_map/class/police (container)
    """
    return self.__police
      
  def _set_police(self, v, load=False):
    """
    Setter method for police, mapped from YANG variable /policy_map/class/police (container)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_police is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_police() directly.
    """
    try:
      t = YANGDynClass(v,base=police.police, is_container='container', yang_name="police", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'cli-compact-syntax': None, u'info': u'Policy Map Class Police Instance', u'cli-sequence-commands': None, u'cli-incomplete-command': None}}, namespace='urn:brocade.com:mgmt:brocade-qos-mqc', defining_module='brocade-qos-mqc', yang_type='container', is_config=True)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """police must be of a type compatible with container""",
          'defined-type': "container",
          'generated-type': """YANGDynClass(base=police.police, is_container='container', yang_name="police", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'cli-compact-syntax': None, u'info': u'Policy Map Class Police Instance', u'cli-sequence-commands': None, u'cli-incomplete-command': None}}, namespace='urn:brocade.com:mgmt:brocade-qos-mqc', defining_module='brocade-qos-mqc', yang_type='container', is_config=True)""",
        })

    self.__police = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_police(self):
    self.__police = YANGDynClass(base=police.police, is_container='container', yang_name="police", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'cli-compact-syntax': None, u'info': u'Policy Map Class Police Instance', u'cli-sequence-commands': None, u'cli-incomplete-command': None}}, namespace='urn:brocade.com:mgmt:brocade-qos-mqc', defining_module='brocade-qos-mqc', yang_type='container', is_config=True)


  def _get_set_(self):
    """
    Getter method for set_, mapped from YANG variable /policy_map/class/set (container)
    """
    return self.__set_
      
  def _set_set_(self, v, load=False):
    """
    Setter method for set_, mapped from YANG variable /policy_map/class/set (container)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_set_ is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_set_() directly.
    """
    try:
      t = YANGDynClass(v,base=set_.set_, is_container='container', yang_name="set", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'info': u'set cos,traffic-class or dscp value', u'cli-compact-syntax': None, u'cli-incomplete-no': None}}, namespace='urn:brocade.com:mgmt:brocade-qos-mqc', defining_module='brocade-qos-mqc', yang_type='container', is_config=True)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """set_ must be of a type compatible with container""",
          'defined-type': "container",
          'generated-type': """YANGDynClass(base=set_.set_, is_container='container', yang_name="set", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'info': u'set cos,traffic-class or dscp value', u'cli-compact-syntax': None, u'cli-incomplete-no': None}}, namespace='urn:brocade.com:mgmt:brocade-qos-mqc', defining_module='brocade-qos-mqc', yang_type='container', is_config=True)""",
        })

    self.__set_ = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_set_(self):
    self.__set_ = YANGDynClass(base=set_.set_, is_container='container', yang_name="set", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'info': u'set cos,traffic-class or dscp value', u'cli-compact-syntax': None, u'cli-incomplete-no': None}}, namespace='urn:brocade.com:mgmt:brocade-qos-mqc', defining_module='brocade-qos-mqc', yang_type='container', is_config=True)


  def _get_span(self):
    """
    Getter method for span, mapped from YANG variable /policy_map/class/span (container)

    YANG Description: span sesion <id>
    """
    return self.__span
      
  def _set_span(self, v, load=False):
    """
    Setter method for span, mapped from YANG variable /policy_map/class/span (container)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_span is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_span() directly.

    YANG Description: span sesion <id>
    """
    try:
      t = YANGDynClass(v,base=span.span, is_container='container', yang_name="span", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'info': u'span sesion <id>'}}, namespace='urn:brocade.com:mgmt:brocade-qos-mqc', defining_module='brocade-qos-mqc', yang_type='container', is_config=True)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """span must be of a type compatible with container""",
          'defined-type': "container",
          'generated-type': """YANGDynClass(base=span.span, is_container='container', yang_name="span", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'info': u'span sesion <id>'}}, namespace='urn:brocade.com:mgmt:brocade-qos-mqc', defining_module='brocade-qos-mqc', yang_type='container', is_config=True)""",
        })

    self.__span = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_span(self):
    self.__span = YANGDynClass(base=span.span, is_container='container', yang_name="span", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'info': u'span sesion <id>'}}, namespace='urn:brocade.com:mgmt:brocade-qos-mqc', defining_module='brocade-qos-mqc', yang_type='container', is_config=True)


  def _get_map_(self):
    """
    Getter method for map_, mapped from YANG variable /policy_map/class/map (container)
    """
    return self.__map_
      
  def _set_map_(self, v, load=False):
    """
    Setter method for map_, mapped from YANG variable /policy_map/class/map (container)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_map_ is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_map_() directly.
    """
    try:
      t = YANGDynClass(v,base=map_.map_, is_container='container', yang_name="map", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'info': u'Configure QoS Map', u'cli-incomplete-no': None}}, namespace='urn:brocade.com:mgmt:brocade-qos-mqc', defining_module='brocade-qos-mqc', yang_type='container', is_config=True)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """map_ must be of a type compatible with container""",
          'defined-type': "container",
          'generated-type': """YANGDynClass(base=map_.map_, is_container='container', yang_name="map", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'info': u'Configure QoS Map', u'cli-incomplete-no': None}}, namespace='urn:brocade.com:mgmt:brocade-qos-mqc', defining_module='brocade-qos-mqc', yang_type='container', is_config=True)""",
        })

    self.__map_ = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_map_(self):
    self.__map_ = YANGDynClass(base=map_.map_, is_container='container', yang_name="map", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'info': u'Configure QoS Map', u'cli-incomplete-no': None}}, namespace='urn:brocade.com:mgmt:brocade-qos-mqc', defining_module='brocade-qos-mqc', yang_type='container', is_config=True)


  def _get_sflow_profile(self):
    """
    Getter method for sflow_profile, mapped from YANG variable /policy_map/class/sflow_profile (sflow:profile-name-type)

    YANG Description: This applies sflow profile.
    """
    return self.__sflow_profile
      
  def _set_sflow_profile(self, v, load=False):
    """
    Setter method for sflow_profile, mapped from YANG variable /policy_map/class/sflow_profile (sflow:profile-name-type)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_sflow_profile is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_sflow_profile() directly.

    YANG Description: This applies sflow profile.
    """
    try:
      t = YANGDynClass(v,base=RestrictedClassType(base_type=unicode, restriction_dict={'pattern': u'[a-zA-Z]{1}([-a-zA-Z0-9_]{0,63})'}), is_leaf=True, yang_name="sflow-profile", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'cli-full-command': None, u'info': u'Apply sflow profile'}}, namespace='urn:brocade.com:mgmt:brocade-qos-mqc', defining_module='brocade-qos-mqc', yang_type='sflow:profile-name-type', is_config=True)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """sflow_profile must be of a type compatible with sflow:profile-name-type""",
          'defined-type': "sflow:profile-name-type",
          'generated-type': """YANGDynClass(base=RestrictedClassType(base_type=unicode, restriction_dict={'pattern': u'[a-zA-Z]{1}([-a-zA-Z0-9_]{0,63})'}), is_leaf=True, yang_name="sflow-profile", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'cli-full-command': None, u'info': u'Apply sflow profile'}}, namespace='urn:brocade.com:mgmt:brocade-qos-mqc', defining_module='brocade-qos-mqc', yang_type='sflow:profile-name-type', is_config=True)""",
        })

    self.__sflow_profile = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_sflow_profile(self):
    self.__sflow_profile = YANGDynClass(base=RestrictedClassType(base_type=unicode, restriction_dict={'pattern': u'[a-zA-Z]{1}([-a-zA-Z0-9_]{0,63})'}), is_leaf=True, yang_name="sflow-profile", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'cli-full-command': None, u'info': u'Apply sflow profile'}}, namespace='urn:brocade.com:mgmt:brocade-qos-mqc', defining_module='brocade-qos-mqc', yang_type='sflow:profile-name-type', is_config=True)


  def _get_shape(self):
    """
    Getter method for shape, mapped from YANG variable /policy_map/class/shape (container)
    """
    return self.__shape
      
  def _set_shape(self, v, load=False):
    """
    Setter method for shape, mapped from YANG variable /policy_map/class/shape (container)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_shape is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_shape() directly.
    """
    try:
      t = YANGDynClass(v,base=shape.shape, is_container='container', yang_name="shape", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'info': u'Configure Shaping rate', u'cli-full-no': None}}, namespace='urn:brocade.com:mgmt:brocade-qos-mqc', defining_module='brocade-qos-mqc', yang_type='container', is_config=True)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """shape must be of a type compatible with container""",
          'defined-type': "container",
          'generated-type': """YANGDynClass(base=shape.shape, is_container='container', yang_name="shape", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'info': u'Configure Shaping rate', u'cli-full-no': None}}, namespace='urn:brocade.com:mgmt:brocade-qos-mqc', defining_module='brocade-qos-mqc', yang_type='container', is_config=True)""",
        })

    self.__shape = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_shape(self):
    self.__shape = YANGDynClass(base=shape.shape, is_container='container', yang_name="shape", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'info': u'Configure Shaping rate', u'cli-full-no': None}}, namespace='urn:brocade.com:mgmt:brocade-qos-mqc', defining_module='brocade-qos-mqc', yang_type='container', is_config=True)


  def _get_scheduler(self):
    """
    Getter method for scheduler, mapped from YANG variable /policy_map/class/scheduler (container)
    """
    return self.__scheduler
      
  def _set_scheduler(self, v, load=False):
    """
    Setter method for scheduler, mapped from YANG variable /policy_map/class/scheduler (container)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_scheduler is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_scheduler() directly.
    """
    try:
      t = YANGDynClass(v,base=scheduler.scheduler, is_container='container', yang_name="scheduler", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'info': u'Configure Traffic Class Scheduler', u'cli-full-no': None}}, namespace='urn:brocade.com:mgmt:brocade-qos-mqc', defining_module='brocade-qos-mqc', yang_type='container', is_config=True)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """scheduler must be of a type compatible with container""",
          'defined-type': "container",
          'generated-type': """YANGDynClass(base=scheduler.scheduler, is_container='container', yang_name="scheduler", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'info': u'Configure Traffic Class Scheduler', u'cli-full-no': None}}, namespace='urn:brocade.com:mgmt:brocade-qos-mqc', defining_module='brocade-qos-mqc', yang_type='container', is_config=True)""",
        })

    self.__scheduler = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_scheduler(self):
    self.__scheduler = YANGDynClass(base=scheduler.scheduler, is_container='container', yang_name="scheduler", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'info': u'Configure Traffic Class Scheduler', u'cli-full-no': None}}, namespace='urn:brocade.com:mgmt:brocade-qos-mqc', defining_module='brocade-qos-mqc', yang_type='container', is_config=True)


  def _get_priority_mapping_table(self):
    """
    Getter method for priority_mapping_table, mapped from YANG variable /policy_map/class/priority_mapping_table (container)
    """
    return self.__priority_mapping_table
      
  def _set_priority_mapping_table(self, v, load=False):
    """
    Setter method for priority_mapping_table, mapped from YANG variable /policy_map/class/priority_mapping_table (container)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_priority_mapping_table is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_priority_mapping_table() directly.
    """
    try:
      t = YANGDynClass(v,base=priority_mapping_table.priority_mapping_table, is_container='container', yang_name="priority-mapping-table", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'info': u'Configure cee priority mapping table', u'cli-incomplete-command': None}}, namespace='urn:brocade.com:mgmt:brocade-qos-mqc', defining_module='brocade-qos-mqc', yang_type='container', is_config=True)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """priority_mapping_table must be of a type compatible with container""",
          'defined-type': "container",
          'generated-type': """YANGDynClass(base=priority_mapping_table.priority_mapping_table, is_container='container', yang_name="priority-mapping-table", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'info': u'Configure cee priority mapping table', u'cli-incomplete-command': None}}, namespace='urn:brocade.com:mgmt:brocade-qos-mqc', defining_module='brocade-qos-mqc', yang_type='container', is_config=True)""",
        })

    self.__priority_mapping_table = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_priority_mapping_table(self):
    self.__priority_mapping_table = YANGDynClass(base=priority_mapping_table.priority_mapping_table, is_container='container', yang_name="priority-mapping-table", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'info': u'Configure cee priority mapping table', u'cli-incomplete-command': None}}, namespace='urn:brocade.com:mgmt:brocade-qos-mqc', defining_module='brocade-qos-mqc', yang_type='container', is_config=True)

  cl_name = __builtin__.property(_get_cl_name, _set_cl_name)
  police = __builtin__.property(_get_police, _set_police)
  set_ = __builtin__.property(_get_set_, _set_set_)
  span = __builtin__.property(_get_span, _set_span)
  map_ = __builtin__.property(_get_map_, _set_map_)
  sflow_profile = __builtin__.property(_get_sflow_profile, _set_sflow_profile)
  shape = __builtin__.property(_get_shape, _set_shape)
  scheduler = __builtin__.property(_get_scheduler, _set_scheduler)
  priority_mapping_table = __builtin__.property(_get_priority_mapping_table, _set_priority_mapping_table)


  _pyangbind_elements = {'cl_name': cl_name, 'police': police, 'set_': set_, 'span': span, 'map_': map_, 'sflow_profile': sflow_profile, 'shape': shape, 'scheduler': scheduler, 'priority_mapping_table': priority_mapping_table, }

