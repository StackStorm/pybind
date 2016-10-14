
from operator import attrgetter
import pyangbind.lib.xpathhelper as xpathhelper
from pyangbind.lib.yangtypes import RestrictedPrecisionDecimalType, RestrictedClassType, TypedListType
from pyangbind.lib.yangtypes import YANGBool, YANGListType, YANGDynClass, ReferenceType
from pyangbind.lib.base import PybindBase
from decimal import Decimal
from bitarray import bitarray
import __builtin__
class statistics(PybindBase):
  """
  This class was auto-generated by the PythonClass plugin for PYANG
  from YANG module brocade-mpls-operational - based on the path /mpls-state/tunnel-traffic-statistics/statistics. Each member element of
  the container is represented as a class variable - with a specific
  YANG type.
  """
  __slots__ = ('_pybind_generated_by', '_path_helper', '_yang_name', '_extmethods', '__number_of_packets','__number_of_packets_since_clear','__number_of_bytes','__number_of_bytes_since_clear','__packets_per_second','__bytes_per_second','__averaging_interval_seconds',)

  _yang_name = 'statistics'

  _pybind_generated_by = 'container'

  def __init__(self, *args, **kwargs):

    helper = kwargs.pop("path_helper", None)
    if helper is False:
      self._path_helper = False
    elif helper is not None and isinstance(helper, xpathhelper.YANGPathHelper):
      self._path_helper = helper
    elif hasattr(self, "_parent"):
      helper = getattr(self._parent, "_path_helper", False)
      self._path_helper = helper
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
    self.__number_of_packets = YANGDynClass(base=RestrictedClassType(base_type=long, restriction_dict={'range':  ['0..18446744073709551615']}, int_size=64), is_leaf=True, yang_name="number-of-packets", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='urn:brocade.com:mgmt:brocade-mpls-operational', defining_module='brocade-mpls-operational', yang_type='uint64', is_config=False)
    self.__packets_per_second = YANGDynClass(base=RestrictedClassType(base_type=long, restriction_dict={'range':  ['0..18446744073709551615']}, int_size=64), is_leaf=True, yang_name="packets-per-second", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='urn:brocade.com:mgmt:brocade-mpls-operational', defining_module='brocade-mpls-operational', yang_type='uint64', is_config=False)
    self.__number_of_bytes = YANGDynClass(base=RestrictedClassType(base_type=long, restriction_dict={'range':  ['0..18446744073709551615']}, int_size=64), is_leaf=True, yang_name="number-of-bytes", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='urn:brocade.com:mgmt:brocade-mpls-operational', defining_module='brocade-mpls-operational', yang_type='uint64', is_config=False)
    self.__number_of_bytes_since_clear = YANGDynClass(base=RestrictedClassType(base_type=long, restriction_dict={'range':  ['0..18446744073709551615']}, int_size=64), is_leaf=True, yang_name="number-of-bytes-since-clear", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='urn:brocade.com:mgmt:brocade-mpls-operational', defining_module='brocade-mpls-operational', yang_type='uint64', is_config=False)
    self.__averaging_interval_seconds = YANGDynClass(base=RestrictedClassType(base_type=long, restriction_dict={'range': ['0..4294967295']}, int_size=32), is_leaf=True, yang_name="averaging-interval-seconds", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='urn:brocade.com:mgmt:brocade-mpls-operational', defining_module='brocade-mpls-operational', yang_type='uint32', is_config=False)
    self.__bytes_per_second = YANGDynClass(base=RestrictedClassType(base_type=long, restriction_dict={'range':  ['0..18446744073709551615']}, int_size=64), is_leaf=True, yang_name="bytes-per-second", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='urn:brocade.com:mgmt:brocade-mpls-operational', defining_module='brocade-mpls-operational', yang_type='uint64', is_config=False)
    self.__number_of_packets_since_clear = YANGDynClass(base=RestrictedClassType(base_type=long, restriction_dict={'range':  ['0..18446744073709551615']}, int_size=64), is_leaf=True, yang_name="number-of-packets-since-clear", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='urn:brocade.com:mgmt:brocade-mpls-operational', defining_module='brocade-mpls-operational', yang_type='uint64', is_config=False)

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
      return [u'mpls-state', u'tunnel-traffic-statistics', u'statistics']

  def _rest_path(self):
    if hasattr(self, "_supplied_register_path"):
      return [self._supplied_register_path]
    if hasattr(self, "_parent"):
      return self._parent._rest_path()+[self._yang_name]
    else:
      return [u'mpls-state', u'tunnel-traffic-statistics', u'statistics']

  def _get_number_of_packets(self):
    """
    Getter method for number_of_packets, mapped from YANG variable /mpls_state/tunnel_traffic_statistics/statistics/number_of_packets (uint64)

    YANG Description: Total number of packets
    """
    return self.__number_of_packets
      
  def _set_number_of_packets(self, v, load=False):
    """
    Setter method for number_of_packets, mapped from YANG variable /mpls_state/tunnel_traffic_statistics/statistics/number_of_packets (uint64)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_number_of_packets is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_number_of_packets() directly.

    YANG Description: Total number of packets
    """
    try:
      t = YANGDynClass(v,base=RestrictedClassType(base_type=long, restriction_dict={'range':  ['0..18446744073709551615']}, int_size=64), is_leaf=True, yang_name="number-of-packets", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='urn:brocade.com:mgmt:brocade-mpls-operational', defining_module='brocade-mpls-operational', yang_type='uint64', is_config=False)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """number_of_packets must be of a type compatible with uint64""",
          'defined-type': "uint64",
          'generated-type': """YANGDynClass(base=RestrictedClassType(base_type=long, restriction_dict={'range':  ['0..18446744073709551615']}, int_size=64), is_leaf=True, yang_name="number-of-packets", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='urn:brocade.com:mgmt:brocade-mpls-operational', defining_module='brocade-mpls-operational', yang_type='uint64', is_config=False)""",
        })

    self.__number_of_packets = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_number_of_packets(self):
    self.__number_of_packets = YANGDynClass(base=RestrictedClassType(base_type=long, restriction_dict={'range':  ['0..18446744073709551615']}, int_size=64), is_leaf=True, yang_name="number-of-packets", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='urn:brocade.com:mgmt:brocade-mpls-operational', defining_module='brocade-mpls-operational', yang_type='uint64', is_config=False)


  def _get_number_of_packets_since_clear(self):
    """
    Getter method for number_of_packets_since_clear, mapped from YANG variable /mpls_state/tunnel_traffic_statistics/statistics/number_of_packets_since_clear (uint64)

    YANG Description: Total number of packets since lst clear
    """
    return self.__number_of_packets_since_clear
      
  def _set_number_of_packets_since_clear(self, v, load=False):
    """
    Setter method for number_of_packets_since_clear, mapped from YANG variable /mpls_state/tunnel_traffic_statistics/statistics/number_of_packets_since_clear (uint64)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_number_of_packets_since_clear is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_number_of_packets_since_clear() directly.

    YANG Description: Total number of packets since lst clear
    """
    try:
      t = YANGDynClass(v,base=RestrictedClassType(base_type=long, restriction_dict={'range':  ['0..18446744073709551615']}, int_size=64), is_leaf=True, yang_name="number-of-packets-since-clear", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='urn:brocade.com:mgmt:brocade-mpls-operational', defining_module='brocade-mpls-operational', yang_type='uint64', is_config=False)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """number_of_packets_since_clear must be of a type compatible with uint64""",
          'defined-type': "uint64",
          'generated-type': """YANGDynClass(base=RestrictedClassType(base_type=long, restriction_dict={'range':  ['0..18446744073709551615']}, int_size=64), is_leaf=True, yang_name="number-of-packets-since-clear", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='urn:brocade.com:mgmt:brocade-mpls-operational', defining_module='brocade-mpls-operational', yang_type='uint64', is_config=False)""",
        })

    self.__number_of_packets_since_clear = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_number_of_packets_since_clear(self):
    self.__number_of_packets_since_clear = YANGDynClass(base=RestrictedClassType(base_type=long, restriction_dict={'range':  ['0..18446744073709551615']}, int_size=64), is_leaf=True, yang_name="number-of-packets-since-clear", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='urn:brocade.com:mgmt:brocade-mpls-operational', defining_module='brocade-mpls-operational', yang_type='uint64', is_config=False)


  def _get_number_of_bytes(self):
    """
    Getter method for number_of_bytes, mapped from YANG variable /mpls_state/tunnel_traffic_statistics/statistics/number_of_bytes (uint64)

    YANG Description: Total number of bytes
    """
    return self.__number_of_bytes
      
  def _set_number_of_bytes(self, v, load=False):
    """
    Setter method for number_of_bytes, mapped from YANG variable /mpls_state/tunnel_traffic_statistics/statistics/number_of_bytes (uint64)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_number_of_bytes is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_number_of_bytes() directly.

    YANG Description: Total number of bytes
    """
    try:
      t = YANGDynClass(v,base=RestrictedClassType(base_type=long, restriction_dict={'range':  ['0..18446744073709551615']}, int_size=64), is_leaf=True, yang_name="number-of-bytes", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='urn:brocade.com:mgmt:brocade-mpls-operational', defining_module='brocade-mpls-operational', yang_type='uint64', is_config=False)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """number_of_bytes must be of a type compatible with uint64""",
          'defined-type': "uint64",
          'generated-type': """YANGDynClass(base=RestrictedClassType(base_type=long, restriction_dict={'range':  ['0..18446744073709551615']}, int_size=64), is_leaf=True, yang_name="number-of-bytes", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='urn:brocade.com:mgmt:brocade-mpls-operational', defining_module='brocade-mpls-operational', yang_type='uint64', is_config=False)""",
        })

    self.__number_of_bytes = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_number_of_bytes(self):
    self.__number_of_bytes = YANGDynClass(base=RestrictedClassType(base_type=long, restriction_dict={'range':  ['0..18446744073709551615']}, int_size=64), is_leaf=True, yang_name="number-of-bytes", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='urn:brocade.com:mgmt:brocade-mpls-operational', defining_module='brocade-mpls-operational', yang_type='uint64', is_config=False)


  def _get_number_of_bytes_since_clear(self):
    """
    Getter method for number_of_bytes_since_clear, mapped from YANG variable /mpls_state/tunnel_traffic_statistics/statistics/number_of_bytes_since_clear (uint64)

    YANG Description: Total number of bytes since last clear
    """
    return self.__number_of_bytes_since_clear
      
  def _set_number_of_bytes_since_clear(self, v, load=False):
    """
    Setter method for number_of_bytes_since_clear, mapped from YANG variable /mpls_state/tunnel_traffic_statistics/statistics/number_of_bytes_since_clear (uint64)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_number_of_bytes_since_clear is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_number_of_bytes_since_clear() directly.

    YANG Description: Total number of bytes since last clear
    """
    try:
      t = YANGDynClass(v,base=RestrictedClassType(base_type=long, restriction_dict={'range':  ['0..18446744073709551615']}, int_size=64), is_leaf=True, yang_name="number-of-bytes-since-clear", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='urn:brocade.com:mgmt:brocade-mpls-operational', defining_module='brocade-mpls-operational', yang_type='uint64', is_config=False)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """number_of_bytes_since_clear must be of a type compatible with uint64""",
          'defined-type': "uint64",
          'generated-type': """YANGDynClass(base=RestrictedClassType(base_type=long, restriction_dict={'range':  ['0..18446744073709551615']}, int_size=64), is_leaf=True, yang_name="number-of-bytes-since-clear", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='urn:brocade.com:mgmt:brocade-mpls-operational', defining_module='brocade-mpls-operational', yang_type='uint64', is_config=False)""",
        })

    self.__number_of_bytes_since_clear = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_number_of_bytes_since_clear(self):
    self.__number_of_bytes_since_clear = YANGDynClass(base=RestrictedClassType(base_type=long, restriction_dict={'range':  ['0..18446744073709551615']}, int_size=64), is_leaf=True, yang_name="number-of-bytes-since-clear", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='urn:brocade.com:mgmt:brocade-mpls-operational', defining_module='brocade-mpls-operational', yang_type='uint64', is_config=False)


  def _get_packets_per_second(self):
    """
    Getter method for packets_per_second, mapped from YANG variable /mpls_state/tunnel_traffic_statistics/statistics/packets_per_second (uint64)

    YANG Description: Packets per second
    """
    return self.__packets_per_second
      
  def _set_packets_per_second(self, v, load=False):
    """
    Setter method for packets_per_second, mapped from YANG variable /mpls_state/tunnel_traffic_statistics/statistics/packets_per_second (uint64)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_packets_per_second is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_packets_per_second() directly.

    YANG Description: Packets per second
    """
    try:
      t = YANGDynClass(v,base=RestrictedClassType(base_type=long, restriction_dict={'range':  ['0..18446744073709551615']}, int_size=64), is_leaf=True, yang_name="packets-per-second", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='urn:brocade.com:mgmt:brocade-mpls-operational', defining_module='brocade-mpls-operational', yang_type='uint64', is_config=False)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """packets_per_second must be of a type compatible with uint64""",
          'defined-type': "uint64",
          'generated-type': """YANGDynClass(base=RestrictedClassType(base_type=long, restriction_dict={'range':  ['0..18446744073709551615']}, int_size=64), is_leaf=True, yang_name="packets-per-second", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='urn:brocade.com:mgmt:brocade-mpls-operational', defining_module='brocade-mpls-operational', yang_type='uint64', is_config=False)""",
        })

    self.__packets_per_second = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_packets_per_second(self):
    self.__packets_per_second = YANGDynClass(base=RestrictedClassType(base_type=long, restriction_dict={'range':  ['0..18446744073709551615']}, int_size=64), is_leaf=True, yang_name="packets-per-second", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='urn:brocade.com:mgmt:brocade-mpls-operational', defining_module='brocade-mpls-operational', yang_type='uint64', is_config=False)


  def _get_bytes_per_second(self):
    """
    Getter method for bytes_per_second, mapped from YANG variable /mpls_state/tunnel_traffic_statistics/statistics/bytes_per_second (uint64)

    YANG Description: Bytes per second
    """
    return self.__bytes_per_second
      
  def _set_bytes_per_second(self, v, load=False):
    """
    Setter method for bytes_per_second, mapped from YANG variable /mpls_state/tunnel_traffic_statistics/statistics/bytes_per_second (uint64)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_bytes_per_second is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_bytes_per_second() directly.

    YANG Description: Bytes per second
    """
    try:
      t = YANGDynClass(v,base=RestrictedClassType(base_type=long, restriction_dict={'range':  ['0..18446744073709551615']}, int_size=64), is_leaf=True, yang_name="bytes-per-second", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='urn:brocade.com:mgmt:brocade-mpls-operational', defining_module='brocade-mpls-operational', yang_type='uint64', is_config=False)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """bytes_per_second must be of a type compatible with uint64""",
          'defined-type': "uint64",
          'generated-type': """YANGDynClass(base=RestrictedClassType(base_type=long, restriction_dict={'range':  ['0..18446744073709551615']}, int_size=64), is_leaf=True, yang_name="bytes-per-second", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='urn:brocade.com:mgmt:brocade-mpls-operational', defining_module='brocade-mpls-operational', yang_type='uint64', is_config=False)""",
        })

    self.__bytes_per_second = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_bytes_per_second(self):
    self.__bytes_per_second = YANGDynClass(base=RestrictedClassType(base_type=long, restriction_dict={'range':  ['0..18446744073709551615']}, int_size=64), is_leaf=True, yang_name="bytes-per-second", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='urn:brocade.com:mgmt:brocade-mpls-operational', defining_module='brocade-mpls-operational', yang_type='uint64', is_config=False)


  def _get_averaging_interval_seconds(self):
    """
    Getter method for averaging_interval_seconds, mapped from YANG variable /mpls_state/tunnel_traffic_statistics/statistics/averaging_interval_seconds (uint32)

    YANG Description: Averaging Interval
    """
    return self.__averaging_interval_seconds
      
  def _set_averaging_interval_seconds(self, v, load=False):
    """
    Setter method for averaging_interval_seconds, mapped from YANG variable /mpls_state/tunnel_traffic_statistics/statistics/averaging_interval_seconds (uint32)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_averaging_interval_seconds is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_averaging_interval_seconds() directly.

    YANG Description: Averaging Interval
    """
    try:
      t = YANGDynClass(v,base=RestrictedClassType(base_type=long, restriction_dict={'range': ['0..4294967295']}, int_size=32), is_leaf=True, yang_name="averaging-interval-seconds", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='urn:brocade.com:mgmt:brocade-mpls-operational', defining_module='brocade-mpls-operational', yang_type='uint32', is_config=False)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """averaging_interval_seconds must be of a type compatible with uint32""",
          'defined-type': "uint32",
          'generated-type': """YANGDynClass(base=RestrictedClassType(base_type=long, restriction_dict={'range': ['0..4294967295']}, int_size=32), is_leaf=True, yang_name="averaging-interval-seconds", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='urn:brocade.com:mgmt:brocade-mpls-operational', defining_module='brocade-mpls-operational', yang_type='uint32', is_config=False)""",
        })

    self.__averaging_interval_seconds = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_averaging_interval_seconds(self):
    self.__averaging_interval_seconds = YANGDynClass(base=RestrictedClassType(base_type=long, restriction_dict={'range': ['0..4294967295']}, int_size=32), is_leaf=True, yang_name="averaging-interval-seconds", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='urn:brocade.com:mgmt:brocade-mpls-operational', defining_module='brocade-mpls-operational', yang_type='uint32', is_config=False)

  number_of_packets = __builtin__.property(_get_number_of_packets)
  number_of_packets_since_clear = __builtin__.property(_get_number_of_packets_since_clear)
  number_of_bytes = __builtin__.property(_get_number_of_bytes)
  number_of_bytes_since_clear = __builtin__.property(_get_number_of_bytes_since_clear)
  packets_per_second = __builtin__.property(_get_packets_per_second)
  bytes_per_second = __builtin__.property(_get_bytes_per_second)
  averaging_interval_seconds = __builtin__.property(_get_averaging_interval_seconds)


  _pyangbind_elements = {'number_of_packets': number_of_packets, 'number_of_packets_since_clear': number_of_packets_since_clear, 'number_of_bytes': number_of_bytes, 'number_of_bytes_since_clear': number_of_bytes_since_clear, 'packets_per_second': packets_per_second, 'bytes_per_second': bytes_per_second, 'averaging_interval_seconds': averaging_interval_seconds, }

