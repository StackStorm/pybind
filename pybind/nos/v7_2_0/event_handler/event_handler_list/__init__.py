
from operator import attrgetter
import pyangbind.lib.xpathhelper as xpathhelper
from pyangbind.lib.yangtypes import RestrictedPrecisionDecimalType, RestrictedClassType, TypedListType
from pyangbind.lib.yangtypes import YANGBool, YANGListType, YANGDynClass, ReferenceType
from pyangbind.lib.base import PybindBase
from decimal import Decimal
from bitarray import bitarray
import __builtin__
import trigger
import action
class event_handler_list(PybindBase):
  """
  This class was auto-generated by the PythonClass plugin for PYANG
  from YANG module brocade-event-handler - based on the path /event-handler/event-handler-list. Each member element of
  the container is represented as a class variable - with a specific
  YANG type.
  """
  __slots__ = ('_pybind_generated_by', '_path_helper', '_yang_name', '_rest_name', '_extmethods', '__name','__description','__trigger','__action',)

  _yang_name = 'event-handler-list'
  _rest_name = 'event-handler-list'

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
    self.__action = YANGDynClass(base=action.action, is_container='container', presence=False, yang_name="action", rest_name="action", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'info': u'Action is run when trigger is detected.'}}, namespace='urn:brocade.com:mgmt:brocade-event-handler', defining_module='brocade-event-handler', yang_type='container', is_config=True)
    self.__trigger = YANGDynClass(base=YANGListType("trigger_id",trigger.trigger, yang_name="trigger", rest_name="trigger", parent=self, is_container='list', user_ordered=False, path_helper=self._path_helper, yang_keys='trigger-id', extensions={u'tailf-common': {u'info': u'VCS event or RASlog event.', u'cli-no-key-completion': None, u'cli-suppress-mode': None, u'cli-full-no': None, u'cli-compact-syntax': None, u'cli-suppress-key-abbreviation': None, u'cli-incomplete-command': None, u'cli-no-match-completion': None, u'callpoint': u'event-handler-trigger-composition-callpoint'}}), is_container='list', yang_name="trigger", rest_name="trigger", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'info': u'VCS event or RASlog event.', u'cli-no-key-completion': None, u'cli-suppress-mode': None, u'cli-full-no': None, u'cli-compact-syntax': None, u'cli-suppress-key-abbreviation': None, u'cli-incomplete-command': None, u'cli-no-match-completion': None, u'callpoint': u'event-handler-trigger-composition-callpoint'}}, namespace='urn:brocade.com:mgmt:brocade-event-handler', defining_module='brocade-event-handler', yang_type='list', is_config=True)
    self.__name = YANGDynClass(base=RestrictedClassType(base_type=unicode, restriction_dict={'pattern': u'[a-zA-Z]{1}([-a-zA-Z0-9\\.\\\\\\\\@#\\+\\*\\(\\)=\\{~\\}%<>=$_\\[\\]\\|]{0,31})'}), is_leaf=True, yang_name="name", rest_name="name", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'info': u'Event handler name'}}, is_keyval=True, namespace='urn:brocade.com:mgmt:brocade-event-handler', defining_module='brocade-event-handler', yang_type='common-def:name-string32', is_config=True)
    self.__description = YANGDynClass(base=RestrictedClassType(base_type=unicode, restriction_dict={'length': [u'1 .. 128']}), is_leaf=True, yang_name="description", rest_name="description", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'info': u'Event handler description (Max Size - 128)', u'cli-multi-value': None}}, namespace='urn:brocade.com:mgmt:brocade-event-handler', defining_module='brocade-event-handler', yang_type='string', is_config=True)

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
      return [u'event-handler', u'event-handler-list']

  def _rest_path(self):
    if hasattr(self, "_parent"):
      if self._rest_name:
        return self._parent._rest_path()+[self._rest_name]
      else:
        return self._parent._rest_path()
    else:
      return [u'event-handler', u'event-handler-list']

  def _get_name(self):
    """
    Getter method for name, mapped from YANG variable /event_handler/event_handler_list/name (common-def:name-string32)

    YANG Description: Event handler name
    """
    return self.__name
      
  def _set_name(self, v, load=False):
    """
    Setter method for name, mapped from YANG variable /event_handler/event_handler_list/name (common-def:name-string32)
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


  def _get_description(self):
    """
    Getter method for description, mapped from YANG variable /event_handler/event_handler_list/description (string)

    YANG Description: Event handler description (Max Size - 128)
    """
    return self.__description
      
  def _set_description(self, v, load=False):
    """
    Setter method for description, mapped from YANG variable /event_handler/event_handler_list/description (string)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_description is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_description() directly.

    YANG Description: Event handler description (Max Size - 128)
    """
    if hasattr(v, "_utype"):
      v = v._utype(v)
    try:
      t = YANGDynClass(v,base=RestrictedClassType(base_type=unicode, restriction_dict={'length': [u'1 .. 128']}), is_leaf=True, yang_name="description", rest_name="description", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'info': u'Event handler description (Max Size - 128)', u'cli-multi-value': None}}, namespace='urn:brocade.com:mgmt:brocade-event-handler', defining_module='brocade-event-handler', yang_type='string', is_config=True)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """description must be of a type compatible with string""",
          'defined-type': "string",
          'generated-type': """YANGDynClass(base=RestrictedClassType(base_type=unicode, restriction_dict={'length': [u'1 .. 128']}), is_leaf=True, yang_name="description", rest_name="description", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'info': u'Event handler description (Max Size - 128)', u'cli-multi-value': None}}, namespace='urn:brocade.com:mgmt:brocade-event-handler', defining_module='brocade-event-handler', yang_type='string', is_config=True)""",
        })

    self.__description = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_description(self):
    self.__description = YANGDynClass(base=RestrictedClassType(base_type=unicode, restriction_dict={'length': [u'1 .. 128']}), is_leaf=True, yang_name="description", rest_name="description", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'info': u'Event handler description (Max Size - 128)', u'cli-multi-value': None}}, namespace='urn:brocade.com:mgmt:brocade-event-handler', defining_module='brocade-event-handler', yang_type='string', is_config=True)


  def _get_trigger(self):
    """
    Getter method for trigger, mapped from YANG variable /event_handler/event_handler_list/trigger (list)

    YANG Description: VCS event or RASlog event.
    """
    return self.__trigger
      
  def _set_trigger(self, v, load=False):
    """
    Setter method for trigger, mapped from YANG variable /event_handler/event_handler_list/trigger (list)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_trigger is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_trigger() directly.

    YANG Description: VCS event or RASlog event.
    """
    if hasattr(v, "_utype"):
      v = v._utype(v)
    try:
      t = YANGDynClass(v,base=YANGListType("trigger_id",trigger.trigger, yang_name="trigger", rest_name="trigger", parent=self, is_container='list', user_ordered=False, path_helper=self._path_helper, yang_keys='trigger-id', extensions={u'tailf-common': {u'info': u'VCS event or RASlog event.', u'cli-no-key-completion': None, u'cli-suppress-mode': None, u'cli-full-no': None, u'cli-compact-syntax': None, u'cli-suppress-key-abbreviation': None, u'cli-incomplete-command': None, u'cli-no-match-completion': None, u'callpoint': u'event-handler-trigger-composition-callpoint'}}), is_container='list', yang_name="trigger", rest_name="trigger", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'info': u'VCS event or RASlog event.', u'cli-no-key-completion': None, u'cli-suppress-mode': None, u'cli-full-no': None, u'cli-compact-syntax': None, u'cli-suppress-key-abbreviation': None, u'cli-incomplete-command': None, u'cli-no-match-completion': None, u'callpoint': u'event-handler-trigger-composition-callpoint'}}, namespace='urn:brocade.com:mgmt:brocade-event-handler', defining_module='brocade-event-handler', yang_type='list', is_config=True)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """trigger must be of a type compatible with list""",
          'defined-type': "list",
          'generated-type': """YANGDynClass(base=YANGListType("trigger_id",trigger.trigger, yang_name="trigger", rest_name="trigger", parent=self, is_container='list', user_ordered=False, path_helper=self._path_helper, yang_keys='trigger-id', extensions={u'tailf-common': {u'info': u'VCS event or RASlog event.', u'cli-no-key-completion': None, u'cli-suppress-mode': None, u'cli-full-no': None, u'cli-compact-syntax': None, u'cli-suppress-key-abbreviation': None, u'cli-incomplete-command': None, u'cli-no-match-completion': None, u'callpoint': u'event-handler-trigger-composition-callpoint'}}), is_container='list', yang_name="trigger", rest_name="trigger", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'info': u'VCS event or RASlog event.', u'cli-no-key-completion': None, u'cli-suppress-mode': None, u'cli-full-no': None, u'cli-compact-syntax': None, u'cli-suppress-key-abbreviation': None, u'cli-incomplete-command': None, u'cli-no-match-completion': None, u'callpoint': u'event-handler-trigger-composition-callpoint'}}, namespace='urn:brocade.com:mgmt:brocade-event-handler', defining_module='brocade-event-handler', yang_type='list', is_config=True)""",
        })

    self.__trigger = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_trigger(self):
    self.__trigger = YANGDynClass(base=YANGListType("trigger_id",trigger.trigger, yang_name="trigger", rest_name="trigger", parent=self, is_container='list', user_ordered=False, path_helper=self._path_helper, yang_keys='trigger-id', extensions={u'tailf-common': {u'info': u'VCS event or RASlog event.', u'cli-no-key-completion': None, u'cli-suppress-mode': None, u'cli-full-no': None, u'cli-compact-syntax': None, u'cli-suppress-key-abbreviation': None, u'cli-incomplete-command': None, u'cli-no-match-completion': None, u'callpoint': u'event-handler-trigger-composition-callpoint'}}), is_container='list', yang_name="trigger", rest_name="trigger", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'info': u'VCS event or RASlog event.', u'cli-no-key-completion': None, u'cli-suppress-mode': None, u'cli-full-no': None, u'cli-compact-syntax': None, u'cli-suppress-key-abbreviation': None, u'cli-incomplete-command': None, u'cli-no-match-completion': None, u'callpoint': u'event-handler-trigger-composition-callpoint'}}, namespace='urn:brocade.com:mgmt:brocade-event-handler', defining_module='brocade-event-handler', yang_type='list', is_config=True)


  def _get_action(self):
    """
    Getter method for action, mapped from YANG variable /event_handler/event_handler_list/action (container)
    """
    return self.__action
      
  def _set_action(self, v, load=False):
    """
    Setter method for action, mapped from YANG variable /event_handler/event_handler_list/action (container)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_action is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_action() directly.
    """
    if hasattr(v, "_utype"):
      v = v._utype(v)
    try:
      t = YANGDynClass(v,base=action.action, is_container='container', presence=False, yang_name="action", rest_name="action", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'info': u'Action is run when trigger is detected.'}}, namespace='urn:brocade.com:mgmt:brocade-event-handler', defining_module='brocade-event-handler', yang_type='container', is_config=True)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """action must be of a type compatible with container""",
          'defined-type': "container",
          'generated-type': """YANGDynClass(base=action.action, is_container='container', presence=False, yang_name="action", rest_name="action", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'info': u'Action is run when trigger is detected.'}}, namespace='urn:brocade.com:mgmt:brocade-event-handler', defining_module='brocade-event-handler', yang_type='container', is_config=True)""",
        })

    self.__action = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_action(self):
    self.__action = YANGDynClass(base=action.action, is_container='container', presence=False, yang_name="action", rest_name="action", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'info': u'Action is run when trigger is detected.'}}, namespace='urn:brocade.com:mgmt:brocade-event-handler', defining_module='brocade-event-handler', yang_type='container', is_config=True)

  name = __builtin__.property(_get_name, _set_name)
  description = __builtin__.property(_get_description, _set_description)
  trigger = __builtin__.property(_get_trigger, _set_trigger)
  action = __builtin__.property(_get_action, _set_action)


  _pyangbind_elements = {'name': name, 'description': description, 'trigger': trigger, 'action': action, }


