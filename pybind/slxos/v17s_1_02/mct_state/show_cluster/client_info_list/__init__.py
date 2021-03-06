
from operator import attrgetter
import pyangbind.lib.xpathhelper as xpathhelper
from pyangbind.lib.yangtypes import RestrictedPrecisionDecimalType, RestrictedClassType, TypedListType
from pyangbind.lib.yangtypes import YANGBool, YANGListType, YANGDynClass, ReferenceType
from pyangbind.lib.base import PybindBase
from decimal import Decimal
from bitarray import bitarray
import __builtin__
import config_vlans
import config_bds
class client_info_list(PybindBase):
  """
  This class was auto-generated by the PythonClass plugin for PYANG
  from YANG module brocade-nsm-operational - based on the path /mct-state/show-cluster/client-info-list. Each member element of
  the container is represented as a class variable - with a specific
  YANG type.

  YANG Description: 
  """
  __slots__ = ('_pybind_generated_by', '_path_helper', '_yang_name', '_rest_name', '_extmethods', '__client_name','__cluster_id','__client_id','__client_esi','__client_interface','__client_state','__num_config_vlans','__num_config_bds','__config_vlans','__config_bds',)

  _yang_name = 'client-info-list'
  _rest_name = 'client-info-list'

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
    self.__client_interface = YANGDynClass(base=unicode, is_leaf=True, yang_name="client-interface", rest_name="client-interface", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='urn:brocade.com:mgmt:brocade-nsm-operational', defining_module='brocade-nsm-operational', yang_type='string', is_config=False)
    self.__num_config_bds = YANGDynClass(base=RestrictedClassType(base_type=long, restriction_dict={'range': ['0..4294967295']}, int_size=32), is_leaf=True, yang_name="num-config-bds", rest_name="num-config-bds", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='urn:brocade.com:mgmt:brocade-nsm-operational', defining_module='brocade-nsm-operational', yang_type='uint32', is_config=False)
    self.__client_name = YANGDynClass(base=unicode, is_leaf=True, yang_name="client-name", rest_name="client-name", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='urn:brocade.com:mgmt:brocade-nsm-operational', defining_module='brocade-nsm-operational', yang_type='string', is_config=False)
    self.__num_config_vlans = YANGDynClass(base=RestrictedClassType(base_type=long, restriction_dict={'range': ['0..4294967295']}, int_size=32), is_leaf=True, yang_name="num-config-vlans", rest_name="num-config-vlans", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='urn:brocade.com:mgmt:brocade-nsm-operational', defining_module='brocade-nsm-operational', yang_type='uint32', is_config=False)
    self.__cluster_id = YANGDynClass(base=RestrictedClassType(base_type=long, restriction_dict={'range': ['0..4294967295']}, int_size=32), is_leaf=True, yang_name="cluster-id", rest_name="cluster-id", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, is_keyval=True, namespace='urn:brocade.com:mgmt:brocade-nsm-operational', defining_module='brocade-nsm-operational', yang_type='uint32', is_config=False)
    self.__client_id = YANGDynClass(base=RestrictedClassType(base_type=long, restriction_dict={'range': ['0..4294967295']}, int_size=32), is_leaf=True, yang_name="client-id", rest_name="client-id", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, is_keyval=True, namespace='urn:brocade.com:mgmt:brocade-nsm-operational', defining_module='brocade-nsm-operational', yang_type='uint32', is_config=False)
    self.__client_esi = YANGDynClass(base=unicode, is_leaf=True, yang_name="client-esi", rest_name="client-esi", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='urn:brocade.com:mgmt:brocade-nsm-operational', defining_module='brocade-nsm-operational', yang_type='string', is_config=False)
    self.__client_state = YANGDynClass(base=YANGBool, is_leaf=True, yang_name="client-state", rest_name="client-state", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='urn:brocade.com:mgmt:brocade-nsm-operational', defining_module='brocade-nsm-operational', yang_type='boolean', is_config=False)
    self.__config_bds = YANGDynClass(base=YANGListType("bd_id",config_bds.config_bds, yang_name="config-bds", rest_name="config-bds", parent=self, is_container='list', user_ordered=False, path_helper=self._path_helper, yang_keys='bd-id', extensions={u'tailf-common': {u'callpoint': u'nsm-show-cluster-bds-config-bds-1'}}), is_container='list', yang_name="config-bds", rest_name="config-bds", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'callpoint': u'nsm-show-cluster-bds-config-bds-1'}}, namespace='urn:brocade.com:mgmt:brocade-nsm-operational', defining_module='brocade-nsm-operational', yang_type='list', is_config=False)
    self.__config_vlans = YANGDynClass(base=YANGListType("vlan_id",config_vlans.config_vlans, yang_name="config-vlans", rest_name="config-vlans", parent=self, is_container='list', user_ordered=False, path_helper=self._path_helper, yang_keys='vlan-id', extensions={u'tailf-common': {u'callpoint': u'nsm-show-cluster-config-vlan-config-vlans-1'}}), is_container='list', yang_name="config-vlans", rest_name="config-vlans", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'callpoint': u'nsm-show-cluster-config-vlan-config-vlans-1'}}, namespace='urn:brocade.com:mgmt:brocade-nsm-operational', defining_module='brocade-nsm-operational', yang_type='list', is_config=False)

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
      return [u'mct-state', u'show-cluster', u'client-info-list']

  def _rest_path(self):
    if hasattr(self, "_parent"):
      if self._rest_name:
        return self._parent._rest_path()+[self._rest_name]
      else:
        return self._parent._rest_path()
    else:
      return [u'mct-state', u'show-cluster', u'client-info-list']

  def _get_client_name(self):
    """
    Getter method for client_name, mapped from YANG variable /mct_state/show_cluster/client_info_list/client_name (string)
    """
    return self.__client_name
      
  def _set_client_name(self, v, load=False):
    """
    Setter method for client_name, mapped from YANG variable /mct_state/show_cluster/client_info_list/client_name (string)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_client_name is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_client_name() directly.
    """
    if hasattr(v, "_utype"):
      v = v._utype(v)
    try:
      t = YANGDynClass(v,base=unicode, is_leaf=True, yang_name="client-name", rest_name="client-name", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='urn:brocade.com:mgmt:brocade-nsm-operational', defining_module='brocade-nsm-operational', yang_type='string', is_config=False)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """client_name must be of a type compatible with string""",
          'defined-type': "string",
          'generated-type': """YANGDynClass(base=unicode, is_leaf=True, yang_name="client-name", rest_name="client-name", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='urn:brocade.com:mgmt:brocade-nsm-operational', defining_module='brocade-nsm-operational', yang_type='string', is_config=False)""",
        })

    self.__client_name = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_client_name(self):
    self.__client_name = YANGDynClass(base=unicode, is_leaf=True, yang_name="client-name", rest_name="client-name", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='urn:brocade.com:mgmt:brocade-nsm-operational', defining_module='brocade-nsm-operational', yang_type='string', is_config=False)


  def _get_cluster_id(self):
    """
    Getter method for cluster_id, mapped from YANG variable /mct_state/show_cluster/client_info_list/cluster_id (uint32)
    """
    return self.__cluster_id
      
  def _set_cluster_id(self, v, load=False):
    """
    Setter method for cluster_id, mapped from YANG variable /mct_state/show_cluster/client_info_list/cluster_id (uint32)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_cluster_id is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_cluster_id() directly.
    """
    parent = getattr(self, "_parent", None)
    if parent is not None and load is False:
      raise AttributeError("Cannot set keys directly when" +
                             " within an instantiated list")

    if hasattr(v, "_utype"):
      v = v._utype(v)
    try:
      t = YANGDynClass(v,base=RestrictedClassType(base_type=long, restriction_dict={'range': ['0..4294967295']}, int_size=32), is_leaf=True, yang_name="cluster-id", rest_name="cluster-id", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, is_keyval=True, namespace='urn:brocade.com:mgmt:brocade-nsm-operational', defining_module='brocade-nsm-operational', yang_type='uint32', is_config=False)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """cluster_id must be of a type compatible with uint32""",
          'defined-type': "uint32",
          'generated-type': """YANGDynClass(base=RestrictedClassType(base_type=long, restriction_dict={'range': ['0..4294967295']}, int_size=32), is_leaf=True, yang_name="cluster-id", rest_name="cluster-id", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, is_keyval=True, namespace='urn:brocade.com:mgmt:brocade-nsm-operational', defining_module='brocade-nsm-operational', yang_type='uint32', is_config=False)""",
        })

    self.__cluster_id = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_cluster_id(self):
    self.__cluster_id = YANGDynClass(base=RestrictedClassType(base_type=long, restriction_dict={'range': ['0..4294967295']}, int_size=32), is_leaf=True, yang_name="cluster-id", rest_name="cluster-id", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, is_keyval=True, namespace='urn:brocade.com:mgmt:brocade-nsm-operational', defining_module='brocade-nsm-operational', yang_type='uint32', is_config=False)


  def _get_client_id(self):
    """
    Getter method for client_id, mapped from YANG variable /mct_state/show_cluster/client_info_list/client_id (uint32)
    """
    return self.__client_id
      
  def _set_client_id(self, v, load=False):
    """
    Setter method for client_id, mapped from YANG variable /mct_state/show_cluster/client_info_list/client_id (uint32)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_client_id is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_client_id() directly.
    """
    parent = getattr(self, "_parent", None)
    if parent is not None and load is False:
      raise AttributeError("Cannot set keys directly when" +
                             " within an instantiated list")

    if hasattr(v, "_utype"):
      v = v._utype(v)
    try:
      t = YANGDynClass(v,base=RestrictedClassType(base_type=long, restriction_dict={'range': ['0..4294967295']}, int_size=32), is_leaf=True, yang_name="client-id", rest_name="client-id", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, is_keyval=True, namespace='urn:brocade.com:mgmt:brocade-nsm-operational', defining_module='brocade-nsm-operational', yang_type='uint32', is_config=False)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """client_id must be of a type compatible with uint32""",
          'defined-type': "uint32",
          'generated-type': """YANGDynClass(base=RestrictedClassType(base_type=long, restriction_dict={'range': ['0..4294967295']}, int_size=32), is_leaf=True, yang_name="client-id", rest_name="client-id", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, is_keyval=True, namespace='urn:brocade.com:mgmt:brocade-nsm-operational', defining_module='brocade-nsm-operational', yang_type='uint32', is_config=False)""",
        })

    self.__client_id = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_client_id(self):
    self.__client_id = YANGDynClass(base=RestrictedClassType(base_type=long, restriction_dict={'range': ['0..4294967295']}, int_size=32), is_leaf=True, yang_name="client-id", rest_name="client-id", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, is_keyval=True, namespace='urn:brocade.com:mgmt:brocade-nsm-operational', defining_module='brocade-nsm-operational', yang_type='uint32', is_config=False)


  def _get_client_esi(self):
    """
    Getter method for client_esi, mapped from YANG variable /mct_state/show_cluster/client_info_list/client_esi (string)
    """
    return self.__client_esi
      
  def _set_client_esi(self, v, load=False):
    """
    Setter method for client_esi, mapped from YANG variable /mct_state/show_cluster/client_info_list/client_esi (string)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_client_esi is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_client_esi() directly.
    """
    if hasattr(v, "_utype"):
      v = v._utype(v)
    try:
      t = YANGDynClass(v,base=unicode, is_leaf=True, yang_name="client-esi", rest_name="client-esi", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='urn:brocade.com:mgmt:brocade-nsm-operational', defining_module='brocade-nsm-operational', yang_type='string', is_config=False)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """client_esi must be of a type compatible with string""",
          'defined-type': "string",
          'generated-type': """YANGDynClass(base=unicode, is_leaf=True, yang_name="client-esi", rest_name="client-esi", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='urn:brocade.com:mgmt:brocade-nsm-operational', defining_module='brocade-nsm-operational', yang_type='string', is_config=False)""",
        })

    self.__client_esi = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_client_esi(self):
    self.__client_esi = YANGDynClass(base=unicode, is_leaf=True, yang_name="client-esi", rest_name="client-esi", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='urn:brocade.com:mgmt:brocade-nsm-operational', defining_module='brocade-nsm-operational', yang_type='string', is_config=False)


  def _get_client_interface(self):
    """
    Getter method for client_interface, mapped from YANG variable /mct_state/show_cluster/client_info_list/client_interface (string)
    """
    return self.__client_interface
      
  def _set_client_interface(self, v, load=False):
    """
    Setter method for client_interface, mapped from YANG variable /mct_state/show_cluster/client_info_list/client_interface (string)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_client_interface is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_client_interface() directly.
    """
    if hasattr(v, "_utype"):
      v = v._utype(v)
    try:
      t = YANGDynClass(v,base=unicode, is_leaf=True, yang_name="client-interface", rest_name="client-interface", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='urn:brocade.com:mgmt:brocade-nsm-operational', defining_module='brocade-nsm-operational', yang_type='string', is_config=False)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """client_interface must be of a type compatible with string""",
          'defined-type': "string",
          'generated-type': """YANGDynClass(base=unicode, is_leaf=True, yang_name="client-interface", rest_name="client-interface", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='urn:brocade.com:mgmt:brocade-nsm-operational', defining_module='brocade-nsm-operational', yang_type='string', is_config=False)""",
        })

    self.__client_interface = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_client_interface(self):
    self.__client_interface = YANGDynClass(base=unicode, is_leaf=True, yang_name="client-interface", rest_name="client-interface", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='urn:brocade.com:mgmt:brocade-nsm-operational', defining_module='brocade-nsm-operational', yang_type='string', is_config=False)


  def _get_client_state(self):
    """
    Getter method for client_state, mapped from YANG variable /mct_state/show_cluster/client_info_list/client_state (boolean)

    YANG Description: Client state
    """
    return self.__client_state
      
  def _set_client_state(self, v, load=False):
    """
    Setter method for client_state, mapped from YANG variable /mct_state/show_cluster/client_info_list/client_state (boolean)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_client_state is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_client_state() directly.

    YANG Description: Client state
    """
    if hasattr(v, "_utype"):
      v = v._utype(v)
    try:
      t = YANGDynClass(v,base=YANGBool, is_leaf=True, yang_name="client-state", rest_name="client-state", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='urn:brocade.com:mgmt:brocade-nsm-operational', defining_module='brocade-nsm-operational', yang_type='boolean', is_config=False)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """client_state must be of a type compatible with boolean""",
          'defined-type': "boolean",
          'generated-type': """YANGDynClass(base=YANGBool, is_leaf=True, yang_name="client-state", rest_name="client-state", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='urn:brocade.com:mgmt:brocade-nsm-operational', defining_module='brocade-nsm-operational', yang_type='boolean', is_config=False)""",
        })

    self.__client_state = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_client_state(self):
    self.__client_state = YANGDynClass(base=YANGBool, is_leaf=True, yang_name="client-state", rest_name="client-state", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='urn:brocade.com:mgmt:brocade-nsm-operational', defining_module='brocade-nsm-operational', yang_type='boolean', is_config=False)


  def _get_num_config_vlans(self):
    """
    Getter method for num_config_vlans, mapped from YANG variable /mct_state/show_cluster/client_info_list/num_config_vlans (uint32)

    YANG Description: Number of vlans
    """
    return self.__num_config_vlans
      
  def _set_num_config_vlans(self, v, load=False):
    """
    Setter method for num_config_vlans, mapped from YANG variable /mct_state/show_cluster/client_info_list/num_config_vlans (uint32)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_num_config_vlans is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_num_config_vlans() directly.

    YANG Description: Number of vlans
    """
    if hasattr(v, "_utype"):
      v = v._utype(v)
    try:
      t = YANGDynClass(v,base=RestrictedClassType(base_type=long, restriction_dict={'range': ['0..4294967295']}, int_size=32), is_leaf=True, yang_name="num-config-vlans", rest_name="num-config-vlans", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='urn:brocade.com:mgmt:brocade-nsm-operational', defining_module='brocade-nsm-operational', yang_type='uint32', is_config=False)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """num_config_vlans must be of a type compatible with uint32""",
          'defined-type': "uint32",
          'generated-type': """YANGDynClass(base=RestrictedClassType(base_type=long, restriction_dict={'range': ['0..4294967295']}, int_size=32), is_leaf=True, yang_name="num-config-vlans", rest_name="num-config-vlans", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='urn:brocade.com:mgmt:brocade-nsm-operational', defining_module='brocade-nsm-operational', yang_type='uint32', is_config=False)""",
        })

    self.__num_config_vlans = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_num_config_vlans(self):
    self.__num_config_vlans = YANGDynClass(base=RestrictedClassType(base_type=long, restriction_dict={'range': ['0..4294967295']}, int_size=32), is_leaf=True, yang_name="num-config-vlans", rest_name="num-config-vlans", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='urn:brocade.com:mgmt:brocade-nsm-operational', defining_module='brocade-nsm-operational', yang_type='uint32', is_config=False)


  def _get_num_config_bds(self):
    """
    Getter method for num_config_bds, mapped from YANG variable /mct_state/show_cluster/client_info_list/num_config_bds (uint32)

    YANG Description: Number of BDs
    """
    return self.__num_config_bds
      
  def _set_num_config_bds(self, v, load=False):
    """
    Setter method for num_config_bds, mapped from YANG variable /mct_state/show_cluster/client_info_list/num_config_bds (uint32)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_num_config_bds is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_num_config_bds() directly.

    YANG Description: Number of BDs
    """
    if hasattr(v, "_utype"):
      v = v._utype(v)
    try:
      t = YANGDynClass(v,base=RestrictedClassType(base_type=long, restriction_dict={'range': ['0..4294967295']}, int_size=32), is_leaf=True, yang_name="num-config-bds", rest_name="num-config-bds", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='urn:brocade.com:mgmt:brocade-nsm-operational', defining_module='brocade-nsm-operational', yang_type='uint32', is_config=False)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """num_config_bds must be of a type compatible with uint32""",
          'defined-type': "uint32",
          'generated-type': """YANGDynClass(base=RestrictedClassType(base_type=long, restriction_dict={'range': ['0..4294967295']}, int_size=32), is_leaf=True, yang_name="num-config-bds", rest_name="num-config-bds", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='urn:brocade.com:mgmt:brocade-nsm-operational', defining_module='brocade-nsm-operational', yang_type='uint32', is_config=False)""",
        })

    self.__num_config_bds = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_num_config_bds(self):
    self.__num_config_bds = YANGDynClass(base=RestrictedClassType(base_type=long, restriction_dict={'range': ['0..4294967295']}, int_size=32), is_leaf=True, yang_name="num-config-bds", rest_name="num-config-bds", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='urn:brocade.com:mgmt:brocade-nsm-operational', defining_module='brocade-nsm-operational', yang_type='uint32', is_config=False)


  def _get_config_vlans(self):
    """
    Getter method for config_vlans, mapped from YANG variable /mct_state/show_cluster/client_info_list/config_vlans (list)
    """
    return self.__config_vlans
      
  def _set_config_vlans(self, v, load=False):
    """
    Setter method for config_vlans, mapped from YANG variable /mct_state/show_cluster/client_info_list/config_vlans (list)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_config_vlans is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_config_vlans() directly.
    """
    if hasattr(v, "_utype"):
      v = v._utype(v)
    try:
      t = YANGDynClass(v,base=YANGListType("vlan_id",config_vlans.config_vlans, yang_name="config-vlans", rest_name="config-vlans", parent=self, is_container='list', user_ordered=False, path_helper=self._path_helper, yang_keys='vlan-id', extensions={u'tailf-common': {u'callpoint': u'nsm-show-cluster-config-vlan-config-vlans-1'}}), is_container='list', yang_name="config-vlans", rest_name="config-vlans", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'callpoint': u'nsm-show-cluster-config-vlan-config-vlans-1'}}, namespace='urn:brocade.com:mgmt:brocade-nsm-operational', defining_module='brocade-nsm-operational', yang_type='list', is_config=False)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """config_vlans must be of a type compatible with list""",
          'defined-type': "list",
          'generated-type': """YANGDynClass(base=YANGListType("vlan_id",config_vlans.config_vlans, yang_name="config-vlans", rest_name="config-vlans", parent=self, is_container='list', user_ordered=False, path_helper=self._path_helper, yang_keys='vlan-id', extensions={u'tailf-common': {u'callpoint': u'nsm-show-cluster-config-vlan-config-vlans-1'}}), is_container='list', yang_name="config-vlans", rest_name="config-vlans", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'callpoint': u'nsm-show-cluster-config-vlan-config-vlans-1'}}, namespace='urn:brocade.com:mgmt:brocade-nsm-operational', defining_module='brocade-nsm-operational', yang_type='list', is_config=False)""",
        })

    self.__config_vlans = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_config_vlans(self):
    self.__config_vlans = YANGDynClass(base=YANGListType("vlan_id",config_vlans.config_vlans, yang_name="config-vlans", rest_name="config-vlans", parent=self, is_container='list', user_ordered=False, path_helper=self._path_helper, yang_keys='vlan-id', extensions={u'tailf-common': {u'callpoint': u'nsm-show-cluster-config-vlan-config-vlans-1'}}), is_container='list', yang_name="config-vlans", rest_name="config-vlans", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'callpoint': u'nsm-show-cluster-config-vlan-config-vlans-1'}}, namespace='urn:brocade.com:mgmt:brocade-nsm-operational', defining_module='brocade-nsm-operational', yang_type='list', is_config=False)


  def _get_config_bds(self):
    """
    Getter method for config_bds, mapped from YANG variable /mct_state/show_cluster/client_info_list/config_bds (list)
    """
    return self.__config_bds
      
  def _set_config_bds(self, v, load=False):
    """
    Setter method for config_bds, mapped from YANG variable /mct_state/show_cluster/client_info_list/config_bds (list)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_config_bds is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_config_bds() directly.
    """
    if hasattr(v, "_utype"):
      v = v._utype(v)
    try:
      t = YANGDynClass(v,base=YANGListType("bd_id",config_bds.config_bds, yang_name="config-bds", rest_name="config-bds", parent=self, is_container='list', user_ordered=False, path_helper=self._path_helper, yang_keys='bd-id', extensions={u'tailf-common': {u'callpoint': u'nsm-show-cluster-bds-config-bds-1'}}), is_container='list', yang_name="config-bds", rest_name="config-bds", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'callpoint': u'nsm-show-cluster-bds-config-bds-1'}}, namespace='urn:brocade.com:mgmt:brocade-nsm-operational', defining_module='brocade-nsm-operational', yang_type='list', is_config=False)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """config_bds must be of a type compatible with list""",
          'defined-type': "list",
          'generated-type': """YANGDynClass(base=YANGListType("bd_id",config_bds.config_bds, yang_name="config-bds", rest_name="config-bds", parent=self, is_container='list', user_ordered=False, path_helper=self._path_helper, yang_keys='bd-id', extensions={u'tailf-common': {u'callpoint': u'nsm-show-cluster-bds-config-bds-1'}}), is_container='list', yang_name="config-bds", rest_name="config-bds", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'callpoint': u'nsm-show-cluster-bds-config-bds-1'}}, namespace='urn:brocade.com:mgmt:brocade-nsm-operational', defining_module='brocade-nsm-operational', yang_type='list', is_config=False)""",
        })

    self.__config_bds = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_config_bds(self):
    self.__config_bds = YANGDynClass(base=YANGListType("bd_id",config_bds.config_bds, yang_name="config-bds", rest_name="config-bds", parent=self, is_container='list', user_ordered=False, path_helper=self._path_helper, yang_keys='bd-id', extensions={u'tailf-common': {u'callpoint': u'nsm-show-cluster-bds-config-bds-1'}}), is_container='list', yang_name="config-bds", rest_name="config-bds", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'callpoint': u'nsm-show-cluster-bds-config-bds-1'}}, namespace='urn:brocade.com:mgmt:brocade-nsm-operational', defining_module='brocade-nsm-operational', yang_type='list', is_config=False)

  client_name = __builtin__.property(_get_client_name)
  cluster_id = __builtin__.property(_get_cluster_id)
  client_id = __builtin__.property(_get_client_id)
  client_esi = __builtin__.property(_get_client_esi)
  client_interface = __builtin__.property(_get_client_interface)
  client_state = __builtin__.property(_get_client_state)
  num_config_vlans = __builtin__.property(_get_num_config_vlans)
  num_config_bds = __builtin__.property(_get_num_config_bds)
  config_vlans = __builtin__.property(_get_config_vlans)
  config_bds = __builtin__.property(_get_config_bds)


  _pyangbind_elements = {'client_name': client_name, 'cluster_id': cluster_id, 'client_id': client_id, 'client_esi': client_esi, 'client_interface': client_interface, 'client_state': client_state, 'num_config_vlans': num_config_vlans, 'num_config_bds': num_config_bds, 'config_vlans': config_vlans, 'config_bds': config_bds, }


