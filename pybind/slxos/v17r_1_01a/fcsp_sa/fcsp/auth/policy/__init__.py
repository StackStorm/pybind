
from operator import attrgetter
import pyangbind.lib.xpathhelper as xpathhelper
from pyangbind.lib.yangtypes import RestrictedPrecisionDecimalType, RestrictedClassType, TypedListType
from pyangbind.lib.yangtypes import YANGBool, YANGListType, YANGDynClass, ReferenceType
from pyangbind.lib.base import PybindBase
from decimal import Decimal
from bitarray import bitarray
import __builtin__
class policy(PybindBase):
  """
  This class was auto-generated by the PythonClass plugin for PYANG
  from YANG module brocade-fc-auth - based on the path /fcsp-sa/fcsp/auth/policy. Each member element of
  the container is represented as a class variable - with a specific
  YANG type.
  """
  __slots__ = ('_pybind_generated_by', '_path_helper', '_yang_name', '_rest_name', '_extmethods', '__switch',)

  _yang_name = 'policy'
  _rest_name = 'policy'

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
    self.__switch = YANGDynClass(base=RestrictedClassType(base_type=unicode,                                     restriction_type="dict_key",                                     restriction_arg={u'active': {}, u'on': {}, u'off': {}, u'passive': {}},), default=unicode("passive"), is_leaf=True, yang_name="switch", rest_name="switch", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'info': u'Enable switch policy'}}, namespace='urn:brocade.com:mgmt:brocade-fc-auth', defining_module='brocade-fc-auth', yang_type='fcsp-switch-policy-state', is_config=True)

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
      return [u'fcsp-sa', u'fcsp', u'auth', u'policy']

  def _rest_path(self):
    if hasattr(self, "_parent"):
      if self._rest_name:
        return self._parent._rest_path()+[self._rest_name]
      else:
        return self._parent._rest_path()
    else:
      return [u'fcsp', u'auth', u'policy']

  def _get_switch(self):
    """
    Getter method for switch, mapped from YANG variable /fcsp_sa/fcsp/auth/policy/switch (fcsp-switch-policy-state)
    """
    return self.__switch
      
  def _set_switch(self, v, load=False):
    """
    Setter method for switch, mapped from YANG variable /fcsp_sa/fcsp/auth/policy/switch (fcsp-switch-policy-state)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_switch is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_switch() directly.
    """
    if hasattr(v, "_utype"):
      v = v._utype(v)
    try:
      t = YANGDynClass(v,base=RestrictedClassType(base_type=unicode,                                     restriction_type="dict_key",                                     restriction_arg={u'active': {}, u'on': {}, u'off': {}, u'passive': {}},), default=unicode("passive"), is_leaf=True, yang_name="switch", rest_name="switch", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'info': u'Enable switch policy'}}, namespace='urn:brocade.com:mgmt:brocade-fc-auth', defining_module='brocade-fc-auth', yang_type='fcsp-switch-policy-state', is_config=True)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """switch must be of a type compatible with fcsp-switch-policy-state""",
          'defined-type': "brocade-fc-auth:fcsp-switch-policy-state",
          'generated-type': """YANGDynClass(base=RestrictedClassType(base_type=unicode,                                     restriction_type="dict_key",                                     restriction_arg={u'active': {}, u'on': {}, u'off': {}, u'passive': {}},), default=unicode("passive"), is_leaf=True, yang_name="switch", rest_name="switch", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'info': u'Enable switch policy'}}, namespace='urn:brocade.com:mgmt:brocade-fc-auth', defining_module='brocade-fc-auth', yang_type='fcsp-switch-policy-state', is_config=True)""",
        })

    self.__switch = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_switch(self):
    self.__switch = YANGDynClass(base=RestrictedClassType(base_type=unicode,                                     restriction_type="dict_key",                                     restriction_arg={u'active': {}, u'on': {}, u'off': {}, u'passive': {}},), default=unicode("passive"), is_leaf=True, yang_name="switch", rest_name="switch", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'info': u'Enable switch policy'}}, namespace='urn:brocade.com:mgmt:brocade-fc-auth', defining_module='brocade-fc-auth', yang_type='fcsp-switch-policy-state', is_config=True)

  switch = __builtin__.property(_get_switch, _set_switch)


  _pyangbind_elements = {'switch': switch, }


