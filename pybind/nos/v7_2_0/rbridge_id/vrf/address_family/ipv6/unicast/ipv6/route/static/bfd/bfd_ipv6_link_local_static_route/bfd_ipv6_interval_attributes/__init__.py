
from operator import attrgetter
import pyangbind.lib.xpathhelper as xpathhelper
from pyangbind.lib.yangtypes import RestrictedPrecisionDecimalType, RestrictedClassType, TypedListType
from pyangbind.lib.yangtypes import YANGBool, YANGListType, YANGDynClass, ReferenceType
from pyangbind.lib.base import PybindBase
from decimal import Decimal
from bitarray import bitarray
import __builtin__
class bfd_ipv6_interval_attributes(PybindBase):
  """
  This class was auto-generated by the PythonClass plugin for PYANG
  from YANG module brocade-rbridge - based on the path /rbridge-id/vrf/address-family/ipv6/unicast/ipv6/route/static/bfd/bfd-ipv6-link-local-static-route/bfd-ipv6-interval-attributes. Each member element of
  the container is represented as a class variable - with a specific
  YANG type.
  """
  __slots__ = ('_pybind_generated_by', '_path_helper', '_yang_name', '_rest_name', '_extmethods', '__interval','__min_rx','__multiplier',)

  _yang_name = 'bfd-ipv6-interval-attributes'
  _rest_name = ''

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
    self.__interval = YANGDynClass(base=RestrictedClassType(base_type=RestrictedClassType(base_type=int, restriction_dict={'range': ['0..65535']},int_size=16), restriction_dict={'range': [u'50..30000']}), is_leaf=True, yang_name="interval", rest_name="interval", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'info': u'Transmit interval', u'cli-incomplete-no': None, u'cli-incomplete-command': None}}, namespace='urn:brocade.com:mgmt:brocade-ipv6-rtm', defining_module='brocade-ipv6-rtm', yang_type='uint16', is_config=True)
    self.__multiplier = YANGDynClass(base=RestrictedClassType(base_type=RestrictedClassType(base_type=int, restriction_dict={'range': ['0..255']}, int_size=8), restriction_dict={'range': [u'3..50']}), is_leaf=True, yang_name="multiplier", rest_name="multiplier", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'info': u'Multiplier value', u'cli-incomplete-no': None}}, namespace='urn:brocade.com:mgmt:brocade-ipv6-rtm', defining_module='brocade-ipv6-rtm', yang_type='uint8', is_config=True)
    self.__min_rx = YANGDynClass(base=RestrictedClassType(base_type=RestrictedClassType(base_type=int, restriction_dict={'range': ['0..65535']},int_size=16), restriction_dict={'range': [u'50..30000']}), is_leaf=True, yang_name="min-rx", rest_name="min-rx", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'info': u'Receive interval', u'cli-incomplete-no': None, u'cli-incomplete-command': None}}, namespace='urn:brocade.com:mgmt:brocade-ipv6-rtm', defining_module='brocade-ipv6-rtm', yang_type='uint16', is_config=True)

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
      return [u'rbridge-id', u'vrf', u'address-family', u'ipv6', u'unicast', u'ipv6', u'route', u'static', u'bfd', u'bfd-ipv6-link-local-static-route', u'bfd-ipv6-interval-attributes']

  def _rest_path(self):
    if hasattr(self, "_parent"):
      if self._rest_name:
        return self._parent._rest_path()+[self._rest_name]
      else:
        return self._parent._rest_path()
    else:
      return [u'rbridge-id', u'vrf', u'address-family', u'ipv6', u'unicast', u'ipv6', u'route', u'static', u'bfd', u'bfd-ipv6-link-local-static-route']

  def _get_interval(self):
    """
    Getter method for interval, mapped from YANG variable /rbridge_id/vrf/address_family/ipv6/unicast/ipv6/route/static/bfd/bfd_ipv6_link_local_static_route/bfd_ipv6_interval_attributes/interval (uint16)
    """
    return self.__interval
      
  def _set_interval(self, v, load=False):
    """
    Setter method for interval, mapped from YANG variable /rbridge_id/vrf/address_family/ipv6/unicast/ipv6/route/static/bfd/bfd_ipv6_link_local_static_route/bfd_ipv6_interval_attributes/interval (uint16)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_interval is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_interval() directly.
    """
    if hasattr(v, "_utype"):
      v = v._utype(v)
    try:
      t = YANGDynClass(v,base=RestrictedClassType(base_type=RestrictedClassType(base_type=int, restriction_dict={'range': ['0..65535']},int_size=16), restriction_dict={'range': [u'50..30000']}), is_leaf=True, yang_name="interval", rest_name="interval", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'info': u'Transmit interval', u'cli-incomplete-no': None, u'cli-incomplete-command': None}}, namespace='urn:brocade.com:mgmt:brocade-ipv6-rtm', defining_module='brocade-ipv6-rtm', yang_type='uint16', is_config=True)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """interval must be of a type compatible with uint16""",
          'defined-type': "uint16",
          'generated-type': """YANGDynClass(base=RestrictedClassType(base_type=RestrictedClassType(base_type=int, restriction_dict={'range': ['0..65535']},int_size=16), restriction_dict={'range': [u'50..30000']}), is_leaf=True, yang_name="interval", rest_name="interval", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'info': u'Transmit interval', u'cli-incomplete-no': None, u'cli-incomplete-command': None}}, namespace='urn:brocade.com:mgmt:brocade-ipv6-rtm', defining_module='brocade-ipv6-rtm', yang_type='uint16', is_config=True)""",
        })

    self.__interval = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_interval(self):
    self.__interval = YANGDynClass(base=RestrictedClassType(base_type=RestrictedClassType(base_type=int, restriction_dict={'range': ['0..65535']},int_size=16), restriction_dict={'range': [u'50..30000']}), is_leaf=True, yang_name="interval", rest_name="interval", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'info': u'Transmit interval', u'cli-incomplete-no': None, u'cli-incomplete-command': None}}, namespace='urn:brocade.com:mgmt:brocade-ipv6-rtm', defining_module='brocade-ipv6-rtm', yang_type='uint16', is_config=True)


  def _get_min_rx(self):
    """
    Getter method for min_rx, mapped from YANG variable /rbridge_id/vrf/address_family/ipv6/unicast/ipv6/route/static/bfd/bfd_ipv6_link_local_static_route/bfd_ipv6_interval_attributes/min_rx (uint16)
    """
    return self.__min_rx
      
  def _set_min_rx(self, v, load=False):
    """
    Setter method for min_rx, mapped from YANG variable /rbridge_id/vrf/address_family/ipv6/unicast/ipv6/route/static/bfd/bfd_ipv6_link_local_static_route/bfd_ipv6_interval_attributes/min_rx (uint16)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_min_rx is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_min_rx() directly.
    """
    if hasattr(v, "_utype"):
      v = v._utype(v)
    try:
      t = YANGDynClass(v,base=RestrictedClassType(base_type=RestrictedClassType(base_type=int, restriction_dict={'range': ['0..65535']},int_size=16), restriction_dict={'range': [u'50..30000']}), is_leaf=True, yang_name="min-rx", rest_name="min-rx", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'info': u'Receive interval', u'cli-incomplete-no': None, u'cli-incomplete-command': None}}, namespace='urn:brocade.com:mgmt:brocade-ipv6-rtm', defining_module='brocade-ipv6-rtm', yang_type='uint16', is_config=True)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """min_rx must be of a type compatible with uint16""",
          'defined-type': "uint16",
          'generated-type': """YANGDynClass(base=RestrictedClassType(base_type=RestrictedClassType(base_type=int, restriction_dict={'range': ['0..65535']},int_size=16), restriction_dict={'range': [u'50..30000']}), is_leaf=True, yang_name="min-rx", rest_name="min-rx", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'info': u'Receive interval', u'cli-incomplete-no': None, u'cli-incomplete-command': None}}, namespace='urn:brocade.com:mgmt:brocade-ipv6-rtm', defining_module='brocade-ipv6-rtm', yang_type='uint16', is_config=True)""",
        })

    self.__min_rx = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_min_rx(self):
    self.__min_rx = YANGDynClass(base=RestrictedClassType(base_type=RestrictedClassType(base_type=int, restriction_dict={'range': ['0..65535']},int_size=16), restriction_dict={'range': [u'50..30000']}), is_leaf=True, yang_name="min-rx", rest_name="min-rx", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'info': u'Receive interval', u'cli-incomplete-no': None, u'cli-incomplete-command': None}}, namespace='urn:brocade.com:mgmt:brocade-ipv6-rtm', defining_module='brocade-ipv6-rtm', yang_type='uint16', is_config=True)


  def _get_multiplier(self):
    """
    Getter method for multiplier, mapped from YANG variable /rbridge_id/vrf/address_family/ipv6/unicast/ipv6/route/static/bfd/bfd_ipv6_link_local_static_route/bfd_ipv6_interval_attributes/multiplier (uint8)
    """
    return self.__multiplier
      
  def _set_multiplier(self, v, load=False):
    """
    Setter method for multiplier, mapped from YANG variable /rbridge_id/vrf/address_family/ipv6/unicast/ipv6/route/static/bfd/bfd_ipv6_link_local_static_route/bfd_ipv6_interval_attributes/multiplier (uint8)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_multiplier is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_multiplier() directly.
    """
    if hasattr(v, "_utype"):
      v = v._utype(v)
    try:
      t = YANGDynClass(v,base=RestrictedClassType(base_type=RestrictedClassType(base_type=int, restriction_dict={'range': ['0..255']}, int_size=8), restriction_dict={'range': [u'3..50']}), is_leaf=True, yang_name="multiplier", rest_name="multiplier", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'info': u'Multiplier value', u'cli-incomplete-no': None}}, namespace='urn:brocade.com:mgmt:brocade-ipv6-rtm', defining_module='brocade-ipv6-rtm', yang_type='uint8', is_config=True)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """multiplier must be of a type compatible with uint8""",
          'defined-type': "uint8",
          'generated-type': """YANGDynClass(base=RestrictedClassType(base_type=RestrictedClassType(base_type=int, restriction_dict={'range': ['0..255']}, int_size=8), restriction_dict={'range': [u'3..50']}), is_leaf=True, yang_name="multiplier", rest_name="multiplier", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'info': u'Multiplier value', u'cli-incomplete-no': None}}, namespace='urn:brocade.com:mgmt:brocade-ipv6-rtm', defining_module='brocade-ipv6-rtm', yang_type='uint8', is_config=True)""",
        })

    self.__multiplier = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_multiplier(self):
    self.__multiplier = YANGDynClass(base=RestrictedClassType(base_type=RestrictedClassType(base_type=int, restriction_dict={'range': ['0..255']}, int_size=8), restriction_dict={'range': [u'3..50']}), is_leaf=True, yang_name="multiplier", rest_name="multiplier", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'info': u'Multiplier value', u'cli-incomplete-no': None}}, namespace='urn:brocade.com:mgmt:brocade-ipv6-rtm', defining_module='brocade-ipv6-rtm', yang_type='uint8', is_config=True)

  interval = __builtin__.property(_get_interval, _set_interval)
  min_rx = __builtin__.property(_get_min_rx, _set_min_rx)
  multiplier = __builtin__.property(_get_multiplier, _set_multiplier)


  _pyangbind_elements = {'interval': interval, 'min_rx': min_rx, 'multiplier': multiplier, }


