
from operator import attrgetter
import pyangbind.lib.xpathhelper as xpathhelper
from pyangbind.lib.yangtypes import RestrictedPrecisionDecimalType, RestrictedClassType, TypedListType
from pyangbind.lib.yangtypes import YANGBool, YANGListType, YANGDynClass, ReferenceType
from pyangbind.lib.base import PybindBase
from decimal import Decimal
from bitarray import bitarray
import __builtin__
import priority_group_table
import priority_table
import remap
class cee_map(PybindBase):
  """
  This class was auto-generated by the PythonClass plugin for PYANG
  from YANG module brocade-qos-cee - based on the path /cee-map. Each member element of
  the container is represented as a class variable - with a specific
  YANG type.
  """
  __slots__ = ('_pybind_generated_by', '_path_helper', '_yang_name', '_rest_name', '_extmethods', '__name','__precedence','__priority_group_table','__priority_table','__remap',)

  _yang_name = 'cee-map'
  _rest_name = 'cee-map'

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
    self.__remap = YANGDynClass(base=remap.remap, is_container='container', presence=False, yang_name="remap", rest_name="remap", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'info': u' Configure Class of Service (CoS) to be \n remapped', u'callpoint': u'qos_cee_remap', u'display-when': u'/vcsmode/vcs-mode = "true"'}}, namespace='urn:brocade.com:mgmt:brocade-qos-cee', defining_module='brocade-qos-cee', yang_type='container', is_config=True)
    self.__priority_table = YANGDynClass(base=priority_table.priority_table, is_container='container', presence=False, yang_name="priority-table", rest_name="priority-table", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'info': u' Configure Priority Table', u'cli-compact-syntax': None, u'cli-sequence-commands': None, u'callpoint': u'qos_priority_map', u'cli-full-no': None}}, namespace='urn:brocade.com:mgmt:brocade-qos-cee', defining_module='brocade-qos-cee', yang_type='container', is_config=True)
    self.__name = YANGDynClass(base=RestrictedClassType(base_type=unicode, restriction_dict={'pattern': u'[a-zA-Z]{1}([-a-zA-Z0-9\\.\\\\\\\\@#\\+\\*\\(\\)=\\{~\\}%<>=$_\\[\\]\\|]{0,31})'}), is_leaf=True, yang_name="name", rest_name="", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'cli-drop-node-name': None}}, is_keyval=True, namespace='urn:brocade.com:mgmt:brocade-qos-cee', defining_module='brocade-qos-cee', yang_type='cee-map-name-type', is_config=True)
    self.__precedence = YANGDynClass(base=RestrictedClassType(base_type=RestrictedClassType(base_type=long, restriction_dict={'range': ['-2147483648..2147483647']}, int_size=32), restriction_dict={'range': [u'1 .. 100']}), is_leaf=True, yang_name="precedence", rest_name="precedence", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'info': u' Precedence value'}}, namespace='urn:brocade.com:mgmt:brocade-qos-cee', defining_module='brocade-qos-cee', yang_type='int32', is_config=True)
    self.__priority_group_table = YANGDynClass(base=YANGListType("PGID",priority_group_table.priority_group_table, yang_name="priority-group-table", rest_name="priority-group-table", parent=self, is_container='list', user_ordered=False, path_helper=self._path_helper, yang_keys='PGID', extensions={u'tailf-common': {u'info': u' Configure Priority Group Table', u'cli-no-key-completion': None, u'cli-full-no': None, u'cli-suppress-list-no': None, u'cli-compact-syntax': None, u'cli-sequence-commands': None, u'cli-suppress-mode': None, u'cli-suppress-key-abbreviation': None, u'cli-incomplete-command': None, u'callpoint': u'qos_priority_group'}}), is_container='list', yang_name="priority-group-table", rest_name="priority-group-table", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'info': u' Configure Priority Group Table', u'cli-no-key-completion': None, u'cli-full-no': None, u'cli-suppress-list-no': None, u'cli-compact-syntax': None, u'cli-sequence-commands': None, u'cli-suppress-mode': None, u'cli-suppress-key-abbreviation': None, u'cli-incomplete-command': None, u'callpoint': u'qos_priority_group'}}, namespace='urn:brocade.com:mgmt:brocade-qos-cee', defining_module='brocade-qos-cee', yang_type='list', is_config=True)

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
      return [u'cee-map']

  def _rest_path(self):
    if hasattr(self, "_parent"):
      if self._rest_name:
        return self._parent._rest_path()+[self._rest_name]
      else:
        return self._parent._rest_path()
    else:
      return [u'cee-map']

  def _get_name(self):
    """
    Getter method for name, mapped from YANG variable /cee_map/name (cee-map-name-type)
    """
    return self.__name
      
  def _set_name(self, v, load=False):
    """
    Setter method for name, mapped from YANG variable /cee_map/name (cee-map-name-type)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_name is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_name() directly.
    """
    parent = getattr(self, "_parent", None)
    if parent is not None and load is False:
      raise AttributeError("Cannot set keys directly when" +
                             " within an instantiated list")

    if hasattr(v, "_utype"):
      v = v._utype(v)
    try:
      t = YANGDynClass(v,base=RestrictedClassType(base_type=unicode, restriction_dict={'pattern': u'[a-zA-Z]{1}([-a-zA-Z0-9\\.\\\\\\\\@#\\+\\*\\(\\)=\\{~\\}%<>=$_\\[\\]\\|]{0,31})'}), is_leaf=True, yang_name="name", rest_name="", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'cli-drop-node-name': None}}, is_keyval=True, namespace='urn:brocade.com:mgmt:brocade-qos-cee', defining_module='brocade-qos-cee', yang_type='cee-map-name-type', is_config=True)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """name must be of a type compatible with cee-map-name-type""",
          'defined-type': "brocade-qos-cee:cee-map-name-type",
          'generated-type': """YANGDynClass(base=RestrictedClassType(base_type=unicode, restriction_dict={'pattern': u'[a-zA-Z]{1}([-a-zA-Z0-9\\.\\\\\\\\@#\\+\\*\\(\\)=\\{~\\}%<>=$_\\[\\]\\|]{0,31})'}), is_leaf=True, yang_name="name", rest_name="", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'cli-drop-node-name': None}}, is_keyval=True, namespace='urn:brocade.com:mgmt:brocade-qos-cee', defining_module='brocade-qos-cee', yang_type='cee-map-name-type', is_config=True)""",
        })

    self.__name = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_name(self):
    self.__name = YANGDynClass(base=RestrictedClassType(base_type=unicode, restriction_dict={'pattern': u'[a-zA-Z]{1}([-a-zA-Z0-9\\.\\\\\\\\@#\\+\\*\\(\\)=\\{~\\}%<>=$_\\[\\]\\|]{0,31})'}), is_leaf=True, yang_name="name", rest_name="", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'cli-drop-node-name': None}}, is_keyval=True, namespace='urn:brocade.com:mgmt:brocade-qos-cee', defining_module='brocade-qos-cee', yang_type='cee-map-name-type', is_config=True)


  def _get_precedence(self):
    """
    Getter method for precedence, mapped from YANG variable /cee_map/precedence (int32)

    YANG Description: CEE map precedence value
    """
    return self.__precedence
      
  def _set_precedence(self, v, load=False):
    """
    Setter method for precedence, mapped from YANG variable /cee_map/precedence (int32)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_precedence is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_precedence() directly.

    YANG Description: CEE map precedence value
    """
    if hasattr(v, "_utype"):
      v = v._utype(v)
    try:
      t = YANGDynClass(v,base=RestrictedClassType(base_type=RestrictedClassType(base_type=long, restriction_dict={'range': ['-2147483648..2147483647']}, int_size=32), restriction_dict={'range': [u'1 .. 100']}), is_leaf=True, yang_name="precedence", rest_name="precedence", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'info': u' Precedence value'}}, namespace='urn:brocade.com:mgmt:brocade-qos-cee', defining_module='brocade-qos-cee', yang_type='int32', is_config=True)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """precedence must be of a type compatible with int32""",
          'defined-type': "int32",
          'generated-type': """YANGDynClass(base=RestrictedClassType(base_type=RestrictedClassType(base_type=long, restriction_dict={'range': ['-2147483648..2147483647']}, int_size=32), restriction_dict={'range': [u'1 .. 100']}), is_leaf=True, yang_name="precedence", rest_name="precedence", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'info': u' Precedence value'}}, namespace='urn:brocade.com:mgmt:brocade-qos-cee', defining_module='brocade-qos-cee', yang_type='int32', is_config=True)""",
        })

    self.__precedence = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_precedence(self):
    self.__precedence = YANGDynClass(base=RestrictedClassType(base_type=RestrictedClassType(base_type=long, restriction_dict={'range': ['-2147483648..2147483647']}, int_size=32), restriction_dict={'range': [u'1 .. 100']}), is_leaf=True, yang_name="precedence", rest_name="precedence", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'info': u' Precedence value'}}, namespace='urn:brocade.com:mgmt:brocade-qos-cee', defining_module='brocade-qos-cee', yang_type='int32', is_config=True)


  def _get_priority_group_table(self):
    """
    Getter method for priority_group_table, mapped from YANG variable /cee_map/priority_group_table (list)
    """
    return self.__priority_group_table
      
  def _set_priority_group_table(self, v, load=False):
    """
    Setter method for priority_group_table, mapped from YANG variable /cee_map/priority_group_table (list)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_priority_group_table is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_priority_group_table() directly.
    """
    if hasattr(v, "_utype"):
      v = v._utype(v)
    try:
      t = YANGDynClass(v,base=YANGListType("PGID",priority_group_table.priority_group_table, yang_name="priority-group-table", rest_name="priority-group-table", parent=self, is_container='list', user_ordered=False, path_helper=self._path_helper, yang_keys='PGID', extensions={u'tailf-common': {u'info': u' Configure Priority Group Table', u'cli-no-key-completion': None, u'cli-full-no': None, u'cli-suppress-list-no': None, u'cli-compact-syntax': None, u'cli-sequence-commands': None, u'cli-suppress-mode': None, u'cli-suppress-key-abbreviation': None, u'cli-incomplete-command': None, u'callpoint': u'qos_priority_group'}}), is_container='list', yang_name="priority-group-table", rest_name="priority-group-table", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'info': u' Configure Priority Group Table', u'cli-no-key-completion': None, u'cli-full-no': None, u'cli-suppress-list-no': None, u'cli-compact-syntax': None, u'cli-sequence-commands': None, u'cli-suppress-mode': None, u'cli-suppress-key-abbreviation': None, u'cli-incomplete-command': None, u'callpoint': u'qos_priority_group'}}, namespace='urn:brocade.com:mgmt:brocade-qos-cee', defining_module='brocade-qos-cee', yang_type='list', is_config=True)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """priority_group_table must be of a type compatible with list""",
          'defined-type': "list",
          'generated-type': """YANGDynClass(base=YANGListType("PGID",priority_group_table.priority_group_table, yang_name="priority-group-table", rest_name="priority-group-table", parent=self, is_container='list', user_ordered=False, path_helper=self._path_helper, yang_keys='PGID', extensions={u'tailf-common': {u'info': u' Configure Priority Group Table', u'cli-no-key-completion': None, u'cli-full-no': None, u'cli-suppress-list-no': None, u'cli-compact-syntax': None, u'cli-sequence-commands': None, u'cli-suppress-mode': None, u'cli-suppress-key-abbreviation': None, u'cli-incomplete-command': None, u'callpoint': u'qos_priority_group'}}), is_container='list', yang_name="priority-group-table", rest_name="priority-group-table", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'info': u' Configure Priority Group Table', u'cli-no-key-completion': None, u'cli-full-no': None, u'cli-suppress-list-no': None, u'cli-compact-syntax': None, u'cli-sequence-commands': None, u'cli-suppress-mode': None, u'cli-suppress-key-abbreviation': None, u'cli-incomplete-command': None, u'callpoint': u'qos_priority_group'}}, namespace='urn:brocade.com:mgmt:brocade-qos-cee', defining_module='brocade-qos-cee', yang_type='list', is_config=True)""",
        })

    self.__priority_group_table = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_priority_group_table(self):
    self.__priority_group_table = YANGDynClass(base=YANGListType("PGID",priority_group_table.priority_group_table, yang_name="priority-group-table", rest_name="priority-group-table", parent=self, is_container='list', user_ordered=False, path_helper=self._path_helper, yang_keys='PGID', extensions={u'tailf-common': {u'info': u' Configure Priority Group Table', u'cli-no-key-completion': None, u'cli-full-no': None, u'cli-suppress-list-no': None, u'cli-compact-syntax': None, u'cli-sequence-commands': None, u'cli-suppress-mode': None, u'cli-suppress-key-abbreviation': None, u'cli-incomplete-command': None, u'callpoint': u'qos_priority_group'}}), is_container='list', yang_name="priority-group-table", rest_name="priority-group-table", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'info': u' Configure Priority Group Table', u'cli-no-key-completion': None, u'cli-full-no': None, u'cli-suppress-list-no': None, u'cli-compact-syntax': None, u'cli-sequence-commands': None, u'cli-suppress-mode': None, u'cli-suppress-key-abbreviation': None, u'cli-incomplete-command': None, u'callpoint': u'qos_priority_group'}}, namespace='urn:brocade.com:mgmt:brocade-qos-cee', defining_module='brocade-qos-cee', yang_type='list', is_config=True)


  def _get_priority_table(self):
    """
    Getter method for priority_table, mapped from YANG variable /cee_map/priority_table (container)

    YANG Description: Configure Priority Table
    """
    return self.__priority_table
      
  def _set_priority_table(self, v, load=False):
    """
    Setter method for priority_table, mapped from YANG variable /cee_map/priority_table (container)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_priority_table is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_priority_table() directly.

    YANG Description: Configure Priority Table
    """
    if hasattr(v, "_utype"):
      v = v._utype(v)
    try:
      t = YANGDynClass(v,base=priority_table.priority_table, is_container='container', presence=False, yang_name="priority-table", rest_name="priority-table", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'info': u' Configure Priority Table', u'cli-compact-syntax': None, u'cli-sequence-commands': None, u'callpoint': u'qos_priority_map', u'cli-full-no': None}}, namespace='urn:brocade.com:mgmt:brocade-qos-cee', defining_module='brocade-qos-cee', yang_type='container', is_config=True)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """priority_table must be of a type compatible with container""",
          'defined-type': "container",
          'generated-type': """YANGDynClass(base=priority_table.priority_table, is_container='container', presence=False, yang_name="priority-table", rest_name="priority-table", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'info': u' Configure Priority Table', u'cli-compact-syntax': None, u'cli-sequence-commands': None, u'callpoint': u'qos_priority_map', u'cli-full-no': None}}, namespace='urn:brocade.com:mgmt:brocade-qos-cee', defining_module='brocade-qos-cee', yang_type='container', is_config=True)""",
        })

    self.__priority_table = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_priority_table(self):
    self.__priority_table = YANGDynClass(base=priority_table.priority_table, is_container='container', presence=False, yang_name="priority-table", rest_name="priority-table", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'info': u' Configure Priority Table', u'cli-compact-syntax': None, u'cli-sequence-commands': None, u'callpoint': u'qos_priority_map', u'cli-full-no': None}}, namespace='urn:brocade.com:mgmt:brocade-qos-cee', defining_module='brocade-qos-cee', yang_type='container', is_config=True)


  def _get_remap(self):
    """
    Getter method for remap, mapped from YANG variable /cee_map/remap (container)
    """
    return self.__remap
      
  def _set_remap(self, v, load=False):
    """
    Setter method for remap, mapped from YANG variable /cee_map/remap (container)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_remap is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_remap() directly.
    """
    if hasattr(v, "_utype"):
      v = v._utype(v)
    try:
      t = YANGDynClass(v,base=remap.remap, is_container='container', presence=False, yang_name="remap", rest_name="remap", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'info': u' Configure Class of Service (CoS) to be \n remapped', u'callpoint': u'qos_cee_remap', u'display-when': u'/vcsmode/vcs-mode = "true"'}}, namespace='urn:brocade.com:mgmt:brocade-qos-cee', defining_module='brocade-qos-cee', yang_type='container', is_config=True)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """remap must be of a type compatible with container""",
          'defined-type': "container",
          'generated-type': """YANGDynClass(base=remap.remap, is_container='container', presence=False, yang_name="remap", rest_name="remap", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'info': u' Configure Class of Service (CoS) to be \n remapped', u'callpoint': u'qos_cee_remap', u'display-when': u'/vcsmode/vcs-mode = "true"'}}, namespace='urn:brocade.com:mgmt:brocade-qos-cee', defining_module='brocade-qos-cee', yang_type='container', is_config=True)""",
        })

    self.__remap = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_remap(self):
    self.__remap = YANGDynClass(base=remap.remap, is_container='container', presence=False, yang_name="remap", rest_name="remap", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'info': u' Configure Class of Service (CoS) to be \n remapped', u'callpoint': u'qos_cee_remap', u'display-when': u'/vcsmode/vcs-mode = "true"'}}, namespace='urn:brocade.com:mgmt:brocade-qos-cee', defining_module='brocade-qos-cee', yang_type='container', is_config=True)

  name = __builtin__.property(_get_name, _set_name)
  precedence = __builtin__.property(_get_precedence, _set_precedence)
  priority_group_table = __builtin__.property(_get_priority_group_table, _set_priority_group_table)
  priority_table = __builtin__.property(_get_priority_table, _set_priority_table)
  remap = __builtin__.property(_get_remap, _set_remap)


  _pyangbind_elements = {'name': name, 'precedence': precedence, 'priority_group_table': priority_group_table, 'priority_table': priority_table, 'remap': remap, }


