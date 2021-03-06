
from operator import attrgetter
import pyangbind.lib.xpathhelper as xpathhelper
from pyangbind.lib.yangtypes import RestrictedPrecisionDecimalType, RestrictedClassType, TypedListType
from pyangbind.lib.yangtypes import YANGBool, YANGListType, YANGDynClass, ReferenceType
from pyangbind.lib.base import PybindBase
from decimal import Decimal
from bitarray import bitarray
import __builtin__
class seq(PybindBase):
  """
  This class was auto-generated by the PythonClass plugin for PYANG
  from YANG module brocade-mac-access-list - based on the path /mac/access-list/standard/hide-mac-acl-std/seq. Each member element of
  the container is represented as a class variable - with a specific
  YANG type.
  """
  __slots__ = ('_pybind_generated_by', '_path_helper', '_yang_name', '_rest_name', '_extmethods', '__seq_id','__action','__source','__srchost','__src_mac_addr_mask','__count','__log',)

  _yang_name = 'seq'
  _rest_name = 'seq'

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
    self.__count = YANGDynClass(base=YANGBool, is_leaf=True, yang_name="count", rest_name="count", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'info': u'Packet count', u'cli-optional-in-sequence': None, u'cli-suppress-no': None}}, namespace='urn:brocade.com:mgmt:brocade-mac-access-list', defining_module='brocade-mac-access-list', yang_type='empty', is_config=True)
    self.__log = YANGDynClass(base=YANGBool, is_leaf=True, yang_name="log", rest_name="log", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'cli-full-command': None, u'cli-optional-in-sequence': None, u'info': u'Log Packet', u'cli-suppress-no': None}}, namespace='urn:brocade.com:mgmt:brocade-mac-access-list', defining_module='brocade-mac-access-list', yang_type='empty', is_config=True)
    self.__srchost = YANGDynClass(base=unicode, is_leaf=True, yang_name="srchost", rest_name="srchost", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'cli-drop-node-name': None, u'cli-suppress-no': None}}, namespace='urn:brocade.com:mgmt:brocade-mac-access-list', defining_module='brocade-mac-access-list', yang_type='mac-address-type', is_config=True)
    self.__seq_id = YANGDynClass(base=RestrictedClassType(base_type=RestrictedClassType(base_type=long, restriction_dict={'range':  ['0..18446744073709551615']}, int_size=64), restriction_dict={'range': [u'0 .. 4294967290']}), is_leaf=True, yang_name="seq-id", rest_name="seq-id", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, is_keyval=True, namespace='urn:brocade.com:mgmt:brocade-mac-access-list', defining_module='brocade-mac-access-list', yang_type='uint64', is_config=True)
    self.__source = YANGDynClass(base=[unicode,RestrictedClassType(base_type=unicode,                                     restriction_type="dict_key",                                     restriction_arg={u'host': {'value': 2}, u'any': {'value': 1}},),], is_leaf=True, yang_name="source", rest_name="source", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'cli-drop-node-name': None, u'cli-suppress-no': None}}, namespace='urn:brocade.com:mgmt:brocade-mac-access-list', defining_module='brocade-mac-access-list', yang_type='union', is_config=True)
    self.__src_mac_addr_mask = YANGDynClass(base=unicode, is_leaf=True, yang_name="src-mac-addr-mask", rest_name="src-mac-addr-mask", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'cli-drop-node-name': None, u'cli-suppress-no': None}}, namespace='urn:brocade.com:mgmt:brocade-mac-access-list', defining_module='brocade-mac-access-list', yang_type='src-dst-mac-address-mask-type', is_config=True)
    self.__action = YANGDynClass(base=RestrictedClassType(base_type=unicode,                                     restriction_type="dict_key",                                     restriction_arg={u'deny': {'value': 2}, u'hard-drop': {'value': 3}, u'permit': {'value': 1}},), is_leaf=True, yang_name="action", rest_name="action", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'cli-drop-node-name': None, u'cli-incomplete-command': None, u'cli-suppress-no': None}}, namespace='urn:brocade.com:mgmt:brocade-mac-access-list', defining_module='brocade-mac-access-list', yang_type='enumeration', is_config=True)

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
      return [u'mac', u'access-list', u'standard', u'hide-mac-acl-std', u'seq']

  def _rest_path(self):
    if hasattr(self, "_parent"):
      if self._rest_name:
        return self._parent._rest_path()+[self._rest_name]
      else:
        return self._parent._rest_path()
    else:
      return [u'mac', u'access-list', u'standard', u'seq']

  def _get_seq_id(self):
    """
    Getter method for seq_id, mapped from YANG variable /mac/access_list/standard/hide_mac_acl_std/seq/seq_id (uint64)
    """
    return self.__seq_id
      
  def _set_seq_id(self, v, load=False):
    """
    Setter method for seq_id, mapped from YANG variable /mac/access_list/standard/hide_mac_acl_std/seq/seq_id (uint64)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_seq_id is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_seq_id() directly.
    """
    parent = getattr(self, "_parent", None)
    if parent is not None and load is False:
      raise AttributeError("Cannot set keys directly when" +
                             " within an instantiated list")

    if hasattr(v, "_utype"):
      v = v._utype(v)
    try:
      t = YANGDynClass(v,base=RestrictedClassType(base_type=RestrictedClassType(base_type=long, restriction_dict={'range':  ['0..18446744073709551615']}, int_size=64), restriction_dict={'range': [u'0 .. 4294967290']}), is_leaf=True, yang_name="seq-id", rest_name="seq-id", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, is_keyval=True, namespace='urn:brocade.com:mgmt:brocade-mac-access-list', defining_module='brocade-mac-access-list', yang_type='uint64', is_config=True)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """seq_id must be of a type compatible with uint64""",
          'defined-type': "uint64",
          'generated-type': """YANGDynClass(base=RestrictedClassType(base_type=RestrictedClassType(base_type=long, restriction_dict={'range':  ['0..18446744073709551615']}, int_size=64), restriction_dict={'range': [u'0 .. 4294967290']}), is_leaf=True, yang_name="seq-id", rest_name="seq-id", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, is_keyval=True, namespace='urn:brocade.com:mgmt:brocade-mac-access-list', defining_module='brocade-mac-access-list', yang_type='uint64', is_config=True)""",
        })

    self.__seq_id = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_seq_id(self):
    self.__seq_id = YANGDynClass(base=RestrictedClassType(base_type=RestrictedClassType(base_type=long, restriction_dict={'range':  ['0..18446744073709551615']}, int_size=64), restriction_dict={'range': [u'0 .. 4294967290']}), is_leaf=True, yang_name="seq-id", rest_name="seq-id", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, is_keyval=True, namespace='urn:brocade.com:mgmt:brocade-mac-access-list', defining_module='brocade-mac-access-list', yang_type='uint64', is_config=True)


  def _get_action(self):
    """
    Getter method for action, mapped from YANG variable /mac/access_list/standard/hide_mac_acl_std/seq/action (enumeration)
    """
    return self.__action
      
  def _set_action(self, v, load=False):
    """
    Setter method for action, mapped from YANG variable /mac/access_list/standard/hide_mac_acl_std/seq/action (enumeration)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_action is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_action() directly.
    """
    if hasattr(v, "_utype"):
      v = v._utype(v)
    try:
      t = YANGDynClass(v,base=RestrictedClassType(base_type=unicode,                                     restriction_type="dict_key",                                     restriction_arg={u'deny': {'value': 2}, u'hard-drop': {'value': 3}, u'permit': {'value': 1}},), is_leaf=True, yang_name="action", rest_name="action", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'cli-drop-node-name': None, u'cli-incomplete-command': None, u'cli-suppress-no': None}}, namespace='urn:brocade.com:mgmt:brocade-mac-access-list', defining_module='brocade-mac-access-list', yang_type='enumeration', is_config=True)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """action must be of a type compatible with enumeration""",
          'defined-type': "brocade-mac-access-list:enumeration",
          'generated-type': """YANGDynClass(base=RestrictedClassType(base_type=unicode,                                     restriction_type="dict_key",                                     restriction_arg={u'deny': {'value': 2}, u'hard-drop': {'value': 3}, u'permit': {'value': 1}},), is_leaf=True, yang_name="action", rest_name="action", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'cli-drop-node-name': None, u'cli-incomplete-command': None, u'cli-suppress-no': None}}, namespace='urn:brocade.com:mgmt:brocade-mac-access-list', defining_module='brocade-mac-access-list', yang_type='enumeration', is_config=True)""",
        })

    self.__action = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_action(self):
    self.__action = YANGDynClass(base=RestrictedClassType(base_type=unicode,                                     restriction_type="dict_key",                                     restriction_arg={u'deny': {'value': 2}, u'hard-drop': {'value': 3}, u'permit': {'value': 1}},), is_leaf=True, yang_name="action", rest_name="action", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'cli-drop-node-name': None, u'cli-incomplete-command': None, u'cli-suppress-no': None}}, namespace='urn:brocade.com:mgmt:brocade-mac-access-list', defining_module='brocade-mac-access-list', yang_type='enumeration', is_config=True)


  def _get_source(self):
    """
    Getter method for source, mapped from YANG variable /mac/access_list/standard/hide_mac_acl_std/seq/source (union)
    """
    return self.__source
      
  def _set_source(self, v, load=False):
    """
    Setter method for source, mapped from YANG variable /mac/access_list/standard/hide_mac_acl_std/seq/source (union)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_source is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_source() directly.
    """
    if hasattr(v, "_utype"):
      v = v._utype(v)
    try:
      t = YANGDynClass(v,base=[unicode,RestrictedClassType(base_type=unicode,                                     restriction_type="dict_key",                                     restriction_arg={u'host': {'value': 2}, u'any': {'value': 1}},),], is_leaf=True, yang_name="source", rest_name="source", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'cli-drop-node-name': None, u'cli-suppress-no': None}}, namespace='urn:brocade.com:mgmt:brocade-mac-access-list', defining_module='brocade-mac-access-list', yang_type='union', is_config=True)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """source must be of a type compatible with union""",
          'defined-type': "brocade-mac-access-list:union",
          'generated-type': """YANGDynClass(base=[unicode,RestrictedClassType(base_type=unicode,                                     restriction_type="dict_key",                                     restriction_arg={u'host': {'value': 2}, u'any': {'value': 1}},),], is_leaf=True, yang_name="source", rest_name="source", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'cli-drop-node-name': None, u'cli-suppress-no': None}}, namespace='urn:brocade.com:mgmt:brocade-mac-access-list', defining_module='brocade-mac-access-list', yang_type='union', is_config=True)""",
        })

    self.__source = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_source(self):
    self.__source = YANGDynClass(base=[unicode,RestrictedClassType(base_type=unicode,                                     restriction_type="dict_key",                                     restriction_arg={u'host': {'value': 2}, u'any': {'value': 1}},),], is_leaf=True, yang_name="source", rest_name="source", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'cli-drop-node-name': None, u'cli-suppress-no': None}}, namespace='urn:brocade.com:mgmt:brocade-mac-access-list', defining_module='brocade-mac-access-list', yang_type='union', is_config=True)


  def _get_srchost(self):
    """
    Getter method for srchost, mapped from YANG variable /mac/access_list/standard/hide_mac_acl_std/seq/srchost (mac-address-type)
    """
    return self.__srchost
      
  def _set_srchost(self, v, load=False):
    """
    Setter method for srchost, mapped from YANG variable /mac/access_list/standard/hide_mac_acl_std/seq/srchost (mac-address-type)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_srchost is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_srchost() directly.
    """
    if hasattr(v, "_utype"):
      v = v._utype(v)
    try:
      t = YANGDynClass(v,base=unicode, is_leaf=True, yang_name="srchost", rest_name="srchost", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'cli-drop-node-name': None, u'cli-suppress-no': None}}, namespace='urn:brocade.com:mgmt:brocade-mac-access-list', defining_module='brocade-mac-access-list', yang_type='mac-address-type', is_config=True)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """srchost must be of a type compatible with mac-address-type""",
          'defined-type': "brocade-mac-access-list:mac-address-type",
          'generated-type': """YANGDynClass(base=unicode, is_leaf=True, yang_name="srchost", rest_name="srchost", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'cli-drop-node-name': None, u'cli-suppress-no': None}}, namespace='urn:brocade.com:mgmt:brocade-mac-access-list', defining_module='brocade-mac-access-list', yang_type='mac-address-type', is_config=True)""",
        })

    self.__srchost = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_srchost(self):
    self.__srchost = YANGDynClass(base=unicode, is_leaf=True, yang_name="srchost", rest_name="srchost", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'cli-drop-node-name': None, u'cli-suppress-no': None}}, namespace='urn:brocade.com:mgmt:brocade-mac-access-list', defining_module='brocade-mac-access-list', yang_type='mac-address-type', is_config=True)


  def _get_src_mac_addr_mask(self):
    """
    Getter method for src_mac_addr_mask, mapped from YANG variable /mac/access_list/standard/hide_mac_acl_std/seq/src_mac_addr_mask (src-dst-mac-address-mask-type)
    """
    return self.__src_mac_addr_mask
      
  def _set_src_mac_addr_mask(self, v, load=False):
    """
    Setter method for src_mac_addr_mask, mapped from YANG variable /mac/access_list/standard/hide_mac_acl_std/seq/src_mac_addr_mask (src-dst-mac-address-mask-type)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_src_mac_addr_mask is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_src_mac_addr_mask() directly.
    """
    if hasattr(v, "_utype"):
      v = v._utype(v)
    try:
      t = YANGDynClass(v,base=unicode, is_leaf=True, yang_name="src-mac-addr-mask", rest_name="src-mac-addr-mask", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'cli-drop-node-name': None, u'cli-suppress-no': None}}, namespace='urn:brocade.com:mgmt:brocade-mac-access-list', defining_module='brocade-mac-access-list', yang_type='src-dst-mac-address-mask-type', is_config=True)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """src_mac_addr_mask must be of a type compatible with src-dst-mac-address-mask-type""",
          'defined-type': "brocade-mac-access-list:src-dst-mac-address-mask-type",
          'generated-type': """YANGDynClass(base=unicode, is_leaf=True, yang_name="src-mac-addr-mask", rest_name="src-mac-addr-mask", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'cli-drop-node-name': None, u'cli-suppress-no': None}}, namespace='urn:brocade.com:mgmt:brocade-mac-access-list', defining_module='brocade-mac-access-list', yang_type='src-dst-mac-address-mask-type', is_config=True)""",
        })

    self.__src_mac_addr_mask = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_src_mac_addr_mask(self):
    self.__src_mac_addr_mask = YANGDynClass(base=unicode, is_leaf=True, yang_name="src-mac-addr-mask", rest_name="src-mac-addr-mask", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'cli-drop-node-name': None, u'cli-suppress-no': None}}, namespace='urn:brocade.com:mgmt:brocade-mac-access-list', defining_module='brocade-mac-access-list', yang_type='src-dst-mac-address-mask-type', is_config=True)


  def _get_count(self):
    """
    Getter method for count, mapped from YANG variable /mac/access_list/standard/hide_mac_acl_std/seq/count (empty)
    """
    return self.__count
      
  def _set_count(self, v, load=False):
    """
    Setter method for count, mapped from YANG variable /mac/access_list/standard/hide_mac_acl_std/seq/count (empty)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_count is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_count() directly.
    """
    if hasattr(v, "_utype"):
      v = v._utype(v)
    try:
      t = YANGDynClass(v,base=YANGBool, is_leaf=True, yang_name="count", rest_name="count", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'info': u'Packet count', u'cli-optional-in-sequence': None, u'cli-suppress-no': None}}, namespace='urn:brocade.com:mgmt:brocade-mac-access-list', defining_module='brocade-mac-access-list', yang_type='empty', is_config=True)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """count must be of a type compatible with empty""",
          'defined-type': "empty",
          'generated-type': """YANGDynClass(base=YANGBool, is_leaf=True, yang_name="count", rest_name="count", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'info': u'Packet count', u'cli-optional-in-sequence': None, u'cli-suppress-no': None}}, namespace='urn:brocade.com:mgmt:brocade-mac-access-list', defining_module='brocade-mac-access-list', yang_type='empty', is_config=True)""",
        })

    self.__count = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_count(self):
    self.__count = YANGDynClass(base=YANGBool, is_leaf=True, yang_name="count", rest_name="count", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'info': u'Packet count', u'cli-optional-in-sequence': None, u'cli-suppress-no': None}}, namespace='urn:brocade.com:mgmt:brocade-mac-access-list', defining_module='brocade-mac-access-list', yang_type='empty', is_config=True)


  def _get_log(self):
    """
    Getter method for log, mapped from YANG variable /mac/access_list/standard/hide_mac_acl_std/seq/log (empty)
    """
    return self.__log
      
  def _set_log(self, v, load=False):
    """
    Setter method for log, mapped from YANG variable /mac/access_list/standard/hide_mac_acl_std/seq/log (empty)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_log is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_log() directly.
    """
    if hasattr(v, "_utype"):
      v = v._utype(v)
    try:
      t = YANGDynClass(v,base=YANGBool, is_leaf=True, yang_name="log", rest_name="log", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'cli-full-command': None, u'cli-optional-in-sequence': None, u'info': u'Log Packet', u'cli-suppress-no': None}}, namespace='urn:brocade.com:mgmt:brocade-mac-access-list', defining_module='brocade-mac-access-list', yang_type='empty', is_config=True)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """log must be of a type compatible with empty""",
          'defined-type': "empty",
          'generated-type': """YANGDynClass(base=YANGBool, is_leaf=True, yang_name="log", rest_name="log", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'cli-full-command': None, u'cli-optional-in-sequence': None, u'info': u'Log Packet', u'cli-suppress-no': None}}, namespace='urn:brocade.com:mgmt:brocade-mac-access-list', defining_module='brocade-mac-access-list', yang_type='empty', is_config=True)""",
        })

    self.__log = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_log(self):
    self.__log = YANGDynClass(base=YANGBool, is_leaf=True, yang_name="log", rest_name="log", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'cli-full-command': None, u'cli-optional-in-sequence': None, u'info': u'Log Packet', u'cli-suppress-no': None}}, namespace='urn:brocade.com:mgmt:brocade-mac-access-list', defining_module='brocade-mac-access-list', yang_type='empty', is_config=True)

  seq_id = __builtin__.property(_get_seq_id, _set_seq_id)
  action = __builtin__.property(_get_action, _set_action)
  source = __builtin__.property(_get_source, _set_source)
  srchost = __builtin__.property(_get_srchost, _set_srchost)
  src_mac_addr_mask = __builtin__.property(_get_src_mac_addr_mask, _set_src_mac_addr_mask)
  count = __builtin__.property(_get_count, _set_count)
  log = __builtin__.property(_get_log, _set_log)


  _pyangbind_elements = {'seq_id': seq_id, 'action': action, 'source': source, 'srchost': srchost, 'src_mac_addr_mask': src_mac_addr_mask, 'count': count, 'log': log, }


