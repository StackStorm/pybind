
from operator import attrgetter
import pyangbind.lib.xpathhelper as xpathhelper
from pyangbind.lib.yangtypes import RestrictedPrecisionDecimalType, RestrictedClassType, TypedListType
from pyangbind.lib.yangtypes import YANGBool, YANGListType, YANGDynClass, ReferenceType
from pyangbind.lib.base import PybindBase
from decimal import Decimal
from bitarray import bitarray
import __builtin__
class pspf6_timer(PybindBase):
  """
  This class was auto-generated by the PythonClass plugin for PYANG
  from YANG module brocade-isis-operational - based on the path /isis-state/router-isis-config/pspf6-timer. Each member element of
  the container is represented as a class variable - with a specific
  YANG type.
  """
  __slots__ = ('_pybind_generated_by', '_path_helper', '_yang_name', '_rest_name', '_extmethods', '__init_delay_time','__hold_down_time','__max_time',)

  _yang_name = 'pspf6-timer'
  _rest_name = 'pspf6-timer'

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
    self.__hold_down_time = YANGDynClass(base=RestrictedClassType(base_type=long, restriction_dict={'range': ['0..4294967295']}, int_size=32), is_leaf=True, yang_name="hold-down-time", rest_name="hold-down-time", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='urn:brocade.com:mgmt:brocade-isis-operational', defining_module='brocade-isis-operational', yang_type='uint32', is_config=False)
    self.__init_delay_time = YANGDynClass(base=RestrictedClassType(base_type=long, restriction_dict={'range': ['0..4294967295']}, int_size=32), is_leaf=True, yang_name="init-delay-time", rest_name="init-delay-time", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='urn:brocade.com:mgmt:brocade-isis-operational', defining_module='brocade-isis-operational', yang_type='uint32', is_config=False)
    self.__max_time = YANGDynClass(base=RestrictedClassType(base_type=long, restriction_dict={'range': ['0..4294967295']}, int_size=32), is_leaf=True, yang_name="max-time", rest_name="max-time", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='urn:brocade.com:mgmt:brocade-isis-operational', defining_module='brocade-isis-operational', yang_type='uint32', is_config=False)

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
      return [u'isis-state', u'router-isis-config', u'pspf6-timer']

  def _rest_path(self):
    if hasattr(self, "_parent"):
      if self._rest_name:
        return self._parent._rest_path()+[self._rest_name]
      else:
        return self._parent._rest_path()
    else:
      return [u'isis-state', u'router-isis-config', u'pspf6-timer']

  def _get_init_delay_time(self):
    """
    Getter method for init_delay_time, mapped from YANG variable /isis_state/router_isis_config/pspf6_timer/init_delay_time (uint32)

    YANG Description: Initial Delay time
    """
    return self.__init_delay_time
      
  def _set_init_delay_time(self, v, load=False):
    """
    Setter method for init_delay_time, mapped from YANG variable /isis_state/router_isis_config/pspf6_timer/init_delay_time (uint32)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_init_delay_time is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_init_delay_time() directly.

    YANG Description: Initial Delay time
    """
    if hasattr(v, "_utype"):
      v = v._utype(v)
    try:
      t = YANGDynClass(v,base=RestrictedClassType(base_type=long, restriction_dict={'range': ['0..4294967295']}, int_size=32), is_leaf=True, yang_name="init-delay-time", rest_name="init-delay-time", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='urn:brocade.com:mgmt:brocade-isis-operational', defining_module='brocade-isis-operational', yang_type='uint32', is_config=False)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """init_delay_time must be of a type compatible with uint32""",
          'defined-type': "uint32",
          'generated-type': """YANGDynClass(base=RestrictedClassType(base_type=long, restriction_dict={'range': ['0..4294967295']}, int_size=32), is_leaf=True, yang_name="init-delay-time", rest_name="init-delay-time", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='urn:brocade.com:mgmt:brocade-isis-operational', defining_module='brocade-isis-operational', yang_type='uint32', is_config=False)""",
        })

    self.__init_delay_time = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_init_delay_time(self):
    self.__init_delay_time = YANGDynClass(base=RestrictedClassType(base_type=long, restriction_dict={'range': ['0..4294967295']}, int_size=32), is_leaf=True, yang_name="init-delay-time", rest_name="init-delay-time", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='urn:brocade.com:mgmt:brocade-isis-operational', defining_module='brocade-isis-operational', yang_type='uint32', is_config=False)


  def _get_hold_down_time(self):
    """
    Getter method for hold_down_time, mapped from YANG variable /isis_state/router_isis_config/pspf6_timer/hold_down_time (uint32)

    YANG Description: Hold down time
    """
    return self.__hold_down_time
      
  def _set_hold_down_time(self, v, load=False):
    """
    Setter method for hold_down_time, mapped from YANG variable /isis_state/router_isis_config/pspf6_timer/hold_down_time (uint32)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_hold_down_time is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_hold_down_time() directly.

    YANG Description: Hold down time
    """
    if hasattr(v, "_utype"):
      v = v._utype(v)
    try:
      t = YANGDynClass(v,base=RestrictedClassType(base_type=long, restriction_dict={'range': ['0..4294967295']}, int_size=32), is_leaf=True, yang_name="hold-down-time", rest_name="hold-down-time", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='urn:brocade.com:mgmt:brocade-isis-operational', defining_module='brocade-isis-operational', yang_type='uint32', is_config=False)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """hold_down_time must be of a type compatible with uint32""",
          'defined-type': "uint32",
          'generated-type': """YANGDynClass(base=RestrictedClassType(base_type=long, restriction_dict={'range': ['0..4294967295']}, int_size=32), is_leaf=True, yang_name="hold-down-time", rest_name="hold-down-time", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='urn:brocade.com:mgmt:brocade-isis-operational', defining_module='brocade-isis-operational', yang_type='uint32', is_config=False)""",
        })

    self.__hold_down_time = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_hold_down_time(self):
    self.__hold_down_time = YANGDynClass(base=RestrictedClassType(base_type=long, restriction_dict={'range': ['0..4294967295']}, int_size=32), is_leaf=True, yang_name="hold-down-time", rest_name="hold-down-time", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='urn:brocade.com:mgmt:brocade-isis-operational', defining_module='brocade-isis-operational', yang_type='uint32', is_config=False)


  def _get_max_time(self):
    """
    Getter method for max_time, mapped from YANG variable /isis_state/router_isis_config/pspf6_timer/max_time (uint32)

    YANG Description: Maximum hold time
    """
    return self.__max_time
      
  def _set_max_time(self, v, load=False):
    """
    Setter method for max_time, mapped from YANG variable /isis_state/router_isis_config/pspf6_timer/max_time (uint32)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_max_time is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_max_time() directly.

    YANG Description: Maximum hold time
    """
    if hasattr(v, "_utype"):
      v = v._utype(v)
    try:
      t = YANGDynClass(v,base=RestrictedClassType(base_type=long, restriction_dict={'range': ['0..4294967295']}, int_size=32), is_leaf=True, yang_name="max-time", rest_name="max-time", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='urn:brocade.com:mgmt:brocade-isis-operational', defining_module='brocade-isis-operational', yang_type='uint32', is_config=False)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """max_time must be of a type compatible with uint32""",
          'defined-type': "uint32",
          'generated-type': """YANGDynClass(base=RestrictedClassType(base_type=long, restriction_dict={'range': ['0..4294967295']}, int_size=32), is_leaf=True, yang_name="max-time", rest_name="max-time", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='urn:brocade.com:mgmt:brocade-isis-operational', defining_module='brocade-isis-operational', yang_type='uint32', is_config=False)""",
        })

    self.__max_time = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_max_time(self):
    self.__max_time = YANGDynClass(base=RestrictedClassType(base_type=long, restriction_dict={'range': ['0..4294967295']}, int_size=32), is_leaf=True, yang_name="max-time", rest_name="max-time", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='urn:brocade.com:mgmt:brocade-isis-operational', defining_module='brocade-isis-operational', yang_type='uint32', is_config=False)

  init_delay_time = __builtin__.property(_get_init_delay_time)
  hold_down_time = __builtin__.property(_get_hold_down_time)
  max_time = __builtin__.property(_get_max_time)


  _pyangbind_elements = {'init_delay_time': init_delay_time, 'hold_down_time': hold_down_time, 'max_time': max_time, }


