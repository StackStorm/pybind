
from operator import attrgetter
import pyangbind.lib.xpathhelper as xpathhelper
from pyangbind.lib.yangtypes import RestrictedPrecisionDecimalType, RestrictedClassType, TypedListType
from pyangbind.lib.yangtypes import YANGBool, YANGListType, YANGDynClass, ReferenceType
from pyangbind.lib.base import PybindBase
from decimal import Decimal
from bitarray import bitarray
import __builtin__
class helper(PybindBase):
  """
  This class was auto-generated by the PythonClass plugin for PYANG
  from YANG module brocade-rbridge - based on the path /rbridge-id/ipv6/router/ospf/graceful-restart/helper. Each member element of
  the container is represented as a class variable - with a specific
  YANG type.

  YANG Description: Set graceful restart helper options
  """
  __slots__ = ('_pybind_generated_by', '_path_helper', '_yang_name', '_rest_name', '_extmethods', '__graceful_restart_helper_disable','__graceful_restart_helper_strict_lsa_checking',)

  _yang_name = 'helper'
  _rest_name = 'helper'

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
    self.__graceful_restart_helper_strict_lsa_checking = YANGDynClass(base=YANGBool, is_leaf=True, yang_name="graceful-restart-helper-strict-lsa-checking", rest_name="strict-lsa-checking", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'cli-full-command': None, u'info': u'Set strict LSA checking', u'alt-name': u'strict-lsa-checking'}}, namespace='urn:brocade.com:mgmt:brocade-ospfv3', defining_module='brocade-ospfv3', yang_type='empty', is_config=True)
    self.__graceful_restart_helper_disable = YANGDynClass(base=YANGBool, is_leaf=True, yang_name="graceful-restart-helper-disable", rest_name="disable", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'cli-full-command': None, u'info': u'Disable graceful restart helper capability', u'alt-name': u'disable'}}, namespace='urn:brocade.com:mgmt:brocade-ospfv3', defining_module='brocade-ospfv3', yang_type='empty', is_config=True)

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
      return [u'rbridge-id', u'ipv6', u'router', u'ospf', u'graceful-restart', u'helper']

  def _rest_path(self):
    if hasattr(self, "_parent"):
      if self._rest_name:
        return self._parent._rest_path()+[self._rest_name]
      else:
        return self._parent._rest_path()
    else:
      return [u'rbridge-id', u'ipv6', u'router', u'ospf', u'graceful-restart', u'helper']

  def _get_graceful_restart_helper_disable(self):
    """
    Getter method for graceful_restart_helper_disable, mapped from YANG variable /rbridge_id/ipv6/router/ospf/graceful_restart/helper/graceful_restart_helper_disable (empty)

    YANG Description: Disable graceful restart helper capability
    """
    return self.__graceful_restart_helper_disable
      
  def _set_graceful_restart_helper_disable(self, v, load=False):
    """
    Setter method for graceful_restart_helper_disable, mapped from YANG variable /rbridge_id/ipv6/router/ospf/graceful_restart/helper/graceful_restart_helper_disable (empty)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_graceful_restart_helper_disable is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_graceful_restart_helper_disable() directly.

    YANG Description: Disable graceful restart helper capability
    """
    if hasattr(v, "_utype"):
      v = v._utype(v)
    try:
      t = YANGDynClass(v,base=YANGBool, is_leaf=True, yang_name="graceful-restart-helper-disable", rest_name="disable", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'cli-full-command': None, u'info': u'Disable graceful restart helper capability', u'alt-name': u'disable'}}, namespace='urn:brocade.com:mgmt:brocade-ospfv3', defining_module='brocade-ospfv3', yang_type='empty', is_config=True)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """graceful_restart_helper_disable must be of a type compatible with empty""",
          'defined-type': "empty",
          'generated-type': """YANGDynClass(base=YANGBool, is_leaf=True, yang_name="graceful-restart-helper-disable", rest_name="disable", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'cli-full-command': None, u'info': u'Disable graceful restart helper capability', u'alt-name': u'disable'}}, namespace='urn:brocade.com:mgmt:brocade-ospfv3', defining_module='brocade-ospfv3', yang_type='empty', is_config=True)""",
        })

    self.__graceful_restart_helper_disable = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_graceful_restart_helper_disable(self):
    self.__graceful_restart_helper_disable = YANGDynClass(base=YANGBool, is_leaf=True, yang_name="graceful-restart-helper-disable", rest_name="disable", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'cli-full-command': None, u'info': u'Disable graceful restart helper capability', u'alt-name': u'disable'}}, namespace='urn:brocade.com:mgmt:brocade-ospfv3', defining_module='brocade-ospfv3', yang_type='empty', is_config=True)


  def _get_graceful_restart_helper_strict_lsa_checking(self):
    """
    Getter method for graceful_restart_helper_strict_lsa_checking, mapped from YANG variable /rbridge_id/ipv6/router/ospf/graceful_restart/helper/graceful_restart_helper_strict_lsa_checking (empty)

    YANG Description: Set strict LSA checking
    """
    return self.__graceful_restart_helper_strict_lsa_checking
      
  def _set_graceful_restart_helper_strict_lsa_checking(self, v, load=False):
    """
    Setter method for graceful_restart_helper_strict_lsa_checking, mapped from YANG variable /rbridge_id/ipv6/router/ospf/graceful_restart/helper/graceful_restart_helper_strict_lsa_checking (empty)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_graceful_restart_helper_strict_lsa_checking is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_graceful_restart_helper_strict_lsa_checking() directly.

    YANG Description: Set strict LSA checking
    """
    if hasattr(v, "_utype"):
      v = v._utype(v)
    try:
      t = YANGDynClass(v,base=YANGBool, is_leaf=True, yang_name="graceful-restart-helper-strict-lsa-checking", rest_name="strict-lsa-checking", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'cli-full-command': None, u'info': u'Set strict LSA checking', u'alt-name': u'strict-lsa-checking'}}, namespace='urn:brocade.com:mgmt:brocade-ospfv3', defining_module='brocade-ospfv3', yang_type='empty', is_config=True)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """graceful_restart_helper_strict_lsa_checking must be of a type compatible with empty""",
          'defined-type': "empty",
          'generated-type': """YANGDynClass(base=YANGBool, is_leaf=True, yang_name="graceful-restart-helper-strict-lsa-checking", rest_name="strict-lsa-checking", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'cli-full-command': None, u'info': u'Set strict LSA checking', u'alt-name': u'strict-lsa-checking'}}, namespace='urn:brocade.com:mgmt:brocade-ospfv3', defining_module='brocade-ospfv3', yang_type='empty', is_config=True)""",
        })

    self.__graceful_restart_helper_strict_lsa_checking = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_graceful_restart_helper_strict_lsa_checking(self):
    self.__graceful_restart_helper_strict_lsa_checking = YANGDynClass(base=YANGBool, is_leaf=True, yang_name="graceful-restart-helper-strict-lsa-checking", rest_name="strict-lsa-checking", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'cli-full-command': None, u'info': u'Set strict LSA checking', u'alt-name': u'strict-lsa-checking'}}, namespace='urn:brocade.com:mgmt:brocade-ospfv3', defining_module='brocade-ospfv3', yang_type='empty', is_config=True)

  graceful_restart_helper_disable = __builtin__.property(_get_graceful_restart_helper_disable, _set_graceful_restart_helper_disable)
  graceful_restart_helper_strict_lsa_checking = __builtin__.property(_get_graceful_restart_helper_strict_lsa_checking, _set_graceful_restart_helper_strict_lsa_checking)


  _pyangbind_elements = {'graceful_restart_helper_disable': graceful_restart_helper_disable, 'graceful_restart_helper_strict_lsa_checking': graceful_restart_helper_strict_lsa_checking, }


