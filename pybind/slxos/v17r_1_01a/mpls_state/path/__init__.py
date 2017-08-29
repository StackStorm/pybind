
from operator import attrgetter
import pyangbind.lib.xpathhelper as xpathhelper
from pyangbind.lib.yangtypes import RestrictedPrecisionDecimalType, RestrictedClassType, TypedListType
from pyangbind.lib.yangtypes import YANGBool, YANGListType, YANGDynClass, ReferenceType
from pyangbind.lib.base import PybindBase
from decimal import Decimal
from bitarray import bitarray
import __builtin__
import path_hops
import path_lsps
class path(PybindBase):
  """
  This class was auto-generated by the PythonClass plugin for PYANG
  from YANG module brocade-mpls-operational - based on the path /mpls-state/path. Each member element of
  the container is represented as a class variable - with a specific
  YANG type.

  YANG Description: MPLS Path
  """
  __slots__ = ('_pybind_generated_by', '_path_helper', '_yang_name', '_rest_name', '_extmethods', '__path_name','__usage_count','__path_hops','__path_lsps',)

  _yang_name = 'path'
  _rest_name = 'path'

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
    self.__path_name = YANGDynClass(base=unicode, is_leaf=True, yang_name="path-name", rest_name="path-name", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, is_keyval=True, namespace='urn:brocade.com:mgmt:brocade-mpls-operational', defining_module='brocade-mpls-operational', yang_type='string', is_config=False)
    self.__path_hops = YANGDynClass(base=YANGListType("hop_address",path_hops.path_hops, yang_name="path-hops", rest_name="path-hops", parent=self, is_container='list', user_ordered=False, path_helper=self._path_helper, yang_keys='hop-address', extensions={u'tailf-common': {u'callpoint': u'mpls-path-hop', u'cli-suppress-show-path': None}}), is_container='list', yang_name="path-hops", rest_name="path-hops", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'callpoint': u'mpls-path-hop', u'cli-suppress-show-path': None}}, namespace='urn:brocade.com:mgmt:brocade-mpls-operational', defining_module='brocade-mpls-operational', yang_type='list', is_config=False)
    self.__usage_count = YANGDynClass(base=RestrictedClassType(base_type=long, restriction_dict={'range': ['0..4294967295']}, int_size=32), is_leaf=True, yang_name="usage-count", rest_name="usage-count", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='urn:brocade.com:mgmt:brocade-mpls-operational', defining_module='brocade-mpls-operational', yang_type='uint32', is_config=False)
    self.__path_lsps = YANGDynClass(base=YANGListType("lsp_name",path_lsps.path_lsps, yang_name="path-lsps", rest_name="path-lsps", parent=self, is_container='list', user_ordered=False, path_helper=self._path_helper, yang_keys='lsp-name', extensions={u'tailf-common': {u'callpoint': u'mpls-path-lsp', u'cli-suppress-show-path': None}}), is_container='list', yang_name="path-lsps", rest_name="path-lsps", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'callpoint': u'mpls-path-lsp', u'cli-suppress-show-path': None}}, namespace='urn:brocade.com:mgmt:brocade-mpls-operational', defining_module='brocade-mpls-operational', yang_type='list', is_config=False)

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
      return [u'mpls-state', u'path']

  def _rest_path(self):
    if hasattr(self, "_parent"):
      if self._rest_name:
        return self._parent._rest_path()+[self._rest_name]
      else:
        return self._parent._rest_path()
    else:
      return [u'mpls-state', u'path']

  def _get_path_name(self):
    """
    Getter method for path_name, mapped from YANG variable /mpls_state/path/path_name (string)

    YANG Description: Path name
    """
    return self.__path_name
      
  def _set_path_name(self, v, load=False):
    """
    Setter method for path_name, mapped from YANG variable /mpls_state/path/path_name (string)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_path_name is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_path_name() directly.

    YANG Description: Path name
    """
    parent = getattr(self, "_parent", None)
    if parent is not None and load is False:
      raise AttributeError("Cannot set keys directly when" +
                             " within an instantiated list")

    if hasattr(v, "_utype"):
      v = v._utype(v)
    try:
      t = YANGDynClass(v,base=unicode, is_leaf=True, yang_name="path-name", rest_name="path-name", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, is_keyval=True, namespace='urn:brocade.com:mgmt:brocade-mpls-operational', defining_module='brocade-mpls-operational', yang_type='string', is_config=False)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """path_name must be of a type compatible with string""",
          'defined-type': "string",
          'generated-type': """YANGDynClass(base=unicode, is_leaf=True, yang_name="path-name", rest_name="path-name", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, is_keyval=True, namespace='urn:brocade.com:mgmt:brocade-mpls-operational', defining_module='brocade-mpls-operational', yang_type='string', is_config=False)""",
        })

    self.__path_name = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_path_name(self):
    self.__path_name = YANGDynClass(base=unicode, is_leaf=True, yang_name="path-name", rest_name="path-name", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, is_keyval=True, namespace='urn:brocade.com:mgmt:brocade-mpls-operational', defining_module='brocade-mpls-operational', yang_type='string', is_config=False)


  def _get_usage_count(self):
    """
    Getter method for usage_count, mapped from YANG variable /mpls_state/path/usage_count (uint32)

    YANG Description: Path usage count
    """
    return self.__usage_count
      
  def _set_usage_count(self, v, load=False):
    """
    Setter method for usage_count, mapped from YANG variable /mpls_state/path/usage_count (uint32)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_usage_count is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_usage_count() directly.

    YANG Description: Path usage count
    """
    if hasattr(v, "_utype"):
      v = v._utype(v)
    try:
      t = YANGDynClass(v,base=RestrictedClassType(base_type=long, restriction_dict={'range': ['0..4294967295']}, int_size=32), is_leaf=True, yang_name="usage-count", rest_name="usage-count", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='urn:brocade.com:mgmt:brocade-mpls-operational', defining_module='brocade-mpls-operational', yang_type='uint32', is_config=False)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """usage_count must be of a type compatible with uint32""",
          'defined-type': "uint32",
          'generated-type': """YANGDynClass(base=RestrictedClassType(base_type=long, restriction_dict={'range': ['0..4294967295']}, int_size=32), is_leaf=True, yang_name="usage-count", rest_name="usage-count", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='urn:brocade.com:mgmt:brocade-mpls-operational', defining_module='brocade-mpls-operational', yang_type='uint32', is_config=False)""",
        })

    self.__usage_count = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_usage_count(self):
    self.__usage_count = YANGDynClass(base=RestrictedClassType(base_type=long, restriction_dict={'range': ['0..4294967295']}, int_size=32), is_leaf=True, yang_name="usage-count", rest_name="usage-count", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='urn:brocade.com:mgmt:brocade-mpls-operational', defining_module='brocade-mpls-operational', yang_type='uint32', is_config=False)


  def _get_path_hops(self):
    """
    Getter method for path_hops, mapped from YANG variable /mpls_state/path/path_hops (list)

    YANG Description: Path hop entry
    """
    return self.__path_hops
      
  def _set_path_hops(self, v, load=False):
    """
    Setter method for path_hops, mapped from YANG variable /mpls_state/path/path_hops (list)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_path_hops is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_path_hops() directly.

    YANG Description: Path hop entry
    """
    if hasattr(v, "_utype"):
      v = v._utype(v)
    try:
      t = YANGDynClass(v,base=YANGListType("hop_address",path_hops.path_hops, yang_name="path-hops", rest_name="path-hops", parent=self, is_container='list', user_ordered=False, path_helper=self._path_helper, yang_keys='hop-address', extensions={u'tailf-common': {u'callpoint': u'mpls-path-hop', u'cli-suppress-show-path': None}}), is_container='list', yang_name="path-hops", rest_name="path-hops", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'callpoint': u'mpls-path-hop', u'cli-suppress-show-path': None}}, namespace='urn:brocade.com:mgmt:brocade-mpls-operational', defining_module='brocade-mpls-operational', yang_type='list', is_config=False)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """path_hops must be of a type compatible with list""",
          'defined-type': "list",
          'generated-type': """YANGDynClass(base=YANGListType("hop_address",path_hops.path_hops, yang_name="path-hops", rest_name="path-hops", parent=self, is_container='list', user_ordered=False, path_helper=self._path_helper, yang_keys='hop-address', extensions={u'tailf-common': {u'callpoint': u'mpls-path-hop', u'cli-suppress-show-path': None}}), is_container='list', yang_name="path-hops", rest_name="path-hops", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'callpoint': u'mpls-path-hop', u'cli-suppress-show-path': None}}, namespace='urn:brocade.com:mgmt:brocade-mpls-operational', defining_module='brocade-mpls-operational', yang_type='list', is_config=False)""",
        })

    self.__path_hops = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_path_hops(self):
    self.__path_hops = YANGDynClass(base=YANGListType("hop_address",path_hops.path_hops, yang_name="path-hops", rest_name="path-hops", parent=self, is_container='list', user_ordered=False, path_helper=self._path_helper, yang_keys='hop-address', extensions={u'tailf-common': {u'callpoint': u'mpls-path-hop', u'cli-suppress-show-path': None}}), is_container='list', yang_name="path-hops", rest_name="path-hops", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'callpoint': u'mpls-path-hop', u'cli-suppress-show-path': None}}, namespace='urn:brocade.com:mgmt:brocade-mpls-operational', defining_module='brocade-mpls-operational', yang_type='list', is_config=False)


  def _get_path_lsps(self):
    """
    Getter method for path_lsps, mapped from YANG variable /mpls_state/path/path_lsps (list)

    YANG Description: Path lsp entry
    """
    return self.__path_lsps
      
  def _set_path_lsps(self, v, load=False):
    """
    Setter method for path_lsps, mapped from YANG variable /mpls_state/path/path_lsps (list)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_path_lsps is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_path_lsps() directly.

    YANG Description: Path lsp entry
    """
    if hasattr(v, "_utype"):
      v = v._utype(v)
    try:
      t = YANGDynClass(v,base=YANGListType("lsp_name",path_lsps.path_lsps, yang_name="path-lsps", rest_name="path-lsps", parent=self, is_container='list', user_ordered=False, path_helper=self._path_helper, yang_keys='lsp-name', extensions={u'tailf-common': {u'callpoint': u'mpls-path-lsp', u'cli-suppress-show-path': None}}), is_container='list', yang_name="path-lsps", rest_name="path-lsps", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'callpoint': u'mpls-path-lsp', u'cli-suppress-show-path': None}}, namespace='urn:brocade.com:mgmt:brocade-mpls-operational', defining_module='brocade-mpls-operational', yang_type='list', is_config=False)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """path_lsps must be of a type compatible with list""",
          'defined-type': "list",
          'generated-type': """YANGDynClass(base=YANGListType("lsp_name",path_lsps.path_lsps, yang_name="path-lsps", rest_name="path-lsps", parent=self, is_container='list', user_ordered=False, path_helper=self._path_helper, yang_keys='lsp-name', extensions={u'tailf-common': {u'callpoint': u'mpls-path-lsp', u'cli-suppress-show-path': None}}), is_container='list', yang_name="path-lsps", rest_name="path-lsps", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'callpoint': u'mpls-path-lsp', u'cli-suppress-show-path': None}}, namespace='urn:brocade.com:mgmt:brocade-mpls-operational', defining_module='brocade-mpls-operational', yang_type='list', is_config=False)""",
        })

    self.__path_lsps = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_path_lsps(self):
    self.__path_lsps = YANGDynClass(base=YANGListType("lsp_name",path_lsps.path_lsps, yang_name="path-lsps", rest_name="path-lsps", parent=self, is_container='list', user_ordered=False, path_helper=self._path_helper, yang_keys='lsp-name', extensions={u'tailf-common': {u'callpoint': u'mpls-path-lsp', u'cli-suppress-show-path': None}}), is_container='list', yang_name="path-lsps", rest_name="path-lsps", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'callpoint': u'mpls-path-lsp', u'cli-suppress-show-path': None}}, namespace='urn:brocade.com:mgmt:brocade-mpls-operational', defining_module='brocade-mpls-operational', yang_type='list', is_config=False)

  path_name = __builtin__.property(_get_path_name)
  usage_count = __builtin__.property(_get_usage_count)
  path_hops = __builtin__.property(_get_path_hops)
  path_lsps = __builtin__.property(_get_path_lsps)


  _pyangbind_elements = {'path_name': path_name, 'usage_count': usage_count, 'path_hops': path_hops, 'path_lsps': path_lsps, }

