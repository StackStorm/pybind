
from operator import attrgetter
import pyangbind.lib.xpathhelper as xpathhelper
from pyangbind.lib.yangtypes import RestrictedPrecisionDecimalType, RestrictedClassType, TypedListType
from pyangbind.lib.yangtypes import YANGBool, YANGListType, YANGDynClass, ReferenceType
from pyangbind.lib.base import PybindBase
from decimal import Decimal
from bitarray import bitarray
import __builtin__
class input(PybindBase):
  """
  This class was auto-generated by the PythonClass plugin for PYANG
  from YANG module brocade-mpls - based on the path /brocade_mpls_rpc/clear-mpls-statistics/input. Each member element of
  the container is represented as a class variable - with a specific
  YANG type.
  """
  __slots__ = ('_pybind_generated_by', '_path_helper', '_yang_name', '_rest_name', '_extmethods', '__mpls_clear_statistics_type','__mpls_clear_statistics_transit_ldp_fec_prefix','__mpls_clear_statistics_transit_ldp_prefix_address','__mpls_clear_statistics_transit_ldp_prefix_mask','__mpls_clear_statistics_transit_label_id','__mpls_clear_statistics_tunnel_ldp_id','__mpls_clear_statistics_tunnel_rsvp_bypass','__mpls_clear_statistics_tunnel_name','__mpls_clear_statistics_tunnel_dest',)

  _yang_name = 'input'
  _rest_name = 'input'

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
    self.__mpls_clear_statistics_tunnel_name = YANGDynClass(base=unicode, is_leaf=True, yang_name="mpls-clear-statistics-tunnel-name", rest_name="mpls-clear-statistics-tunnel-name", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=False, namespace='urn:brocade.com:mgmt:brocade-mpls', defining_module='brocade-mpls', yang_type='string', is_config=True)
    self.__mpls_clear_statistics_tunnel_ldp_id = YANGDynClass(base=RestrictedClassType(base_type=long, restriction_dict={'range': ['0..4294967295']}, int_size=32), is_leaf=True, yang_name="mpls-clear-statistics-tunnel-ldp-id", rest_name="mpls-clear-statistics-tunnel-ldp-id", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=False, namespace='urn:brocade.com:mgmt:brocade-mpls', defining_module='brocade-mpls', yang_type='uint32', is_config=True)
    self.__mpls_clear_statistics_type = YANGDynClass(base=RestrictedClassType(base_type=long, restriction_dict={'range': ['0..4294967295']}, int_size=32), is_leaf=True, yang_name="mpls-clear-statistics-type", rest_name="mpls-clear-statistics-type", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=False, namespace='urn:brocade.com:mgmt:brocade-mpls', defining_module='brocade-mpls', yang_type='uint32', is_config=True)
    self.__mpls_clear_statistics_transit_ldp_prefix_mask = YANGDynClass(base=RestrictedClassType(base_type=unicode, restriction_dict={'pattern': u'(([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])\\.){3}([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])(%[\\p{N}\\p{L}]+)?'}), is_leaf=True, yang_name="mpls-clear-statistics-transit-ldp-prefix-mask", rest_name="mpls-clear-statistics-transit-ldp-prefix-mask", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=False, namespace='urn:brocade.com:mgmt:brocade-mpls', defining_module='brocade-mpls', yang_type='mpls-ipv4-subnet-mask', is_config=True)
    self.__mpls_clear_statistics_tunnel_rsvp_bypass = YANGDynClass(base=RestrictedClassType(base_type=int, restriction_dict={'range': ['0..255']}, int_size=8), is_leaf=True, yang_name="mpls-clear-statistics-tunnel-rsvp-bypass", rest_name="mpls-clear-statistics-tunnel-rsvp-bypass", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=False, namespace='urn:brocade.com:mgmt:brocade-mpls', defining_module='brocade-mpls', yang_type='uint8', is_config=True)
    self.__mpls_clear_statistics_tunnel_dest = YANGDynClass(base=RestrictedClassType(base_type=unicode, restriction_dict={'pattern': u'(([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])\\.){3}([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])(%[\\p{N}\\p{L}]+)?'}), is_leaf=True, yang_name="mpls-clear-statistics-tunnel-dest", rest_name="mpls-clear-statistics-tunnel-dest", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=False, namespace='urn:brocade.com:mgmt:brocade-mpls', defining_module='brocade-mpls', yang_type='mpls-ipv4-address', is_config=True)
    self.__mpls_clear_statistics_transit_ldp_fec_prefix = YANGDynClass(base=RestrictedClassType(base_type=unicode, restriction_dict={'pattern': u'(([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])\\.){3}([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])/(([0-9])|([1-2][0-9])|(3[0-2]))'}), is_leaf=True, yang_name="mpls-clear-statistics-transit-ldp-fec-prefix", rest_name="mpls-clear-statistics-transit-ldp-fec-prefix", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=False, namespace='urn:brocade.com:mgmt:brocade-mpls', defining_module='brocade-mpls', yang_type='mpls-ipv4-prefix', is_config=True)
    self.__mpls_clear_statistics_transit_label_id = YANGDynClass(base=RestrictedClassType(base_type=long, restriction_dict={'range': ['0..4294967295']}, int_size=32), is_leaf=True, yang_name="mpls-clear-statistics-transit-label-id", rest_name="mpls-clear-statistics-transit-label-id", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=False, namespace='urn:brocade.com:mgmt:brocade-mpls', defining_module='brocade-mpls', yang_type='uint32', is_config=True)
    self.__mpls_clear_statistics_transit_ldp_prefix_address = YANGDynClass(base=RestrictedClassType(base_type=unicode, restriction_dict={'pattern': u'(([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])\\.){3}([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])(%[\\p{N}\\p{L}]+)?'}), is_leaf=True, yang_name="mpls-clear-statistics-transit-ldp-prefix-address", rest_name="mpls-clear-statistics-transit-ldp-prefix-address", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=False, namespace='urn:brocade.com:mgmt:brocade-mpls', defining_module='brocade-mpls', yang_type='mpls-ipv4-address', is_config=True)

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
      return [u'brocade_mpls_rpc', u'clear-mpls-statistics', u'input']

  def _rest_path(self):
    if hasattr(self, "_parent"):
      if self._rest_name:
        return self._parent._rest_path()+[self._rest_name]
      else:
        return self._parent._rest_path()
    else:
      return [u'clear-mpls-statistics', u'input']

  def _get_mpls_clear_statistics_type(self):
    """
    Getter method for mpls_clear_statistics_type, mapped from YANG variable /brocade_mpls_rpc/clear_mpls_statistics/input/mpls_clear_statistics_type (uint32)

    YANG Description: Tunnel ID to be cleared
    """
    return self.__mpls_clear_statistics_type
      
  def _set_mpls_clear_statistics_type(self, v, load=False):
    """
    Setter method for mpls_clear_statistics_type, mapped from YANG variable /brocade_mpls_rpc/clear_mpls_statistics/input/mpls_clear_statistics_type (uint32)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_mpls_clear_statistics_type is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_mpls_clear_statistics_type() directly.

    YANG Description: Tunnel ID to be cleared
    """
    if hasattr(v, "_utype"):
      v = v._utype(v)
    try:
      t = YANGDynClass(v,base=RestrictedClassType(base_type=long, restriction_dict={'range': ['0..4294967295']}, int_size=32), is_leaf=True, yang_name="mpls-clear-statistics-type", rest_name="mpls-clear-statistics-type", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=False, namespace='urn:brocade.com:mgmt:brocade-mpls', defining_module='brocade-mpls', yang_type='uint32', is_config=True)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """mpls_clear_statistics_type must be of a type compatible with uint32""",
          'defined-type': "uint32",
          'generated-type': """YANGDynClass(base=RestrictedClassType(base_type=long, restriction_dict={'range': ['0..4294967295']}, int_size=32), is_leaf=True, yang_name="mpls-clear-statistics-type", rest_name="mpls-clear-statistics-type", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=False, namespace='urn:brocade.com:mgmt:brocade-mpls', defining_module='brocade-mpls', yang_type='uint32', is_config=True)""",
        })

    self.__mpls_clear_statistics_type = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_mpls_clear_statistics_type(self):
    self.__mpls_clear_statistics_type = YANGDynClass(base=RestrictedClassType(base_type=long, restriction_dict={'range': ['0..4294967295']}, int_size=32), is_leaf=True, yang_name="mpls-clear-statistics-type", rest_name="mpls-clear-statistics-type", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=False, namespace='urn:brocade.com:mgmt:brocade-mpls', defining_module='brocade-mpls', yang_type='uint32', is_config=True)


  def _get_mpls_clear_statistics_transit_ldp_fec_prefix(self):
    """
    Getter method for mpls_clear_statistics_transit_ldp_fec_prefix, mapped from YANG variable /brocade_mpls_rpc/clear_mpls_statistics/input/mpls_clear_statistics_transit_ldp_fec_prefix (mpls-ipv4-prefix)

    YANG Description: Tunnel ID to be cleared
    """
    return self.__mpls_clear_statistics_transit_ldp_fec_prefix
      
  def _set_mpls_clear_statistics_transit_ldp_fec_prefix(self, v, load=False):
    """
    Setter method for mpls_clear_statistics_transit_ldp_fec_prefix, mapped from YANG variable /brocade_mpls_rpc/clear_mpls_statistics/input/mpls_clear_statistics_transit_ldp_fec_prefix (mpls-ipv4-prefix)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_mpls_clear_statistics_transit_ldp_fec_prefix is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_mpls_clear_statistics_transit_ldp_fec_prefix() directly.

    YANG Description: Tunnel ID to be cleared
    """
    if hasattr(v, "_utype"):
      v = v._utype(v)
    try:
      t = YANGDynClass(v,base=RestrictedClassType(base_type=unicode, restriction_dict={'pattern': u'(([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])\\.){3}([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])/(([0-9])|([1-2][0-9])|(3[0-2]))'}), is_leaf=True, yang_name="mpls-clear-statistics-transit-ldp-fec-prefix", rest_name="mpls-clear-statistics-transit-ldp-fec-prefix", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=False, namespace='urn:brocade.com:mgmt:brocade-mpls', defining_module='brocade-mpls', yang_type='mpls-ipv4-prefix', is_config=True)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """mpls_clear_statistics_transit_ldp_fec_prefix must be of a type compatible with mpls-ipv4-prefix""",
          'defined-type': "brocade-mpls:mpls-ipv4-prefix",
          'generated-type': """YANGDynClass(base=RestrictedClassType(base_type=unicode, restriction_dict={'pattern': u'(([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])\\.){3}([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])/(([0-9])|([1-2][0-9])|(3[0-2]))'}), is_leaf=True, yang_name="mpls-clear-statistics-transit-ldp-fec-prefix", rest_name="mpls-clear-statistics-transit-ldp-fec-prefix", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=False, namespace='urn:brocade.com:mgmt:brocade-mpls', defining_module='brocade-mpls', yang_type='mpls-ipv4-prefix', is_config=True)""",
        })

    self.__mpls_clear_statistics_transit_ldp_fec_prefix = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_mpls_clear_statistics_transit_ldp_fec_prefix(self):
    self.__mpls_clear_statistics_transit_ldp_fec_prefix = YANGDynClass(base=RestrictedClassType(base_type=unicode, restriction_dict={'pattern': u'(([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])\\.){3}([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])/(([0-9])|([1-2][0-9])|(3[0-2]))'}), is_leaf=True, yang_name="mpls-clear-statistics-transit-ldp-fec-prefix", rest_name="mpls-clear-statistics-transit-ldp-fec-prefix", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=False, namespace='urn:brocade.com:mgmt:brocade-mpls', defining_module='brocade-mpls', yang_type='mpls-ipv4-prefix', is_config=True)


  def _get_mpls_clear_statistics_transit_ldp_prefix_address(self):
    """
    Getter method for mpls_clear_statistics_transit_ldp_prefix_address, mapped from YANG variable /brocade_mpls_rpc/clear_mpls_statistics/input/mpls_clear_statistics_transit_ldp_prefix_address (mpls-ipv4-address)

    YANG Description: Tunnel ID to be cleared
    """
    return self.__mpls_clear_statistics_transit_ldp_prefix_address
      
  def _set_mpls_clear_statistics_transit_ldp_prefix_address(self, v, load=False):
    """
    Setter method for mpls_clear_statistics_transit_ldp_prefix_address, mapped from YANG variable /brocade_mpls_rpc/clear_mpls_statistics/input/mpls_clear_statistics_transit_ldp_prefix_address (mpls-ipv4-address)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_mpls_clear_statistics_transit_ldp_prefix_address is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_mpls_clear_statistics_transit_ldp_prefix_address() directly.

    YANG Description: Tunnel ID to be cleared
    """
    if hasattr(v, "_utype"):
      v = v._utype(v)
    try:
      t = YANGDynClass(v,base=RestrictedClassType(base_type=unicode, restriction_dict={'pattern': u'(([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])\\.){3}([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])(%[\\p{N}\\p{L}]+)?'}), is_leaf=True, yang_name="mpls-clear-statistics-transit-ldp-prefix-address", rest_name="mpls-clear-statistics-transit-ldp-prefix-address", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=False, namespace='urn:brocade.com:mgmt:brocade-mpls', defining_module='brocade-mpls', yang_type='mpls-ipv4-address', is_config=True)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """mpls_clear_statistics_transit_ldp_prefix_address must be of a type compatible with mpls-ipv4-address""",
          'defined-type': "brocade-mpls:mpls-ipv4-address",
          'generated-type': """YANGDynClass(base=RestrictedClassType(base_type=unicode, restriction_dict={'pattern': u'(([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])\\.){3}([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])(%[\\p{N}\\p{L}]+)?'}), is_leaf=True, yang_name="mpls-clear-statistics-transit-ldp-prefix-address", rest_name="mpls-clear-statistics-transit-ldp-prefix-address", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=False, namespace='urn:brocade.com:mgmt:brocade-mpls', defining_module='brocade-mpls', yang_type='mpls-ipv4-address', is_config=True)""",
        })

    self.__mpls_clear_statistics_transit_ldp_prefix_address = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_mpls_clear_statistics_transit_ldp_prefix_address(self):
    self.__mpls_clear_statistics_transit_ldp_prefix_address = YANGDynClass(base=RestrictedClassType(base_type=unicode, restriction_dict={'pattern': u'(([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])\\.){3}([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])(%[\\p{N}\\p{L}]+)?'}), is_leaf=True, yang_name="mpls-clear-statistics-transit-ldp-prefix-address", rest_name="mpls-clear-statistics-transit-ldp-prefix-address", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=False, namespace='urn:brocade.com:mgmt:brocade-mpls', defining_module='brocade-mpls', yang_type='mpls-ipv4-address', is_config=True)


  def _get_mpls_clear_statistics_transit_ldp_prefix_mask(self):
    """
    Getter method for mpls_clear_statistics_transit_ldp_prefix_mask, mapped from YANG variable /brocade_mpls_rpc/clear_mpls_statistics/input/mpls_clear_statistics_transit_ldp_prefix_mask (mpls-ipv4-subnet-mask)

    YANG Description: Tunnel ID to be cleared
    """
    return self.__mpls_clear_statistics_transit_ldp_prefix_mask
      
  def _set_mpls_clear_statistics_transit_ldp_prefix_mask(self, v, load=False):
    """
    Setter method for mpls_clear_statistics_transit_ldp_prefix_mask, mapped from YANG variable /brocade_mpls_rpc/clear_mpls_statistics/input/mpls_clear_statistics_transit_ldp_prefix_mask (mpls-ipv4-subnet-mask)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_mpls_clear_statistics_transit_ldp_prefix_mask is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_mpls_clear_statistics_transit_ldp_prefix_mask() directly.

    YANG Description: Tunnel ID to be cleared
    """
    if hasattr(v, "_utype"):
      v = v._utype(v)
    try:
      t = YANGDynClass(v,base=RestrictedClassType(base_type=unicode, restriction_dict={'pattern': u'(([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])\\.){3}([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])(%[\\p{N}\\p{L}]+)?'}), is_leaf=True, yang_name="mpls-clear-statistics-transit-ldp-prefix-mask", rest_name="mpls-clear-statistics-transit-ldp-prefix-mask", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=False, namespace='urn:brocade.com:mgmt:brocade-mpls', defining_module='brocade-mpls', yang_type='mpls-ipv4-subnet-mask', is_config=True)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """mpls_clear_statistics_transit_ldp_prefix_mask must be of a type compatible with mpls-ipv4-subnet-mask""",
          'defined-type': "brocade-mpls:mpls-ipv4-subnet-mask",
          'generated-type': """YANGDynClass(base=RestrictedClassType(base_type=unicode, restriction_dict={'pattern': u'(([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])\\.){3}([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])(%[\\p{N}\\p{L}]+)?'}), is_leaf=True, yang_name="mpls-clear-statistics-transit-ldp-prefix-mask", rest_name="mpls-clear-statistics-transit-ldp-prefix-mask", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=False, namespace='urn:brocade.com:mgmt:brocade-mpls', defining_module='brocade-mpls', yang_type='mpls-ipv4-subnet-mask', is_config=True)""",
        })

    self.__mpls_clear_statistics_transit_ldp_prefix_mask = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_mpls_clear_statistics_transit_ldp_prefix_mask(self):
    self.__mpls_clear_statistics_transit_ldp_prefix_mask = YANGDynClass(base=RestrictedClassType(base_type=unicode, restriction_dict={'pattern': u'(([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])\\.){3}([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])(%[\\p{N}\\p{L}]+)?'}), is_leaf=True, yang_name="mpls-clear-statistics-transit-ldp-prefix-mask", rest_name="mpls-clear-statistics-transit-ldp-prefix-mask", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=False, namespace='urn:brocade.com:mgmt:brocade-mpls', defining_module='brocade-mpls', yang_type='mpls-ipv4-subnet-mask', is_config=True)


  def _get_mpls_clear_statistics_transit_label_id(self):
    """
    Getter method for mpls_clear_statistics_transit_label_id, mapped from YANG variable /brocade_mpls_rpc/clear_mpls_statistics/input/mpls_clear_statistics_transit_label_id (uint32)

    YANG Description: Tunnel ID to be cleared
    """
    return self.__mpls_clear_statistics_transit_label_id
      
  def _set_mpls_clear_statistics_transit_label_id(self, v, load=False):
    """
    Setter method for mpls_clear_statistics_transit_label_id, mapped from YANG variable /brocade_mpls_rpc/clear_mpls_statistics/input/mpls_clear_statistics_transit_label_id (uint32)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_mpls_clear_statistics_transit_label_id is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_mpls_clear_statistics_transit_label_id() directly.

    YANG Description: Tunnel ID to be cleared
    """
    if hasattr(v, "_utype"):
      v = v._utype(v)
    try:
      t = YANGDynClass(v,base=RestrictedClassType(base_type=long, restriction_dict={'range': ['0..4294967295']}, int_size=32), is_leaf=True, yang_name="mpls-clear-statistics-transit-label-id", rest_name="mpls-clear-statistics-transit-label-id", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=False, namespace='urn:brocade.com:mgmt:brocade-mpls', defining_module='brocade-mpls', yang_type='uint32', is_config=True)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """mpls_clear_statistics_transit_label_id must be of a type compatible with uint32""",
          'defined-type': "uint32",
          'generated-type': """YANGDynClass(base=RestrictedClassType(base_type=long, restriction_dict={'range': ['0..4294967295']}, int_size=32), is_leaf=True, yang_name="mpls-clear-statistics-transit-label-id", rest_name="mpls-clear-statistics-transit-label-id", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=False, namespace='urn:brocade.com:mgmt:brocade-mpls', defining_module='brocade-mpls', yang_type='uint32', is_config=True)""",
        })

    self.__mpls_clear_statistics_transit_label_id = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_mpls_clear_statistics_transit_label_id(self):
    self.__mpls_clear_statistics_transit_label_id = YANGDynClass(base=RestrictedClassType(base_type=long, restriction_dict={'range': ['0..4294967295']}, int_size=32), is_leaf=True, yang_name="mpls-clear-statistics-transit-label-id", rest_name="mpls-clear-statistics-transit-label-id", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=False, namespace='urn:brocade.com:mgmt:brocade-mpls', defining_module='brocade-mpls', yang_type='uint32', is_config=True)


  def _get_mpls_clear_statistics_tunnel_ldp_id(self):
    """
    Getter method for mpls_clear_statistics_tunnel_ldp_id, mapped from YANG variable /brocade_mpls_rpc/clear_mpls_statistics/input/mpls_clear_statistics_tunnel_ldp_id (uint32)

    YANG Description: Tunnel ID to be cleared
    """
    return self.__mpls_clear_statistics_tunnel_ldp_id
      
  def _set_mpls_clear_statistics_tunnel_ldp_id(self, v, load=False):
    """
    Setter method for mpls_clear_statistics_tunnel_ldp_id, mapped from YANG variable /brocade_mpls_rpc/clear_mpls_statistics/input/mpls_clear_statistics_tunnel_ldp_id (uint32)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_mpls_clear_statistics_tunnel_ldp_id is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_mpls_clear_statistics_tunnel_ldp_id() directly.

    YANG Description: Tunnel ID to be cleared
    """
    if hasattr(v, "_utype"):
      v = v._utype(v)
    try:
      t = YANGDynClass(v,base=RestrictedClassType(base_type=long, restriction_dict={'range': ['0..4294967295']}, int_size=32), is_leaf=True, yang_name="mpls-clear-statistics-tunnel-ldp-id", rest_name="mpls-clear-statistics-tunnel-ldp-id", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=False, namespace='urn:brocade.com:mgmt:brocade-mpls', defining_module='brocade-mpls', yang_type='uint32', is_config=True)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """mpls_clear_statistics_tunnel_ldp_id must be of a type compatible with uint32""",
          'defined-type': "uint32",
          'generated-type': """YANGDynClass(base=RestrictedClassType(base_type=long, restriction_dict={'range': ['0..4294967295']}, int_size=32), is_leaf=True, yang_name="mpls-clear-statistics-tunnel-ldp-id", rest_name="mpls-clear-statistics-tunnel-ldp-id", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=False, namespace='urn:brocade.com:mgmt:brocade-mpls', defining_module='brocade-mpls', yang_type='uint32', is_config=True)""",
        })

    self.__mpls_clear_statistics_tunnel_ldp_id = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_mpls_clear_statistics_tunnel_ldp_id(self):
    self.__mpls_clear_statistics_tunnel_ldp_id = YANGDynClass(base=RestrictedClassType(base_type=long, restriction_dict={'range': ['0..4294967295']}, int_size=32), is_leaf=True, yang_name="mpls-clear-statistics-tunnel-ldp-id", rest_name="mpls-clear-statistics-tunnel-ldp-id", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=False, namespace='urn:brocade.com:mgmt:brocade-mpls', defining_module='brocade-mpls', yang_type='uint32', is_config=True)


  def _get_mpls_clear_statistics_tunnel_rsvp_bypass(self):
    """
    Getter method for mpls_clear_statistics_tunnel_rsvp_bypass, mapped from YANG variable /brocade_mpls_rpc/clear_mpls_statistics/input/mpls_clear_statistics_tunnel_rsvp_bypass (uint8)

    YANG Description: Tunnel ID to be cleared
    """
    return self.__mpls_clear_statistics_tunnel_rsvp_bypass
      
  def _set_mpls_clear_statistics_tunnel_rsvp_bypass(self, v, load=False):
    """
    Setter method for mpls_clear_statistics_tunnel_rsvp_bypass, mapped from YANG variable /brocade_mpls_rpc/clear_mpls_statistics/input/mpls_clear_statistics_tunnel_rsvp_bypass (uint8)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_mpls_clear_statistics_tunnel_rsvp_bypass is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_mpls_clear_statistics_tunnel_rsvp_bypass() directly.

    YANG Description: Tunnel ID to be cleared
    """
    if hasattr(v, "_utype"):
      v = v._utype(v)
    try:
      t = YANGDynClass(v,base=RestrictedClassType(base_type=int, restriction_dict={'range': ['0..255']}, int_size=8), is_leaf=True, yang_name="mpls-clear-statistics-tunnel-rsvp-bypass", rest_name="mpls-clear-statistics-tunnel-rsvp-bypass", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=False, namespace='urn:brocade.com:mgmt:brocade-mpls', defining_module='brocade-mpls', yang_type='uint8', is_config=True)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """mpls_clear_statistics_tunnel_rsvp_bypass must be of a type compatible with uint8""",
          'defined-type': "uint8",
          'generated-type': """YANGDynClass(base=RestrictedClassType(base_type=int, restriction_dict={'range': ['0..255']}, int_size=8), is_leaf=True, yang_name="mpls-clear-statistics-tunnel-rsvp-bypass", rest_name="mpls-clear-statistics-tunnel-rsvp-bypass", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=False, namespace='urn:brocade.com:mgmt:brocade-mpls', defining_module='brocade-mpls', yang_type='uint8', is_config=True)""",
        })

    self.__mpls_clear_statistics_tunnel_rsvp_bypass = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_mpls_clear_statistics_tunnel_rsvp_bypass(self):
    self.__mpls_clear_statistics_tunnel_rsvp_bypass = YANGDynClass(base=RestrictedClassType(base_type=int, restriction_dict={'range': ['0..255']}, int_size=8), is_leaf=True, yang_name="mpls-clear-statistics-tunnel-rsvp-bypass", rest_name="mpls-clear-statistics-tunnel-rsvp-bypass", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=False, namespace='urn:brocade.com:mgmt:brocade-mpls', defining_module='brocade-mpls', yang_type='uint8', is_config=True)


  def _get_mpls_clear_statistics_tunnel_name(self):
    """
    Getter method for mpls_clear_statistics_tunnel_name, mapped from YANG variable /brocade_mpls_rpc/clear_mpls_statistics/input/mpls_clear_statistics_tunnel_name (string)

    YANG Description: Tunnel ID to be cleared
    """
    return self.__mpls_clear_statistics_tunnel_name
      
  def _set_mpls_clear_statistics_tunnel_name(self, v, load=False):
    """
    Setter method for mpls_clear_statistics_tunnel_name, mapped from YANG variable /brocade_mpls_rpc/clear_mpls_statistics/input/mpls_clear_statistics_tunnel_name (string)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_mpls_clear_statistics_tunnel_name is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_mpls_clear_statistics_tunnel_name() directly.

    YANG Description: Tunnel ID to be cleared
    """
    if hasattr(v, "_utype"):
      v = v._utype(v)
    try:
      t = YANGDynClass(v,base=unicode, is_leaf=True, yang_name="mpls-clear-statistics-tunnel-name", rest_name="mpls-clear-statistics-tunnel-name", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=False, namespace='urn:brocade.com:mgmt:brocade-mpls', defining_module='brocade-mpls', yang_type='string', is_config=True)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """mpls_clear_statistics_tunnel_name must be of a type compatible with string""",
          'defined-type': "string",
          'generated-type': """YANGDynClass(base=unicode, is_leaf=True, yang_name="mpls-clear-statistics-tunnel-name", rest_name="mpls-clear-statistics-tunnel-name", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=False, namespace='urn:brocade.com:mgmt:brocade-mpls', defining_module='brocade-mpls', yang_type='string', is_config=True)""",
        })

    self.__mpls_clear_statistics_tunnel_name = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_mpls_clear_statistics_tunnel_name(self):
    self.__mpls_clear_statistics_tunnel_name = YANGDynClass(base=unicode, is_leaf=True, yang_name="mpls-clear-statistics-tunnel-name", rest_name="mpls-clear-statistics-tunnel-name", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=False, namespace='urn:brocade.com:mgmt:brocade-mpls', defining_module='brocade-mpls', yang_type='string', is_config=True)


  def _get_mpls_clear_statistics_tunnel_dest(self):
    """
    Getter method for mpls_clear_statistics_tunnel_dest, mapped from YANG variable /brocade_mpls_rpc/clear_mpls_statistics/input/mpls_clear_statistics_tunnel_dest (mpls-ipv4-address)

    YANG Description: Tunnel ID to be cleared
    """
    return self.__mpls_clear_statistics_tunnel_dest
      
  def _set_mpls_clear_statistics_tunnel_dest(self, v, load=False):
    """
    Setter method for mpls_clear_statistics_tunnel_dest, mapped from YANG variable /brocade_mpls_rpc/clear_mpls_statistics/input/mpls_clear_statistics_tunnel_dest (mpls-ipv4-address)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_mpls_clear_statistics_tunnel_dest is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_mpls_clear_statistics_tunnel_dest() directly.

    YANG Description: Tunnel ID to be cleared
    """
    if hasattr(v, "_utype"):
      v = v._utype(v)
    try:
      t = YANGDynClass(v,base=RestrictedClassType(base_type=unicode, restriction_dict={'pattern': u'(([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])\\.){3}([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])(%[\\p{N}\\p{L}]+)?'}), is_leaf=True, yang_name="mpls-clear-statistics-tunnel-dest", rest_name="mpls-clear-statistics-tunnel-dest", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=False, namespace='urn:brocade.com:mgmt:brocade-mpls', defining_module='brocade-mpls', yang_type='mpls-ipv4-address', is_config=True)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """mpls_clear_statistics_tunnel_dest must be of a type compatible with mpls-ipv4-address""",
          'defined-type': "brocade-mpls:mpls-ipv4-address",
          'generated-type': """YANGDynClass(base=RestrictedClassType(base_type=unicode, restriction_dict={'pattern': u'(([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])\\.){3}([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])(%[\\p{N}\\p{L}]+)?'}), is_leaf=True, yang_name="mpls-clear-statistics-tunnel-dest", rest_name="mpls-clear-statistics-tunnel-dest", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=False, namespace='urn:brocade.com:mgmt:brocade-mpls', defining_module='brocade-mpls', yang_type='mpls-ipv4-address', is_config=True)""",
        })

    self.__mpls_clear_statistics_tunnel_dest = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_mpls_clear_statistics_tunnel_dest(self):
    self.__mpls_clear_statistics_tunnel_dest = YANGDynClass(base=RestrictedClassType(base_type=unicode, restriction_dict={'pattern': u'(([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])\\.){3}([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])(%[\\p{N}\\p{L}]+)?'}), is_leaf=True, yang_name="mpls-clear-statistics-tunnel-dest", rest_name="mpls-clear-statistics-tunnel-dest", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=False, namespace='urn:brocade.com:mgmt:brocade-mpls', defining_module='brocade-mpls', yang_type='mpls-ipv4-address', is_config=True)

  mpls_clear_statistics_type = __builtin__.property(_get_mpls_clear_statistics_type, _set_mpls_clear_statistics_type)
  mpls_clear_statistics_transit_ldp_fec_prefix = __builtin__.property(_get_mpls_clear_statistics_transit_ldp_fec_prefix, _set_mpls_clear_statistics_transit_ldp_fec_prefix)
  mpls_clear_statistics_transit_ldp_prefix_address = __builtin__.property(_get_mpls_clear_statistics_transit_ldp_prefix_address, _set_mpls_clear_statistics_transit_ldp_prefix_address)
  mpls_clear_statistics_transit_ldp_prefix_mask = __builtin__.property(_get_mpls_clear_statistics_transit_ldp_prefix_mask, _set_mpls_clear_statistics_transit_ldp_prefix_mask)
  mpls_clear_statistics_transit_label_id = __builtin__.property(_get_mpls_clear_statistics_transit_label_id, _set_mpls_clear_statistics_transit_label_id)
  mpls_clear_statistics_tunnel_ldp_id = __builtin__.property(_get_mpls_clear_statistics_tunnel_ldp_id, _set_mpls_clear_statistics_tunnel_ldp_id)
  mpls_clear_statistics_tunnel_rsvp_bypass = __builtin__.property(_get_mpls_clear_statistics_tunnel_rsvp_bypass, _set_mpls_clear_statistics_tunnel_rsvp_bypass)
  mpls_clear_statistics_tunnel_name = __builtin__.property(_get_mpls_clear_statistics_tunnel_name, _set_mpls_clear_statistics_tunnel_name)
  mpls_clear_statistics_tunnel_dest = __builtin__.property(_get_mpls_clear_statistics_tunnel_dest, _set_mpls_clear_statistics_tunnel_dest)


  _pyangbind_elements = {'mpls_clear_statistics_type': mpls_clear_statistics_type, 'mpls_clear_statistics_transit_ldp_fec_prefix': mpls_clear_statistics_transit_ldp_fec_prefix, 'mpls_clear_statistics_transit_ldp_prefix_address': mpls_clear_statistics_transit_ldp_prefix_address, 'mpls_clear_statistics_transit_ldp_prefix_mask': mpls_clear_statistics_transit_ldp_prefix_mask, 'mpls_clear_statistics_transit_label_id': mpls_clear_statistics_transit_label_id, 'mpls_clear_statistics_tunnel_ldp_id': mpls_clear_statistics_tunnel_ldp_id, 'mpls_clear_statistics_tunnel_rsvp_bypass': mpls_clear_statistics_tunnel_rsvp_bypass, 'mpls_clear_statistics_tunnel_name': mpls_clear_statistics_tunnel_name, 'mpls_clear_statistics_tunnel_dest': mpls_clear_statistics_tunnel_dest, }


