
from operator import attrgetter
import pyangbind.lib.xpathhelper as xpathhelper
from pyangbind.lib.yangtypes import RestrictedPrecisionDecimalType, RestrictedClassType, TypedListType
from pyangbind.lib.yangtypes import YANGBool, YANGListType, YANGDynClass, ReferenceType
from pyangbind.lib.base import PybindBase
from decimal import Decimal
from bitarray import bitarray
import __builtin__
import interval
class bfd(PybindBase):
  """
  This class was auto-generated by the PythonClass plugin for PYANG
  from YANG module brocade-rbridge - based on the path /rbridge-id/router/router-bgp/router-bgp-attributes/neighbor/neighbor-ips/neighbor-addr/bfd. Each member element of
  the container is represented as a class variable - with a specific
  YANG type.
  """
  __slots__ = ('_pybind_generated_by', '_path_helper', '_yang_name', '_rest_name', '_extmethods', '__bfd_enable','__holdover_interval','__interval',)

  _yang_name = 'bfd'
  _rest_name = 'bfd'

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
    self.__holdover_interval = YANGDynClass(base=RestrictedClassType(base_type=RestrictedClassType(base_type=long, restriction_dict={'range': ['0..4294967295']}, int_size=32), restriction_dict={'range': [u'1..30']}), is_leaf=True, yang_name="holdover-interval", rest_name="holdover-interval", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'cli-full-command': None, u'info': u'BFD holdover interval configuration'}}, namespace='urn:brocade.com:mgmt:brocade-bgp', defining_module='brocade-bgp', yang_type='bfd:bfd-holdover-interval', is_config=True)
    self.__interval = YANGDynClass(base=interval.interval, is_container='container', presence=False, yang_name="interval", rest_name="interval", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'info': u'Configure BFD desired min transmit interval in milliseconds.', u'cli-sequence-commands': None, u'cli-full-no': None, u'cli-incomplete-command': None}}, namespace='urn:brocade.com:mgmt:brocade-bgp', defining_module='brocade-bgp', yang_type='container', is_config=True)
    self.__bfd_enable = YANGDynClass(base=YANGBool, is_leaf=True, yang_name="bfd-enable", rest_name="bfd-enable", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'cli-full-command': None, u'cli-drop-node-name': None}}, namespace='urn:brocade.com:mgmt:brocade-bgp', defining_module='brocade-bgp', yang_type='empty', is_config=True)

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
      return [u'rbridge-id', u'router', u'router-bgp', u'router-bgp-attributes', u'neighbor', u'neighbor-ips', u'neighbor-addr', u'bfd']

  def _rest_path(self):
    if hasattr(self, "_parent"):
      if self._rest_name:
        return self._parent._rest_path()+[self._rest_name]
      else:
        return self._parent._rest_path()
    else:
      return [u'rbridge-id', u'router', u'bgp', u'neighbor', u'neighbor-addr', u'bfd']

  def _get_bfd_enable(self):
    """
    Getter method for bfd_enable, mapped from YANG variable /rbridge_id/router/router_bgp/router_bgp_attributes/neighbor/neighbor_ips/neighbor_addr/bfd/bfd_enable (empty)
    """
    return self.__bfd_enable
      
  def _set_bfd_enable(self, v, load=False):
    """
    Setter method for bfd_enable, mapped from YANG variable /rbridge_id/router/router_bgp/router_bgp_attributes/neighbor/neighbor_ips/neighbor_addr/bfd/bfd_enable (empty)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_bfd_enable is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_bfd_enable() directly.
    """
    if hasattr(v, "_utype"):
      v = v._utype(v)
    try:
      t = YANGDynClass(v,base=YANGBool, is_leaf=True, yang_name="bfd-enable", rest_name="bfd-enable", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'cli-full-command': None, u'cli-drop-node-name': None}}, namespace='urn:brocade.com:mgmt:brocade-bgp', defining_module='brocade-bgp', yang_type='empty', is_config=True)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """bfd_enable must be of a type compatible with empty""",
          'defined-type': "empty",
          'generated-type': """YANGDynClass(base=YANGBool, is_leaf=True, yang_name="bfd-enable", rest_name="bfd-enable", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'cli-full-command': None, u'cli-drop-node-name': None}}, namespace='urn:brocade.com:mgmt:brocade-bgp', defining_module='brocade-bgp', yang_type='empty', is_config=True)""",
        })

    self.__bfd_enable = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_bfd_enable(self):
    self.__bfd_enable = YANGDynClass(base=YANGBool, is_leaf=True, yang_name="bfd-enable", rest_name="bfd-enable", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'cli-full-command': None, u'cli-drop-node-name': None}}, namespace='urn:brocade.com:mgmt:brocade-bgp', defining_module='brocade-bgp', yang_type='empty', is_config=True)


  def _get_holdover_interval(self):
    """
    Getter method for holdover_interval, mapped from YANG variable /rbridge_id/router/router_bgp/router_bgp_attributes/neighbor/neighbor_ips/neighbor_addr/bfd/holdover_interval (bfd:bfd-holdover-interval)
    """
    return self.__holdover_interval
      
  def _set_holdover_interval(self, v, load=False):
    """
    Setter method for holdover_interval, mapped from YANG variable /rbridge_id/router/router_bgp/router_bgp_attributes/neighbor/neighbor_ips/neighbor_addr/bfd/holdover_interval (bfd:bfd-holdover-interval)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_holdover_interval is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_holdover_interval() directly.
    """
    if hasattr(v, "_utype"):
      v = v._utype(v)
    try:
      t = YANGDynClass(v,base=RestrictedClassType(base_type=RestrictedClassType(base_type=long, restriction_dict={'range': ['0..4294967295']}, int_size=32), restriction_dict={'range': [u'1..30']}), is_leaf=True, yang_name="holdover-interval", rest_name="holdover-interval", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'cli-full-command': None, u'info': u'BFD holdover interval configuration'}}, namespace='urn:brocade.com:mgmt:brocade-bgp', defining_module='brocade-bgp', yang_type='bfd:bfd-holdover-interval', is_config=True)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """holdover_interval must be of a type compatible with bfd:bfd-holdover-interval""",
          'defined-type': "bfd:bfd-holdover-interval",
          'generated-type': """YANGDynClass(base=RestrictedClassType(base_type=RestrictedClassType(base_type=long, restriction_dict={'range': ['0..4294967295']}, int_size=32), restriction_dict={'range': [u'1..30']}), is_leaf=True, yang_name="holdover-interval", rest_name="holdover-interval", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'cli-full-command': None, u'info': u'BFD holdover interval configuration'}}, namespace='urn:brocade.com:mgmt:brocade-bgp', defining_module='brocade-bgp', yang_type='bfd:bfd-holdover-interval', is_config=True)""",
        })

    self.__holdover_interval = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_holdover_interval(self):
    self.__holdover_interval = YANGDynClass(base=RestrictedClassType(base_type=RestrictedClassType(base_type=long, restriction_dict={'range': ['0..4294967295']}, int_size=32), restriction_dict={'range': [u'1..30']}), is_leaf=True, yang_name="holdover-interval", rest_name="holdover-interval", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'cli-full-command': None, u'info': u'BFD holdover interval configuration'}}, namespace='urn:brocade.com:mgmt:brocade-bgp', defining_module='brocade-bgp', yang_type='bfd:bfd-holdover-interval', is_config=True)


  def _get_interval(self):
    """
    Getter method for interval, mapped from YANG variable /rbridge_id/router/router_bgp/router_bgp_attributes/neighbor/neighbor_ips/neighbor_addr/bfd/interval (container)

    YANG Description: Configure BFD desired min transmit interval in milliseconds.
    """
    return self.__interval
      
  def _set_interval(self, v, load=False):
    """
    Setter method for interval, mapped from YANG variable /rbridge_id/router/router_bgp/router_bgp_attributes/neighbor/neighbor_ips/neighbor_addr/bfd/interval (container)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_interval is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_interval() directly.

    YANG Description: Configure BFD desired min transmit interval in milliseconds.
    """
    if hasattr(v, "_utype"):
      v = v._utype(v)
    try:
      t = YANGDynClass(v,base=interval.interval, is_container='container', presence=False, yang_name="interval", rest_name="interval", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'info': u'Configure BFD desired min transmit interval in milliseconds.', u'cli-sequence-commands': None, u'cli-full-no': None, u'cli-incomplete-command': None}}, namespace='urn:brocade.com:mgmt:brocade-bgp', defining_module='brocade-bgp', yang_type='container', is_config=True)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """interval must be of a type compatible with container""",
          'defined-type': "container",
          'generated-type': """YANGDynClass(base=interval.interval, is_container='container', presence=False, yang_name="interval", rest_name="interval", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'info': u'Configure BFD desired min transmit interval in milliseconds.', u'cli-sequence-commands': None, u'cli-full-no': None, u'cli-incomplete-command': None}}, namespace='urn:brocade.com:mgmt:brocade-bgp', defining_module='brocade-bgp', yang_type='container', is_config=True)""",
        })

    self.__interval = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_interval(self):
    self.__interval = YANGDynClass(base=interval.interval, is_container='container', presence=False, yang_name="interval", rest_name="interval", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'info': u'Configure BFD desired min transmit interval in milliseconds.', u'cli-sequence-commands': None, u'cli-full-no': None, u'cli-incomplete-command': None}}, namespace='urn:brocade.com:mgmt:brocade-bgp', defining_module='brocade-bgp', yang_type='container', is_config=True)

  bfd_enable = __builtin__.property(_get_bfd_enable, _set_bfd_enable)
  holdover_interval = __builtin__.property(_get_holdover_interval, _set_holdover_interval)
  interval = __builtin__.property(_get_interval, _set_interval)


  _pyangbind_elements = {'bfd_enable': bfd_enable, 'holdover_interval': holdover_interval, 'interval': interval, }


