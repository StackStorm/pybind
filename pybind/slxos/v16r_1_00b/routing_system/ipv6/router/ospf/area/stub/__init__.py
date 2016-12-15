
from operator import attrgetter
import pyangbind.lib.xpathhelper as xpathhelper
from pyangbind.lib.yangtypes import RestrictedPrecisionDecimalType, RestrictedClassType, TypedListType
from pyangbind.lib.yangtypes import YANGBool, YANGListType, YANGDynClass, ReferenceType
from pyangbind.lib.base import PybindBase
from decimal import Decimal
from bitarray import bitarray
import __builtin__
class stub(PybindBase):
  """
  This class was auto-generated by the PythonClass plugin for PYANG
  from YANG module brocade-common-def - based on the path /routing-system/ipv6/router/ospf/area/stub. Each member element of
  the container is represented as a class variable - with a specific
  YANG type.

  YANG Description: Specify the area as a stub area.OSPFv3 routers within a stub area cannot send or receive External LSAs. In addition,routers in a stub area must use a default route to the area's Area Border Router (ABR) orAutonomous System Boundary Router (ASBR) to send traffic out of the area.
  """
  __slots__ = ('_pybind_generated_by', '_path_helper', '_yang_name', '_rest_name', '_extmethods', '__stub_area_no_summary','__stub_area_metric',)

  _yang_name = 'stub'
  _rest_name = 'stub'

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
    self.__stub_area_metric = YANGDynClass(base=RestrictedClassType(base_type=RestrictedClassType(base_type=long, restriction_dict={'range': ['0..4294967295']}, int_size=32), restriction_dict={'range': [u'1..1048575']}), is_leaf=True, yang_name="stub-area-metric", rest_name="", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'cli-full-command': None, u'cli-drop-node-name': None, u'cli-full-no': None}}, namespace='urn:brocade.com:mgmt:brocade-ospfv3', defining_module='brocade-ospfv3', yang_type='uint32', is_config=True)
    self.__stub_area_no_summary = YANGDynClass(base=YANGBool, is_leaf=True, yang_name="stub-area-no-summary", rest_name="no-summary", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'info': u'Do not send summary LSA into stub area', u'cli-optional-in-sequence': None, u'alt-name': u'no-summary', u'cli-full-no': None}}, namespace='urn:brocade.com:mgmt:brocade-ospfv3', defining_module='brocade-ospfv3', yang_type='empty', is_config=True)

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
      return [u'routing-system', u'ipv6', u'router', u'ospf', u'area', u'stub']

  def _rest_path(self):
    if hasattr(self, "_parent"):
      if self._rest_name:
        return self._parent._rest_path()+[self._rest_name]
      else:
        return self._parent._rest_path()
    else:
      return [u'ipv6', u'router', u'ospf', u'area', u'stub']

  def _get_stub_area_no_summary(self):
    """
    Getter method for stub_area_no_summary, mapped from YANG variable /routing_system/ipv6/router/ospf/area/stub/stub_area_no_summary (empty)

    YANG Description: Disables summary LSAs from being sent into the area.
    """
    return self.__stub_area_no_summary
      
  def _set_stub_area_no_summary(self, v, load=False):
    """
    Setter method for stub_area_no_summary, mapped from YANG variable /routing_system/ipv6/router/ospf/area/stub/stub_area_no_summary (empty)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_stub_area_no_summary is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_stub_area_no_summary() directly.

    YANG Description: Disables summary LSAs from being sent into the area.
    """
    if hasattr(v, "_utype"):
      v = v._utype(v)
    try:
      t = YANGDynClass(v,base=YANGBool, is_leaf=True, yang_name="stub-area-no-summary", rest_name="no-summary", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'info': u'Do not send summary LSA into stub area', u'cli-optional-in-sequence': None, u'alt-name': u'no-summary', u'cli-full-no': None}}, namespace='urn:brocade.com:mgmt:brocade-ospfv3', defining_module='brocade-ospfv3', yang_type='empty', is_config=True)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """stub_area_no_summary must be of a type compatible with empty""",
          'defined-type': "empty",
          'generated-type': """YANGDynClass(base=YANGBool, is_leaf=True, yang_name="stub-area-no-summary", rest_name="no-summary", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'info': u'Do not send summary LSA into stub area', u'cli-optional-in-sequence': None, u'alt-name': u'no-summary', u'cli-full-no': None}}, namespace='urn:brocade.com:mgmt:brocade-ospfv3', defining_module='brocade-ospfv3', yang_type='empty', is_config=True)""",
        })

    self.__stub_area_no_summary = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_stub_area_no_summary(self):
    self.__stub_area_no_summary = YANGDynClass(base=YANGBool, is_leaf=True, yang_name="stub-area-no-summary", rest_name="no-summary", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'info': u'Do not send summary LSA into stub area', u'cli-optional-in-sequence': None, u'alt-name': u'no-summary', u'cli-full-no': None}}, namespace='urn:brocade.com:mgmt:brocade-ospfv3', defining_module='brocade-ospfv3', yang_type='empty', is_config=True)


  def _get_stub_area_metric(self):
    """
    Getter method for stub_area_metric, mapped from YANG variable /routing_system/ipv6/router/ospf/area/stub/stub_area_metric (uint32)

    YANG Description: Stub area's advertised route metricStub metric specifies an additional cost for using a route to or from this area.There is no default. Normal areas do not use the cost parameter.
    """
    return self.__stub_area_metric
      
  def _set_stub_area_metric(self, v, load=False):
    """
    Setter method for stub_area_metric, mapped from YANG variable /routing_system/ipv6/router/ospf/area/stub/stub_area_metric (uint32)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_stub_area_metric is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_stub_area_metric() directly.

    YANG Description: Stub area's advertised route metricStub metric specifies an additional cost for using a route to or from this area.There is no default. Normal areas do not use the cost parameter.
    """
    if hasattr(v, "_utype"):
      v = v._utype(v)
    try:
      t = YANGDynClass(v,base=RestrictedClassType(base_type=RestrictedClassType(base_type=long, restriction_dict={'range': ['0..4294967295']}, int_size=32), restriction_dict={'range': [u'1..1048575']}), is_leaf=True, yang_name="stub-area-metric", rest_name="", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'cli-full-command': None, u'cli-drop-node-name': None, u'cli-full-no': None}}, namespace='urn:brocade.com:mgmt:brocade-ospfv3', defining_module='brocade-ospfv3', yang_type='uint32', is_config=True)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """stub_area_metric must be of a type compatible with uint32""",
          'defined-type': "uint32",
          'generated-type': """YANGDynClass(base=RestrictedClassType(base_type=RestrictedClassType(base_type=long, restriction_dict={'range': ['0..4294967295']}, int_size=32), restriction_dict={'range': [u'1..1048575']}), is_leaf=True, yang_name="stub-area-metric", rest_name="", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'cli-full-command': None, u'cli-drop-node-name': None, u'cli-full-no': None}}, namespace='urn:brocade.com:mgmt:brocade-ospfv3', defining_module='brocade-ospfv3', yang_type='uint32', is_config=True)""",
        })

    self.__stub_area_metric = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_stub_area_metric(self):
    self.__stub_area_metric = YANGDynClass(base=RestrictedClassType(base_type=RestrictedClassType(base_type=long, restriction_dict={'range': ['0..4294967295']}, int_size=32), restriction_dict={'range': [u'1..1048575']}), is_leaf=True, yang_name="stub-area-metric", rest_name="", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'cli-full-command': None, u'cli-drop-node-name': None, u'cli-full-no': None}}, namespace='urn:brocade.com:mgmt:brocade-ospfv3', defining_module='brocade-ospfv3', yang_type='uint32', is_config=True)

  stub_area_no_summary = __builtin__.property(_get_stub_area_no_summary, _set_stub_area_no_summary)
  stub_area_metric = __builtin__.property(_get_stub_area_metric, _set_stub_area_metric)


  _pyangbind_elements = {'stub_area_no_summary': stub_area_no_summary, 'stub_area_metric': stub_area_metric, }


