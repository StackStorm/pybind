
from operator import attrgetter
import pyangbind.lib.xpathhelper as xpathhelper
from pyangbind.lib.yangtypes import RestrictedPrecisionDecimalType, RestrictedClassType, TypedListType
from pyangbind.lib.yangtypes import YANGBool, YANGListType, YANGDynClass, ReferenceType
from pyangbind.lib.base import PybindBase
from decimal import Decimal
from bitarray import bitarray
import __builtin__
class debug_handler(PybindBase):
  """
  This class was auto-generated by the PythonClass plugin for PYANG
  from YANG module brocade-isis-operational - based on the path /isis-state/router-isis-config/debug-handler. Each member element of
  the container is represented as a class variable - with a specific
  YANG type.

  YANG Description: IS-IS debug handler
  """
  __slots__ = ('_pybind_generated_by', '_path_helper', '_yang_name', '_rest_name', '_extmethods', '__debug_nsr',)

  _yang_name = 'debug-handler'
  _rest_name = 'debug-handler'

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
    self.__debug_nsr = YANGDynClass(base=RestrictedClassType(base_type=unicode,                                     restriction_type="dict_key",                                     restriction_arg={u'is-enabled': {'value': 1}, u'is-disabled': {'value': 0}},), is_leaf=True, yang_name="debug-nsr", rest_name="debug-nsr", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='urn:brocade.com:mgmt:brocade-isis-operational', defining_module='brocade-isis-operational', yang_type='isis-status', is_config=False)

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
      return [u'isis-state', u'router-isis-config', u'debug-handler']

  def _rest_path(self):
    if hasattr(self, "_parent"):
      if self._rest_name:
        return self._parent._rest_path()+[self._rest_name]
      else:
        return self._parent._rest_path()
    else:
      return [u'isis-state', u'router-isis-config', u'debug-handler']

  def _get_debug_nsr(self):
    """
    Getter method for debug_nsr, mapped from YANG variable /isis_state/router_isis_config/debug_handler/debug_nsr (isis-status)

    YANG Description: If IS-IS non-stop routing is debug enabled
    """
    return self.__debug_nsr
      
  def _set_debug_nsr(self, v, load=False):
    """
    Setter method for debug_nsr, mapped from YANG variable /isis_state/router_isis_config/debug_handler/debug_nsr (isis-status)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_debug_nsr is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_debug_nsr() directly.

    YANG Description: If IS-IS non-stop routing is debug enabled
    """
    if hasattr(v, "_utype"):
      v = v._utype(v)
    try:
      t = YANGDynClass(v,base=RestrictedClassType(base_type=unicode,                                     restriction_type="dict_key",                                     restriction_arg={u'is-enabled': {'value': 1}, u'is-disabled': {'value': 0}},), is_leaf=True, yang_name="debug-nsr", rest_name="debug-nsr", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='urn:brocade.com:mgmt:brocade-isis-operational', defining_module='brocade-isis-operational', yang_type='isis-status', is_config=False)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """debug_nsr must be of a type compatible with isis-status""",
          'defined-type': "brocade-isis-operational:isis-status",
          'generated-type': """YANGDynClass(base=RestrictedClassType(base_type=unicode,                                     restriction_type="dict_key",                                     restriction_arg={u'is-enabled': {'value': 1}, u'is-disabled': {'value': 0}},), is_leaf=True, yang_name="debug-nsr", rest_name="debug-nsr", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='urn:brocade.com:mgmt:brocade-isis-operational', defining_module='brocade-isis-operational', yang_type='isis-status', is_config=False)""",
        })

    self.__debug_nsr = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_debug_nsr(self):
    self.__debug_nsr = YANGDynClass(base=RestrictedClassType(base_type=unicode,                                     restriction_type="dict_key",                                     restriction_arg={u'is-enabled': {'value': 1}, u'is-disabled': {'value': 0}},), is_leaf=True, yang_name="debug-nsr", rest_name="debug-nsr", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='urn:brocade.com:mgmt:brocade-isis-operational', defining_module='brocade-isis-operational', yang_type='isis-status', is_config=False)

  debug_nsr = __builtin__.property(_get_debug_nsr)


  _pyangbind_elements = {'debug_nsr': debug_nsr, }


