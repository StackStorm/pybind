
from operator import attrgetter
import pyangbind.lib.xpathhelper as xpathhelper
from pyangbind.lib.yangtypes import RestrictedPrecisionDecimalType, RestrictedClassType, TypedListType
from pyangbind.lib.yangtypes import YANGBool, YANGListType, YANGDynClass, ReferenceType
from pyangbind.lib.base import PybindBase
from decimal import Decimal
from bitarray import bitarray
import __builtin__
class raslog(PybindBase):
  """
  This class was auto-generated by the PythonClass plugin for PYANG
  from YANG module brocade-event-handler - based on the path /event-handler/event-handler-list/trigger/raslog. Each member element of
  the container is represented as a class variable - with a specific
  YANG type.

  YANG Description: RASlog Id.
  """
  __slots__ = ('_pybind_generated_by', '_path_helper', '_yang_name', '_rest_name', '_extmethods', '__raslog','__pattern',)

  _yang_name = 'raslog'
  _rest_name = 'raslog'

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
    self.__pattern = YANGDynClass(base=RestrictedClassType(base_type=unicode, restriction_dict={'length': [u'1 .. 128']}), is_leaf=True, yang_name="pattern", rest_name="pattern", parent=self, choice=(u'trigger-choice', u'raslog'), path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'info': u'Regular expression trigger filter.', u'cli-multi-value': None}}, namespace='urn:brocade.com:mgmt:brocade-event-handler', defining_module='brocade-event-handler', yang_type='string', is_config=True)
    self.__raslog = YANGDynClass(base=RestrictedClassType(base_type=unicode, restriction_dict={'pattern': u'[a-zA-Z]{1}([-a-zA-Z0-9\\.\\\\\\\\@#\\+\\*\\(\\)=\\{~\\}%<>=$_\\[\\]\\|]{0,31})'}), is_leaf=True, yang_name="raslog", rest_name="", parent=self, choice=(u'trigger-choice', u'raslog'), path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'info': u'RASlog Id.', u'cli-drop-node-name': None}}, namespace='urn:brocade.com:mgmt:brocade-event-handler', defining_module='brocade-event-handler', yang_type='common-def:name-string32', is_config=True)

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
      return [u'event-handler', u'event-handler-list', u'trigger', u'raslog']

  def _rest_path(self):
    if hasattr(self, "_parent"):
      if self._rest_name:
        return self._parent._rest_path()+[self._rest_name]
      else:
        return self._parent._rest_path()
    else:
      return [u'event-handler', u'trigger', u'raslog']

  def _get_raslog(self):
    """
    Getter method for raslog, mapped from YANG variable /event_handler/event_handler_list/trigger/raslog/raslog (common-def:name-string32)

    YANG Description: RASlog Id.
    """
    return self.__raslog
      
  def _set_raslog(self, v, load=False):
    """
    Setter method for raslog, mapped from YANG variable /event_handler/event_handler_list/trigger/raslog/raslog (common-def:name-string32)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_raslog is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_raslog() directly.

    YANG Description: RASlog Id.
    """
    try:
      t = YANGDynClass(v,base=RestrictedClassType(base_type=unicode, restriction_dict={'pattern': u'[a-zA-Z]{1}([-a-zA-Z0-9\\.\\\\\\\\@#\\+\\*\\(\\)=\\{~\\}%<>=$_\\[\\]\\|]{0,31})'}), is_leaf=True, yang_name="raslog", rest_name="", parent=self, choice=(u'trigger-choice', u'raslog'), path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'info': u'RASlog Id.', u'cli-drop-node-name': None}}, namespace='urn:brocade.com:mgmt:brocade-event-handler', defining_module='brocade-event-handler', yang_type='common-def:name-string32', is_config=True)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """raslog must be of a type compatible with common-def:name-string32""",
          'defined-type': "common-def:name-string32",
          'generated-type': """YANGDynClass(base=RestrictedClassType(base_type=unicode, restriction_dict={'pattern': u'[a-zA-Z]{1}([-a-zA-Z0-9\\.\\\\\\\\@#\\+\\*\\(\\)=\\{~\\}%<>=$_\\[\\]\\|]{0,31})'}), is_leaf=True, yang_name="raslog", rest_name="", parent=self, choice=(u'trigger-choice', u'raslog'), path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'info': u'RASlog Id.', u'cli-drop-node-name': None}}, namespace='urn:brocade.com:mgmt:brocade-event-handler', defining_module='brocade-event-handler', yang_type='common-def:name-string32', is_config=True)""",
        })

    self.__raslog = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_raslog(self):
    self.__raslog = YANGDynClass(base=RestrictedClassType(base_type=unicode, restriction_dict={'pattern': u'[a-zA-Z]{1}([-a-zA-Z0-9\\.\\\\\\\\@#\\+\\*\\(\\)=\\{~\\}%<>=$_\\[\\]\\|]{0,31})'}), is_leaf=True, yang_name="raslog", rest_name="", parent=self, choice=(u'trigger-choice', u'raslog'), path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'info': u'RASlog Id.', u'cli-drop-node-name': None}}, namespace='urn:brocade.com:mgmt:brocade-event-handler', defining_module='brocade-event-handler', yang_type='common-def:name-string32', is_config=True)


  def _get_pattern(self):
    """
    Getter method for pattern, mapped from YANG variable /event_handler/event_handler_list/trigger/raslog/pattern (string)

    YANG Description: Regular expression trigger filter.
    """
    return self.__pattern
      
  def _set_pattern(self, v, load=False):
    """
    Setter method for pattern, mapped from YANG variable /event_handler/event_handler_list/trigger/raslog/pattern (string)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_pattern is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_pattern() directly.

    YANG Description: Regular expression trigger filter.
    """
    try:
      t = YANGDynClass(v,base=RestrictedClassType(base_type=unicode, restriction_dict={'length': [u'1 .. 128']}), is_leaf=True, yang_name="pattern", rest_name="pattern", parent=self, choice=(u'trigger-choice', u'raslog'), path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'info': u'Regular expression trigger filter.', u'cli-multi-value': None}}, namespace='urn:brocade.com:mgmt:brocade-event-handler', defining_module='brocade-event-handler', yang_type='string', is_config=True)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """pattern must be of a type compatible with string""",
          'defined-type': "string",
          'generated-type': """YANGDynClass(base=RestrictedClassType(base_type=unicode, restriction_dict={'length': [u'1 .. 128']}), is_leaf=True, yang_name="pattern", rest_name="pattern", parent=self, choice=(u'trigger-choice', u'raslog'), path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'info': u'Regular expression trigger filter.', u'cli-multi-value': None}}, namespace='urn:brocade.com:mgmt:brocade-event-handler', defining_module='brocade-event-handler', yang_type='string', is_config=True)""",
        })

    self.__pattern = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_pattern(self):
    self.__pattern = YANGDynClass(base=RestrictedClassType(base_type=unicode, restriction_dict={'length': [u'1 .. 128']}), is_leaf=True, yang_name="pattern", rest_name="pattern", parent=self, choice=(u'trigger-choice', u'raslog'), path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'info': u'Regular expression trigger filter.', u'cli-multi-value': None}}, namespace='urn:brocade.com:mgmt:brocade-event-handler', defining_module='brocade-event-handler', yang_type='string', is_config=True)

  raslog = __builtin__.property(_get_raslog, _set_raslog)
  pattern = __builtin__.property(_get_pattern, _set_pattern)

  __choices__ = {u'trigger-choice': {u'raslog': [u'raslog', u'pattern']}}
  _pyangbind_elements = {'raslog': raslog, 'pattern': pattern, }

