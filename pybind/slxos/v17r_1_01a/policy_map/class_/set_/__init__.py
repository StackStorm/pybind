
from operator import attrgetter
import pyangbind.lib.xpathhelper as xpathhelper
from pyangbind.lib.yangtypes import RestrictedPrecisionDecimalType, RestrictedClassType, TypedListType
from pyangbind.lib.yangtypes import YANGBool, YANGListType, YANGDynClass, ReferenceType
from pyangbind.lib.base import PybindBase
from decimal import Decimal
from bitarray import bitarray
import __builtin__
import set_cos_tc
import set_dscp
class set_(PybindBase):
  """
  This class was auto-generated by the PythonClass plugin for PYANG
  from YANG module brocade-qos-mqc - based on the path /policy-map/class/set. Each member element of
  the container is represented as a class variable - with a specific
  YANG type.
  """
  __slots__ = ('_pybind_generated_by', '_path_helper', '_yang_name', '_rest_name', '_extmethods', '__set_cos_tc','__set_dscp',)

  _yang_name = 'set'
  _rest_name = 'set'

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
    self.__set_dscp = YANGDynClass(base=set_dscp.set_dscp, is_container='container', presence=False, yang_name="set_dscp", rest_name="", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'info': u'Differentiated Services Code Point', u'cli-drop-node-name': None}}, namespace='urn:brocade.com:mgmt:brocade-qos-mqc', defining_module='brocade-qos-mqc', yang_type='container', is_config=True)
    self.__set_cos_tc = YANGDynClass(base=set_cos_tc.set_cos_tc, is_container='container', presence=False, yang_name="set_cos_tc", rest_name="", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'cli-compact-syntax': None, u'cli-drop-node-name': None, u'cli-sequence-commands': None, u'info': u'Class of Service'}}, namespace='urn:brocade.com:mgmt:brocade-qos-mqc', defining_module='brocade-qos-mqc', yang_type='container', is_config=True)

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
      return [u'policy-map', u'class', u'set']

  def _rest_path(self):
    if hasattr(self, "_parent"):
      if self._rest_name:
        return self._parent._rest_path()+[self._rest_name]
      else:
        return self._parent._rest_path()
    else:
      return [u'policy-map', u'class', u'set']

  def _get_set_cos_tc(self):
    """
    Getter method for set_cos_tc, mapped from YANG variable /policy_map/class/set/set_cos_tc (container)
    """
    return self.__set_cos_tc
      
  def _set_set_cos_tc(self, v, load=False):
    """
    Setter method for set_cos_tc, mapped from YANG variable /policy_map/class/set/set_cos_tc (container)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_set_cos_tc is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_set_cos_tc() directly.
    """
    if hasattr(v, "_utype"):
      v = v._utype(v)
    try:
      t = YANGDynClass(v,base=set_cos_tc.set_cos_tc, is_container='container', presence=False, yang_name="set_cos_tc", rest_name="", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'cli-compact-syntax': None, u'cli-drop-node-name': None, u'cli-sequence-commands': None, u'info': u'Class of Service'}}, namespace='urn:brocade.com:mgmt:brocade-qos-mqc', defining_module='brocade-qos-mqc', yang_type='container', is_config=True)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """set_cos_tc must be of a type compatible with container""",
          'defined-type': "container",
          'generated-type': """YANGDynClass(base=set_cos_tc.set_cos_tc, is_container='container', presence=False, yang_name="set_cos_tc", rest_name="", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'cli-compact-syntax': None, u'cli-drop-node-name': None, u'cli-sequence-commands': None, u'info': u'Class of Service'}}, namespace='urn:brocade.com:mgmt:brocade-qos-mqc', defining_module='brocade-qos-mqc', yang_type='container', is_config=True)""",
        })

    self.__set_cos_tc = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_set_cos_tc(self):
    self.__set_cos_tc = YANGDynClass(base=set_cos_tc.set_cos_tc, is_container='container', presence=False, yang_name="set_cos_tc", rest_name="", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'cli-compact-syntax': None, u'cli-drop-node-name': None, u'cli-sequence-commands': None, u'info': u'Class of Service'}}, namespace='urn:brocade.com:mgmt:brocade-qos-mqc', defining_module='brocade-qos-mqc', yang_type='container', is_config=True)


  def _get_set_dscp(self):
    """
    Getter method for set_dscp, mapped from YANG variable /policy_map/class/set/set_dscp (container)
    """
    return self.__set_dscp
      
  def _set_set_dscp(self, v, load=False):
    """
    Setter method for set_dscp, mapped from YANG variable /policy_map/class/set/set_dscp (container)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_set_dscp is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_set_dscp() directly.
    """
    if hasattr(v, "_utype"):
      v = v._utype(v)
    try:
      t = YANGDynClass(v,base=set_dscp.set_dscp, is_container='container', presence=False, yang_name="set_dscp", rest_name="", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'info': u'Differentiated Services Code Point', u'cli-drop-node-name': None}}, namespace='urn:brocade.com:mgmt:brocade-qos-mqc', defining_module='brocade-qos-mqc', yang_type='container', is_config=True)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """set_dscp must be of a type compatible with container""",
          'defined-type': "container",
          'generated-type': """YANGDynClass(base=set_dscp.set_dscp, is_container='container', presence=False, yang_name="set_dscp", rest_name="", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'info': u'Differentiated Services Code Point', u'cli-drop-node-name': None}}, namespace='urn:brocade.com:mgmt:brocade-qos-mqc', defining_module='brocade-qos-mqc', yang_type='container', is_config=True)""",
        })

    self.__set_dscp = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_set_dscp(self):
    self.__set_dscp = YANGDynClass(base=set_dscp.set_dscp, is_container='container', presence=False, yang_name="set_dscp", rest_name="", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'info': u'Differentiated Services Code Point', u'cli-drop-node-name': None}}, namespace='urn:brocade.com:mgmt:brocade-qos-mqc', defining_module='brocade-qos-mqc', yang_type='container', is_config=True)

  set_cos_tc = __builtin__.property(_get_set_cos_tc, _set_set_cos_tc)
  set_dscp = __builtin__.property(_get_set_dscp, _set_set_dscp)


  _pyangbind_elements = {'set_cos_tc': set_cos_tc, 'set_dscp': set_dscp, }


