
from operator import attrgetter
import pyangbind.lib.xpathhelper as xpathhelper
from pyangbind.lib.yangtypes import RestrictedPrecisionDecimalType, RestrictedClassType, TypedListType
from pyangbind.lib.yangtypes import YANGBool, YANGListType, YANGDynClass, ReferenceType
from pyangbind.lib.base import PybindBase
from decimal import Decimal
from bitarray import bitarray
import __builtin__
import meterband_info_list
class meter_id(PybindBase):
  """
  This class was auto-generated by the PythonClass plugin for PYANG
  from YANG module brocade-openflow-operational - based on the path /openflow-state/meter-id. Each member element of
  the container is represented as a class variable - with a specific
  YANG type.
  """
  __slots__ = ('_pybind_generated_by', '_path_helper', '_yang_name', '_rest_name', '_extmethods', '__meter_id','__transaction_id','__meterflags_type','__flow_count','__num_of_bands','__in_packet_count','__in_byte_count','__meterband_info_list',)

  _yang_name = 'meter-id'
  _rest_name = 'meter-id'

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
    self.__meterflags_type = YANGDynClass(base=unicode, is_leaf=True, yang_name="meterflags-type", rest_name="meterflags-type", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='urn:brocade.com:mgmt:brocade-openflow-operational', defining_module='brocade-openflow-operational', yang_type='string', is_config=False)
    self.__num_of_bands = YANGDynClass(base=RestrictedClassType(base_type=long, restriction_dict={'range': ['0..4294967295']}, int_size=32), is_leaf=True, yang_name="num-of-bands", rest_name="num-of-bands", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='urn:brocade.com:mgmt:brocade-openflow-operational', defining_module='brocade-openflow-operational', yang_type='uint32', is_config=False)
    self.__meterband_info_list = YANGDynClass(base=YANGListType("band_type",meterband_info_list.meterband_info_list, yang_name="meterband-info-list", rest_name="meterband-info-list", parent=self, is_container='list', user_ordered=False, path_helper=self._path_helper, yang_keys='band-type', extensions={u'tailf-common': {u'callpoint': u'openflow-meterband-info', u'cli-suppress-show-path': None}}), is_container='list', yang_name="meterband-info-list", rest_name="meterband-info-list", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'callpoint': u'openflow-meterband-info', u'cli-suppress-show-path': None}}, namespace='urn:brocade.com:mgmt:brocade-openflow-operational', defining_module='brocade-openflow-operational', yang_type='list', is_config=False)
    self.__in_byte_count = YANGDynClass(base=RestrictedClassType(base_type=long, restriction_dict={'range': ['0..4294967295']}, int_size=32), is_leaf=True, yang_name="in-byte-count", rest_name="in-byte-count", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='urn:brocade.com:mgmt:brocade-openflow-operational', defining_module='brocade-openflow-operational', yang_type='uint32', is_config=False)
    self.__in_packet_count = YANGDynClass(base=RestrictedClassType(base_type=long, restriction_dict={'range': ['0..4294967295']}, int_size=32), is_leaf=True, yang_name="in-packet-count", rest_name="in-packet-count", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='urn:brocade.com:mgmt:brocade-openflow-operational', defining_module='brocade-openflow-operational', yang_type='uint32', is_config=False)
    self.__meter_id = YANGDynClass(base=RestrictedClassType(base_type=long, restriction_dict={'range': ['0..4294967295']}, int_size=32), is_leaf=True, yang_name="meter-id", rest_name="meter-id", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='urn:brocade.com:mgmt:brocade-openflow-operational', defining_module='brocade-openflow-operational', yang_type='uint32', is_config=False)
    self.__flow_count = YANGDynClass(base=RestrictedClassType(base_type=long, restriction_dict={'range': ['0..4294967295']}, int_size=32), is_leaf=True, yang_name="flow-count", rest_name="flow-count", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='urn:brocade.com:mgmt:brocade-openflow-operational', defining_module='brocade-openflow-operational', yang_type='uint32', is_config=False)
    self.__transaction_id = YANGDynClass(base=unicode, is_leaf=True, yang_name="transaction-id", rest_name="transaction-id", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='urn:brocade.com:mgmt:brocade-openflow-operational', defining_module='brocade-openflow-operational', yang_type='string', is_config=False)

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
      return [u'openflow-state', u'meter-id']

  def _rest_path(self):
    if hasattr(self, "_parent"):
      if self._rest_name:
        return self._parent._rest_path()+[self._rest_name]
      else:
        return self._parent._rest_path()
    else:
      return [u'openflow-state', u'meter-id']

  def _get_meter_id(self):
    """
    Getter method for meter_id, mapped from YANG variable /openflow_state/meter_id/meter_id (uint32)

    YANG Description: Meter id
    """
    return self.__meter_id
      
  def _set_meter_id(self, v, load=False):
    """
    Setter method for meter_id, mapped from YANG variable /openflow_state/meter_id/meter_id (uint32)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_meter_id is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_meter_id() directly.

    YANG Description: Meter id
    """
    if hasattr(v, "_utype"):
      v = v._utype(v)
    try:
      t = YANGDynClass(v,base=RestrictedClassType(base_type=long, restriction_dict={'range': ['0..4294967295']}, int_size=32), is_leaf=True, yang_name="meter-id", rest_name="meter-id", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='urn:brocade.com:mgmt:brocade-openflow-operational', defining_module='brocade-openflow-operational', yang_type='uint32', is_config=False)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """meter_id must be of a type compatible with uint32""",
          'defined-type': "uint32",
          'generated-type': """YANGDynClass(base=RestrictedClassType(base_type=long, restriction_dict={'range': ['0..4294967295']}, int_size=32), is_leaf=True, yang_name="meter-id", rest_name="meter-id", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='urn:brocade.com:mgmt:brocade-openflow-operational', defining_module='brocade-openflow-operational', yang_type='uint32', is_config=False)""",
        })

    self.__meter_id = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_meter_id(self):
    self.__meter_id = YANGDynClass(base=RestrictedClassType(base_type=long, restriction_dict={'range': ['0..4294967295']}, int_size=32), is_leaf=True, yang_name="meter-id", rest_name="meter-id", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='urn:brocade.com:mgmt:brocade-openflow-operational', defining_module='brocade-openflow-operational', yang_type='uint32', is_config=False)


  def _get_transaction_id(self):
    """
    Getter method for transaction_id, mapped from YANG variable /openflow_state/meter_id/transaction_id (string)

    YANG Description: Transaction id
    """
    return self.__transaction_id
      
  def _set_transaction_id(self, v, load=False):
    """
    Setter method for transaction_id, mapped from YANG variable /openflow_state/meter_id/transaction_id (string)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_transaction_id is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_transaction_id() directly.

    YANG Description: Transaction id
    """
    if hasattr(v, "_utype"):
      v = v._utype(v)
    try:
      t = YANGDynClass(v,base=unicode, is_leaf=True, yang_name="transaction-id", rest_name="transaction-id", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='urn:brocade.com:mgmt:brocade-openflow-operational', defining_module='brocade-openflow-operational', yang_type='string', is_config=False)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """transaction_id must be of a type compatible with string""",
          'defined-type': "string",
          'generated-type': """YANGDynClass(base=unicode, is_leaf=True, yang_name="transaction-id", rest_name="transaction-id", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='urn:brocade.com:mgmt:brocade-openflow-operational', defining_module='brocade-openflow-operational', yang_type='string', is_config=False)""",
        })

    self.__transaction_id = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_transaction_id(self):
    self.__transaction_id = YANGDynClass(base=unicode, is_leaf=True, yang_name="transaction-id", rest_name="transaction-id", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='urn:brocade.com:mgmt:brocade-openflow-operational', defining_module='brocade-openflow-operational', yang_type='string', is_config=False)


  def _get_meterflags_type(self):
    """
    Getter method for meterflags_type, mapped from YANG variable /openflow_state/meter_id/meterflags_type (string)

    YANG Description: Meter flags
    """
    return self.__meterflags_type
      
  def _set_meterflags_type(self, v, load=False):
    """
    Setter method for meterflags_type, mapped from YANG variable /openflow_state/meter_id/meterflags_type (string)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_meterflags_type is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_meterflags_type() directly.

    YANG Description: Meter flags
    """
    if hasattr(v, "_utype"):
      v = v._utype(v)
    try:
      t = YANGDynClass(v,base=unicode, is_leaf=True, yang_name="meterflags-type", rest_name="meterflags-type", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='urn:brocade.com:mgmt:brocade-openflow-operational', defining_module='brocade-openflow-operational', yang_type='string', is_config=False)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """meterflags_type must be of a type compatible with string""",
          'defined-type': "string",
          'generated-type': """YANGDynClass(base=unicode, is_leaf=True, yang_name="meterflags-type", rest_name="meterflags-type", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='urn:brocade.com:mgmt:brocade-openflow-operational', defining_module='brocade-openflow-operational', yang_type='string', is_config=False)""",
        })

    self.__meterflags_type = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_meterflags_type(self):
    self.__meterflags_type = YANGDynClass(base=unicode, is_leaf=True, yang_name="meterflags-type", rest_name="meterflags-type", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='urn:brocade.com:mgmt:brocade-openflow-operational', defining_module='brocade-openflow-operational', yang_type='string', is_config=False)


  def _get_flow_count(self):
    """
    Getter method for flow_count, mapped from YANG variable /openflow_state/meter_id/flow_count (uint32)

    YANG Description: Flow Count
    """
    return self.__flow_count
      
  def _set_flow_count(self, v, load=False):
    """
    Setter method for flow_count, mapped from YANG variable /openflow_state/meter_id/flow_count (uint32)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_flow_count is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_flow_count() directly.

    YANG Description: Flow Count
    """
    if hasattr(v, "_utype"):
      v = v._utype(v)
    try:
      t = YANGDynClass(v,base=RestrictedClassType(base_type=long, restriction_dict={'range': ['0..4294967295']}, int_size=32), is_leaf=True, yang_name="flow-count", rest_name="flow-count", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='urn:brocade.com:mgmt:brocade-openflow-operational', defining_module='brocade-openflow-operational', yang_type='uint32', is_config=False)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """flow_count must be of a type compatible with uint32""",
          'defined-type': "uint32",
          'generated-type': """YANGDynClass(base=RestrictedClassType(base_type=long, restriction_dict={'range': ['0..4294967295']}, int_size=32), is_leaf=True, yang_name="flow-count", rest_name="flow-count", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='urn:brocade.com:mgmt:brocade-openflow-operational', defining_module='brocade-openflow-operational', yang_type='uint32', is_config=False)""",
        })

    self.__flow_count = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_flow_count(self):
    self.__flow_count = YANGDynClass(base=RestrictedClassType(base_type=long, restriction_dict={'range': ['0..4294967295']}, int_size=32), is_leaf=True, yang_name="flow-count", rest_name="flow-count", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='urn:brocade.com:mgmt:brocade-openflow-operational', defining_module='brocade-openflow-operational', yang_type='uint32', is_config=False)


  def _get_num_of_bands(self):
    """
    Getter method for num_of_bands, mapped from YANG variable /openflow_state/meter_id/num_of_bands (uint32)

    YANG Description: Number of  bands
    """
    return self.__num_of_bands
      
  def _set_num_of_bands(self, v, load=False):
    """
    Setter method for num_of_bands, mapped from YANG variable /openflow_state/meter_id/num_of_bands (uint32)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_num_of_bands is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_num_of_bands() directly.

    YANG Description: Number of  bands
    """
    if hasattr(v, "_utype"):
      v = v._utype(v)
    try:
      t = YANGDynClass(v,base=RestrictedClassType(base_type=long, restriction_dict={'range': ['0..4294967295']}, int_size=32), is_leaf=True, yang_name="num-of-bands", rest_name="num-of-bands", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='urn:brocade.com:mgmt:brocade-openflow-operational', defining_module='brocade-openflow-operational', yang_type='uint32', is_config=False)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """num_of_bands must be of a type compatible with uint32""",
          'defined-type': "uint32",
          'generated-type': """YANGDynClass(base=RestrictedClassType(base_type=long, restriction_dict={'range': ['0..4294967295']}, int_size=32), is_leaf=True, yang_name="num-of-bands", rest_name="num-of-bands", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='urn:brocade.com:mgmt:brocade-openflow-operational', defining_module='brocade-openflow-operational', yang_type='uint32', is_config=False)""",
        })

    self.__num_of_bands = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_num_of_bands(self):
    self.__num_of_bands = YANGDynClass(base=RestrictedClassType(base_type=long, restriction_dict={'range': ['0..4294967295']}, int_size=32), is_leaf=True, yang_name="num-of-bands", rest_name="num-of-bands", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='urn:brocade.com:mgmt:brocade-openflow-operational', defining_module='brocade-openflow-operational', yang_type='uint32', is_config=False)


  def _get_in_packet_count(self):
    """
    Getter method for in_packet_count, mapped from YANG variable /openflow_state/meter_id/in_packet_count (uint32)

    YANG Description: In packet count
    """
    return self.__in_packet_count
      
  def _set_in_packet_count(self, v, load=False):
    """
    Setter method for in_packet_count, mapped from YANG variable /openflow_state/meter_id/in_packet_count (uint32)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_in_packet_count is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_in_packet_count() directly.

    YANG Description: In packet count
    """
    if hasattr(v, "_utype"):
      v = v._utype(v)
    try:
      t = YANGDynClass(v,base=RestrictedClassType(base_type=long, restriction_dict={'range': ['0..4294967295']}, int_size=32), is_leaf=True, yang_name="in-packet-count", rest_name="in-packet-count", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='urn:brocade.com:mgmt:brocade-openflow-operational', defining_module='brocade-openflow-operational', yang_type='uint32', is_config=False)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """in_packet_count must be of a type compatible with uint32""",
          'defined-type': "uint32",
          'generated-type': """YANGDynClass(base=RestrictedClassType(base_type=long, restriction_dict={'range': ['0..4294967295']}, int_size=32), is_leaf=True, yang_name="in-packet-count", rest_name="in-packet-count", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='urn:brocade.com:mgmt:brocade-openflow-operational', defining_module='brocade-openflow-operational', yang_type='uint32', is_config=False)""",
        })

    self.__in_packet_count = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_in_packet_count(self):
    self.__in_packet_count = YANGDynClass(base=RestrictedClassType(base_type=long, restriction_dict={'range': ['0..4294967295']}, int_size=32), is_leaf=True, yang_name="in-packet-count", rest_name="in-packet-count", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='urn:brocade.com:mgmt:brocade-openflow-operational', defining_module='brocade-openflow-operational', yang_type='uint32', is_config=False)


  def _get_in_byte_count(self):
    """
    Getter method for in_byte_count, mapped from YANG variable /openflow_state/meter_id/in_byte_count (uint32)

    YANG Description: In byte count
    """
    return self.__in_byte_count
      
  def _set_in_byte_count(self, v, load=False):
    """
    Setter method for in_byte_count, mapped from YANG variable /openflow_state/meter_id/in_byte_count (uint32)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_in_byte_count is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_in_byte_count() directly.

    YANG Description: In byte count
    """
    if hasattr(v, "_utype"):
      v = v._utype(v)
    try:
      t = YANGDynClass(v,base=RestrictedClassType(base_type=long, restriction_dict={'range': ['0..4294967295']}, int_size=32), is_leaf=True, yang_name="in-byte-count", rest_name="in-byte-count", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='urn:brocade.com:mgmt:brocade-openflow-operational', defining_module='brocade-openflow-operational', yang_type='uint32', is_config=False)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """in_byte_count must be of a type compatible with uint32""",
          'defined-type': "uint32",
          'generated-type': """YANGDynClass(base=RestrictedClassType(base_type=long, restriction_dict={'range': ['0..4294967295']}, int_size=32), is_leaf=True, yang_name="in-byte-count", rest_name="in-byte-count", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='urn:brocade.com:mgmt:brocade-openflow-operational', defining_module='brocade-openflow-operational', yang_type='uint32', is_config=False)""",
        })

    self.__in_byte_count = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_in_byte_count(self):
    self.__in_byte_count = YANGDynClass(base=RestrictedClassType(base_type=long, restriction_dict={'range': ['0..4294967295']}, int_size=32), is_leaf=True, yang_name="in-byte-count", rest_name="in-byte-count", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='urn:brocade.com:mgmt:brocade-openflow-operational', defining_module='brocade-openflow-operational', yang_type='uint32', is_config=False)


  def _get_meterband_info_list(self):
    """
    Getter method for meterband_info_list, mapped from YANG variable /openflow_state/meter_id/meterband_info_list (list)

    YANG Description: Meterband details
    """
    return self.__meterband_info_list
      
  def _set_meterband_info_list(self, v, load=False):
    """
    Setter method for meterband_info_list, mapped from YANG variable /openflow_state/meter_id/meterband_info_list (list)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_meterband_info_list is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_meterband_info_list() directly.

    YANG Description: Meterband details
    """
    if hasattr(v, "_utype"):
      v = v._utype(v)
    try:
      t = YANGDynClass(v,base=YANGListType("band_type",meterband_info_list.meterband_info_list, yang_name="meterband-info-list", rest_name="meterband-info-list", parent=self, is_container='list', user_ordered=False, path_helper=self._path_helper, yang_keys='band-type', extensions={u'tailf-common': {u'callpoint': u'openflow-meterband-info', u'cli-suppress-show-path': None}}), is_container='list', yang_name="meterband-info-list", rest_name="meterband-info-list", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'callpoint': u'openflow-meterband-info', u'cli-suppress-show-path': None}}, namespace='urn:brocade.com:mgmt:brocade-openflow-operational', defining_module='brocade-openflow-operational', yang_type='list', is_config=False)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """meterband_info_list must be of a type compatible with list""",
          'defined-type': "list",
          'generated-type': """YANGDynClass(base=YANGListType("band_type",meterband_info_list.meterband_info_list, yang_name="meterband-info-list", rest_name="meterband-info-list", parent=self, is_container='list', user_ordered=False, path_helper=self._path_helper, yang_keys='band-type', extensions={u'tailf-common': {u'callpoint': u'openflow-meterband-info', u'cli-suppress-show-path': None}}), is_container='list', yang_name="meterband-info-list", rest_name="meterband-info-list", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'callpoint': u'openflow-meterband-info', u'cli-suppress-show-path': None}}, namespace='urn:brocade.com:mgmt:brocade-openflow-operational', defining_module='brocade-openflow-operational', yang_type='list', is_config=False)""",
        })

    self.__meterband_info_list = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_meterband_info_list(self):
    self.__meterband_info_list = YANGDynClass(base=YANGListType("band_type",meterband_info_list.meterband_info_list, yang_name="meterband-info-list", rest_name="meterband-info-list", parent=self, is_container='list', user_ordered=False, path_helper=self._path_helper, yang_keys='band-type', extensions={u'tailf-common': {u'callpoint': u'openflow-meterband-info', u'cli-suppress-show-path': None}}), is_container='list', yang_name="meterband-info-list", rest_name="meterband-info-list", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'callpoint': u'openflow-meterband-info', u'cli-suppress-show-path': None}}, namespace='urn:brocade.com:mgmt:brocade-openflow-operational', defining_module='brocade-openflow-operational', yang_type='list', is_config=False)

  meter_id = __builtin__.property(_get_meter_id)
  transaction_id = __builtin__.property(_get_transaction_id)
  meterflags_type = __builtin__.property(_get_meterflags_type)
  flow_count = __builtin__.property(_get_flow_count)
  num_of_bands = __builtin__.property(_get_num_of_bands)
  in_packet_count = __builtin__.property(_get_in_packet_count)
  in_byte_count = __builtin__.property(_get_in_byte_count)
  meterband_info_list = __builtin__.property(_get_meterband_info_list)


  _pyangbind_elements = {'meter_id': meter_id, 'transaction_id': transaction_id, 'meterflags_type': meterflags_type, 'flow_count': flow_count, 'num_of_bands': num_of_bands, 'in_packet_count': in_packet_count, 'in_byte_count': in_byte_count, 'meterband_info_list': meterband_info_list, }


