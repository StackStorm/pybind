
from operator import attrgetter
import pyangbind.lib.xpathhelper as xpathhelper
from pyangbind.lib.yangtypes import RestrictedPrecisionDecimalType, RestrictedClassType, TypedListType
from pyangbind.lib.yangtypes import YANGBool, YANGListType, YANGDynClass, ReferenceType
from pyangbind.lib.base import PybindBase
from decimal import Decimal
from bitarray import bitarray
import __builtin__
import server
import authentication_key
class ntp(PybindBase):
  """
  This class was auto-generated by the PythonClass plugin for PYANG
  from YANG module brocade-ntp - based on the path /ntp. Each member element of
  the container is represented as a class variable - with a specific
  YANG type.
  """
  __slots__ = ('_pybind_generated_by', '_path_helper', '_yang_name', '_rest_name', '_extmethods', '__server','__authentication_key','__source_ip',)

  _yang_name = 'ntp'
  _rest_name = 'ntp'

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
    self.__authentication_key = YANGDynClass(base=YANGListType("keyid",authentication_key.authentication_key, yang_name="authentication-key", rest_name="authentication-key", parent=self, is_container='list', user_ordered=False, path_helper=self._path_helper, yang_keys='keyid', extensions={u'tailf-common': {u'cli-suppress-key-sort': None, u'info': u'authentication key', u'cli-no-key-completion': None, u'cli-suppress-mode': None, u'sort-priority': u'26', u'cli-suppress-list-no': None, u'cli-full-no': None, u'cli-compact-syntax': None, u'cli-suppress-key-abbreviation': None, u'cli-incomplete-command': None, u'callpoint': u'ntp-key'}}), is_container='list', yang_name="authentication-key", rest_name="authentication-key", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'cli-suppress-key-sort': None, u'info': u'authentication key', u'cli-no-key-completion': None, u'cli-suppress-mode': None, u'sort-priority': u'26', u'cli-suppress-list-no': None, u'cli-full-no': None, u'cli-compact-syntax': None, u'cli-suppress-key-abbreviation': None, u'cli-incomplete-command': None, u'callpoint': u'ntp-key'}}, namespace='urn:brocade.com:mgmt:brocade-ntp', defining_module='brocade-ntp', yang_type='list', is_config=True)
    self.__source_ip = YANGDynClass(base=RestrictedClassType(base_type=unicode,                                     restriction_type="dict_key",                                     restriction_arg={u'chassis-ip': {'value': 1}, u'mm-ip': {'value': 2}},), default=unicode("mm-ip"), is_leaf=True, yang_name="source-ip", rest_name="source-ip", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'info': u'Configure the source ip to be used for NTP', u'cli-full-command': None, u'callpoint': u'ntp_srcip_cp'}}, namespace='urn:brocade.com:mgmt:brocade-ntp', defining_module='brocade-ntp', yang_type='srcip_type', is_config=True)
    self.__server = YANGDynClass(base=YANGListType("ip use_vrf",server.server, yang_name="server", rest_name="server", parent=self, is_container='list', user_ordered=False, path_helper=self._path_helper, yang_keys='ip use-vrf', extensions={u'tailf-common': {u'cli-suppress-key-sort': None, u'info': u'Configure NTP server', u'sort-priority': u'27', u'cli-suppress-list-no': None, u'cli-suppress-key-abbreviation': None, u'cli-full-command': None, u'callpoint': u'ntp-server'}}), is_container='list', yang_name="server", rest_name="server", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'cli-suppress-key-sort': None, u'info': u'Configure NTP server', u'sort-priority': u'27', u'cli-suppress-list-no': None, u'cli-suppress-key-abbreviation': None, u'cli-full-command': None, u'callpoint': u'ntp-server'}}, namespace='urn:brocade.com:mgmt:brocade-ntp', defining_module='brocade-ntp', yang_type='list', is_config=True)

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
      return [u'ntp']

  def _rest_path(self):
    if hasattr(self, "_parent"):
      if self._rest_name:
        return self._parent._rest_path()+[self._rest_name]
      else:
        return self._parent._rest_path()
    else:
      return [u'ntp']

  def _get_server(self):
    """
    Getter method for server, mapped from YANG variable /ntp/server (list)
    """
    return self.__server
      
  def _set_server(self, v, load=False):
    """
    Setter method for server, mapped from YANG variable /ntp/server (list)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_server is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_server() directly.
    """
    if hasattr(v, "_utype"):
      v = v._utype(v)
    try:
      t = YANGDynClass(v,base=YANGListType("ip use_vrf",server.server, yang_name="server", rest_name="server", parent=self, is_container='list', user_ordered=False, path_helper=self._path_helper, yang_keys='ip use-vrf', extensions={u'tailf-common': {u'cli-suppress-key-sort': None, u'info': u'Configure NTP server', u'sort-priority': u'27', u'cli-suppress-list-no': None, u'cli-suppress-key-abbreviation': None, u'cli-full-command': None, u'callpoint': u'ntp-server'}}), is_container='list', yang_name="server", rest_name="server", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'cli-suppress-key-sort': None, u'info': u'Configure NTP server', u'sort-priority': u'27', u'cli-suppress-list-no': None, u'cli-suppress-key-abbreviation': None, u'cli-full-command': None, u'callpoint': u'ntp-server'}}, namespace='urn:brocade.com:mgmt:brocade-ntp', defining_module='brocade-ntp', yang_type='list', is_config=True)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """server must be of a type compatible with list""",
          'defined-type': "list",
          'generated-type': """YANGDynClass(base=YANGListType("ip use_vrf",server.server, yang_name="server", rest_name="server", parent=self, is_container='list', user_ordered=False, path_helper=self._path_helper, yang_keys='ip use-vrf', extensions={u'tailf-common': {u'cli-suppress-key-sort': None, u'info': u'Configure NTP server', u'sort-priority': u'27', u'cli-suppress-list-no': None, u'cli-suppress-key-abbreviation': None, u'cli-full-command': None, u'callpoint': u'ntp-server'}}), is_container='list', yang_name="server", rest_name="server", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'cli-suppress-key-sort': None, u'info': u'Configure NTP server', u'sort-priority': u'27', u'cli-suppress-list-no': None, u'cli-suppress-key-abbreviation': None, u'cli-full-command': None, u'callpoint': u'ntp-server'}}, namespace='urn:brocade.com:mgmt:brocade-ntp', defining_module='brocade-ntp', yang_type='list', is_config=True)""",
        })

    self.__server = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_server(self):
    self.__server = YANGDynClass(base=YANGListType("ip use_vrf",server.server, yang_name="server", rest_name="server", parent=self, is_container='list', user_ordered=False, path_helper=self._path_helper, yang_keys='ip use-vrf', extensions={u'tailf-common': {u'cli-suppress-key-sort': None, u'info': u'Configure NTP server', u'sort-priority': u'27', u'cli-suppress-list-no': None, u'cli-suppress-key-abbreviation': None, u'cli-full-command': None, u'callpoint': u'ntp-server'}}), is_container='list', yang_name="server", rest_name="server", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'cli-suppress-key-sort': None, u'info': u'Configure NTP server', u'sort-priority': u'27', u'cli-suppress-list-no': None, u'cli-suppress-key-abbreviation': None, u'cli-full-command': None, u'callpoint': u'ntp-server'}}, namespace='urn:brocade.com:mgmt:brocade-ntp', defining_module='brocade-ntp', yang_type='list', is_config=True)


  def _get_authentication_key(self):
    """
    Getter method for authentication_key, mapped from YANG variable /ntp/authentication_key (list)
    """
    return self.__authentication_key
      
  def _set_authentication_key(self, v, load=False):
    """
    Setter method for authentication_key, mapped from YANG variable /ntp/authentication_key (list)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_authentication_key is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_authentication_key() directly.
    """
    if hasattr(v, "_utype"):
      v = v._utype(v)
    try:
      t = YANGDynClass(v,base=YANGListType("keyid",authentication_key.authentication_key, yang_name="authentication-key", rest_name="authentication-key", parent=self, is_container='list', user_ordered=False, path_helper=self._path_helper, yang_keys='keyid', extensions={u'tailf-common': {u'cli-suppress-key-sort': None, u'info': u'authentication key', u'cli-no-key-completion': None, u'cli-suppress-mode': None, u'sort-priority': u'26', u'cli-suppress-list-no': None, u'cli-full-no': None, u'cli-compact-syntax': None, u'cli-suppress-key-abbreviation': None, u'cli-incomplete-command': None, u'callpoint': u'ntp-key'}}), is_container='list', yang_name="authentication-key", rest_name="authentication-key", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'cli-suppress-key-sort': None, u'info': u'authentication key', u'cli-no-key-completion': None, u'cli-suppress-mode': None, u'sort-priority': u'26', u'cli-suppress-list-no': None, u'cli-full-no': None, u'cli-compact-syntax': None, u'cli-suppress-key-abbreviation': None, u'cli-incomplete-command': None, u'callpoint': u'ntp-key'}}, namespace='urn:brocade.com:mgmt:brocade-ntp', defining_module='brocade-ntp', yang_type='list', is_config=True)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """authentication_key must be of a type compatible with list""",
          'defined-type': "list",
          'generated-type': """YANGDynClass(base=YANGListType("keyid",authentication_key.authentication_key, yang_name="authentication-key", rest_name="authentication-key", parent=self, is_container='list', user_ordered=False, path_helper=self._path_helper, yang_keys='keyid', extensions={u'tailf-common': {u'cli-suppress-key-sort': None, u'info': u'authentication key', u'cli-no-key-completion': None, u'cli-suppress-mode': None, u'sort-priority': u'26', u'cli-suppress-list-no': None, u'cli-full-no': None, u'cli-compact-syntax': None, u'cli-suppress-key-abbreviation': None, u'cli-incomplete-command': None, u'callpoint': u'ntp-key'}}), is_container='list', yang_name="authentication-key", rest_name="authentication-key", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'cli-suppress-key-sort': None, u'info': u'authentication key', u'cli-no-key-completion': None, u'cli-suppress-mode': None, u'sort-priority': u'26', u'cli-suppress-list-no': None, u'cli-full-no': None, u'cli-compact-syntax': None, u'cli-suppress-key-abbreviation': None, u'cli-incomplete-command': None, u'callpoint': u'ntp-key'}}, namespace='urn:brocade.com:mgmt:brocade-ntp', defining_module='brocade-ntp', yang_type='list', is_config=True)""",
        })

    self.__authentication_key = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_authentication_key(self):
    self.__authentication_key = YANGDynClass(base=YANGListType("keyid",authentication_key.authentication_key, yang_name="authentication-key", rest_name="authentication-key", parent=self, is_container='list', user_ordered=False, path_helper=self._path_helper, yang_keys='keyid', extensions={u'tailf-common': {u'cli-suppress-key-sort': None, u'info': u'authentication key', u'cli-no-key-completion': None, u'cli-suppress-mode': None, u'sort-priority': u'26', u'cli-suppress-list-no': None, u'cli-full-no': None, u'cli-compact-syntax': None, u'cli-suppress-key-abbreviation': None, u'cli-incomplete-command': None, u'callpoint': u'ntp-key'}}), is_container='list', yang_name="authentication-key", rest_name="authentication-key", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'cli-suppress-key-sort': None, u'info': u'authentication key', u'cli-no-key-completion': None, u'cli-suppress-mode': None, u'sort-priority': u'26', u'cli-suppress-list-no': None, u'cli-full-no': None, u'cli-compact-syntax': None, u'cli-suppress-key-abbreviation': None, u'cli-incomplete-command': None, u'callpoint': u'ntp-key'}}, namespace='urn:brocade.com:mgmt:brocade-ntp', defining_module='brocade-ntp', yang_type='list', is_config=True)


  def _get_source_ip(self):
    """
    Getter method for source_ip, mapped from YANG variable /ntp/source_ip (srcip_type)
    """
    return self.__source_ip
      
  def _set_source_ip(self, v, load=False):
    """
    Setter method for source_ip, mapped from YANG variable /ntp/source_ip (srcip_type)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_source_ip is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_source_ip() directly.
    """
    if hasattr(v, "_utype"):
      v = v._utype(v)
    try:
      t = YANGDynClass(v,base=RestrictedClassType(base_type=unicode,                                     restriction_type="dict_key",                                     restriction_arg={u'chassis-ip': {'value': 1}, u'mm-ip': {'value': 2}},), default=unicode("mm-ip"), is_leaf=True, yang_name="source-ip", rest_name="source-ip", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'info': u'Configure the source ip to be used for NTP', u'cli-full-command': None, u'callpoint': u'ntp_srcip_cp'}}, namespace='urn:brocade.com:mgmt:brocade-ntp', defining_module='brocade-ntp', yang_type='srcip_type', is_config=True)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """source_ip must be of a type compatible with srcip_type""",
          'defined-type': "brocade-ntp:srcip_type",
          'generated-type': """YANGDynClass(base=RestrictedClassType(base_type=unicode,                                     restriction_type="dict_key",                                     restriction_arg={u'chassis-ip': {'value': 1}, u'mm-ip': {'value': 2}},), default=unicode("mm-ip"), is_leaf=True, yang_name="source-ip", rest_name="source-ip", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'info': u'Configure the source ip to be used for NTP', u'cli-full-command': None, u'callpoint': u'ntp_srcip_cp'}}, namespace='urn:brocade.com:mgmt:brocade-ntp', defining_module='brocade-ntp', yang_type='srcip_type', is_config=True)""",
        })

    self.__source_ip = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_source_ip(self):
    self.__source_ip = YANGDynClass(base=RestrictedClassType(base_type=unicode,                                     restriction_type="dict_key",                                     restriction_arg={u'chassis-ip': {'value': 1}, u'mm-ip': {'value': 2}},), default=unicode("mm-ip"), is_leaf=True, yang_name="source-ip", rest_name="source-ip", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'info': u'Configure the source ip to be used for NTP', u'cli-full-command': None, u'callpoint': u'ntp_srcip_cp'}}, namespace='urn:brocade.com:mgmt:brocade-ntp', defining_module='brocade-ntp', yang_type='srcip_type', is_config=True)

  server = __builtin__.property(_get_server, _set_server)
  authentication_key = __builtin__.property(_get_authentication_key, _set_authentication_key)
  source_ip = __builtin__.property(_get_source_ip, _set_source_ip)


  _pyangbind_elements = {'server': server, 'authentication_key': authentication_key, 'source_ip': source_ip, }


