
from operator import attrgetter
import pyangbind.lib.xpathhelper as xpathhelper
from pyangbind.lib.yangtypes import RestrictedPrecisionDecimalType, RestrictedClassType, TypedListType
from pyangbind.lib.yangtypes import YANGBool, YANGListType, YANGDynClass, ReferenceType
from pyangbind.lib.base import PybindBase
from decimal import Decimal
from bitarray import bitarray
import __builtin__
class access_list(PybindBase):
  """
  This class was auto-generated by the PythonClass plugin for PYANG
  from YANG module brocade-common-def - based on the path /ip/hide-as-path-holder/as-path/access-list. Each member element of
  the container is represented as a class variable - with a specific
  YANG type.

  YANG Description: BGP AS Path Access List
  """
  __slots__ = ('_pybind_generated_by', '_path_helper', '_yang_name', '_rest_name', '_extmethods', '__name','__seq_keyword','__instance','__ip_action','__ip_reg_expr',)

  _yang_name = 'access-list'
  _rest_name = 'access-list'

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
    self.__instance = YANGDynClass(base=RestrictedClassType(base_type=RestrictedClassType(base_type=int, restriction_dict={'range': ['0..65535']},int_size=16), restriction_dict={'range': [u'1..65535']}), is_leaf=True, yang_name="instance", rest_name="instance", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'cli-full-no': None}}, is_keyval=True, namespace='urn:brocade.com:mgmt:brocade-ip-policy', defining_module='brocade-ip-policy', yang_type='instance-id-t', is_config=True)
    self.__seq_keyword = YANGDynClass(base=RestrictedClassType(base_type=unicode,                                     restriction_type="dict_key",                                     restriction_arg={u'seq': {'value': 1}},), is_leaf=True, yang_name="seq-keyword", rest_name="", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'cli-drop-node-name': None}}, is_keyval=True, namespace='urn:brocade.com:mgmt:brocade-ip-policy', defining_module='brocade-ip-policy', yang_type='enumeration', is_config=True)
    self.__name = YANGDynClass(base=RestrictedClassType(base_type=unicode, restriction_dict={'length': [u'1..32']}), is_leaf=True, yang_name="name", rest_name="", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'cli-drop-node-name': None}}, is_keyval=True, namespace='urn:brocade.com:mgmt:brocade-ip-policy', defining_module='brocade-ip-policy', yang_type='ip-as-path-name-t', is_config=True)
    self.__ip_reg_expr = YANGDynClass(base=unicode, is_leaf=True, yang_name="ip-reg-expr", rest_name="", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'cli-drop-node-name': None, u'cli-suppress-no': None}}, namespace='urn:brocade.com:mgmt:brocade-ip-policy', defining_module='brocade-ip-policy', yang_type='ip-as-path-reg-expr-t', is_config=True)
    self.__ip_action = YANGDynClass(base=RestrictedClassType(base_type=unicode,                                     restriction_type="dict_key",                                     restriction_arg={u'deny': {'value': 2}, u'permit': {'value': 1}},), is_leaf=True, yang_name="ip-action", rest_name="", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'cli-drop-node-name': None, u'cli-suppress-no': None, u'cli-incomplete-command': None}}, namespace='urn:brocade.com:mgmt:brocade-ip-policy', defining_module='brocade-ip-policy', yang_type='action-t', is_config=True)

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
      return [u'ip', u'hide-as-path-holder', u'as-path', u'access-list']

  def _rest_path(self):
    if hasattr(self, "_parent"):
      if self._rest_name:
        return self._parent._rest_path()+[self._rest_name]
      else:
        return self._parent._rest_path()
    else:
      return [u'ip', u'as-path', u'access-list']

  def _get_name(self):
    """
    Getter method for name, mapped from YANG variable /ip/hide_as_path_holder/as_path/access_list/name (ip-as-path-name-t)
    """
    return self.__name
      
  def _set_name(self, v, load=False):
    """
    Setter method for name, mapped from YANG variable /ip/hide_as_path_holder/as_path/access_list/name (ip-as-path-name-t)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_name is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_name() directly.
    """
    parent = getattr(self, "_parent", None)
    if parent is not None and load is False:
      raise AttributeError("Cannot set keys directly when" +
                             " within an instantiated list")

    if hasattr(v, "_utype"):
      v = v._utype(v)
    try:
      t = YANGDynClass(v,base=RestrictedClassType(base_type=unicode, restriction_dict={'length': [u'1..32']}), is_leaf=True, yang_name="name", rest_name="", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'cli-drop-node-name': None}}, is_keyval=True, namespace='urn:brocade.com:mgmt:brocade-ip-policy', defining_module='brocade-ip-policy', yang_type='ip-as-path-name-t', is_config=True)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """name must be of a type compatible with ip-as-path-name-t""",
          'defined-type': "brocade-ip-policy:ip-as-path-name-t",
          'generated-type': """YANGDynClass(base=RestrictedClassType(base_type=unicode, restriction_dict={'length': [u'1..32']}), is_leaf=True, yang_name="name", rest_name="", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'cli-drop-node-name': None}}, is_keyval=True, namespace='urn:brocade.com:mgmt:brocade-ip-policy', defining_module='brocade-ip-policy', yang_type='ip-as-path-name-t', is_config=True)""",
        })

    self.__name = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_name(self):
    self.__name = YANGDynClass(base=RestrictedClassType(base_type=unicode, restriction_dict={'length': [u'1..32']}), is_leaf=True, yang_name="name", rest_name="", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'cli-drop-node-name': None}}, is_keyval=True, namespace='urn:brocade.com:mgmt:brocade-ip-policy', defining_module='brocade-ip-policy', yang_type='ip-as-path-name-t', is_config=True)


  def _get_seq_keyword(self):
    """
    Getter method for seq_keyword, mapped from YANG variable /ip/hide_as_path_holder/as_path/access_list/seq_keyword (enumeration)
    """
    return self.__seq_keyword
      
  def _set_seq_keyword(self, v, load=False):
    """
    Setter method for seq_keyword, mapped from YANG variable /ip/hide_as_path_holder/as_path/access_list/seq_keyword (enumeration)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_seq_keyword is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_seq_keyword() directly.
    """
    parent = getattr(self, "_parent", None)
    if parent is not None and load is False:
      raise AttributeError("Cannot set keys directly when" +
                             " within an instantiated list")

    if hasattr(v, "_utype"):
      v = v._utype(v)
    try:
      t = YANGDynClass(v,base=RestrictedClassType(base_type=unicode,                                     restriction_type="dict_key",                                     restriction_arg={u'seq': {'value': 1}},), is_leaf=True, yang_name="seq-keyword", rest_name="", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'cli-drop-node-name': None}}, is_keyval=True, namespace='urn:brocade.com:mgmt:brocade-ip-policy', defining_module='brocade-ip-policy', yang_type='enumeration', is_config=True)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """seq_keyword must be of a type compatible with enumeration""",
          'defined-type': "brocade-ip-policy:enumeration",
          'generated-type': """YANGDynClass(base=RestrictedClassType(base_type=unicode,                                     restriction_type="dict_key",                                     restriction_arg={u'seq': {'value': 1}},), is_leaf=True, yang_name="seq-keyword", rest_name="", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'cli-drop-node-name': None}}, is_keyval=True, namespace='urn:brocade.com:mgmt:brocade-ip-policy', defining_module='brocade-ip-policy', yang_type='enumeration', is_config=True)""",
        })

    self.__seq_keyword = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_seq_keyword(self):
    self.__seq_keyword = YANGDynClass(base=RestrictedClassType(base_type=unicode,                                     restriction_type="dict_key",                                     restriction_arg={u'seq': {'value': 1}},), is_leaf=True, yang_name="seq-keyword", rest_name="", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'cli-drop-node-name': None}}, is_keyval=True, namespace='urn:brocade.com:mgmt:brocade-ip-policy', defining_module='brocade-ip-policy', yang_type='enumeration', is_config=True)


  def _get_instance(self):
    """
    Getter method for instance, mapped from YANG variable /ip/hide_as_path_holder/as_path/access_list/instance (instance-id-t)
    """
    return self.__instance
      
  def _set_instance(self, v, load=False):
    """
    Setter method for instance, mapped from YANG variable /ip/hide_as_path_holder/as_path/access_list/instance (instance-id-t)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_instance is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_instance() directly.
    """
    parent = getattr(self, "_parent", None)
    if parent is not None and load is False:
      raise AttributeError("Cannot set keys directly when" +
                             " within an instantiated list")

    if hasattr(v, "_utype"):
      v = v._utype(v)
    try:
      t = YANGDynClass(v,base=RestrictedClassType(base_type=RestrictedClassType(base_type=int, restriction_dict={'range': ['0..65535']},int_size=16), restriction_dict={'range': [u'1..65535']}), is_leaf=True, yang_name="instance", rest_name="instance", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'cli-full-no': None}}, is_keyval=True, namespace='urn:brocade.com:mgmt:brocade-ip-policy', defining_module='brocade-ip-policy', yang_type='instance-id-t', is_config=True)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """instance must be of a type compatible with instance-id-t""",
          'defined-type': "brocade-ip-policy:instance-id-t",
          'generated-type': """YANGDynClass(base=RestrictedClassType(base_type=RestrictedClassType(base_type=int, restriction_dict={'range': ['0..65535']},int_size=16), restriction_dict={'range': [u'1..65535']}), is_leaf=True, yang_name="instance", rest_name="instance", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'cli-full-no': None}}, is_keyval=True, namespace='urn:brocade.com:mgmt:brocade-ip-policy', defining_module='brocade-ip-policy', yang_type='instance-id-t', is_config=True)""",
        })

    self.__instance = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_instance(self):
    self.__instance = YANGDynClass(base=RestrictedClassType(base_type=RestrictedClassType(base_type=int, restriction_dict={'range': ['0..65535']},int_size=16), restriction_dict={'range': [u'1..65535']}), is_leaf=True, yang_name="instance", rest_name="instance", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'cli-full-no': None}}, is_keyval=True, namespace='urn:brocade.com:mgmt:brocade-ip-policy', defining_module='brocade-ip-policy', yang_type='instance-id-t', is_config=True)


  def _get_ip_action(self):
    """
    Getter method for ip_action, mapped from YANG variable /ip/hide_as_path_holder/as_path/access_list/ip_action (action-t)
    """
    return self.__ip_action
      
  def _set_ip_action(self, v, load=False):
    """
    Setter method for ip_action, mapped from YANG variable /ip/hide_as_path_holder/as_path/access_list/ip_action (action-t)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_ip_action is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_ip_action() directly.
    """
    if hasattr(v, "_utype"):
      v = v._utype(v)
    try:
      t = YANGDynClass(v,base=RestrictedClassType(base_type=unicode,                                     restriction_type="dict_key",                                     restriction_arg={u'deny': {'value': 2}, u'permit': {'value': 1}},), is_leaf=True, yang_name="ip-action", rest_name="", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'cli-drop-node-name': None, u'cli-suppress-no': None, u'cli-incomplete-command': None}}, namespace='urn:brocade.com:mgmt:brocade-ip-policy', defining_module='brocade-ip-policy', yang_type='action-t', is_config=True)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """ip_action must be of a type compatible with action-t""",
          'defined-type': "brocade-ip-policy:action-t",
          'generated-type': """YANGDynClass(base=RestrictedClassType(base_type=unicode,                                     restriction_type="dict_key",                                     restriction_arg={u'deny': {'value': 2}, u'permit': {'value': 1}},), is_leaf=True, yang_name="ip-action", rest_name="", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'cli-drop-node-name': None, u'cli-suppress-no': None, u'cli-incomplete-command': None}}, namespace='urn:brocade.com:mgmt:brocade-ip-policy', defining_module='brocade-ip-policy', yang_type='action-t', is_config=True)""",
        })

    self.__ip_action = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_ip_action(self):
    self.__ip_action = YANGDynClass(base=RestrictedClassType(base_type=unicode,                                     restriction_type="dict_key",                                     restriction_arg={u'deny': {'value': 2}, u'permit': {'value': 1}},), is_leaf=True, yang_name="ip-action", rest_name="", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'cli-drop-node-name': None, u'cli-suppress-no': None, u'cli-incomplete-command': None}}, namespace='urn:brocade.com:mgmt:brocade-ip-policy', defining_module='brocade-ip-policy', yang_type='action-t', is_config=True)


  def _get_ip_reg_expr(self):
    """
    Getter method for ip_reg_expr, mapped from YANG variable /ip/hide_as_path_holder/as_path/access_list/ip_reg_expr (ip-as-path-reg-expr-t)
    """
    return self.__ip_reg_expr
      
  def _set_ip_reg_expr(self, v, load=False):
    """
    Setter method for ip_reg_expr, mapped from YANG variable /ip/hide_as_path_holder/as_path/access_list/ip_reg_expr (ip-as-path-reg-expr-t)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_ip_reg_expr is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_ip_reg_expr() directly.
    """
    if hasattr(v, "_utype"):
      v = v._utype(v)
    try:
      t = YANGDynClass(v,base=unicode, is_leaf=True, yang_name="ip-reg-expr", rest_name="", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'cli-drop-node-name': None, u'cli-suppress-no': None}}, namespace='urn:brocade.com:mgmt:brocade-ip-policy', defining_module='brocade-ip-policy', yang_type='ip-as-path-reg-expr-t', is_config=True)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """ip_reg_expr must be of a type compatible with ip-as-path-reg-expr-t""",
          'defined-type': "brocade-ip-policy:ip-as-path-reg-expr-t",
          'generated-type': """YANGDynClass(base=unicode, is_leaf=True, yang_name="ip-reg-expr", rest_name="", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'cli-drop-node-name': None, u'cli-suppress-no': None}}, namespace='urn:brocade.com:mgmt:brocade-ip-policy', defining_module='brocade-ip-policy', yang_type='ip-as-path-reg-expr-t', is_config=True)""",
        })

    self.__ip_reg_expr = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_ip_reg_expr(self):
    self.__ip_reg_expr = YANGDynClass(base=unicode, is_leaf=True, yang_name="ip-reg-expr", rest_name="", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'cli-drop-node-name': None, u'cli-suppress-no': None}}, namespace='urn:brocade.com:mgmt:brocade-ip-policy', defining_module='brocade-ip-policy', yang_type='ip-as-path-reg-expr-t', is_config=True)

  name = __builtin__.property(_get_name, _set_name)
  seq_keyword = __builtin__.property(_get_seq_keyword, _set_seq_keyword)
  instance = __builtin__.property(_get_instance, _set_instance)
  ip_action = __builtin__.property(_get_ip_action, _set_ip_action)
  ip_reg_expr = __builtin__.property(_get_ip_reg_expr, _set_ip_reg_expr)


  _pyangbind_elements = {'name': name, 'seq_keyword': seq_keyword, 'instance': instance, 'ip_action': ip_action, 'ip_reg_expr': ip_reg_expr, }


