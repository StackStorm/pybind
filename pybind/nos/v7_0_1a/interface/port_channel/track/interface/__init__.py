
from operator import attrgetter
import pyangbind.lib.xpathhelper as xpathhelper
from pyangbind.lib.yangtypes import RestrictedPrecisionDecimalType, RestrictedClassType, TypedListType
from pyangbind.lib.yangtypes import YANGBool, YANGListType, YANGDynClass, ReferenceType
from pyangbind.lib.base import PybindBase
from decimal import Decimal
from bitarray import bitarray
import __builtin__
class interface(PybindBase):
  """
  This class was auto-generated by the PythonClass plugin for PYANG
  from YANG module brocade-interface - based on the path /interface/port-channel/track/interface. Each member element of
  the container is represented as a class variable - with a specific
  YANG type.

  YANG Description: Interface or Port-channel to be tracked
  """
  __slots__ = ('_pybind_generated_by', '_path_helper', '_yang_name', '_rest_name', '_extmethods', '__track_interface_type','__track_interface_name',)

  _yang_name = 'interface'
  _rest_name = 'interface'

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
    self.__track_interface_type = YANGDynClass(base=RestrictedClassType(base_type=unicode,                                     restriction_type="dict_key",                                     restriction_arg={u'ethernet': {'value': 0}, u'port-channel': {'value': 1}},), is_leaf=True, yang_name="track-interface-type", rest_name="", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'cli-drop-node-name': None}}, is_keyval=True, namespace='urn:brocade.com:mgmt:brocade-interface', defining_module='brocade-interface', yang_type='enumeration', is_config=True)
    self.__track_interface_name = YANGDynClass(base=RestrictedClassType(base_type=unicode, restriction_dict={'pattern': u'(((([1-9]|[1-9][0-9]|1[0-9]{2}|2[0-3][0-9])/)?(([0-9]|1[0-6]))/([1-9]|[1-9][0-9]|[1-9][0-9][0-9])(:[1-4])?)|([1-9]|[1-9][0-9]|[1-9][0-9]{2}|[1-5][0-9]{3}|6[0-1][0-4]{2}))'}), is_leaf=True, yang_name="track-interface-name", rest_name="", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'info': u'Interface name', u'cli-drop-node-name': None}}, is_keyval=True, namespace='urn:brocade.com:mgmt:brocade-interface', defining_module='brocade-interface', yang_type='string', is_config=True)

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
      return [u'interface', u'port-channel', u'track', u'interface']

  def _rest_path(self):
    if hasattr(self, "_parent"):
      if self._rest_name:
        return self._parent._rest_path()+[self._rest_name]
      else:
        return self._parent._rest_path()
    else:
      return [u'interface', u'Port-channel', u'track', u'interface']

  def _get_track_interface_type(self):
    """
    Getter method for track_interface_type, mapped from YANG variable /interface/port_channel/track/interface/track_interface_type (enumeration)
    """
    return self.__track_interface_type
      
  def _set_track_interface_type(self, v, load=False):
    """
    Setter method for track_interface_type, mapped from YANG variable /interface/port_channel/track/interface/track_interface_type (enumeration)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_track_interface_type is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_track_interface_type() directly.
    """
    parent = getattr(self, "_parent", None)
    if parent is not None and load is False:
      raise AttributeError("Cannot set keys directly when" +
                             " within an instantiated list")

    try:
      t = YANGDynClass(v,base=RestrictedClassType(base_type=unicode,                                     restriction_type="dict_key",                                     restriction_arg={u'ethernet': {'value': 0}, u'port-channel': {'value': 1}},), is_leaf=True, yang_name="track-interface-type", rest_name="", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'cli-drop-node-name': None}}, is_keyval=True, namespace='urn:brocade.com:mgmt:brocade-interface', defining_module='brocade-interface', yang_type='enumeration', is_config=True)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """track_interface_type must be of a type compatible with enumeration""",
          'defined-type': "brocade-interface:enumeration",
          'generated-type': """YANGDynClass(base=RestrictedClassType(base_type=unicode,                                     restriction_type="dict_key",                                     restriction_arg={u'ethernet': {'value': 0}, u'port-channel': {'value': 1}},), is_leaf=True, yang_name="track-interface-type", rest_name="", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'cli-drop-node-name': None}}, is_keyval=True, namespace='urn:brocade.com:mgmt:brocade-interface', defining_module='brocade-interface', yang_type='enumeration', is_config=True)""",
        })

    self.__track_interface_type = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_track_interface_type(self):
    self.__track_interface_type = YANGDynClass(base=RestrictedClassType(base_type=unicode,                                     restriction_type="dict_key",                                     restriction_arg={u'ethernet': {'value': 0}, u'port-channel': {'value': 1}},), is_leaf=True, yang_name="track-interface-type", rest_name="", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'cli-drop-node-name': None}}, is_keyval=True, namespace='urn:brocade.com:mgmt:brocade-interface', defining_module='brocade-interface', yang_type='enumeration', is_config=True)


  def _get_track_interface_name(self):
    """
    Getter method for track_interface_name, mapped from YANG variable /interface/port_channel/track/interface/track_interface_name (string)

    YANG Description: Interface name
    """
    return self.__track_interface_name
      
  def _set_track_interface_name(self, v, load=False):
    """
    Setter method for track_interface_name, mapped from YANG variable /interface/port_channel/track/interface/track_interface_name (string)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_track_interface_name is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_track_interface_name() directly.

    YANG Description: Interface name
    """
    parent = getattr(self, "_parent", None)
    if parent is not None and load is False:
      raise AttributeError("Cannot set keys directly when" +
                             " within an instantiated list")

    try:
      t = YANGDynClass(v,base=RestrictedClassType(base_type=unicode, restriction_dict={'pattern': u'(((([1-9]|[1-9][0-9]|1[0-9]{2}|2[0-3][0-9])/)?(([0-9]|1[0-6]))/([1-9]|[1-9][0-9]|[1-9][0-9][0-9])(:[1-4])?)|([1-9]|[1-9][0-9]|[1-9][0-9]{2}|[1-5][0-9]{3}|6[0-1][0-4]{2}))'}), is_leaf=True, yang_name="track-interface-name", rest_name="", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'info': u'Interface name', u'cli-drop-node-name': None}}, is_keyval=True, namespace='urn:brocade.com:mgmt:brocade-interface', defining_module='brocade-interface', yang_type='string', is_config=True)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """track_interface_name must be of a type compatible with string""",
          'defined-type': "string",
          'generated-type': """YANGDynClass(base=RestrictedClassType(base_type=unicode, restriction_dict={'pattern': u'(((([1-9]|[1-9][0-9]|1[0-9]{2}|2[0-3][0-9])/)?(([0-9]|1[0-6]))/([1-9]|[1-9][0-9]|[1-9][0-9][0-9])(:[1-4])?)|([1-9]|[1-9][0-9]|[1-9][0-9]{2}|[1-5][0-9]{3}|6[0-1][0-4]{2}))'}), is_leaf=True, yang_name="track-interface-name", rest_name="", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'info': u'Interface name', u'cli-drop-node-name': None}}, is_keyval=True, namespace='urn:brocade.com:mgmt:brocade-interface', defining_module='brocade-interface', yang_type='string', is_config=True)""",
        })

    self.__track_interface_name = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_track_interface_name(self):
    self.__track_interface_name = YANGDynClass(base=RestrictedClassType(base_type=unicode, restriction_dict={'pattern': u'(((([1-9]|[1-9][0-9]|1[0-9]{2}|2[0-3][0-9])/)?(([0-9]|1[0-6]))/([1-9]|[1-9][0-9]|[1-9][0-9][0-9])(:[1-4])?)|([1-9]|[1-9][0-9]|[1-9][0-9]{2}|[1-5][0-9]{3}|6[0-1][0-4]{2}))'}), is_leaf=True, yang_name="track-interface-name", rest_name="", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'info': u'Interface name', u'cli-drop-node-name': None}}, is_keyval=True, namespace='urn:brocade.com:mgmt:brocade-interface', defining_module='brocade-interface', yang_type='string', is_config=True)

  track_interface_type = __builtin__.property(_get_track_interface_type, _set_track_interface_type)
  track_interface_name = __builtin__.property(_get_track_interface_name, _set_track_interface_name)


  _pyangbind_elements = {'track_interface_type': track_interface_type, 'track_interface_name': track_interface_name, }

