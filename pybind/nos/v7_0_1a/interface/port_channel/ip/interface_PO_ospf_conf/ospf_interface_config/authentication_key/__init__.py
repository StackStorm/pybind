
from operator import attrgetter
import pyangbind.lib.xpathhelper as xpathhelper
from pyangbind.lib.yangtypes import RestrictedPrecisionDecimalType, RestrictedClassType, TypedListType
from pyangbind.lib.yangtypes import YANGBool, YANGListType, YANGDynClass, ReferenceType
from pyangbind.lib.base import PybindBase
from decimal import Decimal
from bitarray import bitarray
import __builtin__
import no_encrypt_auth_key_table
import auth_key_table
class authentication_key(PybindBase):
  """
  This class was auto-generated by the PythonClass plugin for PYANG
  from YANG module brocade-interface - based on the path /interface/port-channel/ip/interface-PO-ospf-conf/ospf-interface-config/authentication-key. Each member element of
  the container is represented as a class variable - with a specific
  YANG type.
  """
  __slots__ = ('_pybind_generated_by', '_path_helper', '_yang_name', '_rest_name', '_extmethods', '__no_encrypt_auth_key_table','__auth_key_table',)

  _yang_name = 'authentication-key'
  _rest_name = 'authentication-key'

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
    self.__no_encrypt_auth_key_table = YANGDynClass(base=no_encrypt_auth_key_table.no_encrypt_auth_key_table, is_container='container', presence=False, yang_name="no-encrypt-auth-key-table", rest_name="", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'cli-drop-node-name': None}}, namespace='urn:brocade.com:mgmt:brocade-ospf', defining_module='brocade-ospf', yang_type='container', is_config=True)
    self.__auth_key_table = YANGDynClass(base=auth_key_table.auth_key_table, is_container='container', presence=False, yang_name="auth-key-table", rest_name="", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'cli-compact-syntax': None, u'cli-drop-node-name': None, u'cli-sequence-commands': None}}, namespace='urn:brocade.com:mgmt:brocade-ospf', defining_module='brocade-ospf', yang_type='container', is_config=True)

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
      return [u'interface', u'port-channel', u'ip', u'interface-PO-ospf-conf', u'ospf-interface-config', u'authentication-key']

  def _rest_path(self):
    if hasattr(self, "_parent"):
      if self._rest_name:
        return self._parent._rest_path()+[self._rest_name]
      else:
        return self._parent._rest_path()
    else:
      return [u'interface', u'Port-channel', u'ip', u'ospf', u'authentication-key']

  def _get_no_encrypt_auth_key_table(self):
    """
    Getter method for no_encrypt_auth_key_table, mapped from YANG variable /interface/port_channel/ip/interface_PO_ospf_conf/ospf_interface_config/authentication_key/no_encrypt_auth_key_table (container)
    """
    return self.__no_encrypt_auth_key_table
      
  def _set_no_encrypt_auth_key_table(self, v, load=False):
    """
    Setter method for no_encrypt_auth_key_table, mapped from YANG variable /interface/port_channel/ip/interface_PO_ospf_conf/ospf_interface_config/authentication_key/no_encrypt_auth_key_table (container)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_no_encrypt_auth_key_table is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_no_encrypt_auth_key_table() directly.
    """
    if hasattr(v, "_utype"):
      v = v._utype(v)
    try:
      t = YANGDynClass(v,base=no_encrypt_auth_key_table.no_encrypt_auth_key_table, is_container='container', presence=False, yang_name="no-encrypt-auth-key-table", rest_name="", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'cli-drop-node-name': None}}, namespace='urn:brocade.com:mgmt:brocade-ospf', defining_module='brocade-ospf', yang_type='container', is_config=True)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """no_encrypt_auth_key_table must be of a type compatible with container""",
          'defined-type': "container",
          'generated-type': """YANGDynClass(base=no_encrypt_auth_key_table.no_encrypt_auth_key_table, is_container='container', presence=False, yang_name="no-encrypt-auth-key-table", rest_name="", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'cli-drop-node-name': None}}, namespace='urn:brocade.com:mgmt:brocade-ospf', defining_module='brocade-ospf', yang_type='container', is_config=True)""",
        })

    self.__no_encrypt_auth_key_table = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_no_encrypt_auth_key_table(self):
    self.__no_encrypt_auth_key_table = YANGDynClass(base=no_encrypt_auth_key_table.no_encrypt_auth_key_table, is_container='container', presence=False, yang_name="no-encrypt-auth-key-table", rest_name="", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'cli-drop-node-name': None}}, namespace='urn:brocade.com:mgmt:brocade-ospf', defining_module='brocade-ospf', yang_type='container', is_config=True)


  def _get_auth_key_table(self):
    """
    Getter method for auth_key_table, mapped from YANG variable /interface/port_channel/ip/interface_PO_ospf_conf/ospf_interface_config/authentication_key/auth_key_table (container)
    """
    return self.__auth_key_table
      
  def _set_auth_key_table(self, v, load=False):
    """
    Setter method for auth_key_table, mapped from YANG variable /interface/port_channel/ip/interface_PO_ospf_conf/ospf_interface_config/authentication_key/auth_key_table (container)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_auth_key_table is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_auth_key_table() directly.
    """
    if hasattr(v, "_utype"):
      v = v._utype(v)
    try:
      t = YANGDynClass(v,base=auth_key_table.auth_key_table, is_container='container', presence=False, yang_name="auth-key-table", rest_name="", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'cli-compact-syntax': None, u'cli-drop-node-name': None, u'cli-sequence-commands': None}}, namespace='urn:brocade.com:mgmt:brocade-ospf', defining_module='brocade-ospf', yang_type='container', is_config=True)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """auth_key_table must be of a type compatible with container""",
          'defined-type': "container",
          'generated-type': """YANGDynClass(base=auth_key_table.auth_key_table, is_container='container', presence=False, yang_name="auth-key-table", rest_name="", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'cli-compact-syntax': None, u'cli-drop-node-name': None, u'cli-sequence-commands': None}}, namespace='urn:brocade.com:mgmt:brocade-ospf', defining_module='brocade-ospf', yang_type='container', is_config=True)""",
        })

    self.__auth_key_table = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_auth_key_table(self):
    self.__auth_key_table = YANGDynClass(base=auth_key_table.auth_key_table, is_container='container', presence=False, yang_name="auth-key-table", rest_name="", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'cli-compact-syntax': None, u'cli-drop-node-name': None, u'cli-sequence-commands': None}}, namespace='urn:brocade.com:mgmt:brocade-ospf', defining_module='brocade-ospf', yang_type='container', is_config=True)

  no_encrypt_auth_key_table = __builtin__.property(_get_no_encrypt_auth_key_table, _set_no_encrypt_auth_key_table)
  auth_key_table = __builtin__.property(_get_auth_key_table, _set_auth_key_table)


  _pyangbind_elements = {'no_encrypt_auth_key_table': no_encrypt_auth_key_table, 'auth_key_table': auth_key_table, }


