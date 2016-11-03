
from operator import attrgetter
import pyangbind.lib.xpathhelper as xpathhelper
from pyangbind.lib.yangtypes import RestrictedPrecisionDecimalType, RestrictedClassType, TypedListType
from pyangbind.lib.yangtypes import YANGBool, YANGListType, YANGDynClass, ReferenceType
from pyangbind.lib.base import PybindBase
from decimal import Decimal
from bitarray import bitarray
import __builtin__
class fcoe_enode_fabric_map(PybindBase):
  """
  This class was auto-generated by the PythonClass plugin for PYANG
  from YANG module brocade-rbridge - based on the path /rbridge-id/fcoe-config/fcoe-enode-fabric-map. Each member element of
  the container is represented as a class variable - with a specific
  YANG type.

  YANG Description: List of FCoE fabric map parameters.
  """
  __slots__ = ('_pybind_generated_by', '_path_helper', '_yang_name', '_rest_name', '_extmethods', '__fcoe_enode_fabric_map_name',)

  _yang_name = 'fcoe-enode-fabric-map'
  _rest_name = 'fabric-map'

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
    self.__fcoe_enode_fabric_map_name = YANGDynClass(base=RestrictedClassType(base_type=unicode, restriction_dict={'pattern': u'default', 'length': [u'1..32']}), is_leaf=True, yang_name="fcoe-enode-fabric-map-name", rest_name="", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'info': u'Configure an FCoE Fabric-map ', u'cli-drop-node-name': None, u'hidden': u'fcoe-enode-fabric-map-name'}}, is_keyval=True, namespace='urn:brocade.com:mgmt:brocade-fcoe', defining_module='brocade-fcoe', yang_type='fcoe-enode-fabric-map-name-type', is_config=True)

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
      return [u'rbridge-id', u'fcoe-config', u'fcoe-enode-fabric-map']

  def _rest_path(self):
    if hasattr(self, "_parent"):
      if self._rest_name:
        return self._parent._rest_path()+[self._rest_name]
      else:
        return self._parent._rest_path()
    else:
      return [u'rbridge-id', u'fcoe', u'fabric-map']

  def _get_fcoe_enode_fabric_map_name(self):
    """
    Getter method for fcoe_enode_fabric_map_name, mapped from YANG variable /rbridge_id/fcoe_config/fcoe_enode_fabric_map/fcoe_enode_fabric_map_name (fcoe-enode-fabric-map-name-type)

    YANG Description: This specifies the name for the FCoE fabric map.
    """
    return self.__fcoe_enode_fabric_map_name
      
  def _set_fcoe_enode_fabric_map_name(self, v, load=False):
    """
    Setter method for fcoe_enode_fabric_map_name, mapped from YANG variable /rbridge_id/fcoe_config/fcoe_enode_fabric_map/fcoe_enode_fabric_map_name (fcoe-enode-fabric-map-name-type)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_fcoe_enode_fabric_map_name is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_fcoe_enode_fabric_map_name() directly.

    YANG Description: This specifies the name for the FCoE fabric map.
    """
    parent = getattr(self, "_parent", None)
    if parent is not None and load is False:
      raise AttributeError("Cannot set keys directly when" +
                             " within an instantiated list")

    try:
      t = YANGDynClass(v,base=RestrictedClassType(base_type=unicode, restriction_dict={'pattern': u'default', 'length': [u'1..32']}), is_leaf=True, yang_name="fcoe-enode-fabric-map-name", rest_name="", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'info': u'Configure an FCoE Fabric-map ', u'cli-drop-node-name': None, u'hidden': u'fcoe-enode-fabric-map-name'}}, is_keyval=True, namespace='urn:brocade.com:mgmt:brocade-fcoe', defining_module='brocade-fcoe', yang_type='fcoe-enode-fabric-map-name-type', is_config=True)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """fcoe_enode_fabric_map_name must be of a type compatible with fcoe-enode-fabric-map-name-type""",
          'defined-type': "brocade-fcoe:fcoe-enode-fabric-map-name-type",
          'generated-type': """YANGDynClass(base=RestrictedClassType(base_type=unicode, restriction_dict={'pattern': u'default', 'length': [u'1..32']}), is_leaf=True, yang_name="fcoe-enode-fabric-map-name", rest_name="", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'info': u'Configure an FCoE Fabric-map ', u'cli-drop-node-name': None, u'hidden': u'fcoe-enode-fabric-map-name'}}, is_keyval=True, namespace='urn:brocade.com:mgmt:brocade-fcoe', defining_module='brocade-fcoe', yang_type='fcoe-enode-fabric-map-name-type', is_config=True)""",
        })

    self.__fcoe_enode_fabric_map_name = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_fcoe_enode_fabric_map_name(self):
    self.__fcoe_enode_fabric_map_name = YANGDynClass(base=RestrictedClassType(base_type=unicode, restriction_dict={'pattern': u'default', 'length': [u'1..32']}), is_leaf=True, yang_name="fcoe-enode-fabric-map-name", rest_name="", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'info': u'Configure an FCoE Fabric-map ', u'cli-drop-node-name': None, u'hidden': u'fcoe-enode-fabric-map-name'}}, is_keyval=True, namespace='urn:brocade.com:mgmt:brocade-fcoe', defining_module='brocade-fcoe', yang_type='fcoe-enode-fabric-map-name-type', is_config=True)

  fcoe_enode_fabric_map_name = __builtin__.property(_get_fcoe_enode_fabric_map_name, _set_fcoe_enode_fabric_map_name)


  _pyangbind_elements = {'fcoe_enode_fabric_map_name': fcoe_enode_fabric_map_name, }

