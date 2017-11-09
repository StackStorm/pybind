
from operator import attrgetter
import pyangbind.lib.xpathhelper as xpathhelper
from pyangbind.lib.yangtypes import RestrictedPrecisionDecimalType, RestrictedClassType, TypedListType
from pyangbind.lib.yangtypes import YANGBool, YANGListType, YANGDynClass, ReferenceType
from pyangbind.lib.base import PybindBase
from decimal import Decimal
from bitarray import bitarray
import __builtin__
class igmp_entry(PybindBase):
  """
  This class was auto-generated by the PythonClass plugin for PYANG
  from YANG module brocade-mc-hms-operational - based on the path /igmp-snooping-state/igmp-mct-groups/igmp-entry. Each member element of
  the container is represented as a class variable - with a specific
  YANG type.

  YANG Description: Igmp Snooping Cluster Group Information
  """
  __slots__ = ('_pybind_generated_by', '_path_helper', '_yang_name', '_rest_name', '_extmethods', '__grp_addr','__src_addr','__interface_name','__member_intf','__member_type','__filter_mode','__mcast_df','__peer_addr',)

  _yang_name = 'igmp-entry'
  _rest_name = 'igmp-entry'

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
    self.__interface_name = YANGDynClass(base=unicode, is_leaf=True, yang_name="interface-name", rest_name="interface-name", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, is_keyval=True, namespace='urn:brocade.com:mgmt:brocade-mc-hms-operational', defining_module='brocade-mc-hms-operational', yang_type='string', is_config=False)
    self.__src_addr = YANGDynClass(base=unicode, is_leaf=True, yang_name="src-addr", rest_name="src-addr", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, is_keyval=True, namespace='urn:brocade.com:mgmt:brocade-mc-hms-operational', defining_module='brocade-mc-hms-operational', yang_type='string', is_config=False)
    self.__member_type = YANGDynClass(base=unicode, is_leaf=True, yang_name="member-type", rest_name="member-type", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='urn:brocade.com:mgmt:brocade-mc-hms-operational', defining_module='brocade-mc-hms-operational', yang_type='string', is_config=False)
    self.__peer_addr = YANGDynClass(base=unicode, is_leaf=True, yang_name="peer-addr", rest_name="peer-addr", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='urn:brocade.com:mgmt:brocade-mc-hms-operational', defining_module='brocade-mc-hms-operational', yang_type='string', is_config=False)
    self.__member_intf = YANGDynClass(base=unicode, is_leaf=True, yang_name="member-intf", rest_name="member-intf", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, is_keyval=True, namespace='urn:brocade.com:mgmt:brocade-mc-hms-operational', defining_module='brocade-mc-hms-operational', yang_type='string', is_config=False)
    self.__grp_addr = YANGDynClass(base=unicode, is_leaf=True, yang_name="grp-addr", rest_name="grp-addr", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, is_keyval=True, namespace='urn:brocade.com:mgmt:brocade-mc-hms-operational', defining_module='brocade-mc-hms-operational', yang_type='string', is_config=False)
    self.__filter_mode = YANGDynClass(base=unicode, is_leaf=True, yang_name="filter-mode", rest_name="filter-mode", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='urn:brocade.com:mgmt:brocade-mc-hms-operational', defining_module='brocade-mc-hms-operational', yang_type='string', is_config=False)
    self.__mcast_df = YANGDynClass(base=unicode, is_leaf=True, yang_name="mcast-df", rest_name="mcast-df", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='urn:brocade.com:mgmt:brocade-mc-hms-operational', defining_module='brocade-mc-hms-operational', yang_type='string', is_config=False)

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
      return [u'igmp-snooping-state', u'igmp-mct-groups', u'igmp-entry']

  def _rest_path(self):
    if hasattr(self, "_parent"):
      if self._rest_name:
        return self._parent._rest_path()+[self._rest_name]
      else:
        return self._parent._rest_path()
    else:
      return [u'igmp-snooping-state', u'igmp-mct-groups', u'igmp-entry']

  def _get_grp_addr(self):
    """
    Getter method for grp_addr, mapped from YANG variable /igmp_snooping_state/igmp_mct_groups/igmp_entry/grp_addr (string)

    YANG Description: Multicast Group Address
    """
    return self.__grp_addr
      
  def _set_grp_addr(self, v, load=False):
    """
    Setter method for grp_addr, mapped from YANG variable /igmp_snooping_state/igmp_mct_groups/igmp_entry/grp_addr (string)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_grp_addr is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_grp_addr() directly.

    YANG Description: Multicast Group Address
    """
    parent = getattr(self, "_parent", None)
    if parent is not None and load is False:
      raise AttributeError("Cannot set keys directly when" +
                             " within an instantiated list")

    if hasattr(v, "_utype"):
      v = v._utype(v)
    try:
      t = YANGDynClass(v,base=unicode, is_leaf=True, yang_name="grp-addr", rest_name="grp-addr", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, is_keyval=True, namespace='urn:brocade.com:mgmt:brocade-mc-hms-operational', defining_module='brocade-mc-hms-operational', yang_type='string', is_config=False)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """grp_addr must be of a type compatible with string""",
          'defined-type': "string",
          'generated-type': """YANGDynClass(base=unicode, is_leaf=True, yang_name="grp-addr", rest_name="grp-addr", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, is_keyval=True, namespace='urn:brocade.com:mgmt:brocade-mc-hms-operational', defining_module='brocade-mc-hms-operational', yang_type='string', is_config=False)""",
        })

    self.__grp_addr = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_grp_addr(self):
    self.__grp_addr = YANGDynClass(base=unicode, is_leaf=True, yang_name="grp-addr", rest_name="grp-addr", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, is_keyval=True, namespace='urn:brocade.com:mgmt:brocade-mc-hms-operational', defining_module='brocade-mc-hms-operational', yang_type='string', is_config=False)


  def _get_src_addr(self):
    """
    Getter method for src_addr, mapped from YANG variable /igmp_snooping_state/igmp_mct_groups/igmp_entry/src_addr (string)

    YANG Description: Multicast Source Address
    """
    return self.__src_addr
      
  def _set_src_addr(self, v, load=False):
    """
    Setter method for src_addr, mapped from YANG variable /igmp_snooping_state/igmp_mct_groups/igmp_entry/src_addr (string)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_src_addr is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_src_addr() directly.

    YANG Description: Multicast Source Address
    """
    parent = getattr(self, "_parent", None)
    if parent is not None and load is False:
      raise AttributeError("Cannot set keys directly when" +
                             " within an instantiated list")

    if hasattr(v, "_utype"):
      v = v._utype(v)
    try:
      t = YANGDynClass(v,base=unicode, is_leaf=True, yang_name="src-addr", rest_name="src-addr", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, is_keyval=True, namespace='urn:brocade.com:mgmt:brocade-mc-hms-operational', defining_module='brocade-mc-hms-operational', yang_type='string', is_config=False)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """src_addr must be of a type compatible with string""",
          'defined-type': "string",
          'generated-type': """YANGDynClass(base=unicode, is_leaf=True, yang_name="src-addr", rest_name="src-addr", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, is_keyval=True, namespace='urn:brocade.com:mgmt:brocade-mc-hms-operational', defining_module='brocade-mc-hms-operational', yang_type='string', is_config=False)""",
        })

    self.__src_addr = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_src_addr(self):
    self.__src_addr = YANGDynClass(base=unicode, is_leaf=True, yang_name="src-addr", rest_name="src-addr", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, is_keyval=True, namespace='urn:brocade.com:mgmt:brocade-mc-hms-operational', defining_module='brocade-mc-hms-operational', yang_type='string', is_config=False)


  def _get_interface_name(self):
    """
    Getter method for interface_name, mapped from YANG variable /igmp_snooping_state/igmp_mct_groups/igmp_entry/interface_name (string)

    YANG Description: Igmp interface name
    """
    return self.__interface_name
      
  def _set_interface_name(self, v, load=False):
    """
    Setter method for interface_name, mapped from YANG variable /igmp_snooping_state/igmp_mct_groups/igmp_entry/interface_name (string)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_interface_name is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_interface_name() directly.

    YANG Description: Igmp interface name
    """
    parent = getattr(self, "_parent", None)
    if parent is not None and load is False:
      raise AttributeError("Cannot set keys directly when" +
                             " within an instantiated list")

    if hasattr(v, "_utype"):
      v = v._utype(v)
    try:
      t = YANGDynClass(v,base=unicode, is_leaf=True, yang_name="interface-name", rest_name="interface-name", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, is_keyval=True, namespace='urn:brocade.com:mgmt:brocade-mc-hms-operational', defining_module='brocade-mc-hms-operational', yang_type='string', is_config=False)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """interface_name must be of a type compatible with string""",
          'defined-type': "string",
          'generated-type': """YANGDynClass(base=unicode, is_leaf=True, yang_name="interface-name", rest_name="interface-name", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, is_keyval=True, namespace='urn:brocade.com:mgmt:brocade-mc-hms-operational', defining_module='brocade-mc-hms-operational', yang_type='string', is_config=False)""",
        })

    self.__interface_name = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_interface_name(self):
    self.__interface_name = YANGDynClass(base=unicode, is_leaf=True, yang_name="interface-name", rest_name="interface-name", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, is_keyval=True, namespace='urn:brocade.com:mgmt:brocade-mc-hms-operational', defining_module='brocade-mc-hms-operational', yang_type='string', is_config=False)


  def _get_member_intf(self):
    """
    Getter method for member_intf, mapped from YANG variable /igmp_snooping_state/igmp_mct_groups/igmp_entry/member_intf (string)

    YANG Description: Group interface member ship
    """
    return self.__member_intf
      
  def _set_member_intf(self, v, load=False):
    """
    Setter method for member_intf, mapped from YANG variable /igmp_snooping_state/igmp_mct_groups/igmp_entry/member_intf (string)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_member_intf is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_member_intf() directly.

    YANG Description: Group interface member ship
    """
    parent = getattr(self, "_parent", None)
    if parent is not None and load is False:
      raise AttributeError("Cannot set keys directly when" +
                             " within an instantiated list")

    if hasattr(v, "_utype"):
      v = v._utype(v)
    try:
      t = YANGDynClass(v,base=unicode, is_leaf=True, yang_name="member-intf", rest_name="member-intf", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, is_keyval=True, namespace='urn:brocade.com:mgmt:brocade-mc-hms-operational', defining_module='brocade-mc-hms-operational', yang_type='string', is_config=False)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """member_intf must be of a type compatible with string""",
          'defined-type': "string",
          'generated-type': """YANGDynClass(base=unicode, is_leaf=True, yang_name="member-intf", rest_name="member-intf", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, is_keyval=True, namespace='urn:brocade.com:mgmt:brocade-mc-hms-operational', defining_module='brocade-mc-hms-operational', yang_type='string', is_config=False)""",
        })

    self.__member_intf = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_member_intf(self):
    self.__member_intf = YANGDynClass(base=unicode, is_leaf=True, yang_name="member-intf", rest_name="member-intf", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, is_keyval=True, namespace='urn:brocade.com:mgmt:brocade-mc-hms-operational', defining_module='brocade-mc-hms-operational', yang_type='string', is_config=False)


  def _get_member_type(self):
    """
    Getter method for member_type, mapped from YANG variable /igmp_snooping_state/igmp_mct_groups/igmp_entry/member_type (string)

    YANG Description: MCT cluster Group member type
    """
    return self.__member_type
      
  def _set_member_type(self, v, load=False):
    """
    Setter method for member_type, mapped from YANG variable /igmp_snooping_state/igmp_mct_groups/igmp_entry/member_type (string)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_member_type is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_member_type() directly.

    YANG Description: MCT cluster Group member type
    """
    if hasattr(v, "_utype"):
      v = v._utype(v)
    try:
      t = YANGDynClass(v,base=unicode, is_leaf=True, yang_name="member-type", rest_name="member-type", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='urn:brocade.com:mgmt:brocade-mc-hms-operational', defining_module='brocade-mc-hms-operational', yang_type='string', is_config=False)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """member_type must be of a type compatible with string""",
          'defined-type': "string",
          'generated-type': """YANGDynClass(base=unicode, is_leaf=True, yang_name="member-type", rest_name="member-type", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='urn:brocade.com:mgmt:brocade-mc-hms-operational', defining_module='brocade-mc-hms-operational', yang_type='string', is_config=False)""",
        })

    self.__member_type = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_member_type(self):
    self.__member_type = YANGDynClass(base=unicode, is_leaf=True, yang_name="member-type", rest_name="member-type", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='urn:brocade.com:mgmt:brocade-mc-hms-operational', defining_module='brocade-mc-hms-operational', yang_type='string', is_config=False)


  def _get_filter_mode(self):
    """
    Getter method for filter_mode, mapped from YANG variable /igmp_snooping_state/igmp_mct_groups/igmp_entry/filter_mode (string)

    YANG Description: IGMPv3 filter mode
    """
    return self.__filter_mode
      
  def _set_filter_mode(self, v, load=False):
    """
    Setter method for filter_mode, mapped from YANG variable /igmp_snooping_state/igmp_mct_groups/igmp_entry/filter_mode (string)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_filter_mode is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_filter_mode() directly.

    YANG Description: IGMPv3 filter mode
    """
    if hasattr(v, "_utype"):
      v = v._utype(v)
    try:
      t = YANGDynClass(v,base=unicode, is_leaf=True, yang_name="filter-mode", rest_name="filter-mode", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='urn:brocade.com:mgmt:brocade-mc-hms-operational', defining_module='brocade-mc-hms-operational', yang_type='string', is_config=False)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """filter_mode must be of a type compatible with string""",
          'defined-type': "string",
          'generated-type': """YANGDynClass(base=unicode, is_leaf=True, yang_name="filter-mode", rest_name="filter-mode", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='urn:brocade.com:mgmt:brocade-mc-hms-operational', defining_module='brocade-mc-hms-operational', yang_type='string', is_config=False)""",
        })

    self.__filter_mode = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_filter_mode(self):
    self.__filter_mode = YANGDynClass(base=unicode, is_leaf=True, yang_name="filter-mode", rest_name="filter-mode", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='urn:brocade.com:mgmt:brocade-mc-hms-operational', defining_module='brocade-mc-hms-operational', yang_type='string', is_config=False)


  def _get_mcast_df(self):
    """
    Getter method for mcast_df, mapped from YANG variable /igmp_snooping_state/igmp_mct_groups/igmp_entry/mcast_df (string)

    YANG Description: Multicast Designated Forwarder in Cluster
    """
    return self.__mcast_df
      
  def _set_mcast_df(self, v, load=False):
    """
    Setter method for mcast_df, mapped from YANG variable /igmp_snooping_state/igmp_mct_groups/igmp_entry/mcast_df (string)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_mcast_df is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_mcast_df() directly.

    YANG Description: Multicast Designated Forwarder in Cluster
    """
    if hasattr(v, "_utype"):
      v = v._utype(v)
    try:
      t = YANGDynClass(v,base=unicode, is_leaf=True, yang_name="mcast-df", rest_name="mcast-df", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='urn:brocade.com:mgmt:brocade-mc-hms-operational', defining_module='brocade-mc-hms-operational', yang_type='string', is_config=False)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """mcast_df must be of a type compatible with string""",
          'defined-type': "string",
          'generated-type': """YANGDynClass(base=unicode, is_leaf=True, yang_name="mcast-df", rest_name="mcast-df", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='urn:brocade.com:mgmt:brocade-mc-hms-operational', defining_module='brocade-mc-hms-operational', yang_type='string', is_config=False)""",
        })

    self.__mcast_df = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_mcast_df(self):
    self.__mcast_df = YANGDynClass(base=unicode, is_leaf=True, yang_name="mcast-df", rest_name="mcast-df", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='urn:brocade.com:mgmt:brocade-mc-hms-operational', defining_module='brocade-mc-hms-operational', yang_type='string', is_config=False)


  def _get_peer_addr(self):
    """
    Getter method for peer_addr, mapped from YANG variable /igmp_snooping_state/igmp_mct_groups/igmp_entry/peer_addr (string)

    YANG Description: MCT Cluster Peer Address
    """
    return self.__peer_addr
      
  def _set_peer_addr(self, v, load=False):
    """
    Setter method for peer_addr, mapped from YANG variable /igmp_snooping_state/igmp_mct_groups/igmp_entry/peer_addr (string)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_peer_addr is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_peer_addr() directly.

    YANG Description: MCT Cluster Peer Address
    """
    if hasattr(v, "_utype"):
      v = v._utype(v)
    try:
      t = YANGDynClass(v,base=unicode, is_leaf=True, yang_name="peer-addr", rest_name="peer-addr", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='urn:brocade.com:mgmt:brocade-mc-hms-operational', defining_module='brocade-mc-hms-operational', yang_type='string', is_config=False)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """peer_addr must be of a type compatible with string""",
          'defined-type': "string",
          'generated-type': """YANGDynClass(base=unicode, is_leaf=True, yang_name="peer-addr", rest_name="peer-addr", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='urn:brocade.com:mgmt:brocade-mc-hms-operational', defining_module='brocade-mc-hms-operational', yang_type='string', is_config=False)""",
        })

    self.__peer_addr = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_peer_addr(self):
    self.__peer_addr = YANGDynClass(base=unicode, is_leaf=True, yang_name="peer-addr", rest_name="peer-addr", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='urn:brocade.com:mgmt:brocade-mc-hms-operational', defining_module='brocade-mc-hms-operational', yang_type='string', is_config=False)

  grp_addr = __builtin__.property(_get_grp_addr)
  src_addr = __builtin__.property(_get_src_addr)
  interface_name = __builtin__.property(_get_interface_name)
  member_intf = __builtin__.property(_get_member_intf)
  member_type = __builtin__.property(_get_member_type)
  filter_mode = __builtin__.property(_get_filter_mode)
  mcast_df = __builtin__.property(_get_mcast_df)
  peer_addr = __builtin__.property(_get_peer_addr)


  _pyangbind_elements = {'grp_addr': grp_addr, 'src_addr': src_addr, 'interface_name': interface_name, 'member_intf': member_intf, 'member_type': member_type, 'filter_mode': filter_mode, 'mcast_df': mcast_df, 'peer_addr': peer_addr, }

