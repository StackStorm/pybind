
from operator import attrgetter
import pyangbind.lib.xpathhelper as xpathhelper
from pyangbind.lib.yangtypes import RestrictedPrecisionDecimalType, RestrictedClassType, TypedListType
from pyangbind.lib.yangtypes import YANGBool, YANGListType, YANGDynClass, ReferenceType
from pyangbind.lib.base import PybindBase
from decimal import Decimal
from bitarray import bitarray
import __builtin__
import static_route_nh
import static_route_nh_vrf
import static_route_oif_vrf
import static_route_oif
import static
class route(PybindBase):
  """
  This class was auto-generated by the PythonClass plugin for PYANG
  from YANG module brocade-vrf - based on the path /vrf/address-family/ip/unicast/ip/route. Each member element of
  the container is represented as a class variable - with a specific
  YANG type.
  """
  __slots__ = ('_pybind_generated_by', '_path_helper', '_yang_name', '_rest_name', '_extmethods', '__static_route_nh','__static_route_nh_vrf','__static_route_oif_vrf','__static_route_oif','__static',)

  _yang_name = 'route'
  _rest_name = 'route'

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
    self.__static_route_oif_vrf = YANGDynClass(base=YANGListType("static_route_next_vrf_dest next_hop_vrf static_route_oif_type static_route_oif_name",static_route_oif_vrf.static_route_oif_vrf, yang_name="static-route-oif-vrf", rest_name="", parent=self, is_container='list', user_ordered=False, path_helper=self._path_helper, yang_keys='static-route-next-vrf-dest next-hop-vrf static-route-oif-type static-route-oif-name', extensions={u'tailf-common': {u'info': u'Route with nexthop IP address', u'cli-no-key-completion': None, u'cli-suppress-mode': None, u'cli-suppress-list-no': None, u'cli-full-no': None, u'cli-drop-node-name': None, u'callpoint': u'Ipv4StaticRouteInterfaceNexthopVrf'}}), is_container='list', yang_name="static-route-oif-vrf", rest_name="", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'info': u'Route with nexthop IP address', u'cli-no-key-completion': None, u'cli-suppress-mode': None, u'cli-suppress-list-no': None, u'cli-full-no': None, u'cli-drop-node-name': None, u'callpoint': u'Ipv4StaticRouteInterfaceNexthopVrf'}}, namespace='urn:brocade.com:mgmt:brocade-rtm', defining_module='brocade-rtm', yang_type='list', is_config=True)
    self.__static_route_nh_vrf = YANGDynClass(base=YANGListType("static_route_next_vrf_dest next_hop_vrf static_route_next_hop",static_route_nh_vrf.static_route_nh_vrf, yang_name="static-route-nh-vrf", rest_name="", parent=self, is_container='list', user_ordered=False, path_helper=self._path_helper, yang_keys='static-route-next-vrf-dest next-hop-vrf static-route-next-hop', extensions={u'tailf-common': {u'info': u'Route with nexthop IP address', u'cli-no-key-completion': None, u'cli-suppress-mode': None, u'cli-suppress-list-no': None, u'cli-full-no': None, u'cli-drop-node-name': None, u'callpoint': u'rtm-static-route-next-hop-vrf'}}), is_container='list', yang_name="static-route-nh-vrf", rest_name="", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'info': u'Route with nexthop IP address', u'cli-no-key-completion': None, u'cli-suppress-mode': None, u'cli-suppress-list-no': None, u'cli-full-no': None, u'cli-drop-node-name': None, u'callpoint': u'rtm-static-route-next-hop-vrf'}}, namespace='urn:brocade.com:mgmt:brocade-rtm', defining_module='brocade-rtm', yang_type='list', is_config=True)
    self.__static_route_oif = YANGDynClass(base=YANGListType("static_route_dest static_route_oif_type static_route_oif_name",static_route_oif.static_route_oif, yang_name="static-route-oif", rest_name="", parent=self, is_container='list', user_ordered=False, path_helper=self._path_helper, yang_keys='static-route-dest static-route-oif-type static-route-oif-name', extensions={u'tailf-common': {u'info': u'Route with egress interface', u'cli-no-key-completion': None, u'cli-suppress-mode': None, u'cli-suppress-list-no': None, u'cli-full-no': None, u'cli-drop-node-name': None, u'callpoint': u'rtm-if-static-route'}}), is_container='list', yang_name="static-route-oif", rest_name="", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'info': u'Route with egress interface', u'cli-no-key-completion': None, u'cli-suppress-mode': None, u'cli-suppress-list-no': None, u'cli-full-no': None, u'cli-drop-node-name': None, u'callpoint': u'rtm-if-static-route'}}, namespace='urn:brocade.com:mgmt:brocade-rtm', defining_module='brocade-rtm', yang_type='list', is_config=True)
    self.__static = YANGDynClass(base=static.static, is_container='container', presence=False, yang_name="static", rest_name="static", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'info': u'BFD static route', u'hidden': u'full'}}, namespace='urn:brocade.com:mgmt:brocade-rtm', defining_module='brocade-rtm', yang_type='container', is_config=True)
    self.__static_route_nh = YANGDynClass(base=YANGListType("static_route_dest static_route_next_hop",static_route_nh.static_route_nh, yang_name="static-route-nh", rest_name="", parent=self, is_container='list', user_ordered=False, path_helper=self._path_helper, yang_keys='static-route-dest static-route-next-hop', extensions={u'tailf-common': {u'info': u'Route with nexthop IP address', u'cli-no-key-completion': None, u'cli-suppress-mode': None, u'cli-suppress-list-no': None, u'cli-full-no': None, u'cli-drop-node-name': None, u'callpoint': u'rtm-static-route'}}), is_container='list', yang_name="static-route-nh", rest_name="", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'info': u'Route with nexthop IP address', u'cli-no-key-completion': None, u'cli-suppress-mode': None, u'cli-suppress-list-no': None, u'cli-full-no': None, u'cli-drop-node-name': None, u'callpoint': u'rtm-static-route'}}, namespace='urn:brocade.com:mgmt:brocade-rtm', defining_module='brocade-rtm', yang_type='list', is_config=True)

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
      return [u'vrf', u'address-family', u'ip', u'unicast', u'ip', u'route']

  def _rest_path(self):
    if hasattr(self, "_parent"):
      if self._rest_name:
        return self._parent._rest_path()+[self._rest_name]
      else:
        return self._parent._rest_path()
    else:
      return [u'vrf', u'address-family', u'ipv4', u'unicast', u'ip', u'route']

  def _get_static_route_nh(self):
    """
    Getter method for static_route_nh, mapped from YANG variable /vrf/address_family/ip/unicast/ip/route/static_route_nh (list)
    """
    return self.__static_route_nh
      
  def _set_static_route_nh(self, v, load=False):
    """
    Setter method for static_route_nh, mapped from YANG variable /vrf/address_family/ip/unicast/ip/route/static_route_nh (list)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_static_route_nh is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_static_route_nh() directly.
    """
    if hasattr(v, "_utype"):
      v = v._utype(v)
    try:
      t = YANGDynClass(v,base=YANGListType("static_route_dest static_route_next_hop",static_route_nh.static_route_nh, yang_name="static-route-nh", rest_name="", parent=self, is_container='list', user_ordered=False, path_helper=self._path_helper, yang_keys='static-route-dest static-route-next-hop', extensions={u'tailf-common': {u'info': u'Route with nexthop IP address', u'cli-no-key-completion': None, u'cli-suppress-mode': None, u'cli-suppress-list-no': None, u'cli-full-no': None, u'cli-drop-node-name': None, u'callpoint': u'rtm-static-route'}}), is_container='list', yang_name="static-route-nh", rest_name="", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'info': u'Route with nexthop IP address', u'cli-no-key-completion': None, u'cli-suppress-mode': None, u'cli-suppress-list-no': None, u'cli-full-no': None, u'cli-drop-node-name': None, u'callpoint': u'rtm-static-route'}}, namespace='urn:brocade.com:mgmt:brocade-rtm', defining_module='brocade-rtm', yang_type='list', is_config=True)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """static_route_nh must be of a type compatible with list""",
          'defined-type': "list",
          'generated-type': """YANGDynClass(base=YANGListType("static_route_dest static_route_next_hop",static_route_nh.static_route_nh, yang_name="static-route-nh", rest_name="", parent=self, is_container='list', user_ordered=False, path_helper=self._path_helper, yang_keys='static-route-dest static-route-next-hop', extensions={u'tailf-common': {u'info': u'Route with nexthop IP address', u'cli-no-key-completion': None, u'cli-suppress-mode': None, u'cli-suppress-list-no': None, u'cli-full-no': None, u'cli-drop-node-name': None, u'callpoint': u'rtm-static-route'}}), is_container='list', yang_name="static-route-nh", rest_name="", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'info': u'Route with nexthop IP address', u'cli-no-key-completion': None, u'cli-suppress-mode': None, u'cli-suppress-list-no': None, u'cli-full-no': None, u'cli-drop-node-name': None, u'callpoint': u'rtm-static-route'}}, namespace='urn:brocade.com:mgmt:brocade-rtm', defining_module='brocade-rtm', yang_type='list', is_config=True)""",
        })

    self.__static_route_nh = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_static_route_nh(self):
    self.__static_route_nh = YANGDynClass(base=YANGListType("static_route_dest static_route_next_hop",static_route_nh.static_route_nh, yang_name="static-route-nh", rest_name="", parent=self, is_container='list', user_ordered=False, path_helper=self._path_helper, yang_keys='static-route-dest static-route-next-hop', extensions={u'tailf-common': {u'info': u'Route with nexthop IP address', u'cli-no-key-completion': None, u'cli-suppress-mode': None, u'cli-suppress-list-no': None, u'cli-full-no': None, u'cli-drop-node-name': None, u'callpoint': u'rtm-static-route'}}), is_container='list', yang_name="static-route-nh", rest_name="", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'info': u'Route with nexthop IP address', u'cli-no-key-completion': None, u'cli-suppress-mode': None, u'cli-suppress-list-no': None, u'cli-full-no': None, u'cli-drop-node-name': None, u'callpoint': u'rtm-static-route'}}, namespace='urn:brocade.com:mgmt:brocade-rtm', defining_module='brocade-rtm', yang_type='list', is_config=True)


  def _get_static_route_nh_vrf(self):
    """
    Getter method for static_route_nh_vrf, mapped from YANG variable /vrf/address_family/ip/unicast/ip/route/static_route_nh_vrf (list)
    """
    return self.__static_route_nh_vrf
      
  def _set_static_route_nh_vrf(self, v, load=False):
    """
    Setter method for static_route_nh_vrf, mapped from YANG variable /vrf/address_family/ip/unicast/ip/route/static_route_nh_vrf (list)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_static_route_nh_vrf is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_static_route_nh_vrf() directly.
    """
    if hasattr(v, "_utype"):
      v = v._utype(v)
    try:
      t = YANGDynClass(v,base=YANGListType("static_route_next_vrf_dest next_hop_vrf static_route_next_hop",static_route_nh_vrf.static_route_nh_vrf, yang_name="static-route-nh-vrf", rest_name="", parent=self, is_container='list', user_ordered=False, path_helper=self._path_helper, yang_keys='static-route-next-vrf-dest next-hop-vrf static-route-next-hop', extensions={u'tailf-common': {u'info': u'Route with nexthop IP address', u'cli-no-key-completion': None, u'cli-suppress-mode': None, u'cli-suppress-list-no': None, u'cli-full-no': None, u'cli-drop-node-name': None, u'callpoint': u'rtm-static-route-next-hop-vrf'}}), is_container='list', yang_name="static-route-nh-vrf", rest_name="", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'info': u'Route with nexthop IP address', u'cli-no-key-completion': None, u'cli-suppress-mode': None, u'cli-suppress-list-no': None, u'cli-full-no': None, u'cli-drop-node-name': None, u'callpoint': u'rtm-static-route-next-hop-vrf'}}, namespace='urn:brocade.com:mgmt:brocade-rtm', defining_module='brocade-rtm', yang_type='list', is_config=True)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """static_route_nh_vrf must be of a type compatible with list""",
          'defined-type': "list",
          'generated-type': """YANGDynClass(base=YANGListType("static_route_next_vrf_dest next_hop_vrf static_route_next_hop",static_route_nh_vrf.static_route_nh_vrf, yang_name="static-route-nh-vrf", rest_name="", parent=self, is_container='list', user_ordered=False, path_helper=self._path_helper, yang_keys='static-route-next-vrf-dest next-hop-vrf static-route-next-hop', extensions={u'tailf-common': {u'info': u'Route with nexthop IP address', u'cli-no-key-completion': None, u'cli-suppress-mode': None, u'cli-suppress-list-no': None, u'cli-full-no': None, u'cli-drop-node-name': None, u'callpoint': u'rtm-static-route-next-hop-vrf'}}), is_container='list', yang_name="static-route-nh-vrf", rest_name="", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'info': u'Route with nexthop IP address', u'cli-no-key-completion': None, u'cli-suppress-mode': None, u'cli-suppress-list-no': None, u'cli-full-no': None, u'cli-drop-node-name': None, u'callpoint': u'rtm-static-route-next-hop-vrf'}}, namespace='urn:brocade.com:mgmt:brocade-rtm', defining_module='brocade-rtm', yang_type='list', is_config=True)""",
        })

    self.__static_route_nh_vrf = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_static_route_nh_vrf(self):
    self.__static_route_nh_vrf = YANGDynClass(base=YANGListType("static_route_next_vrf_dest next_hop_vrf static_route_next_hop",static_route_nh_vrf.static_route_nh_vrf, yang_name="static-route-nh-vrf", rest_name="", parent=self, is_container='list', user_ordered=False, path_helper=self._path_helper, yang_keys='static-route-next-vrf-dest next-hop-vrf static-route-next-hop', extensions={u'tailf-common': {u'info': u'Route with nexthop IP address', u'cli-no-key-completion': None, u'cli-suppress-mode': None, u'cli-suppress-list-no': None, u'cli-full-no': None, u'cli-drop-node-name': None, u'callpoint': u'rtm-static-route-next-hop-vrf'}}), is_container='list', yang_name="static-route-nh-vrf", rest_name="", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'info': u'Route with nexthop IP address', u'cli-no-key-completion': None, u'cli-suppress-mode': None, u'cli-suppress-list-no': None, u'cli-full-no': None, u'cli-drop-node-name': None, u'callpoint': u'rtm-static-route-next-hop-vrf'}}, namespace='urn:brocade.com:mgmt:brocade-rtm', defining_module='brocade-rtm', yang_type='list', is_config=True)


  def _get_static_route_oif_vrf(self):
    """
    Getter method for static_route_oif_vrf, mapped from YANG variable /vrf/address_family/ip/unicast/ip/route/static_route_oif_vrf (list)
    """
    return self.__static_route_oif_vrf
      
  def _set_static_route_oif_vrf(self, v, load=False):
    """
    Setter method for static_route_oif_vrf, mapped from YANG variable /vrf/address_family/ip/unicast/ip/route/static_route_oif_vrf (list)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_static_route_oif_vrf is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_static_route_oif_vrf() directly.
    """
    if hasattr(v, "_utype"):
      v = v._utype(v)
    try:
      t = YANGDynClass(v,base=YANGListType("static_route_next_vrf_dest next_hop_vrf static_route_oif_type static_route_oif_name",static_route_oif_vrf.static_route_oif_vrf, yang_name="static-route-oif-vrf", rest_name="", parent=self, is_container='list', user_ordered=False, path_helper=self._path_helper, yang_keys='static-route-next-vrf-dest next-hop-vrf static-route-oif-type static-route-oif-name', extensions={u'tailf-common': {u'info': u'Route with nexthop IP address', u'cli-no-key-completion': None, u'cli-suppress-mode': None, u'cli-suppress-list-no': None, u'cli-full-no': None, u'cli-drop-node-name': None, u'callpoint': u'Ipv4StaticRouteInterfaceNexthopVrf'}}), is_container='list', yang_name="static-route-oif-vrf", rest_name="", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'info': u'Route with nexthop IP address', u'cli-no-key-completion': None, u'cli-suppress-mode': None, u'cli-suppress-list-no': None, u'cli-full-no': None, u'cli-drop-node-name': None, u'callpoint': u'Ipv4StaticRouteInterfaceNexthopVrf'}}, namespace='urn:brocade.com:mgmt:brocade-rtm', defining_module='brocade-rtm', yang_type='list', is_config=True)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """static_route_oif_vrf must be of a type compatible with list""",
          'defined-type': "list",
          'generated-type': """YANGDynClass(base=YANGListType("static_route_next_vrf_dest next_hop_vrf static_route_oif_type static_route_oif_name",static_route_oif_vrf.static_route_oif_vrf, yang_name="static-route-oif-vrf", rest_name="", parent=self, is_container='list', user_ordered=False, path_helper=self._path_helper, yang_keys='static-route-next-vrf-dest next-hop-vrf static-route-oif-type static-route-oif-name', extensions={u'tailf-common': {u'info': u'Route with nexthop IP address', u'cli-no-key-completion': None, u'cli-suppress-mode': None, u'cli-suppress-list-no': None, u'cli-full-no': None, u'cli-drop-node-name': None, u'callpoint': u'Ipv4StaticRouteInterfaceNexthopVrf'}}), is_container='list', yang_name="static-route-oif-vrf", rest_name="", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'info': u'Route with nexthop IP address', u'cli-no-key-completion': None, u'cli-suppress-mode': None, u'cli-suppress-list-no': None, u'cli-full-no': None, u'cli-drop-node-name': None, u'callpoint': u'Ipv4StaticRouteInterfaceNexthopVrf'}}, namespace='urn:brocade.com:mgmt:brocade-rtm', defining_module='brocade-rtm', yang_type='list', is_config=True)""",
        })

    self.__static_route_oif_vrf = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_static_route_oif_vrf(self):
    self.__static_route_oif_vrf = YANGDynClass(base=YANGListType("static_route_next_vrf_dest next_hop_vrf static_route_oif_type static_route_oif_name",static_route_oif_vrf.static_route_oif_vrf, yang_name="static-route-oif-vrf", rest_name="", parent=self, is_container='list', user_ordered=False, path_helper=self._path_helper, yang_keys='static-route-next-vrf-dest next-hop-vrf static-route-oif-type static-route-oif-name', extensions={u'tailf-common': {u'info': u'Route with nexthop IP address', u'cli-no-key-completion': None, u'cli-suppress-mode': None, u'cli-suppress-list-no': None, u'cli-full-no': None, u'cli-drop-node-name': None, u'callpoint': u'Ipv4StaticRouteInterfaceNexthopVrf'}}), is_container='list', yang_name="static-route-oif-vrf", rest_name="", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'info': u'Route with nexthop IP address', u'cli-no-key-completion': None, u'cli-suppress-mode': None, u'cli-suppress-list-no': None, u'cli-full-no': None, u'cli-drop-node-name': None, u'callpoint': u'Ipv4StaticRouteInterfaceNexthopVrf'}}, namespace='urn:brocade.com:mgmt:brocade-rtm', defining_module='brocade-rtm', yang_type='list', is_config=True)


  def _get_static_route_oif(self):
    """
    Getter method for static_route_oif, mapped from YANG variable /vrf/address_family/ip/unicast/ip/route/static_route_oif (list)
    """
    return self.__static_route_oif
      
  def _set_static_route_oif(self, v, load=False):
    """
    Setter method for static_route_oif, mapped from YANG variable /vrf/address_family/ip/unicast/ip/route/static_route_oif (list)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_static_route_oif is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_static_route_oif() directly.
    """
    if hasattr(v, "_utype"):
      v = v._utype(v)
    try:
      t = YANGDynClass(v,base=YANGListType("static_route_dest static_route_oif_type static_route_oif_name",static_route_oif.static_route_oif, yang_name="static-route-oif", rest_name="", parent=self, is_container='list', user_ordered=False, path_helper=self._path_helper, yang_keys='static-route-dest static-route-oif-type static-route-oif-name', extensions={u'tailf-common': {u'info': u'Route with egress interface', u'cli-no-key-completion': None, u'cli-suppress-mode': None, u'cli-suppress-list-no': None, u'cli-full-no': None, u'cli-drop-node-name': None, u'callpoint': u'rtm-if-static-route'}}), is_container='list', yang_name="static-route-oif", rest_name="", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'info': u'Route with egress interface', u'cli-no-key-completion': None, u'cli-suppress-mode': None, u'cli-suppress-list-no': None, u'cli-full-no': None, u'cli-drop-node-name': None, u'callpoint': u'rtm-if-static-route'}}, namespace='urn:brocade.com:mgmt:brocade-rtm', defining_module='brocade-rtm', yang_type='list', is_config=True)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """static_route_oif must be of a type compatible with list""",
          'defined-type': "list",
          'generated-type': """YANGDynClass(base=YANGListType("static_route_dest static_route_oif_type static_route_oif_name",static_route_oif.static_route_oif, yang_name="static-route-oif", rest_name="", parent=self, is_container='list', user_ordered=False, path_helper=self._path_helper, yang_keys='static-route-dest static-route-oif-type static-route-oif-name', extensions={u'tailf-common': {u'info': u'Route with egress interface', u'cli-no-key-completion': None, u'cli-suppress-mode': None, u'cli-suppress-list-no': None, u'cli-full-no': None, u'cli-drop-node-name': None, u'callpoint': u'rtm-if-static-route'}}), is_container='list', yang_name="static-route-oif", rest_name="", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'info': u'Route with egress interface', u'cli-no-key-completion': None, u'cli-suppress-mode': None, u'cli-suppress-list-no': None, u'cli-full-no': None, u'cli-drop-node-name': None, u'callpoint': u'rtm-if-static-route'}}, namespace='urn:brocade.com:mgmt:brocade-rtm', defining_module='brocade-rtm', yang_type='list', is_config=True)""",
        })

    self.__static_route_oif = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_static_route_oif(self):
    self.__static_route_oif = YANGDynClass(base=YANGListType("static_route_dest static_route_oif_type static_route_oif_name",static_route_oif.static_route_oif, yang_name="static-route-oif", rest_name="", parent=self, is_container='list', user_ordered=False, path_helper=self._path_helper, yang_keys='static-route-dest static-route-oif-type static-route-oif-name', extensions={u'tailf-common': {u'info': u'Route with egress interface', u'cli-no-key-completion': None, u'cli-suppress-mode': None, u'cli-suppress-list-no': None, u'cli-full-no': None, u'cli-drop-node-name': None, u'callpoint': u'rtm-if-static-route'}}), is_container='list', yang_name="static-route-oif", rest_name="", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'info': u'Route with egress interface', u'cli-no-key-completion': None, u'cli-suppress-mode': None, u'cli-suppress-list-no': None, u'cli-full-no': None, u'cli-drop-node-name': None, u'callpoint': u'rtm-if-static-route'}}, namespace='urn:brocade.com:mgmt:brocade-rtm', defining_module='brocade-rtm', yang_type='list', is_config=True)


  def _get_static(self):
    """
    Getter method for static, mapped from YANG variable /vrf/address_family/ip/unicast/ip/route/static (container)
    """
    return self.__static
      
  def _set_static(self, v, load=False):
    """
    Setter method for static, mapped from YANG variable /vrf/address_family/ip/unicast/ip/route/static (container)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_static is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_static() directly.
    """
    if hasattr(v, "_utype"):
      v = v._utype(v)
    try:
      t = YANGDynClass(v,base=static.static, is_container='container', presence=False, yang_name="static", rest_name="static", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'info': u'BFD static route', u'hidden': u'full'}}, namespace='urn:brocade.com:mgmt:brocade-rtm', defining_module='brocade-rtm', yang_type='container', is_config=True)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """static must be of a type compatible with container""",
          'defined-type': "container",
          'generated-type': """YANGDynClass(base=static.static, is_container='container', presence=False, yang_name="static", rest_name="static", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'info': u'BFD static route', u'hidden': u'full'}}, namespace='urn:brocade.com:mgmt:brocade-rtm', defining_module='brocade-rtm', yang_type='container', is_config=True)""",
        })

    self.__static = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_static(self):
    self.__static = YANGDynClass(base=static.static, is_container='container', presence=False, yang_name="static", rest_name="static", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'info': u'BFD static route', u'hidden': u'full'}}, namespace='urn:brocade.com:mgmt:brocade-rtm', defining_module='brocade-rtm', yang_type='container', is_config=True)

  static_route_nh = __builtin__.property(_get_static_route_nh, _set_static_route_nh)
  static_route_nh_vrf = __builtin__.property(_get_static_route_nh_vrf, _set_static_route_nh_vrf)
  static_route_oif_vrf = __builtin__.property(_get_static_route_oif_vrf, _set_static_route_oif_vrf)
  static_route_oif = __builtin__.property(_get_static_route_oif, _set_static_route_oif)
  static = __builtin__.property(_get_static, _set_static)


  _pyangbind_elements = {'static_route_nh': static_route_nh, 'static_route_nh_vrf': static_route_nh_vrf, 'static_route_oif_vrf': static_route_oif_vrf, 'static_route_oif': static_route_oif, 'static': static, }


