
from operator import attrgetter
import pyangbind.lib.xpathhelper as xpathhelper
from pyangbind.lib.yangtypes import RestrictedPrecisionDecimalType, RestrictedClassType, TypedListType
from pyangbind.lib.yangtypes import YANGBool, YANGListType, YANGDynClass, ReferenceType
from pyangbind.lib.base import PybindBase
from decimal import Decimal
from bitarray import bitarray
import __builtin__
class router_preference(PybindBase):
  """
  This class was auto-generated by the PythonClass plugin for PYANG
  from YANG module brocade-common-def - based on the path /routing-system/interface/ve/ipv6/ipv6-nd-ra/ipv6-intf-cmds/nd/router-preference. Each member element of
  the container is represented as a class variable - with a specific
  YANG type.
  """
  __slots__ = ('_pybind_generated_by', '_path_helper', '_yang_name', '_rest_name', '_extmethods', '__router_pref_high','__router_pref_low','__router_pref_medium',)

  _yang_name = 'router-preference'
  _rest_name = 'router-preference'

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
    self.__router_pref_high = YANGDynClass(base=YANGBool, is_leaf=True, yang_name="router-pref-high", rest_name="high", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'cli-full-command': None, u'info': u'Set router-preference to high', u'alt-name': u'high', u'cli-full-no': None}}, namespace='urn:brocade.com:mgmt:brocade-ipv6-nd-ra', defining_module='brocade-ipv6-nd-ra', yang_type='empty', is_config=True)
    self.__router_pref_medium = YANGDynClass(base=YANGBool, is_leaf=True, yang_name="router-pref-medium", rest_name="medium", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'cli-full-command': None, u'info': u'Set router-preference to medium', u'alt-name': u'medium', u'cli-full-no': None}}, namespace='urn:brocade.com:mgmt:brocade-ipv6-nd-ra', defining_module='brocade-ipv6-nd-ra', yang_type='empty', is_config=True)
    self.__router_pref_low = YANGDynClass(base=YANGBool, is_leaf=True, yang_name="router-pref-low", rest_name="low", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'cli-full-command': None, u'info': u' Set router-preference to low', u'alt-name': u'low', u'cli-full-no': None}}, namespace='urn:brocade.com:mgmt:brocade-ipv6-nd-ra', defining_module='brocade-ipv6-nd-ra', yang_type='empty', is_config=True)

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
      return [u'routing-system', u'interface', u've', u'ipv6', u'ipv6-nd-ra', u'ipv6-intf-cmds', u'nd', u'router-preference']

  def _rest_path(self):
    if hasattr(self, "_parent"):
      if self._rest_name:
        return self._parent._rest_path()+[self._rest_name]
      else:
        return self._parent._rest_path()
    else:
      return [u'interface', u'Ve', u'ipv6', u'nd', u'router-preference']

  def _get_router_pref_high(self):
    """
    Getter method for router_pref_high, mapped from YANG variable /routing_system/interface/ve/ipv6/ipv6_nd_ra/ipv6_intf_cmds/nd/router_preference/router_pref_high (empty)
    """
    return self.__router_pref_high
      
  def _set_router_pref_high(self, v, load=False):
    """
    Setter method for router_pref_high, mapped from YANG variable /routing_system/interface/ve/ipv6/ipv6_nd_ra/ipv6_intf_cmds/nd/router_preference/router_pref_high (empty)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_router_pref_high is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_router_pref_high() directly.
    """
    if hasattr(v, "_utype"):
      v = v._utype(v)
    try:
      t = YANGDynClass(v,base=YANGBool, is_leaf=True, yang_name="router-pref-high", rest_name="high", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'cli-full-command': None, u'info': u'Set router-preference to high', u'alt-name': u'high', u'cli-full-no': None}}, namespace='urn:brocade.com:mgmt:brocade-ipv6-nd-ra', defining_module='brocade-ipv6-nd-ra', yang_type='empty', is_config=True)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """router_pref_high must be of a type compatible with empty""",
          'defined-type': "empty",
          'generated-type': """YANGDynClass(base=YANGBool, is_leaf=True, yang_name="router-pref-high", rest_name="high", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'cli-full-command': None, u'info': u'Set router-preference to high', u'alt-name': u'high', u'cli-full-no': None}}, namespace='urn:brocade.com:mgmt:brocade-ipv6-nd-ra', defining_module='brocade-ipv6-nd-ra', yang_type='empty', is_config=True)""",
        })

    self.__router_pref_high = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_router_pref_high(self):
    self.__router_pref_high = YANGDynClass(base=YANGBool, is_leaf=True, yang_name="router-pref-high", rest_name="high", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'cli-full-command': None, u'info': u'Set router-preference to high', u'alt-name': u'high', u'cli-full-no': None}}, namespace='urn:brocade.com:mgmt:brocade-ipv6-nd-ra', defining_module='brocade-ipv6-nd-ra', yang_type='empty', is_config=True)


  def _get_router_pref_low(self):
    """
    Getter method for router_pref_low, mapped from YANG variable /routing_system/interface/ve/ipv6/ipv6_nd_ra/ipv6_intf_cmds/nd/router_preference/router_pref_low (empty)
    """
    return self.__router_pref_low
      
  def _set_router_pref_low(self, v, load=False):
    """
    Setter method for router_pref_low, mapped from YANG variable /routing_system/interface/ve/ipv6/ipv6_nd_ra/ipv6_intf_cmds/nd/router_preference/router_pref_low (empty)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_router_pref_low is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_router_pref_low() directly.
    """
    if hasattr(v, "_utype"):
      v = v._utype(v)
    try:
      t = YANGDynClass(v,base=YANGBool, is_leaf=True, yang_name="router-pref-low", rest_name="low", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'cli-full-command': None, u'info': u' Set router-preference to low', u'alt-name': u'low', u'cli-full-no': None}}, namespace='urn:brocade.com:mgmt:brocade-ipv6-nd-ra', defining_module='brocade-ipv6-nd-ra', yang_type='empty', is_config=True)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """router_pref_low must be of a type compatible with empty""",
          'defined-type': "empty",
          'generated-type': """YANGDynClass(base=YANGBool, is_leaf=True, yang_name="router-pref-low", rest_name="low", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'cli-full-command': None, u'info': u' Set router-preference to low', u'alt-name': u'low', u'cli-full-no': None}}, namespace='urn:brocade.com:mgmt:brocade-ipv6-nd-ra', defining_module='brocade-ipv6-nd-ra', yang_type='empty', is_config=True)""",
        })

    self.__router_pref_low = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_router_pref_low(self):
    self.__router_pref_low = YANGDynClass(base=YANGBool, is_leaf=True, yang_name="router-pref-low", rest_name="low", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'cli-full-command': None, u'info': u' Set router-preference to low', u'alt-name': u'low', u'cli-full-no': None}}, namespace='urn:brocade.com:mgmt:brocade-ipv6-nd-ra', defining_module='brocade-ipv6-nd-ra', yang_type='empty', is_config=True)


  def _get_router_pref_medium(self):
    """
    Getter method for router_pref_medium, mapped from YANG variable /routing_system/interface/ve/ipv6/ipv6_nd_ra/ipv6_intf_cmds/nd/router_preference/router_pref_medium (empty)
    """
    return self.__router_pref_medium
      
  def _set_router_pref_medium(self, v, load=False):
    """
    Setter method for router_pref_medium, mapped from YANG variable /routing_system/interface/ve/ipv6/ipv6_nd_ra/ipv6_intf_cmds/nd/router_preference/router_pref_medium (empty)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_router_pref_medium is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_router_pref_medium() directly.
    """
    if hasattr(v, "_utype"):
      v = v._utype(v)
    try:
      t = YANGDynClass(v,base=YANGBool, is_leaf=True, yang_name="router-pref-medium", rest_name="medium", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'cli-full-command': None, u'info': u'Set router-preference to medium', u'alt-name': u'medium', u'cli-full-no': None}}, namespace='urn:brocade.com:mgmt:brocade-ipv6-nd-ra', defining_module='brocade-ipv6-nd-ra', yang_type='empty', is_config=True)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """router_pref_medium must be of a type compatible with empty""",
          'defined-type': "empty",
          'generated-type': """YANGDynClass(base=YANGBool, is_leaf=True, yang_name="router-pref-medium", rest_name="medium", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'cli-full-command': None, u'info': u'Set router-preference to medium', u'alt-name': u'medium', u'cli-full-no': None}}, namespace='urn:brocade.com:mgmt:brocade-ipv6-nd-ra', defining_module='brocade-ipv6-nd-ra', yang_type='empty', is_config=True)""",
        })

    self.__router_pref_medium = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_router_pref_medium(self):
    self.__router_pref_medium = YANGDynClass(base=YANGBool, is_leaf=True, yang_name="router-pref-medium", rest_name="medium", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'cli-full-command': None, u'info': u'Set router-preference to medium', u'alt-name': u'medium', u'cli-full-no': None}}, namespace='urn:brocade.com:mgmt:brocade-ipv6-nd-ra', defining_module='brocade-ipv6-nd-ra', yang_type='empty', is_config=True)

  router_pref_high = __builtin__.property(_get_router_pref_high, _set_router_pref_high)
  router_pref_low = __builtin__.property(_get_router_pref_low, _set_router_pref_low)
  router_pref_medium = __builtin__.property(_get_router_pref_medium, _set_router_pref_medium)


  _pyangbind_elements = {'router_pref_high': router_pref_high, 'router_pref_low': router_pref_low, 'router_pref_medium': router_pref_medium, }


