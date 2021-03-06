
from operator import attrgetter
import pyangbind.lib.xpathhelper as xpathhelper
from pyangbind.lib.yangtypes import RestrictedPrecisionDecimalType, RestrictedClassType, TypedListType
from pyangbind.lib.yangtypes import YANGBool, YANGListType, YANGDynClass, ReferenceType
from pyangbind.lib.base import PybindBase
from decimal import Decimal
from bitarray import bitarray
import __builtin__
import slot_chip_resource_list
class slot_match_profile_list(PybindBase):
  """
  This class was auto-generated by the PythonClass plugin for PYANG
  from YANG module brocade-openflow-operational - based on the path /openflow-state/resources/slot-resouces-list/slot-match-profile-list. Each member element of
  the container is represented as a class variable - with a specific
  YANG type.

  YANG Description: slot match profile details
  """
  __slots__ = ('_pybind_generated_by', '_path_helper', '_yang_name', '_rest_name', '_extmethods', '__slot_match_profile_idx','__max_flows','__used_flows','__free_flows','__slot_chip_resource_list',)

  _yang_name = 'slot-match-profile-list'
  _rest_name = 'slot-match-profile-list'

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
    self.__used_flows = YANGDynClass(base=RestrictedClassType(base_type=long, restriction_dict={'range': ['0..4294967295']}, int_size=32), is_leaf=True, yang_name="used-flows", rest_name="used-flows", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='urn:brocade.com:mgmt:brocade-openflow-operational', defining_module='brocade-openflow-operational', yang_type='uint32', is_config=False)
    self.__slot_chip_resource_list = YANGDynClass(base=YANGListType("slot_chip_idx",slot_chip_resource_list.slot_chip_resource_list, yang_name="slot-chip-resource-list", rest_name="slot-chip-resource-list", parent=self, is_container='list', user_ordered=False, path_helper=self._path_helper, yang_keys='slot-chip-idx', extensions={u'tailf-common': {u'callpoint': u'openflow-slot-chip-resource-info', u'cli-suppress-show-path': None}}), is_container='list', yang_name="slot-chip-resource-list", rest_name="slot-chip-resource-list", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'callpoint': u'openflow-slot-chip-resource-info', u'cli-suppress-show-path': None}}, namespace='urn:brocade.com:mgmt:brocade-openflow-operational', defining_module='brocade-openflow-operational', yang_type='list', is_config=False)
    self.__max_flows = YANGDynClass(base=RestrictedClassType(base_type=long, restriction_dict={'range': ['0..4294967295']}, int_size=32), is_leaf=True, yang_name="max-flows", rest_name="max-flows", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='urn:brocade.com:mgmt:brocade-openflow-operational', defining_module='brocade-openflow-operational', yang_type='uint32', is_config=False)
    self.__slot_match_profile_idx = YANGDynClass(base=RestrictedClassType(base_type=long, restriction_dict={'range': ['0..4294967295']}, int_size=32), is_leaf=True, yang_name="slot-match-profile-idx", rest_name="slot-match-profile-idx", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, is_keyval=True, namespace='urn:brocade.com:mgmt:brocade-openflow-operational', defining_module='brocade-openflow-operational', yang_type='uint32', is_config=False)
    self.__free_flows = YANGDynClass(base=RestrictedClassType(base_type=long, restriction_dict={'range': ['0..4294967295']}, int_size=32), is_leaf=True, yang_name="free-flows", rest_name="free-flows", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='urn:brocade.com:mgmt:brocade-openflow-operational', defining_module='brocade-openflow-operational', yang_type='uint32', is_config=False)

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
      return [u'openflow-state', u'resources', u'slot-resouces-list', u'slot-match-profile-list']

  def _rest_path(self):
    if hasattr(self, "_parent"):
      if self._rest_name:
        return self._parent._rest_path()+[self._rest_name]
      else:
        return self._parent._rest_path()
    else:
      return [u'openflow-state', u'resources', u'slot-resouces-list', u'slot-match-profile-list']

  def _get_slot_match_profile_idx(self):
    """
    Getter method for slot_match_profile_idx, mapped from YANG variable /openflow_state/resources/slot_resouces_list/slot_match_profile_list/slot_match_profile_idx (uint32)

    YANG Description: Index
    """
    return self.__slot_match_profile_idx
      
  def _set_slot_match_profile_idx(self, v, load=False):
    """
    Setter method for slot_match_profile_idx, mapped from YANG variable /openflow_state/resources/slot_resouces_list/slot_match_profile_list/slot_match_profile_idx (uint32)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_slot_match_profile_idx is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_slot_match_profile_idx() directly.

    YANG Description: Index
    """
    parent = getattr(self, "_parent", None)
    if parent is not None and load is False:
      raise AttributeError("Cannot set keys directly when" +
                             " within an instantiated list")

    if hasattr(v, "_utype"):
      v = v._utype(v)
    try:
      t = YANGDynClass(v,base=RestrictedClassType(base_type=long, restriction_dict={'range': ['0..4294967295']}, int_size=32), is_leaf=True, yang_name="slot-match-profile-idx", rest_name="slot-match-profile-idx", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, is_keyval=True, namespace='urn:brocade.com:mgmt:brocade-openflow-operational', defining_module='brocade-openflow-operational', yang_type='uint32', is_config=False)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """slot_match_profile_idx must be of a type compatible with uint32""",
          'defined-type': "uint32",
          'generated-type': """YANGDynClass(base=RestrictedClassType(base_type=long, restriction_dict={'range': ['0..4294967295']}, int_size=32), is_leaf=True, yang_name="slot-match-profile-idx", rest_name="slot-match-profile-idx", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, is_keyval=True, namespace='urn:brocade.com:mgmt:brocade-openflow-operational', defining_module='brocade-openflow-operational', yang_type='uint32', is_config=False)""",
        })

    self.__slot_match_profile_idx = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_slot_match_profile_idx(self):
    self.__slot_match_profile_idx = YANGDynClass(base=RestrictedClassType(base_type=long, restriction_dict={'range': ['0..4294967295']}, int_size=32), is_leaf=True, yang_name="slot-match-profile-idx", rest_name="slot-match-profile-idx", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, is_keyval=True, namespace='urn:brocade.com:mgmt:brocade-openflow-operational', defining_module='brocade-openflow-operational', yang_type='uint32', is_config=False)


  def _get_max_flows(self):
    """
    Getter method for max_flows, mapped from YANG variable /openflow_state/resources/slot_resouces_list/slot_match_profile_list/max_flows (uint32)

    YANG Description: MAX
    """
    return self.__max_flows
      
  def _set_max_flows(self, v, load=False):
    """
    Setter method for max_flows, mapped from YANG variable /openflow_state/resources/slot_resouces_list/slot_match_profile_list/max_flows (uint32)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_max_flows is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_max_flows() directly.

    YANG Description: MAX
    """
    if hasattr(v, "_utype"):
      v = v._utype(v)
    try:
      t = YANGDynClass(v,base=RestrictedClassType(base_type=long, restriction_dict={'range': ['0..4294967295']}, int_size=32), is_leaf=True, yang_name="max-flows", rest_name="max-flows", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='urn:brocade.com:mgmt:brocade-openflow-operational', defining_module='brocade-openflow-operational', yang_type='uint32', is_config=False)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """max_flows must be of a type compatible with uint32""",
          'defined-type': "uint32",
          'generated-type': """YANGDynClass(base=RestrictedClassType(base_type=long, restriction_dict={'range': ['0..4294967295']}, int_size=32), is_leaf=True, yang_name="max-flows", rest_name="max-flows", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='urn:brocade.com:mgmt:brocade-openflow-operational', defining_module='brocade-openflow-operational', yang_type='uint32', is_config=False)""",
        })

    self.__max_flows = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_max_flows(self):
    self.__max_flows = YANGDynClass(base=RestrictedClassType(base_type=long, restriction_dict={'range': ['0..4294967295']}, int_size=32), is_leaf=True, yang_name="max-flows", rest_name="max-flows", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='urn:brocade.com:mgmt:brocade-openflow-operational', defining_module='brocade-openflow-operational', yang_type='uint32', is_config=False)


  def _get_used_flows(self):
    """
    Getter method for used_flows, mapped from YANG variable /openflow_state/resources/slot_resouces_list/slot_match_profile_list/used_flows (uint32)

    YANG Description: Used
    """
    return self.__used_flows
      
  def _set_used_flows(self, v, load=False):
    """
    Setter method for used_flows, mapped from YANG variable /openflow_state/resources/slot_resouces_list/slot_match_profile_list/used_flows (uint32)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_used_flows is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_used_flows() directly.

    YANG Description: Used
    """
    if hasattr(v, "_utype"):
      v = v._utype(v)
    try:
      t = YANGDynClass(v,base=RestrictedClassType(base_type=long, restriction_dict={'range': ['0..4294967295']}, int_size=32), is_leaf=True, yang_name="used-flows", rest_name="used-flows", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='urn:brocade.com:mgmt:brocade-openflow-operational', defining_module='brocade-openflow-operational', yang_type='uint32', is_config=False)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """used_flows must be of a type compatible with uint32""",
          'defined-type': "uint32",
          'generated-type': """YANGDynClass(base=RestrictedClassType(base_type=long, restriction_dict={'range': ['0..4294967295']}, int_size=32), is_leaf=True, yang_name="used-flows", rest_name="used-flows", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='urn:brocade.com:mgmt:brocade-openflow-operational', defining_module='brocade-openflow-operational', yang_type='uint32', is_config=False)""",
        })

    self.__used_flows = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_used_flows(self):
    self.__used_flows = YANGDynClass(base=RestrictedClassType(base_type=long, restriction_dict={'range': ['0..4294967295']}, int_size=32), is_leaf=True, yang_name="used-flows", rest_name="used-flows", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='urn:brocade.com:mgmt:brocade-openflow-operational', defining_module='brocade-openflow-operational', yang_type='uint32', is_config=False)


  def _get_free_flows(self):
    """
    Getter method for free_flows, mapped from YANG variable /openflow_state/resources/slot_resouces_list/slot_match_profile_list/free_flows (uint32)

    YANG Description: Free
    """
    return self.__free_flows
      
  def _set_free_flows(self, v, load=False):
    """
    Setter method for free_flows, mapped from YANG variable /openflow_state/resources/slot_resouces_list/slot_match_profile_list/free_flows (uint32)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_free_flows is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_free_flows() directly.

    YANG Description: Free
    """
    if hasattr(v, "_utype"):
      v = v._utype(v)
    try:
      t = YANGDynClass(v,base=RestrictedClassType(base_type=long, restriction_dict={'range': ['0..4294967295']}, int_size=32), is_leaf=True, yang_name="free-flows", rest_name="free-flows", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='urn:brocade.com:mgmt:brocade-openflow-operational', defining_module='brocade-openflow-operational', yang_type='uint32', is_config=False)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """free_flows must be of a type compatible with uint32""",
          'defined-type': "uint32",
          'generated-type': """YANGDynClass(base=RestrictedClassType(base_type=long, restriction_dict={'range': ['0..4294967295']}, int_size=32), is_leaf=True, yang_name="free-flows", rest_name="free-flows", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='urn:brocade.com:mgmt:brocade-openflow-operational', defining_module='brocade-openflow-operational', yang_type='uint32', is_config=False)""",
        })

    self.__free_flows = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_free_flows(self):
    self.__free_flows = YANGDynClass(base=RestrictedClassType(base_type=long, restriction_dict={'range': ['0..4294967295']}, int_size=32), is_leaf=True, yang_name="free-flows", rest_name="free-flows", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='urn:brocade.com:mgmt:brocade-openflow-operational', defining_module='brocade-openflow-operational', yang_type='uint32', is_config=False)


  def _get_slot_chip_resource_list(self):
    """
    Getter method for slot_chip_resource_list, mapped from YANG variable /openflow_state/resources/slot_resouces_list/slot_match_profile_list/slot_chip_resource_list (list)

    YANG Description: slot chip resource details
    """
    return self.__slot_chip_resource_list
      
  def _set_slot_chip_resource_list(self, v, load=False):
    """
    Setter method for slot_chip_resource_list, mapped from YANG variable /openflow_state/resources/slot_resouces_list/slot_match_profile_list/slot_chip_resource_list (list)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_slot_chip_resource_list is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_slot_chip_resource_list() directly.

    YANG Description: slot chip resource details
    """
    if hasattr(v, "_utype"):
      v = v._utype(v)
    try:
      t = YANGDynClass(v,base=YANGListType("slot_chip_idx",slot_chip_resource_list.slot_chip_resource_list, yang_name="slot-chip-resource-list", rest_name="slot-chip-resource-list", parent=self, is_container='list', user_ordered=False, path_helper=self._path_helper, yang_keys='slot-chip-idx', extensions={u'tailf-common': {u'callpoint': u'openflow-slot-chip-resource-info', u'cli-suppress-show-path': None}}), is_container='list', yang_name="slot-chip-resource-list", rest_name="slot-chip-resource-list", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'callpoint': u'openflow-slot-chip-resource-info', u'cli-suppress-show-path': None}}, namespace='urn:brocade.com:mgmt:brocade-openflow-operational', defining_module='brocade-openflow-operational', yang_type='list', is_config=False)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """slot_chip_resource_list must be of a type compatible with list""",
          'defined-type': "list",
          'generated-type': """YANGDynClass(base=YANGListType("slot_chip_idx",slot_chip_resource_list.slot_chip_resource_list, yang_name="slot-chip-resource-list", rest_name="slot-chip-resource-list", parent=self, is_container='list', user_ordered=False, path_helper=self._path_helper, yang_keys='slot-chip-idx', extensions={u'tailf-common': {u'callpoint': u'openflow-slot-chip-resource-info', u'cli-suppress-show-path': None}}), is_container='list', yang_name="slot-chip-resource-list", rest_name="slot-chip-resource-list", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'callpoint': u'openflow-slot-chip-resource-info', u'cli-suppress-show-path': None}}, namespace='urn:brocade.com:mgmt:brocade-openflow-operational', defining_module='brocade-openflow-operational', yang_type='list', is_config=False)""",
        })

    self.__slot_chip_resource_list = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_slot_chip_resource_list(self):
    self.__slot_chip_resource_list = YANGDynClass(base=YANGListType("slot_chip_idx",slot_chip_resource_list.slot_chip_resource_list, yang_name="slot-chip-resource-list", rest_name="slot-chip-resource-list", parent=self, is_container='list', user_ordered=False, path_helper=self._path_helper, yang_keys='slot-chip-idx', extensions={u'tailf-common': {u'callpoint': u'openflow-slot-chip-resource-info', u'cli-suppress-show-path': None}}), is_container='list', yang_name="slot-chip-resource-list", rest_name="slot-chip-resource-list", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'callpoint': u'openflow-slot-chip-resource-info', u'cli-suppress-show-path': None}}, namespace='urn:brocade.com:mgmt:brocade-openflow-operational', defining_module='brocade-openflow-operational', yang_type='list', is_config=False)

  slot_match_profile_idx = __builtin__.property(_get_slot_match_profile_idx)
  max_flows = __builtin__.property(_get_max_flows)
  used_flows = __builtin__.property(_get_used_flows)
  free_flows = __builtin__.property(_get_free_flows)
  slot_chip_resource_list = __builtin__.property(_get_slot_chip_resource_list)


  _pyangbind_elements = {'slot_match_profile_idx': slot_match_profile_idx, 'max_flows': max_flows, 'used_flows': used_flows, 'free_flows': free_flows, 'slot_chip_resource_list': slot_chip_resource_list, }


