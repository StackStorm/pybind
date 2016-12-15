
from operator import attrgetter
import pyangbind.lib.xpathhelper as xpathhelper
from pyangbind.lib.yangtypes import RestrictedPrecisionDecimalType, RestrictedClassType, TypedListType
from pyangbind.lib.yangtypes import YANGBool, YANGListType, YANGDynClass, ReferenceType
from pyangbind.lib.base import PybindBase
from decimal import Decimal
from bitarray import bitarray
import __builtin__
import email_list
class sfp(PybindBase):
  """
  This class was auto-generated by the PythonClass plugin for PYANG
  from YANG module brocade-system-monitor - based on the path /system-monitor-mail/sfp. Each member element of
  the container is represented as a class variable - with a specific
  YANG type.
  """
  __slots__ = ('_pybind_generated_by', '_path_helper', '_yang_name', '_rest_name', '_extmethods', '__enable','__email_list',)

  _yang_name = 'sfp'
  _rest_name = 'sfp'

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
    self.__email_list = YANGDynClass(base=YANGListType("email",email_list.email_list, yang_name="email-list", rest_name="", parent=self, is_container='list', user_ordered=False, path_helper=self._path_helper, yang_keys='email', extensions={u'tailf-common': {u'info': u'Configure SFP emails', u'cli-suppress-mode': None, u'cli-suppress-list-no': None, u'cli-drop-node-name': None, u'cli-suppress-key-abbreviation': None, u'callpoint': u'system-monitor-sfp-email'}}), is_container='list', yang_name="email-list", rest_name="", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'info': u'Configure SFP emails', u'cli-suppress-mode': None, u'cli-suppress-list-no': None, u'cli-drop-node-name': None, u'cli-suppress-key-abbreviation': None, u'callpoint': u'system-monitor-sfp-email'}}, namespace='urn:brocade.com:mgmt:brocade-system-monitor', defining_module='brocade-system-monitor', yang_type='list', is_config=True)
    self.__enable = YANGDynClass(base=YANGBool, is_leaf=True, yang_name="enable", rest_name="enable", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'info': u'Enable sfp email alerts', u'cli-full-command': None, u'callpoint': u'system-monitor-mail-sfp-enableflag'}}, namespace='urn:brocade.com:mgmt:brocade-system-monitor', defining_module='brocade-system-monitor', yang_type='empty', is_config=True)

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
      return [u'system-monitor-mail', u'sfp']

  def _rest_path(self):
    if hasattr(self, "_parent"):
      if self._rest_name:
        return self._parent._rest_path()+[self._rest_name]
      else:
        return self._parent._rest_path()
    else:
      return [u'system-monitor-mail', u'sfp']

  def _get_enable(self):
    """
    Getter method for enable, mapped from YANG variable /system_monitor_mail/sfp/enable (empty)
    """
    return self.__enable
      
  def _set_enable(self, v, load=False):
    """
    Setter method for enable, mapped from YANG variable /system_monitor_mail/sfp/enable (empty)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_enable is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_enable() directly.
    """
    if hasattr(v, "_utype"):
      v = v._utype(v)
    try:
      t = YANGDynClass(v,base=YANGBool, is_leaf=True, yang_name="enable", rest_name="enable", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'info': u'Enable sfp email alerts', u'cli-full-command': None, u'callpoint': u'system-monitor-mail-sfp-enableflag'}}, namespace='urn:brocade.com:mgmt:brocade-system-monitor', defining_module='brocade-system-monitor', yang_type='empty', is_config=True)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """enable must be of a type compatible with empty""",
          'defined-type': "empty",
          'generated-type': """YANGDynClass(base=YANGBool, is_leaf=True, yang_name="enable", rest_name="enable", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'info': u'Enable sfp email alerts', u'cli-full-command': None, u'callpoint': u'system-monitor-mail-sfp-enableflag'}}, namespace='urn:brocade.com:mgmt:brocade-system-monitor', defining_module='brocade-system-monitor', yang_type='empty', is_config=True)""",
        })

    self.__enable = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_enable(self):
    self.__enable = YANGDynClass(base=YANGBool, is_leaf=True, yang_name="enable", rest_name="enable", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'info': u'Enable sfp email alerts', u'cli-full-command': None, u'callpoint': u'system-monitor-mail-sfp-enableflag'}}, namespace='urn:brocade.com:mgmt:brocade-system-monitor', defining_module='brocade-system-monitor', yang_type='empty', is_config=True)


  def _get_email_list(self):
    """
    Getter method for email_list, mapped from YANG variable /system_monitor_mail/sfp/email_list (list)
    """
    return self.__email_list
      
  def _set_email_list(self, v, load=False):
    """
    Setter method for email_list, mapped from YANG variable /system_monitor_mail/sfp/email_list (list)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_email_list is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_email_list() directly.
    """
    if hasattr(v, "_utype"):
      v = v._utype(v)
    try:
      t = YANGDynClass(v,base=YANGListType("email",email_list.email_list, yang_name="email-list", rest_name="", parent=self, is_container='list', user_ordered=False, path_helper=self._path_helper, yang_keys='email', extensions={u'tailf-common': {u'info': u'Configure SFP emails', u'cli-suppress-mode': None, u'cli-suppress-list-no': None, u'cli-drop-node-name': None, u'cli-suppress-key-abbreviation': None, u'callpoint': u'system-monitor-sfp-email'}}), is_container='list', yang_name="email-list", rest_name="", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'info': u'Configure SFP emails', u'cli-suppress-mode': None, u'cli-suppress-list-no': None, u'cli-drop-node-name': None, u'cli-suppress-key-abbreviation': None, u'callpoint': u'system-monitor-sfp-email'}}, namespace='urn:brocade.com:mgmt:brocade-system-monitor', defining_module='brocade-system-monitor', yang_type='list', is_config=True)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """email_list must be of a type compatible with list""",
          'defined-type': "list",
          'generated-type': """YANGDynClass(base=YANGListType("email",email_list.email_list, yang_name="email-list", rest_name="", parent=self, is_container='list', user_ordered=False, path_helper=self._path_helper, yang_keys='email', extensions={u'tailf-common': {u'info': u'Configure SFP emails', u'cli-suppress-mode': None, u'cli-suppress-list-no': None, u'cli-drop-node-name': None, u'cli-suppress-key-abbreviation': None, u'callpoint': u'system-monitor-sfp-email'}}), is_container='list', yang_name="email-list", rest_name="", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'info': u'Configure SFP emails', u'cli-suppress-mode': None, u'cli-suppress-list-no': None, u'cli-drop-node-name': None, u'cli-suppress-key-abbreviation': None, u'callpoint': u'system-monitor-sfp-email'}}, namespace='urn:brocade.com:mgmt:brocade-system-monitor', defining_module='brocade-system-monitor', yang_type='list', is_config=True)""",
        })

    self.__email_list = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_email_list(self):
    self.__email_list = YANGDynClass(base=YANGListType("email",email_list.email_list, yang_name="email-list", rest_name="", parent=self, is_container='list', user_ordered=False, path_helper=self._path_helper, yang_keys='email', extensions={u'tailf-common': {u'info': u'Configure SFP emails', u'cli-suppress-mode': None, u'cli-suppress-list-no': None, u'cli-drop-node-name': None, u'cli-suppress-key-abbreviation': None, u'callpoint': u'system-monitor-sfp-email'}}), is_container='list', yang_name="email-list", rest_name="", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'info': u'Configure SFP emails', u'cli-suppress-mode': None, u'cli-suppress-list-no': None, u'cli-drop-node-name': None, u'cli-suppress-key-abbreviation': None, u'callpoint': u'system-monitor-sfp-email'}}, namespace='urn:brocade.com:mgmt:brocade-system-monitor', defining_module='brocade-system-monitor', yang_type='list', is_config=True)

  enable = __builtin__.property(_get_enable, _set_enable)
  email_list = __builtin__.property(_get_email_list, _set_email_list)


  _pyangbind_elements = {'enable': enable, 'email_list': email_list, }


