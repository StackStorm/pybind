
from operator import attrgetter
import pyangbind.lib.xpathhelper as xpathhelper
from pyangbind.lib.yangtypes import RestrictedPrecisionDecimalType, RestrictedClassType, TypedListType
from pyangbind.lib.yangtypes import YANGBool, YANGListType, YANGDynClass, ReferenceType
from pyangbind.lib.base import PybindBase
from decimal import Decimal
from bitarray import bitarray
import __builtin__
class session(PybindBase):
  """
  This class was auto-generated by the PythonClass plugin for PYANG
  from YANG module brocade-netconf-ext - based on the path /brocade_netconf_ext_rpc/get-netconf-client-capabilities/output/session. Each member element of
  the container is represented as a class variable - with a specific
  YANG type.
  """
  __slots__ = ('_pybind_generated_by', '_path_helper', '_yang_name', '_extmethods', '__session_id','__user_name','__vendor','__product','__version','__identity','__af_type','__host_ip_v6','__host_ip','__time',)

  _yang_name = 'session'

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
    self.__product = YANGDynClass(base=unicode, is_leaf=True, yang_name="product", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=False, namespace='urn:brocade.com:mgmt:brocade-netconf-ext', defining_module='brocade-netconf-ext', yang_type='string', is_config=True)
    self.__host_ip_v6 = YANGDynClass(base=RestrictedClassType(base_type=unicode, restriction_dict={'pattern': u'((:|[0-9a-fA-F]{0,4}):)([0-9a-fA-F]{0,4}:){0,5}((([0-9a-fA-F]{0,4}:)?(:|[0-9a-fA-F]{0,4}))|(((25[0-5]|2[0-4][0-9]|[01]?[0-9]?[0-9])\\.){3}(25[0-5]|2[0-4][0-9]|[01]?[0-9]?[0-9])))(%[\\p{N}\\p{L}]+)?'}), is_leaf=True, yang_name="host-ip-v6", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=False, namespace='urn:brocade.com:mgmt:brocade-netconf-ext', defining_module='brocade-netconf-ext', yang_type='inet:ipv6-address', is_config=True)
    self.__vendor = YANGDynClass(base=unicode, is_leaf=True, yang_name="vendor", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=False, namespace='urn:brocade.com:mgmt:brocade-netconf-ext', defining_module='brocade-netconf-ext', yang_type='string', is_config=True)
    self.__host_ip = YANGDynClass(base=RestrictedClassType(base_type=unicode, restriction_dict={'pattern': u'(([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])\\.){3}([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])(%[\\p{N}\\p{L}]+)?'}), is_leaf=True, yang_name="host-ip", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=False, namespace='urn:brocade.com:mgmt:brocade-netconf-ext', defining_module='brocade-netconf-ext', yang_type='inet:ipv4-address', is_config=True)
    self.__session_id = YANGDynClass(base=RestrictedClassType(base_type=long, restriction_dict={'range': ['0..4294967295']}, int_size=32), is_leaf=True, yang_name="session-id", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=False, namespace='urn:brocade.com:mgmt:brocade-netconf-ext', defining_module='brocade-netconf-ext', yang_type='uint32', is_config=True)
    self.__af_type = YANGDynClass(base=RestrictedClassType(base_type=unicode,                                     restriction_type="dict_key",                                     restriction_arg={u'IPV4': {'value': 2}, u'IPV6': {'value': 10}},), is_leaf=True, yang_name="af-type", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=False, namespace='urn:brocade.com:mgmt:brocade-netconf-ext', defining_module='brocade-netconf-ext', yang_type='enumeration', is_config=True)
    self.__version = YANGDynClass(base=unicode, is_leaf=True, yang_name="version", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=False, namespace='urn:brocade.com:mgmt:brocade-netconf-ext', defining_module='brocade-netconf-ext', yang_type='string', is_config=True)
    self.__time = YANGDynClass(base=RestrictedClassType(base_type=unicode, restriction_dict={'pattern': u'\\d{4}-\\d{2}-\\d{2}T\\d{2}:\\d{2}:\\d{2}(\\.\\d+)?(Z|[\\+\\-]\\d{2}:\\d{2})'}), is_leaf=True, yang_name="time", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=False, namespace='urn:brocade.com:mgmt:brocade-netconf-ext', defining_module='brocade-netconf-ext', yang_type='ietfyang:date-and-time', is_config=True)
    self.__user_name = YANGDynClass(base=unicode, is_leaf=True, yang_name="user-name", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=False, namespace='urn:brocade.com:mgmt:brocade-netconf-ext', defining_module='brocade-netconf-ext', yang_type='string', is_config=True)
    self.__identity = YANGDynClass(base=unicode, is_leaf=True, yang_name="identity", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=False, namespace='urn:brocade.com:mgmt:brocade-netconf-ext', defining_module='brocade-netconf-ext', yang_type='string', is_config=True)

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
      return [u'brocade_netconf_ext_rpc', u'get-netconf-client-capabilities', u'output', u'session']

  def _rest_path(self):
    if hasattr(self, "_supplied_register_path"):
      return [self._supplied_register_path]
    if hasattr(self, "_parent"):
      return self._parent._rest_path()+[self._yang_name]
    else:
      return [u'get-netconf-client-capabilities', u'output', u'session']

  def _get_session_id(self):
    """
    Getter method for session_id, mapped from YANG variable /brocade_netconf_ext_rpc/get_netconf_client_capabilities/output/session/session_id (uint32)

    YANG Description: Session Id of the NETCONF client session.
    """
    return self.__session_id
      
  def _set_session_id(self, v, load=False):
    """
    Setter method for session_id, mapped from YANG variable /brocade_netconf_ext_rpc/get_netconf_client_capabilities/output/session/session_id (uint32)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_session_id is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_session_id() directly.

    YANG Description: Session Id of the NETCONF client session.
    """
    try:
      t = YANGDynClass(v,base=RestrictedClassType(base_type=long, restriction_dict={'range': ['0..4294967295']}, int_size=32), is_leaf=True, yang_name="session-id", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=False, namespace='urn:brocade.com:mgmt:brocade-netconf-ext', defining_module='brocade-netconf-ext', yang_type='uint32', is_config=True)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """session_id must be of a type compatible with uint32""",
          'defined-type': "uint32",
          'generated-type': """YANGDynClass(base=RestrictedClassType(base_type=long, restriction_dict={'range': ['0..4294967295']}, int_size=32), is_leaf=True, yang_name="session-id", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=False, namespace='urn:brocade.com:mgmt:brocade-netconf-ext', defining_module='brocade-netconf-ext', yang_type='uint32', is_config=True)""",
        })

    self.__session_id = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_session_id(self):
    self.__session_id = YANGDynClass(base=RestrictedClassType(base_type=long, restriction_dict={'range': ['0..4294967295']}, int_size=32), is_leaf=True, yang_name="session-id", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=False, namespace='urn:brocade.com:mgmt:brocade-netconf-ext', defining_module='brocade-netconf-ext', yang_type='uint32', is_config=True)


  def _get_user_name(self):
    """
    Getter method for user_name, mapped from YANG variable /brocade_netconf_ext_rpc/get_netconf_client_capabilities/output/session/user_name (string)

    YANG Description: Login name of the user for the NETCONF client
session.
    """
    return self.__user_name
      
  def _set_user_name(self, v, load=False):
    """
    Setter method for user_name, mapped from YANG variable /brocade_netconf_ext_rpc/get_netconf_client_capabilities/output/session/user_name (string)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_user_name is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_user_name() directly.

    YANG Description: Login name of the user for the NETCONF client
session.
    """
    try:
      t = YANGDynClass(v,base=unicode, is_leaf=True, yang_name="user-name", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=False, namespace='urn:brocade.com:mgmt:brocade-netconf-ext', defining_module='brocade-netconf-ext', yang_type='string', is_config=True)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """user_name must be of a type compatible with string""",
          'defined-type': "string",
          'generated-type': """YANGDynClass(base=unicode, is_leaf=True, yang_name="user-name", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=False, namespace='urn:brocade.com:mgmt:brocade-netconf-ext', defining_module='brocade-netconf-ext', yang_type='string', is_config=True)""",
        })

    self.__user_name = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_user_name(self):
    self.__user_name = YANGDynClass(base=unicode, is_leaf=True, yang_name="user-name", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=False, namespace='urn:brocade.com:mgmt:brocade-netconf-ext', defining_module='brocade-netconf-ext', yang_type='string', is_config=True)


  def _get_vendor(self):
    """
    Getter method for vendor, mapped from YANG variable /brocade_netconf_ext_rpc/get_netconf_client_capabilities/output/session/vendor (string)

    YANG Description: Vendor name of the NETCONF client session.
    """
    return self.__vendor
      
  def _set_vendor(self, v, load=False):
    """
    Setter method for vendor, mapped from YANG variable /brocade_netconf_ext_rpc/get_netconf_client_capabilities/output/session/vendor (string)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_vendor is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_vendor() directly.

    YANG Description: Vendor name of the NETCONF client session.
    """
    try:
      t = YANGDynClass(v,base=unicode, is_leaf=True, yang_name="vendor", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=False, namespace='urn:brocade.com:mgmt:brocade-netconf-ext', defining_module='brocade-netconf-ext', yang_type='string', is_config=True)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """vendor must be of a type compatible with string""",
          'defined-type': "string",
          'generated-type': """YANGDynClass(base=unicode, is_leaf=True, yang_name="vendor", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=False, namespace='urn:brocade.com:mgmt:brocade-netconf-ext', defining_module='brocade-netconf-ext', yang_type='string', is_config=True)""",
        })

    self.__vendor = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_vendor(self):
    self.__vendor = YANGDynClass(base=unicode, is_leaf=True, yang_name="vendor", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=False, namespace='urn:brocade.com:mgmt:brocade-netconf-ext', defining_module='brocade-netconf-ext', yang_type='string', is_config=True)


  def _get_product(self):
    """
    Getter method for product, mapped from YANG variable /brocade_netconf_ext_rpc/get_netconf_client_capabilities/output/session/product (string)

    YANG Description: Product name of the NETCONF client session.
    """
    return self.__product
      
  def _set_product(self, v, load=False):
    """
    Setter method for product, mapped from YANG variable /brocade_netconf_ext_rpc/get_netconf_client_capabilities/output/session/product (string)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_product is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_product() directly.

    YANG Description: Product name of the NETCONF client session.
    """
    try:
      t = YANGDynClass(v,base=unicode, is_leaf=True, yang_name="product", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=False, namespace='urn:brocade.com:mgmt:brocade-netconf-ext', defining_module='brocade-netconf-ext', yang_type='string', is_config=True)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """product must be of a type compatible with string""",
          'defined-type': "string",
          'generated-type': """YANGDynClass(base=unicode, is_leaf=True, yang_name="product", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=False, namespace='urn:brocade.com:mgmt:brocade-netconf-ext', defining_module='brocade-netconf-ext', yang_type='string', is_config=True)""",
        })

    self.__product = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_product(self):
    self.__product = YANGDynClass(base=unicode, is_leaf=True, yang_name="product", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=False, namespace='urn:brocade.com:mgmt:brocade-netconf-ext', defining_module='brocade-netconf-ext', yang_type='string', is_config=True)


  def _get_version(self):
    """
    Getter method for version, mapped from YANG variable /brocade_netconf_ext_rpc/get_netconf_client_capabilities/output/session/version (string)

    YANG Description: Product version of the NETCONF client
session.
    """
    return self.__version
      
  def _set_version(self, v, load=False):
    """
    Setter method for version, mapped from YANG variable /brocade_netconf_ext_rpc/get_netconf_client_capabilities/output/session/version (string)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_version is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_version() directly.

    YANG Description: Product version of the NETCONF client
session.
    """
    try:
      t = YANGDynClass(v,base=unicode, is_leaf=True, yang_name="version", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=False, namespace='urn:brocade.com:mgmt:brocade-netconf-ext', defining_module='brocade-netconf-ext', yang_type='string', is_config=True)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """version must be of a type compatible with string""",
          'defined-type': "string",
          'generated-type': """YANGDynClass(base=unicode, is_leaf=True, yang_name="version", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=False, namespace='urn:brocade.com:mgmt:brocade-netconf-ext', defining_module='brocade-netconf-ext', yang_type='string', is_config=True)""",
        })

    self.__version = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_version(self):
    self.__version = YANGDynClass(base=unicode, is_leaf=True, yang_name="version", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=False, namespace='urn:brocade.com:mgmt:brocade-netconf-ext', defining_module='brocade-netconf-ext', yang_type='string', is_config=True)


  def _get_identity(self):
    """
    Getter method for identity, mapped from YANG variable /brocade_netconf_ext_rpc/get_netconf_client_capabilities/output/session/identity (string)

    YANG Description: Identity of the NETCONF client session.
    """
    return self.__identity
      
  def _set_identity(self, v, load=False):
    """
    Setter method for identity, mapped from YANG variable /brocade_netconf_ext_rpc/get_netconf_client_capabilities/output/session/identity (string)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_identity is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_identity() directly.

    YANG Description: Identity of the NETCONF client session.
    """
    try:
      t = YANGDynClass(v,base=unicode, is_leaf=True, yang_name="identity", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=False, namespace='urn:brocade.com:mgmt:brocade-netconf-ext', defining_module='brocade-netconf-ext', yang_type='string', is_config=True)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """identity must be of a type compatible with string""",
          'defined-type': "string",
          'generated-type': """YANGDynClass(base=unicode, is_leaf=True, yang_name="identity", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=False, namespace='urn:brocade.com:mgmt:brocade-netconf-ext', defining_module='brocade-netconf-ext', yang_type='string', is_config=True)""",
        })

    self.__identity = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_identity(self):
    self.__identity = YANGDynClass(base=unicode, is_leaf=True, yang_name="identity", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=False, namespace='urn:brocade.com:mgmt:brocade-netconf-ext', defining_module='brocade-netconf-ext', yang_type='string', is_config=True)


  def _get_af_type(self):
    """
    Getter method for af_type, mapped from YANG variable /brocade_netconf_ext_rpc/get_netconf_client_capabilities/output/session/af_type (enumeration)

    YANG Description: This leaf indicates the address family type. If the value is IPV4
then the client host IP will be present in the host-ip leaf.
If the value is IPV6, then the client host IP will be present in
host-ip-V6 leaf
    """
    return self.__af_type
      
  def _set_af_type(self, v, load=False):
    """
    Setter method for af_type, mapped from YANG variable /brocade_netconf_ext_rpc/get_netconf_client_capabilities/output/session/af_type (enumeration)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_af_type is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_af_type() directly.

    YANG Description: This leaf indicates the address family type. If the value is IPV4
then the client host IP will be present in the host-ip leaf.
If the value is IPV6, then the client host IP will be present in
host-ip-V6 leaf
    """
    try:
      t = YANGDynClass(v,base=RestrictedClassType(base_type=unicode,                                     restriction_type="dict_key",                                     restriction_arg={u'IPV4': {'value': 2}, u'IPV6': {'value': 10}},), is_leaf=True, yang_name="af-type", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=False, namespace='urn:brocade.com:mgmt:brocade-netconf-ext', defining_module='brocade-netconf-ext', yang_type='enumeration', is_config=True)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """af_type must be of a type compatible with enumeration""",
          'defined-type': "brocade-netconf-ext:enumeration",
          'generated-type': """YANGDynClass(base=RestrictedClassType(base_type=unicode,                                     restriction_type="dict_key",                                     restriction_arg={u'IPV4': {'value': 2}, u'IPV6': {'value': 10}},), is_leaf=True, yang_name="af-type", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=False, namespace='urn:brocade.com:mgmt:brocade-netconf-ext', defining_module='brocade-netconf-ext', yang_type='enumeration', is_config=True)""",
        })

    self.__af_type = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_af_type(self):
    self.__af_type = YANGDynClass(base=RestrictedClassType(base_type=unicode,                                     restriction_type="dict_key",                                     restriction_arg={u'IPV4': {'value': 2}, u'IPV6': {'value': 10}},), is_leaf=True, yang_name="af-type", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=False, namespace='urn:brocade.com:mgmt:brocade-netconf-ext', defining_module='brocade-netconf-ext', yang_type='enumeration', is_config=True)


  def _get_host_ip_v6(self):
    """
    Getter method for host_ip_v6, mapped from YANG variable /brocade_netconf_ext_rpc/get_netconf_client_capabilities/output/session/host_ip_v6 (inet:ipv6-address)

    YANG Description: IP Address of NETCONF client session
    """
    return self.__host_ip_v6
      
  def _set_host_ip_v6(self, v, load=False):
    """
    Setter method for host_ip_v6, mapped from YANG variable /brocade_netconf_ext_rpc/get_netconf_client_capabilities/output/session/host_ip_v6 (inet:ipv6-address)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_host_ip_v6 is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_host_ip_v6() directly.

    YANG Description: IP Address of NETCONF client session
    """
    try:
      t = YANGDynClass(v,base=RestrictedClassType(base_type=unicode, restriction_dict={'pattern': u'((:|[0-9a-fA-F]{0,4}):)([0-9a-fA-F]{0,4}:){0,5}((([0-9a-fA-F]{0,4}:)?(:|[0-9a-fA-F]{0,4}))|(((25[0-5]|2[0-4][0-9]|[01]?[0-9]?[0-9])\\.){3}(25[0-5]|2[0-4][0-9]|[01]?[0-9]?[0-9])))(%[\\p{N}\\p{L}]+)?'}), is_leaf=True, yang_name="host-ip-v6", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=False, namespace='urn:brocade.com:mgmt:brocade-netconf-ext', defining_module='brocade-netconf-ext', yang_type='inet:ipv6-address', is_config=True)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """host_ip_v6 must be of a type compatible with inet:ipv6-address""",
          'defined-type': "inet:ipv6-address",
          'generated-type': """YANGDynClass(base=RestrictedClassType(base_type=unicode, restriction_dict={'pattern': u'((:|[0-9a-fA-F]{0,4}):)([0-9a-fA-F]{0,4}:){0,5}((([0-9a-fA-F]{0,4}:)?(:|[0-9a-fA-F]{0,4}))|(((25[0-5]|2[0-4][0-9]|[01]?[0-9]?[0-9])\\.){3}(25[0-5]|2[0-4][0-9]|[01]?[0-9]?[0-9])))(%[\\p{N}\\p{L}]+)?'}), is_leaf=True, yang_name="host-ip-v6", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=False, namespace='urn:brocade.com:mgmt:brocade-netconf-ext', defining_module='brocade-netconf-ext', yang_type='inet:ipv6-address', is_config=True)""",
        })

    self.__host_ip_v6 = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_host_ip_v6(self):
    self.__host_ip_v6 = YANGDynClass(base=RestrictedClassType(base_type=unicode, restriction_dict={'pattern': u'((:|[0-9a-fA-F]{0,4}):)([0-9a-fA-F]{0,4}:){0,5}((([0-9a-fA-F]{0,4}:)?(:|[0-9a-fA-F]{0,4}))|(((25[0-5]|2[0-4][0-9]|[01]?[0-9]?[0-9])\\.){3}(25[0-5]|2[0-4][0-9]|[01]?[0-9]?[0-9])))(%[\\p{N}\\p{L}]+)?'}), is_leaf=True, yang_name="host-ip-v6", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=False, namespace='urn:brocade.com:mgmt:brocade-netconf-ext', defining_module='brocade-netconf-ext', yang_type='inet:ipv6-address', is_config=True)


  def _get_host_ip(self):
    """
    Getter method for host_ip, mapped from YANG variable /brocade_netconf_ext_rpc/get_netconf_client_capabilities/output/session/host_ip (inet:ipv4-address)

    YANG Description: IP Address of NETCONF client session
    """
    return self.__host_ip
      
  def _set_host_ip(self, v, load=False):
    """
    Setter method for host_ip, mapped from YANG variable /brocade_netconf_ext_rpc/get_netconf_client_capabilities/output/session/host_ip (inet:ipv4-address)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_host_ip is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_host_ip() directly.

    YANG Description: IP Address of NETCONF client session
    """
    try:
      t = YANGDynClass(v,base=RestrictedClassType(base_type=unicode, restriction_dict={'pattern': u'(([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])\\.){3}([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])(%[\\p{N}\\p{L}]+)?'}), is_leaf=True, yang_name="host-ip", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=False, namespace='urn:brocade.com:mgmt:brocade-netconf-ext', defining_module='brocade-netconf-ext', yang_type='inet:ipv4-address', is_config=True)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """host_ip must be of a type compatible with inet:ipv4-address""",
          'defined-type': "inet:ipv4-address",
          'generated-type': """YANGDynClass(base=RestrictedClassType(base_type=unicode, restriction_dict={'pattern': u'(([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])\\.){3}([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])(%[\\p{N}\\p{L}]+)?'}), is_leaf=True, yang_name="host-ip", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=False, namespace='urn:brocade.com:mgmt:brocade-netconf-ext', defining_module='brocade-netconf-ext', yang_type='inet:ipv4-address', is_config=True)""",
        })

    self.__host_ip = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_host_ip(self):
    self.__host_ip = YANGDynClass(base=RestrictedClassType(base_type=unicode, restriction_dict={'pattern': u'(([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])\\.){3}([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])(%[\\p{N}\\p{L}]+)?'}), is_leaf=True, yang_name="host-ip", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=False, namespace='urn:brocade.com:mgmt:brocade-netconf-ext', defining_module='brocade-netconf-ext', yang_type='inet:ipv4-address', is_config=True)


  def _get_time(self):
    """
    Getter method for time, mapped from YANG variable /brocade_netconf_ext_rpc/get_netconf_client_capabilities/output/session/time (ietfyang:date-and-time)

    YANG Description: Login time of NETCONF client session
    """
    return self.__time
      
  def _set_time(self, v, load=False):
    """
    Setter method for time, mapped from YANG variable /brocade_netconf_ext_rpc/get_netconf_client_capabilities/output/session/time (ietfyang:date-and-time)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_time is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_time() directly.

    YANG Description: Login time of NETCONF client session
    """
    try:
      t = YANGDynClass(v,base=RestrictedClassType(base_type=unicode, restriction_dict={'pattern': u'\\d{4}-\\d{2}-\\d{2}T\\d{2}:\\d{2}:\\d{2}(\\.\\d+)?(Z|[\\+\\-]\\d{2}:\\d{2})'}), is_leaf=True, yang_name="time", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=False, namespace='urn:brocade.com:mgmt:brocade-netconf-ext', defining_module='brocade-netconf-ext', yang_type='ietfyang:date-and-time', is_config=True)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """time must be of a type compatible with ietfyang:date-and-time""",
          'defined-type': "ietfyang:date-and-time",
          'generated-type': """YANGDynClass(base=RestrictedClassType(base_type=unicode, restriction_dict={'pattern': u'\\d{4}-\\d{2}-\\d{2}T\\d{2}:\\d{2}:\\d{2}(\\.\\d+)?(Z|[\\+\\-]\\d{2}:\\d{2})'}), is_leaf=True, yang_name="time", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=False, namespace='urn:brocade.com:mgmt:brocade-netconf-ext', defining_module='brocade-netconf-ext', yang_type='ietfyang:date-and-time', is_config=True)""",
        })

    self.__time = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_time(self):
    self.__time = YANGDynClass(base=RestrictedClassType(base_type=unicode, restriction_dict={'pattern': u'\\d{4}-\\d{2}-\\d{2}T\\d{2}:\\d{2}:\\d{2}(\\.\\d+)?(Z|[\\+\\-]\\d{2}:\\d{2})'}), is_leaf=True, yang_name="time", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=False, namespace='urn:brocade.com:mgmt:brocade-netconf-ext', defining_module='brocade-netconf-ext', yang_type='ietfyang:date-and-time', is_config=True)

  session_id = __builtin__.property(_get_session_id, _set_session_id)
  user_name = __builtin__.property(_get_user_name, _set_user_name)
  vendor = __builtin__.property(_get_vendor, _set_vendor)
  product = __builtin__.property(_get_product, _set_product)
  version = __builtin__.property(_get_version, _set_version)
  identity = __builtin__.property(_get_identity, _set_identity)
  af_type = __builtin__.property(_get_af_type, _set_af_type)
  host_ip_v6 = __builtin__.property(_get_host_ip_v6, _set_host_ip_v6)
  host_ip = __builtin__.property(_get_host_ip, _set_host_ip)
  time = __builtin__.property(_get_time, _set_time)


  _pyangbind_elements = {'session_id': session_id, 'user_name': user_name, 'vendor': vendor, 'product': product, 'version': version, 'identity': identity, 'af_type': af_type, 'host_ip_v6': host_ip_v6, 'host_ip': host_ip, 'time': time, }

