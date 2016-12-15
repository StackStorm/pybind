
from operator import attrgetter
import pyangbind.lib.xpathhelper as xpathhelper
from pyangbind.lib.yangtypes import RestrictedPrecisionDecimalType, RestrictedClassType, TypedListType
from pyangbind.lib.yangtypes import YANGBool, YANGListType, YANGDynClass, ReferenceType
from pyangbind.lib.base import PybindBase
from decimal import Decimal
from bitarray import bitarray
import __builtin__
import dscp
import interface
import next_hop
import global_
import next_vrf
class ip(PybindBase):
  """
  This class was auto-generated by the PythonClass plugin for PYANG
  from YANG module brocade-common-def - based on the path /routing-system/route-map/content/set/ip. Each member element of
  the container is represented as a class variable - with a specific
  YANG type.

  YANG Description: Internet Protocol (IP).
  """
  __slots__ = ('_pybind_generated_by', '_path_helper', '_yang_name', '_rest_name', '_extmethods', '__dscp','__interface','__next_hop','__global_','__next_vrf',)

  _yang_name = 'ip'
  _rest_name = 'ip'

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
    self.__interface = YANGDynClass(base=interface.interface, is_container='container', yang_name="interface", rest_name="interface", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'info': u'Interface', u'cli-incomplete-no': None}}, namespace='urn:brocade.com:mgmt:brocade-ip-policy', defining_module='brocade-ip-policy', yang_type='container', is_config=True)
    self.__next_hop = YANGDynClass(base=next_hop.next_hop, is_container='container', yang_name="next-hop", rest_name="next-hop", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'info': u'Next hop address', u'cli-incomplete-no': None}}, namespace='urn:brocade.com:mgmt:brocade-ip-policy', defining_module='brocade-ip-policy', yang_type='container', is_config=True)
    self.__next_vrf = YANGDynClass(base=next_vrf.next_vrf, is_container='container', yang_name="next-vrf", rest_name="", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'cli-drop-node-name': None}}, namespace='urn:brocade.com:mgmt:brocade-ip-policy', defining_module='brocade-ip-policy', yang_type='container', is_config=True)
    self.__dscp = YANGDynClass(base=dscp.dscp, is_container='container', yang_name="dscp", rest_name="dscp", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'info': u'Dscp'}}, namespace='urn:brocade.com:mgmt:brocade-ip-policy', defining_module='brocade-ip-policy', yang_type='container', is_config=True)
    self.__global_ = YANGDynClass(base=global_.global_, is_container='container', yang_name="global", rest_name="global", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'info': u'Global'}}, namespace='urn:brocade.com:mgmt:brocade-ip-policy', defining_module='brocade-ip-policy', yang_type='container', is_config=True)

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
      return [u'routing-system', u'route-map', u'content', u'set', u'ip']

  def _rest_path(self):
    if hasattr(self, "_parent"):
      if self._rest_name:
        return self._parent._rest_path()+[self._rest_name]
      else:
        return self._parent._rest_path()
    else:
      return [u'route-map', u'set', u'ip']

  def _get_dscp(self):
    """
    Getter method for dscp, mapped from YANG variable /routing_system/route_map/content/set/ip/dscp (container)

    YANG Description: Dscp
    """
    return self.__dscp
      
  def _set_dscp(self, v, load=False):
    """
    Setter method for dscp, mapped from YANG variable /routing_system/route_map/content/set/ip/dscp (container)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_dscp is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_dscp() directly.

    YANG Description: Dscp
    """
    if hasattr(v, "_utype"):
      v = v._utype(v)
    try:
      t = YANGDynClass(v,base=dscp.dscp, is_container='container', yang_name="dscp", rest_name="dscp", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'info': u'Dscp'}}, namespace='urn:brocade.com:mgmt:brocade-ip-policy', defining_module='brocade-ip-policy', yang_type='container', is_config=True)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """dscp must be of a type compatible with container""",
          'defined-type': "container",
          'generated-type': """YANGDynClass(base=dscp.dscp, is_container='container', yang_name="dscp", rest_name="dscp", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'info': u'Dscp'}}, namespace='urn:brocade.com:mgmt:brocade-ip-policy', defining_module='brocade-ip-policy', yang_type='container', is_config=True)""",
        })

    self.__dscp = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_dscp(self):
    self.__dscp = YANGDynClass(base=dscp.dscp, is_container='container', yang_name="dscp", rest_name="dscp", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'info': u'Dscp'}}, namespace='urn:brocade.com:mgmt:brocade-ip-policy', defining_module='brocade-ip-policy', yang_type='container', is_config=True)


  def _get_interface(self):
    """
    Getter method for interface, mapped from YANG variable /routing_system/route_map/content/set/ip/interface (container)

    YANG Description: Interface
    """
    return self.__interface
      
  def _set_interface(self, v, load=False):
    """
    Setter method for interface, mapped from YANG variable /routing_system/route_map/content/set/ip/interface (container)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_interface is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_interface() directly.

    YANG Description: Interface
    """
    if hasattr(v, "_utype"):
      v = v._utype(v)
    try:
      t = YANGDynClass(v,base=interface.interface, is_container='container', yang_name="interface", rest_name="interface", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'info': u'Interface', u'cli-incomplete-no': None}}, namespace='urn:brocade.com:mgmt:brocade-ip-policy', defining_module='brocade-ip-policy', yang_type='container', is_config=True)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """interface must be of a type compatible with container""",
          'defined-type': "container",
          'generated-type': """YANGDynClass(base=interface.interface, is_container='container', yang_name="interface", rest_name="interface", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'info': u'Interface', u'cli-incomplete-no': None}}, namespace='urn:brocade.com:mgmt:brocade-ip-policy', defining_module='brocade-ip-policy', yang_type='container', is_config=True)""",
        })

    self.__interface = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_interface(self):
    self.__interface = YANGDynClass(base=interface.interface, is_container='container', yang_name="interface", rest_name="interface", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'info': u'Interface', u'cli-incomplete-no': None}}, namespace='urn:brocade.com:mgmt:brocade-ip-policy', defining_module='brocade-ip-policy', yang_type='container', is_config=True)


  def _get_next_hop(self):
    """
    Getter method for next_hop, mapped from YANG variable /routing_system/route_map/content/set/ip/next_hop (container)

    YANG Description: Next hop address
    """
    return self.__next_hop
      
  def _set_next_hop(self, v, load=False):
    """
    Setter method for next_hop, mapped from YANG variable /routing_system/route_map/content/set/ip/next_hop (container)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_next_hop is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_next_hop() directly.

    YANG Description: Next hop address
    """
    if hasattr(v, "_utype"):
      v = v._utype(v)
    try:
      t = YANGDynClass(v,base=next_hop.next_hop, is_container='container', yang_name="next-hop", rest_name="next-hop", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'info': u'Next hop address', u'cli-incomplete-no': None}}, namespace='urn:brocade.com:mgmt:brocade-ip-policy', defining_module='brocade-ip-policy', yang_type='container', is_config=True)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """next_hop must be of a type compatible with container""",
          'defined-type': "container",
          'generated-type': """YANGDynClass(base=next_hop.next_hop, is_container='container', yang_name="next-hop", rest_name="next-hop", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'info': u'Next hop address', u'cli-incomplete-no': None}}, namespace='urn:brocade.com:mgmt:brocade-ip-policy', defining_module='brocade-ip-policy', yang_type='container', is_config=True)""",
        })

    self.__next_hop = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_next_hop(self):
    self.__next_hop = YANGDynClass(base=next_hop.next_hop, is_container='container', yang_name="next-hop", rest_name="next-hop", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'info': u'Next hop address', u'cli-incomplete-no': None}}, namespace='urn:brocade.com:mgmt:brocade-ip-policy', defining_module='brocade-ip-policy', yang_type='container', is_config=True)


  def _get_global_(self):
    """
    Getter method for global_, mapped from YANG variable /routing_system/route_map/content/set/ip/global (container)

    YANG Description: Global
    """
    return self.__global_
      
  def _set_global_(self, v, load=False):
    """
    Setter method for global_, mapped from YANG variable /routing_system/route_map/content/set/ip/global (container)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_global_ is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_global_() directly.

    YANG Description: Global
    """
    if hasattr(v, "_utype"):
      v = v._utype(v)
    try:
      t = YANGDynClass(v,base=global_.global_, is_container='container', yang_name="global", rest_name="global", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'info': u'Global'}}, namespace='urn:brocade.com:mgmt:brocade-ip-policy', defining_module='brocade-ip-policy', yang_type='container', is_config=True)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """global_ must be of a type compatible with container""",
          'defined-type': "container",
          'generated-type': """YANGDynClass(base=global_.global_, is_container='container', yang_name="global", rest_name="global", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'info': u'Global'}}, namespace='urn:brocade.com:mgmt:brocade-ip-policy', defining_module='brocade-ip-policy', yang_type='container', is_config=True)""",
        })

    self.__global_ = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_global_(self):
    self.__global_ = YANGDynClass(base=global_.global_, is_container='container', yang_name="global", rest_name="global", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'info': u'Global'}}, namespace='urn:brocade.com:mgmt:brocade-ip-policy', defining_module='brocade-ip-policy', yang_type='container', is_config=True)


  def _get_next_vrf(self):
    """
    Getter method for next_vrf, mapped from YANG variable /routing_system/route_map/content/set/ip/next_vrf (container)
    """
    return self.__next_vrf
      
  def _set_next_vrf(self, v, load=False):
    """
    Setter method for next_vrf, mapped from YANG variable /routing_system/route_map/content/set/ip/next_vrf (container)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_next_vrf is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_next_vrf() directly.
    """
    if hasattr(v, "_utype"):
      v = v._utype(v)
    try:
      t = YANGDynClass(v,base=next_vrf.next_vrf, is_container='container', yang_name="next-vrf", rest_name="", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'cli-drop-node-name': None}}, namespace='urn:brocade.com:mgmt:brocade-ip-policy', defining_module='brocade-ip-policy', yang_type='container', is_config=True)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """next_vrf must be of a type compatible with container""",
          'defined-type': "container",
          'generated-type': """YANGDynClass(base=next_vrf.next_vrf, is_container='container', yang_name="next-vrf", rest_name="", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'cli-drop-node-name': None}}, namespace='urn:brocade.com:mgmt:brocade-ip-policy', defining_module='brocade-ip-policy', yang_type='container', is_config=True)""",
        })

    self.__next_vrf = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_next_vrf(self):
    self.__next_vrf = YANGDynClass(base=next_vrf.next_vrf, is_container='container', yang_name="next-vrf", rest_name="", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'cli-drop-node-name': None}}, namespace='urn:brocade.com:mgmt:brocade-ip-policy', defining_module='brocade-ip-policy', yang_type='container', is_config=True)

  dscp = __builtin__.property(_get_dscp, _set_dscp)
  interface = __builtin__.property(_get_interface, _set_interface)
  next_hop = __builtin__.property(_get_next_hop, _set_next_hop)
  global_ = __builtin__.property(_get_global_, _set_global_)
  next_vrf = __builtin__.property(_get_next_vrf, _set_next_vrf)


  _pyangbind_elements = {'dscp': dscp, 'interface': interface, 'next_hop': next_hop, 'global_': global_, 'next_vrf': next_vrf, }


