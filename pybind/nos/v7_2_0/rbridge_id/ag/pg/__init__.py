
from operator import attrgetter
import pyangbind.lib.xpathhelper as xpathhelper
from pyangbind.lib.yangtypes import RestrictedPrecisionDecimalType, RestrictedClassType, TypedListType
from pyangbind.lib.yangtypes import YANGBool, YANGListType, YANGDynClass, ReferenceType
from pyangbind.lib.base import PybindBase
from decimal import Decimal
from bitarray import bitarray
import __builtin__
import nport
class pg(PybindBase):
  """
  This class was auto-generated by the PythonClass plugin for PYANG
  from YANG module brocade-rbridge - based on the path /rbridge-id/ag/pg. Each member element of
  the container is represented as a class variable - with a specific
  YANG type.
  """
  __slots__ = ('_pybind_generated_by', '_path_helper', '_yang_name', '_rest_name', '_extmethods', '__pgid','__nport','__modes','__rename',)

  _yang_name = 'pg'
  _rest_name = 'pg'

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
    self.__rename = YANGDynClass(base=unicode, is_leaf=True, yang_name="rename", rest_name="rename", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'info': u'Renames the PG'}}, namespace='urn:brocade.com:mgmt:brocade-ag', defining_module='brocade-ag', yang_type='string', is_config=True)
    self.__nport = YANGDynClass(base=nport.nport, is_container='container', presence=False, yang_name="nport", rest_name="nport", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'info': u'Adds N port(s) to the PG'}}, namespace='urn:brocade.com:mgmt:brocade-ag', defining_module='brocade-ag', yang_type='container', is_config=True)
    self.__pgid = YANGDynClass(base=RestrictedClassType(base_type=RestrictedClassType(base_type=long, restriction_dict={'range': ['0..4294967295']}, int_size=32), restriction_dict={'range': [u'0..1000']}), is_leaf=True, yang_name="pgid", rest_name="pgid", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, is_keyval=True, namespace='urn:brocade.com:mgmt:brocade-ag', defining_module='brocade-ag', yang_type='pgid-type', is_config=True)
    self.__modes = YANGDynClass(base=TypedListType(allowed_type=RestrictedClassType(base_type=unicode, restriction_dict={'length': [u'1..10']})), is_leaf=False, yang_name="modes", rest_name="modes", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'info': u'Adds mode(s) to the PG', u'cli-flat-list-syntax': None}}, namespace='urn:brocade.com:mgmt:brocade-ag', defining_module='brocade-ag', yang_type='pg-policy-types', is_config=True)

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
      return [u'rbridge-id', u'ag', u'pg']

  def _rest_path(self):
    if hasattr(self, "_parent"):
      if self._rest_name:
        return self._parent._rest_path()+[self._rest_name]
      else:
        return self._parent._rest_path()
    else:
      return [u'rbridge-id', u'ag', u'pg']

  def _get_pgid(self):
    """
    Getter method for pgid, mapped from YANG variable /rbridge_id/ag/pg/pgid (pgid-type)
    """
    return self.__pgid
      
  def _set_pgid(self, v, load=False):
    """
    Setter method for pgid, mapped from YANG variable /rbridge_id/ag/pg/pgid (pgid-type)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_pgid is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_pgid() directly.
    """
    parent = getattr(self, "_parent", None)
    if parent is not None and load is False:
      raise AttributeError("Cannot set keys directly when" +
                             " within an instantiated list")

    if hasattr(v, "_utype"):
      v = v._utype(v)
    try:
      t = YANGDynClass(v,base=RestrictedClassType(base_type=RestrictedClassType(base_type=long, restriction_dict={'range': ['0..4294967295']}, int_size=32), restriction_dict={'range': [u'0..1000']}), is_leaf=True, yang_name="pgid", rest_name="pgid", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, is_keyval=True, namespace='urn:brocade.com:mgmt:brocade-ag', defining_module='brocade-ag', yang_type='pgid-type', is_config=True)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """pgid must be of a type compatible with pgid-type""",
          'defined-type': "brocade-ag:pgid-type",
          'generated-type': """YANGDynClass(base=RestrictedClassType(base_type=RestrictedClassType(base_type=long, restriction_dict={'range': ['0..4294967295']}, int_size=32), restriction_dict={'range': [u'0..1000']}), is_leaf=True, yang_name="pgid", rest_name="pgid", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, is_keyval=True, namespace='urn:brocade.com:mgmt:brocade-ag', defining_module='brocade-ag', yang_type='pgid-type', is_config=True)""",
        })

    self.__pgid = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_pgid(self):
    self.__pgid = YANGDynClass(base=RestrictedClassType(base_type=RestrictedClassType(base_type=long, restriction_dict={'range': ['0..4294967295']}, int_size=32), restriction_dict={'range': [u'0..1000']}), is_leaf=True, yang_name="pgid", rest_name="pgid", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, is_keyval=True, namespace='urn:brocade.com:mgmt:brocade-ag', defining_module='brocade-ag', yang_type='pgid-type', is_config=True)


  def _get_nport(self):
    """
    Getter method for nport, mapped from YANG variable /rbridge_id/ag/pg/nport (container)
    """
    return self.__nport
      
  def _set_nport(self, v, load=False):
    """
    Setter method for nport, mapped from YANG variable /rbridge_id/ag/pg/nport (container)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_nport is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_nport() directly.
    """
    if hasattr(v, "_utype"):
      v = v._utype(v)
    try:
      t = YANGDynClass(v,base=nport.nport, is_container='container', presence=False, yang_name="nport", rest_name="nport", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'info': u'Adds N port(s) to the PG'}}, namespace='urn:brocade.com:mgmt:brocade-ag', defining_module='brocade-ag', yang_type='container', is_config=True)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """nport must be of a type compatible with container""",
          'defined-type': "container",
          'generated-type': """YANGDynClass(base=nport.nport, is_container='container', presence=False, yang_name="nport", rest_name="nport", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'info': u'Adds N port(s) to the PG'}}, namespace='urn:brocade.com:mgmt:brocade-ag', defining_module='brocade-ag', yang_type='container', is_config=True)""",
        })

    self.__nport = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_nport(self):
    self.__nport = YANGDynClass(base=nport.nport, is_container='container', presence=False, yang_name="nport", rest_name="nport", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'info': u'Adds N port(s) to the PG'}}, namespace='urn:brocade.com:mgmt:brocade-ag', defining_module='brocade-ag', yang_type='container', is_config=True)


  def _get_modes(self):
    """
    Getter method for modes, mapped from YANG variable /rbridge_id/ag/pg/modes (pg-policy-types)
    """
    return self.__modes
      
  def _set_modes(self, v, load=False):
    """
    Setter method for modes, mapped from YANG variable /rbridge_id/ag/pg/modes (pg-policy-types)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_modes is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_modes() directly.
    """
    if hasattr(v, "_utype"):
      v = v._utype(v)
    try:
      t = YANGDynClass(v,base=TypedListType(allowed_type=RestrictedClassType(base_type=unicode, restriction_dict={'length': [u'1..10']})), is_leaf=False, yang_name="modes", rest_name="modes", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'info': u'Adds mode(s) to the PG', u'cli-flat-list-syntax': None}}, namespace='urn:brocade.com:mgmt:brocade-ag', defining_module='brocade-ag', yang_type='pg-policy-types', is_config=True)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """modes must be of a type compatible with pg-policy-types""",
          'defined-type': "brocade-ag:pg-policy-types",
          'generated-type': """YANGDynClass(base=TypedListType(allowed_type=RestrictedClassType(base_type=unicode, restriction_dict={'length': [u'1..10']})), is_leaf=False, yang_name="modes", rest_name="modes", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'info': u'Adds mode(s) to the PG', u'cli-flat-list-syntax': None}}, namespace='urn:brocade.com:mgmt:brocade-ag', defining_module='brocade-ag', yang_type='pg-policy-types', is_config=True)""",
        })

    self.__modes = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_modes(self):
    self.__modes = YANGDynClass(base=TypedListType(allowed_type=RestrictedClassType(base_type=unicode, restriction_dict={'length': [u'1..10']})), is_leaf=False, yang_name="modes", rest_name="modes", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'info': u'Adds mode(s) to the PG', u'cli-flat-list-syntax': None}}, namespace='urn:brocade.com:mgmt:brocade-ag', defining_module='brocade-ag', yang_type='pg-policy-types', is_config=True)


  def _get_rename(self):
    """
    Getter method for rename, mapped from YANG variable /rbridge_id/ag/pg/rename (string)
    """
    return self.__rename
      
  def _set_rename(self, v, load=False):
    """
    Setter method for rename, mapped from YANG variable /rbridge_id/ag/pg/rename (string)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_rename is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_rename() directly.
    """
    if hasattr(v, "_utype"):
      v = v._utype(v)
    try:
      t = YANGDynClass(v,base=unicode, is_leaf=True, yang_name="rename", rest_name="rename", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'info': u'Renames the PG'}}, namespace='urn:brocade.com:mgmt:brocade-ag', defining_module='brocade-ag', yang_type='string', is_config=True)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """rename must be of a type compatible with string""",
          'defined-type': "string",
          'generated-type': """YANGDynClass(base=unicode, is_leaf=True, yang_name="rename", rest_name="rename", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'info': u'Renames the PG'}}, namespace='urn:brocade.com:mgmt:brocade-ag', defining_module='brocade-ag', yang_type='string', is_config=True)""",
        })

    self.__rename = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_rename(self):
    self.__rename = YANGDynClass(base=unicode, is_leaf=True, yang_name="rename", rest_name="rename", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'info': u'Renames the PG'}}, namespace='urn:brocade.com:mgmt:brocade-ag', defining_module='brocade-ag', yang_type='string', is_config=True)

  pgid = __builtin__.property(_get_pgid, _set_pgid)
  nport = __builtin__.property(_get_nport, _set_nport)
  modes = __builtin__.property(_get_modes, _set_modes)
  rename = __builtin__.property(_get_rename, _set_rename)


  _pyangbind_elements = {'pgid': pgid, 'nport': nport, 'modes': modes, 'rename': rename, }


