
from operator import attrgetter
import pyangbind.lib.xpathhelper as xpathhelper
from pyangbind.lib.yangtypes import RestrictedPrecisionDecimalType, RestrictedClassType, TypedListType
from pyangbind.lib.yangtypes import YANGBool, YANGListType, YANGDynClass, ReferenceType
from pyangbind.lib.base import PybindBase
from decimal import Decimal
from bitarray import bitarray
import __builtin__
import dynamic_bypass_global
import dynamic_bypass_interface
class dynamic_bypass(PybindBase):
  """
  This class was auto-generated by the PythonClass plugin for PYANG
  from YANG module brocade-mpls-operational - based on the path /mpls-state/dynamic-bypass. Each member element of
  the container is represented as a class variable - with a specific
  YANG type.

  YANG Description: MPLS dynamic bypass
  """
  __slots__ = ('_pybind_generated_by', '_path_helper', '_yang_name', '_rest_name', '_extmethods', '__dynamic_bypass_global','__dynamic_bypass_interface',)

  _yang_name = 'dynamic-bypass'
  _rest_name = 'dynamic-bypass'

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
    self.__dynamic_bypass_global = YANGDynClass(base=dynamic_bypass_global.dynamic_bypass_global, is_container='container', presence=False, yang_name="dynamic-bypass-global", rest_name="dynamic-bypass-global", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'callpoint': u'mpls-dynamic-bypass-global', u'cli-suppress-show-path': None}}, namespace='urn:brocade.com:mgmt:brocade-mpls-operational', defining_module='brocade-mpls-operational', yang_type='container', is_config=False)
    self.__dynamic_bypass_interface = YANGDynClass(base=YANGListType("if_name if_type",dynamic_bypass_interface.dynamic_bypass_interface, yang_name="dynamic-bypass-interface", rest_name="dynamic-bypass-interface", parent=self, is_container='list', user_ordered=False, path_helper=self._path_helper, yang_keys='if-name if-type', extensions={u'tailf-common': {u'callpoint': u'mpls-dynamic-bypass-interface', u'cli-suppress-show-path': None}}), is_container='list', yang_name="dynamic-bypass-interface", rest_name="dynamic-bypass-interface", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'callpoint': u'mpls-dynamic-bypass-interface', u'cli-suppress-show-path': None}}, namespace='urn:brocade.com:mgmt:brocade-mpls-operational', defining_module='brocade-mpls-operational', yang_type='list', is_config=False)

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
      return [u'mpls-state', u'dynamic-bypass']

  def _rest_path(self):
    if hasattr(self, "_parent"):
      if self._rest_name:
        return self._parent._rest_path()+[self._rest_name]
      else:
        return self._parent._rest_path()
    else:
      return [u'mpls-state', u'dynamic-bypass']

  def _get_dynamic_bypass_global(self):
    """
    Getter method for dynamic_bypass_global, mapped from YANG variable /mpls_state/dynamic_bypass/dynamic_bypass_global (container)

    YANG Description: MPLS dynamic bypass
    """
    return self.__dynamic_bypass_global
      
  def _set_dynamic_bypass_global(self, v, load=False):
    """
    Setter method for dynamic_bypass_global, mapped from YANG variable /mpls_state/dynamic_bypass/dynamic_bypass_global (container)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_dynamic_bypass_global is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_dynamic_bypass_global() directly.

    YANG Description: MPLS dynamic bypass
    """
    if hasattr(v, "_utype"):
      v = v._utype(v)
    try:
      t = YANGDynClass(v,base=dynamic_bypass_global.dynamic_bypass_global, is_container='container', presence=False, yang_name="dynamic-bypass-global", rest_name="dynamic-bypass-global", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'callpoint': u'mpls-dynamic-bypass-global', u'cli-suppress-show-path': None}}, namespace='urn:brocade.com:mgmt:brocade-mpls-operational', defining_module='brocade-mpls-operational', yang_type='container', is_config=False)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """dynamic_bypass_global must be of a type compatible with container""",
          'defined-type': "container",
          'generated-type': """YANGDynClass(base=dynamic_bypass_global.dynamic_bypass_global, is_container='container', presence=False, yang_name="dynamic-bypass-global", rest_name="dynamic-bypass-global", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'callpoint': u'mpls-dynamic-bypass-global', u'cli-suppress-show-path': None}}, namespace='urn:brocade.com:mgmt:brocade-mpls-operational', defining_module='brocade-mpls-operational', yang_type='container', is_config=False)""",
        })

    self.__dynamic_bypass_global = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_dynamic_bypass_global(self):
    self.__dynamic_bypass_global = YANGDynClass(base=dynamic_bypass_global.dynamic_bypass_global, is_container='container', presence=False, yang_name="dynamic-bypass-global", rest_name="dynamic-bypass-global", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'callpoint': u'mpls-dynamic-bypass-global', u'cli-suppress-show-path': None}}, namespace='urn:brocade.com:mgmt:brocade-mpls-operational', defining_module='brocade-mpls-operational', yang_type='container', is_config=False)


  def _get_dynamic_bypass_interface(self):
    """
    Getter method for dynamic_bypass_interface, mapped from YANG variable /mpls_state/dynamic_bypass/dynamic_bypass_interface (list)

    YANG Description: MPLS dynamic bypass interface
    """
    return self.__dynamic_bypass_interface
      
  def _set_dynamic_bypass_interface(self, v, load=False):
    """
    Setter method for dynamic_bypass_interface, mapped from YANG variable /mpls_state/dynamic_bypass/dynamic_bypass_interface (list)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_dynamic_bypass_interface is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_dynamic_bypass_interface() directly.

    YANG Description: MPLS dynamic bypass interface
    """
    if hasattr(v, "_utype"):
      v = v._utype(v)
    try:
      t = YANGDynClass(v,base=YANGListType("if_name if_type",dynamic_bypass_interface.dynamic_bypass_interface, yang_name="dynamic-bypass-interface", rest_name="dynamic-bypass-interface", parent=self, is_container='list', user_ordered=False, path_helper=self._path_helper, yang_keys='if-name if-type', extensions={u'tailf-common': {u'callpoint': u'mpls-dynamic-bypass-interface', u'cli-suppress-show-path': None}}), is_container='list', yang_name="dynamic-bypass-interface", rest_name="dynamic-bypass-interface", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'callpoint': u'mpls-dynamic-bypass-interface', u'cli-suppress-show-path': None}}, namespace='urn:brocade.com:mgmt:brocade-mpls-operational', defining_module='brocade-mpls-operational', yang_type='list', is_config=False)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """dynamic_bypass_interface must be of a type compatible with list""",
          'defined-type': "list",
          'generated-type': """YANGDynClass(base=YANGListType("if_name if_type",dynamic_bypass_interface.dynamic_bypass_interface, yang_name="dynamic-bypass-interface", rest_name="dynamic-bypass-interface", parent=self, is_container='list', user_ordered=False, path_helper=self._path_helper, yang_keys='if-name if-type', extensions={u'tailf-common': {u'callpoint': u'mpls-dynamic-bypass-interface', u'cli-suppress-show-path': None}}), is_container='list', yang_name="dynamic-bypass-interface", rest_name="dynamic-bypass-interface", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'callpoint': u'mpls-dynamic-bypass-interface', u'cli-suppress-show-path': None}}, namespace='urn:brocade.com:mgmt:brocade-mpls-operational', defining_module='brocade-mpls-operational', yang_type='list', is_config=False)""",
        })

    self.__dynamic_bypass_interface = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_dynamic_bypass_interface(self):
    self.__dynamic_bypass_interface = YANGDynClass(base=YANGListType("if_name if_type",dynamic_bypass_interface.dynamic_bypass_interface, yang_name="dynamic-bypass-interface", rest_name="dynamic-bypass-interface", parent=self, is_container='list', user_ordered=False, path_helper=self._path_helper, yang_keys='if-name if-type', extensions={u'tailf-common': {u'callpoint': u'mpls-dynamic-bypass-interface', u'cli-suppress-show-path': None}}), is_container='list', yang_name="dynamic-bypass-interface", rest_name="dynamic-bypass-interface", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'callpoint': u'mpls-dynamic-bypass-interface', u'cli-suppress-show-path': None}}, namespace='urn:brocade.com:mgmt:brocade-mpls-operational', defining_module='brocade-mpls-operational', yang_type='list', is_config=False)

  dynamic_bypass_global = __builtin__.property(_get_dynamic_bypass_global)
  dynamic_bypass_interface = __builtin__.property(_get_dynamic_bypass_interface)


  _pyangbind_elements = {'dynamic_bypass_global': dynamic_bypass_global, 'dynamic_bypass_interface': dynamic_bypass_interface, }


