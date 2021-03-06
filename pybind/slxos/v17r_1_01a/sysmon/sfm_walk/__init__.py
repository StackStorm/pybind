
from operator import attrgetter
import pyangbind.lib.xpathhelper as xpathhelper
from pyangbind.lib.yangtypes import RestrictedPrecisionDecimalType, RestrictedClassType, TypedListType
from pyangbind.lib.yangtypes import YANGBool, YANGListType, YANGDynClass, ReferenceType
from pyangbind.lib.base import PybindBase
from decimal import Decimal
from bitarray import bitarray
import __builtin__
class sfm_walk(PybindBase):
  """
  This class was auto-generated by the PythonClass plugin for PYANG
  from YANG module brocade-sysmon - based on the path /sysmon/sfm-walk. Each member element of
  the container is represented as a class variable - with a specific
  YANG type.
  """
  __slots__ = ('_pybind_generated_by', '_path_helper', '_yang_name', '_rest_name', '_extmethods', '__sfm_walk_auto','__sfm_walk_dis_redundancy_check','__sfm_walk_interval','__sfm_walk_threshold',)

  _yang_name = 'sfm-walk'
  _rest_name = 'sfm-walk'

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
    self.__sfm_walk_interval = YANGDynClass(base=RestrictedClassType(base_type=RestrictedClassType(base_type=int, restriction_dict={'range': ['0..65535']},int_size=16), restriction_dict={'range': [u'1 .. 600']}), is_leaf=True, yang_name="sfm-walk-interval", rest_name="poll-interval", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'cli-full-command': None, u'code-name': u'sfm-walk-intvl', u'cli-full-no': None, u'info': u'Set SFM Walk poll-interval', u'alt-name': u'poll-interval'}}, namespace='urn:brocade.com:mgmt:brocade-sysmon', defining_module='brocade-sysmon', yang_type='uint16', is_config=True)
    self.__sfm_walk_dis_redundancy_check = YANGDynClass(base=YANGBool, is_leaf=True, yang_name="sfm-walk-dis-redundancy-check", rest_name="disable-redundancy-check", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'cli-full-command': None, u'code-name': u'sfm-walk-dis-red-chk', u'cli-full-no': None, u'info': u'Disable SFM Walk redundancy check (Default: Enabled)', u'alt-name': u'disable-redundancy-check'}}, namespace='urn:brocade.com:mgmt:brocade-sysmon', defining_module='brocade-sysmon', yang_type='empty', is_config=True)
    self.__sfm_walk_threshold = YANGDynClass(base=RestrictedClassType(base_type=RestrictedClassType(base_type=int, restriction_dict={'range': ['0..65535']},int_size=16), restriction_dict={'range': [u'1 .. 600']}), is_leaf=True, yang_name="sfm-walk-threshold", rest_name="threshold", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'cli-full-command': None, u'code-name': u'sfm-walk-th', u'cli-full-no': None, u'info': u'Set SFM Walk reassembly error threshold', u'alt-name': u'threshold'}}, namespace='urn:brocade.com:mgmt:brocade-sysmon', defining_module='brocade-sysmon', yang_type='uint16', is_config=True)
    self.__sfm_walk_auto = YANGDynClass(base=YANGBool, is_leaf=True, yang_name="sfm-walk-auto", rest_name="auto", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'cli-full-command': None, u'code-name': u'sfm-walk-auto', u'cli-full-no': None, u'info': u'Enable Auto SFM Walk (Default: Disabled)', u'alt-name': u'auto'}}, namespace='urn:brocade.com:mgmt:brocade-sysmon', defining_module='brocade-sysmon', yang_type='empty', is_config=True)

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
      return [u'sysmon', u'sfm-walk']

  def _rest_path(self):
    if hasattr(self, "_parent"):
      if self._rest_name:
        return self._parent._rest_path()+[self._rest_name]
      else:
        return self._parent._rest_path()
    else:
      return [u'sysmon', u'sfm-walk']

  def _get_sfm_walk_auto(self):
    """
    Getter method for sfm_walk_auto, mapped from YANG variable /sysmon/sfm_walk/sfm_walk_auto (empty)
    """
    return self.__sfm_walk_auto
      
  def _set_sfm_walk_auto(self, v, load=False):
    """
    Setter method for sfm_walk_auto, mapped from YANG variable /sysmon/sfm_walk/sfm_walk_auto (empty)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_sfm_walk_auto is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_sfm_walk_auto() directly.
    """
    if hasattr(v, "_utype"):
      v = v._utype(v)
    try:
      t = YANGDynClass(v,base=YANGBool, is_leaf=True, yang_name="sfm-walk-auto", rest_name="auto", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'cli-full-command': None, u'code-name': u'sfm-walk-auto', u'cli-full-no': None, u'info': u'Enable Auto SFM Walk (Default: Disabled)', u'alt-name': u'auto'}}, namespace='urn:brocade.com:mgmt:brocade-sysmon', defining_module='brocade-sysmon', yang_type='empty', is_config=True)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """sfm_walk_auto must be of a type compatible with empty""",
          'defined-type': "empty",
          'generated-type': """YANGDynClass(base=YANGBool, is_leaf=True, yang_name="sfm-walk-auto", rest_name="auto", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'cli-full-command': None, u'code-name': u'sfm-walk-auto', u'cli-full-no': None, u'info': u'Enable Auto SFM Walk (Default: Disabled)', u'alt-name': u'auto'}}, namespace='urn:brocade.com:mgmt:brocade-sysmon', defining_module='brocade-sysmon', yang_type='empty', is_config=True)""",
        })

    self.__sfm_walk_auto = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_sfm_walk_auto(self):
    self.__sfm_walk_auto = YANGDynClass(base=YANGBool, is_leaf=True, yang_name="sfm-walk-auto", rest_name="auto", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'cli-full-command': None, u'code-name': u'sfm-walk-auto', u'cli-full-no': None, u'info': u'Enable Auto SFM Walk (Default: Disabled)', u'alt-name': u'auto'}}, namespace='urn:brocade.com:mgmt:brocade-sysmon', defining_module='brocade-sysmon', yang_type='empty', is_config=True)


  def _get_sfm_walk_dis_redundancy_check(self):
    """
    Getter method for sfm_walk_dis_redundancy_check, mapped from YANG variable /sysmon/sfm_walk/sfm_walk_dis_redundancy_check (empty)
    """
    return self.__sfm_walk_dis_redundancy_check
      
  def _set_sfm_walk_dis_redundancy_check(self, v, load=False):
    """
    Setter method for sfm_walk_dis_redundancy_check, mapped from YANG variable /sysmon/sfm_walk/sfm_walk_dis_redundancy_check (empty)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_sfm_walk_dis_redundancy_check is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_sfm_walk_dis_redundancy_check() directly.
    """
    if hasattr(v, "_utype"):
      v = v._utype(v)
    try:
      t = YANGDynClass(v,base=YANGBool, is_leaf=True, yang_name="sfm-walk-dis-redundancy-check", rest_name="disable-redundancy-check", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'cli-full-command': None, u'code-name': u'sfm-walk-dis-red-chk', u'cli-full-no': None, u'info': u'Disable SFM Walk redundancy check (Default: Enabled)', u'alt-name': u'disable-redundancy-check'}}, namespace='urn:brocade.com:mgmt:brocade-sysmon', defining_module='brocade-sysmon', yang_type='empty', is_config=True)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """sfm_walk_dis_redundancy_check must be of a type compatible with empty""",
          'defined-type': "empty",
          'generated-type': """YANGDynClass(base=YANGBool, is_leaf=True, yang_name="sfm-walk-dis-redundancy-check", rest_name="disable-redundancy-check", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'cli-full-command': None, u'code-name': u'sfm-walk-dis-red-chk', u'cli-full-no': None, u'info': u'Disable SFM Walk redundancy check (Default: Enabled)', u'alt-name': u'disable-redundancy-check'}}, namespace='urn:brocade.com:mgmt:brocade-sysmon', defining_module='brocade-sysmon', yang_type='empty', is_config=True)""",
        })

    self.__sfm_walk_dis_redundancy_check = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_sfm_walk_dis_redundancy_check(self):
    self.__sfm_walk_dis_redundancy_check = YANGDynClass(base=YANGBool, is_leaf=True, yang_name="sfm-walk-dis-redundancy-check", rest_name="disable-redundancy-check", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'cli-full-command': None, u'code-name': u'sfm-walk-dis-red-chk', u'cli-full-no': None, u'info': u'Disable SFM Walk redundancy check (Default: Enabled)', u'alt-name': u'disable-redundancy-check'}}, namespace='urn:brocade.com:mgmt:brocade-sysmon', defining_module='brocade-sysmon', yang_type='empty', is_config=True)


  def _get_sfm_walk_interval(self):
    """
    Getter method for sfm_walk_interval, mapped from YANG variable /sysmon/sfm_walk/sfm_walk_interval (uint16)
    """
    return self.__sfm_walk_interval
      
  def _set_sfm_walk_interval(self, v, load=False):
    """
    Setter method for sfm_walk_interval, mapped from YANG variable /sysmon/sfm_walk/sfm_walk_interval (uint16)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_sfm_walk_interval is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_sfm_walk_interval() directly.
    """
    if hasattr(v, "_utype"):
      v = v._utype(v)
    try:
      t = YANGDynClass(v,base=RestrictedClassType(base_type=RestrictedClassType(base_type=int, restriction_dict={'range': ['0..65535']},int_size=16), restriction_dict={'range': [u'1 .. 600']}), is_leaf=True, yang_name="sfm-walk-interval", rest_name="poll-interval", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'cli-full-command': None, u'code-name': u'sfm-walk-intvl', u'cli-full-no': None, u'info': u'Set SFM Walk poll-interval', u'alt-name': u'poll-interval'}}, namespace='urn:brocade.com:mgmt:brocade-sysmon', defining_module='brocade-sysmon', yang_type='uint16', is_config=True)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """sfm_walk_interval must be of a type compatible with uint16""",
          'defined-type': "uint16",
          'generated-type': """YANGDynClass(base=RestrictedClassType(base_type=RestrictedClassType(base_type=int, restriction_dict={'range': ['0..65535']},int_size=16), restriction_dict={'range': [u'1 .. 600']}), is_leaf=True, yang_name="sfm-walk-interval", rest_name="poll-interval", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'cli-full-command': None, u'code-name': u'sfm-walk-intvl', u'cli-full-no': None, u'info': u'Set SFM Walk poll-interval', u'alt-name': u'poll-interval'}}, namespace='urn:brocade.com:mgmt:brocade-sysmon', defining_module='brocade-sysmon', yang_type='uint16', is_config=True)""",
        })

    self.__sfm_walk_interval = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_sfm_walk_interval(self):
    self.__sfm_walk_interval = YANGDynClass(base=RestrictedClassType(base_type=RestrictedClassType(base_type=int, restriction_dict={'range': ['0..65535']},int_size=16), restriction_dict={'range': [u'1 .. 600']}), is_leaf=True, yang_name="sfm-walk-interval", rest_name="poll-interval", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'cli-full-command': None, u'code-name': u'sfm-walk-intvl', u'cli-full-no': None, u'info': u'Set SFM Walk poll-interval', u'alt-name': u'poll-interval'}}, namespace='urn:brocade.com:mgmt:brocade-sysmon', defining_module='brocade-sysmon', yang_type='uint16', is_config=True)


  def _get_sfm_walk_threshold(self):
    """
    Getter method for sfm_walk_threshold, mapped from YANG variable /sysmon/sfm_walk/sfm_walk_threshold (uint16)
    """
    return self.__sfm_walk_threshold
      
  def _set_sfm_walk_threshold(self, v, load=False):
    """
    Setter method for sfm_walk_threshold, mapped from YANG variable /sysmon/sfm_walk/sfm_walk_threshold (uint16)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_sfm_walk_threshold is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_sfm_walk_threshold() directly.
    """
    if hasattr(v, "_utype"):
      v = v._utype(v)
    try:
      t = YANGDynClass(v,base=RestrictedClassType(base_type=RestrictedClassType(base_type=int, restriction_dict={'range': ['0..65535']},int_size=16), restriction_dict={'range': [u'1 .. 600']}), is_leaf=True, yang_name="sfm-walk-threshold", rest_name="threshold", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'cli-full-command': None, u'code-name': u'sfm-walk-th', u'cli-full-no': None, u'info': u'Set SFM Walk reassembly error threshold', u'alt-name': u'threshold'}}, namespace='urn:brocade.com:mgmt:brocade-sysmon', defining_module='brocade-sysmon', yang_type='uint16', is_config=True)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """sfm_walk_threshold must be of a type compatible with uint16""",
          'defined-type': "uint16",
          'generated-type': """YANGDynClass(base=RestrictedClassType(base_type=RestrictedClassType(base_type=int, restriction_dict={'range': ['0..65535']},int_size=16), restriction_dict={'range': [u'1 .. 600']}), is_leaf=True, yang_name="sfm-walk-threshold", rest_name="threshold", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'cli-full-command': None, u'code-name': u'sfm-walk-th', u'cli-full-no': None, u'info': u'Set SFM Walk reassembly error threshold', u'alt-name': u'threshold'}}, namespace='urn:brocade.com:mgmt:brocade-sysmon', defining_module='brocade-sysmon', yang_type='uint16', is_config=True)""",
        })

    self.__sfm_walk_threshold = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_sfm_walk_threshold(self):
    self.__sfm_walk_threshold = YANGDynClass(base=RestrictedClassType(base_type=RestrictedClassType(base_type=int, restriction_dict={'range': ['0..65535']},int_size=16), restriction_dict={'range': [u'1 .. 600']}), is_leaf=True, yang_name="sfm-walk-threshold", rest_name="threshold", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'cli-full-command': None, u'code-name': u'sfm-walk-th', u'cli-full-no': None, u'info': u'Set SFM Walk reassembly error threshold', u'alt-name': u'threshold'}}, namespace='urn:brocade.com:mgmt:brocade-sysmon', defining_module='brocade-sysmon', yang_type='uint16', is_config=True)

  sfm_walk_auto = __builtin__.property(_get_sfm_walk_auto, _set_sfm_walk_auto)
  sfm_walk_dis_redundancy_check = __builtin__.property(_get_sfm_walk_dis_redundancy_check, _set_sfm_walk_dis_redundancy_check)
  sfm_walk_interval = __builtin__.property(_get_sfm_walk_interval, _set_sfm_walk_interval)
  sfm_walk_threshold = __builtin__.property(_get_sfm_walk_threshold, _set_sfm_walk_threshold)


  _pyangbind_elements = {'sfm_walk_auto': sfm_walk_auto, 'sfm_walk_dis_redundancy_check': sfm_walk_dis_redundancy_check, 'sfm_walk_interval': sfm_walk_interval, 'sfm_walk_threshold': sfm_walk_threshold, }


