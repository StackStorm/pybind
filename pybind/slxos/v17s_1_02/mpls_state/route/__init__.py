
from operator import attrgetter
import pyangbind.lib.xpathhelper as xpathhelper
from pyangbind.lib.yangtypes import RestrictedPrecisionDecimalType, RestrictedClassType, TypedListType
from pyangbind.lib.yangtypes import YANGBool, YANGListType, YANGDynClass, ReferenceType
from pyangbind.lib.base import PybindBase
from decimal import Decimal
from bitarray import bitarray
import __builtin__
class route(PybindBase):
  """
  This class was auto-generated by the PythonClass plugin for PYANG
  from YANG module brocade-mpls-operational - based on the path /mpls-state/route. Each member element of
  the container is represented as a class variable - with a specific
  YANG type.

  YANG Description: Routes installed by MPLS
  """
  __slots__ = ('_pybind_generated_by', '_path_helper', '_yang_name', '_rest_name', '_extmethods', '__entry_index','__outseg_index','__dest_ip_prefix','__gateway_ip_addr','__out_interface_name','__out_label','__protocol','__vif_index','__metric','__use_count',)

  _yang_name = 'route'
  _rest_name = 'route'

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
    self.__protocol = YANGDynClass(base=RestrictedClassType(base_type=unicode,                                     restriction_type="dict_key",                                     restriction_arg={u'mpls-protocol-none': {'value': 0}, u'mpls-protocol-ldp': {'value': 1}, u'mpls-protocol-rsvp': {'value': 2}},), is_leaf=True, yang_name="protocol", rest_name="protocol", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='urn:brocade.com:mgmt:brocade-mpls-operational', defining_module='brocade-mpls-operational', yang_type='mpls-protocol', is_config=False)
    self.__metric = YANGDynClass(base=RestrictedClassType(base_type=long, restriction_dict={'range': ['0..4294967295']}, int_size=32), is_leaf=True, yang_name="metric", rest_name="metric", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='urn:brocade.com:mgmt:brocade-mpls-operational', defining_module='brocade-mpls-operational', yang_type='uint32', is_config=False)
    self.__dest_ip_prefix = YANGDynClass(base=RestrictedClassType(base_type=unicode, restriction_dict={'pattern': u'(([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])\\.){3}([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])/(([0-9])|([1-2][0-9])|(3[0-2]))'}), is_leaf=True, yang_name="dest-ip-prefix", rest_name="dest-ip-prefix", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='urn:brocade.com:mgmt:brocade-mpls-operational', defining_module='brocade-mpls-operational', yang_type='inet:ipv4-prefix', is_config=False)
    self.__vif_index = YANGDynClass(base=RestrictedClassType(base_type=long, restriction_dict={'range': ['0..4294967295']}, int_size=32), is_leaf=True, yang_name="vif-index", rest_name="vif-index", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='urn:brocade.com:mgmt:brocade-mpls-operational', defining_module='brocade-mpls-operational', yang_type='uint32', is_config=False)
    self.__use_count = YANGDynClass(base=RestrictedClassType(base_type=long, restriction_dict={'range': ['0..4294967295']}, int_size=32), is_leaf=True, yang_name="use-count", rest_name="use-count", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='urn:brocade.com:mgmt:brocade-mpls-operational', defining_module='brocade-mpls-operational', yang_type='uint32', is_config=False)
    self.__out_interface_name = YANGDynClass(base=unicode, is_leaf=True, yang_name="out-interface-name", rest_name="out-interface-name", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='urn:brocade.com:mgmt:brocade-mpls-operational', defining_module='brocade-mpls-operational', yang_type='string', is_config=False)
    self.__entry_index = YANGDynClass(base=RestrictedClassType(base_type=long, restriction_dict={'range': ['0..4294967295']}, int_size=32), is_leaf=True, yang_name="entry-index", rest_name="entry-index", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, is_keyval=True, namespace='urn:brocade.com:mgmt:brocade-mpls-operational', defining_module='brocade-mpls-operational', yang_type='uint32', is_config=False)
    self.__gateway_ip_addr = YANGDynClass(base=RestrictedClassType(base_type=unicode, restriction_dict={'pattern': u'(([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])\\.){3}([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])(%[\\p{N}\\p{L}]+)?'}), is_leaf=True, yang_name="gateway-ip-addr", rest_name="gateway-ip-addr", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='urn:brocade.com:mgmt:brocade-mpls-operational', defining_module='brocade-mpls-operational', yang_type='inet:ipv4-address', is_config=False)
    self.__outseg_index = YANGDynClass(base=RestrictedClassType(base_type=long, restriction_dict={'range': ['0..4294967295']}, int_size=32), is_leaf=True, yang_name="outseg-index", rest_name="outseg-index", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='urn:brocade.com:mgmt:brocade-mpls-operational', defining_module='brocade-mpls-operational', yang_type='uint32', is_config=False)
    self.__out_label = YANGDynClass(base=RestrictedClassType(base_type=long, restriction_dict={'range': ['0..4294967295']}, int_size=32), is_leaf=True, yang_name="out-label", rest_name="out-label", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='urn:brocade.com:mgmt:brocade-mpls-operational', defining_module='brocade-mpls-operational', yang_type='uint32', is_config=False)

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
      return [u'mpls-state', u'route']

  def _rest_path(self):
    if hasattr(self, "_parent"):
      if self._rest_name:
        return self._parent._rest_path()+[self._rest_name]
      else:
        return self._parent._rest_path()
    else:
      return [u'mpls-state', u'route']

  def _get_entry_index(self):
    """
    Getter method for entry_index, mapped from YANG variable /mpls_state/route/entry_index (uint32)

    YANG Description: Entry index. This is a pseudo key and refers to the index of the ordered sequnce. Not guranteed to stay unique over time
    """
    return self.__entry_index
      
  def _set_entry_index(self, v, load=False):
    """
    Setter method for entry_index, mapped from YANG variable /mpls_state/route/entry_index (uint32)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_entry_index is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_entry_index() directly.

    YANG Description: Entry index. This is a pseudo key and refers to the index of the ordered sequnce. Not guranteed to stay unique over time
    """
    parent = getattr(self, "_parent", None)
    if parent is not None and load is False:
      raise AttributeError("Cannot set keys directly when" +
                             " within an instantiated list")

    if hasattr(v, "_utype"):
      v = v._utype(v)
    try:
      t = YANGDynClass(v,base=RestrictedClassType(base_type=long, restriction_dict={'range': ['0..4294967295']}, int_size=32), is_leaf=True, yang_name="entry-index", rest_name="entry-index", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, is_keyval=True, namespace='urn:brocade.com:mgmt:brocade-mpls-operational', defining_module='brocade-mpls-operational', yang_type='uint32', is_config=False)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """entry_index must be of a type compatible with uint32""",
          'defined-type': "uint32",
          'generated-type': """YANGDynClass(base=RestrictedClassType(base_type=long, restriction_dict={'range': ['0..4294967295']}, int_size=32), is_leaf=True, yang_name="entry-index", rest_name="entry-index", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, is_keyval=True, namespace='urn:brocade.com:mgmt:brocade-mpls-operational', defining_module='brocade-mpls-operational', yang_type='uint32', is_config=False)""",
        })

    self.__entry_index = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_entry_index(self):
    self.__entry_index = YANGDynClass(base=RestrictedClassType(base_type=long, restriction_dict={'range': ['0..4294967295']}, int_size=32), is_leaf=True, yang_name="entry-index", rest_name="entry-index", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, is_keyval=True, namespace='urn:brocade.com:mgmt:brocade-mpls-operational', defining_module='brocade-mpls-operational', yang_type='uint32', is_config=False)


  def _get_outseg_index(self):
    """
    Getter method for outseg_index, mapped from YANG variable /mpls_state/route/outseg_index (uint32)

    YANG Description: Out segment index
    """
    return self.__outseg_index
      
  def _set_outseg_index(self, v, load=False):
    """
    Setter method for outseg_index, mapped from YANG variable /mpls_state/route/outseg_index (uint32)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_outseg_index is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_outseg_index() directly.

    YANG Description: Out segment index
    """
    if hasattr(v, "_utype"):
      v = v._utype(v)
    try:
      t = YANGDynClass(v,base=RestrictedClassType(base_type=long, restriction_dict={'range': ['0..4294967295']}, int_size=32), is_leaf=True, yang_name="outseg-index", rest_name="outseg-index", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='urn:brocade.com:mgmt:brocade-mpls-operational', defining_module='brocade-mpls-operational', yang_type='uint32', is_config=False)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """outseg_index must be of a type compatible with uint32""",
          'defined-type': "uint32",
          'generated-type': """YANGDynClass(base=RestrictedClassType(base_type=long, restriction_dict={'range': ['0..4294967295']}, int_size=32), is_leaf=True, yang_name="outseg-index", rest_name="outseg-index", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='urn:brocade.com:mgmt:brocade-mpls-operational', defining_module='brocade-mpls-operational', yang_type='uint32', is_config=False)""",
        })

    self.__outseg_index = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_outseg_index(self):
    self.__outseg_index = YANGDynClass(base=RestrictedClassType(base_type=long, restriction_dict={'range': ['0..4294967295']}, int_size=32), is_leaf=True, yang_name="outseg-index", rest_name="outseg-index", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='urn:brocade.com:mgmt:brocade-mpls-operational', defining_module='brocade-mpls-operational', yang_type='uint32', is_config=False)


  def _get_dest_ip_prefix(self):
    """
    Getter method for dest_ip_prefix, mapped from YANG variable /mpls_state/route/dest_ip_prefix (inet:ipv4-prefix)

    YANG Description: IP prefix of the destination
    """
    return self.__dest_ip_prefix
      
  def _set_dest_ip_prefix(self, v, load=False):
    """
    Setter method for dest_ip_prefix, mapped from YANG variable /mpls_state/route/dest_ip_prefix (inet:ipv4-prefix)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_dest_ip_prefix is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_dest_ip_prefix() directly.

    YANG Description: IP prefix of the destination
    """
    if hasattr(v, "_utype"):
      v = v._utype(v)
    try:
      t = YANGDynClass(v,base=RestrictedClassType(base_type=unicode, restriction_dict={'pattern': u'(([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])\\.){3}([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])/(([0-9])|([1-2][0-9])|(3[0-2]))'}), is_leaf=True, yang_name="dest-ip-prefix", rest_name="dest-ip-prefix", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='urn:brocade.com:mgmt:brocade-mpls-operational', defining_module='brocade-mpls-operational', yang_type='inet:ipv4-prefix', is_config=False)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """dest_ip_prefix must be of a type compatible with inet:ipv4-prefix""",
          'defined-type': "inet:ipv4-prefix",
          'generated-type': """YANGDynClass(base=RestrictedClassType(base_type=unicode, restriction_dict={'pattern': u'(([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])\\.){3}([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])/(([0-9])|([1-2][0-9])|(3[0-2]))'}), is_leaf=True, yang_name="dest-ip-prefix", rest_name="dest-ip-prefix", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='urn:brocade.com:mgmt:brocade-mpls-operational', defining_module='brocade-mpls-operational', yang_type='inet:ipv4-prefix', is_config=False)""",
        })

    self.__dest_ip_prefix = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_dest_ip_prefix(self):
    self.__dest_ip_prefix = YANGDynClass(base=RestrictedClassType(base_type=unicode, restriction_dict={'pattern': u'(([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])\\.){3}([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])/(([0-9])|([1-2][0-9])|(3[0-2]))'}), is_leaf=True, yang_name="dest-ip-prefix", rest_name="dest-ip-prefix", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='urn:brocade.com:mgmt:brocade-mpls-operational', defining_module='brocade-mpls-operational', yang_type='inet:ipv4-prefix', is_config=False)


  def _get_gateway_ip_addr(self):
    """
    Getter method for gateway_ip_addr, mapped from YANG variable /mpls_state/route/gateway_ip_addr (inet:ipv4-address)

    YANG Description: Gateway IP address
    """
    return self.__gateway_ip_addr
      
  def _set_gateway_ip_addr(self, v, load=False):
    """
    Setter method for gateway_ip_addr, mapped from YANG variable /mpls_state/route/gateway_ip_addr (inet:ipv4-address)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_gateway_ip_addr is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_gateway_ip_addr() directly.

    YANG Description: Gateway IP address
    """
    if hasattr(v, "_utype"):
      v = v._utype(v)
    try:
      t = YANGDynClass(v,base=RestrictedClassType(base_type=unicode, restriction_dict={'pattern': u'(([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])\\.){3}([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])(%[\\p{N}\\p{L}]+)?'}), is_leaf=True, yang_name="gateway-ip-addr", rest_name="gateway-ip-addr", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='urn:brocade.com:mgmt:brocade-mpls-operational', defining_module='brocade-mpls-operational', yang_type='inet:ipv4-address', is_config=False)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """gateway_ip_addr must be of a type compatible with inet:ipv4-address""",
          'defined-type': "inet:ipv4-address",
          'generated-type': """YANGDynClass(base=RestrictedClassType(base_type=unicode, restriction_dict={'pattern': u'(([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])\\.){3}([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])(%[\\p{N}\\p{L}]+)?'}), is_leaf=True, yang_name="gateway-ip-addr", rest_name="gateway-ip-addr", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='urn:brocade.com:mgmt:brocade-mpls-operational', defining_module='brocade-mpls-operational', yang_type='inet:ipv4-address', is_config=False)""",
        })

    self.__gateway_ip_addr = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_gateway_ip_addr(self):
    self.__gateway_ip_addr = YANGDynClass(base=RestrictedClassType(base_type=unicode, restriction_dict={'pattern': u'(([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])\\.){3}([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])(%[\\p{N}\\p{L}]+)?'}), is_leaf=True, yang_name="gateway-ip-addr", rest_name="gateway-ip-addr", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='urn:brocade.com:mgmt:brocade-mpls-operational', defining_module='brocade-mpls-operational', yang_type='inet:ipv4-address', is_config=False)


  def _get_out_interface_name(self):
    """
    Getter method for out_interface_name, mapped from YANG variable /mpls_state/route/out_interface_name (string)

    YANG Description: Outgoing interface name
    """
    return self.__out_interface_name
      
  def _set_out_interface_name(self, v, load=False):
    """
    Setter method for out_interface_name, mapped from YANG variable /mpls_state/route/out_interface_name (string)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_out_interface_name is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_out_interface_name() directly.

    YANG Description: Outgoing interface name
    """
    if hasattr(v, "_utype"):
      v = v._utype(v)
    try:
      t = YANGDynClass(v,base=unicode, is_leaf=True, yang_name="out-interface-name", rest_name="out-interface-name", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='urn:brocade.com:mgmt:brocade-mpls-operational', defining_module='brocade-mpls-operational', yang_type='string', is_config=False)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """out_interface_name must be of a type compatible with string""",
          'defined-type': "string",
          'generated-type': """YANGDynClass(base=unicode, is_leaf=True, yang_name="out-interface-name", rest_name="out-interface-name", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='urn:brocade.com:mgmt:brocade-mpls-operational', defining_module='brocade-mpls-operational', yang_type='string', is_config=False)""",
        })

    self.__out_interface_name = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_out_interface_name(self):
    self.__out_interface_name = YANGDynClass(base=unicode, is_leaf=True, yang_name="out-interface-name", rest_name="out-interface-name", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='urn:brocade.com:mgmt:brocade-mpls-operational', defining_module='brocade-mpls-operational', yang_type='string', is_config=False)


  def _get_out_label(self):
    """
    Getter method for out_label, mapped from YANG variable /mpls_state/route/out_label (uint32)

    YANG Description: Outgoing lebel
    """
    return self.__out_label
      
  def _set_out_label(self, v, load=False):
    """
    Setter method for out_label, mapped from YANG variable /mpls_state/route/out_label (uint32)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_out_label is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_out_label() directly.

    YANG Description: Outgoing lebel
    """
    if hasattr(v, "_utype"):
      v = v._utype(v)
    try:
      t = YANGDynClass(v,base=RestrictedClassType(base_type=long, restriction_dict={'range': ['0..4294967295']}, int_size=32), is_leaf=True, yang_name="out-label", rest_name="out-label", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='urn:brocade.com:mgmt:brocade-mpls-operational', defining_module='brocade-mpls-operational', yang_type='uint32', is_config=False)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """out_label must be of a type compatible with uint32""",
          'defined-type': "uint32",
          'generated-type': """YANGDynClass(base=RestrictedClassType(base_type=long, restriction_dict={'range': ['0..4294967295']}, int_size=32), is_leaf=True, yang_name="out-label", rest_name="out-label", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='urn:brocade.com:mgmt:brocade-mpls-operational', defining_module='brocade-mpls-operational', yang_type='uint32', is_config=False)""",
        })

    self.__out_label = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_out_label(self):
    self.__out_label = YANGDynClass(base=RestrictedClassType(base_type=long, restriction_dict={'range': ['0..4294967295']}, int_size=32), is_leaf=True, yang_name="out-label", rest_name="out-label", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='urn:brocade.com:mgmt:brocade-mpls-operational', defining_module='brocade-mpls-operational', yang_type='uint32', is_config=False)


  def _get_protocol(self):
    """
    Getter method for protocol, mapped from YANG variable /mpls_state/route/protocol (mpls-protocol)

    YANG Description: MPLS protocol
    """
    return self.__protocol
      
  def _set_protocol(self, v, load=False):
    """
    Setter method for protocol, mapped from YANG variable /mpls_state/route/protocol (mpls-protocol)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_protocol is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_protocol() directly.

    YANG Description: MPLS protocol
    """
    if hasattr(v, "_utype"):
      v = v._utype(v)
    try:
      t = YANGDynClass(v,base=RestrictedClassType(base_type=unicode,                                     restriction_type="dict_key",                                     restriction_arg={u'mpls-protocol-none': {'value': 0}, u'mpls-protocol-ldp': {'value': 1}, u'mpls-protocol-rsvp': {'value': 2}},), is_leaf=True, yang_name="protocol", rest_name="protocol", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='urn:brocade.com:mgmt:brocade-mpls-operational', defining_module='brocade-mpls-operational', yang_type='mpls-protocol', is_config=False)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """protocol must be of a type compatible with mpls-protocol""",
          'defined-type': "brocade-mpls-operational:mpls-protocol",
          'generated-type': """YANGDynClass(base=RestrictedClassType(base_type=unicode,                                     restriction_type="dict_key",                                     restriction_arg={u'mpls-protocol-none': {'value': 0}, u'mpls-protocol-ldp': {'value': 1}, u'mpls-protocol-rsvp': {'value': 2}},), is_leaf=True, yang_name="protocol", rest_name="protocol", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='urn:brocade.com:mgmt:brocade-mpls-operational', defining_module='brocade-mpls-operational', yang_type='mpls-protocol', is_config=False)""",
        })

    self.__protocol = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_protocol(self):
    self.__protocol = YANGDynClass(base=RestrictedClassType(base_type=unicode,                                     restriction_type="dict_key",                                     restriction_arg={u'mpls-protocol-none': {'value': 0}, u'mpls-protocol-ldp': {'value': 1}, u'mpls-protocol-rsvp': {'value': 2}},), is_leaf=True, yang_name="protocol", rest_name="protocol", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='urn:brocade.com:mgmt:brocade-mpls-operational', defining_module='brocade-mpls-operational', yang_type='mpls-protocol', is_config=False)


  def _get_vif_index(self):
    """
    Getter method for vif_index, mapped from YANG variable /mpls_state/route/vif_index (uint32)

    YANG Description: Virtual interface index
    """
    return self.__vif_index
      
  def _set_vif_index(self, v, load=False):
    """
    Setter method for vif_index, mapped from YANG variable /mpls_state/route/vif_index (uint32)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_vif_index is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_vif_index() directly.

    YANG Description: Virtual interface index
    """
    if hasattr(v, "_utype"):
      v = v._utype(v)
    try:
      t = YANGDynClass(v,base=RestrictedClassType(base_type=long, restriction_dict={'range': ['0..4294967295']}, int_size=32), is_leaf=True, yang_name="vif-index", rest_name="vif-index", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='urn:brocade.com:mgmt:brocade-mpls-operational', defining_module='brocade-mpls-operational', yang_type='uint32', is_config=False)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """vif_index must be of a type compatible with uint32""",
          'defined-type': "uint32",
          'generated-type': """YANGDynClass(base=RestrictedClassType(base_type=long, restriction_dict={'range': ['0..4294967295']}, int_size=32), is_leaf=True, yang_name="vif-index", rest_name="vif-index", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='urn:brocade.com:mgmt:brocade-mpls-operational', defining_module='brocade-mpls-operational', yang_type='uint32', is_config=False)""",
        })

    self.__vif_index = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_vif_index(self):
    self.__vif_index = YANGDynClass(base=RestrictedClassType(base_type=long, restriction_dict={'range': ['0..4294967295']}, int_size=32), is_leaf=True, yang_name="vif-index", rest_name="vif-index", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='urn:brocade.com:mgmt:brocade-mpls-operational', defining_module='brocade-mpls-operational', yang_type='uint32', is_config=False)


  def _get_metric(self):
    """
    Getter method for metric, mapped from YANG variable /mpls_state/route/metric (uint32)

    YANG Description: Interface metric
    """
    return self.__metric
      
  def _set_metric(self, v, load=False):
    """
    Setter method for metric, mapped from YANG variable /mpls_state/route/metric (uint32)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_metric is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_metric() directly.

    YANG Description: Interface metric
    """
    if hasattr(v, "_utype"):
      v = v._utype(v)
    try:
      t = YANGDynClass(v,base=RestrictedClassType(base_type=long, restriction_dict={'range': ['0..4294967295']}, int_size=32), is_leaf=True, yang_name="metric", rest_name="metric", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='urn:brocade.com:mgmt:brocade-mpls-operational', defining_module='brocade-mpls-operational', yang_type='uint32', is_config=False)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """metric must be of a type compatible with uint32""",
          'defined-type': "uint32",
          'generated-type': """YANGDynClass(base=RestrictedClassType(base_type=long, restriction_dict={'range': ['0..4294967295']}, int_size=32), is_leaf=True, yang_name="metric", rest_name="metric", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='urn:brocade.com:mgmt:brocade-mpls-operational', defining_module='brocade-mpls-operational', yang_type='uint32', is_config=False)""",
        })

    self.__metric = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_metric(self):
    self.__metric = YANGDynClass(base=RestrictedClassType(base_type=long, restriction_dict={'range': ['0..4294967295']}, int_size=32), is_leaf=True, yang_name="metric", rest_name="metric", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='urn:brocade.com:mgmt:brocade-mpls-operational', defining_module='brocade-mpls-operational', yang_type='uint32', is_config=False)


  def _get_use_count(self):
    """
    Getter method for use_count, mapped from YANG variable /mpls_state/route/use_count (uint32)

    YANG Description: Use count
    """
    return self.__use_count
      
  def _set_use_count(self, v, load=False):
    """
    Setter method for use_count, mapped from YANG variable /mpls_state/route/use_count (uint32)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_use_count is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_use_count() directly.

    YANG Description: Use count
    """
    if hasattr(v, "_utype"):
      v = v._utype(v)
    try:
      t = YANGDynClass(v,base=RestrictedClassType(base_type=long, restriction_dict={'range': ['0..4294967295']}, int_size=32), is_leaf=True, yang_name="use-count", rest_name="use-count", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='urn:brocade.com:mgmt:brocade-mpls-operational', defining_module='brocade-mpls-operational', yang_type='uint32', is_config=False)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """use_count must be of a type compatible with uint32""",
          'defined-type': "uint32",
          'generated-type': """YANGDynClass(base=RestrictedClassType(base_type=long, restriction_dict={'range': ['0..4294967295']}, int_size=32), is_leaf=True, yang_name="use-count", rest_name="use-count", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='urn:brocade.com:mgmt:brocade-mpls-operational', defining_module='brocade-mpls-operational', yang_type='uint32', is_config=False)""",
        })

    self.__use_count = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_use_count(self):
    self.__use_count = YANGDynClass(base=RestrictedClassType(base_type=long, restriction_dict={'range': ['0..4294967295']}, int_size=32), is_leaf=True, yang_name="use-count", rest_name="use-count", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='urn:brocade.com:mgmt:brocade-mpls-operational', defining_module='brocade-mpls-operational', yang_type='uint32', is_config=False)

  entry_index = __builtin__.property(_get_entry_index)
  outseg_index = __builtin__.property(_get_outseg_index)
  dest_ip_prefix = __builtin__.property(_get_dest_ip_prefix)
  gateway_ip_addr = __builtin__.property(_get_gateway_ip_addr)
  out_interface_name = __builtin__.property(_get_out_interface_name)
  out_label = __builtin__.property(_get_out_label)
  protocol = __builtin__.property(_get_protocol)
  vif_index = __builtin__.property(_get_vif_index)
  metric = __builtin__.property(_get_metric)
  use_count = __builtin__.property(_get_use_count)


  _pyangbind_elements = {'entry_index': entry_index, 'outseg_index': outseg_index, 'dest_ip_prefix': dest_ip_prefix, 'gateway_ip_addr': gateway_ip_addr, 'out_interface_name': out_interface_name, 'out_label': out_label, 'protocol': protocol, 'vif_index': vif_index, 'metric': metric, 'use_count': use_count, }


