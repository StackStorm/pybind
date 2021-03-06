
from operator import attrgetter
import pyangbind.lib.xpathhelper as xpathhelper
from pyangbind.lib.yangtypes import RestrictedPrecisionDecimalType, RestrictedClassType, TypedListType
from pyangbind.lib.yangtypes import YANGBool, YANGListType, YANGDynClass, ReferenceType
from pyangbind.lib.base import PybindBase
from decimal import Decimal
from bitarray import bitarray
import __builtin__
import fcport_group_rbid
class fcoe_fcport_group_config(PybindBase):
  """
  This class was auto-generated by the PythonClass plugin for PYANG
  from YANG module brocade-fcoe - based on the path /fcoe/fcoe-fabric-map/fcoe-fcport-group-config. Each member element of
  the container is represented as a class variable - with a specific
  YANG type.

  YANG Description: This specifies the fcport-group parameters for the fabric-map
  """
  __slots__ = ('_pybind_generated_by', '_path_helper', '_yang_name', '_rest_name', '_extmethods', '__fcport_group_rbid',)

  _yang_name = 'fcoe-fcport-group-config'
  _rest_name = 'fcport-group'

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
    self.__fcport_group_rbid = YANGDynClass(base=fcport_group_rbid.fcport_group_rbid, is_container='container', presence=False, yang_name="fcport-group-rbid", rest_name="fcport-group-rbid", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'info': u'Configure fcport-group rbridge-id/s.', u'alt-name': u'fcport-group-rbid', u'cli-suppress-no': None}}, namespace='urn:brocade.com:mgmt:brocade-fcoe', defining_module='brocade-fcoe', yang_type='container', is_config=True)

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
      return [u'fcoe', u'fcoe-fabric-map', u'fcoe-fcport-group-config']

  def _rest_path(self):
    if hasattr(self, "_parent"):
      if self._rest_name:
        return self._parent._rest_path()+[self._rest_name]
      else:
        return self._parent._rest_path()
    else:
      return [u'fcoe', u'fabric-map', u'fcport-group']

  def _get_fcport_group_rbid(self):
    """
    Getter method for fcport_group_rbid, mapped from YANG variable /fcoe/fcoe_fabric_map/fcoe_fcport_group_config/fcport_group_rbid (container)

    YANG Description: This specifies the FIF rbridge-id/s in the
FCF Group
    """
    return self.__fcport_group_rbid
      
  def _set_fcport_group_rbid(self, v, load=False):
    """
    Setter method for fcport_group_rbid, mapped from YANG variable /fcoe/fcoe_fabric_map/fcoe_fcport_group_config/fcport_group_rbid (container)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_fcport_group_rbid is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_fcport_group_rbid() directly.

    YANG Description: This specifies the FIF rbridge-id/s in the
FCF Group
    """
    if hasattr(v, "_utype"):
      v = v._utype(v)
    try:
      t = YANGDynClass(v,base=fcport_group_rbid.fcport_group_rbid, is_container='container', presence=False, yang_name="fcport-group-rbid", rest_name="fcport-group-rbid", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'info': u'Configure fcport-group rbridge-id/s.', u'alt-name': u'fcport-group-rbid', u'cli-suppress-no': None}}, namespace='urn:brocade.com:mgmt:brocade-fcoe', defining_module='brocade-fcoe', yang_type='container', is_config=True)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """fcport_group_rbid must be of a type compatible with container""",
          'defined-type': "container",
          'generated-type': """YANGDynClass(base=fcport_group_rbid.fcport_group_rbid, is_container='container', presence=False, yang_name="fcport-group-rbid", rest_name="fcport-group-rbid", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'info': u'Configure fcport-group rbridge-id/s.', u'alt-name': u'fcport-group-rbid', u'cli-suppress-no': None}}, namespace='urn:brocade.com:mgmt:brocade-fcoe', defining_module='brocade-fcoe', yang_type='container', is_config=True)""",
        })

    self.__fcport_group_rbid = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_fcport_group_rbid(self):
    self.__fcport_group_rbid = YANGDynClass(base=fcport_group_rbid.fcport_group_rbid, is_container='container', presence=False, yang_name="fcport-group-rbid", rest_name="fcport-group-rbid", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'info': u'Configure fcport-group rbridge-id/s.', u'alt-name': u'fcport-group-rbid', u'cli-suppress-no': None}}, namespace='urn:brocade.com:mgmt:brocade-fcoe', defining_module='brocade-fcoe', yang_type='container', is_config=True)

  fcport_group_rbid = __builtin__.property(_get_fcport_group_rbid, _set_fcport_group_rbid)


  _pyangbind_elements = {'fcport_group_rbid': fcport_group_rbid, }


