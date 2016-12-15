
from operator import attrgetter
import pyangbind.lib.xpathhelper as xpathhelper
from pyangbind.lib.yangtypes import RestrictedPrecisionDecimalType, RestrictedClassType, TypedListType
from pyangbind.lib.yangtypes import YANGBool, YANGListType, YANGDynClass, ReferenceType
from pyangbind.lib.base import PybindBase
from decimal import Decimal
from bitarray import bitarray
import __builtin__
class extcommunity_list(PybindBase):
  """
  This class was auto-generated by the PythonClass plugin for PYANG
  from YANG module brocade-rbridge - based on the path /rbridge-id/ip/extcommunity-list. Each member element of
  the container is represented as a class variable - with a specific
  YANG type.
  """
  __slots__ = ('_pybind_generated_by', '_path_helper', '_yang_name', '_rest_name', '_extmethods', '__extcommunity_list_num','__ext_community_action','__ext_community_expr',)

  _yang_name = 'extcommunity-list'
  _rest_name = 'extcommunity-list'

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
    self.__ext_community_action = YANGDynClass(base=RestrictedClassType(base_type=unicode,                                     restriction_type="dict_key",                                     restriction_arg={u'deny': {'value': 2}, u'permit': {'value': 1}},), is_leaf=True, yang_name="ext-community-action", rest_name="", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'cli-drop-node-name': None, u'cli-incomplete-command': None, u'cli-suppress-no': None}}, namespace='urn:brocade.com:mgmt:brocade-ip-policy', defining_module='brocade-ip-policy', yang_type='action-t', is_config=True)
    self.__ext_community_expr = YANGDynClass(base=RestrictedClassType(base_type=unicode, restriction_dict={'pattern': u'(\\s*)|(\\s*((rt)|(soo)|((([1-9][0-9]{0,8})|([1-3][0-9]{9})|(4[0-1][0-9]{8})|(42[0-8][0-9]{7})|(429[0-3][0-9]{6})|(4294[0-8][0-9]{5})|(42949[0-5][0-9]{4})|(429496[0-6][0-9]{3})|(4294967[0-1][0-9]{2})|(42949672[0-8][0-9])|(429496729[0-5])):(([1-9][0-9]{0,8})|([1-3][0-9]{9})|(4[0-1][0-9]{8})|(42[0-8][0-9]{7})|(429[0-3][0-9]{6})|(4294[0-8][0-9]{5})|(42949[0-5][0-9]{4})|(429496[0-6][0-9]{3})|(4294967[0-1][0-9]{2})|(42949672[0-8][0-9])|(429496729[0-5])))|((([0-9]|[1-9][0-9]|1[0-9]{2}|2[0-4][0-9]|25[0-5])\\.){3}([0-9]|[1-9][0-9]|1[0-9]{2}|2[0-4][0-9]|25[0-5]):(([1-9][0-9]{0,8})|([1-3][0-9]{9})|(4[0-1][0-9]{8})|(42[0-8][0-9]{7})|(429[0-3][0-9]{6})|(4294[0-8][0-9]{5})|(42949[0-5][0-9]{4})|(429496[0-6][0-9]{3})|(4294967[0-1][0-9]{2})|(42949672[0-8][0-9])|(429496729[0-5])))))((\\s+((rt)|(soo)|((([1-9][0-9]{0,8})|([1-3][0-9]{9})|(4[0-1][0-9]{8})|(42[0-8][0-9]{7})|(429[0-3][0-9]{6})|(4294[0-8][0-9]{5})|(42949[0-5][0-9]{4})|(429496[0-6][0-9]{3})|(4294967[0-1][0-9]{2})|(42949672[0-8][0-9])|(429496729[0-5])):(([1-9][0-9]{0,8})|([1-3][0-9]{9})|(4[0-1][0-9]{8})|(42[0-8][0-9]{7})|(429[0-3][0-9]{6})|(4294[0-8][0-9]{5})|(42949[0-5][0-9]{4})|(429496[0-6][0-9]{3})|(4294967[0-1][0-9]{2})|(42949672[0-8][0-9])|(429496729[0-5])))|(((([0-9]|[1-9][0-9]|1[0-9]{2}|2[0-4][0-9]|25[0-5])\\.){3}([0-9]|[1-9][0-9]|1[0-9]{2}|2[0-4][0-9]|25[0-5])):(([1-9][0-9]{0,8})|([1-3][0-9]{9})|(4[0-1][0-9]{8})|(42[0-8][0-9]{7})|(429[0-3][0-9]{6})|(4294[0-8][0-9]{5})|(42949[0-5][0-9]{4})|(429496[0-6][0-9]{3})|(4294967[0-1][0-9]{2})|(42949672[0-8][0-9])|(429496729[0-5])))))*)'}), is_leaf=True, yang_name="ext-community-expr", rest_name="", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'info': u'Ext-community-list', u'cli-multi-value': None, u'cli-suppress-no': None, u'cli-break-sequence-commands': None, u'cli-drop-node-name': None, u'cli-full-command': None, u'cli-completion-actionpoint': u'ip-ext-community-list-action-point'}}, namespace='urn:brocade.com:mgmt:brocade-ip-policy', defining_module='brocade-ip-policy', yang_type='extcommunity-list-expr-t', is_config=True)
    self.__extcommunity_list_num = YANGDynClass(base=RestrictedClassType(base_type=RestrictedClassType(base_type=int, restriction_dict={'range': ['0..65535']},int_size=16), restriction_dict={'range': [u'0..99']}), is_leaf=True, yang_name="extcommunity-list-num", rest_name="", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'cli-drop-node-name': None, u'cli-full-no': None}}, is_keyval=True, namespace='urn:brocade.com:mgmt:brocade-ip-policy', defining_module='brocade-ip-policy', yang_type='extcommunitylist-instance', is_config=True)

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
      return [u'rbridge-id', u'ip', u'extcommunity-list']

  def _rest_path(self):
    if hasattr(self, "_parent"):
      if self._rest_name:
        return self._parent._rest_path()+[self._rest_name]
      else:
        return self._parent._rest_path()
    else:
      return [u'rbridge-id', u'ip', u'extcommunity-list']

  def _get_extcommunity_list_num(self):
    """
    Getter method for extcommunity_list_num, mapped from YANG variable /rbridge_id/ip/extcommunity_list/extcommunity_list_num (extcommunitylist-instance)
    """
    return self.__extcommunity_list_num
      
  def _set_extcommunity_list_num(self, v, load=False):
    """
    Setter method for extcommunity_list_num, mapped from YANG variable /rbridge_id/ip/extcommunity_list/extcommunity_list_num (extcommunitylist-instance)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_extcommunity_list_num is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_extcommunity_list_num() directly.
    """
    parent = getattr(self, "_parent", None)
    if parent is not None and load is False:
      raise AttributeError("Cannot set keys directly when" +
                             " within an instantiated list")

    if hasattr(v, "_utype"):
      v = v._utype(v)
    try:
      t = YANGDynClass(v,base=RestrictedClassType(base_type=RestrictedClassType(base_type=int, restriction_dict={'range': ['0..65535']},int_size=16), restriction_dict={'range': [u'0..99']}), is_leaf=True, yang_name="extcommunity-list-num", rest_name="", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'cli-drop-node-name': None, u'cli-full-no': None}}, is_keyval=True, namespace='urn:brocade.com:mgmt:brocade-ip-policy', defining_module='brocade-ip-policy', yang_type='extcommunitylist-instance', is_config=True)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """extcommunity_list_num must be of a type compatible with extcommunitylist-instance""",
          'defined-type': "brocade-ip-policy:extcommunitylist-instance",
          'generated-type': """YANGDynClass(base=RestrictedClassType(base_type=RestrictedClassType(base_type=int, restriction_dict={'range': ['0..65535']},int_size=16), restriction_dict={'range': [u'0..99']}), is_leaf=True, yang_name="extcommunity-list-num", rest_name="", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'cli-drop-node-name': None, u'cli-full-no': None}}, is_keyval=True, namespace='urn:brocade.com:mgmt:brocade-ip-policy', defining_module='brocade-ip-policy', yang_type='extcommunitylist-instance', is_config=True)""",
        })

    self.__extcommunity_list_num = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_extcommunity_list_num(self):
    self.__extcommunity_list_num = YANGDynClass(base=RestrictedClassType(base_type=RestrictedClassType(base_type=int, restriction_dict={'range': ['0..65535']},int_size=16), restriction_dict={'range': [u'0..99']}), is_leaf=True, yang_name="extcommunity-list-num", rest_name="", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'cli-drop-node-name': None, u'cli-full-no': None}}, is_keyval=True, namespace='urn:brocade.com:mgmt:brocade-ip-policy', defining_module='brocade-ip-policy', yang_type='extcommunitylist-instance', is_config=True)


  def _get_ext_community_action(self):
    """
    Getter method for ext_community_action, mapped from YANG variable /rbridge_id/ip/extcommunity_list/ext_community_action (action-t)
    """
    return self.__ext_community_action
      
  def _set_ext_community_action(self, v, load=False):
    """
    Setter method for ext_community_action, mapped from YANG variable /rbridge_id/ip/extcommunity_list/ext_community_action (action-t)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_ext_community_action is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_ext_community_action() directly.
    """
    if hasattr(v, "_utype"):
      v = v._utype(v)
    try:
      t = YANGDynClass(v,base=RestrictedClassType(base_type=unicode,                                     restriction_type="dict_key",                                     restriction_arg={u'deny': {'value': 2}, u'permit': {'value': 1}},), is_leaf=True, yang_name="ext-community-action", rest_name="", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'cli-drop-node-name': None, u'cli-incomplete-command': None, u'cli-suppress-no': None}}, namespace='urn:brocade.com:mgmt:brocade-ip-policy', defining_module='brocade-ip-policy', yang_type='action-t', is_config=True)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """ext_community_action must be of a type compatible with action-t""",
          'defined-type': "brocade-ip-policy:action-t",
          'generated-type': """YANGDynClass(base=RestrictedClassType(base_type=unicode,                                     restriction_type="dict_key",                                     restriction_arg={u'deny': {'value': 2}, u'permit': {'value': 1}},), is_leaf=True, yang_name="ext-community-action", rest_name="", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'cli-drop-node-name': None, u'cli-incomplete-command': None, u'cli-suppress-no': None}}, namespace='urn:brocade.com:mgmt:brocade-ip-policy', defining_module='brocade-ip-policy', yang_type='action-t', is_config=True)""",
        })

    self.__ext_community_action = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_ext_community_action(self):
    self.__ext_community_action = YANGDynClass(base=RestrictedClassType(base_type=unicode,                                     restriction_type="dict_key",                                     restriction_arg={u'deny': {'value': 2}, u'permit': {'value': 1}},), is_leaf=True, yang_name="ext-community-action", rest_name="", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'cli-drop-node-name': None, u'cli-incomplete-command': None, u'cli-suppress-no': None}}, namespace='urn:brocade.com:mgmt:brocade-ip-policy', defining_module='brocade-ip-policy', yang_type='action-t', is_config=True)


  def _get_ext_community_expr(self):
    """
    Getter method for ext_community_expr, mapped from YANG variable /rbridge_id/ip/extcommunity_list/ext_community_expr (extcommunity-list-expr-t)
    """
    return self.__ext_community_expr
      
  def _set_ext_community_expr(self, v, load=False):
    """
    Setter method for ext_community_expr, mapped from YANG variable /rbridge_id/ip/extcommunity_list/ext_community_expr (extcommunity-list-expr-t)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_ext_community_expr is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_ext_community_expr() directly.
    """
    if hasattr(v, "_utype"):
      v = v._utype(v)
    try:
      t = YANGDynClass(v,base=RestrictedClassType(base_type=unicode, restriction_dict={'pattern': u'(\\s*)|(\\s*((rt)|(soo)|((([1-9][0-9]{0,8})|([1-3][0-9]{9})|(4[0-1][0-9]{8})|(42[0-8][0-9]{7})|(429[0-3][0-9]{6})|(4294[0-8][0-9]{5})|(42949[0-5][0-9]{4})|(429496[0-6][0-9]{3})|(4294967[0-1][0-9]{2})|(42949672[0-8][0-9])|(429496729[0-5])):(([1-9][0-9]{0,8})|([1-3][0-9]{9})|(4[0-1][0-9]{8})|(42[0-8][0-9]{7})|(429[0-3][0-9]{6})|(4294[0-8][0-9]{5})|(42949[0-5][0-9]{4})|(429496[0-6][0-9]{3})|(4294967[0-1][0-9]{2})|(42949672[0-8][0-9])|(429496729[0-5])))|((([0-9]|[1-9][0-9]|1[0-9]{2}|2[0-4][0-9]|25[0-5])\\.){3}([0-9]|[1-9][0-9]|1[0-9]{2}|2[0-4][0-9]|25[0-5]):(([1-9][0-9]{0,8})|([1-3][0-9]{9})|(4[0-1][0-9]{8})|(42[0-8][0-9]{7})|(429[0-3][0-9]{6})|(4294[0-8][0-9]{5})|(42949[0-5][0-9]{4})|(429496[0-6][0-9]{3})|(4294967[0-1][0-9]{2})|(42949672[0-8][0-9])|(429496729[0-5])))))((\\s+((rt)|(soo)|((([1-9][0-9]{0,8})|([1-3][0-9]{9})|(4[0-1][0-9]{8})|(42[0-8][0-9]{7})|(429[0-3][0-9]{6})|(4294[0-8][0-9]{5})|(42949[0-5][0-9]{4})|(429496[0-6][0-9]{3})|(4294967[0-1][0-9]{2})|(42949672[0-8][0-9])|(429496729[0-5])):(([1-9][0-9]{0,8})|([1-3][0-9]{9})|(4[0-1][0-9]{8})|(42[0-8][0-9]{7})|(429[0-3][0-9]{6})|(4294[0-8][0-9]{5})|(42949[0-5][0-9]{4})|(429496[0-6][0-9]{3})|(4294967[0-1][0-9]{2})|(42949672[0-8][0-9])|(429496729[0-5])))|(((([0-9]|[1-9][0-9]|1[0-9]{2}|2[0-4][0-9]|25[0-5])\\.){3}([0-9]|[1-9][0-9]|1[0-9]{2}|2[0-4][0-9]|25[0-5])):(([1-9][0-9]{0,8})|([1-3][0-9]{9})|(4[0-1][0-9]{8})|(42[0-8][0-9]{7})|(429[0-3][0-9]{6})|(4294[0-8][0-9]{5})|(42949[0-5][0-9]{4})|(429496[0-6][0-9]{3})|(4294967[0-1][0-9]{2})|(42949672[0-8][0-9])|(429496729[0-5])))))*)'}), is_leaf=True, yang_name="ext-community-expr", rest_name="", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'info': u'Ext-community-list', u'cli-multi-value': None, u'cli-suppress-no': None, u'cli-break-sequence-commands': None, u'cli-drop-node-name': None, u'cli-full-command': None, u'cli-completion-actionpoint': u'ip-ext-community-list-action-point'}}, namespace='urn:brocade.com:mgmt:brocade-ip-policy', defining_module='brocade-ip-policy', yang_type='extcommunity-list-expr-t', is_config=True)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """ext_community_expr must be of a type compatible with extcommunity-list-expr-t""",
          'defined-type': "brocade-ip-policy:extcommunity-list-expr-t",
          'generated-type': """YANGDynClass(base=RestrictedClassType(base_type=unicode, restriction_dict={'pattern': u'(\\s*)|(\\s*((rt)|(soo)|((([1-9][0-9]{0,8})|([1-3][0-9]{9})|(4[0-1][0-9]{8})|(42[0-8][0-9]{7})|(429[0-3][0-9]{6})|(4294[0-8][0-9]{5})|(42949[0-5][0-9]{4})|(429496[0-6][0-9]{3})|(4294967[0-1][0-9]{2})|(42949672[0-8][0-9])|(429496729[0-5])):(([1-9][0-9]{0,8})|([1-3][0-9]{9})|(4[0-1][0-9]{8})|(42[0-8][0-9]{7})|(429[0-3][0-9]{6})|(4294[0-8][0-9]{5})|(42949[0-5][0-9]{4})|(429496[0-6][0-9]{3})|(4294967[0-1][0-9]{2})|(42949672[0-8][0-9])|(429496729[0-5])))|((([0-9]|[1-9][0-9]|1[0-9]{2}|2[0-4][0-9]|25[0-5])\\.){3}([0-9]|[1-9][0-9]|1[0-9]{2}|2[0-4][0-9]|25[0-5]):(([1-9][0-9]{0,8})|([1-3][0-9]{9})|(4[0-1][0-9]{8})|(42[0-8][0-9]{7})|(429[0-3][0-9]{6})|(4294[0-8][0-9]{5})|(42949[0-5][0-9]{4})|(429496[0-6][0-9]{3})|(4294967[0-1][0-9]{2})|(42949672[0-8][0-9])|(429496729[0-5])))))((\\s+((rt)|(soo)|((([1-9][0-9]{0,8})|([1-3][0-9]{9})|(4[0-1][0-9]{8})|(42[0-8][0-9]{7})|(429[0-3][0-9]{6})|(4294[0-8][0-9]{5})|(42949[0-5][0-9]{4})|(429496[0-6][0-9]{3})|(4294967[0-1][0-9]{2})|(42949672[0-8][0-9])|(429496729[0-5])):(([1-9][0-9]{0,8})|([1-3][0-9]{9})|(4[0-1][0-9]{8})|(42[0-8][0-9]{7})|(429[0-3][0-9]{6})|(4294[0-8][0-9]{5})|(42949[0-5][0-9]{4})|(429496[0-6][0-9]{3})|(4294967[0-1][0-9]{2})|(42949672[0-8][0-9])|(429496729[0-5])))|(((([0-9]|[1-9][0-9]|1[0-9]{2}|2[0-4][0-9]|25[0-5])\\.){3}([0-9]|[1-9][0-9]|1[0-9]{2}|2[0-4][0-9]|25[0-5])):(([1-9][0-9]{0,8})|([1-3][0-9]{9})|(4[0-1][0-9]{8})|(42[0-8][0-9]{7})|(429[0-3][0-9]{6})|(4294[0-8][0-9]{5})|(42949[0-5][0-9]{4})|(429496[0-6][0-9]{3})|(4294967[0-1][0-9]{2})|(42949672[0-8][0-9])|(429496729[0-5])))))*)'}), is_leaf=True, yang_name="ext-community-expr", rest_name="", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'info': u'Ext-community-list', u'cli-multi-value': None, u'cli-suppress-no': None, u'cli-break-sequence-commands': None, u'cli-drop-node-name': None, u'cli-full-command': None, u'cli-completion-actionpoint': u'ip-ext-community-list-action-point'}}, namespace='urn:brocade.com:mgmt:brocade-ip-policy', defining_module='brocade-ip-policy', yang_type='extcommunity-list-expr-t', is_config=True)""",
        })

    self.__ext_community_expr = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_ext_community_expr(self):
    self.__ext_community_expr = YANGDynClass(base=RestrictedClassType(base_type=unicode, restriction_dict={'pattern': u'(\\s*)|(\\s*((rt)|(soo)|((([1-9][0-9]{0,8})|([1-3][0-9]{9})|(4[0-1][0-9]{8})|(42[0-8][0-9]{7})|(429[0-3][0-9]{6})|(4294[0-8][0-9]{5})|(42949[0-5][0-9]{4})|(429496[0-6][0-9]{3})|(4294967[0-1][0-9]{2})|(42949672[0-8][0-9])|(429496729[0-5])):(([1-9][0-9]{0,8})|([1-3][0-9]{9})|(4[0-1][0-9]{8})|(42[0-8][0-9]{7})|(429[0-3][0-9]{6})|(4294[0-8][0-9]{5})|(42949[0-5][0-9]{4})|(429496[0-6][0-9]{3})|(4294967[0-1][0-9]{2})|(42949672[0-8][0-9])|(429496729[0-5])))|((([0-9]|[1-9][0-9]|1[0-9]{2}|2[0-4][0-9]|25[0-5])\\.){3}([0-9]|[1-9][0-9]|1[0-9]{2}|2[0-4][0-9]|25[0-5]):(([1-9][0-9]{0,8})|([1-3][0-9]{9})|(4[0-1][0-9]{8})|(42[0-8][0-9]{7})|(429[0-3][0-9]{6})|(4294[0-8][0-9]{5})|(42949[0-5][0-9]{4})|(429496[0-6][0-9]{3})|(4294967[0-1][0-9]{2})|(42949672[0-8][0-9])|(429496729[0-5])))))((\\s+((rt)|(soo)|((([1-9][0-9]{0,8})|([1-3][0-9]{9})|(4[0-1][0-9]{8})|(42[0-8][0-9]{7})|(429[0-3][0-9]{6})|(4294[0-8][0-9]{5})|(42949[0-5][0-9]{4})|(429496[0-6][0-9]{3})|(4294967[0-1][0-9]{2})|(42949672[0-8][0-9])|(429496729[0-5])):(([1-9][0-9]{0,8})|([1-3][0-9]{9})|(4[0-1][0-9]{8})|(42[0-8][0-9]{7})|(429[0-3][0-9]{6})|(4294[0-8][0-9]{5})|(42949[0-5][0-9]{4})|(429496[0-6][0-9]{3})|(4294967[0-1][0-9]{2})|(42949672[0-8][0-9])|(429496729[0-5])))|(((([0-9]|[1-9][0-9]|1[0-9]{2}|2[0-4][0-9]|25[0-5])\\.){3}([0-9]|[1-9][0-9]|1[0-9]{2}|2[0-4][0-9]|25[0-5])):(([1-9][0-9]{0,8})|([1-3][0-9]{9})|(4[0-1][0-9]{8})|(42[0-8][0-9]{7})|(429[0-3][0-9]{6})|(4294[0-8][0-9]{5})|(42949[0-5][0-9]{4})|(429496[0-6][0-9]{3})|(4294967[0-1][0-9]{2})|(42949672[0-8][0-9])|(429496729[0-5])))))*)'}), is_leaf=True, yang_name="ext-community-expr", rest_name="", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'info': u'Ext-community-list', u'cli-multi-value': None, u'cli-suppress-no': None, u'cli-break-sequence-commands': None, u'cli-drop-node-name': None, u'cli-full-command': None, u'cli-completion-actionpoint': u'ip-ext-community-list-action-point'}}, namespace='urn:brocade.com:mgmt:brocade-ip-policy', defining_module='brocade-ip-policy', yang_type='extcommunity-list-expr-t', is_config=True)

  extcommunity_list_num = __builtin__.property(_get_extcommunity_list_num, _set_extcommunity_list_num)
  ext_community_action = __builtin__.property(_get_ext_community_action, _set_ext_community_action)
  ext_community_expr = __builtin__.property(_get_ext_community_expr, _set_ext_community_expr)


  _pyangbind_elements = {'extcommunity_list_num': extcommunity_list_num, 'ext_community_action': ext_community_action, 'ext_community_expr': ext_community_expr, }


