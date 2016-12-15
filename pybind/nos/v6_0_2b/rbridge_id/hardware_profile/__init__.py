
from operator import attrgetter
import pyangbind.lib.xpathhelper as xpathhelper
from pyangbind.lib.yangtypes import RestrictedPrecisionDecimalType, RestrictedClassType, TypedListType
from pyangbind.lib.yangtypes import YANGBool, YANGListType, YANGDynClass, ReferenceType
from pyangbind.lib.base import PybindBase
from decimal import Decimal
from bitarray import bitarray
import __builtin__
import tcam
import route_table
import vlan_classification
import kap
class hardware_profile(PybindBase):
  """
  This class was auto-generated by the PythonClass plugin for PYANG
  from YANG module brocade-rbridge - based on the path /rbridge-id/hardware-profile. Each member element of
  the container is represented as a class variable - with a specific
  YANG type.
  """
  __slots__ = ('_pybind_generated_by', '_path_helper', '_yang_name', '_rest_name', '_extmethods', '__tcam','__route_table','__vlan_classification','__kap',)

  _yang_name = 'hardware-profile'
  _rest_name = 'hardware-profile'

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
    self.__kap = YANGDynClass(base=kap.kap, is_container='container', yang_name="kap", rest_name="kap", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'info': u'Select KAP profile type', u'callpoint': u'ha_profile_callpoint', u'cli-suppress-no': None}}, namespace='urn:brocade.com:mgmt:brocade-hardware', defining_module='brocade-hardware', yang_type='container', is_config=True)
    self.__tcam = YANGDynClass(base=tcam.tcam, is_container='container', yang_name="tcam", rest_name="tcam", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'info': u'Select TCAM profile type', u'callpoint': u'ha_profile_callpoint', u'cli-suppress-no': None}}, namespace='urn:brocade.com:mgmt:brocade-hardware', defining_module='brocade-hardware', yang_type='container', is_config=True)
    self.__vlan_classification = YANGDynClass(base=vlan_classification.vlan_classification, is_container='container', yang_name="vlan-classification", rest_name="vlan-classification", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'callpoint': u'ha_profile_callpoint', u'info': u'Select vlan classification type', u'hidden': u'debug', u'display-when': u'((../../swbd-number = "153") or (../../swbd-number = "154") or (../../swbd-number = "164"))', u'cli-suppress-no': None}}, namespace='urn:brocade.com:mgmt:brocade-hardware', defining_module='brocade-hardware', yang_type='container', is_config=True)
    self.__route_table = YANGDynClass(base=route_table.route_table, is_container='container', yang_name="route-table", rest_name="route-table", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'info': u'Select route table profile type', u'callpoint': u'ha_profile_callpoint', u'cli-suppress-no': None}}, namespace='urn:brocade.com:mgmt:brocade-hardware', defining_module='brocade-hardware', yang_type='container', is_config=True)

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
      return [u'rbridge-id', u'hardware-profile']

  def _rest_path(self):
    if hasattr(self, "_parent"):
      if self._rest_name:
        return self._parent._rest_path()+[self._rest_name]
      else:
        return self._parent._rest_path()
    else:
      return [u'rbridge-id', u'hardware-profile']

  def _get_tcam(self):
    """
    Getter method for tcam, mapped from YANG variable /rbridge_id/hardware_profile/tcam (container)
    """
    return self.__tcam
      
  def _set_tcam(self, v, load=False):
    """
    Setter method for tcam, mapped from YANG variable /rbridge_id/hardware_profile/tcam (container)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_tcam is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_tcam() directly.
    """
    if hasattr(v, "_utype"):
      v = v._utype(v)
    try:
      t = YANGDynClass(v,base=tcam.tcam, is_container='container', yang_name="tcam", rest_name="tcam", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'info': u'Select TCAM profile type', u'callpoint': u'ha_profile_callpoint', u'cli-suppress-no': None}}, namespace='urn:brocade.com:mgmt:brocade-hardware', defining_module='brocade-hardware', yang_type='container', is_config=True)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """tcam must be of a type compatible with container""",
          'defined-type': "container",
          'generated-type': """YANGDynClass(base=tcam.tcam, is_container='container', yang_name="tcam", rest_name="tcam", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'info': u'Select TCAM profile type', u'callpoint': u'ha_profile_callpoint', u'cli-suppress-no': None}}, namespace='urn:brocade.com:mgmt:brocade-hardware', defining_module='brocade-hardware', yang_type='container', is_config=True)""",
        })

    self.__tcam = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_tcam(self):
    self.__tcam = YANGDynClass(base=tcam.tcam, is_container='container', yang_name="tcam", rest_name="tcam", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'info': u'Select TCAM profile type', u'callpoint': u'ha_profile_callpoint', u'cli-suppress-no': None}}, namespace='urn:brocade.com:mgmt:brocade-hardware', defining_module='brocade-hardware', yang_type='container', is_config=True)


  def _get_route_table(self):
    """
    Getter method for route_table, mapped from YANG variable /rbridge_id/hardware_profile/route_table (container)
    """
    return self.__route_table
      
  def _set_route_table(self, v, load=False):
    """
    Setter method for route_table, mapped from YANG variable /rbridge_id/hardware_profile/route_table (container)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_route_table is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_route_table() directly.
    """
    if hasattr(v, "_utype"):
      v = v._utype(v)
    try:
      t = YANGDynClass(v,base=route_table.route_table, is_container='container', yang_name="route-table", rest_name="route-table", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'info': u'Select route table profile type', u'callpoint': u'ha_profile_callpoint', u'cli-suppress-no': None}}, namespace='urn:brocade.com:mgmt:brocade-hardware', defining_module='brocade-hardware', yang_type='container', is_config=True)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """route_table must be of a type compatible with container""",
          'defined-type': "container",
          'generated-type': """YANGDynClass(base=route_table.route_table, is_container='container', yang_name="route-table", rest_name="route-table", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'info': u'Select route table profile type', u'callpoint': u'ha_profile_callpoint', u'cli-suppress-no': None}}, namespace='urn:brocade.com:mgmt:brocade-hardware', defining_module='brocade-hardware', yang_type='container', is_config=True)""",
        })

    self.__route_table = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_route_table(self):
    self.__route_table = YANGDynClass(base=route_table.route_table, is_container='container', yang_name="route-table", rest_name="route-table", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'info': u'Select route table profile type', u'callpoint': u'ha_profile_callpoint', u'cli-suppress-no': None}}, namespace='urn:brocade.com:mgmt:brocade-hardware', defining_module='brocade-hardware', yang_type='container', is_config=True)


  def _get_vlan_classification(self):
    """
    Getter method for vlan_classification, mapped from YANG variable /rbridge_id/hardware_profile/vlan_classification (container)
    """
    return self.__vlan_classification
      
  def _set_vlan_classification(self, v, load=False):
    """
    Setter method for vlan_classification, mapped from YANG variable /rbridge_id/hardware_profile/vlan_classification (container)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_vlan_classification is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_vlan_classification() directly.
    """
    if hasattr(v, "_utype"):
      v = v._utype(v)
    try:
      t = YANGDynClass(v,base=vlan_classification.vlan_classification, is_container='container', yang_name="vlan-classification", rest_name="vlan-classification", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'callpoint': u'ha_profile_callpoint', u'info': u'Select vlan classification type', u'hidden': u'debug', u'display-when': u'((../../swbd-number = "153") or (../../swbd-number = "154") or (../../swbd-number = "164"))', u'cli-suppress-no': None}}, namespace='urn:brocade.com:mgmt:brocade-hardware', defining_module='brocade-hardware', yang_type='container', is_config=True)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """vlan_classification must be of a type compatible with container""",
          'defined-type': "container",
          'generated-type': """YANGDynClass(base=vlan_classification.vlan_classification, is_container='container', yang_name="vlan-classification", rest_name="vlan-classification", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'callpoint': u'ha_profile_callpoint', u'info': u'Select vlan classification type', u'hidden': u'debug', u'display-when': u'((../../swbd-number = "153") or (../../swbd-number = "154") or (../../swbd-number = "164"))', u'cli-suppress-no': None}}, namespace='urn:brocade.com:mgmt:brocade-hardware', defining_module='brocade-hardware', yang_type='container', is_config=True)""",
        })

    self.__vlan_classification = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_vlan_classification(self):
    self.__vlan_classification = YANGDynClass(base=vlan_classification.vlan_classification, is_container='container', yang_name="vlan-classification", rest_name="vlan-classification", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'callpoint': u'ha_profile_callpoint', u'info': u'Select vlan classification type', u'hidden': u'debug', u'display-when': u'((../../swbd-number = "153") or (../../swbd-number = "154") or (../../swbd-number = "164"))', u'cli-suppress-no': None}}, namespace='urn:brocade.com:mgmt:brocade-hardware', defining_module='brocade-hardware', yang_type='container', is_config=True)


  def _get_kap(self):
    """
    Getter method for kap, mapped from YANG variable /rbridge_id/hardware_profile/kap (container)
    """
    return self.__kap
      
  def _set_kap(self, v, load=False):
    """
    Setter method for kap, mapped from YANG variable /rbridge_id/hardware_profile/kap (container)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_kap is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_kap() directly.
    """
    if hasattr(v, "_utype"):
      v = v._utype(v)
    try:
      t = YANGDynClass(v,base=kap.kap, is_container='container', yang_name="kap", rest_name="kap", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'info': u'Select KAP profile type', u'callpoint': u'ha_profile_callpoint', u'cli-suppress-no': None}}, namespace='urn:brocade.com:mgmt:brocade-hardware', defining_module='brocade-hardware', yang_type='container', is_config=True)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """kap must be of a type compatible with container""",
          'defined-type': "container",
          'generated-type': """YANGDynClass(base=kap.kap, is_container='container', yang_name="kap", rest_name="kap", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'info': u'Select KAP profile type', u'callpoint': u'ha_profile_callpoint', u'cli-suppress-no': None}}, namespace='urn:brocade.com:mgmt:brocade-hardware', defining_module='brocade-hardware', yang_type='container', is_config=True)""",
        })

    self.__kap = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_kap(self):
    self.__kap = YANGDynClass(base=kap.kap, is_container='container', yang_name="kap", rest_name="kap", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'info': u'Select KAP profile type', u'callpoint': u'ha_profile_callpoint', u'cli-suppress-no': None}}, namespace='urn:brocade.com:mgmt:brocade-hardware', defining_module='brocade-hardware', yang_type='container', is_config=True)

  tcam = __builtin__.property(_get_tcam, _set_tcam)
  route_table = __builtin__.property(_get_route_table, _set_route_table)
  vlan_classification = __builtin__.property(_get_vlan_classification, _set_vlan_classification)
  kap = __builtin__.property(_get_kap, _set_kap)


  _pyangbind_elements = {'tcam': tcam, 'route_table': route_table, 'vlan_classification': vlan_classification, 'kap': kap, }


