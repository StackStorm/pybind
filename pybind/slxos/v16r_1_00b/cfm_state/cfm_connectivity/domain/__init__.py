
from operator import attrgetter
import pyangbind.lib.xpathhelper as xpathhelper
from pyangbind.lib.yangtypes import RestrictedPrecisionDecimalType, RestrictedClassType, TypedListType
from pyangbind.lib.yangtypes import YANGBool, YANGListType, YANGDynClass, ReferenceType
from pyangbind.lib.base import PybindBase
from decimal import Decimal
from bitarray import bitarray
import __builtin__
import ma
class domain(PybindBase):
  """
  This class was auto-generated by the PythonClass plugin for PYANG
  from YANG module brocade-dot1ag-operational - based on the path /cfm-state/cfm-connectivity/domain. Each member element of
  the container is represented as a class variable - with a specific
  YANG type.
  """
  __slots__ = ('_pybind_generated_by', '_path_helper', '_yang_name', '_extmethods', '__md_name','__md_level','__ma',)

  _yang_name = 'domain'

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
    self.__md_level = YANGDynClass(base=RestrictedClassType(base_type=int, restriction_dict={'range': ['0..255']}, int_size=8), is_leaf=True, yang_name="md-level", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='urn:brocade.com:mgmt:brocade-dot1ag-operational', defining_module='brocade-dot1ag-operational', yang_type='uint8', is_config=False)
    self.__ma = YANGDynClass(base=YANGListType("ma_name",ma.ma, yang_name="ma", parent=self, is_container='list', user_ordered=False, path_helper=self._path_helper, yang_keys='ma-name', extensions={u'tailf-common': {u'callpoint': u'dot1ag-ma', u'cli-suppress-show-path': None}}), is_container='list', yang_name="ma", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'callpoint': u'dot1ag-ma', u'cli-suppress-show-path': None}}, namespace='urn:brocade.com:mgmt:brocade-dot1ag-operational', defining_module='brocade-dot1ag-operational', yang_type='list', is_config=False)
    self.__md_name = YANGDynClass(base=unicode, is_leaf=True, yang_name="md-name", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, is_keyval=True, namespace='urn:brocade.com:mgmt:brocade-dot1ag-operational', defining_module='brocade-dot1ag-operational', yang_type='string', is_config=False)

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
      return [u'cfm-state', u'cfm-connectivity', u'domain']

  def _rest_path(self):
    if hasattr(self, "_supplied_register_path"):
      return [self._supplied_register_path]
    if hasattr(self, "_parent"):
      return self._parent._rest_path()+[self._yang_name]
    else:
      return [u'cfm-state', u'cfm-connectivity', u'domain']

  def _get_md_name(self):
    """
    Getter method for md_name, mapped from YANG variable /cfm_state/cfm_connectivity/domain/md_name (string)

    YANG Description: domain name
    """
    return self.__md_name
      
  def _set_md_name(self, v, load=False):
    """
    Setter method for md_name, mapped from YANG variable /cfm_state/cfm_connectivity/domain/md_name (string)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_md_name is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_md_name() directly.

    YANG Description: domain name
    """
    parent = getattr(self, "_parent", None)
    if parent is not None and load is False:
      raise AttributeError("Cannot set keys directly when" +
                             " within an instantiated list")

    try:
      t = YANGDynClass(v,base=unicode, is_leaf=True, yang_name="md-name", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, is_keyval=True, namespace='urn:brocade.com:mgmt:brocade-dot1ag-operational', defining_module='brocade-dot1ag-operational', yang_type='string', is_config=False)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """md_name must be of a type compatible with string""",
          'defined-type': "string",
          'generated-type': """YANGDynClass(base=unicode, is_leaf=True, yang_name="md-name", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, is_keyval=True, namespace='urn:brocade.com:mgmt:brocade-dot1ag-operational', defining_module='brocade-dot1ag-operational', yang_type='string', is_config=False)""",
        })

    self.__md_name = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_md_name(self):
    self.__md_name = YANGDynClass(base=unicode, is_leaf=True, yang_name="md-name", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, is_keyval=True, namespace='urn:brocade.com:mgmt:brocade-dot1ag-operational', defining_module='brocade-dot1ag-operational', yang_type='string', is_config=False)


  def _get_md_level(self):
    """
    Getter method for md_level, mapped from YANG variable /cfm_state/cfm_connectivity/domain/md_level (uint8)

    YANG Description: domain level
    """
    return self.__md_level
      
  def _set_md_level(self, v, load=False):
    """
    Setter method for md_level, mapped from YANG variable /cfm_state/cfm_connectivity/domain/md_level (uint8)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_md_level is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_md_level() directly.

    YANG Description: domain level
    """
    try:
      t = YANGDynClass(v,base=RestrictedClassType(base_type=int, restriction_dict={'range': ['0..255']}, int_size=8), is_leaf=True, yang_name="md-level", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='urn:brocade.com:mgmt:brocade-dot1ag-operational', defining_module='brocade-dot1ag-operational', yang_type='uint8', is_config=False)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """md_level must be of a type compatible with uint8""",
          'defined-type': "uint8",
          'generated-type': """YANGDynClass(base=RestrictedClassType(base_type=int, restriction_dict={'range': ['0..255']}, int_size=8), is_leaf=True, yang_name="md-level", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='urn:brocade.com:mgmt:brocade-dot1ag-operational', defining_module='brocade-dot1ag-operational', yang_type='uint8', is_config=False)""",
        })

    self.__md_level = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_md_level(self):
    self.__md_level = YANGDynClass(base=RestrictedClassType(base_type=int, restriction_dict={'range': ['0..255']}, int_size=8), is_leaf=True, yang_name="md-level", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='urn:brocade.com:mgmt:brocade-dot1ag-operational', defining_module='brocade-dot1ag-operational', yang_type='uint8', is_config=False)


  def _get_ma(self):
    """
    Getter method for ma, mapped from YANG variable /cfm_state/cfm_connectivity/domain/ma (list)

    YANG Description: CFM Ma Details
    """
    return self.__ma
      
  def _set_ma(self, v, load=False):
    """
    Setter method for ma, mapped from YANG variable /cfm_state/cfm_connectivity/domain/ma (list)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_ma is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_ma() directly.

    YANG Description: CFM Ma Details
    """
    try:
      t = YANGDynClass(v,base=YANGListType("ma_name",ma.ma, yang_name="ma", parent=self, is_container='list', user_ordered=False, path_helper=self._path_helper, yang_keys='ma-name', extensions={u'tailf-common': {u'callpoint': u'dot1ag-ma', u'cli-suppress-show-path': None}}), is_container='list', yang_name="ma", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'callpoint': u'dot1ag-ma', u'cli-suppress-show-path': None}}, namespace='urn:brocade.com:mgmt:brocade-dot1ag-operational', defining_module='brocade-dot1ag-operational', yang_type='list', is_config=False)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """ma must be of a type compatible with list""",
          'defined-type': "list",
          'generated-type': """YANGDynClass(base=YANGListType("ma_name",ma.ma, yang_name="ma", parent=self, is_container='list', user_ordered=False, path_helper=self._path_helper, yang_keys='ma-name', extensions={u'tailf-common': {u'callpoint': u'dot1ag-ma', u'cli-suppress-show-path': None}}), is_container='list', yang_name="ma", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'callpoint': u'dot1ag-ma', u'cli-suppress-show-path': None}}, namespace='urn:brocade.com:mgmt:brocade-dot1ag-operational', defining_module='brocade-dot1ag-operational', yang_type='list', is_config=False)""",
        })

    self.__ma = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_ma(self):
    self.__ma = YANGDynClass(base=YANGListType("ma_name",ma.ma, yang_name="ma", parent=self, is_container='list', user_ordered=False, path_helper=self._path_helper, yang_keys='ma-name', extensions={u'tailf-common': {u'callpoint': u'dot1ag-ma', u'cli-suppress-show-path': None}}), is_container='list', yang_name="ma", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'callpoint': u'dot1ag-ma', u'cli-suppress-show-path': None}}, namespace='urn:brocade.com:mgmt:brocade-dot1ag-operational', defining_module='brocade-dot1ag-operational', yang_type='list', is_config=False)

  md_name = __builtin__.property(_get_md_name)
  md_level = __builtin__.property(_get_md_level)
  ma = __builtin__.property(_get_ma)


  _pyangbind_elements = {'md_name': md_name, 'md_level': md_level, 'ma': ma, }

