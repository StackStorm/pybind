
from operator import attrgetter
import pyangbind.lib.xpathhelper as xpathhelper
from pyangbind.lib.yangtypes import RestrictedPrecisionDecimalType, RestrictedClassType, TypedListType
from pyangbind.lib.yangtypes import YANGBool, YANGListType, YANGDynClass, ReferenceType
from pyangbind.lib.base import PybindBase
from decimal import Decimal
from bitarray import bitarray
import __builtin__
import cpu_queue_info_details
class cpu_queue_info_state(PybindBase):
  """
  This class was auto-generated by the PythonClass plugin for PYANG
  from YANG module brocade-ssm-operational - based on the path /cpu-queue-info-state. Each member element of
  the container is represented as a class variable - with a specific
  YANG type.

  YANG Description: QoS CPU Queue info
  """
  __slots__ = ('_pybind_generated_by', '_path_helper', '_yang_name', '_rest_name', '_extmethods', '__credits','__cpu_queue_info_details',)

  _yang_name = 'cpu-queue-info-state'
  _rest_name = 'cpu-queue-info-state'

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
    self.__credits = YANGDynClass(base=RestrictedClassType(base_type=long, restriction_dict={'range': ['0..4294967295']}, int_size=32), is_leaf=True, yang_name="credits", rest_name="credits", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='urn:brocade.com:mgmt:brocade-ssm-operational', defining_module='brocade-ssm-operational', yang_type='uint32', is_config=False)
    self.__cpu_queue_info_details = YANGDynClass(base=YANGListType("queue_id",cpu_queue_info_details.cpu_queue_info_details, yang_name="cpu-queue-info-details", rest_name="cpu-queue-info-details", parent=self, is_container='list', user_ordered=False, path_helper=self._path_helper, yang_keys='queue-id', extensions={u'tailf-common': {u'callpoint': u'ssm-cpu-queue-info-details', u'cli-suppress-show-path': None}}), is_container='list', yang_name="cpu-queue-info-details", rest_name="cpu-queue-info-details", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'callpoint': u'ssm-cpu-queue-info-details', u'cli-suppress-show-path': None}}, namespace='urn:brocade.com:mgmt:brocade-ssm-operational', defining_module='brocade-ssm-operational', yang_type='list', is_config=False)

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
      return [u'cpu-queue-info-state']

  def _rest_path(self):
    if hasattr(self, "_parent"):
      if self._rest_name:
        return self._parent._rest_path()+[self._rest_name]
      else:
        return self._parent._rest_path()
    else:
      return [u'cpu-queue-info-state']

  def _get_credits(self):
    """
    Getter method for credits, mapped from YANG variable /cpu_queue_info_state/credits (uint32)

    YANG Description: Unused Credits
    """
    return self.__credits
      
  def _set_credits(self, v, load=False):
    """
    Setter method for credits, mapped from YANG variable /cpu_queue_info_state/credits (uint32)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_credits is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_credits() directly.

    YANG Description: Unused Credits
    """
    if hasattr(v, "_utype"):
      v = v._utype(v)
    try:
      t = YANGDynClass(v,base=RestrictedClassType(base_type=long, restriction_dict={'range': ['0..4294967295']}, int_size=32), is_leaf=True, yang_name="credits", rest_name="credits", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='urn:brocade.com:mgmt:brocade-ssm-operational', defining_module='brocade-ssm-operational', yang_type='uint32', is_config=False)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """credits must be of a type compatible with uint32""",
          'defined-type': "uint32",
          'generated-type': """YANGDynClass(base=RestrictedClassType(base_type=long, restriction_dict={'range': ['0..4294967295']}, int_size=32), is_leaf=True, yang_name="credits", rest_name="credits", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='urn:brocade.com:mgmt:brocade-ssm-operational', defining_module='brocade-ssm-operational', yang_type='uint32', is_config=False)""",
        })

    self.__credits = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_credits(self):
    self.__credits = YANGDynClass(base=RestrictedClassType(base_type=long, restriction_dict={'range': ['0..4294967295']}, int_size=32), is_leaf=True, yang_name="credits", rest_name="credits", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='urn:brocade.com:mgmt:brocade-ssm-operational', defining_module='brocade-ssm-operational', yang_type='uint32', is_config=False)


  def _get_cpu_queue_info_details(self):
    """
    Getter method for cpu_queue_info_details, mapped from YANG variable /cpu_queue_info_state/cpu_queue_info_details (list)

    YANG Description: CPU Queue fps and usage
    """
    return self.__cpu_queue_info_details
      
  def _set_cpu_queue_info_details(self, v, load=False):
    """
    Setter method for cpu_queue_info_details, mapped from YANG variable /cpu_queue_info_state/cpu_queue_info_details (list)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_cpu_queue_info_details is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_cpu_queue_info_details() directly.

    YANG Description: CPU Queue fps and usage
    """
    if hasattr(v, "_utype"):
      v = v._utype(v)
    try:
      t = YANGDynClass(v,base=YANGListType("queue_id",cpu_queue_info_details.cpu_queue_info_details, yang_name="cpu-queue-info-details", rest_name="cpu-queue-info-details", parent=self, is_container='list', user_ordered=False, path_helper=self._path_helper, yang_keys='queue-id', extensions={u'tailf-common': {u'callpoint': u'ssm-cpu-queue-info-details', u'cli-suppress-show-path': None}}), is_container='list', yang_name="cpu-queue-info-details", rest_name="cpu-queue-info-details", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'callpoint': u'ssm-cpu-queue-info-details', u'cli-suppress-show-path': None}}, namespace='urn:brocade.com:mgmt:brocade-ssm-operational', defining_module='brocade-ssm-operational', yang_type='list', is_config=False)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """cpu_queue_info_details must be of a type compatible with list""",
          'defined-type': "list",
          'generated-type': """YANGDynClass(base=YANGListType("queue_id",cpu_queue_info_details.cpu_queue_info_details, yang_name="cpu-queue-info-details", rest_name="cpu-queue-info-details", parent=self, is_container='list', user_ordered=False, path_helper=self._path_helper, yang_keys='queue-id', extensions={u'tailf-common': {u'callpoint': u'ssm-cpu-queue-info-details', u'cli-suppress-show-path': None}}), is_container='list', yang_name="cpu-queue-info-details", rest_name="cpu-queue-info-details", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'callpoint': u'ssm-cpu-queue-info-details', u'cli-suppress-show-path': None}}, namespace='urn:brocade.com:mgmt:brocade-ssm-operational', defining_module='brocade-ssm-operational', yang_type='list', is_config=False)""",
        })

    self.__cpu_queue_info_details = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_cpu_queue_info_details(self):
    self.__cpu_queue_info_details = YANGDynClass(base=YANGListType("queue_id",cpu_queue_info_details.cpu_queue_info_details, yang_name="cpu-queue-info-details", rest_name="cpu-queue-info-details", parent=self, is_container='list', user_ordered=False, path_helper=self._path_helper, yang_keys='queue-id', extensions={u'tailf-common': {u'callpoint': u'ssm-cpu-queue-info-details', u'cli-suppress-show-path': None}}), is_container='list', yang_name="cpu-queue-info-details", rest_name="cpu-queue-info-details", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'callpoint': u'ssm-cpu-queue-info-details', u'cli-suppress-show-path': None}}, namespace='urn:brocade.com:mgmt:brocade-ssm-operational', defining_module='brocade-ssm-operational', yang_type='list', is_config=False)

  credits = __builtin__.property(_get_credits)
  cpu_queue_info_details = __builtin__.property(_get_cpu_queue_info_details)


  _pyangbind_elements = {'credits': credits, 'cpu_queue_info_details': cpu_queue_info_details, }


