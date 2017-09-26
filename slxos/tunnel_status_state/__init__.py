
from operator import attrgetter
import pyangbind.lib.xpathhelper as xpathhelper
from pyangbind.lib.yangtypes import RestrictedPrecisionDecimalType, RestrictedClassType, TypedListType
from pyangbind.lib.yangtypes import YANGBool, YANGListType, YANGDynClass, ReferenceType
from pyangbind.lib.base import PybindBase
from decimal import Decimal
from bitarray import bitarray
import __builtin__
class tunnel_status_state(PybindBase):
  """
  This class was auto-generated by the PythonClass plugin for PYANG
  from YANG module brocade-mpls-operational - based on the path /tunnel-status-state. Each member element of
  the container is represented as a class variable - with a specific
  YANG type.

  YANG Description: MPLS Tunnel Status
  """
  __slots__ = ('_pybind_generated_by', '_path_helper', '_yang_name', '_rest_name', '_extmethods', '__tunnel_destination','__oper_status',)

  _yang_name = 'tunnel-status-state'
  _rest_name = 'tunnel-status-state'

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
    self.__oper_status = YANGDynClass(base=YANGBool, is_leaf=True, yang_name="oper-status", rest_name="oper-status", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='urn:brocade.com:mgmt:brocade-mpls-operational', defining_module='brocade-mpls-operational', yang_type='boolean', is_config=False)
    self.__tunnel_destination = YANGDynClass(base=RestrictedClassType(base_type=long, restriction_dict={'range': ['0..4294967295']}, int_size=32), is_leaf=True, yang_name="tunnel-destination", rest_name="tunnel-destination", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, is_keyval=True, namespace='urn:brocade.com:mgmt:brocade-mpls-operational', defining_module='brocade-mpls-operational', yang_type='uint32', is_config=False)

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
      return [u'tunnel-status-state']

  def _rest_path(self):
    if hasattr(self, "_parent"):
      if self._rest_name:
        return self._parent._rest_path()+[self._rest_name]
      else:
        return self._parent._rest_path()
    else:
      return [u'tunnel-status-state']

  def _get_tunnel_destination(self):
    """
    Getter method for tunnel_destination, mapped from YANG variable /tunnel_status_state/tunnel_destination (uint32)

    YANG Description: tunnel destination
    """
    return self.__tunnel_destination
      
  def _set_tunnel_destination(self, v, load=False):
    """
    Setter method for tunnel_destination, mapped from YANG variable /tunnel_status_state/tunnel_destination (uint32)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_tunnel_destination is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_tunnel_destination() directly.

    YANG Description: tunnel destination
    """
    parent = getattr(self, "_parent", None)
    if parent is not None and load is False:
      raise AttributeError("Cannot set keys directly when" +
                             " within an instantiated list")

    if hasattr(v, "_utype"):
      v = v._utype(v)
    try:
      t = YANGDynClass(v,base=RestrictedClassType(base_type=long, restriction_dict={'range': ['0..4294967295']}, int_size=32), is_leaf=True, yang_name="tunnel-destination", rest_name="tunnel-destination", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, is_keyval=True, namespace='urn:brocade.com:mgmt:brocade-mpls-operational', defining_module='brocade-mpls-operational', yang_type='uint32', is_config=False)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """tunnel_destination must be of a type compatible with uint32""",
          'defined-type': "uint32",
          'generated-type': """YANGDynClass(base=RestrictedClassType(base_type=long, restriction_dict={'range': ['0..4294967295']}, int_size=32), is_leaf=True, yang_name="tunnel-destination", rest_name="tunnel-destination", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, is_keyval=True, namespace='urn:brocade.com:mgmt:brocade-mpls-operational', defining_module='brocade-mpls-operational', yang_type='uint32', is_config=False)""",
        })

    self.__tunnel_destination = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_tunnel_destination(self):
    self.__tunnel_destination = YANGDynClass(base=RestrictedClassType(base_type=long, restriction_dict={'range': ['0..4294967295']}, int_size=32), is_leaf=True, yang_name="tunnel-destination", rest_name="tunnel-destination", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, is_keyval=True, namespace='urn:brocade.com:mgmt:brocade-mpls-operational', defining_module='brocade-mpls-operational', yang_type='uint32', is_config=False)


  def _get_oper_status(self):
    """
    Getter method for oper_status, mapped from YANG variable /tunnel_status_state/oper_status (boolean)

    YANG Description: Oper status of the tunnel
    """
    return self.__oper_status
      
  def _set_oper_status(self, v, load=False):
    """
    Setter method for oper_status, mapped from YANG variable /tunnel_status_state/oper_status (boolean)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_oper_status is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_oper_status() directly.

    YANG Description: Oper status of the tunnel
    """
    if hasattr(v, "_utype"):
      v = v._utype(v)
    try:
      t = YANGDynClass(v,base=YANGBool, is_leaf=True, yang_name="oper-status", rest_name="oper-status", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='urn:brocade.com:mgmt:brocade-mpls-operational', defining_module='brocade-mpls-operational', yang_type='boolean', is_config=False)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """oper_status must be of a type compatible with boolean""",
          'defined-type': "boolean",
          'generated-type': """YANGDynClass(base=YANGBool, is_leaf=True, yang_name="oper-status", rest_name="oper-status", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='urn:brocade.com:mgmt:brocade-mpls-operational', defining_module='brocade-mpls-operational', yang_type='boolean', is_config=False)""",
        })

    self.__oper_status = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_oper_status(self):
    self.__oper_status = YANGDynClass(base=YANGBool, is_leaf=True, yang_name="oper-status", rest_name="oper-status", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='urn:brocade.com:mgmt:brocade-mpls-operational', defining_module='brocade-mpls-operational', yang_type='boolean', is_config=False)

  tunnel_destination = __builtin__.property(_get_tunnel_destination)
  oper_status = __builtin__.property(_get_oper_status)


  _pyangbind_elements = {'tunnel_destination': tunnel_destination, 'oper_status': oper_status, }


