
from operator import attrgetter
import pyangbind.lib.xpathhelper as xpathhelper
from pyangbind.lib.yangtypes import RestrictedPrecisionDecimalType, RestrictedClassType, TypedListType
from pyangbind.lib.yangtypes import YANGBool, YANGListType, YANGDynClass, ReferenceType
from pyangbind.lib.base import PybindBase
from decimal import Decimal
from bitarray import bitarray
import __builtin__
class show_support_save_status(PybindBase):
  """
  This class was auto-generated by the PythonClass plugin for PYANG
  from YANG module brocade-ras-ext - based on the path /brocade_ras_ext_rpc/show-support-save-status/output/show-support-save-status. Each member element of
  the container is represented as a class variable - with a specific
  YANG type.
  """
  __slots__ = ('_pybind_generated_by', '_path_helper', '_yang_name', '_rest_name', '_extmethods', '__rbridge_id','__status','__message','__percentage_of_completion',)

  _yang_name = 'show-support-save-status'
  _rest_name = 'show-support-save-status'

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
    self.__status = YANGDynClass(base=RestrictedClassType(base_type=unicode,                                     restriction_type="dict_key",                                     restriction_arg={u'unknown': {'value': 2}, u'completed': {'value': 3}, u'other': {'value': 1}, u'inProgress': {'value': 4}, u'error': {'value': 5}},), is_leaf=True, yang_name="status", rest_name="status", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=False, namespace='urn:brocade.com:mgmt:brocade-ras-ext', defining_module='brocade-ras-ext', yang_type='enumeration', is_config=True)
    self.__message = YANGDynClass(base=unicode, is_leaf=True, yang_name="message", rest_name="message", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=False, namespace='urn:brocade.com:mgmt:brocade-ras-ext', defining_module='brocade-ras-ext', yang_type='string', is_config=True)
    self.__rbridge_id = YANGDynClass(base=RestrictedClassType(base_type=unicode, restriction_dict={'length': [u'1..3']}), is_leaf=True, yang_name="rbridge-id", rest_name="rbridge-id", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=False, namespace='urn:brocade.com:mgmt:brocade-ras-ext', defining_module='brocade-ras-ext', yang_type='switchid-type', is_config=True)
    self.__percentage_of_completion = YANGDynClass(base=RestrictedClassType(base_type=long, restriction_dict={'range': ['0..4294967295']}, int_size=32), is_leaf=True, yang_name="percentage-of-completion", rest_name="percentage-of-completion", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=False, namespace='urn:brocade.com:mgmt:brocade-ras-ext', defining_module='brocade-ras-ext', yang_type='uint32', is_config=True)

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
      return [u'brocade_ras_ext_rpc', u'show-support-save-status', u'output', u'show-support-save-status']

  def _rest_path(self):
    if hasattr(self, "_parent"):
      if self._rest_name:
        return self._parent._rest_path()+[self._rest_name]
      else:
        return self._parent._rest_path()
    else:
      return [u'show-support-save-status', u'output', u'show-support-save-status']

  def _get_rbridge_id(self):
    """
    Getter method for rbridge_id, mapped from YANG variable /brocade_ras_ext_rpc/show_support_save_status/output/show_support_save_status/rbridge_id (switchid-type)
    """
    return self.__rbridge_id
      
  def _set_rbridge_id(self, v, load=False):
    """
    Setter method for rbridge_id, mapped from YANG variable /brocade_ras_ext_rpc/show_support_save_status/output/show_support_save_status/rbridge_id (switchid-type)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_rbridge_id is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_rbridge_id() directly.
    """
    if hasattr(v, "_utype"):
      v = v._utype(v)
    try:
      t = YANGDynClass(v,base=RestrictedClassType(base_type=unicode, restriction_dict={'length': [u'1..3']}), is_leaf=True, yang_name="rbridge-id", rest_name="rbridge-id", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=False, namespace='urn:brocade.com:mgmt:brocade-ras-ext', defining_module='brocade-ras-ext', yang_type='switchid-type', is_config=True)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """rbridge_id must be of a type compatible with switchid-type""",
          'defined-type': "brocade-ras-ext:switchid-type",
          'generated-type': """YANGDynClass(base=RestrictedClassType(base_type=unicode, restriction_dict={'length': [u'1..3']}), is_leaf=True, yang_name="rbridge-id", rest_name="rbridge-id", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=False, namespace='urn:brocade.com:mgmt:brocade-ras-ext', defining_module='brocade-ras-ext', yang_type='switchid-type', is_config=True)""",
        })

    self.__rbridge_id = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_rbridge_id(self):
    self.__rbridge_id = YANGDynClass(base=RestrictedClassType(base_type=unicode, restriction_dict={'length': [u'1..3']}), is_leaf=True, yang_name="rbridge-id", rest_name="rbridge-id", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=False, namespace='urn:brocade.com:mgmt:brocade-ras-ext', defining_module='brocade-ras-ext', yang_type='switchid-type', is_config=True)


  def _get_status(self):
    """
    Getter method for status, mapped from YANG variable /brocade_ras_ext_rpc/show_support_save_status/output/show_support_save_status/status (enumeration)

    YANG Description: status of recent support save.
    """
    return self.__status
      
  def _set_status(self, v, load=False):
    """
    Setter method for status, mapped from YANG variable /brocade_ras_ext_rpc/show_support_save_status/output/show_support_save_status/status (enumeration)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_status is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_status() directly.

    YANG Description: status of recent support save.
    """
    if hasattr(v, "_utype"):
      v = v._utype(v)
    try:
      t = YANGDynClass(v,base=RestrictedClassType(base_type=unicode,                                     restriction_type="dict_key",                                     restriction_arg={u'unknown': {'value': 2}, u'completed': {'value': 3}, u'other': {'value': 1}, u'inProgress': {'value': 4}, u'error': {'value': 5}},), is_leaf=True, yang_name="status", rest_name="status", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=False, namespace='urn:brocade.com:mgmt:brocade-ras-ext', defining_module='brocade-ras-ext', yang_type='enumeration', is_config=True)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """status must be of a type compatible with enumeration""",
          'defined-type': "brocade-ras-ext:enumeration",
          'generated-type': """YANGDynClass(base=RestrictedClassType(base_type=unicode,                                     restriction_type="dict_key",                                     restriction_arg={u'unknown': {'value': 2}, u'completed': {'value': 3}, u'other': {'value': 1}, u'inProgress': {'value': 4}, u'error': {'value': 5}},), is_leaf=True, yang_name="status", rest_name="status", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=False, namespace='urn:brocade.com:mgmt:brocade-ras-ext', defining_module='brocade-ras-ext', yang_type='enumeration', is_config=True)""",
        })

    self.__status = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_status(self):
    self.__status = YANGDynClass(base=RestrictedClassType(base_type=unicode,                                     restriction_type="dict_key",                                     restriction_arg={u'unknown': {'value': 2}, u'completed': {'value': 3}, u'other': {'value': 1}, u'inProgress': {'value': 4}, u'error': {'value': 5}},), is_leaf=True, yang_name="status", rest_name="status", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=False, namespace='urn:brocade.com:mgmt:brocade-ras-ext', defining_module='brocade-ras-ext', yang_type='enumeration', is_config=True)


  def _get_message(self):
    """
    Getter method for message, mapped from YANG variable /brocade_ras_ext_rpc/show_support_save_status/output/show_support_save_status/message (string)

    YANG Description: Textual description of status of recent support save is
as follows:
 unknown/other - Support Save is failed for
                 Unknown/undefined reason.  
 completed - The recent support save is completed successfully.
 in-progress - The support save is not yet completed.
               It may contain the value of % completed.
 error - Specify the error message.
    """
    return self.__message
      
  def _set_message(self, v, load=False):
    """
    Setter method for message, mapped from YANG variable /brocade_ras_ext_rpc/show_support_save_status/output/show_support_save_status/message (string)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_message is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_message() directly.

    YANG Description: Textual description of status of recent support save is
as follows:
 unknown/other - Support Save is failed for
                 Unknown/undefined reason.  
 completed - The recent support save is completed successfully.
 in-progress - The support save is not yet completed.
               It may contain the value of % completed.
 error - Specify the error message.
    """
    if hasattr(v, "_utype"):
      v = v._utype(v)
    try:
      t = YANGDynClass(v,base=unicode, is_leaf=True, yang_name="message", rest_name="message", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=False, namespace='urn:brocade.com:mgmt:brocade-ras-ext', defining_module='brocade-ras-ext', yang_type='string', is_config=True)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """message must be of a type compatible with string""",
          'defined-type': "string",
          'generated-type': """YANGDynClass(base=unicode, is_leaf=True, yang_name="message", rest_name="message", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=False, namespace='urn:brocade.com:mgmt:brocade-ras-ext', defining_module='brocade-ras-ext', yang_type='string', is_config=True)""",
        })

    self.__message = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_message(self):
    self.__message = YANGDynClass(base=unicode, is_leaf=True, yang_name="message", rest_name="message", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=False, namespace='urn:brocade.com:mgmt:brocade-ras-ext', defining_module='brocade-ras-ext', yang_type='string', is_config=True)


  def _get_percentage_of_completion(self):
    """
    Getter method for percentage_of_completion, mapped from YANG variable /brocade_ras_ext_rpc/show_support_save_status/output/show_support_save_status/percentage_of_completion (uint32)

    YANG Description: It specifies the value of % of completion.
    """
    return self.__percentage_of_completion
      
  def _set_percentage_of_completion(self, v, load=False):
    """
    Setter method for percentage_of_completion, mapped from YANG variable /brocade_ras_ext_rpc/show_support_save_status/output/show_support_save_status/percentage_of_completion (uint32)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_percentage_of_completion is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_percentage_of_completion() directly.

    YANG Description: It specifies the value of % of completion.
    """
    if hasattr(v, "_utype"):
      v = v._utype(v)
    try:
      t = YANGDynClass(v,base=RestrictedClassType(base_type=long, restriction_dict={'range': ['0..4294967295']}, int_size=32), is_leaf=True, yang_name="percentage-of-completion", rest_name="percentage-of-completion", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=False, namespace='urn:brocade.com:mgmt:brocade-ras-ext', defining_module='brocade-ras-ext', yang_type='uint32', is_config=True)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """percentage_of_completion must be of a type compatible with uint32""",
          'defined-type': "uint32",
          'generated-type': """YANGDynClass(base=RestrictedClassType(base_type=long, restriction_dict={'range': ['0..4294967295']}, int_size=32), is_leaf=True, yang_name="percentage-of-completion", rest_name="percentage-of-completion", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=False, namespace='urn:brocade.com:mgmt:brocade-ras-ext', defining_module='brocade-ras-ext', yang_type='uint32', is_config=True)""",
        })

    self.__percentage_of_completion = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_percentage_of_completion(self):
    self.__percentage_of_completion = YANGDynClass(base=RestrictedClassType(base_type=long, restriction_dict={'range': ['0..4294967295']}, int_size=32), is_leaf=True, yang_name="percentage-of-completion", rest_name="percentage-of-completion", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=False, namespace='urn:brocade.com:mgmt:brocade-ras-ext', defining_module='brocade-ras-ext', yang_type='uint32', is_config=True)

  rbridge_id = __builtin__.property(_get_rbridge_id, _set_rbridge_id)
  status = __builtin__.property(_get_status, _set_status)
  message = __builtin__.property(_get_message, _set_message)
  percentage_of_completion = __builtin__.property(_get_percentage_of_completion, _set_percentage_of_completion)


  _pyangbind_elements = {'rbridge_id': rbridge_id, 'status': status, 'message': message, 'percentage_of_completion': percentage_of_completion, }


