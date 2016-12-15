
from operator import attrgetter
import pyangbind.lib.xpathhelper as xpathhelper
from pyangbind.lib.yangtypes import RestrictedPrecisionDecimalType, RestrictedClassType, TypedListType
from pyangbind.lib.yangtypes import YANGBool, YANGListType, YANGDynClass, ReferenceType
from pyangbind.lib.base import PybindBase
from decimal import Decimal
from bitarray import bitarray
import __builtin__
import spf
class timers(PybindBase):
  """
  This class was auto-generated by the PythonClass plugin for PYANG
  from YANG module brocade-rbridge - based on the path /rbridge-id/ipv6/router/ospf/timers. Each member element of
  the container is represented as a class variable - with a specific
  YANG type.

  YANG Description: Adjust routing timers
  """
  __slots__ = ('_pybind_generated_by', '_path_helper', '_yang_name', '_rest_name', '_extmethods', '__lsa_group_pacing','__spf',)

  _yang_name = 'timers'
  _rest_name = 'timers'

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
    self.__spf = YANGDynClass(base=spf.spf, is_container='container', yang_name="spf", rest_name="spf", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'cli-compact-syntax': None, u'info': u'OSPFv3 SPF timers', u'cli-sequence-commands': None, u'cli-full-no': None}}, namespace='urn:brocade.com:mgmt:brocade-ospfv3', defining_module='brocade-ospfv3', yang_type='container', is_config=True)
    self.__lsa_group_pacing = YANGDynClass(base=RestrictedClassType(base_type=RestrictedClassType(base_type=long, restriction_dict={'range': ['0..4294967295']}, int_size=32), restriction_dict={'range': [u'10..1800']}), default=RestrictedClassType(base_type=long, restriction_dict={'range': ['0..4294967295']}, int_size=32)(240), is_leaf=True, yang_name="lsa-group-pacing", rest_name="lsa-group-pacing", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'cli-full-command': None, u'info': u'OSPFv3 LSA group pacing timer'}}, namespace='urn:brocade.com:mgmt:brocade-ospfv3', defining_module='brocade-ospfv3', yang_type='common-def:time-interval-sec', is_config=True)

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
      return [u'rbridge-id', u'ipv6', u'router', u'ospf', u'timers']

  def _rest_path(self):
    if hasattr(self, "_parent"):
      if self._rest_name:
        return self._parent._rest_path()+[self._rest_name]
      else:
        return self._parent._rest_path()
    else:
      return [u'rbridge-id', u'ipv6', u'router', u'ospf', u'timers']

  def _get_lsa_group_pacing(self):
    """
    Getter method for lsa_group_pacing, mapped from YANG variable /rbridge_id/ipv6/router/ospf/timers/lsa_group_pacing (common-def:time-interval-sec)

    YANG Description: The interval at which the device refreshes an accumulated group of LSAs
    """
    return self.__lsa_group_pacing
      
  def _set_lsa_group_pacing(self, v, load=False):
    """
    Setter method for lsa_group_pacing, mapped from YANG variable /rbridge_id/ipv6/router/ospf/timers/lsa_group_pacing (common-def:time-interval-sec)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_lsa_group_pacing is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_lsa_group_pacing() directly.

    YANG Description: The interval at which the device refreshes an accumulated group of LSAs
    """
    if hasattr(v, "_utype"):
      v = v._utype(v)
    try:
      t = YANGDynClass(v,base=RestrictedClassType(base_type=RestrictedClassType(base_type=long, restriction_dict={'range': ['0..4294967295']}, int_size=32), restriction_dict={'range': [u'10..1800']}), default=RestrictedClassType(base_type=long, restriction_dict={'range': ['0..4294967295']}, int_size=32)(240), is_leaf=True, yang_name="lsa-group-pacing", rest_name="lsa-group-pacing", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'cli-full-command': None, u'info': u'OSPFv3 LSA group pacing timer'}}, namespace='urn:brocade.com:mgmt:brocade-ospfv3', defining_module='brocade-ospfv3', yang_type='common-def:time-interval-sec', is_config=True)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """lsa_group_pacing must be of a type compatible with common-def:time-interval-sec""",
          'defined-type': "common-def:time-interval-sec",
          'generated-type': """YANGDynClass(base=RestrictedClassType(base_type=RestrictedClassType(base_type=long, restriction_dict={'range': ['0..4294967295']}, int_size=32), restriction_dict={'range': [u'10..1800']}), default=RestrictedClassType(base_type=long, restriction_dict={'range': ['0..4294967295']}, int_size=32)(240), is_leaf=True, yang_name="lsa-group-pacing", rest_name="lsa-group-pacing", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'cli-full-command': None, u'info': u'OSPFv3 LSA group pacing timer'}}, namespace='urn:brocade.com:mgmt:brocade-ospfv3', defining_module='brocade-ospfv3', yang_type='common-def:time-interval-sec', is_config=True)""",
        })

    self.__lsa_group_pacing = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_lsa_group_pacing(self):
    self.__lsa_group_pacing = YANGDynClass(base=RestrictedClassType(base_type=RestrictedClassType(base_type=long, restriction_dict={'range': ['0..4294967295']}, int_size=32), restriction_dict={'range': [u'10..1800']}), default=RestrictedClassType(base_type=long, restriction_dict={'range': ['0..4294967295']}, int_size=32)(240), is_leaf=True, yang_name="lsa-group-pacing", rest_name="lsa-group-pacing", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'cli-full-command': None, u'info': u'OSPFv3 LSA group pacing timer'}}, namespace='urn:brocade.com:mgmt:brocade-ospfv3', defining_module='brocade-ospfv3', yang_type='common-def:time-interval-sec', is_config=True)


  def _get_spf(self):
    """
    Getter method for spf, mapped from YANG variable /rbridge_id/ipv6/router/ospf/timers/spf (container)

    YANG Description: The SPF delay and hold time can be set to lower values to cause the device to change to alternate paths more quickly if a route fails. Note that lower values for these parameters require more CPU processing time.
    """
    return self.__spf
      
  def _set_spf(self, v, load=False):
    """
    Setter method for spf, mapped from YANG variable /rbridge_id/ipv6/router/ospf/timers/spf (container)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_spf is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_spf() directly.

    YANG Description: The SPF delay and hold time can be set to lower values to cause the device to change to alternate paths more quickly if a route fails. Note that lower values for these parameters require more CPU processing time.
    """
    if hasattr(v, "_utype"):
      v = v._utype(v)
    try:
      t = YANGDynClass(v,base=spf.spf, is_container='container', yang_name="spf", rest_name="spf", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'cli-compact-syntax': None, u'info': u'OSPFv3 SPF timers', u'cli-sequence-commands': None, u'cli-full-no': None}}, namespace='urn:brocade.com:mgmt:brocade-ospfv3', defining_module='brocade-ospfv3', yang_type='container', is_config=True)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """spf must be of a type compatible with container""",
          'defined-type': "container",
          'generated-type': """YANGDynClass(base=spf.spf, is_container='container', yang_name="spf", rest_name="spf", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'cli-compact-syntax': None, u'info': u'OSPFv3 SPF timers', u'cli-sequence-commands': None, u'cli-full-no': None}}, namespace='urn:brocade.com:mgmt:brocade-ospfv3', defining_module='brocade-ospfv3', yang_type='container', is_config=True)""",
        })

    self.__spf = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_spf(self):
    self.__spf = YANGDynClass(base=spf.spf, is_container='container', yang_name="spf", rest_name="spf", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'cli-compact-syntax': None, u'info': u'OSPFv3 SPF timers', u'cli-sequence-commands': None, u'cli-full-no': None}}, namespace='urn:brocade.com:mgmt:brocade-ospfv3', defining_module='brocade-ospfv3', yang_type='container', is_config=True)

  lsa_group_pacing = __builtin__.property(_get_lsa_group_pacing, _set_lsa_group_pacing)
  spf = __builtin__.property(_get_spf, _set_spf)


  _pyangbind_elements = {'lsa_group_pacing': lsa_group_pacing, 'spf': spf, }


