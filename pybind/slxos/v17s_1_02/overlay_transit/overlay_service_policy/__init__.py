
from operator import attrgetter
import pyangbind.lib.xpathhelper as xpathhelper
from pyangbind.lib.yangtypes import RestrictedPrecisionDecimalType, RestrictedClassType, TypedListType
from pyangbind.lib.yangtypes import YANGBool, YANGListType, YANGDynClass, ReferenceType
from pyangbind.lib.base import PybindBase
from decimal import Decimal
from bitarray import bitarray
import __builtin__
class overlay_service_policy(PybindBase):
  """
  This class was auto-generated by the PythonClass plugin for PYANG
  from YANG module brocade-overlay-policy - based on the path /overlay-transit/overlay-service-policy. Each member element of
  the container is represented as a class variable - with a specific
  YANG type.
  """
  __slots__ = ('_pybind_generated_by', '_path_helper', '_yang_name', '_rest_name', '_extmethods', '__overlay_sp_direction','__overlay_sp_pmap_name',)

  _yang_name = 'overlay-service-policy'
  _rest_name = 'overlay-service-policy'

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
    self.__overlay_sp_direction = YANGDynClass(base=RestrictedClassType(base_type=unicode,                                     restriction_type="dict_key",                                     restriction_arg={u'in': {'value': 1}},), is_leaf=True, yang_name="overlay-sp-direction", rest_name="overlay-sp-direction", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'info': u'Policy Direction: Ingress/In', u'cli-drop-node-name': None}}, is_keyval=True, namespace='urn:brocade.com:mgmt:brocade-overlay-policy', defining_module='brocade-overlay-policy', yang_type='enumeration', is_config=True)
    self.__overlay_sp_pmap_name = YANGDynClass(base=RestrictedClassType(base_type=unicode, restriction_dict={'pattern': u'[a-zA-Z]{1}([-a-zA-Z0-9_]{0,62})'}), is_leaf=True, yang_name="overlay-sp-pmap-name", rest_name="overlay-sp-pmap-name", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'info': u'Overlay Service Policy name (Max Size - 63)'}}, is_keyval=True, namespace='urn:brocade.com:mgmt:brocade-overlay-policy', defining_module='brocade-overlay-policy', yang_type='map-name-type', is_config=True)

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
      return [u'overlay-transit', u'overlay-service-policy']

  def _rest_path(self):
    if hasattr(self, "_parent"):
      if self._rest_name:
        return self._parent._rest_path()+[self._rest_name]
      else:
        return self._parent._rest_path()
    else:
      return [u'overlay-transit', u'overlay-service-policy']

  def _get_overlay_sp_direction(self):
    """
    Getter method for overlay_sp_direction, mapped from YANG variable /overlay_transit/overlay_service_policy/overlay_sp_direction (enumeration)
    """
    return self.__overlay_sp_direction
      
  def _set_overlay_sp_direction(self, v, load=False):
    """
    Setter method for overlay_sp_direction, mapped from YANG variable /overlay_transit/overlay_service_policy/overlay_sp_direction (enumeration)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_overlay_sp_direction is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_overlay_sp_direction() directly.
    """
    parent = getattr(self, "_parent", None)
    if parent is not None and load is False:
      raise AttributeError("Cannot set keys directly when" +
                             " within an instantiated list")

    if hasattr(v, "_utype"):
      v = v._utype(v)
    try:
      t = YANGDynClass(v,base=RestrictedClassType(base_type=unicode,                                     restriction_type="dict_key",                                     restriction_arg={u'in': {'value': 1}},), is_leaf=True, yang_name="overlay-sp-direction", rest_name="overlay-sp-direction", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'info': u'Policy Direction: Ingress/In', u'cli-drop-node-name': None}}, is_keyval=True, namespace='urn:brocade.com:mgmt:brocade-overlay-policy', defining_module='brocade-overlay-policy', yang_type='enumeration', is_config=True)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """overlay_sp_direction must be of a type compatible with enumeration""",
          'defined-type': "brocade-overlay-policy:enumeration",
          'generated-type': """YANGDynClass(base=RestrictedClassType(base_type=unicode,                                     restriction_type="dict_key",                                     restriction_arg={u'in': {'value': 1}},), is_leaf=True, yang_name="overlay-sp-direction", rest_name="overlay-sp-direction", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'info': u'Policy Direction: Ingress/In', u'cli-drop-node-name': None}}, is_keyval=True, namespace='urn:brocade.com:mgmt:brocade-overlay-policy', defining_module='brocade-overlay-policy', yang_type='enumeration', is_config=True)""",
        })

    self.__overlay_sp_direction = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_overlay_sp_direction(self):
    self.__overlay_sp_direction = YANGDynClass(base=RestrictedClassType(base_type=unicode,                                     restriction_type="dict_key",                                     restriction_arg={u'in': {'value': 1}},), is_leaf=True, yang_name="overlay-sp-direction", rest_name="overlay-sp-direction", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'info': u'Policy Direction: Ingress/In', u'cli-drop-node-name': None}}, is_keyval=True, namespace='urn:brocade.com:mgmt:brocade-overlay-policy', defining_module='brocade-overlay-policy', yang_type='enumeration', is_config=True)


  def _get_overlay_sp_pmap_name(self):
    """
    Getter method for overlay_sp_pmap_name, mapped from YANG variable /overlay_transit/overlay_service_policy/overlay_sp_pmap_name (map-name-type)
    """
    return self.__overlay_sp_pmap_name
      
  def _set_overlay_sp_pmap_name(self, v, load=False):
    """
    Setter method for overlay_sp_pmap_name, mapped from YANG variable /overlay_transit/overlay_service_policy/overlay_sp_pmap_name (map-name-type)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_overlay_sp_pmap_name is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_overlay_sp_pmap_name() directly.
    """
    parent = getattr(self, "_parent", None)
    if parent is not None and load is False:
      raise AttributeError("Cannot set keys directly when" +
                             " within an instantiated list")

    if hasattr(v, "_utype"):
      v = v._utype(v)
    try:
      t = YANGDynClass(v,base=RestrictedClassType(base_type=unicode, restriction_dict={'pattern': u'[a-zA-Z]{1}([-a-zA-Z0-9_]{0,62})'}), is_leaf=True, yang_name="overlay-sp-pmap-name", rest_name="overlay-sp-pmap-name", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'info': u'Overlay Service Policy name (Max Size - 63)'}}, is_keyval=True, namespace='urn:brocade.com:mgmt:brocade-overlay-policy', defining_module='brocade-overlay-policy', yang_type='map-name-type', is_config=True)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """overlay_sp_pmap_name must be of a type compatible with map-name-type""",
          'defined-type': "brocade-overlay-policy:map-name-type",
          'generated-type': """YANGDynClass(base=RestrictedClassType(base_type=unicode, restriction_dict={'pattern': u'[a-zA-Z]{1}([-a-zA-Z0-9_]{0,62})'}), is_leaf=True, yang_name="overlay-sp-pmap-name", rest_name="overlay-sp-pmap-name", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'info': u'Overlay Service Policy name (Max Size - 63)'}}, is_keyval=True, namespace='urn:brocade.com:mgmt:brocade-overlay-policy', defining_module='brocade-overlay-policy', yang_type='map-name-type', is_config=True)""",
        })

    self.__overlay_sp_pmap_name = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_overlay_sp_pmap_name(self):
    self.__overlay_sp_pmap_name = YANGDynClass(base=RestrictedClassType(base_type=unicode, restriction_dict={'pattern': u'[a-zA-Z]{1}([-a-zA-Z0-9_]{0,62})'}), is_leaf=True, yang_name="overlay-sp-pmap-name", rest_name="overlay-sp-pmap-name", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'info': u'Overlay Service Policy name (Max Size - 63)'}}, is_keyval=True, namespace='urn:brocade.com:mgmt:brocade-overlay-policy', defining_module='brocade-overlay-policy', yang_type='map-name-type', is_config=True)

  overlay_sp_direction = __builtin__.property(_get_overlay_sp_direction, _set_overlay_sp_direction)
  overlay_sp_pmap_name = __builtin__.property(_get_overlay_sp_pmap_name, _set_overlay_sp_pmap_name)


  _pyangbind_elements = {'overlay_sp_direction': overlay_sp_direction, 'overlay_sp_pmap_name': overlay_sp_pmap_name, }


