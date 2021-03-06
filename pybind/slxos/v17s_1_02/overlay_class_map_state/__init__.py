
from operator import attrgetter
import pyangbind.lib.xpathhelper as xpathhelper
from pyangbind.lib.yangtypes import RestrictedPrecisionDecimalType, RestrictedClassType, TypedListType
from pyangbind.lib.yangtypes import YANGBool, YANGListType, YANGDynClass, ReferenceType
from pyangbind.lib.base import PybindBase
from decimal import Decimal
from bitarray import bitarray
import __builtin__
import rules
import policies
class overlay_class_map_state(PybindBase):
  """
  This class was auto-generated by the PythonClass plugin for PYANG
  from YANG module brocade-ssm-operational - based on the path /overlay-class-map-state. Each member element of
  the container is represented as a class variable - with a specific
  YANG type.

  YANG Description: Overlay Class Map
  """
  __slots__ = ('_pybind_generated_by', '_path_helper', '_yang_name', '_rest_name', '_extmethods', '__class_map_name','__rules','__policies',)

  _yang_name = 'overlay-class-map-state'
  _rest_name = 'overlay-class-map-state'

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
    self.__rules = YANGDynClass(base=YANGListType("seq_id",rules.rules, yang_name="rules", rest_name="rules", parent=self, is_container='list', user_ordered=False, path_helper=self._path_helper, yang_keys='seq-id', extensions={u'tailf-common': {u'callpoint': u'ssm-overlay-class-map-rule', u'cli-suppress-show-path': None}}), is_container='list', yang_name="rules", rest_name="rules", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'callpoint': u'ssm-overlay-class-map-rule', u'cli-suppress-show-path': None}}, namespace='urn:brocade.com:mgmt:brocade-ssm-operational', defining_module='brocade-ssm-operational', yang_type='list', is_config=False)
    self.__class_map_name = YANGDynClass(base=unicode, is_leaf=True, yang_name="class-map-name", rest_name="class-map-name", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, is_keyval=True, namespace='urn:brocade.com:mgmt:brocade-ssm-operational', defining_module='brocade-ssm-operational', yang_type='string', is_config=False)
    self.__policies = YANGDynClass(base=YANGListType("seq_id",policies.policies, yang_name="policies", rest_name="policies", parent=self, is_container='list', user_ordered=False, path_helper=self._path_helper, yang_keys='seq-id', extensions={u'tailf-common': {u'callpoint': u'ssm-overlay-class-map-policy-ref', u'cli-suppress-show-path': None}}), is_container='list', yang_name="policies", rest_name="policies", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'callpoint': u'ssm-overlay-class-map-policy-ref', u'cli-suppress-show-path': None}}, namespace='urn:brocade.com:mgmt:brocade-ssm-operational', defining_module='brocade-ssm-operational', yang_type='list', is_config=False)

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
      return [u'overlay-class-map-state']

  def _rest_path(self):
    if hasattr(self, "_parent"):
      if self._rest_name:
        return self._parent._rest_path()+[self._rest_name]
      else:
        return self._parent._rest_path()
    else:
      return [u'overlay-class-map-state']

  def _get_class_map_name(self):
    """
    Getter method for class_map_name, mapped from YANG variable /overlay_class_map_state/class_map_name (string)

    YANG Description: Overlay Policy Map name
    """
    return self.__class_map_name
      
  def _set_class_map_name(self, v, load=False):
    """
    Setter method for class_map_name, mapped from YANG variable /overlay_class_map_state/class_map_name (string)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_class_map_name is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_class_map_name() directly.

    YANG Description: Overlay Policy Map name
    """
    parent = getattr(self, "_parent", None)
    if parent is not None and load is False:
      raise AttributeError("Cannot set keys directly when" +
                             " within an instantiated list")

    if hasattr(v, "_utype"):
      v = v._utype(v)
    try:
      t = YANGDynClass(v,base=unicode, is_leaf=True, yang_name="class-map-name", rest_name="class-map-name", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, is_keyval=True, namespace='urn:brocade.com:mgmt:brocade-ssm-operational', defining_module='brocade-ssm-operational', yang_type='string', is_config=False)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """class_map_name must be of a type compatible with string""",
          'defined-type': "string",
          'generated-type': """YANGDynClass(base=unicode, is_leaf=True, yang_name="class-map-name", rest_name="class-map-name", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, is_keyval=True, namespace='urn:brocade.com:mgmt:brocade-ssm-operational', defining_module='brocade-ssm-operational', yang_type='string', is_config=False)""",
        })

    self.__class_map_name = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_class_map_name(self):
    self.__class_map_name = YANGDynClass(base=unicode, is_leaf=True, yang_name="class-map-name", rest_name="class-map-name", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, is_keyval=True, namespace='urn:brocade.com:mgmt:brocade-ssm-operational', defining_module='brocade-ssm-operational', yang_type='string', is_config=False)


  def _get_rules(self):
    """
    Getter method for rules, mapped from YANG variable /overlay_class_map_state/rules (list)

    YANG Description: Overlay Class Map Rule
    """
    return self.__rules
      
  def _set_rules(self, v, load=False):
    """
    Setter method for rules, mapped from YANG variable /overlay_class_map_state/rules (list)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_rules is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_rules() directly.

    YANG Description: Overlay Class Map Rule
    """
    if hasattr(v, "_utype"):
      v = v._utype(v)
    try:
      t = YANGDynClass(v,base=YANGListType("seq_id",rules.rules, yang_name="rules", rest_name="rules", parent=self, is_container='list', user_ordered=False, path_helper=self._path_helper, yang_keys='seq-id', extensions={u'tailf-common': {u'callpoint': u'ssm-overlay-class-map-rule', u'cli-suppress-show-path': None}}), is_container='list', yang_name="rules", rest_name="rules", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'callpoint': u'ssm-overlay-class-map-rule', u'cli-suppress-show-path': None}}, namespace='urn:brocade.com:mgmt:brocade-ssm-operational', defining_module='brocade-ssm-operational', yang_type='list', is_config=False)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """rules must be of a type compatible with list""",
          'defined-type': "list",
          'generated-type': """YANGDynClass(base=YANGListType("seq_id",rules.rules, yang_name="rules", rest_name="rules", parent=self, is_container='list', user_ordered=False, path_helper=self._path_helper, yang_keys='seq-id', extensions={u'tailf-common': {u'callpoint': u'ssm-overlay-class-map-rule', u'cli-suppress-show-path': None}}), is_container='list', yang_name="rules", rest_name="rules", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'callpoint': u'ssm-overlay-class-map-rule', u'cli-suppress-show-path': None}}, namespace='urn:brocade.com:mgmt:brocade-ssm-operational', defining_module='brocade-ssm-operational', yang_type='list', is_config=False)""",
        })

    self.__rules = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_rules(self):
    self.__rules = YANGDynClass(base=YANGListType("seq_id",rules.rules, yang_name="rules", rest_name="rules", parent=self, is_container='list', user_ordered=False, path_helper=self._path_helper, yang_keys='seq-id', extensions={u'tailf-common': {u'callpoint': u'ssm-overlay-class-map-rule', u'cli-suppress-show-path': None}}), is_container='list', yang_name="rules", rest_name="rules", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'callpoint': u'ssm-overlay-class-map-rule', u'cli-suppress-show-path': None}}, namespace='urn:brocade.com:mgmt:brocade-ssm-operational', defining_module='brocade-ssm-operational', yang_type='list', is_config=False)


  def _get_policies(self):
    """
    Getter method for policies, mapped from YANG variable /overlay_class_map_state/policies (list)

    YANG Description: Overlay Class Map Policy References
    """
    return self.__policies
      
  def _set_policies(self, v, load=False):
    """
    Setter method for policies, mapped from YANG variable /overlay_class_map_state/policies (list)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_policies is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_policies() directly.

    YANG Description: Overlay Class Map Policy References
    """
    if hasattr(v, "_utype"):
      v = v._utype(v)
    try:
      t = YANGDynClass(v,base=YANGListType("seq_id",policies.policies, yang_name="policies", rest_name="policies", parent=self, is_container='list', user_ordered=False, path_helper=self._path_helper, yang_keys='seq-id', extensions={u'tailf-common': {u'callpoint': u'ssm-overlay-class-map-policy-ref', u'cli-suppress-show-path': None}}), is_container='list', yang_name="policies", rest_name="policies", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'callpoint': u'ssm-overlay-class-map-policy-ref', u'cli-suppress-show-path': None}}, namespace='urn:brocade.com:mgmt:brocade-ssm-operational', defining_module='brocade-ssm-operational', yang_type='list', is_config=False)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """policies must be of a type compatible with list""",
          'defined-type': "list",
          'generated-type': """YANGDynClass(base=YANGListType("seq_id",policies.policies, yang_name="policies", rest_name="policies", parent=self, is_container='list', user_ordered=False, path_helper=self._path_helper, yang_keys='seq-id', extensions={u'tailf-common': {u'callpoint': u'ssm-overlay-class-map-policy-ref', u'cli-suppress-show-path': None}}), is_container='list', yang_name="policies", rest_name="policies", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'callpoint': u'ssm-overlay-class-map-policy-ref', u'cli-suppress-show-path': None}}, namespace='urn:brocade.com:mgmt:brocade-ssm-operational', defining_module='brocade-ssm-operational', yang_type='list', is_config=False)""",
        })

    self.__policies = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_policies(self):
    self.__policies = YANGDynClass(base=YANGListType("seq_id",policies.policies, yang_name="policies", rest_name="policies", parent=self, is_container='list', user_ordered=False, path_helper=self._path_helper, yang_keys='seq-id', extensions={u'tailf-common': {u'callpoint': u'ssm-overlay-class-map-policy-ref', u'cli-suppress-show-path': None}}), is_container='list', yang_name="policies", rest_name="policies", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'callpoint': u'ssm-overlay-class-map-policy-ref', u'cli-suppress-show-path': None}}, namespace='urn:brocade.com:mgmt:brocade-ssm-operational', defining_module='brocade-ssm-operational', yang_type='list', is_config=False)

  class_map_name = __builtin__.property(_get_class_map_name)
  rules = __builtin__.property(_get_rules)
  policies = __builtin__.property(_get_policies)


  _pyangbind_elements = {'class_map_name': class_map_name, 'rules': rules, 'policies': policies, }


