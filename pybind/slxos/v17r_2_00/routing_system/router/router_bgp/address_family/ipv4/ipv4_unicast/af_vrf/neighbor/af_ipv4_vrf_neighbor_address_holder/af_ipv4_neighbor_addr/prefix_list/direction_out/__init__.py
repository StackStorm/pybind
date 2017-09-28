
from operator import attrgetter
import pyangbind.lib.xpathhelper as xpathhelper
from pyangbind.lib.yangtypes import RestrictedPrecisionDecimalType, RestrictedClassType, TypedListType
from pyangbind.lib.yangtypes import YANGBool, YANGListType, YANGDynClass, ReferenceType
from pyangbind.lib.base import PybindBase
from decimal import Decimal
from bitarray import bitarray
import __builtin__
class direction_out(PybindBase):
  """
  This class was auto-generated by the PythonClass plugin for PYANG
  from YANG module brocade-common-def - based on the path /routing-system/router/router-bgp/address-family/ipv4/ipv4-unicast/af-vrf/neighbor/af-ipv4-vrf-neighbor-address-holder/af-ipv4-neighbor-addr/prefix-list/direction-out. Each member element of
  the container is represented as a class variable - with a specific
  YANG type.
  """
  __slots__ = ('_pybind_generated_by', '_path_helper', '_yang_name', '_rest_name', '_extmethods', '__prefix_list_direction_out_prefix_name','__prefix_list_direction_out',)

  _yang_name = 'direction-out'
  _rest_name = ''

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
    self.__prefix_list_direction_out = YANGDynClass(base=YANGBool, is_leaf=True, yang_name="prefix-list-direction-out", rest_name="out", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'info': u'Filter outgoing routes', u'alt-name': u'out'}}, namespace='urn:brocade.com:mgmt:brocade-bgp', defining_module='brocade-bgp', yang_type='empty', is_config=True)
    self.__prefix_list_direction_out_prefix_name = YANGDynClass(base=RestrictedClassType(base_type=unicode, restriction_dict={'length': [u'1..63']}), is_leaf=True, yang_name="prefix-list-direction-out-prefix-name", rest_name="prefix-list-direction-out-prefix-name", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'cli-drop-node-name': None, u'cli-incomplete-no': None, u'cli-incomplete-command': None}}, namespace='urn:brocade.com:mgmt:brocade-bgp', defining_module='brocade-bgp', yang_type='nei-prefix-list-filter', is_config=True)

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
      return [u'routing-system', u'router', u'router-bgp', u'address-family', u'ipv4', u'ipv4-unicast', u'af-vrf', u'neighbor', u'af-ipv4-vrf-neighbor-address-holder', u'af-ipv4-neighbor-addr', u'prefix-list', u'direction-out']

  def _rest_path(self):
    if hasattr(self, "_parent"):
      if self._rest_name:
        return self._parent._rest_path()+[self._rest_name]
      else:
        return self._parent._rest_path()
    else:
      return [u'router', u'bgp', u'address-family', u'ipv4', u'unicast', u'vrf', u'neighbor', u'af-ipv4-neighbor-addr', u'prefix-list']

  def _get_prefix_list_direction_out_prefix_name(self):
    """
    Getter method for prefix_list_direction_out_prefix_name, mapped from YANG variable /routing_system/router/router_bgp/address_family/ipv4/ipv4_unicast/af_vrf/neighbor/af_ipv4_vrf_neighbor_address_holder/af_ipv4_neighbor_addr/prefix_list/direction_out/prefix_list_direction_out_prefix_name (nei-prefix-list-filter)
    """
    return self.__prefix_list_direction_out_prefix_name
      
  def _set_prefix_list_direction_out_prefix_name(self, v, load=False):
    """
    Setter method for prefix_list_direction_out_prefix_name, mapped from YANG variable /routing_system/router/router_bgp/address_family/ipv4/ipv4_unicast/af_vrf/neighbor/af_ipv4_vrf_neighbor_address_holder/af_ipv4_neighbor_addr/prefix_list/direction_out/prefix_list_direction_out_prefix_name (nei-prefix-list-filter)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_prefix_list_direction_out_prefix_name is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_prefix_list_direction_out_prefix_name() directly.
    """
    if hasattr(v, "_utype"):
      v = v._utype(v)
    try:
      t = YANGDynClass(v,base=RestrictedClassType(base_type=unicode, restriction_dict={'length': [u'1..63']}), is_leaf=True, yang_name="prefix-list-direction-out-prefix-name", rest_name="prefix-list-direction-out-prefix-name", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'cli-drop-node-name': None, u'cli-incomplete-no': None, u'cli-incomplete-command': None}}, namespace='urn:brocade.com:mgmt:brocade-bgp', defining_module='brocade-bgp', yang_type='nei-prefix-list-filter', is_config=True)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """prefix_list_direction_out_prefix_name must be of a type compatible with nei-prefix-list-filter""",
          'defined-type': "brocade-bgp:nei-prefix-list-filter",
          'generated-type': """YANGDynClass(base=RestrictedClassType(base_type=unicode, restriction_dict={'length': [u'1..63']}), is_leaf=True, yang_name="prefix-list-direction-out-prefix-name", rest_name="prefix-list-direction-out-prefix-name", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'cli-drop-node-name': None, u'cli-incomplete-no': None, u'cli-incomplete-command': None}}, namespace='urn:brocade.com:mgmt:brocade-bgp', defining_module='brocade-bgp', yang_type='nei-prefix-list-filter', is_config=True)""",
        })

    self.__prefix_list_direction_out_prefix_name = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_prefix_list_direction_out_prefix_name(self):
    self.__prefix_list_direction_out_prefix_name = YANGDynClass(base=RestrictedClassType(base_type=unicode, restriction_dict={'length': [u'1..63']}), is_leaf=True, yang_name="prefix-list-direction-out-prefix-name", rest_name="prefix-list-direction-out-prefix-name", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'cli-drop-node-name': None, u'cli-incomplete-no': None, u'cli-incomplete-command': None}}, namespace='urn:brocade.com:mgmt:brocade-bgp', defining_module='brocade-bgp', yang_type='nei-prefix-list-filter', is_config=True)


  def _get_prefix_list_direction_out(self):
    """
    Getter method for prefix_list_direction_out, mapped from YANG variable /routing_system/router/router_bgp/address_family/ipv4/ipv4_unicast/af_vrf/neighbor/af_ipv4_vrf_neighbor_address_holder/af_ipv4_neighbor_addr/prefix_list/direction_out/prefix_list_direction_out (empty)
    """
    return self.__prefix_list_direction_out
      
  def _set_prefix_list_direction_out(self, v, load=False):
    """
    Setter method for prefix_list_direction_out, mapped from YANG variable /routing_system/router/router_bgp/address_family/ipv4/ipv4_unicast/af_vrf/neighbor/af_ipv4_vrf_neighbor_address_holder/af_ipv4_neighbor_addr/prefix_list/direction_out/prefix_list_direction_out (empty)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_prefix_list_direction_out is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_prefix_list_direction_out() directly.
    """
    if hasattr(v, "_utype"):
      v = v._utype(v)
    try:
      t = YANGDynClass(v,base=YANGBool, is_leaf=True, yang_name="prefix-list-direction-out", rest_name="out", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'info': u'Filter outgoing routes', u'alt-name': u'out'}}, namespace='urn:brocade.com:mgmt:brocade-bgp', defining_module='brocade-bgp', yang_type='empty', is_config=True)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """prefix_list_direction_out must be of a type compatible with empty""",
          'defined-type': "empty",
          'generated-type': """YANGDynClass(base=YANGBool, is_leaf=True, yang_name="prefix-list-direction-out", rest_name="out", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'info': u'Filter outgoing routes', u'alt-name': u'out'}}, namespace='urn:brocade.com:mgmt:brocade-bgp', defining_module='brocade-bgp', yang_type='empty', is_config=True)""",
        })

    self.__prefix_list_direction_out = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_prefix_list_direction_out(self):
    self.__prefix_list_direction_out = YANGDynClass(base=YANGBool, is_leaf=True, yang_name="prefix-list-direction-out", rest_name="out", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'info': u'Filter outgoing routes', u'alt-name': u'out'}}, namespace='urn:brocade.com:mgmt:brocade-bgp', defining_module='brocade-bgp', yang_type='empty', is_config=True)

  prefix_list_direction_out_prefix_name = __builtin__.property(_get_prefix_list_direction_out_prefix_name, _set_prefix_list_direction_out_prefix_name)
  prefix_list_direction_out = __builtin__.property(_get_prefix_list_direction_out, _set_prefix_list_direction_out)


  _pyangbind_elements = {'prefix_list_direction_out_prefix_name': prefix_list_direction_out_prefix_name, 'prefix_list_direction_out': prefix_list_direction_out, }

