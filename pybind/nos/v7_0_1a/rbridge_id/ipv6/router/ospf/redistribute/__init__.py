
from operator import attrgetter
import pyangbind.lib.xpathhelper as xpathhelper
from pyangbind.lib.yangtypes import RestrictedPrecisionDecimalType, RestrictedClassType, TypedListType
from pyangbind.lib.yangtypes import YANGBool, YANGListType, YANGDynClass, ReferenceType
from pyangbind.lib.base import PybindBase
from decimal import Decimal
from bitarray import bitarray
import __builtin__
import redistribute_connected
import redistribute_static
import redistribute_bgp
import redistribute_ospf
class redistribute(PybindBase):
  """
  This class was auto-generated by the PythonClass plugin for PYANG
  from YANG module brocade-rbridge - based on the path /rbridge-id/ipv6/router/ospf/redistribute. Each member element of
  the container is represented as a class variable - with a specific
  YANG type.

  YANG Description: Enable route redistribution
  """
  __slots__ = ('_pybind_generated_by', '_path_helper', '_yang_name', '_rest_name', '_extmethods', '__redistribute_connected','__redistribute_static','__redistribute_bgp','__redistribute_ospf',)

  _yang_name = 'redistribute'
  _rest_name = 'redistribute'

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
    self.__redistribute_connected = YANGDynClass(base=redistribute_connected.redistribute_connected, is_container='container', yang_name="redistribute-connected", rest_name="connected", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'info': u'Connected routes', u'alt-name': u'connected'}}, namespace='urn:brocade.com:mgmt:brocade-ospfv3', defining_module='brocade-ospfv3', yang_type='container', is_config=True)
    self.__redistribute_bgp = YANGDynClass(base=redistribute_bgp.redistribute_bgp, is_container='container', yang_name="redistribute-bgp", rest_name="bgp", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'info': u'BGP routes', u'alt-name': u'bgp'}}, namespace='urn:brocade.com:mgmt:brocade-ospfv3', defining_module='brocade-ospfv3', yang_type='container', is_config=True)
    self.__redistribute_ospf = YANGDynClass(base=redistribute_ospf.redistribute_ospf, is_container='container', yang_name="redistribute-ospf", rest_name="ospf", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'info': u'OSPF routes', u'alt-name': u'ospf'}}, namespace='urn:brocade.com:mgmt:brocade-ospfv3', defining_module='brocade-ospfv3', yang_type='container', is_config=True)
    self.__redistribute_static = YANGDynClass(base=redistribute_static.redistribute_static, is_container='container', yang_name="redistribute-static", rest_name="static", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'info': u'Static routes', u'alt-name': u'static'}}, namespace='urn:brocade.com:mgmt:brocade-ospfv3', defining_module='brocade-ospfv3', yang_type='container', is_config=True)

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
      return [u'rbridge-id', u'ipv6', u'router', u'ospf', u'redistribute']

  def _rest_path(self):
    if hasattr(self, "_parent"):
      if self._rest_name:
        return self._parent._rest_path()+[self._rest_name]
      else:
        return self._parent._rest_path()
    else:
      return [u'rbridge-id', u'ipv6', u'router', u'ospf', u'redistribute']

  def _get_redistribute_connected(self):
    """
    Getter method for redistribute_connected, mapped from YANG variable /rbridge_id/ipv6/router/ospf/redistribute/redistribute_connected (container)

    YANG Description: Connected routes
    """
    return self.__redistribute_connected
      
  def _set_redistribute_connected(self, v, load=False):
    """
    Setter method for redistribute_connected, mapped from YANG variable /rbridge_id/ipv6/router/ospf/redistribute/redistribute_connected (container)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_redistribute_connected is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_redistribute_connected() directly.

    YANG Description: Connected routes
    """
    if hasattr(v, "_utype"):
      v = v._utype(v)
    try:
      t = YANGDynClass(v,base=redistribute_connected.redistribute_connected, is_container='container', yang_name="redistribute-connected", rest_name="connected", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'info': u'Connected routes', u'alt-name': u'connected'}}, namespace='urn:brocade.com:mgmt:brocade-ospfv3', defining_module='brocade-ospfv3', yang_type='container', is_config=True)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """redistribute_connected must be of a type compatible with container""",
          'defined-type': "container",
          'generated-type': """YANGDynClass(base=redistribute_connected.redistribute_connected, is_container='container', yang_name="redistribute-connected", rest_name="connected", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'info': u'Connected routes', u'alt-name': u'connected'}}, namespace='urn:brocade.com:mgmt:brocade-ospfv3', defining_module='brocade-ospfv3', yang_type='container', is_config=True)""",
        })

    self.__redistribute_connected = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_redistribute_connected(self):
    self.__redistribute_connected = YANGDynClass(base=redistribute_connected.redistribute_connected, is_container='container', yang_name="redistribute-connected", rest_name="connected", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'info': u'Connected routes', u'alt-name': u'connected'}}, namespace='urn:brocade.com:mgmt:brocade-ospfv3', defining_module='brocade-ospfv3', yang_type='container', is_config=True)


  def _get_redistribute_static(self):
    """
    Getter method for redistribute_static, mapped from YANG variable /rbridge_id/ipv6/router/ospf/redistribute/redistribute_static (container)

    YANG Description: Static routes
    """
    return self.__redistribute_static
      
  def _set_redistribute_static(self, v, load=False):
    """
    Setter method for redistribute_static, mapped from YANG variable /rbridge_id/ipv6/router/ospf/redistribute/redistribute_static (container)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_redistribute_static is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_redistribute_static() directly.

    YANG Description: Static routes
    """
    if hasattr(v, "_utype"):
      v = v._utype(v)
    try:
      t = YANGDynClass(v,base=redistribute_static.redistribute_static, is_container='container', yang_name="redistribute-static", rest_name="static", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'info': u'Static routes', u'alt-name': u'static'}}, namespace='urn:brocade.com:mgmt:brocade-ospfv3', defining_module='brocade-ospfv3', yang_type='container', is_config=True)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """redistribute_static must be of a type compatible with container""",
          'defined-type': "container",
          'generated-type': """YANGDynClass(base=redistribute_static.redistribute_static, is_container='container', yang_name="redistribute-static", rest_name="static", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'info': u'Static routes', u'alt-name': u'static'}}, namespace='urn:brocade.com:mgmt:brocade-ospfv3', defining_module='brocade-ospfv3', yang_type='container', is_config=True)""",
        })

    self.__redistribute_static = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_redistribute_static(self):
    self.__redistribute_static = YANGDynClass(base=redistribute_static.redistribute_static, is_container='container', yang_name="redistribute-static", rest_name="static", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'info': u'Static routes', u'alt-name': u'static'}}, namespace='urn:brocade.com:mgmt:brocade-ospfv3', defining_module='brocade-ospfv3', yang_type='container', is_config=True)


  def _get_redistribute_bgp(self):
    """
    Getter method for redistribute_bgp, mapped from YANG variable /rbridge_id/ipv6/router/ospf/redistribute/redistribute_bgp (container)

    YANG Description: BGP routes
    """
    return self.__redistribute_bgp
      
  def _set_redistribute_bgp(self, v, load=False):
    """
    Setter method for redistribute_bgp, mapped from YANG variable /rbridge_id/ipv6/router/ospf/redistribute/redistribute_bgp (container)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_redistribute_bgp is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_redistribute_bgp() directly.

    YANG Description: BGP routes
    """
    if hasattr(v, "_utype"):
      v = v._utype(v)
    try:
      t = YANGDynClass(v,base=redistribute_bgp.redistribute_bgp, is_container='container', yang_name="redistribute-bgp", rest_name="bgp", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'info': u'BGP routes', u'alt-name': u'bgp'}}, namespace='urn:brocade.com:mgmt:brocade-ospfv3', defining_module='brocade-ospfv3', yang_type='container', is_config=True)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """redistribute_bgp must be of a type compatible with container""",
          'defined-type': "container",
          'generated-type': """YANGDynClass(base=redistribute_bgp.redistribute_bgp, is_container='container', yang_name="redistribute-bgp", rest_name="bgp", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'info': u'BGP routes', u'alt-name': u'bgp'}}, namespace='urn:brocade.com:mgmt:brocade-ospfv3', defining_module='brocade-ospfv3', yang_type='container', is_config=True)""",
        })

    self.__redistribute_bgp = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_redistribute_bgp(self):
    self.__redistribute_bgp = YANGDynClass(base=redistribute_bgp.redistribute_bgp, is_container='container', yang_name="redistribute-bgp", rest_name="bgp", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'info': u'BGP routes', u'alt-name': u'bgp'}}, namespace='urn:brocade.com:mgmt:brocade-ospfv3', defining_module='brocade-ospfv3', yang_type='container', is_config=True)


  def _get_redistribute_ospf(self):
    """
    Getter method for redistribute_ospf, mapped from YANG variable /rbridge_id/ipv6/router/ospf/redistribute/redistribute_ospf (container)

    YANG Description: OSPF routes
    """
    return self.__redistribute_ospf
      
  def _set_redistribute_ospf(self, v, load=False):
    """
    Setter method for redistribute_ospf, mapped from YANG variable /rbridge_id/ipv6/router/ospf/redistribute/redistribute_ospf (container)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_redistribute_ospf is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_redistribute_ospf() directly.

    YANG Description: OSPF routes
    """
    if hasattr(v, "_utype"):
      v = v._utype(v)
    try:
      t = YANGDynClass(v,base=redistribute_ospf.redistribute_ospf, is_container='container', yang_name="redistribute-ospf", rest_name="ospf", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'info': u'OSPF routes', u'alt-name': u'ospf'}}, namespace='urn:brocade.com:mgmt:brocade-ospfv3', defining_module='brocade-ospfv3', yang_type='container', is_config=True)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """redistribute_ospf must be of a type compatible with container""",
          'defined-type': "container",
          'generated-type': """YANGDynClass(base=redistribute_ospf.redistribute_ospf, is_container='container', yang_name="redistribute-ospf", rest_name="ospf", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'info': u'OSPF routes', u'alt-name': u'ospf'}}, namespace='urn:brocade.com:mgmt:brocade-ospfv3', defining_module='brocade-ospfv3', yang_type='container', is_config=True)""",
        })

    self.__redistribute_ospf = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_redistribute_ospf(self):
    self.__redistribute_ospf = YANGDynClass(base=redistribute_ospf.redistribute_ospf, is_container='container', yang_name="redistribute-ospf", rest_name="ospf", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'info': u'OSPF routes', u'alt-name': u'ospf'}}, namespace='urn:brocade.com:mgmt:brocade-ospfv3', defining_module='brocade-ospfv3', yang_type='container', is_config=True)

  redistribute_connected = __builtin__.property(_get_redistribute_connected, _set_redistribute_connected)
  redistribute_static = __builtin__.property(_get_redistribute_static, _set_redistribute_static)
  redistribute_bgp = __builtin__.property(_get_redistribute_bgp, _set_redistribute_bgp)
  redistribute_ospf = __builtin__.property(_get_redistribute_ospf, _set_redistribute_ospf)


  _pyangbind_elements = {'redistribute_connected': redistribute_connected, 'redistribute_static': redistribute_static, 'redistribute_bgp': redistribute_bgp, 'redistribute_ospf': redistribute_ospf, }


