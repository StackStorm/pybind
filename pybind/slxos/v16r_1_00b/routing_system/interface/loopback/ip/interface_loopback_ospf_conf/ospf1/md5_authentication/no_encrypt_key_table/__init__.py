
from operator import attrgetter
import pyangbind.lib.xpathhelper as xpathhelper
from pyangbind.lib.yangtypes import RestrictedPrecisionDecimalType, RestrictedClassType, TypedListType
from pyangbind.lib.yangtypes import YANGBool, YANGListType, YANGDynClass, ReferenceType
from pyangbind.lib.base import PybindBase
from decimal import Decimal
from bitarray import bitarray
import __builtin__
class no_encrypt_key_table(PybindBase):
  """
  This class was auto-generated by the PythonClass plugin for PYANG
  from YANG module brocade-common-def - based on the path /routing-system/interface/loopback/ip/interface-loopback-ospf-conf/ospf1/md5-authentication/no-encrypt-key-table. Each member element of
  the container is represented as a class variable - with a specific
  YANG type.
  """
  __slots__ = ('_pybind_generated_by', '_path_helper', '_yang_name', '_rest_name', '_extmethods', '__no_encrypt_key_id','__no_encrypt_key',)

  _yang_name = 'no-encrypt-key-table'
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
    self.__no_encrypt_key_id = YANGDynClass(base=RestrictedClassType(base_type=RestrictedClassType(base_type=long, restriction_dict={'range': ['0..4294967295']}, int_size=32), restriction_dict={'range': [u'1..255']}), is_leaf=True, yang_name="no-encrypt-key-id", rest_name="no-encrypt-key-id", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'hidden': u'full', u'cli-incomplete-no': None, u'cli-incomplete-command': None}}, namespace='urn:brocade.com:mgmt:brocade-ospf', defining_module='brocade-ospf', yang_type='uint32', is_config=True)
    self.__no_encrypt_key = YANGDynClass(base=unicode, is_leaf=True, yang_name="no-encrypt-key", rest_name="", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'cli-full-command': None, u'cli-drop-node-name': None, u'hidden': u'full', u'info': u'MD5 Authentication password (key)'}}, namespace='urn:brocade.com:mgmt:brocade-ospf', defining_module='brocade-ospf', yang_type='ospf-auth-psswd-string', is_config=True)

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
      return [u'routing-system', u'interface', u'loopback', u'ip', u'interface-loopback-ospf-conf', u'ospf1', u'md5-authentication', u'no-encrypt-key-table']

  def _rest_path(self):
    if hasattr(self, "_parent"):
      if self._rest_name:
        return self._parent._rest_path()+[self._rest_name]
      else:
        return self._parent._rest_path()
    else:
      return [u'interface', u'Loopback', u'ip', u'ospf', u'md5-authentication']

  def _get_no_encrypt_key_id(self):
    """
    Getter method for no_encrypt_key_id, mapped from YANG variable /routing_system/interface/loopback/ip/interface_loopback_ospf_conf/ospf1/md5_authentication/no_encrypt_key_table/no_encrypt_key_id (uint32)
    """
    return self.__no_encrypt_key_id
      
  def _set_no_encrypt_key_id(self, v, load=False):
    """
    Setter method for no_encrypt_key_id, mapped from YANG variable /routing_system/interface/loopback/ip/interface_loopback_ospf_conf/ospf1/md5_authentication/no_encrypt_key_table/no_encrypt_key_id (uint32)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_no_encrypt_key_id is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_no_encrypt_key_id() directly.
    """
    if hasattr(v, "_utype"):
      v = v._utype(v)
    try:
      t = YANGDynClass(v,base=RestrictedClassType(base_type=RestrictedClassType(base_type=long, restriction_dict={'range': ['0..4294967295']}, int_size=32), restriction_dict={'range': [u'1..255']}), is_leaf=True, yang_name="no-encrypt-key-id", rest_name="no-encrypt-key-id", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'hidden': u'full', u'cli-incomplete-no': None, u'cli-incomplete-command': None}}, namespace='urn:brocade.com:mgmt:brocade-ospf', defining_module='brocade-ospf', yang_type='uint32', is_config=True)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """no_encrypt_key_id must be of a type compatible with uint32""",
          'defined-type': "uint32",
          'generated-type': """YANGDynClass(base=RestrictedClassType(base_type=RestrictedClassType(base_type=long, restriction_dict={'range': ['0..4294967295']}, int_size=32), restriction_dict={'range': [u'1..255']}), is_leaf=True, yang_name="no-encrypt-key-id", rest_name="no-encrypt-key-id", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'hidden': u'full', u'cli-incomplete-no': None, u'cli-incomplete-command': None}}, namespace='urn:brocade.com:mgmt:brocade-ospf', defining_module='brocade-ospf', yang_type='uint32', is_config=True)""",
        })

    self.__no_encrypt_key_id = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_no_encrypt_key_id(self):
    self.__no_encrypt_key_id = YANGDynClass(base=RestrictedClassType(base_type=RestrictedClassType(base_type=long, restriction_dict={'range': ['0..4294967295']}, int_size=32), restriction_dict={'range': [u'1..255']}), is_leaf=True, yang_name="no-encrypt-key-id", rest_name="no-encrypt-key-id", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'hidden': u'full', u'cli-incomplete-no': None, u'cli-incomplete-command': None}}, namespace='urn:brocade.com:mgmt:brocade-ospf', defining_module='brocade-ospf', yang_type='uint32', is_config=True)


  def _get_no_encrypt_key(self):
    """
    Getter method for no_encrypt_key, mapped from YANG variable /routing_system/interface/loopback/ip/interface_loopback_ospf_conf/ospf1/md5_authentication/no_encrypt_key_table/no_encrypt_key (ospf-auth-psswd-string)
    """
    return self.__no_encrypt_key
      
  def _set_no_encrypt_key(self, v, load=False):
    """
    Setter method for no_encrypt_key, mapped from YANG variable /routing_system/interface/loopback/ip/interface_loopback_ospf_conf/ospf1/md5_authentication/no_encrypt_key_table/no_encrypt_key (ospf-auth-psswd-string)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_no_encrypt_key is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_no_encrypt_key() directly.
    """
    if hasattr(v, "_utype"):
      v = v._utype(v)
    try:
      t = YANGDynClass(v,base=unicode, is_leaf=True, yang_name="no-encrypt-key", rest_name="", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'cli-full-command': None, u'cli-drop-node-name': None, u'hidden': u'full', u'info': u'MD5 Authentication password (key)'}}, namespace='urn:brocade.com:mgmt:brocade-ospf', defining_module='brocade-ospf', yang_type='ospf-auth-psswd-string', is_config=True)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """no_encrypt_key must be of a type compatible with ospf-auth-psswd-string""",
          'defined-type': "brocade-ospf:ospf-auth-psswd-string",
          'generated-type': """YANGDynClass(base=unicode, is_leaf=True, yang_name="no-encrypt-key", rest_name="", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'cli-full-command': None, u'cli-drop-node-name': None, u'hidden': u'full', u'info': u'MD5 Authentication password (key)'}}, namespace='urn:brocade.com:mgmt:brocade-ospf', defining_module='brocade-ospf', yang_type='ospf-auth-psswd-string', is_config=True)""",
        })

    self.__no_encrypt_key = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_no_encrypt_key(self):
    self.__no_encrypt_key = YANGDynClass(base=unicode, is_leaf=True, yang_name="no-encrypt-key", rest_name="", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'cli-full-command': None, u'cli-drop-node-name': None, u'hidden': u'full', u'info': u'MD5 Authentication password (key)'}}, namespace='urn:brocade.com:mgmt:brocade-ospf', defining_module='brocade-ospf', yang_type='ospf-auth-psswd-string', is_config=True)

  no_encrypt_key_id = __builtin__.property(_get_no_encrypt_key_id, _set_no_encrypt_key_id)
  no_encrypt_key = __builtin__.property(_get_no_encrypt_key, _set_no_encrypt_key)


  _pyangbind_elements = {'no_encrypt_key_id': no_encrypt_key_id, 'no_encrypt_key': no_encrypt_key, }


