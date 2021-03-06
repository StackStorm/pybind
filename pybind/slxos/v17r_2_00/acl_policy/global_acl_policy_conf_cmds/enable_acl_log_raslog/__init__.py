
from operator import attrgetter
import pyangbind.lib.xpathhelper as xpathhelper
from pyangbind.lib.yangtypes import RestrictedPrecisionDecimalType, RestrictedClassType, TypedListType
from pyangbind.lib.yangtypes import YANGBool, YANGListType, YANGDynClass, ReferenceType
from pyangbind.lib.base import PybindBase
from decimal import Decimal
from bitarray import bitarray
import __builtin__
class enable_acl_log_raslog(PybindBase):
  """
  This class was auto-generated by the PythonClass plugin for PYANG
  from YANG module brocade-acl-policy - based on the path /acl-policy/global-acl-policy-conf-cmds/enable-acl-log-raslog. Each member element of
  the container is represented as a class variable - with a specific
  YANG type.
  """
  __slots__ = ('_pybind_generated_by', '_path_helper', '_yang_name', '_rest_name', '_extmethods', '__acl_log_raslog','__log_interval',)

  _yang_name = 'enable-acl-log-raslog'
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
    self.__acl_log_raslog = YANGDynClass(base=YANGBool, is_leaf=True, yang_name="acl-log-raslog", rest_name="acl-log-raslog", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'info': u'Enable ACL log message to Raslog'}}, namespace='urn:brocade.com:mgmt:brocade-acl-policy', defining_module='brocade-acl-policy', yang_type='empty', is_config=True)
    self.__log_interval = YANGDynClass(base=RestrictedClassType(base_type=RestrictedClassType(base_type=long, restriction_dict={'range': ['0..4294967295']}, int_size=32), restriction_dict={'range': [u'1..10']}), default=RestrictedClassType(base_type=long, restriction_dict={'range': ['0..4294967295']}, int_size=32)(5), is_leaf=True, yang_name="log-interval", rest_name="log-interval", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'info': u'Time interval between ACL log Message to Raslog', u'cli-optional-in-sequence': None}}, namespace='urn:brocade.com:mgmt:brocade-acl-policy', defining_module='brocade-acl-policy', yang_type='common-def:time-interval-sec', is_config=True)

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
      return [u'acl-policy', u'global-acl-policy-conf-cmds', u'enable-acl-log-raslog']

  def _rest_path(self):
    if hasattr(self, "_parent"):
      if self._rest_name:
        return self._parent._rest_path()+[self._rest_name]
      else:
        return self._parent._rest_path()
    else:
      return [u'acl-policy']

  def _get_acl_log_raslog(self):
    """
    Getter method for acl_log_raslog, mapped from YANG variable /acl_policy/global_acl_policy_conf_cmds/enable_acl_log_raslog/acl_log_raslog (empty)
    """
    return self.__acl_log_raslog
      
  def _set_acl_log_raslog(self, v, load=False):
    """
    Setter method for acl_log_raslog, mapped from YANG variable /acl_policy/global_acl_policy_conf_cmds/enable_acl_log_raslog/acl_log_raslog (empty)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_acl_log_raslog is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_acl_log_raslog() directly.
    """
    if hasattr(v, "_utype"):
      v = v._utype(v)
    try:
      t = YANGDynClass(v,base=YANGBool, is_leaf=True, yang_name="acl-log-raslog", rest_name="acl-log-raslog", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'info': u'Enable ACL log message to Raslog'}}, namespace='urn:brocade.com:mgmt:brocade-acl-policy', defining_module='brocade-acl-policy', yang_type='empty', is_config=True)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """acl_log_raslog must be of a type compatible with empty""",
          'defined-type': "empty",
          'generated-type': """YANGDynClass(base=YANGBool, is_leaf=True, yang_name="acl-log-raslog", rest_name="acl-log-raslog", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'info': u'Enable ACL log message to Raslog'}}, namespace='urn:brocade.com:mgmt:brocade-acl-policy', defining_module='brocade-acl-policy', yang_type='empty', is_config=True)""",
        })

    self.__acl_log_raslog = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_acl_log_raslog(self):
    self.__acl_log_raslog = YANGDynClass(base=YANGBool, is_leaf=True, yang_name="acl-log-raslog", rest_name="acl-log-raslog", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'info': u'Enable ACL log message to Raslog'}}, namespace='urn:brocade.com:mgmt:brocade-acl-policy', defining_module='brocade-acl-policy', yang_type='empty', is_config=True)


  def _get_log_interval(self):
    """
    Getter method for log_interval, mapped from YANG variable /acl_policy/global_acl_policy_conf_cmds/enable_acl_log_raslog/log_interval (common-def:time-interval-sec)
    """
    return self.__log_interval
      
  def _set_log_interval(self, v, load=False):
    """
    Setter method for log_interval, mapped from YANG variable /acl_policy/global_acl_policy_conf_cmds/enable_acl_log_raslog/log_interval (common-def:time-interval-sec)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_log_interval is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_log_interval() directly.
    """
    if hasattr(v, "_utype"):
      v = v._utype(v)
    try:
      t = YANGDynClass(v,base=RestrictedClassType(base_type=RestrictedClassType(base_type=long, restriction_dict={'range': ['0..4294967295']}, int_size=32), restriction_dict={'range': [u'1..10']}), default=RestrictedClassType(base_type=long, restriction_dict={'range': ['0..4294967295']}, int_size=32)(5), is_leaf=True, yang_name="log-interval", rest_name="log-interval", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'info': u'Time interval between ACL log Message to Raslog', u'cli-optional-in-sequence': None}}, namespace='urn:brocade.com:mgmt:brocade-acl-policy', defining_module='brocade-acl-policy', yang_type='common-def:time-interval-sec', is_config=True)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """log_interval must be of a type compatible with common-def:time-interval-sec""",
          'defined-type': "common-def:time-interval-sec",
          'generated-type': """YANGDynClass(base=RestrictedClassType(base_type=RestrictedClassType(base_type=long, restriction_dict={'range': ['0..4294967295']}, int_size=32), restriction_dict={'range': [u'1..10']}), default=RestrictedClassType(base_type=long, restriction_dict={'range': ['0..4294967295']}, int_size=32)(5), is_leaf=True, yang_name="log-interval", rest_name="log-interval", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'info': u'Time interval between ACL log Message to Raslog', u'cli-optional-in-sequence': None}}, namespace='urn:brocade.com:mgmt:brocade-acl-policy', defining_module='brocade-acl-policy', yang_type='common-def:time-interval-sec', is_config=True)""",
        })

    self.__log_interval = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_log_interval(self):
    self.__log_interval = YANGDynClass(base=RestrictedClassType(base_type=RestrictedClassType(base_type=long, restriction_dict={'range': ['0..4294967295']}, int_size=32), restriction_dict={'range': [u'1..10']}), default=RestrictedClassType(base_type=long, restriction_dict={'range': ['0..4294967295']}, int_size=32)(5), is_leaf=True, yang_name="log-interval", rest_name="log-interval", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'info': u'Time interval between ACL log Message to Raslog', u'cli-optional-in-sequence': None}}, namespace='urn:brocade.com:mgmt:brocade-acl-policy', defining_module='brocade-acl-policy', yang_type='common-def:time-interval-sec', is_config=True)

  acl_log_raslog = __builtin__.property(_get_acl_log_raslog, _set_acl_log_raslog)
  log_interval = __builtin__.property(_get_log_interval, _set_log_interval)


  _pyangbind_elements = {'acl_log_raslog': acl_log_raslog, 'log_interval': log_interval, }


