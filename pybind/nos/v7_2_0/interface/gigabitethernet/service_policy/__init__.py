
from operator import attrgetter
import pyangbind.lib.xpathhelper as xpathhelper
from pyangbind.lib.yangtypes import RestrictedPrecisionDecimalType, RestrictedClassType, TypedListType
from pyangbind.lib.yangtypes import YANGBool, YANGListType, YANGDynClass, ReferenceType
from pyangbind.lib.base import PybindBase
from decimal import Decimal
from bitarray import bitarray
import __builtin__
class service_policy(PybindBase):
  """
  This class was auto-generated by the PythonClass plugin for PYANG
  from YANG module brocade-interface - based on the path /interface/gigabitethernet/service-policy. Each member element of
  the container is represented as a class variable - with a specific
  YANG type.
  """
  __slots__ = ('_pybind_generated_by', '_path_helper', '_yang_name', '_rest_name', '_extmethods', '__in_','__out',)

  _yang_name = 'service-policy'
  _rest_name = 'service-policy'

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
    self.__in_ = YANGDynClass(base=RestrictedClassType(base_type=unicode, restriction_dict={'pattern': u'[a-zA-Z]{1}([-a-zA-Z0-9_]{0,63})'}), is_leaf=True, yang_name="in", rest_name="in", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'cli-full-command': None, u'info': u'Input Policy Map', u'cli-full-no': None}}, namespace='urn:brocade.com:mgmt:brocade-policer', defining_module='brocade-policer', yang_type='map-name-type', is_config=True)
    self.__out = YANGDynClass(base=RestrictedClassType(base_type=unicode, restriction_dict={'pattern': u'[a-zA-Z]{1}([-a-zA-Z0-9_]{0,63})'}), is_leaf=True, yang_name="out", rest_name="out", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'cli-full-command': None, u'info': u'Output Policy Map', u'cli-full-no': None}}, namespace='urn:brocade.com:mgmt:brocade-policer', defining_module='brocade-policer', yang_type='map-name-type', is_config=True)

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
      return [u'interface', u'gigabitethernet', u'service-policy']

  def _rest_path(self):
    if hasattr(self, "_parent"):
      if self._rest_name:
        return self._parent._rest_path()+[self._rest_name]
      else:
        return self._parent._rest_path()
    else:
      return [u'interface', u'GigabitEthernet', u'service-policy']

  def _get_in_(self):
    """
    Getter method for in_, mapped from YANG variable /interface/gigabitethernet/service_policy/in (map-name-type)
    """
    return self.__in_
      
  def _set_in_(self, v, load=False):
    """
    Setter method for in_, mapped from YANG variable /interface/gigabitethernet/service_policy/in (map-name-type)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_in_ is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_in_() directly.
    """
    if hasattr(v, "_utype"):
      v = v._utype(v)
    try:
      t = YANGDynClass(v,base=RestrictedClassType(base_type=unicode, restriction_dict={'pattern': u'[a-zA-Z]{1}([-a-zA-Z0-9_]{0,63})'}), is_leaf=True, yang_name="in", rest_name="in", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'cli-full-command': None, u'info': u'Input Policy Map', u'cli-full-no': None}}, namespace='urn:brocade.com:mgmt:brocade-policer', defining_module='brocade-policer', yang_type='map-name-type', is_config=True)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """in_ must be of a type compatible with map-name-type""",
          'defined-type': "brocade-policer:map-name-type",
          'generated-type': """YANGDynClass(base=RestrictedClassType(base_type=unicode, restriction_dict={'pattern': u'[a-zA-Z]{1}([-a-zA-Z0-9_]{0,63})'}), is_leaf=True, yang_name="in", rest_name="in", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'cli-full-command': None, u'info': u'Input Policy Map', u'cli-full-no': None}}, namespace='urn:brocade.com:mgmt:brocade-policer', defining_module='brocade-policer', yang_type='map-name-type', is_config=True)""",
        })

    self.__in_ = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_in_(self):
    self.__in_ = YANGDynClass(base=RestrictedClassType(base_type=unicode, restriction_dict={'pattern': u'[a-zA-Z]{1}([-a-zA-Z0-9_]{0,63})'}), is_leaf=True, yang_name="in", rest_name="in", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'cli-full-command': None, u'info': u'Input Policy Map', u'cli-full-no': None}}, namespace='urn:brocade.com:mgmt:brocade-policer', defining_module='brocade-policer', yang_type='map-name-type', is_config=True)


  def _get_out(self):
    """
    Getter method for out, mapped from YANG variable /interface/gigabitethernet/service_policy/out (map-name-type)
    """
    return self.__out
      
  def _set_out(self, v, load=False):
    """
    Setter method for out, mapped from YANG variable /interface/gigabitethernet/service_policy/out (map-name-type)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_out is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_out() directly.
    """
    if hasattr(v, "_utype"):
      v = v._utype(v)
    try:
      t = YANGDynClass(v,base=RestrictedClassType(base_type=unicode, restriction_dict={'pattern': u'[a-zA-Z]{1}([-a-zA-Z0-9_]{0,63})'}), is_leaf=True, yang_name="out", rest_name="out", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'cli-full-command': None, u'info': u'Output Policy Map', u'cli-full-no': None}}, namespace='urn:brocade.com:mgmt:brocade-policer', defining_module='brocade-policer', yang_type='map-name-type', is_config=True)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """out must be of a type compatible with map-name-type""",
          'defined-type': "brocade-policer:map-name-type",
          'generated-type': """YANGDynClass(base=RestrictedClassType(base_type=unicode, restriction_dict={'pattern': u'[a-zA-Z]{1}([-a-zA-Z0-9_]{0,63})'}), is_leaf=True, yang_name="out", rest_name="out", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'cli-full-command': None, u'info': u'Output Policy Map', u'cli-full-no': None}}, namespace='urn:brocade.com:mgmt:brocade-policer', defining_module='brocade-policer', yang_type='map-name-type', is_config=True)""",
        })

    self.__out = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_out(self):
    self.__out = YANGDynClass(base=RestrictedClassType(base_type=unicode, restriction_dict={'pattern': u'[a-zA-Z]{1}([-a-zA-Z0-9_]{0,63})'}), is_leaf=True, yang_name="out", rest_name="out", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'cli-full-command': None, u'info': u'Output Policy Map', u'cli-full-no': None}}, namespace='urn:brocade.com:mgmt:brocade-policer', defining_module='brocade-policer', yang_type='map-name-type', is_config=True)

  in_ = __builtin__.property(_get_in_, _set_in_)
  out = __builtin__.property(_get_out, _set_out)


  _pyangbind_elements = {'in_': in_, 'out': out, }


