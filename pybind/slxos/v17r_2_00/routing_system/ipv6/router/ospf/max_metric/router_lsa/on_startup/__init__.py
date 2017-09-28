
from operator import attrgetter
import pyangbind.lib.xpathhelper as xpathhelper
from pyangbind.lib.yangtypes import RestrictedPrecisionDecimalType, RestrictedClassType, TypedListType
from pyangbind.lib.yangtypes import YANGBool, YANGListType, YANGDynClass, ReferenceType
from pyangbind.lib.base import PybindBase
from decimal import Decimal
from bitarray import bitarray
import __builtin__
class on_startup(PybindBase):
  """
  This class was auto-generated by the PythonClass plugin for PYANG
  from YANG module brocade-common-def - based on the path /routing-system/ipv6/router/ospf/max-metric/router-lsa/on-startup. Each member element of
  the container is represented as a class variable - with a specific
  YANG type.

  YANG Description: The on-startup parameter specifies the advertisement of the maximum metric for a limited period only, on startup.
  """
  __slots__ = ('_pybind_generated_by', '_path_helper', '_yang_name', '_rest_name', '_extmethods', '__on_startup_time','__wait_for_bgp',)

  _yang_name = 'on-startup'
  _rest_name = 'on-startup'

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
    self.__wait_for_bgp = YANGDynClass(base=YANGBool, is_leaf=True, yang_name="wait-for-bgp", rest_name="wait-for-bgp", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'info': u'Advertise maximum metric until BGP has converged or 600 seconds', u'cli-full-command': None, u'cli-full-no': None}}, namespace='urn:brocade.com:mgmt:brocade-ospfv3', defining_module='brocade-ospfv3', yang_type='empty', is_config=True)
    self.__on_startup_time = YANGDynClass(base=RestrictedClassType(base_type=RestrictedClassType(base_type=long, restriction_dict={'range': ['0..4294967295']}, int_size=32), restriction_dict={'range': [u'5 ..86400']}), is_leaf=True, yang_name="on-startup-time", rest_name="on-startup-time", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'info': u'DECIMAL Amount of time to advertise maximum metric,range 5 to 86400 seconds', u'cli-drop-node-name': None, u'cli-full-no': None, u'cli-full-command': None}}, namespace='urn:brocade.com:mgmt:brocade-ospfv3', defining_module='brocade-ospfv3', yang_type='uint32', is_config=True)

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
      return [u'routing-system', u'ipv6', u'router', u'ospf', u'max-metric', u'router-lsa', u'on-startup']

  def _rest_path(self):
    if hasattr(self, "_parent"):
      if self._rest_name:
        return self._parent._rest_path()+[self._rest_name]
      else:
        return self._parent._rest_path()
    else:
      return [u'ipv6', u'router', u'ospf', u'max-metric', u'router-lsa', u'on-startup']

  def _get_on_startup_time(self):
    """
    Getter method for on_startup_time, mapped from YANG variable /routing_system/ipv6/router/ospf/max_metric/router_lsa/on_startup/on_startup_time (uint32)
    """
    return self.__on_startup_time
      
  def _set_on_startup_time(self, v, load=False):
    """
    Setter method for on_startup_time, mapped from YANG variable /routing_system/ipv6/router/ospf/max_metric/router_lsa/on_startup/on_startup_time (uint32)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_on_startup_time is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_on_startup_time() directly.
    """
    if hasattr(v, "_utype"):
      v = v._utype(v)
    try:
      t = YANGDynClass(v,base=RestrictedClassType(base_type=RestrictedClassType(base_type=long, restriction_dict={'range': ['0..4294967295']}, int_size=32), restriction_dict={'range': [u'5 ..86400']}), is_leaf=True, yang_name="on-startup-time", rest_name="on-startup-time", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'info': u'DECIMAL Amount of time to advertise maximum metric,range 5 to 86400 seconds', u'cli-drop-node-name': None, u'cli-full-no': None, u'cli-full-command': None}}, namespace='urn:brocade.com:mgmt:brocade-ospfv3', defining_module='brocade-ospfv3', yang_type='uint32', is_config=True)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """on_startup_time must be of a type compatible with uint32""",
          'defined-type': "uint32",
          'generated-type': """YANGDynClass(base=RestrictedClassType(base_type=RestrictedClassType(base_type=long, restriction_dict={'range': ['0..4294967295']}, int_size=32), restriction_dict={'range': [u'5 ..86400']}), is_leaf=True, yang_name="on-startup-time", rest_name="on-startup-time", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'info': u'DECIMAL Amount of time to advertise maximum metric,range 5 to 86400 seconds', u'cli-drop-node-name': None, u'cli-full-no': None, u'cli-full-command': None}}, namespace='urn:brocade.com:mgmt:brocade-ospfv3', defining_module='brocade-ospfv3', yang_type='uint32', is_config=True)""",
        })

    self.__on_startup_time = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_on_startup_time(self):
    self.__on_startup_time = YANGDynClass(base=RestrictedClassType(base_type=RestrictedClassType(base_type=long, restriction_dict={'range': ['0..4294967295']}, int_size=32), restriction_dict={'range': [u'5 ..86400']}), is_leaf=True, yang_name="on-startup-time", rest_name="on-startup-time", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'info': u'DECIMAL Amount of time to advertise maximum metric,range 5 to 86400 seconds', u'cli-drop-node-name': None, u'cli-full-no': None, u'cli-full-command': None}}, namespace='urn:brocade.com:mgmt:brocade-ospfv3', defining_module='brocade-ospfv3', yang_type='uint32', is_config=True)


  def _get_wait_for_bgp(self):
    """
    Getter method for wait_for_bgp, mapped from YANG variable /routing_system/ipv6/router/ospf/max_metric/router_lsa/on_startup/wait_for_bgp (empty)

    YANG Description: The wait-for-bgp parameter specifies that the maximum metric is advertised until BGP converges or for 600 seconds.When the on-startup option is not specified, a device configured with max-metric router-lsa always advertises the max-metric.
    """
    return self.__wait_for_bgp
      
  def _set_wait_for_bgp(self, v, load=False):
    """
    Setter method for wait_for_bgp, mapped from YANG variable /routing_system/ipv6/router/ospf/max_metric/router_lsa/on_startup/wait_for_bgp (empty)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_wait_for_bgp is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_wait_for_bgp() directly.

    YANG Description: The wait-for-bgp parameter specifies that the maximum metric is advertised until BGP converges or for 600 seconds.When the on-startup option is not specified, a device configured with max-metric router-lsa always advertises the max-metric.
    """
    if hasattr(v, "_utype"):
      v = v._utype(v)
    try:
      t = YANGDynClass(v,base=YANGBool, is_leaf=True, yang_name="wait-for-bgp", rest_name="wait-for-bgp", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'info': u'Advertise maximum metric until BGP has converged or 600 seconds', u'cli-full-command': None, u'cli-full-no': None}}, namespace='urn:brocade.com:mgmt:brocade-ospfv3', defining_module='brocade-ospfv3', yang_type='empty', is_config=True)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """wait_for_bgp must be of a type compatible with empty""",
          'defined-type': "empty",
          'generated-type': """YANGDynClass(base=YANGBool, is_leaf=True, yang_name="wait-for-bgp", rest_name="wait-for-bgp", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'info': u'Advertise maximum metric until BGP has converged or 600 seconds', u'cli-full-command': None, u'cli-full-no': None}}, namespace='urn:brocade.com:mgmt:brocade-ospfv3', defining_module='brocade-ospfv3', yang_type='empty', is_config=True)""",
        })

    self.__wait_for_bgp = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_wait_for_bgp(self):
    self.__wait_for_bgp = YANGDynClass(base=YANGBool, is_leaf=True, yang_name="wait-for-bgp", rest_name="wait-for-bgp", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'info': u'Advertise maximum metric until BGP has converged or 600 seconds', u'cli-full-command': None, u'cli-full-no': None}}, namespace='urn:brocade.com:mgmt:brocade-ospfv3', defining_module='brocade-ospfv3', yang_type='empty', is_config=True)

  on_startup_time = __builtin__.property(_get_on_startup_time, _set_on_startup_time)
  wait_for_bgp = __builtin__.property(_get_wait_for_bgp, _set_wait_for_bgp)


  _pyangbind_elements = {'on_startup_time': on_startup_time, 'wait_for_bgp': wait_for_bgp, }

