
from operator import attrgetter
import pyangbind.lib.xpathhelper as xpathhelper
from pyangbind.lib.yangtypes import RestrictedPrecisionDecimalType, RestrictedClassType, TypedListType
from pyangbind.lib.yangtypes import YANGBool, YANGListType, YANGDynClass, ReferenceType
from pyangbind.lib.base import PybindBase
from decimal import Decimal
from bitarray import bitarray
import __builtin__
import addpath_txrx
import addpath_advertise
class additional_paths(PybindBase):
  """
  This class was auto-generated by the PythonClass plugin for PYANG
  from YANG module brocade-common-def - based on the path /routing-system/router/router-bgp/address-family/ipv4/ipv4-unicast/af-vrf/neighbor/af-ipv4-vrf-neighbor-address-holder/af-ipv4-neighbor-addr/additional-paths. Each member element of
  the container is represented as a class variable - with a specific
  YANG type.
  """
  __slots__ = ('_pybind_generated_by', '_path_helper', '_yang_name', '_rest_name', '_extmethods', '__addpath_disable','__addpath_txrx','__addpath_advertise',)

  _yang_name = 'additional-paths'
  _rest_name = 'additional-paths'

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
    self.__addpath_txrx = YANGDynClass(base=addpath_txrx.addpath_txrx, is_container='container', presence=False, yang_name="addpath-txrx", rest_name="", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'cli-compact-syntax': None, u'cli-drop-node-name': None, u'cli-incomplete-command': None}}, namespace='urn:brocade.com:mgmt:brocade-bgp', defining_module='brocade-bgp', yang_type='container', is_config=True)
    self.__addpath_disable = YANGDynClass(base=YANGBool, is_leaf=True, yang_name="addpath-disable", rest_name="disable", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'info': u'disable additional paths capability', u'cli-full-command': None, u'alt-name': u'disable'}}, namespace='urn:brocade.com:mgmt:brocade-bgp', defining_module='brocade-bgp', yang_type='empty', is_config=True)
    self.__addpath_advertise = YANGDynClass(base=addpath_advertise.addpath_advertise, is_container='container', presence=False, yang_name="addpath-advertise", rest_name="advertise", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'info': u'Specify which routes should be advertised for additional path', u'cli-compact-syntax': None, u'alt-name': u'advertise', u'cli-incomplete-command': None}}, namespace='urn:brocade.com:mgmt:brocade-bgp', defining_module='brocade-bgp', yang_type='container', is_config=True)

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
      return [u'routing-system', u'router', u'router-bgp', u'address-family', u'ipv4', u'ipv4-unicast', u'af-vrf', u'neighbor', u'af-ipv4-vrf-neighbor-address-holder', u'af-ipv4-neighbor-addr', u'additional-paths']

  def _rest_path(self):
    if hasattr(self, "_parent"):
      if self._rest_name:
        return self._parent._rest_path()+[self._rest_name]
      else:
        return self._parent._rest_path()
    else:
      return [u'router', u'bgp', u'address-family', u'ipv4', u'unicast', u'vrf', u'neighbor', u'af-ipv4-neighbor-addr', u'additional-paths']

  def _get_addpath_disable(self):
    """
    Getter method for addpath_disable, mapped from YANG variable /routing_system/router/router_bgp/address_family/ipv4/ipv4_unicast/af_vrf/neighbor/af_ipv4_vrf_neighbor_address_holder/af_ipv4_neighbor_addr/additional_paths/addpath_disable (empty)
    """
    return self.__addpath_disable
      
  def _set_addpath_disable(self, v, load=False):
    """
    Setter method for addpath_disable, mapped from YANG variable /routing_system/router/router_bgp/address_family/ipv4/ipv4_unicast/af_vrf/neighbor/af_ipv4_vrf_neighbor_address_holder/af_ipv4_neighbor_addr/additional_paths/addpath_disable (empty)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_addpath_disable is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_addpath_disable() directly.
    """
    if hasattr(v, "_utype"):
      v = v._utype(v)
    try:
      t = YANGDynClass(v,base=YANGBool, is_leaf=True, yang_name="addpath-disable", rest_name="disable", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'info': u'disable additional paths capability', u'cli-full-command': None, u'alt-name': u'disable'}}, namespace='urn:brocade.com:mgmt:brocade-bgp', defining_module='brocade-bgp', yang_type='empty', is_config=True)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """addpath_disable must be of a type compatible with empty""",
          'defined-type': "empty",
          'generated-type': """YANGDynClass(base=YANGBool, is_leaf=True, yang_name="addpath-disable", rest_name="disable", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'info': u'disable additional paths capability', u'cli-full-command': None, u'alt-name': u'disable'}}, namespace='urn:brocade.com:mgmt:brocade-bgp', defining_module='brocade-bgp', yang_type='empty', is_config=True)""",
        })

    self.__addpath_disable = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_addpath_disable(self):
    self.__addpath_disable = YANGDynClass(base=YANGBool, is_leaf=True, yang_name="addpath-disable", rest_name="disable", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'info': u'disable additional paths capability', u'cli-full-command': None, u'alt-name': u'disable'}}, namespace='urn:brocade.com:mgmt:brocade-bgp', defining_module='brocade-bgp', yang_type='empty', is_config=True)


  def _get_addpath_txrx(self):
    """
    Getter method for addpath_txrx, mapped from YANG variable /routing_system/router/router_bgp/address_family/ipv4/ipv4_unicast/af_vrf/neighbor/af_ipv4_vrf_neighbor_address_holder/af_ipv4_neighbor_addr/additional_paths/addpath_txrx (container)
    """
    return self.__addpath_txrx
      
  def _set_addpath_txrx(self, v, load=False):
    """
    Setter method for addpath_txrx, mapped from YANG variable /routing_system/router/router_bgp/address_family/ipv4/ipv4_unicast/af_vrf/neighbor/af_ipv4_vrf_neighbor_address_holder/af_ipv4_neighbor_addr/additional_paths/addpath_txrx (container)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_addpath_txrx is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_addpath_txrx() directly.
    """
    if hasattr(v, "_utype"):
      v = v._utype(v)
    try:
      t = YANGDynClass(v,base=addpath_txrx.addpath_txrx, is_container='container', presence=False, yang_name="addpath-txrx", rest_name="", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'cli-compact-syntax': None, u'cli-drop-node-name': None, u'cli-incomplete-command': None}}, namespace='urn:brocade.com:mgmt:brocade-bgp', defining_module='brocade-bgp', yang_type='container', is_config=True)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """addpath_txrx must be of a type compatible with container""",
          'defined-type': "container",
          'generated-type': """YANGDynClass(base=addpath_txrx.addpath_txrx, is_container='container', presence=False, yang_name="addpath-txrx", rest_name="", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'cli-compact-syntax': None, u'cli-drop-node-name': None, u'cli-incomplete-command': None}}, namespace='urn:brocade.com:mgmt:brocade-bgp', defining_module='brocade-bgp', yang_type='container', is_config=True)""",
        })

    self.__addpath_txrx = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_addpath_txrx(self):
    self.__addpath_txrx = YANGDynClass(base=addpath_txrx.addpath_txrx, is_container='container', presence=False, yang_name="addpath-txrx", rest_name="", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'cli-compact-syntax': None, u'cli-drop-node-name': None, u'cli-incomplete-command': None}}, namespace='urn:brocade.com:mgmt:brocade-bgp', defining_module='brocade-bgp', yang_type='container', is_config=True)


  def _get_addpath_advertise(self):
    """
    Getter method for addpath_advertise, mapped from YANG variable /routing_system/router/router_bgp/address_family/ipv4/ipv4_unicast/af_vrf/neighbor/af_ipv4_vrf_neighbor_address_holder/af_ipv4_neighbor_addr/additional_paths/addpath_advertise (container)
    """
    return self.__addpath_advertise
      
  def _set_addpath_advertise(self, v, load=False):
    """
    Setter method for addpath_advertise, mapped from YANG variable /routing_system/router/router_bgp/address_family/ipv4/ipv4_unicast/af_vrf/neighbor/af_ipv4_vrf_neighbor_address_holder/af_ipv4_neighbor_addr/additional_paths/addpath_advertise (container)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_addpath_advertise is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_addpath_advertise() directly.
    """
    if hasattr(v, "_utype"):
      v = v._utype(v)
    try:
      t = YANGDynClass(v,base=addpath_advertise.addpath_advertise, is_container='container', presence=False, yang_name="addpath-advertise", rest_name="advertise", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'info': u'Specify which routes should be advertised for additional path', u'cli-compact-syntax': None, u'alt-name': u'advertise', u'cli-incomplete-command': None}}, namespace='urn:brocade.com:mgmt:brocade-bgp', defining_module='brocade-bgp', yang_type='container', is_config=True)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """addpath_advertise must be of a type compatible with container""",
          'defined-type': "container",
          'generated-type': """YANGDynClass(base=addpath_advertise.addpath_advertise, is_container='container', presence=False, yang_name="addpath-advertise", rest_name="advertise", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'info': u'Specify which routes should be advertised for additional path', u'cli-compact-syntax': None, u'alt-name': u'advertise', u'cli-incomplete-command': None}}, namespace='urn:brocade.com:mgmt:brocade-bgp', defining_module='brocade-bgp', yang_type='container', is_config=True)""",
        })

    self.__addpath_advertise = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_addpath_advertise(self):
    self.__addpath_advertise = YANGDynClass(base=addpath_advertise.addpath_advertise, is_container='container', presence=False, yang_name="addpath-advertise", rest_name="advertise", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'info': u'Specify which routes should be advertised for additional path', u'cli-compact-syntax': None, u'alt-name': u'advertise', u'cli-incomplete-command': None}}, namespace='urn:brocade.com:mgmt:brocade-bgp', defining_module='brocade-bgp', yang_type='container', is_config=True)

  addpath_disable = __builtin__.property(_get_addpath_disable, _set_addpath_disable)
  addpath_txrx = __builtin__.property(_get_addpath_txrx, _set_addpath_txrx)
  addpath_advertise = __builtin__.property(_get_addpath_advertise, _set_addpath_advertise)


  _pyangbind_elements = {'addpath_disable': addpath_disable, 'addpath_txrx': addpath_txrx, 'addpath_advertise': addpath_advertise, }


