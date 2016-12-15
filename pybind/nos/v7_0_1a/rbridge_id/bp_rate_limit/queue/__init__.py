
from operator import attrgetter
import pyangbind.lib.xpathhelper as xpathhelper
from pyangbind.lib.yangtypes import RestrictedPrecisionDecimalType, RestrictedClassType, TypedListType
from pyangbind.lib.yangtypes import YANGBool, YANGListType, YANGDynClass, ReferenceType
from pyangbind.lib.base import PybindBase
from decimal import Decimal
from bitarray import bitarray
import __builtin__
class queue(PybindBase):
  """
  This class was auto-generated by the PythonClass plugin for PYANG
  from YANG module brocade-rbridge - based on the path /rbridge-id/bp-rate-limit/queue. Each member element of
  the container is represented as a class variable - with a specific
  YANG type.
  """
  __slots__ = ('_pybind_generated_by', '_path_helper', '_yang_name', '_rest_name', '_extmethods', '__queue_id','__limit_percent',)

  _yang_name = 'queue'
  _rest_name = 'queue'

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
    self.__limit_percent = YANGDynClass(base=RestrictedClassType(base_type=RestrictedClassType(base_type=long, restriction_dict={'range': ['0..4294967295']}, int_size=32), restriction_dict={'range': [u'3 .. 100']}), is_leaf=True, yang_name="limit-percent", rest_name="limit-percent", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'info': u'BP queue limit in percentage'}}, namespace='urn:brocade.com:mgmt:brocade-bprate-limit', defining_module='brocade-bprate-limit', yang_type='queue-limit-percentage-type', is_config=True)
    self.__queue_id = YANGDynClass(base=RestrictedClassType(base_type=RestrictedClassType(base_type=long, restriction_dict={'range': ['0..4294967295']}, int_size=32), restriction_dict={'range': [u'0..15']}), is_leaf=True, yang_name="queue-id", rest_name="queue-id", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'info': u'BP queue number (only queue 0 is supported)'}}, is_keyval=True, namespace='urn:brocade.com:mgmt:brocade-bprate-limit', defining_module='brocade-bprate-limit', yang_type='queue-id-type', is_config=True)

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
      return [u'rbridge-id', u'bp-rate-limit', u'queue']

  def _rest_path(self):
    if hasattr(self, "_parent"):
      if self._rest_name:
        return self._parent._rest_path()+[self._rest_name]
      else:
        return self._parent._rest_path()
    else:
      return [u'rbridge-id', u'bp-rate-limit', u'queue']

  def _get_queue_id(self):
    """
    Getter method for queue_id, mapped from YANG variable /rbridge_id/bp_rate_limit/queue/queue_id (queue-id-type)
    """
    return self.__queue_id
      
  def _set_queue_id(self, v, load=False):
    """
    Setter method for queue_id, mapped from YANG variable /rbridge_id/bp_rate_limit/queue/queue_id (queue-id-type)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_queue_id is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_queue_id() directly.
    """
    parent = getattr(self, "_parent", None)
    if parent is not None and load is False:
      raise AttributeError("Cannot set keys directly when" +
                             " within an instantiated list")

    if hasattr(v, "_utype"):
      v = v._utype(v)
    try:
      t = YANGDynClass(v,base=RestrictedClassType(base_type=RestrictedClassType(base_type=long, restriction_dict={'range': ['0..4294967295']}, int_size=32), restriction_dict={'range': [u'0..15']}), is_leaf=True, yang_name="queue-id", rest_name="queue-id", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'info': u'BP queue number (only queue 0 is supported)'}}, is_keyval=True, namespace='urn:brocade.com:mgmt:brocade-bprate-limit', defining_module='brocade-bprate-limit', yang_type='queue-id-type', is_config=True)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """queue_id must be of a type compatible with queue-id-type""",
          'defined-type': "brocade-bprate-limit:queue-id-type",
          'generated-type': """YANGDynClass(base=RestrictedClassType(base_type=RestrictedClassType(base_type=long, restriction_dict={'range': ['0..4294967295']}, int_size=32), restriction_dict={'range': [u'0..15']}), is_leaf=True, yang_name="queue-id", rest_name="queue-id", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'info': u'BP queue number (only queue 0 is supported)'}}, is_keyval=True, namespace='urn:brocade.com:mgmt:brocade-bprate-limit', defining_module='brocade-bprate-limit', yang_type='queue-id-type', is_config=True)""",
        })

    self.__queue_id = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_queue_id(self):
    self.__queue_id = YANGDynClass(base=RestrictedClassType(base_type=RestrictedClassType(base_type=long, restriction_dict={'range': ['0..4294967295']}, int_size=32), restriction_dict={'range': [u'0..15']}), is_leaf=True, yang_name="queue-id", rest_name="queue-id", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'info': u'BP queue number (only queue 0 is supported)'}}, is_keyval=True, namespace='urn:brocade.com:mgmt:brocade-bprate-limit', defining_module='brocade-bprate-limit', yang_type='queue-id-type', is_config=True)


  def _get_limit_percent(self):
    """
    Getter method for limit_percent, mapped from YANG variable /rbridge_id/bp_rate_limit/queue/limit_percent (queue-limit-percentage-type)
    """
    return self.__limit_percent
      
  def _set_limit_percent(self, v, load=False):
    """
    Setter method for limit_percent, mapped from YANG variable /rbridge_id/bp_rate_limit/queue/limit_percent (queue-limit-percentage-type)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_limit_percent is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_limit_percent() directly.
    """
    if hasattr(v, "_utype"):
      v = v._utype(v)
    try:
      t = YANGDynClass(v,base=RestrictedClassType(base_type=RestrictedClassType(base_type=long, restriction_dict={'range': ['0..4294967295']}, int_size=32), restriction_dict={'range': [u'3 .. 100']}), is_leaf=True, yang_name="limit-percent", rest_name="limit-percent", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'info': u'BP queue limit in percentage'}}, namespace='urn:brocade.com:mgmt:brocade-bprate-limit', defining_module='brocade-bprate-limit', yang_type='queue-limit-percentage-type', is_config=True)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """limit_percent must be of a type compatible with queue-limit-percentage-type""",
          'defined-type': "brocade-bprate-limit:queue-limit-percentage-type",
          'generated-type': """YANGDynClass(base=RestrictedClassType(base_type=RestrictedClassType(base_type=long, restriction_dict={'range': ['0..4294967295']}, int_size=32), restriction_dict={'range': [u'3 .. 100']}), is_leaf=True, yang_name="limit-percent", rest_name="limit-percent", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'info': u'BP queue limit in percentage'}}, namespace='urn:brocade.com:mgmt:brocade-bprate-limit', defining_module='brocade-bprate-limit', yang_type='queue-limit-percentage-type', is_config=True)""",
        })

    self.__limit_percent = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_limit_percent(self):
    self.__limit_percent = YANGDynClass(base=RestrictedClassType(base_type=RestrictedClassType(base_type=long, restriction_dict={'range': ['0..4294967295']}, int_size=32), restriction_dict={'range': [u'3 .. 100']}), is_leaf=True, yang_name="limit-percent", rest_name="limit-percent", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'info': u'BP queue limit in percentage'}}, namespace='urn:brocade.com:mgmt:brocade-bprate-limit', defining_module='brocade-bprate-limit', yang_type='queue-limit-percentage-type', is_config=True)

  queue_id = __builtin__.property(_get_queue_id, _set_queue_id)
  limit_percent = __builtin__.property(_get_limit_percent, _set_limit_percent)


  _pyangbind_elements = {'queue_id': queue_id, 'limit_percent': limit_percent, }


