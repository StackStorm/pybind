
from operator import attrgetter
import pyangbind.lib.xpathhelper as xpathhelper
from pyangbind.lib.yangtypes import RestrictedPrecisionDecimalType, RestrictedClassType, TypedListType
from pyangbind.lib.yangtypes import YANGBool, YANGListType, YANGDynClass, ReferenceType
from pyangbind.lib.base import PybindBase
from decimal import Decimal
from bitarray import bitarray
import __builtin__
class autoupgrade_params(PybindBase):
  """
  This class was auto-generated by the PythonClass plugin for PYANG
  from YANG module brocade-firmware - based on the path /firmware/autoupgrade-params. Each member element of
  the container is represented as a class variable - with a specific
  YANG type.
  """
  __slots__ = ('_pybind_generated_by', '_path_helper', '_yang_name', '_rest_name', '_extmethods', '__path','__protocol','__ipaddress','__username','__pass_',)

  _yang_name = 'autoupgrade-params'
  _rest_name = 'auto-upgrade-params'

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
    self.__ipaddress = YANGDynClass(base=unicode, is_leaf=True, yang_name="ipaddress", rest_name="host", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'info': u'Ipaddress or hostname', u'alt-name': u'host'}}, namespace='urn:brocade.com:mgmt:brocade-firmware', defining_module='brocade-firmware', yang_type='string', is_config=True)
    self.__path = YANGDynClass(base=unicode, is_leaf=True, yang_name="path", rest_name="path", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'info': u'Auto-upgrade firmware path'}}, namespace='urn:brocade.com:mgmt:brocade-firmware', defining_module='brocade-firmware', yang_type='string', is_config=True)
    self.__username = YANGDynClass(base=unicode, is_leaf=True, yang_name="username", rest_name="username", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'info': u'Username'}}, namespace='urn:brocade.com:mgmt:brocade-firmware', defining_module='brocade-firmware', yang_type='string', is_config=True)
    self.__pass_ = YANGDynClass(base=unicode, is_leaf=True, yang_name="pass", rest_name="password", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'info': u'Password', u'alt-name': u'password', u'suppress-echo': u'true'}}, namespace='urn:brocade.com:mgmt:brocade-firmware', defining_module='brocade-firmware', yang_type='string', is_config=True)
    self.__protocol = YANGDynClass(base=RestrictedClassType(base_type=unicode,                                     restriction_type="dict_key",                                     restriction_arg={u'ftp': {'value': 1}, u'scp': {'value': 2}, u'sftp': {'value': 3}},), is_leaf=True, yang_name="protocol", rest_name="protocol", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'info': u'Protocol type : ftp, scp, sftp, usb'}}, namespace='urn:brocade.com:mgmt:brocade-firmware', defining_module='brocade-firmware', yang_type='enumeration', is_config=True)

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
      return [u'firmware', u'autoupgrade-params']

  def _rest_path(self):
    if hasattr(self, "_parent"):
      if self._rest_name:
        return self._parent._rest_path()+[self._rest_name]
      else:
        return self._parent._rest_path()
    else:
      return [u'firmware', u'auto-upgrade-params']

  def _get_path(self):
    """
    Getter method for path, mapped from YANG variable /firmware/autoupgrade_params/path (string)
    """
    return self.__path
      
  def _set_path(self, v, load=False):
    """
    Setter method for path, mapped from YANG variable /firmware/autoupgrade_params/path (string)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_path is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_path() directly.
    """
    if hasattr(v, "_utype"):
      v = v._utype(v)
    try:
      t = YANGDynClass(v,base=unicode, is_leaf=True, yang_name="path", rest_name="path", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'info': u'Auto-upgrade firmware path'}}, namespace='urn:brocade.com:mgmt:brocade-firmware', defining_module='brocade-firmware', yang_type='string', is_config=True)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """path must be of a type compatible with string""",
          'defined-type': "string",
          'generated-type': """YANGDynClass(base=unicode, is_leaf=True, yang_name="path", rest_name="path", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'info': u'Auto-upgrade firmware path'}}, namespace='urn:brocade.com:mgmt:brocade-firmware', defining_module='brocade-firmware', yang_type='string', is_config=True)""",
        })

    self.__path = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_path(self):
    self.__path = YANGDynClass(base=unicode, is_leaf=True, yang_name="path", rest_name="path", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'info': u'Auto-upgrade firmware path'}}, namespace='urn:brocade.com:mgmt:brocade-firmware', defining_module='brocade-firmware', yang_type='string', is_config=True)


  def _get_protocol(self):
    """
    Getter method for protocol, mapped from YANG variable /firmware/autoupgrade_params/protocol (enumeration)
    """
    return self.__protocol
      
  def _set_protocol(self, v, load=False):
    """
    Setter method for protocol, mapped from YANG variable /firmware/autoupgrade_params/protocol (enumeration)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_protocol is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_protocol() directly.
    """
    if hasattr(v, "_utype"):
      v = v._utype(v)
    try:
      t = YANGDynClass(v,base=RestrictedClassType(base_type=unicode,                                     restriction_type="dict_key",                                     restriction_arg={u'ftp': {'value': 1}, u'scp': {'value': 2}, u'sftp': {'value': 3}},), is_leaf=True, yang_name="protocol", rest_name="protocol", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'info': u'Protocol type : ftp, scp, sftp, usb'}}, namespace='urn:brocade.com:mgmt:brocade-firmware', defining_module='brocade-firmware', yang_type='enumeration', is_config=True)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """protocol must be of a type compatible with enumeration""",
          'defined-type': "brocade-firmware:enumeration",
          'generated-type': """YANGDynClass(base=RestrictedClassType(base_type=unicode,                                     restriction_type="dict_key",                                     restriction_arg={u'ftp': {'value': 1}, u'scp': {'value': 2}, u'sftp': {'value': 3}},), is_leaf=True, yang_name="protocol", rest_name="protocol", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'info': u'Protocol type : ftp, scp, sftp, usb'}}, namespace='urn:brocade.com:mgmt:brocade-firmware', defining_module='brocade-firmware', yang_type='enumeration', is_config=True)""",
        })

    self.__protocol = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_protocol(self):
    self.__protocol = YANGDynClass(base=RestrictedClassType(base_type=unicode,                                     restriction_type="dict_key",                                     restriction_arg={u'ftp': {'value': 1}, u'scp': {'value': 2}, u'sftp': {'value': 3}},), is_leaf=True, yang_name="protocol", rest_name="protocol", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'info': u'Protocol type : ftp, scp, sftp, usb'}}, namespace='urn:brocade.com:mgmt:brocade-firmware', defining_module='brocade-firmware', yang_type='enumeration', is_config=True)


  def _get_ipaddress(self):
    """
    Getter method for ipaddress, mapped from YANG variable /firmware/autoupgrade_params/ipaddress (string)
    """
    return self.__ipaddress
      
  def _set_ipaddress(self, v, load=False):
    """
    Setter method for ipaddress, mapped from YANG variable /firmware/autoupgrade_params/ipaddress (string)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_ipaddress is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_ipaddress() directly.
    """
    if hasattr(v, "_utype"):
      v = v._utype(v)
    try:
      t = YANGDynClass(v,base=unicode, is_leaf=True, yang_name="ipaddress", rest_name="host", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'info': u'Ipaddress or hostname', u'alt-name': u'host'}}, namespace='urn:brocade.com:mgmt:brocade-firmware', defining_module='brocade-firmware', yang_type='string', is_config=True)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """ipaddress must be of a type compatible with string""",
          'defined-type': "string",
          'generated-type': """YANGDynClass(base=unicode, is_leaf=True, yang_name="ipaddress", rest_name="host", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'info': u'Ipaddress or hostname', u'alt-name': u'host'}}, namespace='urn:brocade.com:mgmt:brocade-firmware', defining_module='brocade-firmware', yang_type='string', is_config=True)""",
        })

    self.__ipaddress = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_ipaddress(self):
    self.__ipaddress = YANGDynClass(base=unicode, is_leaf=True, yang_name="ipaddress", rest_name="host", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'info': u'Ipaddress or hostname', u'alt-name': u'host'}}, namespace='urn:brocade.com:mgmt:brocade-firmware', defining_module='brocade-firmware', yang_type='string', is_config=True)


  def _get_username(self):
    """
    Getter method for username, mapped from YANG variable /firmware/autoupgrade_params/username (string)
    """
    return self.__username
      
  def _set_username(self, v, load=False):
    """
    Setter method for username, mapped from YANG variable /firmware/autoupgrade_params/username (string)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_username is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_username() directly.
    """
    if hasattr(v, "_utype"):
      v = v._utype(v)
    try:
      t = YANGDynClass(v,base=unicode, is_leaf=True, yang_name="username", rest_name="username", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'info': u'Username'}}, namespace='urn:brocade.com:mgmt:brocade-firmware', defining_module='brocade-firmware', yang_type='string', is_config=True)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """username must be of a type compatible with string""",
          'defined-type': "string",
          'generated-type': """YANGDynClass(base=unicode, is_leaf=True, yang_name="username", rest_name="username", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'info': u'Username'}}, namespace='urn:brocade.com:mgmt:brocade-firmware', defining_module='brocade-firmware', yang_type='string', is_config=True)""",
        })

    self.__username = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_username(self):
    self.__username = YANGDynClass(base=unicode, is_leaf=True, yang_name="username", rest_name="username", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'info': u'Username'}}, namespace='urn:brocade.com:mgmt:brocade-firmware', defining_module='brocade-firmware', yang_type='string', is_config=True)


  def _get_pass_(self):
    """
    Getter method for pass_, mapped from YANG variable /firmware/autoupgrade_params/pass (string)
    """
    return self.__pass_
      
  def _set_pass_(self, v, load=False):
    """
    Setter method for pass_, mapped from YANG variable /firmware/autoupgrade_params/pass (string)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_pass_ is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_pass_() directly.
    """
    if hasattr(v, "_utype"):
      v = v._utype(v)
    try:
      t = YANGDynClass(v,base=unicode, is_leaf=True, yang_name="pass", rest_name="password", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'info': u'Password', u'alt-name': u'password', u'suppress-echo': u'true'}}, namespace='urn:brocade.com:mgmt:brocade-firmware', defining_module='brocade-firmware', yang_type='string', is_config=True)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """pass_ must be of a type compatible with string""",
          'defined-type': "string",
          'generated-type': """YANGDynClass(base=unicode, is_leaf=True, yang_name="pass", rest_name="password", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'info': u'Password', u'alt-name': u'password', u'suppress-echo': u'true'}}, namespace='urn:brocade.com:mgmt:brocade-firmware', defining_module='brocade-firmware', yang_type='string', is_config=True)""",
        })

    self.__pass_ = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_pass_(self):
    self.__pass_ = YANGDynClass(base=unicode, is_leaf=True, yang_name="pass", rest_name="password", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'info': u'Password', u'alt-name': u'password', u'suppress-echo': u'true'}}, namespace='urn:brocade.com:mgmt:brocade-firmware', defining_module='brocade-firmware', yang_type='string', is_config=True)

  path = __builtin__.property(_get_path, _set_path)
  protocol = __builtin__.property(_get_protocol, _set_protocol)
  ipaddress = __builtin__.property(_get_ipaddress, _set_ipaddress)
  username = __builtin__.property(_get_username, _set_username)
  pass_ = __builtin__.property(_get_pass_, _set_pass_)


  _pyangbind_elements = {'path': path, 'protocol': protocol, 'ipaddress': ipaddress, 'username': username, 'pass_': pass_, }


