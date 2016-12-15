
from operator import attrgetter
import pyangbind.lib.xpathhelper as xpathhelper
from pyangbind.lib.yangtypes import RestrictedPrecisionDecimalType, RestrictedClassType, TypedListType
from pyangbind.lib.yangtypes import YANGBool, YANGListType, YANGDynClass, ReferenceType
from pyangbind.lib.base import PybindBase
from decimal import Decimal
from bitarray import bitarray
import __builtin__
import gos_stats
import host_stats
class cpu_interface_state(PybindBase):
  """
  This class was auto-generated by the PythonClass plugin for PYANG
  from YANG module brocade-sysdiag-operational - based on the path /cpu-interface-state. Each member element of
  the container is represented as a class variable - with a specific
  YANG type.

  YANG Description: CPU ethernet interface stats
  """
  __slots__ = ('_pybind_generated_by', '_path_helper', '_yang_name', '_rest_name', '_extmethods', '__ifname','__gos_stats','__host_stats',)

  _yang_name = 'cpu-interface-state'
  _rest_name = 'cpu-interface-state'

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
    self.__gos_stats = YANGDynClass(base=gos_stats.gos_stats, is_container='container', yang_name="gos-stats", rest_name="gos-stats", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'callpoint': u'sysdiag-stats-gos-stats-1'}}, namespace='urn:brocade.com:mgmt:brocade-sysdiag-operational', defining_module='brocade-sysdiag-operational', yang_type='container', is_config=False)
    self.__ifname = YANGDynClass(base=unicode, is_leaf=True, yang_name="ifname", rest_name="ifname", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, is_keyval=True, namespace='urn:brocade.com:mgmt:brocade-sysdiag-operational', defining_module='brocade-sysdiag-operational', yang_type='string', is_config=False)
    self.__host_stats = YANGDynClass(base=host_stats.host_stats, is_container='container', yang_name="host-stats", rest_name="host-stats", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'callpoint': u'sysdiag-stats-host-stats-1'}}, namespace='urn:brocade.com:mgmt:brocade-sysdiag-operational', defining_module='brocade-sysdiag-operational', yang_type='container', is_config=False)

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
      return [u'cpu-interface-state']

  def _rest_path(self):
    if hasattr(self, "_parent"):
      if self._rest_name:
        return self._parent._rest_path()+[self._rest_name]
      else:
        return self._parent._rest_path()
    else:
      return [u'cpu-interface-state']

  def _get_ifname(self):
    """
    Getter method for ifname, mapped from YANG variable /cpu_interface_state/ifname (string)

    YANG Description: Interface name
    """
    return self.__ifname
      
  def _set_ifname(self, v, load=False):
    """
    Setter method for ifname, mapped from YANG variable /cpu_interface_state/ifname (string)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_ifname is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_ifname() directly.

    YANG Description: Interface name
    """
    parent = getattr(self, "_parent", None)
    if parent is not None and load is False:
      raise AttributeError("Cannot set keys directly when" +
                             " within an instantiated list")

    if hasattr(v, "_utype"):
      v = v._utype(v)
    try:
      t = YANGDynClass(v,base=unicode, is_leaf=True, yang_name="ifname", rest_name="ifname", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, is_keyval=True, namespace='urn:brocade.com:mgmt:brocade-sysdiag-operational', defining_module='brocade-sysdiag-operational', yang_type='string', is_config=False)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """ifname must be of a type compatible with string""",
          'defined-type': "string",
          'generated-type': """YANGDynClass(base=unicode, is_leaf=True, yang_name="ifname", rest_name="ifname", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, is_keyval=True, namespace='urn:brocade.com:mgmt:brocade-sysdiag-operational', defining_module='brocade-sysdiag-operational', yang_type='string', is_config=False)""",
        })

    self.__ifname = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_ifname(self):
    self.__ifname = YANGDynClass(base=unicode, is_leaf=True, yang_name="ifname", rest_name="ifname", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, is_keyval=True, namespace='urn:brocade.com:mgmt:brocade-sysdiag-operational', defining_module='brocade-sysdiag-operational', yang_type='string', is_config=False)


  def _get_gos_stats(self):
    """
    Getter method for gos_stats, mapped from YANG variable /cpu_interface_state/gos_stats (container)
    """
    return self.__gos_stats
      
  def _set_gos_stats(self, v, load=False):
    """
    Setter method for gos_stats, mapped from YANG variable /cpu_interface_state/gos_stats (container)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_gos_stats is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_gos_stats() directly.
    """
    if hasattr(v, "_utype"):
      v = v._utype(v)
    try:
      t = YANGDynClass(v,base=gos_stats.gos_stats, is_container='container', yang_name="gos-stats", rest_name="gos-stats", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'callpoint': u'sysdiag-stats-gos-stats-1'}}, namespace='urn:brocade.com:mgmt:brocade-sysdiag-operational', defining_module='brocade-sysdiag-operational', yang_type='container', is_config=False)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """gos_stats must be of a type compatible with container""",
          'defined-type': "container",
          'generated-type': """YANGDynClass(base=gos_stats.gos_stats, is_container='container', yang_name="gos-stats", rest_name="gos-stats", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'callpoint': u'sysdiag-stats-gos-stats-1'}}, namespace='urn:brocade.com:mgmt:brocade-sysdiag-operational', defining_module='brocade-sysdiag-operational', yang_type='container', is_config=False)""",
        })

    self.__gos_stats = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_gos_stats(self):
    self.__gos_stats = YANGDynClass(base=gos_stats.gos_stats, is_container='container', yang_name="gos-stats", rest_name="gos-stats", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'callpoint': u'sysdiag-stats-gos-stats-1'}}, namespace='urn:brocade.com:mgmt:brocade-sysdiag-operational', defining_module='brocade-sysdiag-operational', yang_type='container', is_config=False)


  def _get_host_stats(self):
    """
    Getter method for host_stats, mapped from YANG variable /cpu_interface_state/host_stats (container)
    """
    return self.__host_stats
      
  def _set_host_stats(self, v, load=False):
    """
    Setter method for host_stats, mapped from YANG variable /cpu_interface_state/host_stats (container)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_host_stats is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_host_stats() directly.
    """
    if hasattr(v, "_utype"):
      v = v._utype(v)
    try:
      t = YANGDynClass(v,base=host_stats.host_stats, is_container='container', yang_name="host-stats", rest_name="host-stats", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'callpoint': u'sysdiag-stats-host-stats-1'}}, namespace='urn:brocade.com:mgmt:brocade-sysdiag-operational', defining_module='brocade-sysdiag-operational', yang_type='container', is_config=False)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """host_stats must be of a type compatible with container""",
          'defined-type': "container",
          'generated-type': """YANGDynClass(base=host_stats.host_stats, is_container='container', yang_name="host-stats", rest_name="host-stats", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'callpoint': u'sysdiag-stats-host-stats-1'}}, namespace='urn:brocade.com:mgmt:brocade-sysdiag-operational', defining_module='brocade-sysdiag-operational', yang_type='container', is_config=False)""",
        })

    self.__host_stats = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_host_stats(self):
    self.__host_stats = YANGDynClass(base=host_stats.host_stats, is_container='container', yang_name="host-stats", rest_name="host-stats", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'callpoint': u'sysdiag-stats-host-stats-1'}}, namespace='urn:brocade.com:mgmt:brocade-sysdiag-operational', defining_module='brocade-sysdiag-operational', yang_type='container', is_config=False)

  ifname = __builtin__.property(_get_ifname)
  gos_stats = __builtin__.property(_get_gos_stats)
  host_stats = __builtin__.property(_get_host_stats)


  _pyangbind_elements = {'ifname': ifname, 'gos_stats': gos_stats, 'host_stats': host_stats, }


