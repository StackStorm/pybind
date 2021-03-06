
from operator import attrgetter
import pyangbind.lib.xpathhelper as xpathhelper
from pyangbind.lib.yangtypes import RestrictedPrecisionDecimalType, RestrictedClassType, TypedListType
from pyangbind.lib.yangtypes import YANGBool, YANGListType, YANGDynClass, ReferenceType
from pyangbind.lib.base import PybindBase
from decimal import Decimal
from bitarray import bitarray
import __builtin__
class isis(PybindBase):
  """
  This class was auto-generated by the PythonClass plugin for PYANG
  from YANG module brocade-common-def - based on the path /routing-system/router/ospf/redistribute/isis. Each member element of
  the container is represented as a class variable - with a specific
  YANG type.
  """
  __slots__ = ('_pybind_generated_by', '_path_helper', '_yang_name', '_rest_name', '_extmethods', '__isis_level_one','__isis_level_two','__isis_level_one_and_two','__isis_route_map',)

  _yang_name = 'isis'
  _rest_name = 'isis'

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
    self.__isis_level_one_and_two = YANGDynClass(base=YANGBool, is_leaf=True, yang_name="isis-level-one-and-two", rest_name="level-1-2", parent=self, choice=(u'ch-isis-level', u'ca-level-1-2'), path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'cli-full-command': None, u'info': u'Redistribution of IS-IS Level-1-2 routes', u'alt-name': u'level-1-2', u'cli-full-no': None}}, namespace='urn:brocade.com:mgmt:brocade-ospf', defining_module='brocade-ospf', yang_type='empty', is_config=True)
    self.__isis_level_two = YANGDynClass(base=YANGBool, is_leaf=True, yang_name="isis-level-two", rest_name="level-2", parent=self, choice=(u'ch-isis-level', u'ca-level-2'), path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'cli-full-command': None, u'info': u'Redistribution of IS-IS Level-2 routes', u'alt-name': u'level-2', u'cli-full-no': None}}, namespace='urn:brocade.com:mgmt:brocade-ospf', defining_module='brocade-ospf', yang_type='empty', is_config=True)
    self.__isis_level_one = YANGDynClass(base=YANGBool, is_leaf=True, yang_name="isis-level-one", rest_name="level-1", parent=self, choice=(u'ch-isis-level', u'ca-level-1'), path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'cli-full-command': None, u'info': u'Redistribution of IS-IS Level-1 routes', u'alt-name': u'level-1', u'cli-full-no': None}}, namespace='urn:brocade.com:mgmt:brocade-ospf', defining_module='brocade-ospf', yang_type='empty', is_config=True)
    self.__isis_route_map = YANGDynClass(base=RestrictedClassType(base_type=unicode, restriction_dict={'pattern': u'[a-zA-Z]{1}([-a-zA-Z0-9\\.\\\\\\\\@#\\+\\*\\(\\)=\\{~\\}%<>=$_\\[\\]\\|]{0,62})'}), is_leaf=True, yang_name="isis-route-map", rest_name="route-map", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'cli-full-command': None, u'info': u'Route map reference', u'alt-name': u'route-map', u'cli-full-no': None}}, namespace='urn:brocade.com:mgmt:brocade-ospf', defining_module='brocade-ospf', yang_type='common-def:name-string63', is_config=True)

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
      return [u'routing-system', u'router', u'ospf', u'redistribute', u'isis']

  def _rest_path(self):
    if hasattr(self, "_parent"):
      if self._rest_name:
        return self._parent._rest_path()+[self._rest_name]
      else:
        return self._parent._rest_path()
    else:
      return [u'router', u'ospf', u'redistribute', u'isis']

  def _get_isis_level_one(self):
    """
    Getter method for isis_level_one, mapped from YANG variable /routing_system/router/ospf/redistribute/isis/isis_level_one (empty)
    """
    return self.__isis_level_one
      
  def _set_isis_level_one(self, v, load=False):
    """
    Setter method for isis_level_one, mapped from YANG variable /routing_system/router/ospf/redistribute/isis/isis_level_one (empty)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_isis_level_one is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_isis_level_one() directly.
    """
    if hasattr(v, "_utype"):
      v = v._utype(v)
    try:
      t = YANGDynClass(v,base=YANGBool, is_leaf=True, yang_name="isis-level-one", rest_name="level-1", parent=self, choice=(u'ch-isis-level', u'ca-level-1'), path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'cli-full-command': None, u'info': u'Redistribution of IS-IS Level-1 routes', u'alt-name': u'level-1', u'cli-full-no': None}}, namespace='urn:brocade.com:mgmt:brocade-ospf', defining_module='brocade-ospf', yang_type='empty', is_config=True)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """isis_level_one must be of a type compatible with empty""",
          'defined-type': "empty",
          'generated-type': """YANGDynClass(base=YANGBool, is_leaf=True, yang_name="isis-level-one", rest_name="level-1", parent=self, choice=(u'ch-isis-level', u'ca-level-1'), path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'cli-full-command': None, u'info': u'Redistribution of IS-IS Level-1 routes', u'alt-name': u'level-1', u'cli-full-no': None}}, namespace='urn:brocade.com:mgmt:brocade-ospf', defining_module='brocade-ospf', yang_type='empty', is_config=True)""",
        })

    self.__isis_level_one = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_isis_level_one(self):
    self.__isis_level_one = YANGDynClass(base=YANGBool, is_leaf=True, yang_name="isis-level-one", rest_name="level-1", parent=self, choice=(u'ch-isis-level', u'ca-level-1'), path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'cli-full-command': None, u'info': u'Redistribution of IS-IS Level-1 routes', u'alt-name': u'level-1', u'cli-full-no': None}}, namespace='urn:brocade.com:mgmt:brocade-ospf', defining_module='brocade-ospf', yang_type='empty', is_config=True)


  def _get_isis_level_two(self):
    """
    Getter method for isis_level_two, mapped from YANG variable /routing_system/router/ospf/redistribute/isis/isis_level_two (empty)
    """
    return self.__isis_level_two
      
  def _set_isis_level_two(self, v, load=False):
    """
    Setter method for isis_level_two, mapped from YANG variable /routing_system/router/ospf/redistribute/isis/isis_level_two (empty)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_isis_level_two is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_isis_level_two() directly.
    """
    if hasattr(v, "_utype"):
      v = v._utype(v)
    try:
      t = YANGDynClass(v,base=YANGBool, is_leaf=True, yang_name="isis-level-two", rest_name="level-2", parent=self, choice=(u'ch-isis-level', u'ca-level-2'), path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'cli-full-command': None, u'info': u'Redistribution of IS-IS Level-2 routes', u'alt-name': u'level-2', u'cli-full-no': None}}, namespace='urn:brocade.com:mgmt:brocade-ospf', defining_module='brocade-ospf', yang_type='empty', is_config=True)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """isis_level_two must be of a type compatible with empty""",
          'defined-type': "empty",
          'generated-type': """YANGDynClass(base=YANGBool, is_leaf=True, yang_name="isis-level-two", rest_name="level-2", parent=self, choice=(u'ch-isis-level', u'ca-level-2'), path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'cli-full-command': None, u'info': u'Redistribution of IS-IS Level-2 routes', u'alt-name': u'level-2', u'cli-full-no': None}}, namespace='urn:brocade.com:mgmt:brocade-ospf', defining_module='brocade-ospf', yang_type='empty', is_config=True)""",
        })

    self.__isis_level_two = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_isis_level_two(self):
    self.__isis_level_two = YANGDynClass(base=YANGBool, is_leaf=True, yang_name="isis-level-two", rest_name="level-2", parent=self, choice=(u'ch-isis-level', u'ca-level-2'), path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'cli-full-command': None, u'info': u'Redistribution of IS-IS Level-2 routes', u'alt-name': u'level-2', u'cli-full-no': None}}, namespace='urn:brocade.com:mgmt:brocade-ospf', defining_module='brocade-ospf', yang_type='empty', is_config=True)


  def _get_isis_level_one_and_two(self):
    """
    Getter method for isis_level_one_and_two, mapped from YANG variable /routing_system/router/ospf/redistribute/isis/isis_level_one_and_two (empty)
    """
    return self.__isis_level_one_and_two
      
  def _set_isis_level_one_and_two(self, v, load=False):
    """
    Setter method for isis_level_one_and_two, mapped from YANG variable /routing_system/router/ospf/redistribute/isis/isis_level_one_and_two (empty)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_isis_level_one_and_two is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_isis_level_one_and_two() directly.
    """
    if hasattr(v, "_utype"):
      v = v._utype(v)
    try:
      t = YANGDynClass(v,base=YANGBool, is_leaf=True, yang_name="isis-level-one-and-two", rest_name="level-1-2", parent=self, choice=(u'ch-isis-level', u'ca-level-1-2'), path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'cli-full-command': None, u'info': u'Redistribution of IS-IS Level-1-2 routes', u'alt-name': u'level-1-2', u'cli-full-no': None}}, namespace='urn:brocade.com:mgmt:brocade-ospf', defining_module='brocade-ospf', yang_type='empty', is_config=True)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """isis_level_one_and_two must be of a type compatible with empty""",
          'defined-type': "empty",
          'generated-type': """YANGDynClass(base=YANGBool, is_leaf=True, yang_name="isis-level-one-and-two", rest_name="level-1-2", parent=self, choice=(u'ch-isis-level', u'ca-level-1-2'), path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'cli-full-command': None, u'info': u'Redistribution of IS-IS Level-1-2 routes', u'alt-name': u'level-1-2', u'cli-full-no': None}}, namespace='urn:brocade.com:mgmt:brocade-ospf', defining_module='brocade-ospf', yang_type='empty', is_config=True)""",
        })

    self.__isis_level_one_and_two = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_isis_level_one_and_two(self):
    self.__isis_level_one_and_two = YANGDynClass(base=YANGBool, is_leaf=True, yang_name="isis-level-one-and-two", rest_name="level-1-2", parent=self, choice=(u'ch-isis-level', u'ca-level-1-2'), path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'cli-full-command': None, u'info': u'Redistribution of IS-IS Level-1-2 routes', u'alt-name': u'level-1-2', u'cli-full-no': None}}, namespace='urn:brocade.com:mgmt:brocade-ospf', defining_module='brocade-ospf', yang_type='empty', is_config=True)


  def _get_isis_route_map(self):
    """
    Getter method for isis_route_map, mapped from YANG variable /routing_system/router/ospf/redistribute/isis/isis_route_map (common-def:name-string63)
    """
    return self.__isis_route_map
      
  def _set_isis_route_map(self, v, load=False):
    """
    Setter method for isis_route_map, mapped from YANG variable /routing_system/router/ospf/redistribute/isis/isis_route_map (common-def:name-string63)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_isis_route_map is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_isis_route_map() directly.
    """
    if hasattr(v, "_utype"):
      v = v._utype(v)
    try:
      t = YANGDynClass(v,base=RestrictedClassType(base_type=unicode, restriction_dict={'pattern': u'[a-zA-Z]{1}([-a-zA-Z0-9\\.\\\\\\\\@#\\+\\*\\(\\)=\\{~\\}%<>=$_\\[\\]\\|]{0,62})'}), is_leaf=True, yang_name="isis-route-map", rest_name="route-map", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'cli-full-command': None, u'info': u'Route map reference', u'alt-name': u'route-map', u'cli-full-no': None}}, namespace='urn:brocade.com:mgmt:brocade-ospf', defining_module='brocade-ospf', yang_type='common-def:name-string63', is_config=True)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """isis_route_map must be of a type compatible with common-def:name-string63""",
          'defined-type': "common-def:name-string63",
          'generated-type': """YANGDynClass(base=RestrictedClassType(base_type=unicode, restriction_dict={'pattern': u'[a-zA-Z]{1}([-a-zA-Z0-9\\.\\\\\\\\@#\\+\\*\\(\\)=\\{~\\}%<>=$_\\[\\]\\|]{0,62})'}), is_leaf=True, yang_name="isis-route-map", rest_name="route-map", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'cli-full-command': None, u'info': u'Route map reference', u'alt-name': u'route-map', u'cli-full-no': None}}, namespace='urn:brocade.com:mgmt:brocade-ospf', defining_module='brocade-ospf', yang_type='common-def:name-string63', is_config=True)""",
        })

    self.__isis_route_map = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_isis_route_map(self):
    self.__isis_route_map = YANGDynClass(base=RestrictedClassType(base_type=unicode, restriction_dict={'pattern': u'[a-zA-Z]{1}([-a-zA-Z0-9\\.\\\\\\\\@#\\+\\*\\(\\)=\\{~\\}%<>=$_\\[\\]\\|]{0,62})'}), is_leaf=True, yang_name="isis-route-map", rest_name="route-map", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'cli-full-command': None, u'info': u'Route map reference', u'alt-name': u'route-map', u'cli-full-no': None}}, namespace='urn:brocade.com:mgmt:brocade-ospf', defining_module='brocade-ospf', yang_type='common-def:name-string63', is_config=True)

  isis_level_one = __builtin__.property(_get_isis_level_one, _set_isis_level_one)
  isis_level_two = __builtin__.property(_get_isis_level_two, _set_isis_level_two)
  isis_level_one_and_two = __builtin__.property(_get_isis_level_one_and_two, _set_isis_level_one_and_two)
  isis_route_map = __builtin__.property(_get_isis_route_map, _set_isis_route_map)

  __choices__ = {u'ch-isis-level': {u'ca-level-1-2': [u'isis_level_one_and_two'], u'ca-level-1': [u'isis_level_one'], u'ca-level-2': [u'isis_level_two']}}
  _pyangbind_elements = {'isis_level_one': isis_level_one, 'isis_level_two': isis_level_two, 'isis_level_one_and_two': isis_level_one_and_two, 'isis_route_map': isis_route_map, }


