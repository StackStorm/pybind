
from operator import attrgetter
import pyangbind.lib.xpathhelper as xpathhelper
from pyangbind.lib.yangtypes import RestrictedPrecisionDecimalType, RestrictedClassType, TypedListType
from pyangbind.lib.yangtypes import YANGBool, YANGListType, YANGDynClass, ReferenceType
from pyangbind.lib.base import PybindBase
from decimal import Decimal
from bitarray import bitarray
import __builtin__
class group_resouces_list(PybindBase):
  """
  This class was auto-generated by the PythonClass plugin for PYANG
  from YANG module brocade-openflow-operational - based on the path /openflow-state/resources/group-resouces-list. Each member element of
  the container is represented as a class variable - with a specific
  YANG type.

  YANG Description: Group resources
  """
  __slots__ = ('_pybind_generated_by', '_path_helper', '_yang_name', '_rest_name', '_extmethods', '__max_','__used','__free','__group_type',)

  _yang_name = 'group-resouces-list'
  _rest_name = 'group-resouces-list'

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
    self.__used = YANGDynClass(base=RestrictedClassType(base_type=long, restriction_dict={'range': ['0..4294967295']}, int_size=32), is_leaf=True, yang_name="used", rest_name="used", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='urn:brocade.com:mgmt:brocade-openflow-operational', defining_module='brocade-openflow-operational', yang_type='uint32', is_config=False)
    self.__max_ = YANGDynClass(base=RestrictedClassType(base_type=long, restriction_dict={'range': ['0..4294967295']}, int_size=32), is_leaf=True, yang_name="max", rest_name="max", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='urn:brocade.com:mgmt:brocade-openflow-operational', defining_module='brocade-openflow-operational', yang_type='uint32', is_config=False)
    self.__free = YANGDynClass(base=RestrictedClassType(base_type=long, restriction_dict={'range': ['0..4294967295']}, int_size=32), is_leaf=True, yang_name="free", rest_name="free", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='urn:brocade.com:mgmt:brocade-openflow-operational', defining_module='brocade-openflow-operational', yang_type='uint32', is_config=False)
    self.__group_type = YANGDynClass(base=RestrictedClassType(base_type=unicode,                                     restriction_type="dict_key",                                     restriction_arg={u'dcm-group-type-select': {'value': 2}, u'dcm-group-type-invalid': {'value': 0}, u'dcm-group-type-fast-failover': {'value': 4}, u'dcm-group-type-indirect': {'value': 3}, u'dcm-group-type-all': {'value': 1}},), is_leaf=True, yang_name="group-type", rest_name="group-type", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, is_keyval=True, namespace='urn:brocade.com:mgmt:brocade-openflow-operational', defining_module='brocade-openflow-operational', yang_type='group-type', is_config=False)

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
      return [u'openflow-state', u'resources', u'group-resouces-list']

  def _rest_path(self):
    if hasattr(self, "_parent"):
      if self._rest_name:
        return self._parent._rest_path()+[self._rest_name]
      else:
        return self._parent._rest_path()
    else:
      return [u'openflow-state', u'resources', u'group-resouces-list']

  def _get_max_(self):
    """
    Getter method for max_, mapped from YANG variable /openflow_state/resources/group_resouces_list/max (uint32)

    YANG Description: MAX
    """
    return self.__max_
      
  def _set_max_(self, v, load=False):
    """
    Setter method for max_, mapped from YANG variable /openflow_state/resources/group_resouces_list/max (uint32)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_max_ is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_max_() directly.

    YANG Description: MAX
    """
    if hasattr(v, "_utype"):
      v = v._utype(v)
    try:
      t = YANGDynClass(v,base=RestrictedClassType(base_type=long, restriction_dict={'range': ['0..4294967295']}, int_size=32), is_leaf=True, yang_name="max", rest_name="max", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='urn:brocade.com:mgmt:brocade-openflow-operational', defining_module='brocade-openflow-operational', yang_type='uint32', is_config=False)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """max_ must be of a type compatible with uint32""",
          'defined-type': "uint32",
          'generated-type': """YANGDynClass(base=RestrictedClassType(base_type=long, restriction_dict={'range': ['0..4294967295']}, int_size=32), is_leaf=True, yang_name="max", rest_name="max", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='urn:brocade.com:mgmt:brocade-openflow-operational', defining_module='brocade-openflow-operational', yang_type='uint32', is_config=False)""",
        })

    self.__max_ = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_max_(self):
    self.__max_ = YANGDynClass(base=RestrictedClassType(base_type=long, restriction_dict={'range': ['0..4294967295']}, int_size=32), is_leaf=True, yang_name="max", rest_name="max", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='urn:brocade.com:mgmt:brocade-openflow-operational', defining_module='brocade-openflow-operational', yang_type='uint32', is_config=False)


  def _get_used(self):
    """
    Getter method for used, mapped from YANG variable /openflow_state/resources/group_resouces_list/used (uint32)

    YANG Description: Used
    """
    return self.__used
      
  def _set_used(self, v, load=False):
    """
    Setter method for used, mapped from YANG variable /openflow_state/resources/group_resouces_list/used (uint32)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_used is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_used() directly.

    YANG Description: Used
    """
    if hasattr(v, "_utype"):
      v = v._utype(v)
    try:
      t = YANGDynClass(v,base=RestrictedClassType(base_type=long, restriction_dict={'range': ['0..4294967295']}, int_size=32), is_leaf=True, yang_name="used", rest_name="used", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='urn:brocade.com:mgmt:brocade-openflow-operational', defining_module='brocade-openflow-operational', yang_type='uint32', is_config=False)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """used must be of a type compatible with uint32""",
          'defined-type': "uint32",
          'generated-type': """YANGDynClass(base=RestrictedClassType(base_type=long, restriction_dict={'range': ['0..4294967295']}, int_size=32), is_leaf=True, yang_name="used", rest_name="used", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='urn:brocade.com:mgmt:brocade-openflow-operational', defining_module='brocade-openflow-operational', yang_type='uint32', is_config=False)""",
        })

    self.__used = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_used(self):
    self.__used = YANGDynClass(base=RestrictedClassType(base_type=long, restriction_dict={'range': ['0..4294967295']}, int_size=32), is_leaf=True, yang_name="used", rest_name="used", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='urn:brocade.com:mgmt:brocade-openflow-operational', defining_module='brocade-openflow-operational', yang_type='uint32', is_config=False)


  def _get_free(self):
    """
    Getter method for free, mapped from YANG variable /openflow_state/resources/group_resouces_list/free (uint32)

    YANG Description: Free
    """
    return self.__free
      
  def _set_free(self, v, load=False):
    """
    Setter method for free, mapped from YANG variable /openflow_state/resources/group_resouces_list/free (uint32)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_free is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_free() directly.

    YANG Description: Free
    """
    if hasattr(v, "_utype"):
      v = v._utype(v)
    try:
      t = YANGDynClass(v,base=RestrictedClassType(base_type=long, restriction_dict={'range': ['0..4294967295']}, int_size=32), is_leaf=True, yang_name="free", rest_name="free", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='urn:brocade.com:mgmt:brocade-openflow-operational', defining_module='brocade-openflow-operational', yang_type='uint32', is_config=False)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """free must be of a type compatible with uint32""",
          'defined-type': "uint32",
          'generated-type': """YANGDynClass(base=RestrictedClassType(base_type=long, restriction_dict={'range': ['0..4294967295']}, int_size=32), is_leaf=True, yang_name="free", rest_name="free", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='urn:brocade.com:mgmt:brocade-openflow-operational', defining_module='brocade-openflow-operational', yang_type='uint32', is_config=False)""",
        })

    self.__free = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_free(self):
    self.__free = YANGDynClass(base=RestrictedClassType(base_type=long, restriction_dict={'range': ['0..4294967295']}, int_size=32), is_leaf=True, yang_name="free", rest_name="free", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='urn:brocade.com:mgmt:brocade-openflow-operational', defining_module='brocade-openflow-operational', yang_type='uint32', is_config=False)


  def _get_group_type(self):
    """
    Getter method for group_type, mapped from YANG variable /openflow_state/resources/group_resouces_list/group_type (group-type)

    YANG Description: Group Type
    """
    return self.__group_type
      
  def _set_group_type(self, v, load=False):
    """
    Setter method for group_type, mapped from YANG variable /openflow_state/resources/group_resouces_list/group_type (group-type)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_group_type is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_group_type() directly.

    YANG Description: Group Type
    """
    parent = getattr(self, "_parent", None)
    if parent is not None and load is False:
      raise AttributeError("Cannot set keys directly when" +
                             " within an instantiated list")

    if hasattr(v, "_utype"):
      v = v._utype(v)
    try:
      t = YANGDynClass(v,base=RestrictedClassType(base_type=unicode,                                     restriction_type="dict_key",                                     restriction_arg={u'dcm-group-type-select': {'value': 2}, u'dcm-group-type-invalid': {'value': 0}, u'dcm-group-type-fast-failover': {'value': 4}, u'dcm-group-type-indirect': {'value': 3}, u'dcm-group-type-all': {'value': 1}},), is_leaf=True, yang_name="group-type", rest_name="group-type", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, is_keyval=True, namespace='urn:brocade.com:mgmt:brocade-openflow-operational', defining_module='brocade-openflow-operational', yang_type='group-type', is_config=False)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """group_type must be of a type compatible with group-type""",
          'defined-type': "brocade-openflow-operational:group-type",
          'generated-type': """YANGDynClass(base=RestrictedClassType(base_type=unicode,                                     restriction_type="dict_key",                                     restriction_arg={u'dcm-group-type-select': {'value': 2}, u'dcm-group-type-invalid': {'value': 0}, u'dcm-group-type-fast-failover': {'value': 4}, u'dcm-group-type-indirect': {'value': 3}, u'dcm-group-type-all': {'value': 1}},), is_leaf=True, yang_name="group-type", rest_name="group-type", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, is_keyval=True, namespace='urn:brocade.com:mgmt:brocade-openflow-operational', defining_module='brocade-openflow-operational', yang_type='group-type', is_config=False)""",
        })

    self.__group_type = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_group_type(self):
    self.__group_type = YANGDynClass(base=RestrictedClassType(base_type=unicode,                                     restriction_type="dict_key",                                     restriction_arg={u'dcm-group-type-select': {'value': 2}, u'dcm-group-type-invalid': {'value': 0}, u'dcm-group-type-fast-failover': {'value': 4}, u'dcm-group-type-indirect': {'value': 3}, u'dcm-group-type-all': {'value': 1}},), is_leaf=True, yang_name="group-type", rest_name="group-type", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, is_keyval=True, namespace='urn:brocade.com:mgmt:brocade-openflow-operational', defining_module='brocade-openflow-operational', yang_type='group-type', is_config=False)

  max_ = __builtin__.property(_get_max_)
  used = __builtin__.property(_get_used)
  free = __builtin__.property(_get_free)
  group_type = __builtin__.property(_get_group_type)


  _pyangbind_elements = {'max_': max_, 'used': used, 'free': free, 'group_type': group_type, }


