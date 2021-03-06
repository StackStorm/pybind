
from operator import attrgetter
import pyangbind.lib.xpathhelper as xpathhelper
from pyangbind.lib.yangtypes import RestrictedPrecisionDecimalType, RestrictedClassType, TypedListType
from pyangbind.lib.yangtypes import YANGBool, YANGListType, YANGDynClass, ReferenceType
from pyangbind.lib.base import PybindBase
from decimal import Decimal
from bitarray import bitarray
import __builtin__
class vxlan(PybindBase):
  """
  This class was auto-generated by the PythonClass plugin for PYANG
  from YANG module brocade-system-capabilities - based on the path /capabilities/overlay/vxlan. Each member element of
  the container is represented as a class variable - with a specific
  YANG type.
  """
  __slots__ = ('_pybind_generated_by', '_path_helper', '_yang_name', '_rest_name', '_extmethods', '__hardware_vtep','__vtep_ip_ve','__vxlan_tunnel_bfd','__vxlan_tunnel_mac_learn_protocol_bgp',)

  _yang_name = 'vxlan'
  _rest_name = 'vxlan'

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
    self.__vxlan_tunnel_mac_learn_protocol_bgp = YANGDynClass(base=YANGBool, is_leaf=True, yang_name="vxlan-tunnel-mac-learn-protocol-bgp", rest_name="vxlan-tunnel-mac-learn-protocol-bgp", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='urn:brocade.com:mgmt:brocade-system-capabilities', defining_module='brocade-system-capabilities', yang_type='boolean', is_config=False)
    self.__vxlan_tunnel_bfd = YANGDynClass(base=YANGBool, is_leaf=True, yang_name="vxlan-tunnel-bfd", rest_name="vxlan-tunnel-bfd", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='urn:brocade.com:mgmt:brocade-system-capabilities', defining_module='brocade-system-capabilities', yang_type='boolean', is_config=False)
    self.__vtep_ip_ve = YANGDynClass(base=YANGBool, is_leaf=True, yang_name="vtep-ip-ve", rest_name="vtep-ip-ve", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='urn:brocade.com:mgmt:brocade-system-capabilities', defining_module='brocade-system-capabilities', yang_type='boolean', is_config=False)
    self.__hardware_vtep = YANGDynClass(base=YANGBool, is_leaf=True, yang_name="hardware-vtep", rest_name="hardware-vtep", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='urn:brocade.com:mgmt:brocade-system-capabilities', defining_module='brocade-system-capabilities', yang_type='boolean', is_config=False)

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
      return [u'capabilities', u'overlay', u'vxlan']

  def _rest_path(self):
    if hasattr(self, "_parent"):
      if self._rest_name:
        return self._parent._rest_path()+[self._rest_name]
      else:
        return self._parent._rest_path()
    else:
      return [u'capabilities', u'overlay', u'vxlan']

  def _get_hardware_vtep(self):
    """
    Getter method for hardware_vtep, mapped from YANG variable /capabilities/overlay/vxlan/hardware_vtep (boolean)
    """
    return self.__hardware_vtep
      
  def _set_hardware_vtep(self, v, load=False):
    """
    Setter method for hardware_vtep, mapped from YANG variable /capabilities/overlay/vxlan/hardware_vtep (boolean)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_hardware_vtep is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_hardware_vtep() directly.
    """
    if hasattr(v, "_utype"):
      v = v._utype(v)
    try:
      t = YANGDynClass(v,base=YANGBool, is_leaf=True, yang_name="hardware-vtep", rest_name="hardware-vtep", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='urn:brocade.com:mgmt:brocade-system-capabilities', defining_module='brocade-system-capabilities', yang_type='boolean', is_config=False)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """hardware_vtep must be of a type compatible with boolean""",
          'defined-type': "boolean",
          'generated-type': """YANGDynClass(base=YANGBool, is_leaf=True, yang_name="hardware-vtep", rest_name="hardware-vtep", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='urn:brocade.com:mgmt:brocade-system-capabilities', defining_module='brocade-system-capabilities', yang_type='boolean', is_config=False)""",
        })

    self.__hardware_vtep = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_hardware_vtep(self):
    self.__hardware_vtep = YANGDynClass(base=YANGBool, is_leaf=True, yang_name="hardware-vtep", rest_name="hardware-vtep", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='urn:brocade.com:mgmt:brocade-system-capabilities', defining_module='brocade-system-capabilities', yang_type='boolean', is_config=False)


  def _get_vtep_ip_ve(self):
    """
    Getter method for vtep_ip_ve, mapped from YANG variable /capabilities/overlay/vxlan/vtep_ip_ve (boolean)
    """
    return self.__vtep_ip_ve
      
  def _set_vtep_ip_ve(self, v, load=False):
    """
    Setter method for vtep_ip_ve, mapped from YANG variable /capabilities/overlay/vxlan/vtep_ip_ve (boolean)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_vtep_ip_ve is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_vtep_ip_ve() directly.
    """
    if hasattr(v, "_utype"):
      v = v._utype(v)
    try:
      t = YANGDynClass(v,base=YANGBool, is_leaf=True, yang_name="vtep-ip-ve", rest_name="vtep-ip-ve", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='urn:brocade.com:mgmt:brocade-system-capabilities', defining_module='brocade-system-capabilities', yang_type='boolean', is_config=False)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """vtep_ip_ve must be of a type compatible with boolean""",
          'defined-type': "boolean",
          'generated-type': """YANGDynClass(base=YANGBool, is_leaf=True, yang_name="vtep-ip-ve", rest_name="vtep-ip-ve", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='urn:brocade.com:mgmt:brocade-system-capabilities', defining_module='brocade-system-capabilities', yang_type='boolean', is_config=False)""",
        })

    self.__vtep_ip_ve = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_vtep_ip_ve(self):
    self.__vtep_ip_ve = YANGDynClass(base=YANGBool, is_leaf=True, yang_name="vtep-ip-ve", rest_name="vtep-ip-ve", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='urn:brocade.com:mgmt:brocade-system-capabilities', defining_module='brocade-system-capabilities', yang_type='boolean', is_config=False)


  def _get_vxlan_tunnel_bfd(self):
    """
    Getter method for vxlan_tunnel_bfd, mapped from YANG variable /capabilities/overlay/vxlan/vxlan_tunnel_bfd (boolean)
    """
    return self.__vxlan_tunnel_bfd
      
  def _set_vxlan_tunnel_bfd(self, v, load=False):
    """
    Setter method for vxlan_tunnel_bfd, mapped from YANG variable /capabilities/overlay/vxlan/vxlan_tunnel_bfd (boolean)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_vxlan_tunnel_bfd is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_vxlan_tunnel_bfd() directly.
    """
    if hasattr(v, "_utype"):
      v = v._utype(v)
    try:
      t = YANGDynClass(v,base=YANGBool, is_leaf=True, yang_name="vxlan-tunnel-bfd", rest_name="vxlan-tunnel-bfd", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='urn:brocade.com:mgmt:brocade-system-capabilities', defining_module='brocade-system-capabilities', yang_type='boolean', is_config=False)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """vxlan_tunnel_bfd must be of a type compatible with boolean""",
          'defined-type': "boolean",
          'generated-type': """YANGDynClass(base=YANGBool, is_leaf=True, yang_name="vxlan-tunnel-bfd", rest_name="vxlan-tunnel-bfd", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='urn:brocade.com:mgmt:brocade-system-capabilities', defining_module='brocade-system-capabilities', yang_type='boolean', is_config=False)""",
        })

    self.__vxlan_tunnel_bfd = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_vxlan_tunnel_bfd(self):
    self.__vxlan_tunnel_bfd = YANGDynClass(base=YANGBool, is_leaf=True, yang_name="vxlan-tunnel-bfd", rest_name="vxlan-tunnel-bfd", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='urn:brocade.com:mgmt:brocade-system-capabilities', defining_module='brocade-system-capabilities', yang_type='boolean', is_config=False)


  def _get_vxlan_tunnel_mac_learn_protocol_bgp(self):
    """
    Getter method for vxlan_tunnel_mac_learn_protocol_bgp, mapped from YANG variable /capabilities/overlay/vxlan/vxlan_tunnel_mac_learn_protocol_bgp (boolean)
    """
    return self.__vxlan_tunnel_mac_learn_protocol_bgp
      
  def _set_vxlan_tunnel_mac_learn_protocol_bgp(self, v, load=False):
    """
    Setter method for vxlan_tunnel_mac_learn_protocol_bgp, mapped from YANG variable /capabilities/overlay/vxlan/vxlan_tunnel_mac_learn_protocol_bgp (boolean)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_vxlan_tunnel_mac_learn_protocol_bgp is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_vxlan_tunnel_mac_learn_protocol_bgp() directly.
    """
    if hasattr(v, "_utype"):
      v = v._utype(v)
    try:
      t = YANGDynClass(v,base=YANGBool, is_leaf=True, yang_name="vxlan-tunnel-mac-learn-protocol-bgp", rest_name="vxlan-tunnel-mac-learn-protocol-bgp", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='urn:brocade.com:mgmt:brocade-system-capabilities', defining_module='brocade-system-capabilities', yang_type='boolean', is_config=False)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """vxlan_tunnel_mac_learn_protocol_bgp must be of a type compatible with boolean""",
          'defined-type': "boolean",
          'generated-type': """YANGDynClass(base=YANGBool, is_leaf=True, yang_name="vxlan-tunnel-mac-learn-protocol-bgp", rest_name="vxlan-tunnel-mac-learn-protocol-bgp", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='urn:brocade.com:mgmt:brocade-system-capabilities', defining_module='brocade-system-capabilities', yang_type='boolean', is_config=False)""",
        })

    self.__vxlan_tunnel_mac_learn_protocol_bgp = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_vxlan_tunnel_mac_learn_protocol_bgp(self):
    self.__vxlan_tunnel_mac_learn_protocol_bgp = YANGDynClass(base=YANGBool, is_leaf=True, yang_name="vxlan-tunnel-mac-learn-protocol-bgp", rest_name="vxlan-tunnel-mac-learn-protocol-bgp", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='urn:brocade.com:mgmt:brocade-system-capabilities', defining_module='brocade-system-capabilities', yang_type='boolean', is_config=False)

  hardware_vtep = __builtin__.property(_get_hardware_vtep)
  vtep_ip_ve = __builtin__.property(_get_vtep_ip_ve)
  vxlan_tunnel_bfd = __builtin__.property(_get_vxlan_tunnel_bfd)
  vxlan_tunnel_mac_learn_protocol_bgp = __builtin__.property(_get_vxlan_tunnel_mac_learn_protocol_bgp)


  _pyangbind_elements = {'hardware_vtep': hardware_vtep, 'vtep_ip_ve': vtep_ip_ve, 'vxlan_tunnel_bfd': vxlan_tunnel_bfd, 'vxlan_tunnel_mac_learn_protocol_bgp': vxlan_tunnel_mac_learn_protocol_bgp, }


