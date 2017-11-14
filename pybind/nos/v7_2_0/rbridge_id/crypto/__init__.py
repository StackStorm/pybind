
from operator import attrgetter
import pyangbind.lib.xpathhelper as xpathhelper
from pyangbind.lib.yangtypes import RestrictedPrecisionDecimalType, RestrictedClassType, TypedListType
from pyangbind.lib.yangtypes import YANGBool, YANGListType, YANGDynClass, ReferenceType
from pyangbind.lib.base import PybindBase
from decimal import Decimal
from bitarray import bitarray
import __builtin__
import key
import ca
class crypto(PybindBase):
  """
  This class was auto-generated by the PythonClass plugin for PYANG
  from YANG module brocade-rbridge - based on the path /rbridge-id/crypto. Each member element of
  the container is represented as a class variable - with a specific
  YANG type.
  """
  __slots__ = ('_pybind_generated_by', '_path_helper', '_yang_name', '_rest_name', '_extmethods', '__key','__ca',)

  _yang_name = 'crypto'
  _rest_name = 'crypto'

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
    self.__ca = YANGDynClass(base=YANGListType("trustpoint",ca.ca, yang_name="ca", rest_name="ca", parent=self, is_container='list', user_ordered=False, path_helper=self._path_helper, yang_keys='trustpoint', extensions={u'tailf-common': {u'info': u'Configure TrustpointCA', u'cli-suppress-list-no': None, u'callpoint': u'crypto_ca_cp', u'cli-full-command': None}}), is_container='list', yang_name="ca", rest_name="ca", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'info': u'Configure TrustpointCA', u'cli-suppress-list-no': None, u'callpoint': u'crypto_ca_cp', u'cli-full-command': None}}, namespace='urn:brocade.com:mgmt:brocade-crypto', defining_module='brocade-crypto', yang_type='list', is_config=True)
    self.__key = YANGDynClass(base=YANGListType("label",key.key, yang_name="key", rest_name="key", parent=self, is_container='list', user_ordered=False, path_helper=self._path_helper, yang_keys='label', extensions={u'tailf-common': {u'info': u'Configure keypair', u'cli-suppress-mode': None, u'cli-compact-syntax': None, u'callpoint': u'crypto_key_cp', u'cli-suppress-list-no': None}}), is_container='list', yang_name="key", rest_name="key", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'info': u'Configure keypair', u'cli-suppress-mode': None, u'cli-compact-syntax': None, u'callpoint': u'crypto_key_cp', u'cli-suppress-list-no': None}}, namespace='urn:brocade.com:mgmt:brocade-crypto', defining_module='brocade-crypto', yang_type='list', is_config=True)

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
      return [u'rbridge-id', u'crypto']

  def _rest_path(self):
    if hasattr(self, "_parent"):
      if self._rest_name:
        return self._parent._rest_path()+[self._rest_name]
      else:
        return self._parent._rest_path()
    else:
      return [u'rbridge-id', u'crypto']

  def _get_key(self):
    """
    Getter method for key, mapped from YANG variable /rbridge_id/crypto/key (list)
    """
    return self.__key
      
  def _set_key(self, v, load=False):
    """
    Setter method for key, mapped from YANG variable /rbridge_id/crypto/key (list)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_key is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_key() directly.
    """
    if hasattr(v, "_utype"):
      v = v._utype(v)
    try:
      t = YANGDynClass(v,base=YANGListType("label",key.key, yang_name="key", rest_name="key", parent=self, is_container='list', user_ordered=False, path_helper=self._path_helper, yang_keys='label', extensions={u'tailf-common': {u'info': u'Configure keypair', u'cli-suppress-mode': None, u'cli-compact-syntax': None, u'callpoint': u'crypto_key_cp', u'cli-suppress-list-no': None}}), is_container='list', yang_name="key", rest_name="key", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'info': u'Configure keypair', u'cli-suppress-mode': None, u'cli-compact-syntax': None, u'callpoint': u'crypto_key_cp', u'cli-suppress-list-no': None}}, namespace='urn:brocade.com:mgmt:brocade-crypto', defining_module='brocade-crypto', yang_type='list', is_config=True)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """key must be of a type compatible with list""",
          'defined-type': "list",
          'generated-type': """YANGDynClass(base=YANGListType("label",key.key, yang_name="key", rest_name="key", parent=self, is_container='list', user_ordered=False, path_helper=self._path_helper, yang_keys='label', extensions={u'tailf-common': {u'info': u'Configure keypair', u'cli-suppress-mode': None, u'cli-compact-syntax': None, u'callpoint': u'crypto_key_cp', u'cli-suppress-list-no': None}}), is_container='list', yang_name="key", rest_name="key", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'info': u'Configure keypair', u'cli-suppress-mode': None, u'cli-compact-syntax': None, u'callpoint': u'crypto_key_cp', u'cli-suppress-list-no': None}}, namespace='urn:brocade.com:mgmt:brocade-crypto', defining_module='brocade-crypto', yang_type='list', is_config=True)""",
        })

    self.__key = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_key(self):
    self.__key = YANGDynClass(base=YANGListType("label",key.key, yang_name="key", rest_name="key", parent=self, is_container='list', user_ordered=False, path_helper=self._path_helper, yang_keys='label', extensions={u'tailf-common': {u'info': u'Configure keypair', u'cli-suppress-mode': None, u'cli-compact-syntax': None, u'callpoint': u'crypto_key_cp', u'cli-suppress-list-no': None}}), is_container='list', yang_name="key", rest_name="key", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'info': u'Configure keypair', u'cli-suppress-mode': None, u'cli-compact-syntax': None, u'callpoint': u'crypto_key_cp', u'cli-suppress-list-no': None}}, namespace='urn:brocade.com:mgmt:brocade-crypto', defining_module='brocade-crypto', yang_type='list', is_config=True)


  def _get_ca(self):
    """
    Getter method for ca, mapped from YANG variable /rbridge_id/crypto/ca (list)
    """
    return self.__ca
      
  def _set_ca(self, v, load=False):
    """
    Setter method for ca, mapped from YANG variable /rbridge_id/crypto/ca (list)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_ca is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_ca() directly.
    """
    if hasattr(v, "_utype"):
      v = v._utype(v)
    try:
      t = YANGDynClass(v,base=YANGListType("trustpoint",ca.ca, yang_name="ca", rest_name="ca", parent=self, is_container='list', user_ordered=False, path_helper=self._path_helper, yang_keys='trustpoint', extensions={u'tailf-common': {u'info': u'Configure TrustpointCA', u'cli-suppress-list-no': None, u'callpoint': u'crypto_ca_cp', u'cli-full-command': None}}), is_container='list', yang_name="ca", rest_name="ca", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'info': u'Configure TrustpointCA', u'cli-suppress-list-no': None, u'callpoint': u'crypto_ca_cp', u'cli-full-command': None}}, namespace='urn:brocade.com:mgmt:brocade-crypto', defining_module='brocade-crypto', yang_type='list', is_config=True)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """ca must be of a type compatible with list""",
          'defined-type': "list",
          'generated-type': """YANGDynClass(base=YANGListType("trustpoint",ca.ca, yang_name="ca", rest_name="ca", parent=self, is_container='list', user_ordered=False, path_helper=self._path_helper, yang_keys='trustpoint', extensions={u'tailf-common': {u'info': u'Configure TrustpointCA', u'cli-suppress-list-no': None, u'callpoint': u'crypto_ca_cp', u'cli-full-command': None}}), is_container='list', yang_name="ca", rest_name="ca", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'info': u'Configure TrustpointCA', u'cli-suppress-list-no': None, u'callpoint': u'crypto_ca_cp', u'cli-full-command': None}}, namespace='urn:brocade.com:mgmt:brocade-crypto', defining_module='brocade-crypto', yang_type='list', is_config=True)""",
        })

    self.__ca = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_ca(self):
    self.__ca = YANGDynClass(base=YANGListType("trustpoint",ca.ca, yang_name="ca", rest_name="ca", parent=self, is_container='list', user_ordered=False, path_helper=self._path_helper, yang_keys='trustpoint', extensions={u'tailf-common': {u'info': u'Configure TrustpointCA', u'cli-suppress-list-no': None, u'callpoint': u'crypto_ca_cp', u'cli-full-command': None}}), is_container='list', yang_name="ca", rest_name="ca", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'info': u'Configure TrustpointCA', u'cli-suppress-list-no': None, u'callpoint': u'crypto_ca_cp', u'cli-full-command': None}}, namespace='urn:brocade.com:mgmt:brocade-crypto', defining_module='brocade-crypto', yang_type='list', is_config=True)

  key = __builtin__.property(_get_key, _set_key)
  ca = __builtin__.property(_get_ca, _set_ca)


  _pyangbind_elements = {'key': key, 'ca': ca, }


