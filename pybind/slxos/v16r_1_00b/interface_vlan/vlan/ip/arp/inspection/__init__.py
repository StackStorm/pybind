
from operator import attrgetter
import pyangbind.lib.xpathhelper as xpathhelper
from pyangbind.lib.yangtypes import RestrictedPrecisionDecimalType, RestrictedClassType, TypedListType
from pyangbind.lib.yangtypes import YANGBool, YANGListType, YANGDynClass, ReferenceType
from pyangbind.lib.base import PybindBase
from decimal import Decimal
from bitarray import bitarray
import __builtin__
import filter
import logging
class inspection(PybindBase):
  """
  This class was auto-generated by the PythonClass plugin for PYANG
  from YANG module brocade-interface - based on the path /interface-vlan/vlan/ip/arp/inspection. Each member element of
  the container is represented as a class variable - with a specific
  YANG type.
  """
  __slots__ = ('_pybind_generated_by', '_path_helper', '_yang_name', '_rest_name', '_extmethods', '__trust','__filter','__logging',)

  _yang_name = 'inspection'
  _rest_name = 'inspection'

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
    self.__filter = YANGDynClass(base=filter.filter, is_container='container', yang_name="filter", rest_name="filter", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'info': u'Configure Arp Inspection Filter'}}, namespace='urn:brocade.com:mgmt:brocade-dai', defining_module='brocade-dai', yang_type='container', is_config=True)
    self.__trust = YANGDynClass(base=YANGBool, is_leaf=True, yang_name="trust", rest_name="", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'info': u'Trusted Interface', u'cli-full-command': None, u'cli-drop-node-name': None}}, namespace='urn:brocade.com:mgmt:brocade-dai', defining_module='brocade-dai', yang_type='empty', is_config=True)
    self.__logging = YANGDynClass(base=logging.logging, is_container='container', yang_name="logging", rest_name="logging", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'info': u'Configure Arp Inspection Logging', u'cli-incomplete-no': None}}, namespace='urn:brocade.com:mgmt:brocade-dai', defining_module='brocade-dai', yang_type='container', is_config=True)

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
      return [u'interface-vlan', u'vlan', u'ip', u'arp', u'inspection']

  def _rest_path(self):
    if hasattr(self, "_parent"):
      if self._rest_name:
        return self._parent._rest_path()+[self._rest_name]
      else:
        return self._parent._rest_path()
    else:
      return [u'vlan', u'ip', u'arp', u'inspection']

  def _get_trust(self):
    """
    Getter method for trust, mapped from YANG variable /interface_vlan/vlan/ip/arp/inspection/trust (empty)
    """
    return self.__trust
      
  def _set_trust(self, v, load=False):
    """
    Setter method for trust, mapped from YANG variable /interface_vlan/vlan/ip/arp/inspection/trust (empty)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_trust is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_trust() directly.
    """
    if hasattr(v, "_utype"):
      v = v._utype(v)
    try:
      t = YANGDynClass(v,base=YANGBool, is_leaf=True, yang_name="trust", rest_name="", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'info': u'Trusted Interface', u'cli-full-command': None, u'cli-drop-node-name': None}}, namespace='urn:brocade.com:mgmt:brocade-dai', defining_module='brocade-dai', yang_type='empty', is_config=True)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """trust must be of a type compatible with empty""",
          'defined-type': "empty",
          'generated-type': """YANGDynClass(base=YANGBool, is_leaf=True, yang_name="trust", rest_name="", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'info': u'Trusted Interface', u'cli-full-command': None, u'cli-drop-node-name': None}}, namespace='urn:brocade.com:mgmt:brocade-dai', defining_module='brocade-dai', yang_type='empty', is_config=True)""",
        })

    self.__trust = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_trust(self):
    self.__trust = YANGDynClass(base=YANGBool, is_leaf=True, yang_name="trust", rest_name="", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'info': u'Trusted Interface', u'cli-full-command': None, u'cli-drop-node-name': None}}, namespace='urn:brocade.com:mgmt:brocade-dai', defining_module='brocade-dai', yang_type='empty', is_config=True)


  def _get_filter(self):
    """
    Getter method for filter, mapped from YANG variable /interface_vlan/vlan/ip/arp/inspection/filter (container)
    """
    return self.__filter
      
  def _set_filter(self, v, load=False):
    """
    Setter method for filter, mapped from YANG variable /interface_vlan/vlan/ip/arp/inspection/filter (container)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_filter is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_filter() directly.
    """
    if hasattr(v, "_utype"):
      v = v._utype(v)
    try:
      t = YANGDynClass(v,base=filter.filter, is_container='container', yang_name="filter", rest_name="filter", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'info': u'Configure Arp Inspection Filter'}}, namespace='urn:brocade.com:mgmt:brocade-dai', defining_module='brocade-dai', yang_type='container', is_config=True)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """filter must be of a type compatible with container""",
          'defined-type': "container",
          'generated-type': """YANGDynClass(base=filter.filter, is_container='container', yang_name="filter", rest_name="filter", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'info': u'Configure Arp Inspection Filter'}}, namespace='urn:brocade.com:mgmt:brocade-dai', defining_module='brocade-dai', yang_type='container', is_config=True)""",
        })

    self.__filter = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_filter(self):
    self.__filter = YANGDynClass(base=filter.filter, is_container='container', yang_name="filter", rest_name="filter", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'info': u'Configure Arp Inspection Filter'}}, namespace='urn:brocade.com:mgmt:brocade-dai', defining_module='brocade-dai', yang_type='container', is_config=True)


  def _get_logging(self):
    """
    Getter method for logging, mapped from YANG variable /interface_vlan/vlan/ip/arp/inspection/logging (container)
    """
    return self.__logging
      
  def _set_logging(self, v, load=False):
    """
    Setter method for logging, mapped from YANG variable /interface_vlan/vlan/ip/arp/inspection/logging (container)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_logging is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_logging() directly.
    """
    if hasattr(v, "_utype"):
      v = v._utype(v)
    try:
      t = YANGDynClass(v,base=logging.logging, is_container='container', yang_name="logging", rest_name="logging", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'info': u'Configure Arp Inspection Logging', u'cli-incomplete-no': None}}, namespace='urn:brocade.com:mgmt:brocade-dai', defining_module='brocade-dai', yang_type='container', is_config=True)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """logging must be of a type compatible with container""",
          'defined-type': "container",
          'generated-type': """YANGDynClass(base=logging.logging, is_container='container', yang_name="logging", rest_name="logging", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'info': u'Configure Arp Inspection Logging', u'cli-incomplete-no': None}}, namespace='urn:brocade.com:mgmt:brocade-dai', defining_module='brocade-dai', yang_type='container', is_config=True)""",
        })

    self.__logging = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_logging(self):
    self.__logging = YANGDynClass(base=logging.logging, is_container='container', yang_name="logging", rest_name="logging", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'info': u'Configure Arp Inspection Logging', u'cli-incomplete-no': None}}, namespace='urn:brocade.com:mgmt:brocade-dai', defining_module='brocade-dai', yang_type='container', is_config=True)

  trust = __builtin__.property(_get_trust, _set_trust)
  filter = __builtin__.property(_get_filter, _set_filter)
  logging = __builtin__.property(_get_logging, _set_logging)


  _pyangbind_elements = {'trust': trust, 'filter': filter, 'logging': logging, }


