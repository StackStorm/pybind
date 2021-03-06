
from operator import attrgetter
import pyangbind.lib.xpathhelper as xpathhelper
from pyangbind.lib.yangtypes import RestrictedPrecisionDecimalType, RestrictedClassType, TypedListType
from pyangbind.lib.yangtypes import YANGBool, YANGListType, YANGDynClass, ReferenceType
from pyangbind.lib.base import PybindBase
from decimal import Decimal
from bitarray import bitarray
import __builtin__
class listen_range(PybindBase):
  """
  This class was auto-generated by the PythonClass plugin for PYANG
  from YANG module brocade-rbridge - based on the path /rbridge-id/router/router-bgp/address-family/ipv4/ipv4-unicast/af-vrf/listen-range. Each member element of
  the container is represented as a class variable - with a specific
  YANG type.
  """
  __slots__ = ('_pybind_generated_by', '_path_helper', '_yang_name', '_rest_name', '_extmethods', '__listen_range_prefix','__peer_group','__limit',)

  _yang_name = 'listen-range'
  _rest_name = 'listen-range'

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
    self.__listen_range_prefix = YANGDynClass(base=RestrictedClassType(base_type=unicode, restriction_dict={'pattern': u'(([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])\\.){3}([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])/(([0-9])|([1-2][0-9])|(3[0-2]))'}), is_leaf=True, yang_name="listen-range-prefix", rest_name="listen-range-prefix", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'info': u'A.B.C.D/M IP address in dotted decimal/Mask'}}, is_keyval=True, namespace='urn:brocade.com:mgmt:brocade-bgp', defining_module='brocade-bgp', yang_type='inet:ipv4-prefix', is_config=True)
    self.__peer_group = YANGDynClass(base=RestrictedClassType(base_type=unicode, restriction_dict={'pattern': u'[a-zA-Z]{1}([-a-zA-Z0-9\\\\\\\\@#\\+\\*\\(\\)=\\{~\\}%<>=$_\\[\\]\\|]{0,62})'}), is_leaf=True, yang_name="peer-group", rest_name="peer-group", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'info': u'Peer group name', u'cli-expose-key-name': None}}, is_keyval=True, namespace='urn:brocade.com:mgmt:brocade-bgp', defining_module='brocade-bgp', yang_type='bgp-peergroup', is_config=True)
    self.__limit = YANGDynClass(base=RestrictedClassType(base_type=RestrictedClassType(base_type=long, restriction_dict={'range': ['0..4294967295']}, int_size=32), restriction_dict={'range': [u'1..255']}), is_leaf=True, yang_name="limit", rest_name="limit", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'info': u'Limit the neighbor'}}, namespace='urn:brocade.com:mgmt:brocade-bgp', defining_module='brocade-bgp', yang_type='listen-limit-type', is_config=True)

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
      return [u'rbridge-id', u'router', u'router-bgp', u'address-family', u'ipv4', u'ipv4-unicast', u'af-vrf', u'listen-range']

  def _rest_path(self):
    if hasattr(self, "_parent"):
      if self._rest_name:
        return self._parent._rest_path()+[self._rest_name]
      else:
        return self._parent._rest_path()
    else:
      return [u'rbridge-id', u'router', u'bgp', u'address-family', u'ipv4', u'unicast', u'vrf', u'listen-range']

  def _get_listen_range_prefix(self):
    """
    Getter method for listen_range_prefix, mapped from YANG variable /rbridge_id/router/router_bgp/address_family/ipv4/ipv4_unicast/af_vrf/listen_range/listen_range_prefix (inet:ipv4-prefix)
    """
    return self.__listen_range_prefix
      
  def _set_listen_range_prefix(self, v, load=False):
    """
    Setter method for listen_range_prefix, mapped from YANG variable /rbridge_id/router/router_bgp/address_family/ipv4/ipv4_unicast/af_vrf/listen_range/listen_range_prefix (inet:ipv4-prefix)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_listen_range_prefix is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_listen_range_prefix() directly.
    """
    parent = getattr(self, "_parent", None)
    if parent is not None and load is False:
      raise AttributeError("Cannot set keys directly when" +
                             " within an instantiated list")

    if hasattr(v, "_utype"):
      v = v._utype(v)
    try:
      t = YANGDynClass(v,base=RestrictedClassType(base_type=unicode, restriction_dict={'pattern': u'(([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])\\.){3}([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])/(([0-9])|([1-2][0-9])|(3[0-2]))'}), is_leaf=True, yang_name="listen-range-prefix", rest_name="listen-range-prefix", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'info': u'A.B.C.D/M IP address in dotted decimal/Mask'}}, is_keyval=True, namespace='urn:brocade.com:mgmt:brocade-bgp', defining_module='brocade-bgp', yang_type='inet:ipv4-prefix', is_config=True)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """listen_range_prefix must be of a type compatible with inet:ipv4-prefix""",
          'defined-type': "inet:ipv4-prefix",
          'generated-type': """YANGDynClass(base=RestrictedClassType(base_type=unicode, restriction_dict={'pattern': u'(([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])\\.){3}([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])/(([0-9])|([1-2][0-9])|(3[0-2]))'}), is_leaf=True, yang_name="listen-range-prefix", rest_name="listen-range-prefix", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'info': u'A.B.C.D/M IP address in dotted decimal/Mask'}}, is_keyval=True, namespace='urn:brocade.com:mgmt:brocade-bgp', defining_module='brocade-bgp', yang_type='inet:ipv4-prefix', is_config=True)""",
        })

    self.__listen_range_prefix = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_listen_range_prefix(self):
    self.__listen_range_prefix = YANGDynClass(base=RestrictedClassType(base_type=unicode, restriction_dict={'pattern': u'(([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])\\.){3}([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])/(([0-9])|([1-2][0-9])|(3[0-2]))'}), is_leaf=True, yang_name="listen-range-prefix", rest_name="listen-range-prefix", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'info': u'A.B.C.D/M IP address in dotted decimal/Mask'}}, is_keyval=True, namespace='urn:brocade.com:mgmt:brocade-bgp', defining_module='brocade-bgp', yang_type='inet:ipv4-prefix', is_config=True)


  def _get_peer_group(self):
    """
    Getter method for peer_group, mapped from YANG variable /rbridge_id/router/router_bgp/address_family/ipv4/ipv4_unicast/af_vrf/listen_range/peer_group (bgp-peergroup)
    """
    return self.__peer_group
      
  def _set_peer_group(self, v, load=False):
    """
    Setter method for peer_group, mapped from YANG variable /rbridge_id/router/router_bgp/address_family/ipv4/ipv4_unicast/af_vrf/listen_range/peer_group (bgp-peergroup)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_peer_group is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_peer_group() directly.
    """
    parent = getattr(self, "_parent", None)
    if parent is not None and load is False:
      raise AttributeError("Cannot set keys directly when" +
                             " within an instantiated list")

    if hasattr(v, "_utype"):
      v = v._utype(v)
    try:
      t = YANGDynClass(v,base=RestrictedClassType(base_type=unicode, restriction_dict={'pattern': u'[a-zA-Z]{1}([-a-zA-Z0-9\\\\\\\\@#\\+\\*\\(\\)=\\{~\\}%<>=$_\\[\\]\\|]{0,62})'}), is_leaf=True, yang_name="peer-group", rest_name="peer-group", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'info': u'Peer group name', u'cli-expose-key-name': None}}, is_keyval=True, namespace='urn:brocade.com:mgmt:brocade-bgp', defining_module='brocade-bgp', yang_type='bgp-peergroup', is_config=True)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """peer_group must be of a type compatible with bgp-peergroup""",
          'defined-type': "brocade-bgp:bgp-peergroup",
          'generated-type': """YANGDynClass(base=RestrictedClassType(base_type=unicode, restriction_dict={'pattern': u'[a-zA-Z]{1}([-a-zA-Z0-9\\\\\\\\@#\\+\\*\\(\\)=\\{~\\}%<>=$_\\[\\]\\|]{0,62})'}), is_leaf=True, yang_name="peer-group", rest_name="peer-group", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'info': u'Peer group name', u'cli-expose-key-name': None}}, is_keyval=True, namespace='urn:brocade.com:mgmt:brocade-bgp', defining_module='brocade-bgp', yang_type='bgp-peergroup', is_config=True)""",
        })

    self.__peer_group = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_peer_group(self):
    self.__peer_group = YANGDynClass(base=RestrictedClassType(base_type=unicode, restriction_dict={'pattern': u'[a-zA-Z]{1}([-a-zA-Z0-9\\\\\\\\@#\\+\\*\\(\\)=\\{~\\}%<>=$_\\[\\]\\|]{0,62})'}), is_leaf=True, yang_name="peer-group", rest_name="peer-group", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'info': u'Peer group name', u'cli-expose-key-name': None}}, is_keyval=True, namespace='urn:brocade.com:mgmt:brocade-bgp', defining_module='brocade-bgp', yang_type='bgp-peergroup', is_config=True)


  def _get_limit(self):
    """
    Getter method for limit, mapped from YANG variable /rbridge_id/router/router_bgp/address_family/ipv4/ipv4_unicast/af_vrf/listen_range/limit (listen-limit-type)
    """
    return self.__limit
      
  def _set_limit(self, v, load=False):
    """
    Setter method for limit, mapped from YANG variable /rbridge_id/router/router_bgp/address_family/ipv4/ipv4_unicast/af_vrf/listen_range/limit (listen-limit-type)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_limit is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_limit() directly.
    """
    if hasattr(v, "_utype"):
      v = v._utype(v)
    try:
      t = YANGDynClass(v,base=RestrictedClassType(base_type=RestrictedClassType(base_type=long, restriction_dict={'range': ['0..4294967295']}, int_size=32), restriction_dict={'range': [u'1..255']}), is_leaf=True, yang_name="limit", rest_name="limit", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'info': u'Limit the neighbor'}}, namespace='urn:brocade.com:mgmt:brocade-bgp', defining_module='brocade-bgp', yang_type='listen-limit-type', is_config=True)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """limit must be of a type compatible with listen-limit-type""",
          'defined-type': "brocade-bgp:listen-limit-type",
          'generated-type': """YANGDynClass(base=RestrictedClassType(base_type=RestrictedClassType(base_type=long, restriction_dict={'range': ['0..4294967295']}, int_size=32), restriction_dict={'range': [u'1..255']}), is_leaf=True, yang_name="limit", rest_name="limit", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'info': u'Limit the neighbor'}}, namespace='urn:brocade.com:mgmt:brocade-bgp', defining_module='brocade-bgp', yang_type='listen-limit-type', is_config=True)""",
        })

    self.__limit = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_limit(self):
    self.__limit = YANGDynClass(base=RestrictedClassType(base_type=RestrictedClassType(base_type=long, restriction_dict={'range': ['0..4294967295']}, int_size=32), restriction_dict={'range': [u'1..255']}), is_leaf=True, yang_name="limit", rest_name="limit", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'info': u'Limit the neighbor'}}, namespace='urn:brocade.com:mgmt:brocade-bgp', defining_module='brocade-bgp', yang_type='listen-limit-type', is_config=True)

  listen_range_prefix = __builtin__.property(_get_listen_range_prefix, _set_listen_range_prefix)
  peer_group = __builtin__.property(_get_peer_group, _set_peer_group)
  limit = __builtin__.property(_get_limit, _set_limit)


  _pyangbind_elements = {'listen_range_prefix': listen_range_prefix, 'peer_group': peer_group, 'limit': limit, }


