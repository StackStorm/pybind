
from operator import attrgetter
import pyangbind.lib.xpathhelper as xpathhelper
from pyangbind.lib.yangtypes import RestrictedPrecisionDecimalType, RestrictedClassType, TypedListType
from pyangbind.lib.yangtypes import YANGBool, YANGListType, YANGDynClass, ReferenceType
from pyangbind.lib.base import PybindBase
from decimal import Decimal
from bitarray import bitarray
import __builtin__
import trigger_function_container
class name(PybindBase):
  """
  This class was auto-generated by the PythonClass plugin for PYANG
  from YANG module brocade-event-handler - based on the path /event-handler/activate/name. Each member element of
  the container is represented as a class variable - with a specific
  YANG type.
  """
  __slots__ = ('_pybind_generated_by', '_path_helper', '_yang_name', '_rest_name', '_extmethods', '__name','__delay','__iterations','__interval','__run_mode','__trigger_mode','__trigger_function_container',)

  _yang_name = 'name'
  _rest_name = ''

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
    self.__name = YANGDynClass(base=RestrictedClassType(base_type=unicode, restriction_dict={'pattern': u'[a-zA-Z]{1}([-a-zA-Z0-9\\.\\\\\\\\@#\\+\\*\\(\\)=\\{~\\}%<>=$_\\[\\]\\|]{0,31})'}), is_leaf=True, yang_name="name", rest_name="name", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'info': u'Event handler name'}}, is_keyval=True, namespace='urn:brocade.com:mgmt:brocade-event-handler', defining_module='brocade-event-handler', yang_type='common-def:name-string32', is_config=True)
    self.__interval = YANGDynClass(base=RestrictedClassType(base_type=long, restriction_dict={'range': ['0..4294967295']}, int_size=32), default=RestrictedClassType(base_type=long, restriction_dict={'range': ['0..4294967295']}, int_size=32)(0), is_leaf=True, yang_name="interval", rest_name="interval", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'info': u'Time (in seconds) that the event-handler will wait between iterations of completing the previous action (default = 0).'}}, namespace='urn:brocade.com:mgmt:brocade-event-handler', defining_module='brocade-event-handler', yang_type='uint32', is_config=True)
    self.__trigger_function_container = YANGDynClass(base=trigger_function_container.trigger_function_container, is_container='container', presence=False, yang_name="trigger-function-container", rest_name="", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'cli-compact-syntax': None, u'cli-drop-node-name': None, u'cli-sequence-commands': None}}, namespace='urn:brocade.com:mgmt:brocade-event-handler', defining_module='brocade-event-handler', yang_type='container', is_config=True)
    self.__trigger_mode = YANGDynClass(base=RestrictedClassType(base_type=unicode,                                     restriction_type="dict_key",                                     restriction_arg={u'each-instance': {'value': 1}, u'only-once': {'value': 3}, u'on-first-instance': {'value': 2}},), default=unicode("each-instance"), is_leaf=True, yang_name="trigger-mode", rest_name="trigger-mode", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'info': u'Trigger-mode controls how the action is launched with the configured event trigger (default = each-instance).'}}, namespace='urn:brocade.com:mgmt:brocade-event-handler', defining_module='brocade-event-handler', yang_type='enumeration', is_config=True)
    self.__delay = YANGDynClass(base=RestrictedClassType(base_type=long, restriction_dict={'range': ['0..4294967295']}, int_size=32), default=RestrictedClassType(base_type=long, restriction_dict={'range': ['0..4294967295']}, int_size=32)(0), is_leaf=True, yang_name="delay", rest_name="delay", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'info': u'Delay (in seconds) that the event-handler will wait, for the initial launch of the action after the trigger has been received (default = 0).'}}, namespace='urn:brocade.com:mgmt:brocade-event-handler', defining_module='brocade-event-handler', yang_type='uint32', is_config=True)
    self.__iterations = YANGDynClass(base=RestrictedClassType(base_type=long, restriction_dict={'range': ['0..4294967295']}, int_size=32), default=RestrictedClassType(base_type=long, restriction_dict={'range': ['0..4294967295']}, int_size=32)(1), is_leaf=True, yang_name="iterations", rest_name="iterations", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'info': u'Number of times to launch the action after the initial trigger has been received (default = 1).'}}, namespace='urn:brocade.com:mgmt:brocade-event-handler', defining_module='brocade-event-handler', yang_type='uint32', is_config=True)
    self.__run_mode = YANGDynClass(base=RestrictedClassType(base_type=unicode,                                     restriction_type="dict_key",                                     restriction_arg={u'exclusive': {'value': 1}, u'non-exclusive': {'value': 2}},), default=unicode("non-exclusive"), is_leaf=True, yang_name="run-mode", rest_name="run-mode", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'info': u'Run-mode controls how the action is launched with cluster formation (default = non-exclusive).'}}, namespace='urn:brocade.com:mgmt:brocade-event-handler', defining_module='brocade-event-handler', yang_type='enumeration', is_config=True)

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
      return [u'event-handler', u'activate', u'name']

  def _rest_path(self):
    if hasattr(self, "_parent"):
      if self._rest_name:
        return self._parent._rest_path()+[self._rest_name]
      else:
        return self._parent._rest_path()
    else:
      return [u'event-handler', u'activate']

  def _get_name(self):
    """
    Getter method for name, mapped from YANG variable /event_handler/activate/name/name (common-def:name-string32)

    YANG Description: Event handler name
    """
    return self.__name
      
  def _set_name(self, v, load=False):
    """
    Setter method for name, mapped from YANG variable /event_handler/activate/name/name (common-def:name-string32)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_name is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_name() directly.

    YANG Description: Event handler name
    """
    parent = getattr(self, "_parent", None)
    if parent is not None and load is False:
      raise AttributeError("Cannot set keys directly when" +
                             " within an instantiated list")

    if hasattr(v, "_utype"):
      v = v._utype(v)
    try:
      t = YANGDynClass(v,base=RestrictedClassType(base_type=unicode, restriction_dict={'pattern': u'[a-zA-Z]{1}([-a-zA-Z0-9\\.\\\\\\\\@#\\+\\*\\(\\)=\\{~\\}%<>=$_\\[\\]\\|]{0,31})'}), is_leaf=True, yang_name="name", rest_name="name", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'info': u'Event handler name'}}, is_keyval=True, namespace='urn:brocade.com:mgmt:brocade-event-handler', defining_module='brocade-event-handler', yang_type='common-def:name-string32', is_config=True)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """name must be of a type compatible with common-def:name-string32""",
          'defined-type': "common-def:name-string32",
          'generated-type': """YANGDynClass(base=RestrictedClassType(base_type=unicode, restriction_dict={'pattern': u'[a-zA-Z]{1}([-a-zA-Z0-9\\.\\\\\\\\@#\\+\\*\\(\\)=\\{~\\}%<>=$_\\[\\]\\|]{0,31})'}), is_leaf=True, yang_name="name", rest_name="name", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'info': u'Event handler name'}}, is_keyval=True, namespace='urn:brocade.com:mgmt:brocade-event-handler', defining_module='brocade-event-handler', yang_type='common-def:name-string32', is_config=True)""",
        })

    self.__name = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_name(self):
    self.__name = YANGDynClass(base=RestrictedClassType(base_type=unicode, restriction_dict={'pattern': u'[a-zA-Z]{1}([-a-zA-Z0-9\\.\\\\\\\\@#\\+\\*\\(\\)=\\{~\\}%<>=$_\\[\\]\\|]{0,31})'}), is_leaf=True, yang_name="name", rest_name="name", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'info': u'Event handler name'}}, is_keyval=True, namespace='urn:brocade.com:mgmt:brocade-event-handler', defining_module='brocade-event-handler', yang_type='common-def:name-string32', is_config=True)


  def _get_delay(self):
    """
    Getter method for delay, mapped from YANG variable /event_handler/activate/name/delay (uint32)
    """
    return self.__delay
      
  def _set_delay(self, v, load=False):
    """
    Setter method for delay, mapped from YANG variable /event_handler/activate/name/delay (uint32)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_delay is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_delay() directly.
    """
    if hasattr(v, "_utype"):
      v = v._utype(v)
    try:
      t = YANGDynClass(v,base=RestrictedClassType(base_type=long, restriction_dict={'range': ['0..4294967295']}, int_size=32), default=RestrictedClassType(base_type=long, restriction_dict={'range': ['0..4294967295']}, int_size=32)(0), is_leaf=True, yang_name="delay", rest_name="delay", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'info': u'Delay (in seconds) that the event-handler will wait, for the initial launch of the action after the trigger has been received (default = 0).'}}, namespace='urn:brocade.com:mgmt:brocade-event-handler', defining_module='brocade-event-handler', yang_type='uint32', is_config=True)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """delay must be of a type compatible with uint32""",
          'defined-type': "uint32",
          'generated-type': """YANGDynClass(base=RestrictedClassType(base_type=long, restriction_dict={'range': ['0..4294967295']}, int_size=32), default=RestrictedClassType(base_type=long, restriction_dict={'range': ['0..4294967295']}, int_size=32)(0), is_leaf=True, yang_name="delay", rest_name="delay", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'info': u'Delay (in seconds) that the event-handler will wait, for the initial launch of the action after the trigger has been received (default = 0).'}}, namespace='urn:brocade.com:mgmt:brocade-event-handler', defining_module='brocade-event-handler', yang_type='uint32', is_config=True)""",
        })

    self.__delay = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_delay(self):
    self.__delay = YANGDynClass(base=RestrictedClassType(base_type=long, restriction_dict={'range': ['0..4294967295']}, int_size=32), default=RestrictedClassType(base_type=long, restriction_dict={'range': ['0..4294967295']}, int_size=32)(0), is_leaf=True, yang_name="delay", rest_name="delay", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'info': u'Delay (in seconds) that the event-handler will wait, for the initial launch of the action after the trigger has been received (default = 0).'}}, namespace='urn:brocade.com:mgmt:brocade-event-handler', defining_module='brocade-event-handler', yang_type='uint32', is_config=True)


  def _get_iterations(self):
    """
    Getter method for iterations, mapped from YANG variable /event_handler/activate/name/iterations (uint32)
    """
    return self.__iterations
      
  def _set_iterations(self, v, load=False):
    """
    Setter method for iterations, mapped from YANG variable /event_handler/activate/name/iterations (uint32)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_iterations is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_iterations() directly.
    """
    if hasattr(v, "_utype"):
      v = v._utype(v)
    try:
      t = YANGDynClass(v,base=RestrictedClassType(base_type=long, restriction_dict={'range': ['0..4294967295']}, int_size=32), default=RestrictedClassType(base_type=long, restriction_dict={'range': ['0..4294967295']}, int_size=32)(1), is_leaf=True, yang_name="iterations", rest_name="iterations", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'info': u'Number of times to launch the action after the initial trigger has been received (default = 1).'}}, namespace='urn:brocade.com:mgmt:brocade-event-handler', defining_module='brocade-event-handler', yang_type='uint32', is_config=True)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """iterations must be of a type compatible with uint32""",
          'defined-type': "uint32",
          'generated-type': """YANGDynClass(base=RestrictedClassType(base_type=long, restriction_dict={'range': ['0..4294967295']}, int_size=32), default=RestrictedClassType(base_type=long, restriction_dict={'range': ['0..4294967295']}, int_size=32)(1), is_leaf=True, yang_name="iterations", rest_name="iterations", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'info': u'Number of times to launch the action after the initial trigger has been received (default = 1).'}}, namespace='urn:brocade.com:mgmt:brocade-event-handler', defining_module='brocade-event-handler', yang_type='uint32', is_config=True)""",
        })

    self.__iterations = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_iterations(self):
    self.__iterations = YANGDynClass(base=RestrictedClassType(base_type=long, restriction_dict={'range': ['0..4294967295']}, int_size=32), default=RestrictedClassType(base_type=long, restriction_dict={'range': ['0..4294967295']}, int_size=32)(1), is_leaf=True, yang_name="iterations", rest_name="iterations", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'info': u'Number of times to launch the action after the initial trigger has been received (default = 1).'}}, namespace='urn:brocade.com:mgmt:brocade-event-handler', defining_module='brocade-event-handler', yang_type='uint32', is_config=True)


  def _get_interval(self):
    """
    Getter method for interval, mapped from YANG variable /event_handler/activate/name/interval (uint32)
    """
    return self.__interval
      
  def _set_interval(self, v, load=False):
    """
    Setter method for interval, mapped from YANG variable /event_handler/activate/name/interval (uint32)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_interval is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_interval() directly.
    """
    if hasattr(v, "_utype"):
      v = v._utype(v)
    try:
      t = YANGDynClass(v,base=RestrictedClassType(base_type=long, restriction_dict={'range': ['0..4294967295']}, int_size=32), default=RestrictedClassType(base_type=long, restriction_dict={'range': ['0..4294967295']}, int_size=32)(0), is_leaf=True, yang_name="interval", rest_name="interval", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'info': u'Time (in seconds) that the event-handler will wait between iterations of completing the previous action (default = 0).'}}, namespace='urn:brocade.com:mgmt:brocade-event-handler', defining_module='brocade-event-handler', yang_type='uint32', is_config=True)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """interval must be of a type compatible with uint32""",
          'defined-type': "uint32",
          'generated-type': """YANGDynClass(base=RestrictedClassType(base_type=long, restriction_dict={'range': ['0..4294967295']}, int_size=32), default=RestrictedClassType(base_type=long, restriction_dict={'range': ['0..4294967295']}, int_size=32)(0), is_leaf=True, yang_name="interval", rest_name="interval", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'info': u'Time (in seconds) that the event-handler will wait between iterations of completing the previous action (default = 0).'}}, namespace='urn:brocade.com:mgmt:brocade-event-handler', defining_module='brocade-event-handler', yang_type='uint32', is_config=True)""",
        })

    self.__interval = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_interval(self):
    self.__interval = YANGDynClass(base=RestrictedClassType(base_type=long, restriction_dict={'range': ['0..4294967295']}, int_size=32), default=RestrictedClassType(base_type=long, restriction_dict={'range': ['0..4294967295']}, int_size=32)(0), is_leaf=True, yang_name="interval", rest_name="interval", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'info': u'Time (in seconds) that the event-handler will wait between iterations of completing the previous action (default = 0).'}}, namespace='urn:brocade.com:mgmt:brocade-event-handler', defining_module='brocade-event-handler', yang_type='uint32', is_config=True)


  def _get_run_mode(self):
    """
    Getter method for run_mode, mapped from YANG variable /event_handler/activate/name/run_mode (enumeration)
    """
    return self.__run_mode
      
  def _set_run_mode(self, v, load=False):
    """
    Setter method for run_mode, mapped from YANG variable /event_handler/activate/name/run_mode (enumeration)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_run_mode is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_run_mode() directly.
    """
    if hasattr(v, "_utype"):
      v = v._utype(v)
    try:
      t = YANGDynClass(v,base=RestrictedClassType(base_type=unicode,                                     restriction_type="dict_key",                                     restriction_arg={u'exclusive': {'value': 1}, u'non-exclusive': {'value': 2}},), default=unicode("non-exclusive"), is_leaf=True, yang_name="run-mode", rest_name="run-mode", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'info': u'Run-mode controls how the action is launched with cluster formation (default = non-exclusive).'}}, namespace='urn:brocade.com:mgmt:brocade-event-handler', defining_module='brocade-event-handler', yang_type='enumeration', is_config=True)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """run_mode must be of a type compatible with enumeration""",
          'defined-type': "brocade-event-handler:enumeration",
          'generated-type': """YANGDynClass(base=RestrictedClassType(base_type=unicode,                                     restriction_type="dict_key",                                     restriction_arg={u'exclusive': {'value': 1}, u'non-exclusive': {'value': 2}},), default=unicode("non-exclusive"), is_leaf=True, yang_name="run-mode", rest_name="run-mode", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'info': u'Run-mode controls how the action is launched with cluster formation (default = non-exclusive).'}}, namespace='urn:brocade.com:mgmt:brocade-event-handler', defining_module='brocade-event-handler', yang_type='enumeration', is_config=True)""",
        })

    self.__run_mode = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_run_mode(self):
    self.__run_mode = YANGDynClass(base=RestrictedClassType(base_type=unicode,                                     restriction_type="dict_key",                                     restriction_arg={u'exclusive': {'value': 1}, u'non-exclusive': {'value': 2}},), default=unicode("non-exclusive"), is_leaf=True, yang_name="run-mode", rest_name="run-mode", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'info': u'Run-mode controls how the action is launched with cluster formation (default = non-exclusive).'}}, namespace='urn:brocade.com:mgmt:brocade-event-handler', defining_module='brocade-event-handler', yang_type='enumeration', is_config=True)


  def _get_trigger_mode(self):
    """
    Getter method for trigger_mode, mapped from YANG variable /event_handler/activate/name/trigger_mode (enumeration)
    """
    return self.__trigger_mode
      
  def _set_trigger_mode(self, v, load=False):
    """
    Setter method for trigger_mode, mapped from YANG variable /event_handler/activate/name/trigger_mode (enumeration)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_trigger_mode is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_trigger_mode() directly.
    """
    if hasattr(v, "_utype"):
      v = v._utype(v)
    try:
      t = YANGDynClass(v,base=RestrictedClassType(base_type=unicode,                                     restriction_type="dict_key",                                     restriction_arg={u'each-instance': {'value': 1}, u'only-once': {'value': 3}, u'on-first-instance': {'value': 2}},), default=unicode("each-instance"), is_leaf=True, yang_name="trigger-mode", rest_name="trigger-mode", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'info': u'Trigger-mode controls how the action is launched with the configured event trigger (default = each-instance).'}}, namespace='urn:brocade.com:mgmt:brocade-event-handler', defining_module='brocade-event-handler', yang_type='enumeration', is_config=True)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """trigger_mode must be of a type compatible with enumeration""",
          'defined-type': "brocade-event-handler:enumeration",
          'generated-type': """YANGDynClass(base=RestrictedClassType(base_type=unicode,                                     restriction_type="dict_key",                                     restriction_arg={u'each-instance': {'value': 1}, u'only-once': {'value': 3}, u'on-first-instance': {'value': 2}},), default=unicode("each-instance"), is_leaf=True, yang_name="trigger-mode", rest_name="trigger-mode", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'info': u'Trigger-mode controls how the action is launched with the configured event trigger (default = each-instance).'}}, namespace='urn:brocade.com:mgmt:brocade-event-handler', defining_module='brocade-event-handler', yang_type='enumeration', is_config=True)""",
        })

    self.__trigger_mode = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_trigger_mode(self):
    self.__trigger_mode = YANGDynClass(base=RestrictedClassType(base_type=unicode,                                     restriction_type="dict_key",                                     restriction_arg={u'each-instance': {'value': 1}, u'only-once': {'value': 3}, u'on-first-instance': {'value': 2}},), default=unicode("each-instance"), is_leaf=True, yang_name="trigger-mode", rest_name="trigger-mode", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'info': u'Trigger-mode controls how the action is launched with the configured event trigger (default = each-instance).'}}, namespace='urn:brocade.com:mgmt:brocade-event-handler', defining_module='brocade-event-handler', yang_type='enumeration', is_config=True)


  def _get_trigger_function_container(self):
    """
    Getter method for trigger_function_container, mapped from YANG variable /event_handler/activate/name/trigger_function_container (container)
    """
    return self.__trigger_function_container
      
  def _set_trigger_function_container(self, v, load=False):
    """
    Setter method for trigger_function_container, mapped from YANG variable /event_handler/activate/name/trigger_function_container (container)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_trigger_function_container is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_trigger_function_container() directly.
    """
    if hasattr(v, "_utype"):
      v = v._utype(v)
    try:
      t = YANGDynClass(v,base=trigger_function_container.trigger_function_container, is_container='container', presence=False, yang_name="trigger-function-container", rest_name="", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'cli-compact-syntax': None, u'cli-drop-node-name': None, u'cli-sequence-commands': None}}, namespace='urn:brocade.com:mgmt:brocade-event-handler', defining_module='brocade-event-handler', yang_type='container', is_config=True)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """trigger_function_container must be of a type compatible with container""",
          'defined-type': "container",
          'generated-type': """YANGDynClass(base=trigger_function_container.trigger_function_container, is_container='container', presence=False, yang_name="trigger-function-container", rest_name="", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'cli-compact-syntax': None, u'cli-drop-node-name': None, u'cli-sequence-commands': None}}, namespace='urn:brocade.com:mgmt:brocade-event-handler', defining_module='brocade-event-handler', yang_type='container', is_config=True)""",
        })

    self.__trigger_function_container = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_trigger_function_container(self):
    self.__trigger_function_container = YANGDynClass(base=trigger_function_container.trigger_function_container, is_container='container', presence=False, yang_name="trigger-function-container", rest_name="", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'cli-compact-syntax': None, u'cli-drop-node-name': None, u'cli-sequence-commands': None}}, namespace='urn:brocade.com:mgmt:brocade-event-handler', defining_module='brocade-event-handler', yang_type='container', is_config=True)

  name = __builtin__.property(_get_name, _set_name)
  delay = __builtin__.property(_get_delay, _set_delay)
  iterations = __builtin__.property(_get_iterations, _set_iterations)
  interval = __builtin__.property(_get_interval, _set_interval)
  run_mode = __builtin__.property(_get_run_mode, _set_run_mode)
  trigger_mode = __builtin__.property(_get_trigger_mode, _set_trigger_mode)
  trigger_function_container = __builtin__.property(_get_trigger_function_container, _set_trigger_function_container)


  _pyangbind_elements = {'name': name, 'delay': delay, 'iterations': iterations, 'interval': interval, 'run_mode': run_mode, 'trigger_mode': trigger_mode, 'trigger_function_container': trigger_function_container, }


