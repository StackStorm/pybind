
from operator import attrgetter
import pyangbind.lib.xpathhelper as xpathhelper
from pyangbind.lib.yangtypes import RestrictedPrecisionDecimalType, RestrictedClassType, TypedListType
from pyangbind.lib.yangtypes import YANGBool, YANGListType, YANGDynClass, ReferenceType
from pyangbind.lib.base import PybindBase
from decimal import Decimal
from bitarray import bitarray
import __builtin__
import authentication_key
import authentication
import md5_authentication
class virtual_link(PybindBase):
  """
  This class was auto-generated by the PythonClass plugin for PYANG
  from YANG module brocade-common-def - based on the path /routing-system/router/ospf/area/virtual-link. Each member element of
  the container is represented as a class variable - with a specific
  YANG type.
  """
  __slots__ = ('_pybind_generated_by', '_path_helper', '_yang_name', '_rest_name', '_extmethods', '__virt_link_neighbor','__authentication_key','__authentication','__hello_interval','__dead_interval','__retransmit_interval','__transmit_delay','__md5_authentication',)

  _yang_name = 'virtual-link'
  _rest_name = 'virtual-link'

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
    self.__retransmit_interval = YANGDynClass(base=RestrictedClassType(base_type=RestrictedClassType(base_type=long, restriction_dict={'range': ['0..4294967295']}, int_size=32), restriction_dict={'range': [u'0..3600']}), is_leaf=True, yang_name="retransmit-interval", rest_name="retransmit-interval", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'cli-full-command': None, u'info': u'Time between retransmitting lost link state\n   advertisements'}}, namespace='urn:brocade.com:mgmt:brocade-ospf', defining_module='brocade-ospf', yang_type='common-def:time-interval-sec', is_config=True)
    self.__md5_authentication = YANGDynClass(base=md5_authentication.md5_authentication, is_container='container', presence=False, yang_name="md5-authentication", rest_name="md5-authentication", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'info': u'MD5 authentication parameters', u'cli-incomplete-no': None, u'cli-incomplete-command': None}}, namespace='urn:brocade.com:mgmt:brocade-ospf', defining_module='brocade-ospf', yang_type='container', is_config=True)
    self.__authentication = YANGDynClass(base=authentication.authentication, is_container='container', presence=False, yang_name="authentication", rest_name="authentication", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'info': u'Authentication of OSPF messages', u'cli-incomplete-no': None, u'cli-incomplete-command': None}}, namespace='urn:brocade.com:mgmt:brocade-ospf', defining_module='brocade-ospf', yang_type='container', is_config=True)
    self.__dead_interval = YANGDynClass(base=RestrictedClassType(base_type=RestrictedClassType(base_type=long, restriction_dict={'range': ['0..4294967295']}, int_size=32), restriction_dict={'range': [u'3..65535']}), default=RestrictedClassType(base_type=long, restriction_dict={'range': ['0..4294967295']}, int_size=32)(40), is_leaf=True, yang_name="dead-interval", rest_name="dead-interval", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'cli-full-command': None, u'info': u'Interval after which a neighbor is declared dead'}}, namespace='urn:brocade.com:mgmt:brocade-ospf', defining_module='brocade-ospf', yang_type='common-def:time-interval-sec', is_config=True)
    self.__hello_interval = YANGDynClass(base=RestrictedClassType(base_type=RestrictedClassType(base_type=long, restriction_dict={'range': ['0..4294967295']}, int_size=32), restriction_dict={'range': [u'1..65535']}), default=RestrictedClassType(base_type=long, restriction_dict={'range': ['0..4294967295']}, int_size=32)(10), is_leaf=True, yang_name="hello-interval", rest_name="hello-interval", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'cli-full-command': None, u'info': u'Time between HELLO packets'}}, namespace='urn:brocade.com:mgmt:brocade-ospf', defining_module='brocade-ospf', yang_type='common-def:time-interval-sec', is_config=True)
    self.__authentication_key = YANGDynClass(base=authentication_key.authentication_key, is_container='container', presence=False, yang_name="authentication-key", rest_name="authentication-key", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'info': u'Authentication password (key)', u'cli-full-no': None, u'cli-incomplete-command': None}}, namespace='urn:brocade.com:mgmt:brocade-ospf', defining_module='brocade-ospf', yang_type='container', is_config=True)
    self.__virt_link_neighbor = YANGDynClass(base=RestrictedClassType(base_type=unicode, restriction_dict={'pattern': u'(([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])\\.){3}([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])(%[\\p{N}\\p{L}]+)?'}), is_leaf=True, yang_name="virt-link-neighbor", rest_name="virt-link-neighbor", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, is_keyval=True, namespace='urn:brocade.com:mgmt:brocade-ospf', defining_module='brocade-ospf', yang_type='inet:ipv4-address', is_config=True)
    self.__transmit_delay = YANGDynClass(base=RestrictedClassType(base_type=RestrictedClassType(base_type=long, restriction_dict={'range': ['0..4294967295']}, int_size=32), restriction_dict={'range': [u'0..3600']}), is_leaf=True, yang_name="transmit-delay", rest_name="transmit-delay", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'cli-full-command': None, u'info': u'Link state transmit delay'}}, namespace='urn:brocade.com:mgmt:brocade-ospf', defining_module='brocade-ospf', yang_type='common-def:time-interval-sec', is_config=True)

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
      return [u'routing-system', u'router', u'ospf', u'area', u'virtual-link']

  def _rest_path(self):
    if hasattr(self, "_parent"):
      if self._rest_name:
        return self._parent._rest_path()+[self._rest_name]
      else:
        return self._parent._rest_path()
    else:
      return [u'router', u'ospf', u'area', u'virtual-link']

  def _get_virt_link_neighbor(self):
    """
    Getter method for virt_link_neighbor, mapped from YANG variable /routing_system/router/ospf/area/virtual_link/virt_link_neighbor (inet:ipv4-address)
    """
    return self.__virt_link_neighbor
      
  def _set_virt_link_neighbor(self, v, load=False):
    """
    Setter method for virt_link_neighbor, mapped from YANG variable /routing_system/router/ospf/area/virtual_link/virt_link_neighbor (inet:ipv4-address)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_virt_link_neighbor is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_virt_link_neighbor() directly.
    """
    parent = getattr(self, "_parent", None)
    if parent is not None and load is False:
      raise AttributeError("Cannot set keys directly when" +
                             " within an instantiated list")

    if hasattr(v, "_utype"):
      v = v._utype(v)
    try:
      t = YANGDynClass(v,base=RestrictedClassType(base_type=unicode, restriction_dict={'pattern': u'(([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])\\.){3}([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])(%[\\p{N}\\p{L}]+)?'}), is_leaf=True, yang_name="virt-link-neighbor", rest_name="virt-link-neighbor", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, is_keyval=True, namespace='urn:brocade.com:mgmt:brocade-ospf', defining_module='brocade-ospf', yang_type='inet:ipv4-address', is_config=True)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """virt_link_neighbor must be of a type compatible with inet:ipv4-address""",
          'defined-type': "inet:ipv4-address",
          'generated-type': """YANGDynClass(base=RestrictedClassType(base_type=unicode, restriction_dict={'pattern': u'(([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])\\.){3}([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])(%[\\p{N}\\p{L}]+)?'}), is_leaf=True, yang_name="virt-link-neighbor", rest_name="virt-link-neighbor", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, is_keyval=True, namespace='urn:brocade.com:mgmt:brocade-ospf', defining_module='brocade-ospf', yang_type='inet:ipv4-address', is_config=True)""",
        })

    self.__virt_link_neighbor = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_virt_link_neighbor(self):
    self.__virt_link_neighbor = YANGDynClass(base=RestrictedClassType(base_type=unicode, restriction_dict={'pattern': u'(([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])\\.){3}([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])(%[\\p{N}\\p{L}]+)?'}), is_leaf=True, yang_name="virt-link-neighbor", rest_name="virt-link-neighbor", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, is_keyval=True, namespace='urn:brocade.com:mgmt:brocade-ospf', defining_module='brocade-ospf', yang_type='inet:ipv4-address', is_config=True)


  def _get_authentication_key(self):
    """
    Getter method for authentication_key, mapped from YANG variable /routing_system/router/ospf/area/virtual_link/authentication_key (container)
    """
    return self.__authentication_key
      
  def _set_authentication_key(self, v, load=False):
    """
    Setter method for authentication_key, mapped from YANG variable /routing_system/router/ospf/area/virtual_link/authentication_key (container)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_authentication_key is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_authentication_key() directly.
    """
    if hasattr(v, "_utype"):
      v = v._utype(v)
    try:
      t = YANGDynClass(v,base=authentication_key.authentication_key, is_container='container', presence=False, yang_name="authentication-key", rest_name="authentication-key", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'info': u'Authentication password (key)', u'cli-full-no': None, u'cli-incomplete-command': None}}, namespace='urn:brocade.com:mgmt:brocade-ospf', defining_module='brocade-ospf', yang_type='container', is_config=True)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """authentication_key must be of a type compatible with container""",
          'defined-type': "container",
          'generated-type': """YANGDynClass(base=authentication_key.authentication_key, is_container='container', presence=False, yang_name="authentication-key", rest_name="authentication-key", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'info': u'Authentication password (key)', u'cli-full-no': None, u'cli-incomplete-command': None}}, namespace='urn:brocade.com:mgmt:brocade-ospf', defining_module='brocade-ospf', yang_type='container', is_config=True)""",
        })

    self.__authentication_key = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_authentication_key(self):
    self.__authentication_key = YANGDynClass(base=authentication_key.authentication_key, is_container='container', presence=False, yang_name="authentication-key", rest_name="authentication-key", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'info': u'Authentication password (key)', u'cli-full-no': None, u'cli-incomplete-command': None}}, namespace='urn:brocade.com:mgmt:brocade-ospf', defining_module='brocade-ospf', yang_type='container', is_config=True)


  def _get_authentication(self):
    """
    Getter method for authentication, mapped from YANG variable /routing_system/router/ospf/area/virtual_link/authentication (container)

    YANG Description: Authentication of OSPF messages
    """
    return self.__authentication
      
  def _set_authentication(self, v, load=False):
    """
    Setter method for authentication, mapped from YANG variable /routing_system/router/ospf/area/virtual_link/authentication (container)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_authentication is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_authentication() directly.

    YANG Description: Authentication of OSPF messages
    """
    if hasattr(v, "_utype"):
      v = v._utype(v)
    try:
      t = YANGDynClass(v,base=authentication.authentication, is_container='container', presence=False, yang_name="authentication", rest_name="authentication", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'info': u'Authentication of OSPF messages', u'cli-incomplete-no': None, u'cli-incomplete-command': None}}, namespace='urn:brocade.com:mgmt:brocade-ospf', defining_module='brocade-ospf', yang_type='container', is_config=True)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """authentication must be of a type compatible with container""",
          'defined-type': "container",
          'generated-type': """YANGDynClass(base=authentication.authentication, is_container='container', presence=False, yang_name="authentication", rest_name="authentication", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'info': u'Authentication of OSPF messages', u'cli-incomplete-no': None, u'cli-incomplete-command': None}}, namespace='urn:brocade.com:mgmt:brocade-ospf', defining_module='brocade-ospf', yang_type='container', is_config=True)""",
        })

    self.__authentication = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_authentication(self):
    self.__authentication = YANGDynClass(base=authentication.authentication, is_container='container', presence=False, yang_name="authentication", rest_name="authentication", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'info': u'Authentication of OSPF messages', u'cli-incomplete-no': None, u'cli-incomplete-command': None}}, namespace='urn:brocade.com:mgmt:brocade-ospf', defining_module='brocade-ospf', yang_type='container', is_config=True)


  def _get_hello_interval(self):
    """
    Getter method for hello_interval, mapped from YANG variable /routing_system/router/ospf/area/virtual_link/hello_interval (common-def:time-interval-sec)
    """
    return self.__hello_interval
      
  def _set_hello_interval(self, v, load=False):
    """
    Setter method for hello_interval, mapped from YANG variable /routing_system/router/ospf/area/virtual_link/hello_interval (common-def:time-interval-sec)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_hello_interval is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_hello_interval() directly.
    """
    if hasattr(v, "_utype"):
      v = v._utype(v)
    try:
      t = YANGDynClass(v,base=RestrictedClassType(base_type=RestrictedClassType(base_type=long, restriction_dict={'range': ['0..4294967295']}, int_size=32), restriction_dict={'range': [u'1..65535']}), default=RestrictedClassType(base_type=long, restriction_dict={'range': ['0..4294967295']}, int_size=32)(10), is_leaf=True, yang_name="hello-interval", rest_name="hello-interval", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'cli-full-command': None, u'info': u'Time between HELLO packets'}}, namespace='urn:brocade.com:mgmt:brocade-ospf', defining_module='brocade-ospf', yang_type='common-def:time-interval-sec', is_config=True)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """hello_interval must be of a type compatible with common-def:time-interval-sec""",
          'defined-type': "common-def:time-interval-sec",
          'generated-type': """YANGDynClass(base=RestrictedClassType(base_type=RestrictedClassType(base_type=long, restriction_dict={'range': ['0..4294967295']}, int_size=32), restriction_dict={'range': [u'1..65535']}), default=RestrictedClassType(base_type=long, restriction_dict={'range': ['0..4294967295']}, int_size=32)(10), is_leaf=True, yang_name="hello-interval", rest_name="hello-interval", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'cli-full-command': None, u'info': u'Time between HELLO packets'}}, namespace='urn:brocade.com:mgmt:brocade-ospf', defining_module='brocade-ospf', yang_type='common-def:time-interval-sec', is_config=True)""",
        })

    self.__hello_interval = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_hello_interval(self):
    self.__hello_interval = YANGDynClass(base=RestrictedClassType(base_type=RestrictedClassType(base_type=long, restriction_dict={'range': ['0..4294967295']}, int_size=32), restriction_dict={'range': [u'1..65535']}), default=RestrictedClassType(base_type=long, restriction_dict={'range': ['0..4294967295']}, int_size=32)(10), is_leaf=True, yang_name="hello-interval", rest_name="hello-interval", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'cli-full-command': None, u'info': u'Time between HELLO packets'}}, namespace='urn:brocade.com:mgmt:brocade-ospf', defining_module='brocade-ospf', yang_type='common-def:time-interval-sec', is_config=True)


  def _get_dead_interval(self):
    """
    Getter method for dead_interval, mapped from YANG variable /routing_system/router/ospf/area/virtual_link/dead_interval (common-def:time-interval-sec)
    """
    return self.__dead_interval
      
  def _set_dead_interval(self, v, load=False):
    """
    Setter method for dead_interval, mapped from YANG variable /routing_system/router/ospf/area/virtual_link/dead_interval (common-def:time-interval-sec)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_dead_interval is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_dead_interval() directly.
    """
    if hasattr(v, "_utype"):
      v = v._utype(v)
    try:
      t = YANGDynClass(v,base=RestrictedClassType(base_type=RestrictedClassType(base_type=long, restriction_dict={'range': ['0..4294967295']}, int_size=32), restriction_dict={'range': [u'3..65535']}), default=RestrictedClassType(base_type=long, restriction_dict={'range': ['0..4294967295']}, int_size=32)(40), is_leaf=True, yang_name="dead-interval", rest_name="dead-interval", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'cli-full-command': None, u'info': u'Interval after which a neighbor is declared dead'}}, namespace='urn:brocade.com:mgmt:brocade-ospf', defining_module='brocade-ospf', yang_type='common-def:time-interval-sec', is_config=True)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """dead_interval must be of a type compatible with common-def:time-interval-sec""",
          'defined-type': "common-def:time-interval-sec",
          'generated-type': """YANGDynClass(base=RestrictedClassType(base_type=RestrictedClassType(base_type=long, restriction_dict={'range': ['0..4294967295']}, int_size=32), restriction_dict={'range': [u'3..65535']}), default=RestrictedClassType(base_type=long, restriction_dict={'range': ['0..4294967295']}, int_size=32)(40), is_leaf=True, yang_name="dead-interval", rest_name="dead-interval", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'cli-full-command': None, u'info': u'Interval after which a neighbor is declared dead'}}, namespace='urn:brocade.com:mgmt:brocade-ospf', defining_module='brocade-ospf', yang_type='common-def:time-interval-sec', is_config=True)""",
        })

    self.__dead_interval = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_dead_interval(self):
    self.__dead_interval = YANGDynClass(base=RestrictedClassType(base_type=RestrictedClassType(base_type=long, restriction_dict={'range': ['0..4294967295']}, int_size=32), restriction_dict={'range': [u'3..65535']}), default=RestrictedClassType(base_type=long, restriction_dict={'range': ['0..4294967295']}, int_size=32)(40), is_leaf=True, yang_name="dead-interval", rest_name="dead-interval", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'cli-full-command': None, u'info': u'Interval after which a neighbor is declared dead'}}, namespace='urn:brocade.com:mgmt:brocade-ospf', defining_module='brocade-ospf', yang_type='common-def:time-interval-sec', is_config=True)


  def _get_retransmit_interval(self):
    """
    Getter method for retransmit_interval, mapped from YANG variable /routing_system/router/ospf/area/virtual_link/retransmit_interval (common-def:time-interval-sec)
    """
    return self.__retransmit_interval
      
  def _set_retransmit_interval(self, v, load=False):
    """
    Setter method for retransmit_interval, mapped from YANG variable /routing_system/router/ospf/area/virtual_link/retransmit_interval (common-def:time-interval-sec)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_retransmit_interval is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_retransmit_interval() directly.
    """
    if hasattr(v, "_utype"):
      v = v._utype(v)
    try:
      t = YANGDynClass(v,base=RestrictedClassType(base_type=RestrictedClassType(base_type=long, restriction_dict={'range': ['0..4294967295']}, int_size=32), restriction_dict={'range': [u'0..3600']}), is_leaf=True, yang_name="retransmit-interval", rest_name="retransmit-interval", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'cli-full-command': None, u'info': u'Time between retransmitting lost link state\n   advertisements'}}, namespace='urn:brocade.com:mgmt:brocade-ospf', defining_module='brocade-ospf', yang_type='common-def:time-interval-sec', is_config=True)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """retransmit_interval must be of a type compatible with common-def:time-interval-sec""",
          'defined-type': "common-def:time-interval-sec",
          'generated-type': """YANGDynClass(base=RestrictedClassType(base_type=RestrictedClassType(base_type=long, restriction_dict={'range': ['0..4294967295']}, int_size=32), restriction_dict={'range': [u'0..3600']}), is_leaf=True, yang_name="retransmit-interval", rest_name="retransmit-interval", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'cli-full-command': None, u'info': u'Time between retransmitting lost link state\n   advertisements'}}, namespace='urn:brocade.com:mgmt:brocade-ospf', defining_module='brocade-ospf', yang_type='common-def:time-interval-sec', is_config=True)""",
        })

    self.__retransmit_interval = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_retransmit_interval(self):
    self.__retransmit_interval = YANGDynClass(base=RestrictedClassType(base_type=RestrictedClassType(base_type=long, restriction_dict={'range': ['0..4294967295']}, int_size=32), restriction_dict={'range': [u'0..3600']}), is_leaf=True, yang_name="retransmit-interval", rest_name="retransmit-interval", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'cli-full-command': None, u'info': u'Time between retransmitting lost link state\n   advertisements'}}, namespace='urn:brocade.com:mgmt:brocade-ospf', defining_module='brocade-ospf', yang_type='common-def:time-interval-sec', is_config=True)


  def _get_transmit_delay(self):
    """
    Getter method for transmit_delay, mapped from YANG variable /routing_system/router/ospf/area/virtual_link/transmit_delay (common-def:time-interval-sec)
    """
    return self.__transmit_delay
      
  def _set_transmit_delay(self, v, load=False):
    """
    Setter method for transmit_delay, mapped from YANG variable /routing_system/router/ospf/area/virtual_link/transmit_delay (common-def:time-interval-sec)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_transmit_delay is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_transmit_delay() directly.
    """
    if hasattr(v, "_utype"):
      v = v._utype(v)
    try:
      t = YANGDynClass(v,base=RestrictedClassType(base_type=RestrictedClassType(base_type=long, restriction_dict={'range': ['0..4294967295']}, int_size=32), restriction_dict={'range': [u'0..3600']}), is_leaf=True, yang_name="transmit-delay", rest_name="transmit-delay", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'cli-full-command': None, u'info': u'Link state transmit delay'}}, namespace='urn:brocade.com:mgmt:brocade-ospf', defining_module='brocade-ospf', yang_type='common-def:time-interval-sec', is_config=True)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """transmit_delay must be of a type compatible with common-def:time-interval-sec""",
          'defined-type': "common-def:time-interval-sec",
          'generated-type': """YANGDynClass(base=RestrictedClassType(base_type=RestrictedClassType(base_type=long, restriction_dict={'range': ['0..4294967295']}, int_size=32), restriction_dict={'range': [u'0..3600']}), is_leaf=True, yang_name="transmit-delay", rest_name="transmit-delay", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'cli-full-command': None, u'info': u'Link state transmit delay'}}, namespace='urn:brocade.com:mgmt:brocade-ospf', defining_module='brocade-ospf', yang_type='common-def:time-interval-sec', is_config=True)""",
        })

    self.__transmit_delay = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_transmit_delay(self):
    self.__transmit_delay = YANGDynClass(base=RestrictedClassType(base_type=RestrictedClassType(base_type=long, restriction_dict={'range': ['0..4294967295']}, int_size=32), restriction_dict={'range': [u'0..3600']}), is_leaf=True, yang_name="transmit-delay", rest_name="transmit-delay", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'cli-full-command': None, u'info': u'Link state transmit delay'}}, namespace='urn:brocade.com:mgmt:brocade-ospf', defining_module='brocade-ospf', yang_type='common-def:time-interval-sec', is_config=True)


  def _get_md5_authentication(self):
    """
    Getter method for md5_authentication, mapped from YANG variable /routing_system/router/ospf/area/virtual_link/md5_authentication (container)
    """
    return self.__md5_authentication
      
  def _set_md5_authentication(self, v, load=False):
    """
    Setter method for md5_authentication, mapped from YANG variable /routing_system/router/ospf/area/virtual_link/md5_authentication (container)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_md5_authentication is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_md5_authentication() directly.
    """
    if hasattr(v, "_utype"):
      v = v._utype(v)
    try:
      t = YANGDynClass(v,base=md5_authentication.md5_authentication, is_container='container', presence=False, yang_name="md5-authentication", rest_name="md5-authentication", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'info': u'MD5 authentication parameters', u'cli-incomplete-no': None, u'cli-incomplete-command': None}}, namespace='urn:brocade.com:mgmt:brocade-ospf', defining_module='brocade-ospf', yang_type='container', is_config=True)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """md5_authentication must be of a type compatible with container""",
          'defined-type': "container",
          'generated-type': """YANGDynClass(base=md5_authentication.md5_authentication, is_container='container', presence=False, yang_name="md5-authentication", rest_name="md5-authentication", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'info': u'MD5 authentication parameters', u'cli-incomplete-no': None, u'cli-incomplete-command': None}}, namespace='urn:brocade.com:mgmt:brocade-ospf', defining_module='brocade-ospf', yang_type='container', is_config=True)""",
        })

    self.__md5_authentication = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_md5_authentication(self):
    self.__md5_authentication = YANGDynClass(base=md5_authentication.md5_authentication, is_container='container', presence=False, yang_name="md5-authentication", rest_name="md5-authentication", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'info': u'MD5 authentication parameters', u'cli-incomplete-no': None, u'cli-incomplete-command': None}}, namespace='urn:brocade.com:mgmt:brocade-ospf', defining_module='brocade-ospf', yang_type='container', is_config=True)

  virt_link_neighbor = __builtin__.property(_get_virt_link_neighbor, _set_virt_link_neighbor)
  authentication_key = __builtin__.property(_get_authentication_key, _set_authentication_key)
  authentication = __builtin__.property(_get_authentication, _set_authentication)
  hello_interval = __builtin__.property(_get_hello_interval, _set_hello_interval)
  dead_interval = __builtin__.property(_get_dead_interval, _set_dead_interval)
  retransmit_interval = __builtin__.property(_get_retransmit_interval, _set_retransmit_interval)
  transmit_delay = __builtin__.property(_get_transmit_delay, _set_transmit_delay)
  md5_authentication = __builtin__.property(_get_md5_authentication, _set_md5_authentication)


  _pyangbind_elements = {'virt_link_neighbor': virt_link_neighbor, 'authentication_key': authentication_key, 'authentication': authentication, 'hello_interval': hello_interval, 'dead_interval': dead_interval, 'retransmit_interval': retransmit_interval, 'transmit_delay': transmit_delay, 'md5_authentication': md5_authentication, }


