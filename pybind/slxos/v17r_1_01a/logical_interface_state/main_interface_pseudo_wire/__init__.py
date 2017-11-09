
from operator import attrgetter
import pyangbind.lib.xpathhelper as xpathhelper
from pyangbind.lib.yangtypes import RestrictedPrecisionDecimalType, RestrictedClassType, TypedListType
from pyangbind.lib.yangtypes import YANGBool, YANGListType, YANGDynClass, ReferenceType
from pyangbind.lib.base import PybindBase
from decimal import Decimal
from bitarray import bitarray
import __builtin__
import counters
import logical_interface_pseudo_wire
class main_interface_pseudo_wire(PybindBase):
  """
  This class was auto-generated by the PythonClass plugin for PYANG
  from YANG module brocade-nsm-operational - based on the path /logical-interface-state/main-interface-pseudo-wire. Each member element of
  the container is represented as a class variable - with a specific
  YANG type.

  YANG Description: main interface pseudo wire
  """
  __slots__ = ('_pybind_generated_by', '_path_helper', '_yang_name', '_rest_name', '_extmethods', '__protocol_status','__admin_status','__counters','__interface_index','__logical_interface_pseudo_wire',)

  _yang_name = 'main-interface-pseudo-wire'
  _rest_name = 'main-interface-pseudo-wire'

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
    self.__logical_interface_pseudo_wire = YANGDynClass(base=YANGListType("logical_interface_name",logical_interface_pseudo_wire.logical_interface_pseudo_wire, yang_name="logical-interface-pseudo-wire", rest_name="logical-interface-pseudo-wire", parent=self, is_container='list', user_ordered=False, path_helper=self._path_helper, yang_keys='logical-interface-name', extensions=None), is_container='list', yang_name="logical-interface-pseudo-wire", rest_name="logical-interface-pseudo-wire", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions=None, namespace='urn:brocade.com:mgmt:brocade-nsm-operational', defining_module='brocade-nsm-operational', yang_type='list', is_config=False)
    self.__admin_status = YANGDynClass(base=YANGBool, is_leaf=True, yang_name="admin-status", rest_name="admin-status", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='urn:brocade.com:mgmt:brocade-nsm-operational', defining_module='brocade-nsm-operational', yang_type='boolean', is_config=False)
    self.__interface_index = YANGDynClass(base=RestrictedClassType(base_type=long, restriction_dict={'range': ['0..4294967295']}, int_size=32), is_leaf=True, yang_name="interface-index", rest_name="interface-index", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, is_keyval=True, namespace='urn:brocade.com:mgmt:brocade-nsm-operational', defining_module='brocade-nsm-operational', yang_type='uint32', is_config=False)
    self.__protocol_status = YANGDynClass(base=YANGBool, is_leaf=True, yang_name="protocol-status", rest_name="protocol-status", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='urn:brocade.com:mgmt:brocade-nsm-operational', defining_module='brocade-nsm-operational', yang_type='boolean', is_config=False)
    self.__counters = YANGDynClass(base=YANGListType("implicit_lifs explicit_lifs",counters.counters, yang_name="counters", rest_name="counters", parent=self, is_container='list', user_ordered=False, path_helper=self._path_helper, yang_keys='implicit-lifs explicit-lifs', extensions=None), is_container='list', yang_name="counters", rest_name="counters", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions=None, namespace='urn:brocade.com:mgmt:brocade-nsm-operational', defining_module='brocade-nsm-operational', yang_type='list', is_config=False)

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
      return [u'logical-interface-state', u'main-interface-pseudo-wire']

  def _rest_path(self):
    if hasattr(self, "_parent"):
      if self._rest_name:
        return self._parent._rest_path()+[self._rest_name]
      else:
        return self._parent._rest_path()
    else:
      return [u'logical-interface-state', u'main-interface-pseudo-wire']

  def _get_protocol_status(self):
    """
    Getter method for protocol_status, mapped from YANG variable /logical_interface_state/main_interface_pseudo_wire/protocol_status (boolean)

    YANG Description: Protocol Status
    """
    return self.__protocol_status
      
  def _set_protocol_status(self, v, load=False):
    """
    Setter method for protocol_status, mapped from YANG variable /logical_interface_state/main_interface_pseudo_wire/protocol_status (boolean)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_protocol_status is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_protocol_status() directly.

    YANG Description: Protocol Status
    """
    if hasattr(v, "_utype"):
      v = v._utype(v)
    try:
      t = YANGDynClass(v,base=YANGBool, is_leaf=True, yang_name="protocol-status", rest_name="protocol-status", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='urn:brocade.com:mgmt:brocade-nsm-operational', defining_module='brocade-nsm-operational', yang_type='boolean', is_config=False)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """protocol_status must be of a type compatible with boolean""",
          'defined-type': "boolean",
          'generated-type': """YANGDynClass(base=YANGBool, is_leaf=True, yang_name="protocol-status", rest_name="protocol-status", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='urn:brocade.com:mgmt:brocade-nsm-operational', defining_module='brocade-nsm-operational', yang_type='boolean', is_config=False)""",
        })

    self.__protocol_status = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_protocol_status(self):
    self.__protocol_status = YANGDynClass(base=YANGBool, is_leaf=True, yang_name="protocol-status", rest_name="protocol-status", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='urn:brocade.com:mgmt:brocade-nsm-operational', defining_module='brocade-nsm-operational', yang_type='boolean', is_config=False)


  def _get_admin_status(self):
    """
    Getter method for admin_status, mapped from YANG variable /logical_interface_state/main_interface_pseudo_wire/admin_status (boolean)

    YANG Description: Admin Status
    """
    return self.__admin_status
      
  def _set_admin_status(self, v, load=False):
    """
    Setter method for admin_status, mapped from YANG variable /logical_interface_state/main_interface_pseudo_wire/admin_status (boolean)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_admin_status is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_admin_status() directly.

    YANG Description: Admin Status
    """
    if hasattr(v, "_utype"):
      v = v._utype(v)
    try:
      t = YANGDynClass(v,base=YANGBool, is_leaf=True, yang_name="admin-status", rest_name="admin-status", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='urn:brocade.com:mgmt:brocade-nsm-operational', defining_module='brocade-nsm-operational', yang_type='boolean', is_config=False)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """admin_status must be of a type compatible with boolean""",
          'defined-type': "boolean",
          'generated-type': """YANGDynClass(base=YANGBool, is_leaf=True, yang_name="admin-status", rest_name="admin-status", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='urn:brocade.com:mgmt:brocade-nsm-operational', defining_module='brocade-nsm-operational', yang_type='boolean', is_config=False)""",
        })

    self.__admin_status = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_admin_status(self):
    self.__admin_status = YANGDynClass(base=YANGBool, is_leaf=True, yang_name="admin-status", rest_name="admin-status", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='urn:brocade.com:mgmt:brocade-nsm-operational', defining_module='brocade-nsm-operational', yang_type='boolean', is_config=False)


  def _get_counters(self):
    """
    Getter method for counters, mapped from YANG variable /logical_interface_state/main_interface_pseudo_wire/counters (list)

    YANG Description: Lif counters
    """
    return self.__counters
      
  def _set_counters(self, v, load=False):
    """
    Setter method for counters, mapped from YANG variable /logical_interface_state/main_interface_pseudo_wire/counters (list)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_counters is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_counters() directly.

    YANG Description: Lif counters
    """
    if hasattr(v, "_utype"):
      v = v._utype(v)
    try:
      t = YANGDynClass(v,base=YANGListType("implicit_lifs explicit_lifs",counters.counters, yang_name="counters", rest_name="counters", parent=self, is_container='list', user_ordered=False, path_helper=self._path_helper, yang_keys='implicit-lifs explicit-lifs', extensions=None), is_container='list', yang_name="counters", rest_name="counters", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions=None, namespace='urn:brocade.com:mgmt:brocade-nsm-operational', defining_module='brocade-nsm-operational', yang_type='list', is_config=False)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """counters must be of a type compatible with list""",
          'defined-type': "list",
          'generated-type': """YANGDynClass(base=YANGListType("implicit_lifs explicit_lifs",counters.counters, yang_name="counters", rest_name="counters", parent=self, is_container='list', user_ordered=False, path_helper=self._path_helper, yang_keys='implicit-lifs explicit-lifs', extensions=None), is_container='list', yang_name="counters", rest_name="counters", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions=None, namespace='urn:brocade.com:mgmt:brocade-nsm-operational', defining_module='brocade-nsm-operational', yang_type='list', is_config=False)""",
        })

    self.__counters = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_counters(self):
    self.__counters = YANGDynClass(base=YANGListType("implicit_lifs explicit_lifs",counters.counters, yang_name="counters", rest_name="counters", parent=self, is_container='list', user_ordered=False, path_helper=self._path_helper, yang_keys='implicit-lifs explicit-lifs', extensions=None), is_container='list', yang_name="counters", rest_name="counters", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions=None, namespace='urn:brocade.com:mgmt:brocade-nsm-operational', defining_module='brocade-nsm-operational', yang_type='list', is_config=False)


  def _get_interface_index(self):
    """
    Getter method for interface_index, mapped from YANG variable /logical_interface_state/main_interface_pseudo_wire/interface_index (uint32)

    YANG Description: interface index
    """
    return self.__interface_index
      
  def _set_interface_index(self, v, load=False):
    """
    Setter method for interface_index, mapped from YANG variable /logical_interface_state/main_interface_pseudo_wire/interface_index (uint32)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_interface_index is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_interface_index() directly.

    YANG Description: interface index
    """
    parent = getattr(self, "_parent", None)
    if parent is not None and load is False:
      raise AttributeError("Cannot set keys directly when" +
                             " within an instantiated list")

    if hasattr(v, "_utype"):
      v = v._utype(v)
    try:
      t = YANGDynClass(v,base=RestrictedClassType(base_type=long, restriction_dict={'range': ['0..4294967295']}, int_size=32), is_leaf=True, yang_name="interface-index", rest_name="interface-index", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, is_keyval=True, namespace='urn:brocade.com:mgmt:brocade-nsm-operational', defining_module='brocade-nsm-operational', yang_type='uint32', is_config=False)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """interface_index must be of a type compatible with uint32""",
          'defined-type': "uint32",
          'generated-type': """YANGDynClass(base=RestrictedClassType(base_type=long, restriction_dict={'range': ['0..4294967295']}, int_size=32), is_leaf=True, yang_name="interface-index", rest_name="interface-index", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, is_keyval=True, namespace='urn:brocade.com:mgmt:brocade-nsm-operational', defining_module='brocade-nsm-operational', yang_type='uint32', is_config=False)""",
        })

    self.__interface_index = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_interface_index(self):
    self.__interface_index = YANGDynClass(base=RestrictedClassType(base_type=long, restriction_dict={'range': ['0..4294967295']}, int_size=32), is_leaf=True, yang_name="interface-index", rest_name="interface-index", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, is_keyval=True, namespace='urn:brocade.com:mgmt:brocade-nsm-operational', defining_module='brocade-nsm-operational', yang_type='uint32', is_config=False)


  def _get_logical_interface_pseudo_wire(self):
    """
    Getter method for logical_interface_pseudo_wire, mapped from YANG variable /logical_interface_state/main_interface_pseudo_wire/logical_interface_pseudo_wire (list)

    YANG Description: logical interface pseudo wire
    """
    return self.__logical_interface_pseudo_wire
      
  def _set_logical_interface_pseudo_wire(self, v, load=False):
    """
    Setter method for logical_interface_pseudo_wire, mapped from YANG variable /logical_interface_state/main_interface_pseudo_wire/logical_interface_pseudo_wire (list)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_logical_interface_pseudo_wire is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_logical_interface_pseudo_wire() directly.

    YANG Description: logical interface pseudo wire
    """
    if hasattr(v, "_utype"):
      v = v._utype(v)
    try:
      t = YANGDynClass(v,base=YANGListType("logical_interface_name",logical_interface_pseudo_wire.logical_interface_pseudo_wire, yang_name="logical-interface-pseudo-wire", rest_name="logical-interface-pseudo-wire", parent=self, is_container='list', user_ordered=False, path_helper=self._path_helper, yang_keys='logical-interface-name', extensions=None), is_container='list', yang_name="logical-interface-pseudo-wire", rest_name="logical-interface-pseudo-wire", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions=None, namespace='urn:brocade.com:mgmt:brocade-nsm-operational', defining_module='brocade-nsm-operational', yang_type='list', is_config=False)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """logical_interface_pseudo_wire must be of a type compatible with list""",
          'defined-type': "list",
          'generated-type': """YANGDynClass(base=YANGListType("logical_interface_name",logical_interface_pseudo_wire.logical_interface_pseudo_wire, yang_name="logical-interface-pseudo-wire", rest_name="logical-interface-pseudo-wire", parent=self, is_container='list', user_ordered=False, path_helper=self._path_helper, yang_keys='logical-interface-name', extensions=None), is_container='list', yang_name="logical-interface-pseudo-wire", rest_name="logical-interface-pseudo-wire", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions=None, namespace='urn:brocade.com:mgmt:brocade-nsm-operational', defining_module='brocade-nsm-operational', yang_type='list', is_config=False)""",
        })

    self.__logical_interface_pseudo_wire = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_logical_interface_pseudo_wire(self):
    self.__logical_interface_pseudo_wire = YANGDynClass(base=YANGListType("logical_interface_name",logical_interface_pseudo_wire.logical_interface_pseudo_wire, yang_name="logical-interface-pseudo-wire", rest_name="logical-interface-pseudo-wire", parent=self, is_container='list', user_ordered=False, path_helper=self._path_helper, yang_keys='logical-interface-name', extensions=None), is_container='list', yang_name="logical-interface-pseudo-wire", rest_name="logical-interface-pseudo-wire", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions=None, namespace='urn:brocade.com:mgmt:brocade-nsm-operational', defining_module='brocade-nsm-operational', yang_type='list', is_config=False)

  protocol_status = __builtin__.property(_get_protocol_status)
  admin_status = __builtin__.property(_get_admin_status)
  counters = __builtin__.property(_get_counters)
  interface_index = __builtin__.property(_get_interface_index)
  logical_interface_pseudo_wire = __builtin__.property(_get_logical_interface_pseudo_wire)


  _pyangbind_elements = {'protocol_status': protocol_status, 'admin_status': admin_status, 'counters': counters, 'interface_index': interface_index, 'logical_interface_pseudo_wire': logical_interface_pseudo_wire, }

