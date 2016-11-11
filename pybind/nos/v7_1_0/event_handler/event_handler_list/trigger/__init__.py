
from operator import attrgetter
import pyangbind.lib.xpathhelper as xpathhelper
from pyangbind.lib.yangtypes import RestrictedPrecisionDecimalType, RestrictedClassType, TypedListType
from pyangbind.lib.yangtypes import YANGBool, YANGListType, YANGDynClass, ReferenceType
from pyangbind.lib.base import PybindBase
from decimal import Decimal
from bitarray import bitarray
import __builtin__
import raslog
class trigger(PybindBase):
  """
  This class was auto-generated by the PythonClass plugin for PYANG
  from YANG module brocade-event-handler - based on the path /event-handler/event-handler-list/trigger. Each member element of
  the container is represented as a class variable - with a specific
  YANG type.

  YANG Description: VCS event or RASlog event.
  """
  __slots__ = ('_pybind_generated_by', '_path_helper', '_yang_name', '_rest_name', '_extmethods', '__trigger_id','__vcs','__raslog',)

  _yang_name = 'trigger'
  _rest_name = 'trigger'

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
    self.__vcs = YANGDynClass(base=RestrictedClassType(base_type=unicode,                                     restriction_type="dict_key",                                     restriction_arg={u'switch-bootup': {'value': 1}, u'switch-ready-for-configuration': {'value': 2}},), is_leaf=True, yang_name="vcs", rest_name="vcs", parent=self, choice=(u'trigger-choice', u'vcs'), path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'info': u'VCS event type.'}}, namespace='urn:brocade.com:mgmt:brocade-event-handler', defining_module='brocade-event-handler', yang_type='enumeration', is_config=True)
    self.__raslog = YANGDynClass(base=raslog.raslog, is_container='container', yang_name="raslog", rest_name="raslog", parent=self, choice=(u'trigger-choice', u'raslog'), path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'cli-compact-syntax': None, u'info': u'RASlog Id.', u'cli-sequence-commands': None}}, namespace='urn:brocade.com:mgmt:brocade-event-handler', defining_module='brocade-event-handler', yang_type='container', is_config=True)
    self.__trigger_id = YANGDynClass(base=RestrictedClassType(base_type=RestrictedClassType(base_type=long, restriction_dict={'range': ['0..4294967295']}, int_size=32), restriction_dict={'range': [u'1..100']}), is_leaf=True, yang_name="trigger-id", rest_name="trigger-id", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, is_keyval=True, namespace='urn:brocade.com:mgmt:brocade-event-handler', defining_module='brocade-event-handler', yang_type='uint32', is_config=True)

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
      return [u'event-handler', u'event-handler-list', u'trigger']

  def _rest_path(self):
    if hasattr(self, "_parent"):
      if self._rest_name:
        return self._parent._rest_path()+[self._rest_name]
      else:
        return self._parent._rest_path()
    else:
      return [u'event-handler', u'trigger']

  def _get_trigger_id(self):
    """
    Getter method for trigger_id, mapped from YANG variable /event_handler/event_handler_list/trigger/trigger_id (uint32)
    """
    return self.__trigger_id
      
  def _set_trigger_id(self, v, load=False):
    """
    Setter method for trigger_id, mapped from YANG variable /event_handler/event_handler_list/trigger/trigger_id (uint32)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_trigger_id is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_trigger_id() directly.
    """
    parent = getattr(self, "_parent", None)
    if parent is not None and load is False:
      raise AttributeError("Cannot set keys directly when" +
                             " within an instantiated list")

    try:
      t = YANGDynClass(v,base=RestrictedClassType(base_type=RestrictedClassType(base_type=long, restriction_dict={'range': ['0..4294967295']}, int_size=32), restriction_dict={'range': [u'1..100']}), is_leaf=True, yang_name="trigger-id", rest_name="trigger-id", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, is_keyval=True, namespace='urn:brocade.com:mgmt:brocade-event-handler', defining_module='brocade-event-handler', yang_type='uint32', is_config=True)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """trigger_id must be of a type compatible with uint32""",
          'defined-type': "uint32",
          'generated-type': """YANGDynClass(base=RestrictedClassType(base_type=RestrictedClassType(base_type=long, restriction_dict={'range': ['0..4294967295']}, int_size=32), restriction_dict={'range': [u'1..100']}), is_leaf=True, yang_name="trigger-id", rest_name="trigger-id", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, is_keyval=True, namespace='urn:brocade.com:mgmt:brocade-event-handler', defining_module='brocade-event-handler', yang_type='uint32', is_config=True)""",
        })

    self.__trigger_id = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_trigger_id(self):
    self.__trigger_id = YANGDynClass(base=RestrictedClassType(base_type=RestrictedClassType(base_type=long, restriction_dict={'range': ['0..4294967295']}, int_size=32), restriction_dict={'range': [u'1..100']}), is_leaf=True, yang_name="trigger-id", rest_name="trigger-id", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, is_keyval=True, namespace='urn:brocade.com:mgmt:brocade-event-handler', defining_module='brocade-event-handler', yang_type='uint32', is_config=True)


  def _get_vcs(self):
    """
    Getter method for vcs, mapped from YANG variable /event_handler/event_handler_list/trigger/vcs (enumeration)

    YANG Description: VCS event type.
    """
    return self.__vcs
      
  def _set_vcs(self, v, load=False):
    """
    Setter method for vcs, mapped from YANG variable /event_handler/event_handler_list/trigger/vcs (enumeration)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_vcs is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_vcs() directly.

    YANG Description: VCS event type.
    """
    try:
      t = YANGDynClass(v,base=RestrictedClassType(base_type=unicode,                                     restriction_type="dict_key",                                     restriction_arg={u'switch-bootup': {'value': 1}, u'switch-ready-for-configuration': {'value': 2}},), is_leaf=True, yang_name="vcs", rest_name="vcs", parent=self, choice=(u'trigger-choice', u'vcs'), path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'info': u'VCS event type.'}}, namespace='urn:brocade.com:mgmt:brocade-event-handler', defining_module='brocade-event-handler', yang_type='enumeration', is_config=True)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """vcs must be of a type compatible with enumeration""",
          'defined-type': "brocade-event-handler:enumeration",
          'generated-type': """YANGDynClass(base=RestrictedClassType(base_type=unicode,                                     restriction_type="dict_key",                                     restriction_arg={u'switch-bootup': {'value': 1}, u'switch-ready-for-configuration': {'value': 2}},), is_leaf=True, yang_name="vcs", rest_name="vcs", parent=self, choice=(u'trigger-choice', u'vcs'), path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'info': u'VCS event type.'}}, namespace='urn:brocade.com:mgmt:brocade-event-handler', defining_module='brocade-event-handler', yang_type='enumeration', is_config=True)""",
        })

    self.__vcs = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_vcs(self):
    self.__vcs = YANGDynClass(base=RestrictedClassType(base_type=unicode,                                     restriction_type="dict_key",                                     restriction_arg={u'switch-bootup': {'value': 1}, u'switch-ready-for-configuration': {'value': 2}},), is_leaf=True, yang_name="vcs", rest_name="vcs", parent=self, choice=(u'trigger-choice', u'vcs'), path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'info': u'VCS event type.'}}, namespace='urn:brocade.com:mgmt:brocade-event-handler', defining_module='brocade-event-handler', yang_type='enumeration', is_config=True)


  def _get_raslog(self):
    """
    Getter method for raslog, mapped from YANG variable /event_handler/event_handler_list/trigger/raslog (container)

    YANG Description: RASlog Id.
    """
    return self.__raslog
      
  def _set_raslog(self, v, load=False):
    """
    Setter method for raslog, mapped from YANG variable /event_handler/event_handler_list/trigger/raslog (container)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_raslog is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_raslog() directly.

    YANG Description: RASlog Id.
    """
    try:
      t = YANGDynClass(v,base=raslog.raslog, is_container='container', yang_name="raslog", rest_name="raslog", parent=self, choice=(u'trigger-choice', u'raslog'), path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'cli-compact-syntax': None, u'info': u'RASlog Id.', u'cli-sequence-commands': None}}, namespace='urn:brocade.com:mgmt:brocade-event-handler', defining_module='brocade-event-handler', yang_type='container', is_config=True)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """raslog must be of a type compatible with container""",
          'defined-type': "container",
          'generated-type': """YANGDynClass(base=raslog.raslog, is_container='container', yang_name="raslog", rest_name="raslog", parent=self, choice=(u'trigger-choice', u'raslog'), path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'cli-compact-syntax': None, u'info': u'RASlog Id.', u'cli-sequence-commands': None}}, namespace='urn:brocade.com:mgmt:brocade-event-handler', defining_module='brocade-event-handler', yang_type='container', is_config=True)""",
        })

    self.__raslog = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_raslog(self):
    self.__raslog = YANGDynClass(base=raslog.raslog, is_container='container', yang_name="raslog", rest_name="raslog", parent=self, choice=(u'trigger-choice', u'raslog'), path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'cli-compact-syntax': None, u'info': u'RASlog Id.', u'cli-sequence-commands': None}}, namespace='urn:brocade.com:mgmt:brocade-event-handler', defining_module='brocade-event-handler', yang_type='container', is_config=True)

  trigger_id = __builtin__.property(_get_trigger_id, _set_trigger_id)
  vcs = __builtin__.property(_get_vcs, _set_vcs)
  raslog = __builtin__.property(_get_raslog, _set_raslog)

  __choices__ = {u'trigger-choice': {u'vcs': [u'vcs'], u'raslog': [u'raslog']}}
  _pyangbind_elements = {'trigger_id': trigger_id, 'vcs': vcs, 'raslog': raslog, }

