
from operator import attrgetter
import pyangbind.lib.xpathhelper as xpathhelper
from pyangbind.lib.yangtypes import RestrictedPrecisionDecimalType, RestrictedClassType, TypedListType
from pyangbind.lib.yangtypes import YANGBool, YANGListType, YANGDynClass, ReferenceType
from pyangbind.lib.base import PybindBase
from decimal import Decimal
from bitarray import bitarray
import __builtin__
import route_map
class hide_routemap_holder(PybindBase):
  """
  This class was auto-generated by the PythonClass plugin for PYANG
  from YANG module brocade-ip-policy - based on the path /hide-routemap-holder. Each member element of
  the container is represented as a class variable - with a specific
  YANG type.
  """
  __slots__ = ('_pybind_generated_by', '_path_helper', '_yang_name', '_rest_name', '_extmethods', '__route_map',)

  _yang_name = 'hide-routemap-holder'
  _rest_name = ''

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
    self.__route_map = YANGDynClass(base=YANGListType("name action_rm instance",route_map.route_map, yang_name="route-map", rest_name="route-map", parent=self, is_container='list', user_ordered=False, path_helper=self._path_helper, yang_keys='name action-rm instance', extensions={u'tailf-common': {u'info': u'Configure a route-map instance', u'cli-no-key-completion': None, u'sort-priority': u'64', u'cli-suppress-list-no': None, u'cli-full-command': None, u'callpoint': u'routemap-cp'}}), is_container='list', yang_name="route-map", rest_name="route-map", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'info': u'Configure a route-map instance', u'cli-no-key-completion': None, u'sort-priority': u'64', u'cli-suppress-list-no': None, u'cli-full-command': None, u'callpoint': u'routemap-cp'}}, namespace='urn:brocade.com:mgmt:brocade-ip-policy', defining_module='brocade-ip-policy', yang_type='list', is_config=True)

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
      return [u'hide-routemap-holder']

  def _rest_path(self):
    if hasattr(self, "_parent"):
      if self._rest_name:
        return self._parent._rest_path()+[self._rest_name]
      else:
        return self._parent._rest_path()
    else:
      return []

  def _get_route_map(self):
    """
    Getter method for route_map, mapped from YANG variable /hide_routemap_holder/route_map (list)

    YANG Description: Configure a route-map instance
    """
    return self.__route_map
      
  def _set_route_map(self, v, load=False):
    """
    Setter method for route_map, mapped from YANG variable /hide_routemap_holder/route_map (list)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_route_map is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_route_map() directly.

    YANG Description: Configure a route-map instance
    """
    if hasattr(v, "_utype"):
      v = v._utype(v)
    try:
      t = YANGDynClass(v,base=YANGListType("name action_rm instance",route_map.route_map, yang_name="route-map", rest_name="route-map", parent=self, is_container='list', user_ordered=False, path_helper=self._path_helper, yang_keys='name action-rm instance', extensions={u'tailf-common': {u'info': u'Configure a route-map instance', u'cli-no-key-completion': None, u'sort-priority': u'64', u'cli-suppress-list-no': None, u'cli-full-command': None, u'callpoint': u'routemap-cp'}}), is_container='list', yang_name="route-map", rest_name="route-map", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'info': u'Configure a route-map instance', u'cli-no-key-completion': None, u'sort-priority': u'64', u'cli-suppress-list-no': None, u'cli-full-command': None, u'callpoint': u'routemap-cp'}}, namespace='urn:brocade.com:mgmt:brocade-ip-policy', defining_module='brocade-ip-policy', yang_type='list', is_config=True)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """route_map must be of a type compatible with list""",
          'defined-type': "list",
          'generated-type': """YANGDynClass(base=YANGListType("name action_rm instance",route_map.route_map, yang_name="route-map", rest_name="route-map", parent=self, is_container='list', user_ordered=False, path_helper=self._path_helper, yang_keys='name action-rm instance', extensions={u'tailf-common': {u'info': u'Configure a route-map instance', u'cli-no-key-completion': None, u'sort-priority': u'64', u'cli-suppress-list-no': None, u'cli-full-command': None, u'callpoint': u'routemap-cp'}}), is_container='list', yang_name="route-map", rest_name="route-map", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'info': u'Configure a route-map instance', u'cli-no-key-completion': None, u'sort-priority': u'64', u'cli-suppress-list-no': None, u'cli-full-command': None, u'callpoint': u'routemap-cp'}}, namespace='urn:brocade.com:mgmt:brocade-ip-policy', defining_module='brocade-ip-policy', yang_type='list', is_config=True)""",
        })

    self.__route_map = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_route_map(self):
    self.__route_map = YANGDynClass(base=YANGListType("name action_rm instance",route_map.route_map, yang_name="route-map", rest_name="route-map", parent=self, is_container='list', user_ordered=False, path_helper=self._path_helper, yang_keys='name action-rm instance', extensions={u'tailf-common': {u'info': u'Configure a route-map instance', u'cli-no-key-completion': None, u'sort-priority': u'64', u'cli-suppress-list-no': None, u'cli-full-command': None, u'callpoint': u'routemap-cp'}}), is_container='list', yang_name="route-map", rest_name="route-map", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'info': u'Configure a route-map instance', u'cli-no-key-completion': None, u'sort-priority': u'64', u'cli-suppress-list-no': None, u'cli-full-command': None, u'callpoint': u'routemap-cp'}}, namespace='urn:brocade.com:mgmt:brocade-ip-policy', defining_module='brocade-ip-policy', yang_type='list', is_config=True)

  route_map = __builtin__.property(_get_route_map, _set_route_map)


  _pyangbind_elements = {'route_map': route_map, }


