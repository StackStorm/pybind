
from operator import attrgetter
import pyangbind.lib.xpathhelper as xpathhelper
from pyangbind.lib.yangtypes import RestrictedPrecisionDecimalType, RestrictedClassType, TypedListType
from pyangbind.lib.yangtypes import YANGBool, YANGListType, YANGDynClass, ReferenceType
from pyangbind.lib.base import PybindBase
from decimal import Decimal
from bitarray import bitarray
import __builtin__
class dad_status_entries(PybindBase):
  """
  This class was auto-generated by the PythonClass plugin for PYANG
  from YANG module brocade-firmware - based on the path /brocade_firmware_rpc/dad-status/output/dad-status-entries. Each member element of
  the container is represented as a class variable - with a specific
  YANG type.
  """
  __slots__ = ('_pybind_generated_by', '_path_helper', '_yang_name', '_rest_name', '_extmethods', '__index','__date_and_time_info','__message',)

  _yang_name = 'dad-status-entries'
  _rest_name = 'dad-status-entries'

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
    self.__index = YANGDynClass(base=RestrictedClassType(base_type=long, restriction_dict={'range': ['0..4294967295']}, int_size=32), is_leaf=True, yang_name="index", rest_name="index", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=False, extensions={u'tailf-common': {u'info': u'Sequence number for the message'}}, namespace='urn:brocade.com:mgmt:brocade-firmware', defining_module='brocade-firmware', yang_type='uint32', is_config=True)
    self.__message = YANGDynClass(base=unicode, is_leaf=True, yang_name="message", rest_name="message", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=False, extensions={u'tailf-common': {u'info': u'Textual description of the status'}}, namespace='urn:brocade.com:mgmt:brocade-firmware', defining_module='brocade-firmware', yang_type='string', is_config=True)
    self.__date_and_time_info = YANGDynClass(base=unicode, is_leaf=True, yang_name="date-and-time-info", rest_name="date-and-time-info", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=False, extensions={u'tailf-common': {u'info': u'Date and time of the message. The format is YYYY-MM-DD/HH:MM:SS.SSSS (micro seconds)'}}, namespace='urn:brocade.com:mgmt:brocade-firmware', defining_module='brocade-firmware', yang_type='string', is_config=True)

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
      return [u'brocade_firmware_rpc', u'dad-status', u'output', u'dad-status-entries']

  def _rest_path(self):
    if hasattr(self, "_parent"):
      if self._rest_name:
        return self._parent._rest_path()+[self._rest_name]
      else:
        return self._parent._rest_path()
    else:
      return [u'dad-status', u'output', u'dad-status-entries']

  def _get_index(self):
    """
    Getter method for index, mapped from YANG variable /brocade_firmware_rpc/dad_status/output/dad_status_entries/index (uint32)
    """
    return self.__index
      
  def _set_index(self, v, load=False):
    """
    Setter method for index, mapped from YANG variable /brocade_firmware_rpc/dad_status/output/dad_status_entries/index (uint32)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_index is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_index() directly.
    """
    if hasattr(v, "_utype"):
      v = v._utype(v)
    try:
      t = YANGDynClass(v,base=RestrictedClassType(base_type=long, restriction_dict={'range': ['0..4294967295']}, int_size=32), is_leaf=True, yang_name="index", rest_name="index", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=False, extensions={u'tailf-common': {u'info': u'Sequence number for the message'}}, namespace='urn:brocade.com:mgmt:brocade-firmware', defining_module='brocade-firmware', yang_type='uint32', is_config=True)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """index must be of a type compatible with uint32""",
          'defined-type': "uint32",
          'generated-type': """YANGDynClass(base=RestrictedClassType(base_type=long, restriction_dict={'range': ['0..4294967295']}, int_size=32), is_leaf=True, yang_name="index", rest_name="index", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=False, extensions={u'tailf-common': {u'info': u'Sequence number for the message'}}, namespace='urn:brocade.com:mgmt:brocade-firmware', defining_module='brocade-firmware', yang_type='uint32', is_config=True)""",
        })

    self.__index = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_index(self):
    self.__index = YANGDynClass(base=RestrictedClassType(base_type=long, restriction_dict={'range': ['0..4294967295']}, int_size=32), is_leaf=True, yang_name="index", rest_name="index", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=False, extensions={u'tailf-common': {u'info': u'Sequence number for the message'}}, namespace='urn:brocade.com:mgmt:brocade-firmware', defining_module='brocade-firmware', yang_type='uint32', is_config=True)


  def _get_date_and_time_info(self):
    """
    Getter method for date_and_time_info, mapped from YANG variable /brocade_firmware_rpc/dad_status/output/dad_status_entries/date_and_time_info (string)
    """
    return self.__date_and_time_info
      
  def _set_date_and_time_info(self, v, load=False):
    """
    Setter method for date_and_time_info, mapped from YANG variable /brocade_firmware_rpc/dad_status/output/dad_status_entries/date_and_time_info (string)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_date_and_time_info is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_date_and_time_info() directly.
    """
    if hasattr(v, "_utype"):
      v = v._utype(v)
    try:
      t = YANGDynClass(v,base=unicode, is_leaf=True, yang_name="date-and-time-info", rest_name="date-and-time-info", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=False, extensions={u'tailf-common': {u'info': u'Date and time of the message. The format is YYYY-MM-DD/HH:MM:SS.SSSS (micro seconds)'}}, namespace='urn:brocade.com:mgmt:brocade-firmware', defining_module='brocade-firmware', yang_type='string', is_config=True)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """date_and_time_info must be of a type compatible with string""",
          'defined-type': "string",
          'generated-type': """YANGDynClass(base=unicode, is_leaf=True, yang_name="date-and-time-info", rest_name="date-and-time-info", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=False, extensions={u'tailf-common': {u'info': u'Date and time of the message. The format is YYYY-MM-DD/HH:MM:SS.SSSS (micro seconds)'}}, namespace='urn:brocade.com:mgmt:brocade-firmware', defining_module='brocade-firmware', yang_type='string', is_config=True)""",
        })

    self.__date_and_time_info = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_date_and_time_info(self):
    self.__date_and_time_info = YANGDynClass(base=unicode, is_leaf=True, yang_name="date-and-time-info", rest_name="date-and-time-info", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=False, extensions={u'tailf-common': {u'info': u'Date and time of the message. The format is YYYY-MM-DD/HH:MM:SS.SSSS (micro seconds)'}}, namespace='urn:brocade.com:mgmt:brocade-firmware', defining_module='brocade-firmware', yang_type='string', is_config=True)


  def _get_message(self):
    """
    Getter method for message, mapped from YANG variable /brocade_firmware_rpc/dad_status/output/dad_status_entries/message (string)
    """
    return self.__message
      
  def _set_message(self, v, load=False):
    """
    Setter method for message, mapped from YANG variable /brocade_firmware_rpc/dad_status/output/dad_status_entries/message (string)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_message is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_message() directly.
    """
    if hasattr(v, "_utype"):
      v = v._utype(v)
    try:
      t = YANGDynClass(v,base=unicode, is_leaf=True, yang_name="message", rest_name="message", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=False, extensions={u'tailf-common': {u'info': u'Textual description of the status'}}, namespace='urn:brocade.com:mgmt:brocade-firmware', defining_module='brocade-firmware', yang_type='string', is_config=True)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """message must be of a type compatible with string""",
          'defined-type': "string",
          'generated-type': """YANGDynClass(base=unicode, is_leaf=True, yang_name="message", rest_name="message", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=False, extensions={u'tailf-common': {u'info': u'Textual description of the status'}}, namespace='urn:brocade.com:mgmt:brocade-firmware', defining_module='brocade-firmware', yang_type='string', is_config=True)""",
        })

    self.__message = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_message(self):
    self.__message = YANGDynClass(base=unicode, is_leaf=True, yang_name="message", rest_name="message", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=False, extensions={u'tailf-common': {u'info': u'Textual description of the status'}}, namespace='urn:brocade.com:mgmt:brocade-firmware', defining_module='brocade-firmware', yang_type='string', is_config=True)

  index = __builtin__.property(_get_index, _set_index)
  date_and_time_info = __builtin__.property(_get_date_and_time_info, _set_date_and_time_info)
  message = __builtin__.property(_get_message, _set_message)


  _pyangbind_elements = {'index': index, 'date_and_time_info': date_and_time_info, 'message': message, }


