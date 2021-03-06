
from operator import attrgetter
import pyangbind.lib.xpathhelper as xpathhelper
from pyangbind.lib.yangtypes import RestrictedPrecisionDecimalType, RestrictedClassType, TypedListType
from pyangbind.lib.yangtypes import YANGBool, YANGListType, YANGDynClass, ReferenceType
from pyangbind.lib.base import PybindBase
from decimal import Decimal
from bitarray import bitarray
import __builtin__
import neighbor
class ldp_neighbors(PybindBase):
  """
  This class was auto-generated by the PythonClass plugin for PYANG
  from YANG module brocade-mpls-operational - based on the path /mpls-state/ldp/ldp-neighbors. Each member element of
  the container is represented as a class variable - with a specific
  YANG type.

  YANG Description: LDP neighbors information
  """
  __slots__ = ('_pybind_generated_by', '_path_helper', '_yang_name', '_rest_name', '_extmethods', '__num_link_neighbors','__num_targeted_neighbors','__neighbor',)

  _yang_name = 'ldp-neighbors'
  _rest_name = 'ldp-neighbors'

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
    self.__num_link_neighbors = YANGDynClass(base=RestrictedClassType(base_type=long, restriction_dict={'range': ['0..4294967295']}, int_size=32), is_leaf=True, yang_name="num-link-neighbors", rest_name="num-link-neighbors", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='urn:brocade.com:mgmt:brocade-mpls-operational', defining_module='brocade-mpls-operational', yang_type='uint32', is_config=False)
    self.__num_targeted_neighbors = YANGDynClass(base=RestrictedClassType(base_type=long, restriction_dict={'range': ['0..4294967295']}, int_size=32), is_leaf=True, yang_name="num-targeted-neighbors", rest_name="num-targeted-neighbors", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='urn:brocade.com:mgmt:brocade-mpls-operational', defining_module='brocade-mpls-operational', yang_type='uint32', is_config=False)
    self.__neighbor = YANGDynClass(base=YANGListType("neighbor_ldpid labelspaceid",neighbor.neighbor, yang_name="neighbor", rest_name="neighbor", parent=self, is_container='list', user_ordered=False, path_helper=self._path_helper, yang_keys='neighbor-ldpid labelspaceid', extensions={u'tailf-common': {u'callpoint': u'mpls-ldp-neighbor', u'cli-suppress-show-path': None}}), is_container='list', yang_name="neighbor", rest_name="neighbor", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'callpoint': u'mpls-ldp-neighbor', u'cli-suppress-show-path': None}}, namespace='urn:brocade.com:mgmt:brocade-mpls-operational', defining_module='brocade-mpls-operational', yang_type='list', is_config=False)

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
      return [u'mpls-state', u'ldp', u'ldp-neighbors']

  def _rest_path(self):
    if hasattr(self, "_parent"):
      if self._rest_name:
        return self._parent._rest_path()+[self._rest_name]
      else:
        return self._parent._rest_path()
    else:
      return [u'mpls-state', u'ldp', u'ldp-neighbors']

  def _get_num_link_neighbors(self):
    """
    Getter method for num_link_neighbors, mapped from YANG variable /mpls_state/ldp/ldp_neighbors/num_link_neighbors (uint32)

    YANG Description: Number of link neighbors
    """
    return self.__num_link_neighbors
      
  def _set_num_link_neighbors(self, v, load=False):
    """
    Setter method for num_link_neighbors, mapped from YANG variable /mpls_state/ldp/ldp_neighbors/num_link_neighbors (uint32)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_num_link_neighbors is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_num_link_neighbors() directly.

    YANG Description: Number of link neighbors
    """
    if hasattr(v, "_utype"):
      v = v._utype(v)
    try:
      t = YANGDynClass(v,base=RestrictedClassType(base_type=long, restriction_dict={'range': ['0..4294967295']}, int_size=32), is_leaf=True, yang_name="num-link-neighbors", rest_name="num-link-neighbors", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='urn:brocade.com:mgmt:brocade-mpls-operational', defining_module='brocade-mpls-operational', yang_type='uint32', is_config=False)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """num_link_neighbors must be of a type compatible with uint32""",
          'defined-type': "uint32",
          'generated-type': """YANGDynClass(base=RestrictedClassType(base_type=long, restriction_dict={'range': ['0..4294967295']}, int_size=32), is_leaf=True, yang_name="num-link-neighbors", rest_name="num-link-neighbors", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='urn:brocade.com:mgmt:brocade-mpls-operational', defining_module='brocade-mpls-operational', yang_type='uint32', is_config=False)""",
        })

    self.__num_link_neighbors = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_num_link_neighbors(self):
    self.__num_link_neighbors = YANGDynClass(base=RestrictedClassType(base_type=long, restriction_dict={'range': ['0..4294967295']}, int_size=32), is_leaf=True, yang_name="num-link-neighbors", rest_name="num-link-neighbors", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='urn:brocade.com:mgmt:brocade-mpls-operational', defining_module='brocade-mpls-operational', yang_type='uint32', is_config=False)


  def _get_num_targeted_neighbors(self):
    """
    Getter method for num_targeted_neighbors, mapped from YANG variable /mpls_state/ldp/ldp_neighbors/num_targeted_neighbors (uint32)

    YANG Description: Number of targeted neighbors
    """
    return self.__num_targeted_neighbors
      
  def _set_num_targeted_neighbors(self, v, load=False):
    """
    Setter method for num_targeted_neighbors, mapped from YANG variable /mpls_state/ldp/ldp_neighbors/num_targeted_neighbors (uint32)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_num_targeted_neighbors is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_num_targeted_neighbors() directly.

    YANG Description: Number of targeted neighbors
    """
    if hasattr(v, "_utype"):
      v = v._utype(v)
    try:
      t = YANGDynClass(v,base=RestrictedClassType(base_type=long, restriction_dict={'range': ['0..4294967295']}, int_size=32), is_leaf=True, yang_name="num-targeted-neighbors", rest_name="num-targeted-neighbors", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='urn:brocade.com:mgmt:brocade-mpls-operational', defining_module='brocade-mpls-operational', yang_type='uint32', is_config=False)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """num_targeted_neighbors must be of a type compatible with uint32""",
          'defined-type': "uint32",
          'generated-type': """YANGDynClass(base=RestrictedClassType(base_type=long, restriction_dict={'range': ['0..4294967295']}, int_size=32), is_leaf=True, yang_name="num-targeted-neighbors", rest_name="num-targeted-neighbors", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='urn:brocade.com:mgmt:brocade-mpls-operational', defining_module='brocade-mpls-operational', yang_type='uint32', is_config=False)""",
        })

    self.__num_targeted_neighbors = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_num_targeted_neighbors(self):
    self.__num_targeted_neighbors = YANGDynClass(base=RestrictedClassType(base_type=long, restriction_dict={'range': ['0..4294967295']}, int_size=32), is_leaf=True, yang_name="num-targeted-neighbors", rest_name="num-targeted-neighbors", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='urn:brocade.com:mgmt:brocade-mpls-operational', defining_module='brocade-mpls-operational', yang_type='uint32', is_config=False)


  def _get_neighbor(self):
    """
    Getter method for neighbor, mapped from YANG variable /mpls_state/ldp/ldp_neighbors/neighbor (list)

    YANG Description: LDP neighbor details
    """
    return self.__neighbor
      
  def _set_neighbor(self, v, load=False):
    """
    Setter method for neighbor, mapped from YANG variable /mpls_state/ldp/ldp_neighbors/neighbor (list)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_neighbor is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_neighbor() directly.

    YANG Description: LDP neighbor details
    """
    if hasattr(v, "_utype"):
      v = v._utype(v)
    try:
      t = YANGDynClass(v,base=YANGListType("neighbor_ldpid labelspaceid",neighbor.neighbor, yang_name="neighbor", rest_name="neighbor", parent=self, is_container='list', user_ordered=False, path_helper=self._path_helper, yang_keys='neighbor-ldpid labelspaceid', extensions={u'tailf-common': {u'callpoint': u'mpls-ldp-neighbor', u'cli-suppress-show-path': None}}), is_container='list', yang_name="neighbor", rest_name="neighbor", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'callpoint': u'mpls-ldp-neighbor', u'cli-suppress-show-path': None}}, namespace='urn:brocade.com:mgmt:brocade-mpls-operational', defining_module='brocade-mpls-operational', yang_type='list', is_config=False)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """neighbor must be of a type compatible with list""",
          'defined-type': "list",
          'generated-type': """YANGDynClass(base=YANGListType("neighbor_ldpid labelspaceid",neighbor.neighbor, yang_name="neighbor", rest_name="neighbor", parent=self, is_container='list', user_ordered=False, path_helper=self._path_helper, yang_keys='neighbor-ldpid labelspaceid', extensions={u'tailf-common': {u'callpoint': u'mpls-ldp-neighbor', u'cli-suppress-show-path': None}}), is_container='list', yang_name="neighbor", rest_name="neighbor", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'callpoint': u'mpls-ldp-neighbor', u'cli-suppress-show-path': None}}, namespace='urn:brocade.com:mgmt:brocade-mpls-operational', defining_module='brocade-mpls-operational', yang_type='list', is_config=False)""",
        })

    self.__neighbor = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_neighbor(self):
    self.__neighbor = YANGDynClass(base=YANGListType("neighbor_ldpid labelspaceid",neighbor.neighbor, yang_name="neighbor", rest_name="neighbor", parent=self, is_container='list', user_ordered=False, path_helper=self._path_helper, yang_keys='neighbor-ldpid labelspaceid', extensions={u'tailf-common': {u'callpoint': u'mpls-ldp-neighbor', u'cli-suppress-show-path': None}}), is_container='list', yang_name="neighbor", rest_name="neighbor", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'callpoint': u'mpls-ldp-neighbor', u'cli-suppress-show-path': None}}, namespace='urn:brocade.com:mgmt:brocade-mpls-operational', defining_module='brocade-mpls-operational', yang_type='list', is_config=False)

  num_link_neighbors = __builtin__.property(_get_num_link_neighbors)
  num_targeted_neighbors = __builtin__.property(_get_num_targeted_neighbors)
  neighbor = __builtin__.property(_get_neighbor)


  _pyangbind_elements = {'num_link_neighbors': num_link_neighbors, 'num_targeted_neighbors': num_targeted_neighbors, 'neighbor': neighbor, }


