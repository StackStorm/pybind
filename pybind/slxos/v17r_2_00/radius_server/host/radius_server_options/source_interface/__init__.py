
from operator import attrgetter
import pyangbind.lib.xpathhelper as xpathhelper
from pyangbind.lib.yangtypes import RestrictedPrecisionDecimalType, RestrictedClassType, TypedListType
from pyangbind.lib.yangtypes import YANGBool, YANGListType, YANGDynClass, ReferenceType
from pyangbind.lib.base import PybindBase
from decimal import Decimal
from bitarray import bitarray
import __builtin__
class source_interface(PybindBase):
  """
  This class was auto-generated by the PythonClass plugin for PYANG
  from YANG module brocade-aaa - based on the path /radius-server/host/radius-server-options/source-interface. Each member element of
  the container is represented as a class variable - with a specific
  YANG type.
  """
  __slots__ = ('_pybind_generated_by', '_path_helper', '_yang_name', '_rest_name', '_extmethods', '__source_interface_name','__source_interface_value',)

  _yang_name = 'source-interface'
  _rest_name = 'source-interface'

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
    self.__source_interface_name = YANGDynClass(base=RestrictedClassType(base_type=unicode,                                     restriction_type="dict_key",                                     restriction_arg={u'ethernet': {'value': 1}, u'management': {'value': 4}, u've': {'value': 3}, u'loopback': {'value': 2}},), is_leaf=True, yang_name="source-interface-name", rest_name="source-interface-name", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'cli-drop-node-name': None, u'cli-incomplete-command': None}}, namespace='urn:brocade.com:mgmt:brocade-aaa', defining_module='brocade-aaa', yang_type='track-iftype', is_config=True)
    self.__source_interface_value = YANGDynClass(base=[RestrictedClassType(base_type=unicode, restriction_dict={'pattern': u'((([0-9]|[1][0-6]))/([1-9]|[1-9][0-9]|[1-9][0-9][0-9])(:[1-4])?)', 'length': [u'3..16']}),RestrictedClassType(base_type=unicode, restriction_dict={'pattern': u'([1-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])'}),RestrictedClassType(base_type=unicode, restriction_dict={'pattern': u'([1-9]|[1-9][0-9]|[1-9][0-9][0-9]|[1-3][0-9][0-9][0-9]|4[0][0-9][0-6])'}),RestrictedClassType(base_type=unicode, restriction_dict={'pattern': u'([0-1])'}),], is_leaf=True, yang_name="source-interface-value", rest_name="source-interface-value", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'cli-full-command': None, u'cli-drop-node-name': None}}, namespace='urn:brocade.com:mgmt:brocade-aaa', defining_module='brocade-aaa', yang_type='union', is_config=True)

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
      return [u'radius-server', u'host', u'radius-server-options', u'source-interface']

  def _rest_path(self):
    if hasattr(self, "_parent"):
      if self._rest_name:
        return self._parent._rest_path()+[self._rest_name]
      else:
        return self._parent._rest_path()
    else:
      return [u'radius-server', u'host', u'source-interface']

  def _get_source_interface_name(self):
    """
    Getter method for source_interface_name, mapped from YANG variable /radius_server/host/radius_server_options/source_interface/source_interface_name (track-iftype)
    """
    return self.__source_interface_name
      
  def _set_source_interface_name(self, v, load=False):
    """
    Setter method for source_interface_name, mapped from YANG variable /radius_server/host/radius_server_options/source_interface/source_interface_name (track-iftype)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_source_interface_name is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_source_interface_name() directly.
    """
    if hasattr(v, "_utype"):
      v = v._utype(v)
    try:
      t = YANGDynClass(v,base=RestrictedClassType(base_type=unicode,                                     restriction_type="dict_key",                                     restriction_arg={u'ethernet': {'value': 1}, u'management': {'value': 4}, u've': {'value': 3}, u'loopback': {'value': 2}},), is_leaf=True, yang_name="source-interface-name", rest_name="source-interface-name", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'cli-drop-node-name': None, u'cli-incomplete-command': None}}, namespace='urn:brocade.com:mgmt:brocade-aaa', defining_module='brocade-aaa', yang_type='track-iftype', is_config=True)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """source_interface_name must be of a type compatible with track-iftype""",
          'defined-type': "brocade-aaa:track-iftype",
          'generated-type': """YANGDynClass(base=RestrictedClassType(base_type=unicode,                                     restriction_type="dict_key",                                     restriction_arg={u'ethernet': {'value': 1}, u'management': {'value': 4}, u've': {'value': 3}, u'loopback': {'value': 2}},), is_leaf=True, yang_name="source-interface-name", rest_name="source-interface-name", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'cli-drop-node-name': None, u'cli-incomplete-command': None}}, namespace='urn:brocade.com:mgmt:brocade-aaa', defining_module='brocade-aaa', yang_type='track-iftype', is_config=True)""",
        })

    self.__source_interface_name = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_source_interface_name(self):
    self.__source_interface_name = YANGDynClass(base=RestrictedClassType(base_type=unicode,                                     restriction_type="dict_key",                                     restriction_arg={u'ethernet': {'value': 1}, u'management': {'value': 4}, u've': {'value': 3}, u'loopback': {'value': 2}},), is_leaf=True, yang_name="source-interface-name", rest_name="source-interface-name", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'cli-drop-node-name': None, u'cli-incomplete-command': None}}, namespace='urn:brocade.com:mgmt:brocade-aaa', defining_module='brocade-aaa', yang_type='track-iftype', is_config=True)


  def _get_source_interface_value(self):
    """
    Getter method for source_interface_value, mapped from YANG variable /radius_server/host/radius_server_options/source_interface/source_interface_value (union)
    """
    return self.__source_interface_value
      
  def _set_source_interface_value(self, v, load=False):
    """
    Setter method for source_interface_value, mapped from YANG variable /radius_server/host/radius_server_options/source_interface/source_interface_value (union)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_source_interface_value is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_source_interface_value() directly.
    """
    if hasattr(v, "_utype"):
      v = v._utype(v)
    try:
      t = YANGDynClass(v,base=[RestrictedClassType(base_type=unicode, restriction_dict={'pattern': u'((([0-9]|[1][0-6]))/([1-9]|[1-9][0-9]|[1-9][0-9][0-9])(:[1-4])?)', 'length': [u'3..16']}),RestrictedClassType(base_type=unicode, restriction_dict={'pattern': u'([1-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])'}),RestrictedClassType(base_type=unicode, restriction_dict={'pattern': u'([1-9]|[1-9][0-9]|[1-9][0-9][0-9]|[1-3][0-9][0-9][0-9]|4[0][0-9][0-6])'}),RestrictedClassType(base_type=unicode, restriction_dict={'pattern': u'([0-1])'}),], is_leaf=True, yang_name="source-interface-value", rest_name="source-interface-value", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'cli-full-command': None, u'cli-drop-node-name': None}}, namespace='urn:brocade.com:mgmt:brocade-aaa', defining_module='brocade-aaa', yang_type='union', is_config=True)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """source_interface_value must be of a type compatible with union""",
          'defined-type': "brocade-aaa:union",
          'generated-type': """YANGDynClass(base=[RestrictedClassType(base_type=unicode, restriction_dict={'pattern': u'((([0-9]|[1][0-6]))/([1-9]|[1-9][0-9]|[1-9][0-9][0-9])(:[1-4])?)', 'length': [u'3..16']}),RestrictedClassType(base_type=unicode, restriction_dict={'pattern': u'([1-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])'}),RestrictedClassType(base_type=unicode, restriction_dict={'pattern': u'([1-9]|[1-9][0-9]|[1-9][0-9][0-9]|[1-3][0-9][0-9][0-9]|4[0][0-9][0-6])'}),RestrictedClassType(base_type=unicode, restriction_dict={'pattern': u'([0-1])'}),], is_leaf=True, yang_name="source-interface-value", rest_name="source-interface-value", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'cli-full-command': None, u'cli-drop-node-name': None}}, namespace='urn:brocade.com:mgmt:brocade-aaa', defining_module='brocade-aaa', yang_type='union', is_config=True)""",
        })

    self.__source_interface_value = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_source_interface_value(self):
    self.__source_interface_value = YANGDynClass(base=[RestrictedClassType(base_type=unicode, restriction_dict={'pattern': u'((([0-9]|[1][0-6]))/([1-9]|[1-9][0-9]|[1-9][0-9][0-9])(:[1-4])?)', 'length': [u'3..16']}),RestrictedClassType(base_type=unicode, restriction_dict={'pattern': u'([1-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])'}),RestrictedClassType(base_type=unicode, restriction_dict={'pattern': u'([1-9]|[1-9][0-9]|[1-9][0-9][0-9]|[1-3][0-9][0-9][0-9]|4[0][0-9][0-6])'}),RestrictedClassType(base_type=unicode, restriction_dict={'pattern': u'([0-1])'}),], is_leaf=True, yang_name="source-interface-value", rest_name="source-interface-value", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'cli-full-command': None, u'cli-drop-node-name': None}}, namespace='urn:brocade.com:mgmt:brocade-aaa', defining_module='brocade-aaa', yang_type='union', is_config=True)

  source_interface_name = __builtin__.property(_get_source_interface_name, _set_source_interface_name)
  source_interface_value = __builtin__.property(_get_source_interface_value, _set_source_interface_value)


  _pyangbind_elements = {'source_interface_name': source_interface_name, 'source_interface_value': source_interface_value, }


