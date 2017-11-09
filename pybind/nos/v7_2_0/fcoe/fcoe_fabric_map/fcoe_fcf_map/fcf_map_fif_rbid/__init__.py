
from operator import attrgetter
import pyangbind.lib.xpathhelper as xpathhelper
from pyangbind.lib.yangtypes import RestrictedPrecisionDecimalType, RestrictedClassType, TypedListType
from pyangbind.lib.yangtypes import YANGBool, YANGListType, YANGDynClass, ReferenceType
from pyangbind.lib.base import PybindBase
from decimal import Decimal
from bitarray import bitarray
import __builtin__
class fcf_map_fif_rbid(PybindBase):
  """
  This class was auto-generated by the PythonClass plugin for PYANG
  from YANG module brocade-fcoe - based on the path /fcoe/fcoe-fabric-map/fcoe-fcf-map/fcf-map-fif-rbid. Each member element of
  the container is represented as a class variable - with a specific
  YANG type.

  YANG Description: This specifies the FIF rbridge-id/s in the
FCF Group
  """
  __slots__ = ('_pybind_generated_by', '_path_helper', '_yang_name', '_rest_name', '_extmethods', '__fcf_map_fif_rbid_add','__fcf_map_fif_rbid_remove',)

  _yang_name = 'fcf-map-fif-rbid'
  _rest_name = 'fif-rbid'

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
    self.__fcf_map_fif_rbid_remove = YANGDynClass(base=RestrictedClassType(base_type=unicode, restriction_dict={'pattern': u'(([1-9][0-9]{0,1})|(1[0-9]{2})|(2[0-3][0-9]))(-((1[0-9]{0,1})|([2-9][0-9]{0,1})|(1[0-9]{2})|(2[0-3][0-9])))?((,((1[0-9]{0,1})|([2-9][0-9]{0,1})|(1[0-9]{2})|(2[0-3][0-9]))(-((1[0-9]{0,1})|([2-9][0-9]{0,1})|(1[0-9]{2})|(2[0-3][0-9])))?)?)*', 'length': [u'1..567']}), is_leaf=True, yang_name="fcf-map-fif-rbid-remove", rest_name="remove", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'alt-name': u'remove'}}, namespace='urn:brocade.com:mgmt:brocade-fcoe', defining_module='brocade-fcoe', yang_type='ui32-rbridge-id-range', is_config=True)
    self.__fcf_map_fif_rbid_add = YANGDynClass(base=RestrictedClassType(base_type=unicode, restriction_dict={'pattern': u'(([1-9][0-9]{0,1})|(1[0-9]{2})|(2[0-3][0-9]))(-((1[0-9]{0,1})|([2-9][0-9]{0,1})|(1[0-9]{2})|(2[0-3][0-9])))?((,((1[0-9]{0,1})|([2-9][0-9]{0,1})|(1[0-9]{2})|(2[0-3][0-9]))(-((1[0-9]{0,1})|([2-9][0-9]{0,1})|(1[0-9]{2})|(2[0-3][0-9])))?)?)*', 'length': [u'1..567']}), is_leaf=True, yang_name="fcf-map-fif-rbid-add", rest_name="add", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'alt-name': u'add'}}, namespace='urn:brocade.com:mgmt:brocade-fcoe', defining_module='brocade-fcoe', yang_type='ui32-rbridge-id-range', is_config=True)

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
      return [u'fcoe', u'fcoe-fabric-map', u'fcoe-fcf-map', u'fcf-map-fif-rbid']

  def _rest_path(self):
    if hasattr(self, "_parent"):
      if self._rest_name:
        return self._parent._rest_path()+[self._rest_name]
      else:
        return self._parent._rest_path()
    else:
      return [u'fcoe', u'fabric-map', u'fcf-group', u'fif-rbid']

  def _get_fcf_map_fif_rbid_add(self):
    """
    Getter method for fcf_map_fif_rbid_add, mapped from YANG variable /fcoe/fcoe_fabric_map/fcoe_fcf_map/fcf_map_fif_rbid/fcf_map_fif_rbid_add (ui32-rbridge-id-range)

    YANG Description: This specifies the FIF rbridge-id/s in the
FCF Group
    """
    return self.__fcf_map_fif_rbid_add
      
  def _set_fcf_map_fif_rbid_add(self, v, load=False):
    """
    Setter method for fcf_map_fif_rbid_add, mapped from YANG variable /fcoe/fcoe_fabric_map/fcoe_fcf_map/fcf_map_fif_rbid/fcf_map_fif_rbid_add (ui32-rbridge-id-range)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_fcf_map_fif_rbid_add is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_fcf_map_fif_rbid_add() directly.

    YANG Description: This specifies the FIF rbridge-id/s in the
FCF Group
    """
    if hasattr(v, "_utype"):
      v = v._utype(v)
    try:
      t = YANGDynClass(v,base=RestrictedClassType(base_type=unicode, restriction_dict={'pattern': u'(([1-9][0-9]{0,1})|(1[0-9]{2})|(2[0-3][0-9]))(-((1[0-9]{0,1})|([2-9][0-9]{0,1})|(1[0-9]{2})|(2[0-3][0-9])))?((,((1[0-9]{0,1})|([2-9][0-9]{0,1})|(1[0-9]{2})|(2[0-3][0-9]))(-((1[0-9]{0,1})|([2-9][0-9]{0,1})|(1[0-9]{2})|(2[0-3][0-9])))?)?)*', 'length': [u'1..567']}), is_leaf=True, yang_name="fcf-map-fif-rbid-add", rest_name="add", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'alt-name': u'add'}}, namespace='urn:brocade.com:mgmt:brocade-fcoe', defining_module='brocade-fcoe', yang_type='ui32-rbridge-id-range', is_config=True)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """fcf_map_fif_rbid_add must be of a type compatible with ui32-rbridge-id-range""",
          'defined-type': "brocade-fcoe:ui32-rbridge-id-range",
          'generated-type': """YANGDynClass(base=RestrictedClassType(base_type=unicode, restriction_dict={'pattern': u'(([1-9][0-9]{0,1})|(1[0-9]{2})|(2[0-3][0-9]))(-((1[0-9]{0,1})|([2-9][0-9]{0,1})|(1[0-9]{2})|(2[0-3][0-9])))?((,((1[0-9]{0,1})|([2-9][0-9]{0,1})|(1[0-9]{2})|(2[0-3][0-9]))(-((1[0-9]{0,1})|([2-9][0-9]{0,1})|(1[0-9]{2})|(2[0-3][0-9])))?)?)*', 'length': [u'1..567']}), is_leaf=True, yang_name="fcf-map-fif-rbid-add", rest_name="add", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'alt-name': u'add'}}, namespace='urn:brocade.com:mgmt:brocade-fcoe', defining_module='brocade-fcoe', yang_type='ui32-rbridge-id-range', is_config=True)""",
        })

    self.__fcf_map_fif_rbid_add = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_fcf_map_fif_rbid_add(self):
    self.__fcf_map_fif_rbid_add = YANGDynClass(base=RestrictedClassType(base_type=unicode, restriction_dict={'pattern': u'(([1-9][0-9]{0,1})|(1[0-9]{2})|(2[0-3][0-9]))(-((1[0-9]{0,1})|([2-9][0-9]{0,1})|(1[0-9]{2})|(2[0-3][0-9])))?((,((1[0-9]{0,1})|([2-9][0-9]{0,1})|(1[0-9]{2})|(2[0-3][0-9]))(-((1[0-9]{0,1})|([2-9][0-9]{0,1})|(1[0-9]{2})|(2[0-3][0-9])))?)?)*', 'length': [u'1..567']}), is_leaf=True, yang_name="fcf-map-fif-rbid-add", rest_name="add", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'alt-name': u'add'}}, namespace='urn:brocade.com:mgmt:brocade-fcoe', defining_module='brocade-fcoe', yang_type='ui32-rbridge-id-range', is_config=True)


  def _get_fcf_map_fif_rbid_remove(self):
    """
    Getter method for fcf_map_fif_rbid_remove, mapped from YANG variable /fcoe/fcoe_fabric_map/fcoe_fcf_map/fcf_map_fif_rbid/fcf_map_fif_rbid_remove (ui32-rbridge-id-range)

    YANG Description: This specifies the FIF rbridge-id/s in the
FCF Group
    """
    return self.__fcf_map_fif_rbid_remove
      
  def _set_fcf_map_fif_rbid_remove(self, v, load=False):
    """
    Setter method for fcf_map_fif_rbid_remove, mapped from YANG variable /fcoe/fcoe_fabric_map/fcoe_fcf_map/fcf_map_fif_rbid/fcf_map_fif_rbid_remove (ui32-rbridge-id-range)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_fcf_map_fif_rbid_remove is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_fcf_map_fif_rbid_remove() directly.

    YANG Description: This specifies the FIF rbridge-id/s in the
FCF Group
    """
    if hasattr(v, "_utype"):
      v = v._utype(v)
    try:
      t = YANGDynClass(v,base=RestrictedClassType(base_type=unicode, restriction_dict={'pattern': u'(([1-9][0-9]{0,1})|(1[0-9]{2})|(2[0-3][0-9]))(-((1[0-9]{0,1})|([2-9][0-9]{0,1})|(1[0-9]{2})|(2[0-3][0-9])))?((,((1[0-9]{0,1})|([2-9][0-9]{0,1})|(1[0-9]{2})|(2[0-3][0-9]))(-((1[0-9]{0,1})|([2-9][0-9]{0,1})|(1[0-9]{2})|(2[0-3][0-9])))?)?)*', 'length': [u'1..567']}), is_leaf=True, yang_name="fcf-map-fif-rbid-remove", rest_name="remove", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'alt-name': u'remove'}}, namespace='urn:brocade.com:mgmt:brocade-fcoe', defining_module='brocade-fcoe', yang_type='ui32-rbridge-id-range', is_config=True)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """fcf_map_fif_rbid_remove must be of a type compatible with ui32-rbridge-id-range""",
          'defined-type': "brocade-fcoe:ui32-rbridge-id-range",
          'generated-type': """YANGDynClass(base=RestrictedClassType(base_type=unicode, restriction_dict={'pattern': u'(([1-9][0-9]{0,1})|(1[0-9]{2})|(2[0-3][0-9]))(-((1[0-9]{0,1})|([2-9][0-9]{0,1})|(1[0-9]{2})|(2[0-3][0-9])))?((,((1[0-9]{0,1})|([2-9][0-9]{0,1})|(1[0-9]{2})|(2[0-3][0-9]))(-((1[0-9]{0,1})|([2-9][0-9]{0,1})|(1[0-9]{2})|(2[0-3][0-9])))?)?)*', 'length': [u'1..567']}), is_leaf=True, yang_name="fcf-map-fif-rbid-remove", rest_name="remove", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'alt-name': u'remove'}}, namespace='urn:brocade.com:mgmt:brocade-fcoe', defining_module='brocade-fcoe', yang_type='ui32-rbridge-id-range', is_config=True)""",
        })

    self.__fcf_map_fif_rbid_remove = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_fcf_map_fif_rbid_remove(self):
    self.__fcf_map_fif_rbid_remove = YANGDynClass(base=RestrictedClassType(base_type=unicode, restriction_dict={'pattern': u'(([1-9][0-9]{0,1})|(1[0-9]{2})|(2[0-3][0-9]))(-((1[0-9]{0,1})|([2-9][0-9]{0,1})|(1[0-9]{2})|(2[0-3][0-9])))?((,((1[0-9]{0,1})|([2-9][0-9]{0,1})|(1[0-9]{2})|(2[0-3][0-9]))(-((1[0-9]{0,1})|([2-9][0-9]{0,1})|(1[0-9]{2})|(2[0-3][0-9])))?)?)*', 'length': [u'1..567']}), is_leaf=True, yang_name="fcf-map-fif-rbid-remove", rest_name="remove", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'alt-name': u'remove'}}, namespace='urn:brocade.com:mgmt:brocade-fcoe', defining_module='brocade-fcoe', yang_type='ui32-rbridge-id-range', is_config=True)

  fcf_map_fif_rbid_add = __builtin__.property(_get_fcf_map_fif_rbid_add, _set_fcf_map_fif_rbid_add)
  fcf_map_fif_rbid_remove = __builtin__.property(_get_fcf_map_fif_rbid_remove, _set_fcf_map_fif_rbid_remove)


  _pyangbind_elements = {'fcf_map_fif_rbid_add': fcf_map_fif_rbid_add, 'fcf_map_fif_rbid_remove': fcf_map_fif_rbid_remove, }

