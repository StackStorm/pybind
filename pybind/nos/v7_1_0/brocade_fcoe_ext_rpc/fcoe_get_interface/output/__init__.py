
from operator import attrgetter
import pyangbind.lib.xpathhelper as xpathhelper
from pyangbind.lib.yangtypes import RestrictedPrecisionDecimalType, RestrictedClassType, TypedListType
from pyangbind.lib.yangtypes import YANGBool, YANGListType, YANGDynClass, ReferenceType
from pyangbind.lib.base import PybindBase
from decimal import Decimal
from bitarray import bitarray
import __builtin__
import fcoe_intf_list
class output(PybindBase):
  """
  This class was auto-generated by the PythonClass plugin for PYANG
  from YANG module brocade-fcoe-ext - based on the path /brocade_fcoe_ext_rpc/fcoe-get-interface/output. Each member element of
  the container is represented as a class variable - with a specific
  YANG type.
  """
  __slots__ = ('_pybind_generated_by', '_path_helper', '_yang_name', '_rest_name', '_extmethods', '__fcoe_intf_list','__fcoe_intf_total_interfaces',)

  _yang_name = 'output'
  _rest_name = 'output'

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
    self.__fcoe_intf_list = YANGDynClass(base=YANGListType("fcoe_intf_fcoe_port_id",fcoe_intf_list.fcoe_intf_list, yang_name="fcoe-intf-list", rest_name="fcoe-intf-list", parent=self, is_container='list', user_ordered=False, path_helper=self._path_helper, yang_keys='fcoe-intf-fcoe-port-id', extensions=None), is_container='list', yang_name="fcoe-intf-list", rest_name="fcoe-intf-list", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=False, extensions=None, namespace='urn:brocade.com:mgmt:brocade-fcoe-ext', defining_module='brocade-fcoe-ext', yang_type='list', is_config=True)
    self.__fcoe_intf_total_interfaces = YANGDynClass(base=RestrictedClassType(base_type=long, restriction_dict={'range': ['0..4294967295']}, int_size=32), default=RestrictedClassType(base_type=long, restriction_dict={'range': ['0..4294967295']}, int_size=32)(0), is_leaf=True, yang_name="fcoe-intf-total-interfaces", rest_name="fcoe-intf-total-interfaces", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=False, namespace='urn:brocade.com:mgmt:brocade-fcoe-ext', defining_module='brocade-fcoe-ext', yang_type='yang:zero-based-counter32', is_config=True)

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
      return [u'brocade_fcoe_ext_rpc', u'fcoe-get-interface', u'output']

  def _rest_path(self):
    if hasattr(self, "_parent"):
      if self._rest_name:
        return self._parent._rest_path()+[self._rest_name]
      else:
        return self._parent._rest_path()
    else:
      return [u'fcoe-get-interface', u'output']

  def _get_fcoe_intf_list(self):
    """
    Getter method for fcoe_intf_list, mapped from YANG variable /brocade_fcoe_ext_rpc/fcoe_get_interface/output/fcoe_intf_list (list)

    YANG Description: The format of the output for this rpc function 
will be a list of entries. Each row represents a 
FCoE interface operational characteristics such as 
fcoe port number, ethernet port number, the current
operational mode of the port and Tx/Rx stats for 
control traffic on that port.
    """
    return self.__fcoe_intf_list
      
  def _set_fcoe_intf_list(self, v, load=False):
    """
    Setter method for fcoe_intf_list, mapped from YANG variable /brocade_fcoe_ext_rpc/fcoe_get_interface/output/fcoe_intf_list (list)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_fcoe_intf_list is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_fcoe_intf_list() directly.

    YANG Description: The format of the output for this rpc function 
will be a list of entries. Each row represents a 
FCoE interface operational characteristics such as 
fcoe port number, ethernet port number, the current
operational mode of the port and Tx/Rx stats for 
control traffic on that port.
    """
    if hasattr(v, "_utype"):
      v = v._utype(v)
    try:
      t = YANGDynClass(v,base=YANGListType("fcoe_intf_fcoe_port_id",fcoe_intf_list.fcoe_intf_list, yang_name="fcoe-intf-list", rest_name="fcoe-intf-list", parent=self, is_container='list', user_ordered=False, path_helper=self._path_helper, yang_keys='fcoe-intf-fcoe-port-id', extensions=None), is_container='list', yang_name="fcoe-intf-list", rest_name="fcoe-intf-list", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=False, extensions=None, namespace='urn:brocade.com:mgmt:brocade-fcoe-ext', defining_module='brocade-fcoe-ext', yang_type='list', is_config=True)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """fcoe_intf_list must be of a type compatible with list""",
          'defined-type': "list",
          'generated-type': """YANGDynClass(base=YANGListType("fcoe_intf_fcoe_port_id",fcoe_intf_list.fcoe_intf_list, yang_name="fcoe-intf-list", rest_name="fcoe-intf-list", parent=self, is_container='list', user_ordered=False, path_helper=self._path_helper, yang_keys='fcoe-intf-fcoe-port-id', extensions=None), is_container='list', yang_name="fcoe-intf-list", rest_name="fcoe-intf-list", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=False, extensions=None, namespace='urn:brocade.com:mgmt:brocade-fcoe-ext', defining_module='brocade-fcoe-ext', yang_type='list', is_config=True)""",
        })

    self.__fcoe_intf_list = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_fcoe_intf_list(self):
    self.__fcoe_intf_list = YANGDynClass(base=YANGListType("fcoe_intf_fcoe_port_id",fcoe_intf_list.fcoe_intf_list, yang_name="fcoe-intf-list", rest_name="fcoe-intf-list", parent=self, is_container='list', user_ordered=False, path_helper=self._path_helper, yang_keys='fcoe-intf-fcoe-port-id', extensions=None), is_container='list', yang_name="fcoe-intf-list", rest_name="fcoe-intf-list", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=False, extensions=None, namespace='urn:brocade.com:mgmt:brocade-fcoe-ext', defining_module='brocade-fcoe-ext', yang_type='list', is_config=True)


  def _get_fcoe_intf_total_interfaces(self):
    """
    Getter method for fcoe_intf_total_interfaces, mapped from YANG variable /brocade_fcoe_ext_rpc/fcoe_get_interface/output/fcoe_intf_total_interfaces (yang:zero-based-counter32)

    YANG Description: This leaf indicates the total Number of interfaces
whose details are being returned by this 
function.
    """
    return self.__fcoe_intf_total_interfaces
      
  def _set_fcoe_intf_total_interfaces(self, v, load=False):
    """
    Setter method for fcoe_intf_total_interfaces, mapped from YANG variable /brocade_fcoe_ext_rpc/fcoe_get_interface/output/fcoe_intf_total_interfaces (yang:zero-based-counter32)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_fcoe_intf_total_interfaces is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_fcoe_intf_total_interfaces() directly.

    YANG Description: This leaf indicates the total Number of interfaces
whose details are being returned by this 
function.
    """
    if hasattr(v, "_utype"):
      v = v._utype(v)
    try:
      t = YANGDynClass(v,base=RestrictedClassType(base_type=long, restriction_dict={'range': ['0..4294967295']}, int_size=32), default=RestrictedClassType(base_type=long, restriction_dict={'range': ['0..4294967295']}, int_size=32)(0), is_leaf=True, yang_name="fcoe-intf-total-interfaces", rest_name="fcoe-intf-total-interfaces", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=False, namespace='urn:brocade.com:mgmt:brocade-fcoe-ext', defining_module='brocade-fcoe-ext', yang_type='yang:zero-based-counter32', is_config=True)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """fcoe_intf_total_interfaces must be of a type compatible with yang:zero-based-counter32""",
          'defined-type': "yang:zero-based-counter32",
          'generated-type': """YANGDynClass(base=RestrictedClassType(base_type=long, restriction_dict={'range': ['0..4294967295']}, int_size=32), default=RestrictedClassType(base_type=long, restriction_dict={'range': ['0..4294967295']}, int_size=32)(0), is_leaf=True, yang_name="fcoe-intf-total-interfaces", rest_name="fcoe-intf-total-interfaces", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=False, namespace='urn:brocade.com:mgmt:brocade-fcoe-ext', defining_module='brocade-fcoe-ext', yang_type='yang:zero-based-counter32', is_config=True)""",
        })

    self.__fcoe_intf_total_interfaces = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_fcoe_intf_total_interfaces(self):
    self.__fcoe_intf_total_interfaces = YANGDynClass(base=RestrictedClassType(base_type=long, restriction_dict={'range': ['0..4294967295']}, int_size=32), default=RestrictedClassType(base_type=long, restriction_dict={'range': ['0..4294967295']}, int_size=32)(0), is_leaf=True, yang_name="fcoe-intf-total-interfaces", rest_name="fcoe-intf-total-interfaces", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=False, namespace='urn:brocade.com:mgmt:brocade-fcoe-ext', defining_module='brocade-fcoe-ext', yang_type='yang:zero-based-counter32', is_config=True)

  fcoe_intf_list = __builtin__.property(_get_fcoe_intf_list, _set_fcoe_intf_list)
  fcoe_intf_total_interfaces = __builtin__.property(_get_fcoe_intf_total_interfaces, _set_fcoe_intf_total_interfaces)


  _pyangbind_elements = {'fcoe_intf_list': fcoe_intf_list, 'fcoe_intf_total_interfaces': fcoe_intf_total_interfaces, }


