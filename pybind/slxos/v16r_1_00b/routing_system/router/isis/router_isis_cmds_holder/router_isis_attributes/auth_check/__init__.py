
from operator import attrgetter
import pyangbind.lib.xpathhelper as xpathhelper
from pyangbind.lib.yangtypes import RestrictedPrecisionDecimalType, RestrictedClassType, TypedListType
from pyangbind.lib.yangtypes import YANGBool, YANGListType, YANGDynClass, ReferenceType
from pyangbind.lib.base import PybindBase
from decimal import Decimal
from bitarray import bitarray
import __builtin__
import auth_check_level1
import auth_check_level2
class auth_check(PybindBase):
  """
  This class was auto-generated by the PythonClass plugin for PYANG
  from YANG module brocade-common-def - based on the path /routing-system/router/isis/router-isis-cmds-holder/router-isis-attributes/auth-check. Each member element of
  the container is represented as a class variable - with a specific
  YANG type.
  """
  __slots__ = ('_pybind_generated_by', '_path_helper', '_yang_name', '_rest_name', '_extmethods', '__auth_check_level1','__auth_check_level2',)

  _yang_name = 'auth-check'
  _rest_name = 'auth-check'

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
    self.__auth_check_level1 = YANGDynClass(base=auth_check_level1.auth_check_level1, is_container='container', yang_name="auth-check-level1", rest_name="level-1", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'info': u'Authenticate incoming PDUs for Level-1 LSPs, CSNP, PSNP', u'alt-name': u'level-1', u'cli-incomplete-no': None, u'cli-incomplete-command': None}}, namespace='urn:brocade.com:mgmt:brocade-isis', defining_module='brocade-isis', yang_type='container', is_config=True)
    self.__auth_check_level2 = YANGDynClass(base=auth_check_level2.auth_check_level2, is_container='container', yang_name="auth-check-level2", rest_name="level-2", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'info': u'Authenticate incoming PDUs for Level-2 LSPs, CSNP, PSNP', u'alt-name': u'level-2', u'cli-incomplete-no': None, u'cli-incomplete-command': None}}, namespace='urn:brocade.com:mgmt:brocade-isis', defining_module='brocade-isis', yang_type='container', is_config=True)

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
      return [u'routing-system', u'router', u'isis', u'router-isis-cmds-holder', u'router-isis-attributes', u'auth-check']

  def _rest_path(self):
    if hasattr(self, "_parent"):
      if self._rest_name:
        return self._parent._rest_path()+[self._rest_name]
      else:
        return self._parent._rest_path()
    else:
      return [u'router', u'isis', u'auth-check']

  def _get_auth_check_level1(self):
    """
    Getter method for auth_check_level1, mapped from YANG variable /routing_system/router/isis/router_isis_cmds_holder/router_isis_attributes/auth_check/auth_check_level1 (container)
    """
    return self.__auth_check_level1
      
  def _set_auth_check_level1(self, v, load=False):
    """
    Setter method for auth_check_level1, mapped from YANG variable /routing_system/router/isis/router_isis_cmds_holder/router_isis_attributes/auth_check/auth_check_level1 (container)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_auth_check_level1 is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_auth_check_level1() directly.
    """
    if hasattr(v, "_utype"):
      v = v._utype(v)
    try:
      t = YANGDynClass(v,base=auth_check_level1.auth_check_level1, is_container='container', yang_name="auth-check-level1", rest_name="level-1", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'info': u'Authenticate incoming PDUs for Level-1 LSPs, CSNP, PSNP', u'alt-name': u'level-1', u'cli-incomplete-no': None, u'cli-incomplete-command': None}}, namespace='urn:brocade.com:mgmt:brocade-isis', defining_module='brocade-isis', yang_type='container', is_config=True)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """auth_check_level1 must be of a type compatible with container""",
          'defined-type': "container",
          'generated-type': """YANGDynClass(base=auth_check_level1.auth_check_level1, is_container='container', yang_name="auth-check-level1", rest_name="level-1", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'info': u'Authenticate incoming PDUs for Level-1 LSPs, CSNP, PSNP', u'alt-name': u'level-1', u'cli-incomplete-no': None, u'cli-incomplete-command': None}}, namespace='urn:brocade.com:mgmt:brocade-isis', defining_module='brocade-isis', yang_type='container', is_config=True)""",
        })

    self.__auth_check_level1 = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_auth_check_level1(self):
    self.__auth_check_level1 = YANGDynClass(base=auth_check_level1.auth_check_level1, is_container='container', yang_name="auth-check-level1", rest_name="level-1", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'info': u'Authenticate incoming PDUs for Level-1 LSPs, CSNP, PSNP', u'alt-name': u'level-1', u'cli-incomplete-no': None, u'cli-incomplete-command': None}}, namespace='urn:brocade.com:mgmt:brocade-isis', defining_module='brocade-isis', yang_type='container', is_config=True)


  def _get_auth_check_level2(self):
    """
    Getter method for auth_check_level2, mapped from YANG variable /routing_system/router/isis/router_isis_cmds_holder/router_isis_attributes/auth_check/auth_check_level2 (container)
    """
    return self.__auth_check_level2
      
  def _set_auth_check_level2(self, v, load=False):
    """
    Setter method for auth_check_level2, mapped from YANG variable /routing_system/router/isis/router_isis_cmds_holder/router_isis_attributes/auth_check/auth_check_level2 (container)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_auth_check_level2 is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_auth_check_level2() directly.
    """
    if hasattr(v, "_utype"):
      v = v._utype(v)
    try:
      t = YANGDynClass(v,base=auth_check_level2.auth_check_level2, is_container='container', yang_name="auth-check-level2", rest_name="level-2", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'info': u'Authenticate incoming PDUs for Level-2 LSPs, CSNP, PSNP', u'alt-name': u'level-2', u'cli-incomplete-no': None, u'cli-incomplete-command': None}}, namespace='urn:brocade.com:mgmt:brocade-isis', defining_module='brocade-isis', yang_type='container', is_config=True)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """auth_check_level2 must be of a type compatible with container""",
          'defined-type': "container",
          'generated-type': """YANGDynClass(base=auth_check_level2.auth_check_level2, is_container='container', yang_name="auth-check-level2", rest_name="level-2", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'info': u'Authenticate incoming PDUs for Level-2 LSPs, CSNP, PSNP', u'alt-name': u'level-2', u'cli-incomplete-no': None, u'cli-incomplete-command': None}}, namespace='urn:brocade.com:mgmt:brocade-isis', defining_module='brocade-isis', yang_type='container', is_config=True)""",
        })

    self.__auth_check_level2 = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_auth_check_level2(self):
    self.__auth_check_level2 = YANGDynClass(base=auth_check_level2.auth_check_level2, is_container='container', yang_name="auth-check-level2", rest_name="level-2", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'info': u'Authenticate incoming PDUs for Level-2 LSPs, CSNP, PSNP', u'alt-name': u'level-2', u'cli-incomplete-no': None, u'cli-incomplete-command': None}}, namespace='urn:brocade.com:mgmt:brocade-isis', defining_module='brocade-isis', yang_type='container', is_config=True)

  auth_check_level1 = __builtin__.property(_get_auth_check_level1, _set_auth_check_level1)
  auth_check_level2 = __builtin__.property(_get_auth_check_level2, _set_auth_check_level2)


  _pyangbind_elements = {'auth_check_level1': auth_check_level1, 'auth_check_level2': auth_check_level2, }


