
from operator import attrgetter
import pyangbind.lib.xpathhelper as xpathhelper
from pyangbind.lib.yangtypes import RestrictedPrecisionDecimalType, RestrictedClassType, TypedListType
from pyangbind.lib.yangtypes import YANGBool, YANGListType, YANGDynClass, ReferenceType
from pyangbind.lib.base import PybindBase
from decimal import Decimal
from bitarray import bitarray
import __builtin__
class in_(PybindBase):
  """
  This class was auto-generated by the PythonClass plugin for PYANG
  from YANG module brocade-common-def - based on the path /routing-system/router/router-bgp/address-family/ipv4/ipv4-unicast/af-vrf/neighbor/af-ipv4-vrf-neighbor-address-holder/af-ipv4-neighbor-addr/maxas-limit/in. Each member element of
  the container is represented as a class variable - with a specific
  YANG type.
  """
  __slots__ = ('_pybind_generated_by', '_path_helper', '_yang_name', '_rest_name', '_extmethods', '__num_as_in_as_path','__maxas_limit_disable',)

  _yang_name = 'in'
  _rest_name = 'in'

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
    self.__maxas_limit_disable = YANGDynClass(base=YANGBool, is_leaf=True, yang_name="maxas-limit-disable", rest_name="disable", parent=self, choice=(u'ch-maxas-limit', u'ca-maxas-limit-disable'), path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'info': u'Disable maxas-limit', u'alt-name': u'disable'}}, namespace='urn:brocade.com:mgmt:brocade-bgp', defining_module='brocade-bgp', yang_type='empty', is_config=True)
    self.__num_as_in_as_path = YANGDynClass(base=RestrictedClassType(base_type=RestrictedClassType(base_type=long, restriction_dict={'range': ['0..4294967295']}, int_size=32), restriction_dict={'range': [u'0..300']}), is_leaf=True, yang_name="num-as-in-as-path", rest_name="", parent=self, choice=(u'ch-maxas-limit', u'ca-maxas-limit-enable'), path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'cli-drop-node-name': None}}, namespace='urn:brocade.com:mgmt:brocade-bgp', defining_module='brocade-bgp', yang_type='num-as-in-as-path', is_config=True)

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
      return [u'routing-system', u'router', u'router-bgp', u'address-family', u'ipv4', u'ipv4-unicast', u'af-vrf', u'neighbor', u'af-ipv4-vrf-neighbor-address-holder', u'af-ipv4-neighbor-addr', u'maxas-limit', u'in']

  def _rest_path(self):
    if hasattr(self, "_parent"):
      if self._rest_name:
        return self._parent._rest_path()+[self._rest_name]
      else:
        return self._parent._rest_path()
    else:
      return [u'router', u'bgp', u'address-family', u'ipv4', u'unicast', u'vrf', u'neighbor', u'maxas-limit', u'in']

  def _get_num_as_in_as_path(self):
    """
    Getter method for num_as_in_as_path, mapped from YANG variable /routing_system/router/router_bgp/address_family/ipv4/ipv4_unicast/af_vrf/neighbor/af_ipv4_vrf_neighbor_address_holder/af_ipv4_neighbor_addr/maxas_limit/in/num_as_in_as_path (num-as-in-as-path)
    """
    return self.__num_as_in_as_path
      
  def _set_num_as_in_as_path(self, v, load=False):
    """
    Setter method for num_as_in_as_path, mapped from YANG variable /routing_system/router/router_bgp/address_family/ipv4/ipv4_unicast/af_vrf/neighbor/af_ipv4_vrf_neighbor_address_holder/af_ipv4_neighbor_addr/maxas_limit/in/num_as_in_as_path (num-as-in-as-path)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_num_as_in_as_path is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_num_as_in_as_path() directly.
    """
    if hasattr(v, "_utype"):
      v = v._utype(v)
    try:
      t = YANGDynClass(v,base=RestrictedClassType(base_type=RestrictedClassType(base_type=long, restriction_dict={'range': ['0..4294967295']}, int_size=32), restriction_dict={'range': [u'0..300']}), is_leaf=True, yang_name="num-as-in-as-path", rest_name="", parent=self, choice=(u'ch-maxas-limit', u'ca-maxas-limit-enable'), path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'cli-drop-node-name': None}}, namespace='urn:brocade.com:mgmt:brocade-bgp', defining_module='brocade-bgp', yang_type='num-as-in-as-path', is_config=True)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """num_as_in_as_path must be of a type compatible with num-as-in-as-path""",
          'defined-type': "brocade-bgp:num-as-in-as-path",
          'generated-type': """YANGDynClass(base=RestrictedClassType(base_type=RestrictedClassType(base_type=long, restriction_dict={'range': ['0..4294967295']}, int_size=32), restriction_dict={'range': [u'0..300']}), is_leaf=True, yang_name="num-as-in-as-path", rest_name="", parent=self, choice=(u'ch-maxas-limit', u'ca-maxas-limit-enable'), path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'cli-drop-node-name': None}}, namespace='urn:brocade.com:mgmt:brocade-bgp', defining_module='brocade-bgp', yang_type='num-as-in-as-path', is_config=True)""",
        })

    self.__num_as_in_as_path = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_num_as_in_as_path(self):
    self.__num_as_in_as_path = YANGDynClass(base=RestrictedClassType(base_type=RestrictedClassType(base_type=long, restriction_dict={'range': ['0..4294967295']}, int_size=32), restriction_dict={'range': [u'0..300']}), is_leaf=True, yang_name="num-as-in-as-path", rest_name="", parent=self, choice=(u'ch-maxas-limit', u'ca-maxas-limit-enable'), path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'cli-drop-node-name': None}}, namespace='urn:brocade.com:mgmt:brocade-bgp', defining_module='brocade-bgp', yang_type='num-as-in-as-path', is_config=True)


  def _get_maxas_limit_disable(self):
    """
    Getter method for maxas_limit_disable, mapped from YANG variable /routing_system/router/router_bgp/address_family/ipv4/ipv4_unicast/af_vrf/neighbor/af_ipv4_vrf_neighbor_address_holder/af_ipv4_neighbor_addr/maxas_limit/in/maxas_limit_disable (empty)
    """
    return self.__maxas_limit_disable
      
  def _set_maxas_limit_disable(self, v, load=False):
    """
    Setter method for maxas_limit_disable, mapped from YANG variable /routing_system/router/router_bgp/address_family/ipv4/ipv4_unicast/af_vrf/neighbor/af_ipv4_vrf_neighbor_address_holder/af_ipv4_neighbor_addr/maxas_limit/in/maxas_limit_disable (empty)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_maxas_limit_disable is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_maxas_limit_disable() directly.
    """
    if hasattr(v, "_utype"):
      v = v._utype(v)
    try:
      t = YANGDynClass(v,base=YANGBool, is_leaf=True, yang_name="maxas-limit-disable", rest_name="disable", parent=self, choice=(u'ch-maxas-limit', u'ca-maxas-limit-disable'), path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'info': u'Disable maxas-limit', u'alt-name': u'disable'}}, namespace='urn:brocade.com:mgmt:brocade-bgp', defining_module='brocade-bgp', yang_type='empty', is_config=True)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """maxas_limit_disable must be of a type compatible with empty""",
          'defined-type': "empty",
          'generated-type': """YANGDynClass(base=YANGBool, is_leaf=True, yang_name="maxas-limit-disable", rest_name="disable", parent=self, choice=(u'ch-maxas-limit', u'ca-maxas-limit-disable'), path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'info': u'Disable maxas-limit', u'alt-name': u'disable'}}, namespace='urn:brocade.com:mgmt:brocade-bgp', defining_module='brocade-bgp', yang_type='empty', is_config=True)""",
        })

    self.__maxas_limit_disable = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_maxas_limit_disable(self):
    self.__maxas_limit_disable = YANGDynClass(base=YANGBool, is_leaf=True, yang_name="maxas-limit-disable", rest_name="disable", parent=self, choice=(u'ch-maxas-limit', u'ca-maxas-limit-disable'), path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'info': u'Disable maxas-limit', u'alt-name': u'disable'}}, namespace='urn:brocade.com:mgmt:brocade-bgp', defining_module='brocade-bgp', yang_type='empty', is_config=True)

  num_as_in_as_path = __builtin__.property(_get_num_as_in_as_path, _set_num_as_in_as_path)
  maxas_limit_disable = __builtin__.property(_get_maxas_limit_disable, _set_maxas_limit_disable)

  __choices__ = {u'ch-maxas-limit': {u'ca-maxas-limit-enable': [u'num_as_in_as_path'], u'ca-maxas-limit-disable': [u'maxas_limit_disable']}}
  _pyangbind_elements = {'num_as_in_as_path': num_as_in_as_path, 'maxas_limit_disable': maxas_limit_disable, }


