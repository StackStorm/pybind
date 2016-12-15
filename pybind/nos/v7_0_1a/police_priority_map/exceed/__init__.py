
from operator import attrgetter
import pyangbind.lib.xpathhelper as xpathhelper
from pyangbind.lib.yangtypes import RestrictedPrecisionDecimalType, RestrictedClassType, TypedListType
from pyangbind.lib.yangtypes import YANGBool, YANGListType, YANGDynClass, ReferenceType
from pyangbind.lib.base import PybindBase
from decimal import Decimal
from bitarray import bitarray
import __builtin__
class exceed(PybindBase):
  """
  This class was auto-generated by the PythonClass plugin for PYANG
  from YANG module brocade-policer - based on the path /police-priority-map/exceed. Each member element of
  the container is represented as a class variable - with a specific
  YANG type.
  """
  __slots__ = ('_pybind_generated_by', '_path_helper', '_yang_name', '_rest_name', '_extmethods', '__map_pri0_exceed','__map_pri1_exceed','__map_pri2_exceed','__map_pri3_exceed','__map_pri4_exceed','__map_pri5_exceed','__map_pri6_exceed','__map_pri7_exceed',)

  _yang_name = 'exceed'
  _rest_name = 'exceed'

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
    self.__map_pri3_exceed = YANGDynClass(base=RestrictedClassType(base_type=RestrictedClassType(base_type=long, restriction_dict={'range': ['0..4294967295']}, int_size=32), restriction_dict={'range': [u'0..7']}), is_leaf=True, yang_name="map-pri3-exceed", rest_name="", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'info': u'Mapping Priority Number 3', u'cli-drop-node-name': None, u'cli-incomplete-command': None, u'cli-suppress-no': None}}, namespace='urn:brocade.com:mgmt:brocade-policer', defining_module='brocade-policer', yang_type='priority-value', is_config=True)
    self.__map_pri4_exceed = YANGDynClass(base=RestrictedClassType(base_type=RestrictedClassType(base_type=long, restriction_dict={'range': ['0..4294967295']}, int_size=32), restriction_dict={'range': [u'0..7']}), is_leaf=True, yang_name="map-pri4-exceed", rest_name="", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'info': u'Mapping Priority Number 4', u'cli-drop-node-name': None, u'cli-incomplete-command': None, u'cli-suppress-no': None}}, namespace='urn:brocade.com:mgmt:brocade-policer', defining_module='brocade-policer', yang_type='priority-value', is_config=True)
    self.__map_pri0_exceed = YANGDynClass(base=RestrictedClassType(base_type=RestrictedClassType(base_type=long, restriction_dict={'range': ['0..4294967295']}, int_size=32), restriction_dict={'range': [u'0..7']}), is_leaf=True, yang_name="map-pri0-exceed", rest_name="", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'info': u'Mapping Priority Number 0', u'cli-drop-node-name': None, u'cli-incomplete-command': None, u'cli-suppress-no': None}}, namespace='urn:brocade.com:mgmt:brocade-policer', defining_module='brocade-policer', yang_type='priority-value', is_config=True)
    self.__map_pri5_exceed = YANGDynClass(base=RestrictedClassType(base_type=RestrictedClassType(base_type=long, restriction_dict={'range': ['0..4294967295']}, int_size=32), restriction_dict={'range': [u'0..7']}), is_leaf=True, yang_name="map-pri5-exceed", rest_name="", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'info': u'Mapping Priority Number 5', u'cli-drop-node-name': None, u'cli-incomplete-command': None, u'cli-suppress-no': None}}, namespace='urn:brocade.com:mgmt:brocade-policer', defining_module='brocade-policer', yang_type='priority-value', is_config=True)
    self.__map_pri6_exceed = YANGDynClass(base=RestrictedClassType(base_type=RestrictedClassType(base_type=long, restriction_dict={'range': ['0..4294967295']}, int_size=32), restriction_dict={'range': [u'0..7']}), is_leaf=True, yang_name="map-pri6-exceed", rest_name="", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'info': u'Mapping Priority Number 6', u'cli-drop-node-name': None, u'cli-incomplete-command': None, u'cli-suppress-no': None}}, namespace='urn:brocade.com:mgmt:brocade-policer', defining_module='brocade-policer', yang_type='priority-value', is_config=True)
    self.__map_pri2_exceed = YANGDynClass(base=RestrictedClassType(base_type=RestrictedClassType(base_type=long, restriction_dict={'range': ['0..4294967295']}, int_size=32), restriction_dict={'range': [u'0..7']}), is_leaf=True, yang_name="map-pri2-exceed", rest_name="", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'info': u'Mapping Priority Number 2', u'cli-drop-node-name': None, u'cli-incomplete-command': None, u'cli-suppress-no': None}}, namespace='urn:brocade.com:mgmt:brocade-policer', defining_module='brocade-policer', yang_type='priority-value', is_config=True)
    self.__map_pri7_exceed = YANGDynClass(base=RestrictedClassType(base_type=RestrictedClassType(base_type=long, restriction_dict={'range': ['0..4294967295']}, int_size=32), restriction_dict={'range': [u'0..7']}), is_leaf=True, yang_name="map-pri7-exceed", rest_name="", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'info': u'Mapping Priority Number 7', u'cli-drop-node-name': None, u'cli-suppress-no': None}}, namespace='urn:brocade.com:mgmt:brocade-policer', defining_module='brocade-policer', yang_type='priority-value', is_config=True)
    self.__map_pri1_exceed = YANGDynClass(base=RestrictedClassType(base_type=RestrictedClassType(base_type=long, restriction_dict={'range': ['0..4294967295']}, int_size=32), restriction_dict={'range': [u'0..7']}), is_leaf=True, yang_name="map-pri1-exceed", rest_name="", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'info': u'Mapping Priority Number 1', u'cli-drop-node-name': None, u'cli-incomplete-command': None, u'cli-suppress-no': None}}, namespace='urn:brocade.com:mgmt:brocade-policer', defining_module='brocade-policer', yang_type='priority-value', is_config=True)

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
      return [u'police-priority-map', u'exceed']

  def _rest_path(self):
    if hasattr(self, "_parent"):
      if self._rest_name:
        return self._parent._rest_path()+[self._rest_name]
      else:
        return self._parent._rest_path()
    else:
      return [u'police-priority-map', u'exceed']

  def _get_map_pri0_exceed(self):
    """
    Getter method for map_pri0_exceed, mapped from YANG variable /police_priority_map/exceed/map_pri0_exceed (priority-value)
    """
    return self.__map_pri0_exceed
      
  def _set_map_pri0_exceed(self, v, load=False):
    """
    Setter method for map_pri0_exceed, mapped from YANG variable /police_priority_map/exceed/map_pri0_exceed (priority-value)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_map_pri0_exceed is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_map_pri0_exceed() directly.
    """
    if hasattr(v, "_utype"):
      v = v._utype(v)
    try:
      t = YANGDynClass(v,base=RestrictedClassType(base_type=RestrictedClassType(base_type=long, restriction_dict={'range': ['0..4294967295']}, int_size=32), restriction_dict={'range': [u'0..7']}), is_leaf=True, yang_name="map-pri0-exceed", rest_name="", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'info': u'Mapping Priority Number 0', u'cli-drop-node-name': None, u'cli-incomplete-command': None, u'cli-suppress-no': None}}, namespace='urn:brocade.com:mgmt:brocade-policer', defining_module='brocade-policer', yang_type='priority-value', is_config=True)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """map_pri0_exceed must be of a type compatible with priority-value""",
          'defined-type': "brocade-policer:priority-value",
          'generated-type': """YANGDynClass(base=RestrictedClassType(base_type=RestrictedClassType(base_type=long, restriction_dict={'range': ['0..4294967295']}, int_size=32), restriction_dict={'range': [u'0..7']}), is_leaf=True, yang_name="map-pri0-exceed", rest_name="", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'info': u'Mapping Priority Number 0', u'cli-drop-node-name': None, u'cli-incomplete-command': None, u'cli-suppress-no': None}}, namespace='urn:brocade.com:mgmt:brocade-policer', defining_module='brocade-policer', yang_type='priority-value', is_config=True)""",
        })

    self.__map_pri0_exceed = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_map_pri0_exceed(self):
    self.__map_pri0_exceed = YANGDynClass(base=RestrictedClassType(base_type=RestrictedClassType(base_type=long, restriction_dict={'range': ['0..4294967295']}, int_size=32), restriction_dict={'range': [u'0..7']}), is_leaf=True, yang_name="map-pri0-exceed", rest_name="", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'info': u'Mapping Priority Number 0', u'cli-drop-node-name': None, u'cli-incomplete-command': None, u'cli-suppress-no': None}}, namespace='urn:brocade.com:mgmt:brocade-policer', defining_module='brocade-policer', yang_type='priority-value', is_config=True)


  def _get_map_pri1_exceed(self):
    """
    Getter method for map_pri1_exceed, mapped from YANG variable /police_priority_map/exceed/map_pri1_exceed (priority-value)
    """
    return self.__map_pri1_exceed
      
  def _set_map_pri1_exceed(self, v, load=False):
    """
    Setter method for map_pri1_exceed, mapped from YANG variable /police_priority_map/exceed/map_pri1_exceed (priority-value)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_map_pri1_exceed is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_map_pri1_exceed() directly.
    """
    if hasattr(v, "_utype"):
      v = v._utype(v)
    try:
      t = YANGDynClass(v,base=RestrictedClassType(base_type=RestrictedClassType(base_type=long, restriction_dict={'range': ['0..4294967295']}, int_size=32), restriction_dict={'range': [u'0..7']}), is_leaf=True, yang_name="map-pri1-exceed", rest_name="", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'info': u'Mapping Priority Number 1', u'cli-drop-node-name': None, u'cli-incomplete-command': None, u'cli-suppress-no': None}}, namespace='urn:brocade.com:mgmt:brocade-policer', defining_module='brocade-policer', yang_type='priority-value', is_config=True)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """map_pri1_exceed must be of a type compatible with priority-value""",
          'defined-type': "brocade-policer:priority-value",
          'generated-type': """YANGDynClass(base=RestrictedClassType(base_type=RestrictedClassType(base_type=long, restriction_dict={'range': ['0..4294967295']}, int_size=32), restriction_dict={'range': [u'0..7']}), is_leaf=True, yang_name="map-pri1-exceed", rest_name="", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'info': u'Mapping Priority Number 1', u'cli-drop-node-name': None, u'cli-incomplete-command': None, u'cli-suppress-no': None}}, namespace='urn:brocade.com:mgmt:brocade-policer', defining_module='brocade-policer', yang_type='priority-value', is_config=True)""",
        })

    self.__map_pri1_exceed = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_map_pri1_exceed(self):
    self.__map_pri1_exceed = YANGDynClass(base=RestrictedClassType(base_type=RestrictedClassType(base_type=long, restriction_dict={'range': ['0..4294967295']}, int_size=32), restriction_dict={'range': [u'0..7']}), is_leaf=True, yang_name="map-pri1-exceed", rest_name="", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'info': u'Mapping Priority Number 1', u'cli-drop-node-name': None, u'cli-incomplete-command': None, u'cli-suppress-no': None}}, namespace='urn:brocade.com:mgmt:brocade-policer', defining_module='brocade-policer', yang_type='priority-value', is_config=True)


  def _get_map_pri2_exceed(self):
    """
    Getter method for map_pri2_exceed, mapped from YANG variable /police_priority_map/exceed/map_pri2_exceed (priority-value)
    """
    return self.__map_pri2_exceed
      
  def _set_map_pri2_exceed(self, v, load=False):
    """
    Setter method for map_pri2_exceed, mapped from YANG variable /police_priority_map/exceed/map_pri2_exceed (priority-value)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_map_pri2_exceed is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_map_pri2_exceed() directly.
    """
    if hasattr(v, "_utype"):
      v = v._utype(v)
    try:
      t = YANGDynClass(v,base=RestrictedClassType(base_type=RestrictedClassType(base_type=long, restriction_dict={'range': ['0..4294967295']}, int_size=32), restriction_dict={'range': [u'0..7']}), is_leaf=True, yang_name="map-pri2-exceed", rest_name="", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'info': u'Mapping Priority Number 2', u'cli-drop-node-name': None, u'cli-incomplete-command': None, u'cli-suppress-no': None}}, namespace='urn:brocade.com:mgmt:brocade-policer', defining_module='brocade-policer', yang_type='priority-value', is_config=True)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """map_pri2_exceed must be of a type compatible with priority-value""",
          'defined-type': "brocade-policer:priority-value",
          'generated-type': """YANGDynClass(base=RestrictedClassType(base_type=RestrictedClassType(base_type=long, restriction_dict={'range': ['0..4294967295']}, int_size=32), restriction_dict={'range': [u'0..7']}), is_leaf=True, yang_name="map-pri2-exceed", rest_name="", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'info': u'Mapping Priority Number 2', u'cli-drop-node-name': None, u'cli-incomplete-command': None, u'cli-suppress-no': None}}, namespace='urn:brocade.com:mgmt:brocade-policer', defining_module='brocade-policer', yang_type='priority-value', is_config=True)""",
        })

    self.__map_pri2_exceed = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_map_pri2_exceed(self):
    self.__map_pri2_exceed = YANGDynClass(base=RestrictedClassType(base_type=RestrictedClassType(base_type=long, restriction_dict={'range': ['0..4294967295']}, int_size=32), restriction_dict={'range': [u'0..7']}), is_leaf=True, yang_name="map-pri2-exceed", rest_name="", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'info': u'Mapping Priority Number 2', u'cli-drop-node-name': None, u'cli-incomplete-command': None, u'cli-suppress-no': None}}, namespace='urn:brocade.com:mgmt:brocade-policer', defining_module='brocade-policer', yang_type='priority-value', is_config=True)


  def _get_map_pri3_exceed(self):
    """
    Getter method for map_pri3_exceed, mapped from YANG variable /police_priority_map/exceed/map_pri3_exceed (priority-value)
    """
    return self.__map_pri3_exceed
      
  def _set_map_pri3_exceed(self, v, load=False):
    """
    Setter method for map_pri3_exceed, mapped from YANG variable /police_priority_map/exceed/map_pri3_exceed (priority-value)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_map_pri3_exceed is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_map_pri3_exceed() directly.
    """
    if hasattr(v, "_utype"):
      v = v._utype(v)
    try:
      t = YANGDynClass(v,base=RestrictedClassType(base_type=RestrictedClassType(base_type=long, restriction_dict={'range': ['0..4294967295']}, int_size=32), restriction_dict={'range': [u'0..7']}), is_leaf=True, yang_name="map-pri3-exceed", rest_name="", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'info': u'Mapping Priority Number 3', u'cli-drop-node-name': None, u'cli-incomplete-command': None, u'cli-suppress-no': None}}, namespace='urn:brocade.com:mgmt:brocade-policer', defining_module='brocade-policer', yang_type='priority-value', is_config=True)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """map_pri3_exceed must be of a type compatible with priority-value""",
          'defined-type': "brocade-policer:priority-value",
          'generated-type': """YANGDynClass(base=RestrictedClassType(base_type=RestrictedClassType(base_type=long, restriction_dict={'range': ['0..4294967295']}, int_size=32), restriction_dict={'range': [u'0..7']}), is_leaf=True, yang_name="map-pri3-exceed", rest_name="", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'info': u'Mapping Priority Number 3', u'cli-drop-node-name': None, u'cli-incomplete-command': None, u'cli-suppress-no': None}}, namespace='urn:brocade.com:mgmt:brocade-policer', defining_module='brocade-policer', yang_type='priority-value', is_config=True)""",
        })

    self.__map_pri3_exceed = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_map_pri3_exceed(self):
    self.__map_pri3_exceed = YANGDynClass(base=RestrictedClassType(base_type=RestrictedClassType(base_type=long, restriction_dict={'range': ['0..4294967295']}, int_size=32), restriction_dict={'range': [u'0..7']}), is_leaf=True, yang_name="map-pri3-exceed", rest_name="", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'info': u'Mapping Priority Number 3', u'cli-drop-node-name': None, u'cli-incomplete-command': None, u'cli-suppress-no': None}}, namespace='urn:brocade.com:mgmt:brocade-policer', defining_module='brocade-policer', yang_type='priority-value', is_config=True)


  def _get_map_pri4_exceed(self):
    """
    Getter method for map_pri4_exceed, mapped from YANG variable /police_priority_map/exceed/map_pri4_exceed (priority-value)
    """
    return self.__map_pri4_exceed
      
  def _set_map_pri4_exceed(self, v, load=False):
    """
    Setter method for map_pri4_exceed, mapped from YANG variable /police_priority_map/exceed/map_pri4_exceed (priority-value)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_map_pri4_exceed is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_map_pri4_exceed() directly.
    """
    if hasattr(v, "_utype"):
      v = v._utype(v)
    try:
      t = YANGDynClass(v,base=RestrictedClassType(base_type=RestrictedClassType(base_type=long, restriction_dict={'range': ['0..4294967295']}, int_size=32), restriction_dict={'range': [u'0..7']}), is_leaf=True, yang_name="map-pri4-exceed", rest_name="", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'info': u'Mapping Priority Number 4', u'cli-drop-node-name': None, u'cli-incomplete-command': None, u'cli-suppress-no': None}}, namespace='urn:brocade.com:mgmt:brocade-policer', defining_module='brocade-policer', yang_type='priority-value', is_config=True)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """map_pri4_exceed must be of a type compatible with priority-value""",
          'defined-type': "brocade-policer:priority-value",
          'generated-type': """YANGDynClass(base=RestrictedClassType(base_type=RestrictedClassType(base_type=long, restriction_dict={'range': ['0..4294967295']}, int_size=32), restriction_dict={'range': [u'0..7']}), is_leaf=True, yang_name="map-pri4-exceed", rest_name="", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'info': u'Mapping Priority Number 4', u'cli-drop-node-name': None, u'cli-incomplete-command': None, u'cli-suppress-no': None}}, namespace='urn:brocade.com:mgmt:brocade-policer', defining_module='brocade-policer', yang_type='priority-value', is_config=True)""",
        })

    self.__map_pri4_exceed = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_map_pri4_exceed(self):
    self.__map_pri4_exceed = YANGDynClass(base=RestrictedClassType(base_type=RestrictedClassType(base_type=long, restriction_dict={'range': ['0..4294967295']}, int_size=32), restriction_dict={'range': [u'0..7']}), is_leaf=True, yang_name="map-pri4-exceed", rest_name="", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'info': u'Mapping Priority Number 4', u'cli-drop-node-name': None, u'cli-incomplete-command': None, u'cli-suppress-no': None}}, namespace='urn:brocade.com:mgmt:brocade-policer', defining_module='brocade-policer', yang_type='priority-value', is_config=True)


  def _get_map_pri5_exceed(self):
    """
    Getter method for map_pri5_exceed, mapped from YANG variable /police_priority_map/exceed/map_pri5_exceed (priority-value)
    """
    return self.__map_pri5_exceed
      
  def _set_map_pri5_exceed(self, v, load=False):
    """
    Setter method for map_pri5_exceed, mapped from YANG variable /police_priority_map/exceed/map_pri5_exceed (priority-value)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_map_pri5_exceed is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_map_pri5_exceed() directly.
    """
    if hasattr(v, "_utype"):
      v = v._utype(v)
    try:
      t = YANGDynClass(v,base=RestrictedClassType(base_type=RestrictedClassType(base_type=long, restriction_dict={'range': ['0..4294967295']}, int_size=32), restriction_dict={'range': [u'0..7']}), is_leaf=True, yang_name="map-pri5-exceed", rest_name="", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'info': u'Mapping Priority Number 5', u'cli-drop-node-name': None, u'cli-incomplete-command': None, u'cli-suppress-no': None}}, namespace='urn:brocade.com:mgmt:brocade-policer', defining_module='brocade-policer', yang_type='priority-value', is_config=True)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """map_pri5_exceed must be of a type compatible with priority-value""",
          'defined-type': "brocade-policer:priority-value",
          'generated-type': """YANGDynClass(base=RestrictedClassType(base_type=RestrictedClassType(base_type=long, restriction_dict={'range': ['0..4294967295']}, int_size=32), restriction_dict={'range': [u'0..7']}), is_leaf=True, yang_name="map-pri5-exceed", rest_name="", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'info': u'Mapping Priority Number 5', u'cli-drop-node-name': None, u'cli-incomplete-command': None, u'cli-suppress-no': None}}, namespace='urn:brocade.com:mgmt:brocade-policer', defining_module='brocade-policer', yang_type='priority-value', is_config=True)""",
        })

    self.__map_pri5_exceed = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_map_pri5_exceed(self):
    self.__map_pri5_exceed = YANGDynClass(base=RestrictedClassType(base_type=RestrictedClassType(base_type=long, restriction_dict={'range': ['0..4294967295']}, int_size=32), restriction_dict={'range': [u'0..7']}), is_leaf=True, yang_name="map-pri5-exceed", rest_name="", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'info': u'Mapping Priority Number 5', u'cli-drop-node-name': None, u'cli-incomplete-command': None, u'cli-suppress-no': None}}, namespace='urn:brocade.com:mgmt:brocade-policer', defining_module='brocade-policer', yang_type='priority-value', is_config=True)


  def _get_map_pri6_exceed(self):
    """
    Getter method for map_pri6_exceed, mapped from YANG variable /police_priority_map/exceed/map_pri6_exceed (priority-value)
    """
    return self.__map_pri6_exceed
      
  def _set_map_pri6_exceed(self, v, load=False):
    """
    Setter method for map_pri6_exceed, mapped from YANG variable /police_priority_map/exceed/map_pri6_exceed (priority-value)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_map_pri6_exceed is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_map_pri6_exceed() directly.
    """
    if hasattr(v, "_utype"):
      v = v._utype(v)
    try:
      t = YANGDynClass(v,base=RestrictedClassType(base_type=RestrictedClassType(base_type=long, restriction_dict={'range': ['0..4294967295']}, int_size=32), restriction_dict={'range': [u'0..7']}), is_leaf=True, yang_name="map-pri6-exceed", rest_name="", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'info': u'Mapping Priority Number 6', u'cli-drop-node-name': None, u'cli-incomplete-command': None, u'cli-suppress-no': None}}, namespace='urn:brocade.com:mgmt:brocade-policer', defining_module='brocade-policer', yang_type='priority-value', is_config=True)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """map_pri6_exceed must be of a type compatible with priority-value""",
          'defined-type': "brocade-policer:priority-value",
          'generated-type': """YANGDynClass(base=RestrictedClassType(base_type=RestrictedClassType(base_type=long, restriction_dict={'range': ['0..4294967295']}, int_size=32), restriction_dict={'range': [u'0..7']}), is_leaf=True, yang_name="map-pri6-exceed", rest_name="", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'info': u'Mapping Priority Number 6', u'cli-drop-node-name': None, u'cli-incomplete-command': None, u'cli-suppress-no': None}}, namespace='urn:brocade.com:mgmt:brocade-policer', defining_module='brocade-policer', yang_type='priority-value', is_config=True)""",
        })

    self.__map_pri6_exceed = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_map_pri6_exceed(self):
    self.__map_pri6_exceed = YANGDynClass(base=RestrictedClassType(base_type=RestrictedClassType(base_type=long, restriction_dict={'range': ['0..4294967295']}, int_size=32), restriction_dict={'range': [u'0..7']}), is_leaf=True, yang_name="map-pri6-exceed", rest_name="", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'info': u'Mapping Priority Number 6', u'cli-drop-node-name': None, u'cli-incomplete-command': None, u'cli-suppress-no': None}}, namespace='urn:brocade.com:mgmt:brocade-policer', defining_module='brocade-policer', yang_type='priority-value', is_config=True)


  def _get_map_pri7_exceed(self):
    """
    Getter method for map_pri7_exceed, mapped from YANG variable /police_priority_map/exceed/map_pri7_exceed (priority-value)
    """
    return self.__map_pri7_exceed
      
  def _set_map_pri7_exceed(self, v, load=False):
    """
    Setter method for map_pri7_exceed, mapped from YANG variable /police_priority_map/exceed/map_pri7_exceed (priority-value)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_map_pri7_exceed is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_map_pri7_exceed() directly.
    """
    if hasattr(v, "_utype"):
      v = v._utype(v)
    try:
      t = YANGDynClass(v,base=RestrictedClassType(base_type=RestrictedClassType(base_type=long, restriction_dict={'range': ['0..4294967295']}, int_size=32), restriction_dict={'range': [u'0..7']}), is_leaf=True, yang_name="map-pri7-exceed", rest_name="", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'info': u'Mapping Priority Number 7', u'cli-drop-node-name': None, u'cli-suppress-no': None}}, namespace='urn:brocade.com:mgmt:brocade-policer', defining_module='brocade-policer', yang_type='priority-value', is_config=True)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """map_pri7_exceed must be of a type compatible with priority-value""",
          'defined-type': "brocade-policer:priority-value",
          'generated-type': """YANGDynClass(base=RestrictedClassType(base_type=RestrictedClassType(base_type=long, restriction_dict={'range': ['0..4294967295']}, int_size=32), restriction_dict={'range': [u'0..7']}), is_leaf=True, yang_name="map-pri7-exceed", rest_name="", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'info': u'Mapping Priority Number 7', u'cli-drop-node-name': None, u'cli-suppress-no': None}}, namespace='urn:brocade.com:mgmt:brocade-policer', defining_module='brocade-policer', yang_type='priority-value', is_config=True)""",
        })

    self.__map_pri7_exceed = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_map_pri7_exceed(self):
    self.__map_pri7_exceed = YANGDynClass(base=RestrictedClassType(base_type=RestrictedClassType(base_type=long, restriction_dict={'range': ['0..4294967295']}, int_size=32), restriction_dict={'range': [u'0..7']}), is_leaf=True, yang_name="map-pri7-exceed", rest_name="", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'info': u'Mapping Priority Number 7', u'cli-drop-node-name': None, u'cli-suppress-no': None}}, namespace='urn:brocade.com:mgmt:brocade-policer', defining_module='brocade-policer', yang_type='priority-value', is_config=True)

  map_pri0_exceed = __builtin__.property(_get_map_pri0_exceed, _set_map_pri0_exceed)
  map_pri1_exceed = __builtin__.property(_get_map_pri1_exceed, _set_map_pri1_exceed)
  map_pri2_exceed = __builtin__.property(_get_map_pri2_exceed, _set_map_pri2_exceed)
  map_pri3_exceed = __builtin__.property(_get_map_pri3_exceed, _set_map_pri3_exceed)
  map_pri4_exceed = __builtin__.property(_get_map_pri4_exceed, _set_map_pri4_exceed)
  map_pri5_exceed = __builtin__.property(_get_map_pri5_exceed, _set_map_pri5_exceed)
  map_pri6_exceed = __builtin__.property(_get_map_pri6_exceed, _set_map_pri6_exceed)
  map_pri7_exceed = __builtin__.property(_get_map_pri7_exceed, _set_map_pri7_exceed)


  _pyangbind_elements = {'map_pri0_exceed': map_pri0_exceed, 'map_pri1_exceed': map_pri1_exceed, 'map_pri2_exceed': map_pri2_exceed, 'map_pri3_exceed': map_pri3_exceed, 'map_pri4_exceed': map_pri4_exceed, 'map_pri5_exceed': map_pri5_exceed, 'map_pri6_exceed': map_pri6_exceed, 'map_pri7_exceed': map_pri7_exceed, }


