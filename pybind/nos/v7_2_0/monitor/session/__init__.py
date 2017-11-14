
from operator import attrgetter
import pyangbind.lib.xpathhelper as xpathhelper
from pyangbind.lib.yangtypes import RestrictedPrecisionDecimalType, RestrictedClassType, TypedListType
from pyangbind.lib.yangtypes import YANGBool, YANGListType, YANGDynClass, ReferenceType
from pyangbind.lib.base import PybindBase
from decimal import Decimal
from bitarray import bitarray
import __builtin__
import span_command
class session(PybindBase):
  """
  This class was auto-generated by the PythonClass plugin for PYANG
  from YANG module brocade-span - based on the path /monitor/session. Each member element of
  the container is represented as a class variable - with a specific
  YANG type.
  """
  __slots__ = ('_pybind_generated_by', '_path_helper', '_yang_name', '_rest_name', '_extmethods', '__session_number','__description','__span_command',)

  _yang_name = 'session'
  _rest_name = 'session'

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
    self.__session_number = YANGDynClass(base=RestrictedClassType(base_type=RestrictedClassType(base_type=long, restriction_dict={'range': ['0..4294967295']}, int_size=32), restriction_dict={'range': [u'1..512']}), is_leaf=True, yang_name="session-number", rest_name="session-number", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'cli-completion-actionpoint': u'SpanActionpoint'}}, is_keyval=True, namespace='urn:brocade.com:mgmt:brocade-span', defining_module='brocade-span', yang_type='session-type', is_config=True)
    self.__span_command = YANGDynClass(base=span_command.span_command, is_container='container', presence=False, yang_name="span-command", rest_name="", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'cli-compact-syntax': None, u'cli-drop-node-name': None, u'cli-sequence-commands': None}}, namespace='urn:brocade.com:mgmt:brocade-span', defining_module='brocade-span', yang_type='container', is_config=True)
    self.__description = YANGDynClass(base=RestrictedClassType(base_type=unicode, restriction_dict={'length': [u'1..64']}), is_leaf=True, yang_name="description", rest_name="description", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'info': u'Description string of session', u'cli-multi-value': None}}, namespace='urn:brocade.com:mgmt:brocade-span', defining_module='brocade-span', yang_type='string', is_config=True)

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
      return [u'monitor', u'session']

  def _rest_path(self):
    if hasattr(self, "_parent"):
      if self._rest_name:
        return self._parent._rest_path()+[self._rest_name]
      else:
        return self._parent._rest_path()
    else:
      return [u'monitor', u'session']

  def _get_session_number(self):
    """
    Getter method for session_number, mapped from YANG variable /monitor/session/session_number (session-type)
    """
    return self.__session_number
      
  def _set_session_number(self, v, load=False):
    """
    Setter method for session_number, mapped from YANG variable /monitor/session/session_number (session-type)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_session_number is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_session_number() directly.
    """
    parent = getattr(self, "_parent", None)
    if parent is not None and load is False:
      raise AttributeError("Cannot set keys directly when" +
                             " within an instantiated list")

    if hasattr(v, "_utype"):
      v = v._utype(v)
    try:
      t = YANGDynClass(v,base=RestrictedClassType(base_type=RestrictedClassType(base_type=long, restriction_dict={'range': ['0..4294967295']}, int_size=32), restriction_dict={'range': [u'1..512']}), is_leaf=True, yang_name="session-number", rest_name="session-number", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'cli-completion-actionpoint': u'SpanActionpoint'}}, is_keyval=True, namespace='urn:brocade.com:mgmt:brocade-span', defining_module='brocade-span', yang_type='session-type', is_config=True)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """session_number must be of a type compatible with session-type""",
          'defined-type': "brocade-span:session-type",
          'generated-type': """YANGDynClass(base=RestrictedClassType(base_type=RestrictedClassType(base_type=long, restriction_dict={'range': ['0..4294967295']}, int_size=32), restriction_dict={'range': [u'1..512']}), is_leaf=True, yang_name="session-number", rest_name="session-number", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'cli-completion-actionpoint': u'SpanActionpoint'}}, is_keyval=True, namespace='urn:brocade.com:mgmt:brocade-span', defining_module='brocade-span', yang_type='session-type', is_config=True)""",
        })

    self.__session_number = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_session_number(self):
    self.__session_number = YANGDynClass(base=RestrictedClassType(base_type=RestrictedClassType(base_type=long, restriction_dict={'range': ['0..4294967295']}, int_size=32), restriction_dict={'range': [u'1..512']}), is_leaf=True, yang_name="session-number", rest_name="session-number", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'cli-completion-actionpoint': u'SpanActionpoint'}}, is_keyval=True, namespace='urn:brocade.com:mgmt:brocade-span', defining_module='brocade-span', yang_type='session-type', is_config=True)


  def _get_description(self):
    """
    Getter method for description, mapped from YANG variable /monitor/session/description (string)
    """
    return self.__description
      
  def _set_description(self, v, load=False):
    """
    Setter method for description, mapped from YANG variable /monitor/session/description (string)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_description is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_description() directly.
    """
    if hasattr(v, "_utype"):
      v = v._utype(v)
    try:
      t = YANGDynClass(v,base=RestrictedClassType(base_type=unicode, restriction_dict={'length': [u'1..64']}), is_leaf=True, yang_name="description", rest_name="description", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'info': u'Description string of session', u'cli-multi-value': None}}, namespace='urn:brocade.com:mgmt:brocade-span', defining_module='brocade-span', yang_type='string', is_config=True)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """description must be of a type compatible with string""",
          'defined-type': "string",
          'generated-type': """YANGDynClass(base=RestrictedClassType(base_type=unicode, restriction_dict={'length': [u'1..64']}), is_leaf=True, yang_name="description", rest_name="description", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'info': u'Description string of session', u'cli-multi-value': None}}, namespace='urn:brocade.com:mgmt:brocade-span', defining_module='brocade-span', yang_type='string', is_config=True)""",
        })

    self.__description = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_description(self):
    self.__description = YANGDynClass(base=RestrictedClassType(base_type=unicode, restriction_dict={'length': [u'1..64']}), is_leaf=True, yang_name="description", rest_name="description", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'info': u'Description string of session', u'cli-multi-value': None}}, namespace='urn:brocade.com:mgmt:brocade-span', defining_module='brocade-span', yang_type='string', is_config=True)


  def _get_span_command(self):
    """
    Getter method for span_command, mapped from YANG variable /monitor/session/span_command (container)
    """
    return self.__span_command
      
  def _set_span_command(self, v, load=False):
    """
    Setter method for span_command, mapped from YANG variable /monitor/session/span_command (container)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_span_command is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_span_command() directly.
    """
    if hasattr(v, "_utype"):
      v = v._utype(v)
    try:
      t = YANGDynClass(v,base=span_command.span_command, is_container='container', presence=False, yang_name="span-command", rest_name="", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'cli-compact-syntax': None, u'cli-drop-node-name': None, u'cli-sequence-commands': None}}, namespace='urn:brocade.com:mgmt:brocade-span', defining_module='brocade-span', yang_type='container', is_config=True)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """span_command must be of a type compatible with container""",
          'defined-type': "container",
          'generated-type': """YANGDynClass(base=span_command.span_command, is_container='container', presence=False, yang_name="span-command", rest_name="", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'cli-compact-syntax': None, u'cli-drop-node-name': None, u'cli-sequence-commands': None}}, namespace='urn:brocade.com:mgmt:brocade-span', defining_module='brocade-span', yang_type='container', is_config=True)""",
        })

    self.__span_command = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_span_command(self):
    self.__span_command = YANGDynClass(base=span_command.span_command, is_container='container', presence=False, yang_name="span-command", rest_name="", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'cli-compact-syntax': None, u'cli-drop-node-name': None, u'cli-sequence-commands': None}}, namespace='urn:brocade.com:mgmt:brocade-span', defining_module='brocade-span', yang_type='container', is_config=True)

  session_number = __builtin__.property(_get_session_number, _set_session_number)
  description = __builtin__.property(_get_description, _set_description)
  span_command = __builtin__.property(_get_span_command, _set_span_command)


  _pyangbind_elements = {'session_number': session_number, 'description': description, 'span_command': span_command, }


