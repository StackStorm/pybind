
from operator import attrgetter
import pyangbind.lib.xpathhelper as xpathhelper
from pyangbind.lib.yangtypes import RestrictedPrecisionDecimalType, RestrictedClassType, TypedListType
from pyangbind.lib.yangtypes import YANGBool, YANGListType, YANGDynClass, ReferenceType
from pyangbind.lib.base import PybindBase
from decimal import Decimal
from bitarray import bitarray
import __builtin__
class duplicate_mac_timer(PybindBase):
  """
  This class was auto-generated by the PythonClass plugin for PYANG
  from YANG module brocade-common-def - based on the path /routing-system/evpn-config/evpn/evpn-instance/duplicate-mac-timer. Each member element of
  the container is represented as a class variable - with a specific
  YANG type.

  YANG Description: Duplicate mac timer
  """
  __slots__ = ('_pybind_generated_by', '_path_helper', '_yang_name', '_rest_name', '_extmethods', '__duplicate_mac_timer_value','__max_count',)

  _yang_name = 'duplicate-mac-timer'
  _rest_name = 'duplicate-mac-timer'

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
    self.__duplicate_mac_timer_value = YANGDynClass(base=RestrictedClassType(base_type=RestrictedClassType(base_type=long, restriction_dict={'range': ['0..4294967295']}, int_size=32), restriction_dict={'range': [u'5..300']}), is_leaf=True, yang_name="duplicate-mac-timer-value", rest_name="duplicate-mac-timer-value", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'info': u'Duplicate mac timer value in seconds', u'cli-drop-node-name': None, u'cli-incomplete-no': None, u'cli-incomplete-command': None}}, namespace='urn:brocade.com:mgmt:brocade-bgp', defining_module='brocade-bgp', yang_type='dup-mac-timer', is_config=True)
    self.__max_count = YANGDynClass(base=RestrictedClassType(base_type=RestrictedClassType(base_type=long, restriction_dict={'range': ['0..4294967295']}, int_size=32), restriction_dict={'range': [u'3..10']}), is_leaf=True, yang_name="max-count", rest_name="max-count", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'info': u'Max count.'}}, namespace='urn:brocade.com:mgmt:brocade-bgp', defining_module='brocade-bgp', yang_type='max-count', is_config=True)

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
      return [u'routing-system', u'evpn-config', u'evpn', u'evpn-instance', u'duplicate-mac-timer']

  def _rest_path(self):
    if hasattr(self, "_parent"):
      if self._rest_name:
        return self._parent._rest_path()+[self._rest_name]
      else:
        return self._parent._rest_path()
    else:
      return [u'evpn', u'evpn-instance', u'duplicate-mac-timer']

  def _get_duplicate_mac_timer_value(self):
    """
    Getter method for duplicate_mac_timer_value, mapped from YANG variable /routing_system/evpn_config/evpn/evpn_instance/duplicate_mac_timer/duplicate_mac_timer_value (dup-mac-timer)
    """
    return self.__duplicate_mac_timer_value
      
  def _set_duplicate_mac_timer_value(self, v, load=False):
    """
    Setter method for duplicate_mac_timer_value, mapped from YANG variable /routing_system/evpn_config/evpn/evpn_instance/duplicate_mac_timer/duplicate_mac_timer_value (dup-mac-timer)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_duplicate_mac_timer_value is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_duplicate_mac_timer_value() directly.
    """
    if hasattr(v, "_utype"):
      v = v._utype(v)
    try:
      t = YANGDynClass(v,base=RestrictedClassType(base_type=RestrictedClassType(base_type=long, restriction_dict={'range': ['0..4294967295']}, int_size=32), restriction_dict={'range': [u'5..300']}), is_leaf=True, yang_name="duplicate-mac-timer-value", rest_name="duplicate-mac-timer-value", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'info': u'Duplicate mac timer value in seconds', u'cli-drop-node-name': None, u'cli-incomplete-no': None, u'cli-incomplete-command': None}}, namespace='urn:brocade.com:mgmt:brocade-bgp', defining_module='brocade-bgp', yang_type='dup-mac-timer', is_config=True)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """duplicate_mac_timer_value must be of a type compatible with dup-mac-timer""",
          'defined-type': "brocade-bgp:dup-mac-timer",
          'generated-type': """YANGDynClass(base=RestrictedClassType(base_type=RestrictedClassType(base_type=long, restriction_dict={'range': ['0..4294967295']}, int_size=32), restriction_dict={'range': [u'5..300']}), is_leaf=True, yang_name="duplicate-mac-timer-value", rest_name="duplicate-mac-timer-value", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'info': u'Duplicate mac timer value in seconds', u'cli-drop-node-name': None, u'cli-incomplete-no': None, u'cli-incomplete-command': None}}, namespace='urn:brocade.com:mgmt:brocade-bgp', defining_module='brocade-bgp', yang_type='dup-mac-timer', is_config=True)""",
        })

    self.__duplicate_mac_timer_value = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_duplicate_mac_timer_value(self):
    self.__duplicate_mac_timer_value = YANGDynClass(base=RestrictedClassType(base_type=RestrictedClassType(base_type=long, restriction_dict={'range': ['0..4294967295']}, int_size=32), restriction_dict={'range': [u'5..300']}), is_leaf=True, yang_name="duplicate-mac-timer-value", rest_name="duplicate-mac-timer-value", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'info': u'Duplicate mac timer value in seconds', u'cli-drop-node-name': None, u'cli-incomplete-no': None, u'cli-incomplete-command': None}}, namespace='urn:brocade.com:mgmt:brocade-bgp', defining_module='brocade-bgp', yang_type='dup-mac-timer', is_config=True)


  def _get_max_count(self):
    """
    Getter method for max_count, mapped from YANG variable /routing_system/evpn_config/evpn/evpn_instance/duplicate_mac_timer/max_count (max-count)

    YANG Description: Max count.
    """
    return self.__max_count
      
  def _set_max_count(self, v, load=False):
    """
    Setter method for max_count, mapped from YANG variable /routing_system/evpn_config/evpn/evpn_instance/duplicate_mac_timer/max_count (max-count)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_max_count is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_max_count() directly.

    YANG Description: Max count.
    """
    if hasattr(v, "_utype"):
      v = v._utype(v)
    try:
      t = YANGDynClass(v,base=RestrictedClassType(base_type=RestrictedClassType(base_type=long, restriction_dict={'range': ['0..4294967295']}, int_size=32), restriction_dict={'range': [u'3..10']}), is_leaf=True, yang_name="max-count", rest_name="max-count", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'info': u'Max count.'}}, namespace='urn:brocade.com:mgmt:brocade-bgp', defining_module='brocade-bgp', yang_type='max-count', is_config=True)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """max_count must be of a type compatible with max-count""",
          'defined-type': "brocade-bgp:max-count",
          'generated-type': """YANGDynClass(base=RestrictedClassType(base_type=RestrictedClassType(base_type=long, restriction_dict={'range': ['0..4294967295']}, int_size=32), restriction_dict={'range': [u'3..10']}), is_leaf=True, yang_name="max-count", rest_name="max-count", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'info': u'Max count.'}}, namespace='urn:brocade.com:mgmt:brocade-bgp', defining_module='brocade-bgp', yang_type='max-count', is_config=True)""",
        })

    self.__max_count = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_max_count(self):
    self.__max_count = YANGDynClass(base=RestrictedClassType(base_type=RestrictedClassType(base_type=long, restriction_dict={'range': ['0..4294967295']}, int_size=32), restriction_dict={'range': [u'3..10']}), is_leaf=True, yang_name="max-count", rest_name="max-count", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'info': u'Max count.'}}, namespace='urn:brocade.com:mgmt:brocade-bgp', defining_module='brocade-bgp', yang_type='max-count', is_config=True)

  duplicate_mac_timer_value = __builtin__.property(_get_duplicate_mac_timer_value, _set_duplicate_mac_timer_value)
  max_count = __builtin__.property(_get_max_count, _set_max_count)


  _pyangbind_elements = {'duplicate_mac_timer_value': duplicate_mac_timer_value, 'max_count': max_count, }


