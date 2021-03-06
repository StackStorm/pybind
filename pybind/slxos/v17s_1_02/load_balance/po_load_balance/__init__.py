
from operator import attrgetter
import pyangbind.lib.xpathhelper as xpathhelper
from pyangbind.lib.yangtypes import RestrictedPrecisionDecimalType, RestrictedClassType, TypedListType
from pyangbind.lib.yangtypes import YANGBool, YANGListType, YANGDynClass, ReferenceType
from pyangbind.lib.base import PybindBase
from decimal import Decimal
from bitarray import bitarray
import __builtin__
class po_load_balance(PybindBase):
  """
  This class was auto-generated by the PythonClass plugin for PYANG
  from YANG module brocade-rbridge-lag - based on the path /load-balance/po-load-balance. Each member element of
  the container is represented as a class variable - with a specific
  YANG type.
  """
  __slots__ = ('_pybind_generated_by', '_path_helper', '_yang_name', '_rest_name', '_extmethods', '__load_balance_type',)

  _yang_name = 'po-load-balance'
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
    self.__load_balance_type = YANGDynClass(base=RestrictedClassType(base_type=unicode,                                     restriction_type="dict_key",                                     restriction_arg={u'src-dst-ip-port': {'value': 6}, u'src-mac-vid': {'value': 2}, u'src-dst-ip': {'value': 4}, u'src-dst-ip-mac-vid': {'value': 5}, u'dst-mac-vid': {'value': 1}, u'src-dst-mac-vid': {'value': 3}, u'src-dst-ip-mac-vid-port': {'value': 7}},), default=unicode("src-dst-ip-mac-vid-port"), is_leaf=True, yang_name="load-balance-type", rest_name="load-balance-type", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'cli-full-command': None, u'cli-drop-node-name': None, u'cli-full-no': None, u'info': u'Load balancing Commands'}}, namespace='urn:brocade.com:mgmt:brocade-rbridge-lag', defining_module='brocade-rbridge-lag', yang_type='enumeration', is_config=True)

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
      return [u'load-balance', u'po-load-balance']

  def _rest_path(self):
    if hasattr(self, "_parent"):
      if self._rest_name:
        return self._parent._rest_path()+[self._rest_name]
      else:
        return self._parent._rest_path()
    else:
      return [u'load-balance']

  def _get_load_balance_type(self):
    """
    Getter method for load_balance_type, mapped from YANG variable /load_balance/po_load_balance/load_balance_type (enumeration)
    """
    return self.__load_balance_type
      
  def _set_load_balance_type(self, v, load=False):
    """
    Setter method for load_balance_type, mapped from YANG variable /load_balance/po_load_balance/load_balance_type (enumeration)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_load_balance_type is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_load_balance_type() directly.
    """
    if hasattr(v, "_utype"):
      v = v._utype(v)
    try:
      t = YANGDynClass(v,base=RestrictedClassType(base_type=unicode,                                     restriction_type="dict_key",                                     restriction_arg={u'src-dst-ip-port': {'value': 6}, u'src-mac-vid': {'value': 2}, u'src-dst-ip': {'value': 4}, u'src-dst-ip-mac-vid': {'value': 5}, u'dst-mac-vid': {'value': 1}, u'src-dst-mac-vid': {'value': 3}, u'src-dst-ip-mac-vid-port': {'value': 7}},), default=unicode("src-dst-ip-mac-vid-port"), is_leaf=True, yang_name="load-balance-type", rest_name="load-balance-type", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'cli-full-command': None, u'cli-drop-node-name': None, u'cli-full-no': None, u'info': u'Load balancing Commands'}}, namespace='urn:brocade.com:mgmt:brocade-rbridge-lag', defining_module='brocade-rbridge-lag', yang_type='enumeration', is_config=True)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """load_balance_type must be of a type compatible with enumeration""",
          'defined-type': "brocade-rbridge-lag:enumeration",
          'generated-type': """YANGDynClass(base=RestrictedClassType(base_type=unicode,                                     restriction_type="dict_key",                                     restriction_arg={u'src-dst-ip-port': {'value': 6}, u'src-mac-vid': {'value': 2}, u'src-dst-ip': {'value': 4}, u'src-dst-ip-mac-vid': {'value': 5}, u'dst-mac-vid': {'value': 1}, u'src-dst-mac-vid': {'value': 3}, u'src-dst-ip-mac-vid-port': {'value': 7}},), default=unicode("src-dst-ip-mac-vid-port"), is_leaf=True, yang_name="load-balance-type", rest_name="load-balance-type", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'cli-full-command': None, u'cli-drop-node-name': None, u'cli-full-no': None, u'info': u'Load balancing Commands'}}, namespace='urn:brocade.com:mgmt:brocade-rbridge-lag', defining_module='brocade-rbridge-lag', yang_type='enumeration', is_config=True)""",
        })

    self.__load_balance_type = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_load_balance_type(self):
    self.__load_balance_type = YANGDynClass(base=RestrictedClassType(base_type=unicode,                                     restriction_type="dict_key",                                     restriction_arg={u'src-dst-ip-port': {'value': 6}, u'src-mac-vid': {'value': 2}, u'src-dst-ip': {'value': 4}, u'src-dst-ip-mac-vid': {'value': 5}, u'dst-mac-vid': {'value': 1}, u'src-dst-mac-vid': {'value': 3}, u'src-dst-ip-mac-vid-port': {'value': 7}},), default=unicode("src-dst-ip-mac-vid-port"), is_leaf=True, yang_name="load-balance-type", rest_name="load-balance-type", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'cli-full-command': None, u'cli-drop-node-name': None, u'cli-full-no': None, u'info': u'Load balancing Commands'}}, namespace='urn:brocade.com:mgmt:brocade-rbridge-lag', defining_module='brocade-rbridge-lag', yang_type='enumeration', is_config=True)

  load_balance_type = __builtin__.property(_get_load_balance_type, _set_load_balance_type)


  _pyangbind_elements = {'load_balance_type': load_balance_type, }


