
from operator import attrgetter
import pyangbind.lib.xpathhelper as xpathhelper
from pyangbind.lib.yangtypes import RestrictedPrecisionDecimalType, RestrictedClassType, TypedListType
from pyangbind.lib.yangtypes import YANGBool, YANGListType, YANGDynClass, ReferenceType
from pyangbind.lib.base import PybindBase
from decimal import Decimal
from bitarray import bitarray
import __builtin__
import ethernet
import ip
import ipv6
import mpls
class hash(PybindBase):
  """
  This class was auto-generated by the PythonClass plugin for PYANG
  from YANG module brocade-rbridge-lag - based on the path /load-balance-lag/load-balance/hash. Each member element of
  the container is represented as a class variable - with a specific
  YANG type.
  """
  __slots__ = ('_pybind_generated_by', '_path_helper', '_yang_name', '_rest_name', '_extmethods', '__ethernet','__ip','__ipv6','__mpls',)

  _yang_name = 'hash'
  _rest_name = 'hash'

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
    self.__ethernet = YANGDynClass(base=ethernet.ethernet, is_container='container', yang_name="ethernet", rest_name="ethernet", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'info': u'ethernet <sa-mac> <da-mac> <vlan> <etype>'}}, namespace='urn:brocade.com:mgmt:brocade-rbridge-lag', defining_module='brocade-rbridge-lag', yang_type='container', is_config=True)
    self.__ipv6 = YANGDynClass(base=ipv6.ipv6, is_container='container', yang_name="ipv6", rest_name="ipv6", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'info': u'ipv6 <ipv6-src-l4-port> <ipv6-dst-l4-port> <ipv6-src-ip> <ipv6-dst-ip> <ipv6-next-hdr>'}}, namespace='urn:brocade.com:mgmt:brocade-rbridge-lag', defining_module='brocade-rbridge-lag', yang_type='container', is_config=True)
    self.__mpls = YANGDynClass(base=mpls.mpls, is_container='container', yang_name="mpls", rest_name="mpls", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'info': u'mpls <label1> <label2> <label3>'}}, namespace='urn:brocade.com:mgmt:brocade-rbridge-lag', defining_module='brocade-rbridge-lag', yang_type='container', is_config=True)
    self.__ip = YANGDynClass(base=ip.ip, is_container='container', yang_name="ip", rest_name="ip", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'info': u'ip <src-l4-port> <dst-l4-port> <src-ip> <dst-ip> <protocol>'}}, namespace='urn:brocade.com:mgmt:brocade-rbridge-lag', defining_module='brocade-rbridge-lag', yang_type='container', is_config=True)

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
      return [u'load-balance-lag', u'load-balance', u'hash']

  def _rest_path(self):
    if hasattr(self, "_parent"):
      if self._rest_name:
        return self._parent._rest_path()+[self._rest_name]
      else:
        return self._parent._rest_path()
    else:
      return [u'load-balance', u'hash']

  def _get_ethernet(self):
    """
    Getter method for ethernet, mapped from YANG variable /load_balance_lag/load_balance/hash/ethernet (container)
    """
    return self.__ethernet
      
  def _set_ethernet(self, v, load=False):
    """
    Setter method for ethernet, mapped from YANG variable /load_balance_lag/load_balance/hash/ethernet (container)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_ethernet is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_ethernet() directly.
    """
    if hasattr(v, "_utype"):
      v = v._utype(v)
    try:
      t = YANGDynClass(v,base=ethernet.ethernet, is_container='container', yang_name="ethernet", rest_name="ethernet", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'info': u'ethernet <sa-mac> <da-mac> <vlan> <etype>'}}, namespace='urn:brocade.com:mgmt:brocade-rbridge-lag', defining_module='brocade-rbridge-lag', yang_type='container', is_config=True)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """ethernet must be of a type compatible with container""",
          'defined-type': "container",
          'generated-type': """YANGDynClass(base=ethernet.ethernet, is_container='container', yang_name="ethernet", rest_name="ethernet", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'info': u'ethernet <sa-mac> <da-mac> <vlan> <etype>'}}, namespace='urn:brocade.com:mgmt:brocade-rbridge-lag', defining_module='brocade-rbridge-lag', yang_type='container', is_config=True)""",
        })

    self.__ethernet = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_ethernet(self):
    self.__ethernet = YANGDynClass(base=ethernet.ethernet, is_container='container', yang_name="ethernet", rest_name="ethernet", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'info': u'ethernet <sa-mac> <da-mac> <vlan> <etype>'}}, namespace='urn:brocade.com:mgmt:brocade-rbridge-lag', defining_module='brocade-rbridge-lag', yang_type='container', is_config=True)


  def _get_ip(self):
    """
    Getter method for ip, mapped from YANG variable /load_balance_lag/load_balance/hash/ip (container)
    """
    return self.__ip
      
  def _set_ip(self, v, load=False):
    """
    Setter method for ip, mapped from YANG variable /load_balance_lag/load_balance/hash/ip (container)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_ip is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_ip() directly.
    """
    if hasattr(v, "_utype"):
      v = v._utype(v)
    try:
      t = YANGDynClass(v,base=ip.ip, is_container='container', yang_name="ip", rest_name="ip", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'info': u'ip <src-l4-port> <dst-l4-port> <src-ip> <dst-ip> <protocol>'}}, namespace='urn:brocade.com:mgmt:brocade-rbridge-lag', defining_module='brocade-rbridge-lag', yang_type='container', is_config=True)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """ip must be of a type compatible with container""",
          'defined-type': "container",
          'generated-type': """YANGDynClass(base=ip.ip, is_container='container', yang_name="ip", rest_name="ip", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'info': u'ip <src-l4-port> <dst-l4-port> <src-ip> <dst-ip> <protocol>'}}, namespace='urn:brocade.com:mgmt:brocade-rbridge-lag', defining_module='brocade-rbridge-lag', yang_type='container', is_config=True)""",
        })

    self.__ip = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_ip(self):
    self.__ip = YANGDynClass(base=ip.ip, is_container='container', yang_name="ip", rest_name="ip", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'info': u'ip <src-l4-port> <dst-l4-port> <src-ip> <dst-ip> <protocol>'}}, namespace='urn:brocade.com:mgmt:brocade-rbridge-lag', defining_module='brocade-rbridge-lag', yang_type='container', is_config=True)


  def _get_ipv6(self):
    """
    Getter method for ipv6, mapped from YANG variable /load_balance_lag/load_balance/hash/ipv6 (container)
    """
    return self.__ipv6
      
  def _set_ipv6(self, v, load=False):
    """
    Setter method for ipv6, mapped from YANG variable /load_balance_lag/load_balance/hash/ipv6 (container)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_ipv6 is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_ipv6() directly.
    """
    if hasattr(v, "_utype"):
      v = v._utype(v)
    try:
      t = YANGDynClass(v,base=ipv6.ipv6, is_container='container', yang_name="ipv6", rest_name="ipv6", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'info': u'ipv6 <ipv6-src-l4-port> <ipv6-dst-l4-port> <ipv6-src-ip> <ipv6-dst-ip> <ipv6-next-hdr>'}}, namespace='urn:brocade.com:mgmt:brocade-rbridge-lag', defining_module='brocade-rbridge-lag', yang_type='container', is_config=True)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """ipv6 must be of a type compatible with container""",
          'defined-type': "container",
          'generated-type': """YANGDynClass(base=ipv6.ipv6, is_container='container', yang_name="ipv6", rest_name="ipv6", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'info': u'ipv6 <ipv6-src-l4-port> <ipv6-dst-l4-port> <ipv6-src-ip> <ipv6-dst-ip> <ipv6-next-hdr>'}}, namespace='urn:brocade.com:mgmt:brocade-rbridge-lag', defining_module='brocade-rbridge-lag', yang_type='container', is_config=True)""",
        })

    self.__ipv6 = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_ipv6(self):
    self.__ipv6 = YANGDynClass(base=ipv6.ipv6, is_container='container', yang_name="ipv6", rest_name="ipv6", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'info': u'ipv6 <ipv6-src-l4-port> <ipv6-dst-l4-port> <ipv6-src-ip> <ipv6-dst-ip> <ipv6-next-hdr>'}}, namespace='urn:brocade.com:mgmt:brocade-rbridge-lag', defining_module='brocade-rbridge-lag', yang_type='container', is_config=True)


  def _get_mpls(self):
    """
    Getter method for mpls, mapped from YANG variable /load_balance_lag/load_balance/hash/mpls (container)
    """
    return self.__mpls
      
  def _set_mpls(self, v, load=False):
    """
    Setter method for mpls, mapped from YANG variable /load_balance_lag/load_balance/hash/mpls (container)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_mpls is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_mpls() directly.
    """
    if hasattr(v, "_utype"):
      v = v._utype(v)
    try:
      t = YANGDynClass(v,base=mpls.mpls, is_container='container', yang_name="mpls", rest_name="mpls", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'info': u'mpls <label1> <label2> <label3>'}}, namespace='urn:brocade.com:mgmt:brocade-rbridge-lag', defining_module='brocade-rbridge-lag', yang_type='container', is_config=True)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """mpls must be of a type compatible with container""",
          'defined-type': "container",
          'generated-type': """YANGDynClass(base=mpls.mpls, is_container='container', yang_name="mpls", rest_name="mpls", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'info': u'mpls <label1> <label2> <label3>'}}, namespace='urn:brocade.com:mgmt:brocade-rbridge-lag', defining_module='brocade-rbridge-lag', yang_type='container', is_config=True)""",
        })

    self.__mpls = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_mpls(self):
    self.__mpls = YANGDynClass(base=mpls.mpls, is_container='container', yang_name="mpls", rest_name="mpls", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'info': u'mpls <label1> <label2> <label3>'}}, namespace='urn:brocade.com:mgmt:brocade-rbridge-lag', defining_module='brocade-rbridge-lag', yang_type='container', is_config=True)

  ethernet = __builtin__.property(_get_ethernet, _set_ethernet)
  ip = __builtin__.property(_get_ip, _set_ip)
  ipv6 = __builtin__.property(_get_ipv6, _set_ipv6)
  mpls = __builtin__.property(_get_mpls, _set_mpls)


  _pyangbind_elements = {'ethernet': ethernet, 'ip': ip, 'ipv6': ipv6, 'mpls': mpls, }


