
from operator import attrgetter
import pyangbind.lib.xpathhelper as xpathhelper
from pyangbind.lib.yangtypes import RestrictedPrecisionDecimalType, RestrictedClassType, TypedListType
from pyangbind.lib.yangtypes import YANGBool, YANGListType, YANGDynClass, ReferenceType
from pyangbind.lib.base import PybindBase
from decimal import Decimal
from bitarray import bitarray
import __builtin__
import both
import export
import import_
class route_target(PybindBase):
  """
  This class was auto-generated by the PythonClass plugin for PYANG
  from YANG module brocade-common-def - based on the path /routing-system/evpn-config/evpn/evpn-instance/route-target. Each member element of
  the container is represented as a class variable - with a specific
  YANG type.
  """
  __slots__ = ('_pybind_generated_by', '_path_helper', '_yang_name', '_rest_name', '_extmethods', '__both','__export','__import_',)

  _yang_name = 'route-target'
  _rest_name = 'route-target'

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
    self.__both = YANGDynClass(base=YANGListType("target_community",both.both, yang_name="both", rest_name="both", parent=self, is_container='list', user_ordered=False, path_helper=self._path_helper, yang_keys='target-community', extensions={u'tailf-common': {u'info': u'Configure Target VPN Extended Communities', u'cli-suppress-mode': None, u'callpoint': u'EvpnRTConfigBoth', u'cli-full-no': None}}), is_container='list', yang_name="both", rest_name="both", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'info': u'Configure Target VPN Extended Communities', u'cli-suppress-mode': None, u'callpoint': u'EvpnRTConfigBoth', u'cli-full-no': None}}, namespace='urn:brocade.com:mgmt:brocade-bgp', defining_module='brocade-bgp', yang_type='list', is_config=True)
    self.__export = YANGDynClass(base=YANGListType("target_community",export.export, yang_name="export", rest_name="export", parent=self, is_container='list', user_ordered=False, path_helper=self._path_helper, yang_keys='target-community', extensions={u'tailf-common': {u'cli-full-command': None, u'info': u'Configure Target VPN Extended Communities', u'cli-suppress-mode': None, u'callpoint': u'EvpnRTConfigExport', u'cli-full-no': None}}), is_container='list', yang_name="export", rest_name="export", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'cli-full-command': None, u'info': u'Configure Target VPN Extended Communities', u'cli-suppress-mode': None, u'callpoint': u'EvpnRTConfigExport', u'cli-full-no': None}}, namespace='urn:brocade.com:mgmt:brocade-bgp', defining_module='brocade-bgp', yang_type='list', is_config=True)
    self.__import_ = YANGDynClass(base=YANGListType("target_community",import_.import_, yang_name="import", rest_name="import", parent=self, is_container='list', user_ordered=False, path_helper=self._path_helper, yang_keys='target-community', extensions={u'tailf-common': {u'info': u'Configure Target VPN Extended Communities', u'cli-suppress-mode': None, u'callpoint': u'EvpnRTConfigImport', u'cli-full-no': None}}), is_container='list', yang_name="import", rest_name="import", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'info': u'Configure Target VPN Extended Communities', u'cli-suppress-mode': None, u'callpoint': u'EvpnRTConfigImport', u'cli-full-no': None}}, namespace='urn:brocade.com:mgmt:brocade-bgp', defining_module='brocade-bgp', yang_type='list', is_config=True)

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
      return [u'routing-system', u'evpn-config', u'evpn', u'evpn-instance', u'route-target']

  def _rest_path(self):
    if hasattr(self, "_parent"):
      if self._rest_name:
        return self._parent._rest_path()+[self._rest_name]
      else:
        return self._parent._rest_path()
    else:
      return [u'evpn', u'evpn-instance', u'route-target']

  def _get_both(self):
    """
    Getter method for both, mapped from YANG variable /routing_system/evpn_config/evpn/evpn_instance/route_target/both (list)
    """
    return self.__both
      
  def _set_both(self, v, load=False):
    """
    Setter method for both, mapped from YANG variable /routing_system/evpn_config/evpn/evpn_instance/route_target/both (list)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_both is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_both() directly.
    """
    if hasattr(v, "_utype"):
      v = v._utype(v)
    try:
      t = YANGDynClass(v,base=YANGListType("target_community",both.both, yang_name="both", rest_name="both", parent=self, is_container='list', user_ordered=False, path_helper=self._path_helper, yang_keys='target-community', extensions={u'tailf-common': {u'info': u'Configure Target VPN Extended Communities', u'cli-suppress-mode': None, u'callpoint': u'EvpnRTConfigBoth', u'cli-full-no': None}}), is_container='list', yang_name="both", rest_name="both", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'info': u'Configure Target VPN Extended Communities', u'cli-suppress-mode': None, u'callpoint': u'EvpnRTConfigBoth', u'cli-full-no': None}}, namespace='urn:brocade.com:mgmt:brocade-bgp', defining_module='brocade-bgp', yang_type='list', is_config=True)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """both must be of a type compatible with list""",
          'defined-type': "list",
          'generated-type': """YANGDynClass(base=YANGListType("target_community",both.both, yang_name="both", rest_name="both", parent=self, is_container='list', user_ordered=False, path_helper=self._path_helper, yang_keys='target-community', extensions={u'tailf-common': {u'info': u'Configure Target VPN Extended Communities', u'cli-suppress-mode': None, u'callpoint': u'EvpnRTConfigBoth', u'cli-full-no': None}}), is_container='list', yang_name="both", rest_name="both", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'info': u'Configure Target VPN Extended Communities', u'cli-suppress-mode': None, u'callpoint': u'EvpnRTConfigBoth', u'cli-full-no': None}}, namespace='urn:brocade.com:mgmt:brocade-bgp', defining_module='brocade-bgp', yang_type='list', is_config=True)""",
        })

    self.__both = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_both(self):
    self.__both = YANGDynClass(base=YANGListType("target_community",both.both, yang_name="both", rest_name="both", parent=self, is_container='list', user_ordered=False, path_helper=self._path_helper, yang_keys='target-community', extensions={u'tailf-common': {u'info': u'Configure Target VPN Extended Communities', u'cli-suppress-mode': None, u'callpoint': u'EvpnRTConfigBoth', u'cli-full-no': None}}), is_container='list', yang_name="both", rest_name="both", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'info': u'Configure Target VPN Extended Communities', u'cli-suppress-mode': None, u'callpoint': u'EvpnRTConfigBoth', u'cli-full-no': None}}, namespace='urn:brocade.com:mgmt:brocade-bgp', defining_module='brocade-bgp', yang_type='list', is_config=True)


  def _get_export(self):
    """
    Getter method for export, mapped from YANG variable /routing_system/evpn_config/evpn/evpn_instance/route_target/export (list)
    """
    return self.__export
      
  def _set_export(self, v, load=False):
    """
    Setter method for export, mapped from YANG variable /routing_system/evpn_config/evpn/evpn_instance/route_target/export (list)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_export is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_export() directly.
    """
    if hasattr(v, "_utype"):
      v = v._utype(v)
    try:
      t = YANGDynClass(v,base=YANGListType("target_community",export.export, yang_name="export", rest_name="export", parent=self, is_container='list', user_ordered=False, path_helper=self._path_helper, yang_keys='target-community', extensions={u'tailf-common': {u'cli-full-command': None, u'info': u'Configure Target VPN Extended Communities', u'cli-suppress-mode': None, u'callpoint': u'EvpnRTConfigExport', u'cli-full-no': None}}), is_container='list', yang_name="export", rest_name="export", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'cli-full-command': None, u'info': u'Configure Target VPN Extended Communities', u'cli-suppress-mode': None, u'callpoint': u'EvpnRTConfigExport', u'cli-full-no': None}}, namespace='urn:brocade.com:mgmt:brocade-bgp', defining_module='brocade-bgp', yang_type='list', is_config=True)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """export must be of a type compatible with list""",
          'defined-type': "list",
          'generated-type': """YANGDynClass(base=YANGListType("target_community",export.export, yang_name="export", rest_name="export", parent=self, is_container='list', user_ordered=False, path_helper=self._path_helper, yang_keys='target-community', extensions={u'tailf-common': {u'cli-full-command': None, u'info': u'Configure Target VPN Extended Communities', u'cli-suppress-mode': None, u'callpoint': u'EvpnRTConfigExport', u'cli-full-no': None}}), is_container='list', yang_name="export", rest_name="export", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'cli-full-command': None, u'info': u'Configure Target VPN Extended Communities', u'cli-suppress-mode': None, u'callpoint': u'EvpnRTConfigExport', u'cli-full-no': None}}, namespace='urn:brocade.com:mgmt:brocade-bgp', defining_module='brocade-bgp', yang_type='list', is_config=True)""",
        })

    self.__export = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_export(self):
    self.__export = YANGDynClass(base=YANGListType("target_community",export.export, yang_name="export", rest_name="export", parent=self, is_container='list', user_ordered=False, path_helper=self._path_helper, yang_keys='target-community', extensions={u'tailf-common': {u'cli-full-command': None, u'info': u'Configure Target VPN Extended Communities', u'cli-suppress-mode': None, u'callpoint': u'EvpnRTConfigExport', u'cli-full-no': None}}), is_container='list', yang_name="export", rest_name="export", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'cli-full-command': None, u'info': u'Configure Target VPN Extended Communities', u'cli-suppress-mode': None, u'callpoint': u'EvpnRTConfigExport', u'cli-full-no': None}}, namespace='urn:brocade.com:mgmt:brocade-bgp', defining_module='brocade-bgp', yang_type='list', is_config=True)


  def _get_import_(self):
    """
    Getter method for import_, mapped from YANG variable /routing_system/evpn_config/evpn/evpn_instance/route_target/import (list)
    """
    return self.__import_
      
  def _set_import_(self, v, load=False):
    """
    Setter method for import_, mapped from YANG variable /routing_system/evpn_config/evpn/evpn_instance/route_target/import (list)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_import_ is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_import_() directly.
    """
    if hasattr(v, "_utype"):
      v = v._utype(v)
    try:
      t = YANGDynClass(v,base=YANGListType("target_community",import_.import_, yang_name="import", rest_name="import", parent=self, is_container='list', user_ordered=False, path_helper=self._path_helper, yang_keys='target-community', extensions={u'tailf-common': {u'info': u'Configure Target VPN Extended Communities', u'cli-suppress-mode': None, u'callpoint': u'EvpnRTConfigImport', u'cli-full-no': None}}), is_container='list', yang_name="import", rest_name="import", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'info': u'Configure Target VPN Extended Communities', u'cli-suppress-mode': None, u'callpoint': u'EvpnRTConfigImport', u'cli-full-no': None}}, namespace='urn:brocade.com:mgmt:brocade-bgp', defining_module='brocade-bgp', yang_type='list', is_config=True)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """import_ must be of a type compatible with list""",
          'defined-type': "list",
          'generated-type': """YANGDynClass(base=YANGListType("target_community",import_.import_, yang_name="import", rest_name="import", parent=self, is_container='list', user_ordered=False, path_helper=self._path_helper, yang_keys='target-community', extensions={u'tailf-common': {u'info': u'Configure Target VPN Extended Communities', u'cli-suppress-mode': None, u'callpoint': u'EvpnRTConfigImport', u'cli-full-no': None}}), is_container='list', yang_name="import", rest_name="import", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'info': u'Configure Target VPN Extended Communities', u'cli-suppress-mode': None, u'callpoint': u'EvpnRTConfigImport', u'cli-full-no': None}}, namespace='urn:brocade.com:mgmt:brocade-bgp', defining_module='brocade-bgp', yang_type='list', is_config=True)""",
        })

    self.__import_ = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_import_(self):
    self.__import_ = YANGDynClass(base=YANGListType("target_community",import_.import_, yang_name="import", rest_name="import", parent=self, is_container='list', user_ordered=False, path_helper=self._path_helper, yang_keys='target-community', extensions={u'tailf-common': {u'info': u'Configure Target VPN Extended Communities', u'cli-suppress-mode': None, u'callpoint': u'EvpnRTConfigImport', u'cli-full-no': None}}), is_container='list', yang_name="import", rest_name="import", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'info': u'Configure Target VPN Extended Communities', u'cli-suppress-mode': None, u'callpoint': u'EvpnRTConfigImport', u'cli-full-no': None}}, namespace='urn:brocade.com:mgmt:brocade-bgp', defining_module='brocade-bgp', yang_type='list', is_config=True)

  both = __builtin__.property(_get_both, _set_both)
  export = __builtin__.property(_get_export, _set_export)
  import_ = __builtin__.property(_get_import_, _set_import_)


  _pyangbind_elements = {'both': both, 'export': export, 'import_': import_, }

